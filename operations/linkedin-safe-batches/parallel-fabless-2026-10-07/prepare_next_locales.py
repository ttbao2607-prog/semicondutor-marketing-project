"""Bounded B14/B15 source authoring and release assembly; never calls ImageGen.

Semantic verdicts must be supplied by the root's actual recorded review.
Shared core/adapter/canonical files remain read-only.
"""
import copy
import hashlib
import importlib.util
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
LANE = Path(__file__).resolve().parent.relative_to(ROOT).as_posix()
V1 = LANE + '/B13-en-f1-v1'
V5 = LANE + '/B13-en-f1-v5'
ART5 = 'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5'
PERSONA = 'Operations / SCM Manager influencing business-system decisions at an eligible commercial Fabless FDI entity with outsourced production'
ENTITY = '上海晶丰明源半导体股份有限公司'
LOGO = 'operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03/common/references/digiwin-logo.webp'
CLOSING = 'operations/linkedin-imagegen-dogfood/closing-standard-harness-2026-10-03/references/po-accepted-closing-b.png'


def load(p):
    return json.loads((ROOT / p).read_text(encoding='utf-8-sig'))


def sha(p):
    return hashlib.sha256((ROOT / p).read_bytes()).hexdigest()


def put(p, v):
    q = ROOT / p
    q.parent.mkdir(parents=True, exist_ok=True)
    q.write_text(json.dumps(v, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def ref(p, revision=None):
    if revision is None:
        revision = load(p)['revision']
    return dict(path=p, sha256=sha(p), revision=revision)


def module(p):
    s = importlib.util.spec_from_file_location(Path(p).stem, ROOT / p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def author(batch):
    locale = 'zh-Hans' if batch == 'B14' else 'zh-Hant'
    base = LANE + '/' + batch + '-' + locale + '-f1-v1'
    assert not (ROOT / base / 'draft-manifest.json').exists()
    authored = load(LANE + '/next-locales-authored-input.json')['locales'][locale]
    oldcards = load(ART5 + '/selected-copy.json')['cards']
    oldprompts = {x['card_id']: x for x in load(ART5 + '/selected-prompts.json')['calls']}
    specs = {}
    for p in (ROOT / LANE).rglob('spec.json'):
        for c in json.loads(p.read_text(encoding='utf-8-sig')).get('calls', []):
            specs[c['call_id']] = c
    concepts = {x['card_id']: copy.deepcopy(specs[oldprompts[x['card_id']]['call_id']]['concepts'][0]) for x in oldcards}
    profiles = load('operations/linkedin-locale-adapter/profiles.json')['locales'][locale]
    frozen = load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']
    assert len(frozen) == 24 and all(sha(x['path']) == x['sha256'] for x in frozen)
    mandate = dict(revision=batch.lower() + '-po-two-batch-mandate-v1',
                   instruction='Chạy 2 batch kế tiếp trong worktee fabless, giữ anchor như batch v5.',
                   explicit_cap_reply='Giữ đủ 11 card, cho phép 11 lượt tạo gốc mỗi batch (đề xuất)',
                   scope='B14 F1 zh-Hans then B15 F1 zh-Hant; 1cold+6explanation+4proof each; preserve B13v5 message and Vietnam team nuance.',
                   original_cap=11, corrective_cap=2, per_card_corrective_cap=1,
                   cap_exception='Explicit PO reply replaces 10original only for B14/B15; frozen gates unchanged.',
                   stop='After B15 or per-card corrective/cap/material blocker. Do not start B16.',
                   git_scope='No new commit/merge/push instruction in this generation turn; previous B13 commit remains unchanged.',
                   review='New actual locale script/anchor review required; B13 technical pending state is not inherited as PASS.')
    put(base + '/generation-mandate.json', mandate)
    route = 'offline ' + locale + ' cold -> F1 outsourced-lot reporting -> Vietnam ERP consulting/implementation discussion -> qualitative China Bright Power integrated-solution case -> ' + locale + ' case reader'
    (ROOT / base / 'execution-brief.md').write_text(
        '# ' + batch + ' F1 ' + locale + ' execution brief\n\n'
        + 'Owner: /root, owned Fabless worktree on slice/linkedin-safe-fabless-parallel; source checkpoint e3b65780356cdf5f489ea3a45ac4927af616cd81.\n\n'
        + 'Persona: ' + PERSONA + '. Actual entity fit/system-buying authority remains unverified. Existing process/system fixes are alternatives to ERP purchase.\n\n'
        + 'Route: ' + route + '. Same B13v5 business value: a shared basis for the next outsourced-production decision and accountable updates; no invented ROI or automatic synchronization.\n\n'
        + '11 newly localized units under explicit PO cap exception; canary F1-A6 and RMK-BRIGHT-3, then remaining cards; at most2corrective and1percard. Calls sequential. Fresh callable guard before every inference. No generation from draft payloads.\n\n'
        + 'Vietnam team presence supports prospective ERP consulting/implementation discussion only. The China Bright case remains separate qualitative integrated-solution context; no Vietnam Fabless deployment, case metrics or ERP-only causality.\n\n'
        + 'Scope: own batch artifacts, reader, local receipts/ledger/docs-impact only. Frozen24/core/adapter/shared canon read-only. Browser uses atomic shared lock, own tab/server and cleanup. Root SELF_REVIEW; no independent/native-market certification. Inspect actual native/feed/main/mobile and reader when available; gaps remain INSUFFICIENT_EVIDENCE. No main/push/live/B16.\n', encoding='utf-8')
    proof = copy.deepcopy(load(V1 + '/proof-source-mapping.json'))
    proof['revision'] = batch.lower() + '-proof-map-v1'
    proof['observed_date'] = '2026-10-07'
    proof['retrieval'] = 'Fresh read-only official web open confirms case04 at lines239-249; no numbers imported.'
    proof['locale'] = locale
    proof['legal_name_rule'] = 'Exact source legal entity remains Simplified Chinese in both scripts; this is proper-name preservation, disclosed in Traditional reader.'
    put(base + '/proof-source-mapping.json', proof)
    vn = copy.deepcopy(load(V5 + '/vietnam-team-source.json'))
    vn['revision'] = batch.lower() + '-vietnam-team-source-v1'
    vn['fresh_reverification'] = 'Official Huakun Vietnam publication reopened2026-10-07; local ERP consulting/implementation team context confirmed at162-167. No customer numbers/testimonial or all-team language claim reused.'
    put(base + '/vietnam-team-source.json', vn)
    put(base + '/reader-script.json', dict(revision=batch.lower() + '-reader-' + locale + '-v1', entity=ENTITY,
                                        source_url=proof['source_url'], **authored['reader']))
    pins = [ref(base + '/generation-mandate.json'), ref(base + '/reader-script.json'),
            ref(base + '/proof-source-mapping.json'), ref(base + '/vietnam-team-source.json')]
    observations = []
    templates = {'cold': V1 + '/cold/release-v2/campaign/contract.json',
                 'explanation': V5 + '/release/f1-a6/contract.json',
                 'proof': V1 + '/proof/release-v2/closing/contract.json'}
    for stage in ['cold', 'explanation', 'proof']:
        oldstage = [x for x in oldcards if x['stage'] == stage]
        rows = []
        stageconcepts = {}
        for old in oldstage:
            oldid = old['card_id']
            cid = 'COLD-FABLESS-' + batch if stage == 'cold' else oldid
            a = authored['cards'][oldid]
            labels = authored['labels'][stage][:]
            if stage != 'cold':
                labels.append(old['artwork_labels'][-1])
            row = dict(card_id=cid, headline=a['headline'], body=a['body'], source_text=a.get('source_text', ''),
                       cta=a.get('cta', ''), native_headline=a['headline'], alt=authored['alt_prefix'] + a['headline'], artwork_labels=labels)
            rows.append(row)
            concept = concepts[oldid]
            concept.update(card_id=cid, concept_id=batch.lower() + '-' + cid.lower() + '-scene-v1', reader_question=a['headline'], artwork_labels=labels)
            concept['description'] += ' New locale ' + locale + ': only supplied localized artwork text may be printed; do not inherit English reference labels. All data surfaces blank; no chart, tick, records, values, customer facility or geographic decoration. The original source name remains exact.'
            stageconcepts[cid] = concept
            observations.append(dict(stage=stage, card_id=cid, reviewed_fields=['caption'] + list(module('scripts/verify_imagegen_preflight.py').CARD_FIELDS),
                                     exact_fields=row, caption=authored['captions'][stage], scene=concept['description'],
                                     observation=a['rationale'], source_scope='China qualitative case scope, separate from Vietnam service' if stage == 'proof' else 'Bounded operating questions/local consultation; no product-mechanism or result assertion',
                                     reference_artwork=ART5 + '/' + old['image'], original_card_id=oldid))
        ad = batch + '-COLD' if stage == 'cold' else 'F1-A' if stage == 'explanation' else 'RMK-BRIGHT'
        p = base + '/' + stage + '/public-copy.json'
        put(p, dict(schema_version=1, revision=batch.lower() + '-' + stage + '-' + locale + '-copy-v1', ads=[dict(ad_id=ad, caption=authored['captions'][stage], cards=rows)]))
        c = load(templates[stage])
        c.update(revision=batch.lower() + '-' + stage + '-contract-draft-v1', locale=locale, copy=ref(p), ad_order=[ad],
                 card_order={ad: [x['card_id'] for x in rows]}, groups=[[x['card_id']] for x in rows], definitions=profiles['definitions'])
        c['surfaces'] = {ad: [dict(surface_id='full-feed', reading_order=['caption'] + [x['card_id'] + '.' + f for x in rows for f in module('scripts/verify_imagegen_preflight.py').CARD_FIELDS])]}
        c['limits']['caption'] = 255
        c['sources'] = [ref(base + '/execution-brief.md', batch.lower() + '-brief-v1'), ref(base + '/proof-source-mapping.json'),
                        ref(base + '/vietnam-team-source.json'), ref(LANE + '/next-locales-authored-input.json'),
                        ref(ART5 + '/selected-copy.json'), ref('operations/linkedin-locale-adapter/profiles.json')]
        c['card_sources'] = {x['card_id']: [s['path'] for s in c['sources']] for x in rows}
        c['style']['campaign']['instructions'] = (
            'Use case: ads-marketing. ' + profiles['prompt_guidance'] + ' ' + profiles['typography']
            + ' New artwork in the B13v5 visual family: bright white/pale blue, grounded daylight, navy/blue type, material depth. No English/Vietnamese reference wording. Supplied Latin Digiwin, ERP, MES, domain and exact legal company name are intentional proper literals. Official supplied logo once; no additional DIGIWIN header label.'
            + ' Category and sequence are separate from source, exact near logo. Headline dominant and body comfortably readable at333CSSpx. Every source is a full-width normal main paragraph on WHITE, at least body-sized, high contrast, with complete legal name on its own readable line. Reserve bottom35percent for source/CTA when long; shrink scene before type. No source icon column, tiny footer/divider, skyline/pagoda/map/customer facility/seal/badge, unapproved punctuation, chart/tick/data glyphs or technical UI. All paper surfaces blank. No copy of English labels, reference wording or exact composition. Narrative/props stay within the reviewed concept.'
            + (' Cold single image: exact category and ERP role line; no sequence/swipe/CTA.' if stage == 'cold' else ' Exact counter and category required; CTA only if supplied.'))
        if stage != 'proof':
            c['style'].pop('closing', None)
        else:
            c['style']['closing']['cards'] = ['RMK-BRIGHT-4']
        c['output']['directory'] = base + '/' + stage + '/native'
        put(base + '/' + stage + '/contract.draft.json', c)
        put(base + '/' + stage + '/concepts.draft.json', dict(revision=batch.lower() + '-' + stage + '-concepts-v1', concepts=stageconcepts))
        pins += [ref(p), ref(base + '/' + stage + '/contract.draft.json'), ref(base + '/' + stage + '/concepts.draft.json')]
    put(base + '/draft-observations.json', dict(revision=batch.lower() + '-actual-author-observations-v1', cards=observations))
    pins.append(ref(base + '/draft-observations.json'))
    put(base + '/draft-manifest.json', dict(revision=batch.lower() + '-draft-manifest-v1', locale=locale, persona=PERSONA, route=route,
                                          files=pins, frozen_files_verified=24, selected_intent=11, postgen='POSTGEN_NOT_RUN'))
    for helper in ['fresh_preflight.py', 'record_attempt.py', 'prepare_draft.py']:
        shutil.copyfile(ROOT / V5 / helper, ROOT / base / helper)
    print(batch + ': authored11locale units and reader; no release/PASS/generation automatically created.')


def release(batch):
    locale = 'zh-Hans' if batch == 'B14' else 'zh-Hant'
    base = LANE + '/' + batch + '-' + locale + '-f1-v1'
    assert not (ROOT / base / 'dispatch-plan.json').exists()
    core = module('scripts/verify_imagegen_preflight.py')
    guard = module('scripts/verify_imagegen_anchor_preflight.py')
    semantic = load(base + '/semantic-review.json')
    draft = load(base + '/draft-manifest.json')
    assert semantic['verdict'] == 'SCRIPT_REVIEW_PASS' and semantic['anchor_verdict'] == 'MESSAGE_ANCHOR_PASS'
    assert semantic['draft_manifest_sha256'] == sha(base + '/draft-manifest.json')
    assert all(sha(x['path']) == x['sha256'] for x in draft['files'])
    observations = load(base + '/draft-observations.json')['cards']
    plans = []
    for o in observations:
        stage = o['stage']; cid = o['card_id']; folder = base + '/release/' + cid.lower()
        c = copy.deepcopy(load(base + '/' + stage + '/contract.draft.json'))
        target = load(c['copy']['path']); ids = [x['card_id'] for a in target['ads'] for x in a['cards']]
        c['revision'] = batch.lower() + '-' + cid.lower() + '-contract-v1'
        c['output']['directory'] = folder + '/native'
        c['references'] = [dict(**ref(o['reference_artwork'], o.get('reference_revision', 'b13-v5-selected-visual-family-reference')), role='campaign_visual',
                                attributes=['colors', 'lighting', 'shadows', 'material_depth', 'typography_hierarchy', 'campaign_identity', 'scene_diagram_integration']),
                           dict(**ref(LOGO, 'official-logo-pinned'), role='brand_asset', attributes=['brand_mark'])]
        if cid == 'RMK-BRIGHT-4':
            c['references'].append(dict(**ref(CLOSING, 'po-closing-standard-2026-10-03-v1'), role='closing_layout',
                                        attributes=['cta_separation', 'layout_hierarchy', 'source_body_hierarchy', 'source_full_width']))
        else:
            c['style'].pop('closing', None)
        c['sources'].append(ref(base + '/semantic-review.json'))
        for k in c['card_sources']:
            c['card_sources'][k].append(base + '/semantic-review.json')
        put(folder + '/contract.json', c); cr = ref(folder + '/contract.json'); pr = c['copy']
        fields = {a['ad_id']: ['caption'] + [x['card_id'] + '.' + f for x in a['cards'] for f in core.CARD_FIELDS] for a in target['ads']}
        reviewed = [x for x in observations if x['stage'] == stage]
        assert [x['card_id'] for x in reviewed] == ids
        review = dict(schema_version=1, revision=batch.lower() + '-' + cid.lower() + '-source-review-v1', writer='/root', reviewer='/root',
                      date='2026-10-07', scope='OFFLINE_SOURCE_COPY', independence='SELF_REVIEW', subjects=dict(contract=cr, copy=pr, sources=c['sources']),
                      verdicts=dict(source_copy='PASS', editorial='PASS', first_mention='PASS'), reviewed_ads=c['ad_order'],
                      reviewed_fields=[a + '/' + f for a, fs in fields.items() for f in fs], unresolved_findings=[])
        put(folder + '/review.json', review)
        release = dict(schema_version=1, revision=batch.lower() + '-' + cid.lower() + '-release-v1', authorizer='/root recording explicit PO B14/B15 mandate',
                       authority_ref=ref(base + '/generation-mandate.json'), purpose='OFFLINE_IMAGEGEN', contract=cr, copy=pr,
                       review=ref(folder + '/review.json'), groups=[[cid]])
        put(folder + '/release.json', release)
        concept = load(base + '/' + stage + '/concepts.draft.json')['concepts'][cid]
        row = next(x for a in target['ads'] for x in a['cards'] if x['card_id'] == cid)
        call = dict(call_id=batch + '_' + cid.replace('-', '_') + '_V1', targets=[cid], references=c['references'], concepts=[concept],
                    artwork_text={cid: {f: row[f] for f in ['headline', 'body', 'source_text', 'cta', 'artwork_labels']}},
                    output_id=cid.lower() + '-' + locale + '-v1', output_path=c['output']['directory'] + '/' + cid.lower() + '-' + locale + '-v1.png')
        call['prompt'] = core.make_prompt(c, call)
        call['prompt_sha256'] = hashlib.sha256(call['prompt'].encode()).hexdigest()
        spec = dict(schema_version=1, revision=batch.lower() + '-' + cid.lower() + '-spec-v1', release=ref(folder + '/release.json'),
                    contract=cr, copy=pr, review=release['review'], calls=[call])
        put(folder + '/spec.json', spec)
        script = dict(revision=batch.lower() + '-' + cid.lower() + '-script-v1', gate_id='AD-ED-01', stage='PREGEN_SCRIPT', verdict='SCRIPT_REVIEW_PASS',
                      copy_sha256=pr['sha256'], reviewed_ads=c['ad_order'], reviewed_fields=fields,
                      BRAND_ROLE=dict(verdict='PASS', observation=semantic['brand_role']), ADVERTISER_VOICE=dict(verdict='PASS', observation=semantic['advertiser_voice']),
                      independence='SELF_REVIEW', per_card_observations=reviewed, reader_script=ref(base + '/reader-script.json'),
                      actual_review_ref=ref(base + '/semantic-review.json'), postgen='POSTGEN_NOT_RUN')
        put(folder + '/script-review.json', script)
        anchor = dict(schema_version=1, revision=batch.lower() + '-' + cid.lower() + '-anchor-v1', gate_id='MSG-ANCHOR-01', stage='PREGEN_SCRIPT', verdict='MESSAGE_ANCHOR_PASS',
                      anchor=ref('operations/Vy_Email_Content_Anchor.md', '1.0'), source=ref('operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md', 'VY-MAIL-USER-20261006'),
                      subjects=dict(contract=cr, copy=pr, spec=ref(folder + '/spec.json'), script_review=ref(folder + '/script-review.json')),
                      scope=dict(segment='FDI', locale=locale, persona=PERSONA, route=draft['route']), writer='/root', reviewer='/root', independence='SELF_REVIEW',
                      coverage=dict(ads=c['ad_order'], cards=ids, fields=fields, storyboard_cards=ids),
                      rules={k: dict(verdict='N/A' if k == 'A5' else 'MATCH', observation=semantic[k]) for k in ['A1','A2','A3','A4','A5','A6','A7']},
                      units=[dict(card_id=x['card_id'], verdict='MATCH', observation=x['observation'] + ' Exact text: ' + json.dumps(x['exact_fields'], ensure_ascii=False) + ' Scene: ' + x['scene']) for x in reviewed],
                      transitions=[dict(cards=[x['card_id'], y['card_id']], verdict='MATCH', observation=x['headline'] + ' -> ' + y['headline'] + '; ' + semantic['A7']) for a in target['ads'] for x,y in zip(a['cards'],a['cards'][1:])],
                      context=dict(scope='FULL_JOURNEY', verdict='MATCH', observation=semantic['A7'] + ' Reader: ' + semantic['reader'],
                                   brief=ref(base + '/execution-brief.md', batch.lower() + '-brief-v1'),
                                   related_inputs=[ref(base + '/' + other + '/public-copy.json') for other in ['cold','explanation','proof'] if other != stage]
                                   + [ref(base + '/reader-script.json'), ref(base + '/semantic-review.json'), ref(base + '/proof-source-mapping.json'), ref(base + '/vietnam-team-source.json')]),
                      unresolved_findings=[])
        put(folder + '/anchor-review.json', anchor)
        checked = guard.check(ROOT, folder + '/release.json', sha(folder + '/release.json'), folder + '/spec.json', folder + '/anchor-review.json',
                              sha(folder + '/anchor-review.json'), call['call_id'], 'FDI', PERSONA, draft['route'])
        put(folder + '/preparation-preflight.json', checked)
        plans.append(dict(folder=folder, call_id=call['call_id'], card_id=cid, output_path=call['output_path'],
                          release_sha256=sha(folder + '/release.json'), review_sha256=sha(folder + '/anchor-review.json')))
    canary = ['F1-A6', 'RMK-BRIGHT-3']
    order = [x['card_id'] for x in observations]
    plans.sort(key=lambda p: (0,canary.index(p['card_id'])) if p['card_id'] in canary else (1,order.index(p['card_id'])))
    put(base + '/dispatch-plan.json', dict(revision=batch.lower() + '-dispatch-v1', persona=PERSONA, route=draft['route'], locale=locale,
                                         original_cap=11, corrective_cap=2, per_card_corrective_cap=1, calls=plans,
                                         fresh_preflight_required_before_each_call=True, trust='Root actual coordinator/reviewer SELF_REVIEW; no independent/native-market certification'))
    print(batch + ': 11 prepared releases; fresh wrapper still mandatory before every actual call.')


if __name__ == '__main__':
    assert sys.argv[1] in ['author', 'release'] and sys.argv[2] in ['B14', 'B15']
    (author if sys.argv[1] == 'author' else release)(sys.argv[2])
