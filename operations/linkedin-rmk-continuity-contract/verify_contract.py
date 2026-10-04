"""Bounded v1 contract verifier. Does not validate a produced ad, page or live route."""
import argparse
import copy
import hashlib
import json
import subprocess
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

PACK = Path(__file__).resolve().parent
ROOT = PACK.parent.parent
BASE = 'd163ce7e8040c763cd649c11cd14de3ee48bc204'
RELEASE = 'rmk-continuity-v1'
IDS = ['O1', 'O2', 'O3', 'O4-Q', 'O4-O', 'F1', 'F2', 'F3', 'P1', 'P2', 'P3']
R4 = 'operations/linkedin-rmk-proof/quality-pilot-harness-r4'
SOURCE_URL = 'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/'
NAMES = ['contract.json', 'case-content.json', 'continuity-matrix.json', 'input-manifest.json', 'worktree-registry.json', 'execution-contract.json']

def read(path):
    return json.loads(Path(path).read_text(encoding='utf-8-sig'))

def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()

def git(root, *args):
    return subprocess.check_output(['git', '-C', str(root), *args], text=True, stderr=subprocess.STDOUT).strip()

def safe_path(root, relative):
    result = (root / relative).resolve()
    if Path(relative).is_absolute() or not result.is_relative_to(root.resolve()):
        raise ValueError('path escapes repository: ' + relative)
    return result

def load():
    return {name: read(PACK / name) for name in NAMES}

