"""Assemble bounded reviewed paper or locale-label edits; no ImageGen calls."""
import copy
import sys
from prepare_next_locales import ROOT, LANE, load, put, ref, sha, module, PERSONA

batch = sys.argv[1]
assert batch in ['B14', 'B15']
locale = 'zh-Hans' if batch == 'B14' else 'zh-Hant'
base = LANE + '/' + batch + '-' + locale + '-f1-v1'
record_path = base + '/corrective-native-review.json'
actual = load(record_path)
assert actual['verdict'] == 'SCRIPT_REVIEW_PASS' and actual['anchor_verdict'] == 'MESSAGE_ANCHOR_PASS'
assert actual['scope'] in ['BLANK_PAPER_ONLY', 'LOCALE_LABEL_ONLY'] and actual['independence'] == 'SELF_REVIEW'
label_edit = actual['scope'] == 'LOCALE_LABEL_ONLY'
tag = 'locale-label' if label_edit else 'blank-paper'
if label_edit:
    assert batch == 'B15' and len(actual['cards']) == 1
    edit = ' TARGETED EDIT OF FIRST REFERENCE IMAGE: change ONLY the small category label beside the official Digiwin logo from 晶片设计案例 to the exact approved Traditional Chinese literal 晶片設計案例. Replace 设计 with 設計 in that category and nothing else. Preserve every other existing approved glyph, headline, body, full publisher/source, exact proper legal name 上海晶丰明源半导体股份有限公司, counter 2/4, official logo, layout, font sizes, colors, photographic props and uniformly blank paper. Do not convert the legal company name or any other wording. No new marks, paper rules, extra words or other changes.'
    anchor_observation = ' Actual locale-label corrective reviewed: replacing the two mistaken Simplified glyphs 设计 with approved Traditional 設計 restores exact category 晶片設計案例. All other approved wording, story, source, persona and locale remain unchanged. The exact Simplified source legal name is intentionally preserved; this limited proper-name exception does not apply to the category. No new claim or customer evidence.'
else:
    edit = ' TARGETED EDIT OF FIRST REFERENCE IMAGE: preserve all existing approved Chinese wording, source, CTA, category, counter, official logo, layout, typography and photographic props. Change ONLY paper surfaces: erase every pale rule, bar, line and form pattern on every sheet including foreground, left folio and clipped stack; make all paper uniformly blank white with natural shadows. Do not erase approved artwork text or decorative header counter line. No new marks or other changes.'
    anchor_observation = ' Actual blank-paper corrective reviewed: all wording, story, source, persona and locale unchanged; removing unlabelled lines adds no customer evidence or product promise.'
assert 0 < len(actual['cards']) <= 2
ledger = load(base + '/attempt-ledger.json')['attempts']
assert not any(x['kind'] == 'corrective' for x in ledger)
plan = load(base + '/dispatch-plan.json')
core = module('scripts/verify_imagegen_preflight.py')
guard = module('scripts/verify_imagegen_anchor_preflight.py')
calls = []
for reviewed in actual['cards']:
    cid = reviewed['card_id']
    assert reviewed['finding'] == ('MIXED_SCRIPT_CATEGORY' if label_edit else 'UNLABELLED_PAPER_RULES') and reviewed['review'] == 'PASS'
    if label_edit:
        assert cid == 'RMK-BRIGHT-2'
    original = next(x for x in ledger if x['card_id'] == cid)
    assert original['sha256'] == reviewed['original_sha256'] == sha(original['path'])
    old = next(x for x in plan['calls'] if x['card_id'] == cid)['folder']
    folder = base + '/corrective-v1/' + cid.lower()
    assert not (ROOT / folder / 'native').exists()
    contract = copy.deepcopy(load(old + '/contract.json'))
    contract['revision'] = batch.lower() + '-' + cid.lower() + '-' + tag + '-contract-v1'
    contract['output']['directory'] = folder + '/native'
    contract['references'][0] = dict(**ref(original['path'], original['call_id'] + '-actual-edit-target'), role='campaign_visual', attributes=['colors', 'lighting', 'shadows', 'material_depth', 'typography_hierarchy', 'campaign_identity', 'scene_diagram_integration'])
    contract['sources'].append(ref(record_path))
    for k in contract['card_sources']:
        contract['card_sources'][k].append(record_path)
    contract['style']['campaign']['instructions'] += edit
    put(folder + '/contract.json', contract)
    cr = ref(folder + '/contract.json')
    review = copy.deepcopy(load(old + '/review.json'))
    review['revision'] = batch.lower() + '-' + cid.lower() + '-' + tag + '-source-review-v1'
    review['subjects'] = dict(contract=cr, copy=contract['copy'], sources=contract['sources'])
    put(folder + '/review.json', review)
    release = copy.deepcopy(load(old + '/release.json'))
    release.update(revision=batch.lower() + '-' + cid.lower() + '-' + tag + '-release-v1', contract=cr, review=ref(folder + '/review.json'))
    put(folder + '/release.json', release)
    call = copy.deepcopy(load(old + '/spec.json')['calls'][0])
    call.update(call_id=batch + '_' + cid.replace('-', '_') + '_C1', references=contract['references'], output_id=cid.lower() + '-' + locale + '-c1', output_path=contract['output']['directory'] + '/' + cid.lower() + '-' + locale + '-c1.png')
    call['prompt'] = core.make_prompt(contract, call)
    import hashlib
    call['prompt_sha256'] = hashlib.sha256(call['prompt'].encode()).hexdigest()
    spec = copy.deepcopy(load(old + '/spec.json'))
    spec.update(revision=batch.lower() + '-' + cid.lower() + '-' + tag + '-spec-v1', release=ref(folder + '/release.json'), contract=cr, review=release['review'], calls=[call])
    put(folder + '/spec.json', spec)
    script = copy.deepcopy(load(old + '/script-review.json'))
    script['revision'] = batch.lower() + '-' + cid.lower() + '-' + tag + '-script-v1'
    script['corrective_review'] = ref(record_path)
    script['corrective_observation'] = reviewed['observation']
    put(folder + '/script-review.json', script)
    anchor = copy.deepcopy(load(old + '/anchor-review.json'))
    anchor['revision'] = batch.lower() + '-' + cid.lower() + '-' + tag + '-anchor-v1'
    anchor['subjects'] = dict(contract=cr, copy=contract['copy'], spec=ref(folder + '/spec.json'), script_review=ref(folder + '/script-review.json'))
    anchor['context']['related_inputs'].append(ref(record_path))
    anchor['context']['observation'] += anchor_observation
    put(folder + '/anchor-review.json', anchor)
    result = guard.check(ROOT, folder + '/release.json', sha(folder + '/release.json'), folder + '/spec.json', folder + '/anchor-review.json', sha(folder + '/anchor-review.json'), call['call_id'], 'FDI', PERSONA, plan['route'])
    put(folder + '/preparation-preflight.json', result)
    calls.append(dict(folder=folder, card_id=cid, call_id=call['call_id'], output_path=call['output_path'], release_sha256=sha(folder + '/release.json'), review_sha256=sha(folder + '/anchor-review.json')))
put(base + '/corrective-dispatch-plan.json', dict(revision=batch.lower() + '-' + tag + '-corrective-dispatch-v1', persona=PERSONA, route=plan['route'], locale=locale, calls=calls, corrective_cap=2, per_card_corrective_cap=1, fresh_preflight_required_before_each_call=True))
print(batch + ': ' + str(len(calls)) + ' actual-reviewed ' + tag + ' edits prepared; fresh wrapper required before inference.')
