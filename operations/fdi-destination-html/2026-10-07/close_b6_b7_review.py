"""Bound final O2 semantic/render evidence, preserve source bytes and status."""
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
REVIEW = PACKET / 'B6-B7-review'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
intake = json.loads((PACKET / 'B6-B7-intake.json').read_text(encoding='utf-8'))
packs = json.loads((PACKET / 'B6-B7-copy-v1.json').read_text(encoding='utf-8'))
runtime = json.loads((REVIEW / 'render-runtime.json').read_text(encoding='utf-8'))
assert len(runtime) == 24 and all(not r['overflow'] and r['photo'] and r['textParity'] and r['attrParity'] and r['back'] == 'index.html' for r in runtime)
functional = json.loads((REVIEW / 'functional-runtime.json').read_text(encoding='utf-8'))
assert len(functional) == 18
for t in intake['targets']:
    checks=[r for r in functional if r['batch']==t['batch']]
    assert len(checks)==9
    for r in checks:
        if r['test'].startswith('fallback') or r['test']=='journey-entry': assert r['lang']==t['locale']
        elif r['test']=='toggle':
            assert r['focused']==r['lang'] and r['back']=='index.html'
            assert r['url'].endswith('?lang='+r['lang'])
            assert r['alt']==t['copy_by_locale'][r['lang']]['figureAlt']
        elif r['test']=='refresh': assert r['lang']=='zh-Hant'
        elif r['test']=='return':
            assert r['loadedAd'] and r['entry']=='case-reader.html?lang='+t['locale']
            assert r['url'].endswith(t['directory']+'/index.html')
    for lang in ['en','vi','zh-Hans','zh-Hant']:
        for side in ['left','right']: assert (REVIEW/f"{t['batch']}-desktop-{lang}-{side}.png").exists()
        assert (REVIEW/f"{t['batch']}-mobile-{lang}.png").exists()

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
assert sha(PACKET / 'B6-B7-copy-v1.json') == intake['copy_sha256']
groups = [
 ('hero', ['title', 'lead', 'caseLabel', 'market'], 'A1/A2/A3/A4', 'Operations-led packaging/testing lot handoff: same lot, stage/time and source/confirmation owner. Two differing reports may both be correct. No test-result-investigation or domestic chain-entry promise.'),
 ('photo', ['figure', 'figureSource', 'figureAlt'], 'A3/A7', 'Same exact-case2020 Digiwin visit photo as approved B1. Historical caption/date/Sohu byline translated; no inference of present factory operations or software outcomes. Photo rights remain unknown.'),
 ('case context', ['contextTitle', 'contextBody'], 'A1/A2/A6', 'China named customer implemented integrated ERP+iMES; records/process/efficiency problems remain attributed, not outcomes or promises.'),
 ('mechanisms', ['mechanismTitle', 'mechanismLead', 'm0Title', 'm0Body', 'm1Title', 'm1Body', 'm2Title', 'm2Body', 'm3Title', 'm3Body'], 'A6', 'SPC real-time collection/analysis, ECN parameter distribution, MES-linked lot/workstation/operator/product-material records, automatic exception records/escalation match frozen case source. No ERP-alone or equipment-substitute claim.'),
 ('same-basis comparison', ['valueTitle', 'valueLead', 'v1Title', 'v1Body', 'v1Prepare'], 'A3/A4/A7', 'Operations/Quality compare same lot/stage/recording time. Qualitative common basis and current example, not measured reduction of handoff time.'),
 ('handoff source', ['v2Title', 'v2Body', 'v2Prepare'], 'A4/A6', 'Identify authoritative source record and receiver information needs; reader workflow question, not extra unverified software feature.'),
 ('confirmation and next check', ['v3Title', 'v3Body', 'v3Prepare', 'bridge'], 'A4/A6/A7', 'Missing information/source and who confirms the next step before receiver updates lot status; conditional coordination value, no fabricated financial ROI/guarantee.'),
 ('consultation', ['consultLabel', 'consultTitle', 'consultBody', 'next', 'cta'], 'A2/A7', 'Bring actual lot handoff, compare status/source/next owner; Digiwin manufacturing-provider role explicit. Same Vietnamese external request page disclosed; no form/dispatch embedded.'),
 ('source/return', ['sourceLabel', 'sourceLink', 'sourceHint', 'sourceLang', 'back'], 'A7', 'Exact Chinese case06 instructions; old15454 mismatched detail link omitted, frozen source unchanged. Local O2 index preserved after toggle; external source/contact language disclosed.')
]
receipt = {
 'revision': 'B6-B7-O2-four-language-photo-v1', 'date': '2026-10-07', 'stage': 'POSTGEN_ARTIFACT', 'format': 'HTML, no ImageGen',
 'reviewer': 'root', 'independence': 'SELF_REVIEW', 'execution_status': 'SUCCESS',
 'scope': 'B6/B7 destination HTML and textual journey continuity/actual entry-return only; no new full ad-artwork journey certification',
 'message_anchor': {'id': 'VY-CONTENT-ANCHOR', 'revision': '1.0', 'sha256': sha(ROOT / 'operations/Vy_Email_Content_Anchor.md'), 'email_record': 'VY-MAIL-USER-20261006', 'original_email_sha256': sha(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md')},
 'html_anchor': {'id': 'FDI-DESTINATION-HTML-ANCHOR', 'revision': '1.0', 'sha256': sha(PACKET / 'Destination_HTML_Anchor.md')},
 'persona': 'B6 O2 and B7 O4-O: FDI manufacturing Operations with Quality collaboration. Vietnamese is the same FDI translation, not VN-domestic adaptation.',
 'audience': 'Hypothesis for content relevance; no live targeting or authority of individual enterprise verified.',
 'A5': 'N/A: FDI handoff-value framing, not domestic supply-chain entry readiness.',
 'unit_review': [{'batch': t['batch'], 'locale': locale, 'unit': unit, 'rules': rules, 'observed': {key: pack[key] for key in keys}, 'judgment': judgment, 'verdict': 'MATCH'} for t in intake['targets'] for locale, pack in t['copy_by_locale'].items() for unit, keys, rules, judgment in groups],
 'journey_text_review': [{'batch': t['batch'], 'ordered_observations': [{'card_id': c['card_id'], 'headline': c['headline'], 'body': c['body'], 'caption': c['caption'], 'cta': c['cta']} for c in t['ordered_source_cards']], 'judgment': 'Cold same-lot reports -> scope stage/time -> source for receiving team -> missing information/confirmation owner -> shared basis. B6 O2 explains this sequence; B7 O4-O explicitly numbers three questions. Proof provider -> named China integrated case -> linked records/exceptions -> implementation reader. Destination retains that same case and questions; unchanged10PNGs receive no new native/artwork verdict.'} for t in intake['targets']],
 'transitions': ['O2 same-lot status -> same stage/time: different reports may both be correct; no simplistic data error accusation.', 'Stage/time -> source/receiver -> missing info/owner: clear handoff decision unit.', 'Provider -> exact China integrated case -> linked record/exception -> destination: same named proof/source scope.', 'Destination hero -> case -> published mechanisms: O2 context and attribution distinct from reference photo.', 'Mechanisms -> workflow questions: questions for present company, not case-measured handoff outcomes.', 'Questions -> consultation -> original journey return: one real workflow, disclosed external Vietnamese page, local O2 context retained.'],
 'locale_review': 'en international manufacturing language; vi concrete Quý Doanh Nghiệp direct-reader passages; Hans 工序/记录/生产运营/质量 vs Hant 製程階段/紀錄/營運/品質. Registered entity retained original script. Glyph/line-wrap visually reviewed in all16states; native-market/independent reviewer not claimed.',
 'proof': {'entity': '江苏中科智芯集成科技有限公司', 'geography': 'China', 'solution': 'integrated ERP + iMES', 'metric': 'No numeric result/ROI', 'source': 'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/', 'frozen_source_sha256': sha(ROOT / 'operations/linkedin-rmk-production-coordination/shared-releases/rmk-case06-harness-freeze-v2/public-content.json'), 'photo_sha256': sha(PACKET / 'B1-photo-research/case06-digiwin-visit-2020.jpeg'), 'photo_provenance_sha256': sha(PACKET / 'B1-photo-research/provenance.json'), 'public_paid_reuse': 'UNKNOWN; offline internal draft only'},
 'targets': intake['targets'],
 'copy_sha256': sha(PACKET / 'B6-B7-copy-v1.json'),
 'evidence': {p.name: sha(p) for p in sorted(REVIEW.iterdir()) if p.is_file() and p.suffix in ['.png', '.json'] and p.name != 'review-receipt.json'},
 'bounded_revision': 'B6 continues O2 handoff; B7 explicitly continues three-question O4-O framing. Source copy/20PNG/prompts/manifests/README preserved. Only readers and entry language query changed.',
 'render': '16actual complete render states, covered by24full-height screenshots, visually inspected:2routes x4locales x1280desktop/390mobile;8additional320overflow smoke states. Photo original ratio, captions/source, full sections, title/text/alt/aria match; VI and Chinese glyph/wrapping reviewed. Initial source translated, no JS-disabled browser test claimed.',
 'browser_security': 'Shared OSAT browser lock was waited out, then atomically owned. Ordinary fullPage capture repeatedly timed out. Documented clip screenshot API succeeded for complete390px mobile and paired640px desktop regions covering1280px full width/height;24final screenshots for16states. Failed/intermediate screenshots excluded. No raw CDP or alternative browser-control mechanism. Temporary viewport reset.',
 'interactions': '18actual checks: absent/invalid defaults B6Hant/B7en;4toggles with focus/URL/alt parity per route; refresh persistence; original index return with loaded ad and journey entry correct locale. External source/contact unchanged from B1; no form submission.',
 'MSG-ANCHOR-01': 'MESSAGE_ANCHOR_PASS', 'content_status': 'SCOPED_SELF_REVIEW_COMPLETE_PO_PENDING',
 'historical_status': 'Approved ad selection remains approved offline; historical REVIEW_DRAFT_RENDER_GATE_PENDING/INSUFFICIENT_EVIDENCE for artwork/full journey retained. Destination-only review does not retroactively close these.',
 'pending': ['PO review of B6/B7 destination revision', 'Independent/native-market review', 'Public/paid photograph rights', 'Live deployment/runtime'],
 'git': 'O3 checkpoint4317610 local-only; B6/B7 working files only, no commit/main integration/push/live. Main selected sources copied read-only.',
 'docs_impact': 'Reviewed impact map/current/build/readiness/anchors/source register. Current packet/inventory updated to10implemented,8PO-approved and2pending. Same source/photo/rights, no new source-register state, budget/form/tracking/frozen core unchanged.'
}
(REVIEW / 'review-receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

(REVIEW/'README.md').write_text('''# B6–B7 destination review

SUCCESS / SCOPED_SELF_REVIEW_COMPLETE / PO_PENDING. B6 O2 defaults zh-Hant; B7 O4-O defaults en. Both use approved VN Soft Structuralism + Editorial Split, authentic exact-case2020 Digiwin visit photo,4language toggles and exact source-journey return. B7 explicitly continues3questions for scope/source/confirmation. Questions describe current workflow review, not measured case outcomes; no15→5month-close metric in these handoff destinations.

[Fresh receipt](review-receipt.json) binds actual reader/index, source/copy/anchors and individual unit observations for both routes in all4languages. [Render checks](render-runtime.json):16actual desktop/mobile render states inspected using24full-height screenshots,8additional320overflow smoke states. [Functional checks](functional-runtime.json):18actual fallback/toggle/focus/URL/refresh/return/entry tests. Desktop screenshot pairs named B6/B7-desktop-en/vi/zh-Hans/zh-Hant-left/right.png cover x0–640 and640–1280 across full page height; mobile screenshots named B6/B7-mobile-en/vi/zh-Hans/zh-Hant.png cover full390px page width/height. Ordinary fullPage API repeatedly timed out; documented clip API succeeded. No image compositing/overlay, no raw CDP, no security-denial workaround. Root SELF_REVIEW only, not independent/native-market/full-journey certification. Photo/source/contact languages disclosed; reuse rights remain unknown.

Selected main source folders copied read-only, pinned in B6-B7-intake.json. All20ad PNG/copy/prompts/manifests/README preserved exactly. No source worktree or frozen core changed. Historical artwork/mobile/eligibility findings retained. O3 checkpoint4317610 local only; new B6/B7 readers are working files, uncommitted and PO_PENDING. No main integration/push/live.

All10concrete destination readers now implemented:8PO checkpoint-approved,2new pending. Docs impact reviewed: scoped current/README/build/readiness/inventory synchronized, source/rights/budget/core unchanged.
''',encoding='utf-8')
inventory=PACKET/'inventory.csv'
with inventory.open(encoding='utf-8',newline='') as f:
 r=csv.DictReader(f); fields=r.fieldnames; rows=list(r)
for row in rows:
 if (row['Treatment'],row['Locale']) in [('O2','zh-Hant'),('O4-O','en')]:
  t=next(t for t in intake['targets'] if t['locale']==row['Locale'])
  row.update(State=t['batch']+'_FOUR_LANGUAGE_PHOTO_READER_SELF_REVIEW_COMPLETE',Completion='IMPLEMENTED_SELF_REVIEW_PO_PENDING',OutputRoute=t['directory']+'/case-reader.html?lang='+t['locale'])
with inventory.open('w',encoding='utf-8',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,quoting=csv.QUOTE_ALL,lineterminator='\n'); w.writeheader(); w.writerows(rows)
for rel in ['CURRENT_STATE.md','README.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','operations/fdi-destination-html/2026-10-07/README.md']:
 f=ROOT/rel
 link='operations/fdi-destination-html/2026-10-07/B6-B7-review/README.md'
 if rel.startswith('ads/'): link='../../'+link
 elif rel=='operations/Pre_Ad_Readiness_Plan.md': link=link.removeprefix('operations/')
 elif rel.endswith('2026-10-07/README.md'): link='B6-B7-review/README.md'
 note=f'> **B6–B7 destination implementation ·2026-10-07:** PO mandate “OKie làm B6-7”. Two selected source main readers rebuilt with approved VN Soft Structuralism + Editorial Split, authentic same-case2020 photo and4toggles; B6 O2 defaults zh-Hant, B7 O4-O defaults en with3explicit workflow questions.16actual complete desktop/mobile render states (24full-height clip screenshots),8small-width smoke states and18functional checks reviewed; fresh destination-only MSG-ANCHOR PASS/root SELF_REVIEW; PO_PENDING. Current10concrete readers implemented (8approved checkpoints,2new pending). All20PNG/source copy/manifests preserved, historical whole-journey findings and photo-rights unknown retained. [Evidence]({link}). O3 checkpoint4317610 local; B6/B7 working files only, no new commit/main integration/push/live. Docs impact reviewed: current/owned inventory synchronized; budget/source rights/frozen core unchanged. Earlier counts are dated scope snapshots.\n\n'
 f.write_text(note+f.read_text(encoding='utf-8'),encoding='utf-8')
print('B6/B7 closure verified; scoped docs and inventory synchronized.')