def validate(data, check_files=False):
    errors = []
    def check(condition, reason):
        if not condition:
            errors.append(reason)
    c = data['contract.json']
    content = data['case-content.json']
    matrix = data['continuity-matrix.json']
    inputs = data['input-manifest.json']
    registry = data['worktree-registry.json']
    execution = data['execution-contract.json']
    for obj in [c, content, matrix]:
        check(obj['release_id'] == RELEASE, 'release ID mismatch')
    for obj in [c, matrix, inputs, registry]:
        check(obj['baseline_commit'] == BASE, 'baseline mismatch')
    check(c['expected_cold_treatments'] == IDS, 'declared Cold treatment set mismatch')
    check(c['authority']['corrective_rounds_authorized'] == 0 and execution['corrective_rounds_authorized'] == 0, 'Corrective 1 must not be authorized')
    check(not c['authority']['push'] and not c['authority']['live_operation'] and not c['authority']['production_workers_started'], 'setup authority exceeded')
    check(c['primary_destination'] == 'mobile_multilingual_ldp_adapter' and c['pdf_status'] == 'NOT_SELECTED_OPTIONAL_DERIVATIVE', 'LDP/PDF direction mismatch')
    check(c['routing']['public_base_url'] is None and c['routing']['public_route_status'] == 'NOT_CONFIGURED', 'fabricated configured public route')
    check(c['routing']['required_controls'] == ['entry', 'case', 'contract', 'lang'], 'missing route control')
    check(c['routing']['unknown_or_conflicting_identity'] == 'EXPLICIT_UNAVAILABLE_NO_CASE_SUBSTITUTION', 'unknown/conflicting identity substitution')
    check(c['routing']['duplicate_controls'] == 'REJECT', 'duplicate identity controls not rejected')
    check(c['routing']['missing_or_invalid_lang'] == 'EXPLICIT_VI_FALLBACK_WITH_VISIBLE_LANGUAGE_LABEL', 'language fallback mislabeling')
    check(set(c['routing']['preserve_on_toggle']) == {'entry', 'case', 'contract', 'section', 'utm_parameters'}, 'toggle continuity fields incomplete')
    check(c['change_control']['new_release_required'] and c['change_control']['forbid_silent_latest'] and c['change_control']['preserve_previous_releases'], 'release drift control missing')
    check(c['consumer_binding_required_fields'] == ['entry_ids', 'release_id', 'release_manifest_sha256', 'content_revision', 'claim_ids', 'locale', 'promise_fields', 'logical_destination', 'artifact_hashes', 'branch', 'commit'], 'consumer identity binding incomplete')
    check(set(c['pair_receipt_required_fields']) == {'release_manifest_sha256', 'rmk_binding_sha256', 'ldp_binding_sha256', 'artifact_hashes', 'tested_urls', 'locales', 'viewports', 'semantic_observations', 'click_toggle_source_observations', 'auditor_verdict', 'candidate_commits'}, 'pair acceptance evidence incomplete')
    check(c['ownership']['rmk']['write_prefix'] == 'operations/linkedin-rmk-fulfillment/' and c['ownership']['ldp']['write_prefix'] == 'operations/linkedin-rmk-mobile-adapter/', 'consumer write boundaries not disjoint/exact')
    check(c['content_owner'] == 'coordinator_shared_content_owner', 'shared content ownership drift')
    check(len(content['cases']) == 1, 'v1 includes an unselected case')
    case = content['cases'][0]
    check(case['case_id'] == 'case06' and case['entity_native'] == '江苏中科智芯集成科技有限公司', 'case entity mismatch')
    check(case['market'] == 'China' and case['industry_context'] == 'packaging_and_testing', 'case context/market mismatch')
    check(case['solution_scope'] == 'integrated_digital_solution', 'ERP-only or expanded solution scope')
    check(case['numeric_invariants'] == {'metric': 'month_close_duration', 'baseline': 15, 'result': 5, 'unit': 'days'}, 'case numeric meaning mismatch')
    check(case['claim_ids'] == ['PR10-role', 'PR05-case', 'PR05-month-close'], 'unsupported claim added')
    check(case['claim_source_bindings'] == {'PR10-role': {'proof_id': 'PR10', 'r4_card_ids': ['RMK-R4-1']}, 'PR05-case': {'proof_id': 'PR05', 'r4_card_ids': ['RMK-R4-2']}, 'PR05-month-close': {'proof_id': 'PR05', 'r4_card_ids': ['RMK-R4-3']}}, 'claim/source/card binding mismatch')
    check(case['original_source']['url'] == SOURCE_URL and case['original_source']['locator'] == 'case06; 江苏中科智芯集成科技有限公司', 'original source locator mismatch')
    check(not case['original_source']['direct_anchor_verified'], 'unobserved direct source anchor claimed')
    check(c['locales']['enabled_payloads'] == ['vi'] and c['locales']['planned'] == ['vi', 'en', 'zh-Hans', 'zh-Hant'], 'unready locale enabled or planned locales changed')
    source_copy = read(ROOT / R4 / 'copy-vi.json')['ads'][0]
    check(case['locales']['vi']['cards'] == source_copy['cards'] and case['locales']['vi']['caption'] == source_copy['caption'], 'shared VI factual public copy differs from frozen R4')
    check(case['locales']['vi']['status'] == 'READY_SOURCE_PAYLOAD', 'VI source payload promoted to page acceptance')
    for lang in ['en', 'zh-Hans', 'zh-Hant']:
        check(case['locales'][lang]['status'] == 'TRANSLATION_PENDING' and case['locales'][lang]['payload'] is None, 'unreviewed translation masquerades as ready: ' + lang)
    rows = matrix['rows']
    check([r['cold_treatment_id'] for r in rows] == IDS, 'missing/duplicated/reordered Cold rows')
    pin_records = inputs['pins']
    pin_map = {p['path']: p for p in pin_records}
    check(len(pin_map) == len(pin_records), 'duplicate source pins')
    check(len([p for p in pin_records if p['role'] == 'selected_cold_public_artifact']) == 77, 'selected Cold reader/asset inventory not 77 files')
    expected_entries = ['RMK-R4-O1', 'RMK-R4-O4-Q']
    check([e['entry_id'] for e in c['entries']] == expected_entries, 'unselected/missing entry')
    entry_map = {e['entry_id']: e for e in c['entries']}
    for row in rows:
        tid = row['cold_treatment_id']
        check(bool(row['persona'] and row['pain'] and row['remaining_reader_question'] and row['rationale'] and row['hold']), 'missing continuity reasoning: ' + tid)
        cp = row['cold']['copy_path']
        ap = row['cold']['acceptance_path']
        check(cp in pin_map and ap in pin_map, 'cold copy/acceptance unpinned: ' + tid)
        if cp in pin_map:
            check(row['cold']['copy_sha256'] == pin_map[cp]['sha256'], 'cold row hash differs from manifest: ' + tid)
        selected = tid in ['O1', 'O4-Q']
        check(row['pair_acceptance'] is None, 'unproduced pair given acceptance: ' + tid)
        check(row['delivery_gate'] == 'ACCOUNT_AUDIENCE_OBJECTIVE_TRACKING_BUDGET_AND_LIVE_UNVERIFIED', 'offline match promoted to live audience readiness')
        if selected:
            check(row['selection_status'] == 'EXISTING_SCOPED_R4_CONTENT' and row['pair_state'] == 'DESTINATION_PENDING', 'existing R4 status altered')
            check(row['match_class'] == 'adjacent_operations', 'Quality adjacent evidence relabeled direct outcome')
            rmk = row['rmk']
            check(rmk['ad_id'] == 'RMK-R4' and rmk['public_copy_path'] == R4 + '/copy-vi.json', 'selected ad identity mismatch')
            check(rmk['case_id'] == 'case06' and rmk['entry_id'] == 'RMK-R4-' + tid, 'selected case/entry mismatch')
            check(rmk['claim_ids'] == case['claim_ids'] and rmk['closing_card_id'] == 'RMK-R4-4', 'selected claim/closing card mismatch')
            check(rmk['closing_promise'] == source_copy['cards'][-1]['body'] and rmk['cta'] == source_copy['cards'][-1]['cta'], 'closing promise/CTA differs from frozen R4')
            e = entry_map.get(rmk['entry_id'])
            check(e is not None, 'selected row has no route')
            if e:
                check(e['case_id'] == rmk['case_id'] and e['claim_ids'] == rmk['claim_ids'] and e['cold_treatment_id'] == tid and e['ad_id'] == rmk['ad_id'], 'route and row identity/claims differ')
                check(e['configured_live_url'] is None and e['state'] == 'DESTINATION_PENDING', 'pending route promoted')
                u = urlsplit(e['logical_destination'])
                q = parse_qs(u.query, keep_blank_values=True)
                check(not u.scheme and not u.netloc and u.path == c['routing']['logical_path'], 'logical destination is fabricated live URL/wrong path')
                check(q == {'entry': [e['entry_id']], 'case': ['case06'], 'contract': [RELEASE], 'lang': ['vi']}, 'logical destination identity/version/locale mismatch')
                check(u.fragment == e['section'] == 'case-summary' and e['initial_locale'] == 'vi', 'route section/initial locale mismatch')
        else:
            check(row['selection_status'] == row['pair_state'] == 'PROOF_SELECTION_PENDING', 'unselected proof promoted: ' + tid)
            rmk = row['rmk']
            check(all(rmk[key] is None for key in ['ad_id', 'public_copy_path', 'case_id', 'entry_id', 'closing_card_id', 'closing_promise', 'cta']) and rmk['claim_ids'] == [], 'unselected row silently routed: ' + tid)
        if check_files and cp in pin_map and ap in pin_map:
            ad = read(safe_path(ROOT, cp))['ads'][0]
            audit = read(safe_path(ROOT, ap))
            check(row['cold']['ad_id'] == ad['ad_id'] and row['cold']['caption'] == ad['caption'] and row['cold']['opening_headline'] == ad['cards'][0]['headline'] and row['cold']['opening_body'] == ad['cards'][0]['body'] and row['cold']['closing_cta'] == ad['cards'][-1]['cta'], 'cold extract differs from actual public copy: ' + tid)
            check(row['cold']['acceptance_status'] == audit['status'] and audit['status'].startswith('AUDIT_PASSED'), 'cold receipt acceptance unsupported: ' + tid)
            for public_name, expected_hash in audit['public_files'].items():
                path = ap.rsplit('/operator/', 1)[0] + '/public/' + public_name
                check(path in pin_map and pin_map[path]['sha256'] == expected_hash, 'selected public artifact/receipt discrepancy: ' + path)
    check([a['id'] for a in execution['acceptance_criteria']] == ['AC' + str(i) for i in range(1, 9)], 'AC coverage incomplete')
    check(execution['audit_dispatch'] == {'model': 'gpt-6.1-sol', 'reasoning_effort': 'low', 'fork_turns': 'none', 'children': 1, 'write_permission': False, 'runtime_admission_and_acceptance_required': True}, 'auditor authorization/topology drift')
    check(registry['production_state'] == 'NOT_STARTED' and [w['lane'] for w in registry['worktrees']] == ['rmk', 'ldp'], 'setup registry claims production/missing lane')
    for w in registry['worktrees']:
        check(all(w[k] == c['ownership'][w['lane']][k] for k in ['path', 'branch', 'write_prefix']) and w['shared_pack_access'] == 'read_only', 'worktree ownership identity mismatch')
    if check_files:
        for p in pin_records:
            path = safe_path(ROOT, p['path'])
            check(path.is_file(), 'missing pinned input: ' + p['path'])
            if path.is_file():
                check(digest(path) == p['sha256'] and path.stat().st_size == p['bytes'], 'working pinned input changed: ' + p['path'])
                blob = git(ROOT, 'rev-parse', BASE + ':' + p['path'])
                check(blob == p['git_blob'], 'baseline blob identity changed: ' + p['path'])
        freeze = read(ROOT / R4 / 'operator/bao-freeze-receipt.json')
        for p in freeze['pins']:
            check(p['path'] in pin_map and pin_map[p['path']]['sha256'] == p['sha256'], 'freeze receipt and input binding mismatch')
        release = read(PACK / 'release-manifest.json')
        check(release['release_id'] == RELEASE, 'manifest release mismatch')
        actual_pack_files = {p.name for p in PACK.iterdir() if p.is_file() and p.name != 'release-manifest.json'}
        declared_pack_files = {p['path'] for p in release['files']}
        check(actual_pack_files == declared_pack_files and len(release['files']) == len(declared_pack_files), 'release manifest coverage incomplete')
        for p in release['files']:
            path = safe_path(PACK, p['path'])
            check(path.is_file() and digest(path) == p['sha256'], 'shared pack release hash changed: ' + p['path'])
    return errors

