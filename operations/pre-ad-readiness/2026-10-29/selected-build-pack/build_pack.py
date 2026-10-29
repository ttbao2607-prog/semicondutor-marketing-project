"""Derive the selected internal tables; never modifies creative or legacy library."""
import csv
import hashlib
import json
import struct
import subprocess
from pathlib import Path
from urllib.parse import urlencode

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]
HOST = 'https://solutions.digiwin.com.vn/semiconductor-case-reader'
REF = 'slice/linkedin-contingency-audience'
FIT_PATH = 'operations/contingency-audience/revisions/r5-true-only/result/FULL_ROW_REVIEW.json'


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write_json(name, data):
    (OUT / name).write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


def write_csv(name, rows):
    with (OUT / name).open('w', newline='', encoding='utf-8-sig') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)


def main():
    old = json.loads((ROOT / 'operations/pre-ad-readiness/2026-10-28/journey-shortlist/SOURCE_BINDING.json').read_text(encoding='utf-8-sig'))
    selected = old['selected'][:2]
    assert [x['treatment'] for x in selected] == ['P1', 'P2']
    pins = {}
    ads, cards = [], []
    for s in selected:
        for pin in s['pins']:
            assert sha((ROOT / pin['path']).read_bytes()) == pin['sha256'], pin['path']
        copy_path = s['directory'] + '/selected-copy.json'
        source = json.loads((ROOT / copy_path).read_text(encoding='utf-8-sig'))
        assert source['revision'] == s['revision']
        pins[copy_path] = sha((ROOT / copy_path).read_bytes())
        for stage in source['stages']:
            sid = stage['id']
            role = {'cold': 'COLD', 'explanation': 'EXPL', 'proof': 'PROOF'}[sid]
            lane = 'cold' if sid == 'cold' else 'rmk'
            t = s['treatment']
            ad_name = f'LI-wave01-{t}-en-{role}-v1'
            batch = 'b22' if t == 'P1' else 'b25'
            campaign = f'fdi_{t.lower()}_en_{lane}_wave01'
            def url(content):
                return HOST + '?' + urlencode(dict(t=t, lang='en', utm_source='linkedin', utm_medium='paid_social', utm_campaign=campaign, utm_content=content, creative_version=source['revision']))
            ad_url = url(f'{batch}_{role.lower()}_v1')
            ads.append(dict(ad_name=ad_name, treatment=t, locale='en', role=role,
                            readiness='INTERNAL_DRAFT_NOT_RELEASED',
                            phase='WEEK1_COLD_CANDIDATE' if lane == 'cold' else 'DEFER_UNTIL_RMK_READY',
                            format='Single image' if lane == 'cold' else 'Carousel',
                            objective='Brand awareness' if lane == 'cold' else 'UNDECIDED_RMK_R4',
                            intro_text=stage['caption'], intro_chars=len(stage['caption']),
                            platform_cta='Learn more', destination_url=ad_url,
                            card_count=len(stage['cards']), copy_revision=source['revision'],
                            source_copy=copy_path, actual_ad_id='', actual_adset_id=''))
            for i, c in enumerate(stage['cards'], 1):
                image = (Path(s['directory']) / c['image']).as_posix()
                raw = (ROOT / image).read_bytes()
                assert raw[:8] == b'\x89PNG\r\n\x1a\n'
                width, height = struct.unpack('>II', raw[16:24])
                pins[image] = sha(raw)
                cards.append(dict(ad_name=ad_name, treatment=t, role=role, position=i,
                                  card_id=c['card_id'], native_headline=c['native_headline'],
                                  native_headline_chars=len(c['native_headline']),
                                  artwork_headline=c['headline'], body=c.get('body', ''),
                                  source_text=c.get('source_text', ''),
                                  artwork_cta=c.get('cta', ''), alt=c.get('alt', ''),
                                  image_path=image, image_sha256=sha(raw), width=width,
                                  height=height, bytes=len(raw),
                                  destination_url=ad_url if lane == 'cold' else url(f'{batch}_{role.lower()}_{c["card_id"].lower().replace("-", "_")}_v1')))
    for p in [old['anchor']['path'], old['email']['path'], old['partner_anchor']['path'],
              'deliverables/unified-case-reader/unified-case-reader.html',
              'tracking/semiconductor-reader-bridge.js']:
        pins[p] = sha((ROOT / p).read_bytes())
    assert pins[old['anchor']['path']] == old['anchor']['sha256']
    assert pins[old['email']['path']] == old['email']['sha256']
    fit_raw = subprocess.check_output(['git', 'show', REF + ':' + FIT_PATH], cwd=ROOT)
    fit = json.loads(fit_raw)
    retained = [r for r in fit['rows'] if r['final_membership'] == 'KEEP_SUPPORTED']
    from collections import Counter
    write_json('FIT_RECONCILIATION.json', dict(
        source_ref=subprocess.check_output(['git', 'rev-parse', REF], cwd=ROOT).decode().strip(),
        source_path=FIT_PATH, source_sha256=sha(fit_raw),
        evidence_date='2026-10-06/07 historical research, reread 2026-10-29; not fresh live validation',
        retained_rows=len(retained), page_scope=dict(Counter(r['page_scope'] for r in retained)),
        decision_unit_status=dict(Counter(r['decision_unit_status'] for r in retained)),
        conclusion='Mixed semiconductor/electronics scope includes chip design and equipment/process components; does not establish equipment-component fit for all R5 recipients. All 52 have unverified purchasing authority. No targeting change or raw roster copied.'))
    write_csv('BUILD_ADS.csv', ads)
    write_csv('BUILD_CARDS.csv', cards)
    write_json('SOURCE_BINDING.json', dict(stage='INTERNAL_CONTENT_REVIEW',
        branch='slice/executive-approval-corrected-2026-10-28', source_checkpoint='9d9f061b950daf763e3211dd5a1793c0250eac31',
        anchor=old['anchor'], email=old['email'], partner_anchor=old['partner_anchor'],
        persona={'P1': 'Equipment-component supplier Operations; planning handoff', 'P2': 'Equipment-component supplier factory IT with Operations; record ownership'},
        locale='en', pins=[dict(path=p, sha256=h) for p,h in sorted(pins.items())],
        actual_platform_ids='Unassigned; blank CSV fields are deliberate, never upload as identifiers',
        names='wave01 is proposed concrete local wave label, not a saved platform object',
        rights='Existing approval retained; exact selected-set paid release not established'))
    assert len(ads) == 6 and len(cards) == 20
    assert len(set(c['image_sha256'] for c in cards)) == 16
    lines = ['# Selected ad fields — internal draft', '', 'Exact copy retained; no new wording or creative. Two cold candidates; four deferred RMK ads. Native platform CTA: Learn more, availability still needs saved native UI readback.', '']
    for a in ads:
        lines += ['## ' + a['ad_name'], '', f"Phase: {a['phase']} · {a['format']} · {a['copy_revision']}", '', a['intro_text'], '', f"Intro characters: {a['intro_chars']}. Existing text above 150 may truncate in feed; not a 150-character hard-limit failure. No automatic rewrite.", '', a['destination_url'], '', '| Position | Card | Native headline | Original asset |', '|---|---|---|---|']
        for c in [c for c in cards if c['ad_name'] == a['ad_name']]:
            lines += [f"| {c['position']} | {c['card_id']} | {c['native_headline']} | [{Path(c['image_path']).name}](../../../../{c['image_path']}) |"]
        lines += ['']
    (OUT / 'AD_FIELDS.md').write_text('\n'.join(lines), encoding='utf-8')
    print(json.dumps(dict(ads=len(ads), slots=len(cards), unique_images=16, source_pins=len(pins), source_integrity='PASS'), ensure_ascii=False))


if __name__ == '__main__':
    main()
