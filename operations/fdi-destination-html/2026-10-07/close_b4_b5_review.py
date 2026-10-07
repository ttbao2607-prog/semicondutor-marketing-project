"""Bound final O2 semantic/render evidence, preserve source bytes and status."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
REVIEW = PACKET / 'B4-B5-review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
intake = json.loads((PACKET / 'B4-B5-intake.json').read_text(encoding='utf-8'))
packs = json.loads((PACKET / 'B4-B5-copy-v1.json').read_text(encoding='utf-8'))
runtime = json.loads((REVIEW / 'render-runtime.json').read_text(encoding='utf-8'))
assert len(runtime) == 24 and all(not r['overflow'] and r['photo'] and r['textParity'] and r['attrParity'] and r['back'] == 'index.html' for r in runtime)
functional = json.loads((REVIEW / 'functional-runtime.json').read_text(encoding='utf-8'))
assert len(functional) == 18
for t in intake['targets']:
    d = ROOT / t['directory']
    source = Path(intake['source_worktree']) / t['directory']
    assert sha(d / 'case-reader.html') == t['reader_after_sha256']
    assert sha(d / 'index.html') == t['entry_after_sha256']
    for name, digest in t['source_files_sha256'].items():
        assert sha(source / name) == digest, 'Source worktree changed: reconcile first'
        if name not in ['case-reader.html', 'index.html']:
            assert sha(d / name) == digest, 'Approved dependencies must remain exact bytes'
    original = (source / 'index.html').read_text(encoding='utf-8-sig')
    expected = re.sub(r'href="case-reader\.html(?:\?lang=[^"]+)?"', f'href="case-reader.html?lang={t["locale"]}"', original)
    assert (d / 'index.html').read_text(encoding='utf-8') == expected
    html = (d / 'case-reader.html').read_text(encoding='utf-8')
    assert not re.search(r'<form\b|<iframe\b|gtag\(|fetch\(', html, re.I)
    assert '15454.html' not in html
assert sha(ROOT / 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html') == intake['base_reader_sha256']
assert sha(PACKET / 'B4-B5-copy-v1.json') == intake['copy_sha256']
groups = [
 ('hero', ['title', 'lead', 'caseLabel', 'market'], 'A1/A2/A3/A4', 'Operations-led packaging/testing lot handoff: same lot, stage/time and source/confirmation owner. Two differing reports may both be correct. No test-result-investigation or domestic chain-entry promise.'),
 ('photo', ['figure', 'figureSource', 'figureAlt'], 'A3/A7', 'Same exact-case2020 Digiwin visit photo as approved B1. Historical caption/date/Sohu byline translated; no inference of present factory operations or software outcomes. Photo rights remain unknown.'),
 ('case context', ['contextTitle', 'contextBody'], 'A1/A2/A6', 'China named customer implemented integrated ERP+iMES; records/process/efficiency problems remain attributed, not outcomes or promises.'),
 ('mechanisms', ['mechanismTitle', 'mechanismLead', 'm0Title', 'm0Body', 'm1Title', 'm1Body', 'm2Title', 'm2Body', 'm3Title', 'm3Body'], 'A6', 'SPC real-time collection/analysis, ECN parameter distribution, MES-linked lot/workstation/operator/product-material records, automatic exception records/escalation match frozen case source. No ERP-alone or equipment-substitute claim.'),
 ('same-basis comparison', ['valueTitle', 'valueLead', 'v1Title', 'v1Body', 'v1Prepare'], 'A3/A4/A7', 'Operations/Quality compare same lot/stage/recording time. Qualitative common basis and current example, not measured reduction of handoff time.'),
 ('handoff source', ['v2Title', 'v2Body', 'v2Prepare'], 'A4/A6', 'Identify authoritative source record and receiver information needs; reader workflow question, not extra unverified software feature.'),
 ('confirmation and next check', ['v3Title', 'v3Body', 'v3Prepare', 'bridge'], 'A4/A6/A7', 'Missing information, applicable parameter revision and exception follow-up have responsible confirmation roles. Conditional coordination value, no fabricated financial ROI/guarantee.'),
 ('consultation', ['consultLabel', 'consultTitle', 'consultBody', 'next', 'cta'], 'A2/A7', 'Bring actual lot handoff, compare status/source/next owner; Digiwin manufacturing-provider role explicit. Same Vietnamese external request page disclosed; no form/dispatch embedded.'),
 ('source/return', ['sourceLabel', 'sourceLink', 'sourceHint', 'sourceLang', 'back'], 'A7', 'Exact Chinese case06 instructions; old15454 mismatched detail link omitted, frozen source unchanged. Local O2 index preserved after toggle; external source/contact language disclosed.')
]
receipt = {
 'revision': 'B4-B5-O2-four-language-photo-v1', 'date': '2026-10-07', 'stage': 'POSTGEN_ARTIFACT', 'format': 'HTML, no ImageGen',
 'reviewer': 'root', 'independence': 'SELF_REVIEW', 'execution_status': 'SUCCESS',
 'scope': 'B4/B5 destination HTML and textual journey continuity/actual entry-return only; no new full ad-artwork journey certification',
 'message_anchor': {'id': 'VY-CONTENT-ANCHOR', 'revision': '1.0', 'sha256': sha(ROOT / 'operations/Vy_Email_Content_Anchor.md'), 'email_record': 'VY-MAIL-USER-20261006', 'original_email_sha256': sha(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md')},
 'html_anchor': {'id': 'FDI-DESTINATION-HTML-ANCHOR', 'revision': '1.0', 'sha256': sha(PACKET / 'Destination_HTML_Anchor.md')},
 'persona': 'O2 Operations + Quality / FDI manufacturing decision unit. Vietnamese is same FDI translation, not VN-domestic adaptation.',
 'audience': 'Hypothesis for content relevance; no live targeting or authority of individual enterprise verified.',
 'A5': 'N/A: FDI handoff-value framing, not domestic supply-chain entry readiness.',
 'unit_review': [{'locale': locale, 'unit': unit, 'rules': rules, 'observed': {key: pack[key] for key in keys}, 'judgment': judgment, 'verdict': 'MATCH'} for locale, pack in packs.items() for unit, keys, rules, judgment in groups],
 'journey_text_review': [{'batch': t['batch'], 'ordered_observations': [{'card_id': c['card_id'], 'headline': c['headline'], 'body': c['body'], 'caption': c['caption'], 'cta': c['cta']} for c in t['ordered_source_cards']], 'judgment': 'Cold/O2: conflicting lot status -> compare stage/time -> source for receiving team -> missing info and next owner -> shared handoff basis. Proof: Digiwin provider -> named China integrated case -> linked records/exceptions -> details. Destination expands that same case and reconnects to O2 handoff questions. Text continuity matches; no new render/native judgment of unchanged10PNGs.'} for t in intake['targets']],
 'transitions': ['O2 same-lot status -> same stage/time: different reports may both be correct; no simplistic data error accusation.', 'Stage/time -> source/receiver -> missing info/owner: clear handoff decision unit.', 'Provider -> exact China integrated case -> linked record/exception -> destination: same named proof/source scope.', 'Destination hero -> case -> published mechanisms: O2 context and attribution distinct from reference photo.', 'Mechanisms -> workflow questions: questions for present company, not case-measured handoff outcomes.', 'Questions -> consultation -> original journey return: one real workflow, disclosed external Vietnamese page, local O2 context retained.'],
 'locale_review': 'en international manufacturing language; vi concrete Quý Doanh Nghiệp direct-reader passages; Hans 工序/记录/生产运营/质量 vs Hant 製程階段/紀錄/營運/品質. Registered entity retained original script. Glyph/line-wrap visually reviewed in all16states; native-market/independent reviewer not claimed.',
 'proof': {'entity': '江苏中科智芯集成科技有限公司', 'geography': 'China', 'solution': 'integrated ERP + iMES', 'metric': 'No numeric result/ROI', 'source': 'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/', 'frozen_source_sha256': sha(ROOT / 'operations/linkedin-rmk-production-coordination/shared-releases/rmk-case06-harness-freeze-v2/public-content.json'), 'photo_sha256': sha(PACKET / 'B1-photo-research/case06-digiwin-visit-2020.jpeg'), 'photo_provenance_sha256': sha(PACKET / 'B1-photo-research/provenance.json'), 'public_paid_reuse': 'UNKNOWN; offline internal draft only'},
 'targets': intake['targets'],
 'copy_sha256': sha(PACKET / 'B4-B5-copy-v1.json'),
 'evidence': {p.name: sha(p) for p in sorted(REVIEW.iterdir()) if p.is_file() and p.suffix in ['.png', '.json'] and p.name != 'review-receipt.json'},
 'bounded_revision': 'VI title refined to “Cùng thông tin làm căn cứ bàn giao lô” to avoid implying an unverified shared-database capability. Fresh4affected desktop/mobile screenshots and2smoke checks replace VI evidence. Other locale rendered strings/photo/design unchanged; existing actual observations retained with explicit affected-scope recheck.',
 'render': '16 complete full-page states visually inspected:2routes×4locales×1280desktop/390mobile. All24runtime checks including320smoke pass. Original photo ratio, caption/source and all text/title/alt/aria match. Full-page screenshot timeouts initially led to viewport fallback; some intermediate viewport captures contained blank regions and were not accepted. Final5mobile full-page captures recovered through ordinary screenshot API after separate observed navigation; final16 sufficient. Intermediate raw/ snapshots are troubleshooting only, not final acceptance evidence.',
 'browser_security': 'Raw CDP capture permission was denied; no raw commands executed or denial bypassed. Continued only with ordinary documented screenshot API, which succeeded. Temporary viewport reset.',
 'interactions': '18 actual checks: absent/invalid fallback B4en/B5Hans; each4toggle updates locale/URL/alt and retains focus; reload selected Hant; actual return click shows original index with loaded selected ad; actual entry link opens correct original locale. Static initial no-JS copy/attributes inspected in source; not JS-disabled browser runtime. Unchanged external source/contact clicks not repeated.',
 'MSG-ANCHOR-01': 'MESSAGE_ANCHOR_PASS', 'content_status': 'SCOPED_SELF_REVIEW_COMPLETE_PO_PENDING',
 'historical_status': 'Approved ad selection remains approved offline; historical REVIEW_DRAFT_RENDER_GATE_PENDING/INSUFFICIENT_EVIDENCE for artwork/full journey retained. Destination-only review does not retroactively close these.',
 'pending': ['PO review of B4/B5 destination revision', 'Independent/native-market review', 'Public/paid photograph rights', 'Live deployment/runtime'],
 'git': 'B2/B3 checkpoint809dd1a local-only; B4/B5 working files only. Main source copied read-only; no merge/push.',
 'docs_impact': 'Reviewed DOCS_IMPACT_MAP, CURRENT_STATE/README/build/readiness, anchors/source register. Scoped current/inventory updated to5implemented,3O3remain. Same photo/source/rights; no additional source-register update required. No strategy/budget/provider/form/tracking/frozen-core change.'
}
(REVIEW / 'review-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
(REVIEW / 'README.md').write_text('''# B4–B5 destination review · 2026-10-07

SUCCESS / SCOPED_SELF_REVIEW_COMPLETE / PO_PENDING. O2 lot-handoff readers use approved VN Soft Structuralism + Editorial Split, authentic exact-case2020 photo and four toggles. B4 opens English; B5 Simplified Chinese; valid URL language overrides, absent/invalid falls back to journey. Hero/value/questions/CTA focus lot stage, recording time, source and confirmation responsibilities. China ERP+iMES capabilities remain attributed, with no new numeric outcome.

[Fresh MSG-ANCHOR receipt](review-receipt.json) binds actual HTML/entry/four-language copy/source and both anchors. [24render checks](render-runtime.json) include desktop1280/mobile390 and320overflow smoke. [18functional tests](functional-runtime.json) cover default/invalid, toggles/focus, refresh and actual entry/return. All16complete full-page final screenshots visually inspected; named B4/B5-desktop/mobile-en/vi/zh-Hans/zh-Hant.png. [B4 preview](B4-preview.png) · [B5 preview](B5-preview.png).

Capture recovery: initial timeouts prompted viewport captures; some intermediate images had blank areas and were not accepted. Ordinary documented screenshot API ultimately recovered all5missing mobile full-page images after separate navigation observation. Raw CDP permission denied; no raw action executed/bypassed. raw/ and section-runtime are troubleshooting records only, not final accepted evidence.

Main b2694b4 selected folders copied into this slice as read-only source dependencies; all20selectedPNG and copy/prompts/manifests/README match original bytes. Only reader and entry language query differ. B1–B3/frozen core/source worktrees unchanged. Same photo provenance and unknown public/paid rights as B1. Historical artwork/full-journey insufficient findings retained.

Checkpoint809dd1a saves B2/B3 PO-approved readers locally. B4/B5 current revisions remain uncommitted working files for PO review; no main integration/push/live. Total5implemented (B1–B3 PO-approved, B4–B5 pending),3O3pilot routes remain. Docs impact reviewed: scoped current/README/build/readiness and inventory updated; no new budget/strategy/tracking/source-rights state.
''', encoding='utf-8')
inventory = PACKET / 'inventory.csv'
with inventory.open(encoding='utf-8', newline='') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
for row in rows:
    if row['Treatment'] == 'O2' and row['Locale'] in ['en', 'zh-Hans']:
        t = next(t for t in intake['targets'] if t['locale'] == row['Locale'])
        row.update(State=t['batch'] + '_FOUR_LANGUAGE_PHOTO_READER_SELF_REVIEW_COMPLETE', Completion='IMPLEMENTED_SELF_REVIEW_PO_PENDING', OutputRoute=t['directory'] + '/case-reader.html?lang=' + t['locale'])
with inventory.open('w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fields, quoting=csv.QUOTE_ALL); writer.writeheader(); writer.writerows(rows)
for relative in ['CURRENT_STATE.md', 'README.md', 'ads/linkedin/LinkedIn_Build_Pack.md', 'operations/Pre_Ad_Readiness_Plan.md', 'operations/fdi-destination-html/2026-10-07/README.md']:
    p = ROOT / relative
    link = ('../../operations/' if relative.startswith('ads/') else '' if relative.startswith('operations/') else 'operations/') + 'fdi-destination-html/2026-10-07/B4-B5-review/README.md'
    if relative.endswith('2026-10-07/README.md'): link = 'B4-B5-review/README.md'
    note = f'> **B4–B5 destination implementation · 2026-10-07:** B2–B3 PO-approved checkpoint809dd1a saved local. Current O2 B4/B5 readers rebuilt theo VN design + anchor ảnh thật;4toggle mỗi HTML, defaults en/zh-Hans. Nội dung bàn giao lô giữ công đoạn/thời điểm/hồ sơ nguồn/người xác nhận; same-case2020photo và ERP+iMES scope. Actual16complete desktop/mobile +320smoke, entry/toggle/refresh/return reviewed; fresh destination-only MSG-ANCHOR PASS/root SELF_REVIEW, new B4/B5 revisions PO_PENDING. [Evidence]({link}). Tổng5implemented (B1–B3 approved, B4–B5 pending),3O3pilot còn lại. Read-only copy2selected main folders b2694b4 into owned slice; approved20PNG/copy/prompts/manifest giữ byte. B4/B5 working files only, chưa commit/main/push/live; concurrent worktrees/frozen core unchanged. Docs impact reviewed: scoped status/inventory synchronized; historical whole-journey findings and image-rights unknown retained. Earlier status/counts below are dated snapshots.\n\n'
    text = p.read_text(encoding='utf-8')
    if not text.startswith('> **B4–B5 destination implementation'): p.write_text(note + text, encoding='utf-8')
print('Final16 visual states and24DOM checks bound; approved source bytes preserved; scoped docs updated.')