def probes(data):
    cases = []
    def probe(name, mutate):
        candidate = copy.deepcopy(data)
        mutate(candidate)
        result = validate(candidate)
        cases.append({'probe': name, 'rejected': bool(result), 'errors': result})
    probe('wrong_case_entity', lambda d: d['case-content.json']['cases'][0].update(entity_native='another customer'))
    probe('wrong_metric_or_market', lambda d: d['case-content.json']['cases'][0]['numeric_invariants'].update(result=2))
    probe('wrong_closing_promise', lambda d: d['continuity-matrix.json']['rows'][0]['rmk'].update(closing_promise='ERP xử lý kiểm thử bất thường'))
    probe('wrong_expand_route_case', lambda d: d['contract.json']['entries'][0].update(logical_destination='/rmk-case/?entry=RMK-R4-O1&case=case04&contract=rmk-continuity-v1&lang=vi#case-summary'))
    probe('silent_latest_release', lambda d: d['contract.json']['entries'][0].update(logical_destination='/rmk-case/?entry=RMK-R4-O1&case=case06&contract=latest&lang=vi#case-summary'))
    probe('unreviewed_locale_enabled', lambda d: d['contract.json']['locales']['enabled_payloads'].append('en'))
    probe('force_case06_into_fabless', lambda d: d['continuity-matrix.json']['rows'][5]['rmk'].update(case_id='case06'))
    probe('fake_pair_acceptance', lambda d: d['continuity-matrix.json']['rows'][0].update(pair_state='PAIR_ACCEPTED_OFFLINE', pair_acceptance={'verdict': 'PASS'}))
    probe('missing_cold_treatment', lambda d: d['continuity-matrix.json']['rows'].pop())
    probe('overlapping_consumer_ownership', lambda d: d['contract.json']['ownership']['ldp'].update(write_prefix='operations/linkedin-rmk-fulfillment/'))
    return cases

