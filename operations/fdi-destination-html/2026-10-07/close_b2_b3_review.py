"""Pin observed B2/B3 destination review and synchronize owned status."""
import csv
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
REVIEW = PACKET / 'B2-B3-review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
intake = json.loads((PACKET / 'B2-B3-intake.json').read_text(encoding='utf-8'))
copy = json.loads((PACKET / 'B1-copy-v2.json').read_text(encoding='utf-8'))
runtime = json.loads((REVIEW / 'render-runtime.json').read_text(encoding='utf-8'))
functional = json.loads((REVIEW / 'functional-runtime.json').read_text(encoding='utf-8'))
assert len(runtime) == 24 and len(functional) == 18
assert all(not r['overflow'] and r['photo'] and r['textParity'] and r['attrParity'] for r in runtime)
groups = [
    ('hero', ['title', 'caseLabel', 'market', 'lead'], 'A1/A2/A3', 'Packaging/testing Quality and Operations review of lot/test context; no nationality stereotype or domestic supply-chain promise.'),
    ('photograph', ['figure', 'figureSource', 'figureAlt'], 'A3/A7', 'Exact named customer; September2020 historical visit, Sohu byline. Photo is not evidence of current factory conditions or ERP results.'),
    ('context', ['contextTitle', 'contextBody'], 'A1/A2/A6', 'China customer and integrated ERP+iMES remain attributed; records/process/efficiency are published problems, not new outcomes.'),
    ('mechanisms', ['mechanismTitle', 'mechanismLead', 'm0Title', 'm0Body', 'm1Title', 'm1Body', 'm2Title', 'm2Body', 'm3Title', 'm3Body'], 'A6', 'SPC collection/analysis, ECN parameter distribution, linked records and automatic exception records/escalation preserve integrated solution scope. No ERP-alone or test-equipment substitute claim.'),
    ('lot/context value', ['valueTitle', 'valueLead', 'v1Title', 'v1Body', 'v1Prepare'], 'A3/A4', 'Qualitative common basis for Quality/Operations; asks about lot/test time/context and one current example. No numeric ROI or guaranteed result.'),
    ('handoff value', ['v2Title', 'v2Body', 'v2Prepare'], 'A3/A4/A6', 'Source confirmation, missing records and responsible next owner are specific review questions, not measured customer outcomes.'),
    ('change value', ['v3Title', 'v3Body', 'v3Prepare', 'bridge'], 'A4/A6/A7', 'Applicable revision/exception follow-up connects case mechanisms to the reader workflow; conditional benefit without fabricated savings.'),
    ('consultation', ['consultLabel', 'consultTitle', 'consultBody', 'next', 'cta'], 'A2/A7', 'Bring one review workflow; Digiwin manufacturing-solution provider role explicit. Existing external Vietnamese request page and language disclosed; HTML has no form or analytics dispatch.'),
    ('source and return', ['sourceLabel', 'sourceLink', 'sourceHint', 'sourceLang', 'back'], 'A7', 'Chinese collection exact case06 selection instructions; no claim external pages translate with toggle. Local index returns to original journey, even after language switch.'),
]
receipt = {
    'revision': 'B2-B3-four-language-authentic-photo-v1', 'date': '2026-10-07',
    'stage': 'POSTGEN_ARTIFACT', 'format': 'HTML built without ImageGen',
    'reviewer': 'root', 'independence': 'SELF_REVIEW',
    'scope': 'Two destination HTMLs and adjacent closing-card textual continuity only; not whole-journey certification',
    'message_anchor': {'id': 'VY-CONTENT-ANCHOR', 'revision': '1.0', 'sha256': sha(ROOT / 'operations/Vy_Email_Content_Anchor.md'),
        'email_record': 'VY-MAIL-USER-20261006', 'original_email_sha256': sha(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md')},
    'html_anchor': {'id': 'FDI-DESTINATION-HTML-ANCHOR', 'revision': '1.0', 'sha256': sha(PACKET / 'Destination_HTML_Anchor.md')},
    'persona': 'O1 Quality + Operations / FDI manufacturing decision unit; Vietnamese toggle translates same FDI persona',
    'audience': 'Content hypothesis only; live targeting/eligibility not reviewed',
    'A5': 'N/A: FDI operations value, not VN domestic entry-readiness promise',
    'locale_review': 'All four current copies inspected with actual desktop/mobile renders; Hans production/record terms and Hant 製程/紀錄/品質 remain separate. Registered legal entity remains original Simplified name. No independent native-market reviewer claimed.',
    'unit_review': [{'locale': locale, 'unit': unit, 'rules': rules, 'observed': {key: pack[key] for key in keys}, 'judgment': judgment, 'verdict': 'MATCH'} for locale, pack in copy.items() for unit, keys, rules, judgment in groups],
    'transitions': ['Closing card record association/parameter changes/exceptions -> hero lot/test review -> attributed integrated case: same O1 problem and entity.', 'Case context -> mechanisms: published capability, not unsupported standalone ERP result.', 'Mechanisms -> three review questions: qualitative business value and current workflow questions, no invented measurement.', 'Review questions -> consultation: actual workflow and responsibility discussion; external Vietnamese language disclosed.', 'Attribution -> return: original local journey retained; new toggle language does not change return route.'],
    'proof': {'entity': '江苏中科智芯集成科技有限公司', 'geography': 'China', 'solution': 'integrated ERP + iMES', 'metric': 'No numeric outcome/ROI claim', 'claim_source': 'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/', 'photo': 'Digiwin-branded visit September2020, Sohu byline 鼎捷智造___new', 'public_paid_rights': 'UNKNOWN; internal draft only'},
    'targets': intake['targets'],
    'evidence': {p.name: sha(p) for p in sorted(REVIEW.iterdir()) if p.suffix in ('.png', '.json')},
    'render': '16 full-page states visually inspected:2routes x4locales x1280desktop/390mobile. All24DOM checks including320smoke pass loaded photo, original ratio, overflow, text/alt/title/aria parity. Intermittent screenshot timeouts resolved by fresh Chrome tab; final16 captures available.',
    'interaction': '18 observed tests: absent/invalid default per route,4toggles/focus/URL/alt, refresh persistence, actual return click and actual entry link per route. No-JS initial locale inspected in static HTML, not browser JS-disabled runtime. External source/contact clicks not repeated for unchanged B1 links.',
    'MSG-ANCHOR-01': 'MESSAGE_ANCHOR_PASS', 'content_status': 'SCOPED_SELF_REVIEW_COMPLETE_PO_PENDING',
    'historical_findings': 'B2 proof1-2/B3 proof1 small source and whole-journey INSUFFICIENT_EVIDENCE retained; new reader review does not close those artwork/whole-journey findings.',
    'pending': ['PO review of new destination revision', 'Independent/native-market review', 'Public/paid image rights', 'Live runtime/deployment'],
    'git': 'Working files only on dedicated local slice; no commit/main integration/push',
    'docs_impact': 'Reviewed DOCS_IMPACT_MAP, current/README/build/readiness, email+HTML anchors and source register. Updated scoped status and inventory; source rights unchanged, no additional source-register update required. Strategy/budget/tracking/form contracts and frozen core unchanged.'
}
for t in intake['targets']:
    d = ROOT / t['directory']
    assert sha(d / 'case-reader.html') == t['reader_after_sha256']
    assert sha(d / 'index.html') == t['entry_after_sha256']
    assert sha(d / 'selected-copy.json') == t['selected_copy_sha256']
    assert sha(d / 'manifest.json') == t['manifest_sha256']
assert sha(ROOT / 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html') == intake['base_reader_sha256']
(REVIEW / 'review-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(REVIEW / 'README.md').write_text('''# B2–B3 destination review · 2026-10-07

SCOPED_SELF_REVIEW_COMPLETE / PO_PENDING. B2 and B3 rebuilt from approved B1 VN layout and exact-case photo on dedicated local slice. Four toggles each; defaults zh-Hans and zh-Hant. Explicit valid language wins; absent/invalid uses the journey default. Local index return stays the original journey.

[Fresh MSG-ANCHOR receipt](review-receipt.json) pins actual HTML/entry/copy/manifest and email/HTML anchors. [Render DOM evidence](render-runtime.json) covers24states; [functional evidence](functional-runtime.json) covers18tests. All16 full-page desktop1280/mobile390 screenshots visually inspected;320px smoke has no horizontal overflow. Preview: [B2](B2-preview.png), [B3](B3-preview.png). Each locale has separately named desktop/mobile full-page PNGs.

Photo reuse is exact same O1 customer/source bytes as B1, not a new image or source claim. Historical2020 visit caption/alt translated. Public/paid rights remain unknown. B1, all ad PNGs, selected copy/prompts/manifests and frozen core unchanged. Historical source-small and whole-journey insufficient findings remain.

Two of the7remaining established routes now implemented for PO review;5remain: B4, B5 and3O3pilot readers. No commit, main integration, GitHub push or live action. Docs impact reviewed: scoped current/README/build/readiness and owned inventory updated; no new strategy/budget/source-rights/tracking truth.
''', encoding='utf-8')
inventory = PACKET / 'inventory.csv'
with inventory.open(encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f)
    fields = reader.fieldnames
    rows = list(reader)
for row in rows:
    if row['Treatment'] == 'O1' and row['Locale'] in ('zh-Hans', 'zh-Hant'):
        t = next(t for t in intake['targets'] if t['locale'] == row['Locale'])
        row.update(State=t['batch'] + '_FOUR_LANGUAGE_PHOTO_READER_SELF_REVIEW_COMPLETE', Completion='IMPLEMENTED_SELF_REVIEW_PO_PENDING', OutputRoute=t['directory'] + '/case-reader.html?lang=' + t['locale'])
with inventory.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL)
    writer.writeheader()
    writer.writerows(rows)
targets = ['CURRENT_STATE.md', 'README.md', 'ads/linkedin/LinkedIn_Build_Pack.md', 'operations/Pre_Ad_Readiness_Plan.md', 'operations/fdi-destination-html/2026-10-07/README.md']
for relative in targets:
    p = ROOT / relative
    if relative.startswith('ads/'):
        link = '../../operations/fdi-destination-html/2026-10-07/B2-B3-review/README.md'
    elif relative == 'operations/Pre_Ad_Readiness_Plan.md':
        link = 'fdi-destination-html/2026-10-07/B2-B3-review/README.md'
    elif relative.endswith('2026-10-07/README.md'):
        link = 'B2-B3-review/README.md'
    else:
        link = 'operations/fdi-destination-html/2026-10-07/B2-B3-review/README.md'
    note = f'> **B2–B3 destination implementation · 2026-10-07:** Theo mandate làm7HTML còn lại, current slice đã dựng2reader B2/B3 theo B1 approved/VN design và anchor ảnh thật. Mỗi HTML4toggle, B2 mặc định zh-Hans, B3 zh-Hant; exact-case2020 photo/source/alt giữ đúng scope. Actual16desktop/mobile +320smoke và entry/toggle/refresh/return reviewed; fresh destination-only MSG-ANCHOR PASS / root SELF_REVIEW. New destination revisions PO_PENDING; historical artwork/full-journey findings giữ nguyên. Tổng3reader implemented (B1 PO approved, B2/B3 chờ duyệt),5mapped routes còn lại B4/B5+3O3. [Evidence]({link}). Working files trên slice riêng, chưa commit/main/push/live; không sửa worktree đang chạy. Docs impact reviewed: scoped status/inventory synchronized, nguồn/quyền ảnh/budget/frozen core unchanged. Earlier counts/status below are dated snapshots.\n\n'
    text = p.read_text(encoding='utf-8')
    if not text.startswith('> **B2–B3 destination implementation'):
        p.write_text(note + text, encoding='utf-8')
print('Review bound, protected hashes verified, scoped docs/inventory synchronized.')
