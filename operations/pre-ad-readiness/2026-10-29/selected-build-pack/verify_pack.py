"""Check resulting review tables directly against original copy and assets."""
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

OUT = Path(__file__).resolve().parent
ROOT = OUT.parents[3]


def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main():
    binding = json.loads((OUT / 'SOURCE_BINDING.json').read_text(encoding='utf-8'))
    for pin in binding['pins']:
        assert digest(ROOT / pin['path']) == pin['sha256'], pin['path']
    with (OUT / 'BUILD_ADS.csv').open(encoding='utf-8-sig', newline='') as f:
        ads = list(csv.DictReader(f))
    with (OUT / 'BUILD_CARDS.csv').open(encoding='utf-8-sig', newline='') as f:
        cards = list(csv.DictReader(f))
    assert len(ads) == 6 and len(cards) == 20
    assert len({a['ad_name'] for a in ads}) == 6
    assert len({c['image_sha256'] for c in cards}) == 16
    assert sum(a['phase'] == 'WEEK1_COLD_CANDIDATE' for a in ads) == 2
    for a in ads:
        source = json.loads((ROOT / a['source_copy']).read_text(encoding='utf-8-sig'))
        stage = next(s for s in source['stages'] if s['id'] == {'COLD': 'cold', 'EXPL': 'explanation', 'PROOF': 'proof'}[a['role']])
        assert a['intro_text'] == stage['caption']
        assert int(a['intro_chars']) == len(a['intro_text'])
        assert len(a['intro_text']) <= (3000 if a['role'] == 'COLD' else 255)
        assert a['actual_ad_id'] == a['actual_adset_id'] == ''
        assert a['platform_cta'] == 'Learn more'
        group = [c for c in cards if c['ad_name'] == a['ad_name']]
        assert len(group) == int(a['card_count']) == len(stage['cards'])
        for i, (row, original) in enumerate(zip(group, stage['cards']), 1):
            assert int(row['position']) == i
            for field in ['card_id', 'native_headline', 'body', 'source_text', 'alt']:
                assert row[field] == original.get(field, ''), (row['card_id'], field)
            assert row['artwork_headline'] == original['headline']
            assert row['artwork_cta'] == original.get('cta', '')
            assert int(row['native_headline_chars']) == len(row['native_headline'])
            assert len(row['native_headline']) <= (200 if a['role'] == 'COLD' else 45)
            expected = (Path(a['source_copy']).parent / original['image']).as_posix()
            assert row['image_path'] == expected
            assert digest(ROOT / expected) == row['image_sha256']
            assert int(row['bytes']) <= (5_000_000 if a['role'] == 'COLD' else 10_000_000)
            assert int(row['width']) == int(row['height']) == 1254
    urls = [a['destination_url'] for a in ads] + [c['destination_url'] for c in cards]
    for row in ads + cards:
        u = urlsplit(row['destination_url']); q = parse_qs(u.query)
        assert u.scheme == 'https' and u.netloc == 'solutions.digiwin.com.vn'
        assert u.path == '/semiconductor-case-reader'
        assert q['t'] == [row['treatment']] and q['lang'] == ['en']
        assert q['utm_source'] == ['linkedin'] and q['utm_medium'] == ['paid_social']
        lane = 'cold' if row['role'] == 'COLD' else 'rmk'
        assert '_' + lane + '_' in q['utm_campaign'][0]
        assert len(row['destination_url']) < 2000
        assert '<' not in row['destination_url'] and 'UNKNOWN' not in row['destination_url']
        assert 'bridge_ad_id' not in q and 'bridge_adset_id' not in q
    carousel_urls = [c['destination_url'] for c in cards if c['role'] != 'COLD']
    assert len(set(carousel_urls)) == 18
    link_count = 0
    for p in OUT.glob('*.md'):
        for target in re.findall(r'\]\(([^)]+)\)', p.read_text(encoding='utf-8')):
            if target.startswith(('http:', 'https:')):
                continue
            resolved = (p.parent / target.split('#')[0].split('?')[0]).resolve()
            if resolved != (OUT / 'CHECKS.json').resolve():
                assert resolved.exists(), (p.name, target)
            link_count += 1
    changed = subprocess.check_output(['git', 'diff', '--name-only'], cwd=ROOT).decode().splitlines()
    assert not any(p.startswith(('deliverables/', 'tracking/')) for p in changed)
    diffcheck = subprocess.run(['git', '-c', 'core.whitespace=cr-at-eol', 'diff', '--check'], cwd=ROOT, capture_output=True, text=True)
    assert diffcheck.returncode == 0, diffcheck.stdout
    outputs = [p for p in OUT.iterdir() if p.is_file() and p.name != 'CHECKS.json']
    result = dict(status='PASS_INTERNAL_PACK', execution='SUCCESS',
        paid_readiness='INSUFFICIENT_EVIDENCE_LAUNCH_HOLD', independent_audit='NOT_RUN_ROOT_SELF_REVIEW',
        ads=6, card_slots=20, unique_images=16, unchanged_source_pins=len(binding['pins']),
        local_links_checked=link_count, source_copy_and_order='EXACT', destination_and_utm='PASS_OFFLINE',
        native_ui='NOT_RUN', live_mutations=0, git_actions_during_verifier='READ_ONLY; local checkpoint authorized separately, no push/merge',
        protected_creative_reader_tracking_diff='NONE', whitespace_diff='PASS',
        outputs=[dict(path=p.name, sha256=digest(p)) for p in sorted(outputs)])
    (OUT / 'CHECKS.json').write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    assert (OUT / 'CHECKS.json').exists()
    print(json.dumps({k:v for k,v in result.items() if k != 'outputs'}))


if __name__ == '__main__':
    main()