def verify_worktrees(data):
    errors = []
    observations = []
    canonical_head = git(ROOT, 'rev-parse', 'HEAD')
    manifest = read(PACK / 'release-manifest.json')
    shared_names = [p['path'] for p in manifest['files']] + ['release-manifest.json']
    for w in data['worktree-registry.json']['worktrees']:
        path = Path(w['path'])
        if not path.is_dir():
            errors.append('worktree missing: ' + str(path))
            continue
        branch = git(path, 'branch', '--show-current')
        head = git(path, 'rev-parse', 'HEAD')
        status = git(path, 'status', '--porcelain=v1')
        if branch != w['branch'] or head != canonical_head or status:
            errors.append('setup worktree branch/checkpoint/cleanliness mismatch: ' + w['lane'])
        consumer_pack = path / PACK.relative_to(ROOT)
        for name in shared_names:
            target = consumer_pack / name
            if not target.is_file() or digest(target) != digest(PACK / name):
                errors.append('consumer shared pack mismatch: ' + w['lane'] + '/' + name)
        observations.append({'lane': w['lane'], 'path': w['path'], 'branch': branch, 'head': head, 'clean': not bool(status), 'release_manifest_sha256': digest(consumer_pack / 'release-manifest.json') if (consumer_pack / 'release-manifest.json').is_file() else None})
    return errors, observations

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--probes', action='store_true')
    parser.add_argument('--worktrees', action='store_true')
    parser.add_argument('--output')
    args = parser.parse_args()
    try:
        data = load()
        errors = validate(data, check_files=True)
        probe_results = probes(data) if args.probes else []
        errors.extend('negative probe failed: ' + p['probe'] for p in probe_results if not p['rejected'])
        worktrees = []
        if args.worktrees:
            wt_errors, worktrees = verify_worktrees(data)
            errors.extend(wt_errors)
        result = {'status': 'FAIL' if errors else 'PASS_BOUNDED_CONTRACT_CHECKS', 'candidate_head': git(ROOT, 'rev-parse', 'HEAD'), 'baseline': BASE, 'release_id': RELEASE, 'input_pins': len(data['input-manifest.json']['pins']), 'cold_rows': len(data['continuity-matrix.json']['rows']), 'bound_entries': len(data['contract.json']['entries']), 'errors': errors, 'probes': probe_results, 'worktrees': worktrees, 'limits': 'No RMK/LDP production, source semantic revalidation, translation review, browser navigation/render, public route or live acceptance is established.'}
    except (KeyError, ValueError, OSError, subprocess.CalledProcessError) as exc:
        result = {'status': 'FAIL', 'errors': [str(exc)], 'limits': 'Malformed/missing evidence fails closed.'}
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        Path(args.output).write_text(text + '\n', encoding='utf-8')
    print(text)
    return 1 if result['status'] == 'FAIL' else 0

if __name__ == '__main__':
    raise SystemExit(main())
