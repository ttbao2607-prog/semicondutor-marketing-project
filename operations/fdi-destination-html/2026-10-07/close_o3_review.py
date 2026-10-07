"""Bind observed O3 review evidence and synchronize owned slice status. No Git mutation."""
from pathlib import Path
import csv
import hashlib
import json

ROOT = Path(__file__).resolve().parents[3]
P = Path(__file__).resolve().parent
R = P / 'O3-review'
def read(path):
    return json.loads(path.read_text(encoding='utf-8'))
def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()
def dump(path, value):
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

intake = read(P / 'O3-intake.json')
copy = read(P / 'O3-copy-v1.json')
render = read(R / 'render-runtime.json')
functional = read(R / 'functional-runtime.json')
assert len(render) == 36 and len(functional) == 27
assert all(x['textParity'] and x['attrParity'] and x['photo'] and not x['overflow'] for x in render)
assert sha(P / 'O3-copy-v1.json') == intake['copy_sha256']
protected = []
for t in intake['targets']:
    folder = ROOT / t['directory']
    assert sha(folder / 'case-reader.html') == t['reader_after_sha256']
    assert sha(folder / 'index.html') == t['entry_after_sha256']
    for name, h in t['original_files_sha256'].items():
        if name not in ('case-reader.html', 'index.html'):
            assert sha(folder / name) == h, name
            protected.append(t['directory'] + '/' + name)
    f = [x for x in functional if x['batch'] == t['batch']]
    assert len(f) == 9
    for x in f:
        if x['test'].startswith('fallback') or x['test'] == 'journey-entry':
            assert x['lang'] == t['locale']
        elif x['test'] == 'toggle':
            assert x['focused'] == x['lang'] and x['back'] == 'index.html'
            assert x['url'].endswith('?lang=' + x['lang'])
            assert x['alt'] == copy[x['lang']]['figureAlt']
            assert x['result'] == copy[x['lang']]['resultValue']
        elif x['test'] == 'refresh':
            assert x['lang'] == 'zh-Hant'
        elif x['test'] == 'return':
            assert x['loadedAd'] and x['entry'] == 'case-reader.html?lang=' + t['locale']
            assert x['url'].endswith(t['directory'] + '/index.html')

groups = [
 ('hero','A1/A2/A3/A4',['title','lead','caseLabel','market'], 'Packaging/testing Operations prepares month-end records for Finance. China reference and integrated ERP+iMES, no assumed live Finance targeting.'),
 ('photo','A3/A7',['figure','figureSource','figureAlt'], 'Authentic exact-entity September2020 Digiwin visit, original Chinese banner and source disclosed; historical event only, rights unknown.'),
 ('case context','A1/A2/A6',['contextTitle','contextBody'], 'Named Chinese case with integrated ERP+iMES and attributed records/process problems; no present target-account fit inference.'),
 ('published result','A4/A6',['resultTitle','resultValue','resultNote'], '15 days to5 days is reported month-close duration for named integrated case, not financial ROI, standalone ERP effect or promise.'),
 ('mechanisms','A6',['mechanismTitle','mechanismLead'] + [f'm{i}{s}' for i in range(4) for s in ('Title','Body')], 'Source-bound SPC collect/analyze, ECN parameter changes, MES-linked records, automatic exception records/escalation. No new accounting automation capability.'),
 ('unfinished work','A3/A4/A7',['valueTitle','valueLead','v1Title','v1Body','v1Prepare'], 'Review unfinished work by lot/stage/cutoff/source/confirmation role; qualitative current-practice questions, no measured improvement.'),
 ('output and loss','A3/A4/A7',['v2Title','v2Body','v2Prepare'], 'Completed output, scrap/loss for same period with sources/unresolved discrepancies; no cost-saving estimate or inferred financial result.'),
 ('handoff ownership','A3/A4/A7',['v3Title','v3Body','v3Prepare','bridge'], 'Identify who verifies records and hands off to Finance, current example/time; case result expressly not a forecast for another factory.'),
 ('next step','A1/A3/A7',['consultLabel','consultTitle','consultBody','next','cta'], 'Bring one month-end records handoff to manufacturing ERP/smart manufacturing discussion; external Vietnamese consultation request disclosed, no submission performed.'),
 ('source and return','A6/A7',['sourceLabel','sourceLink','sourceHint','sourceLang','back','footer'], 'Named Digiwin Vietnam case collection and original Chinese source language disclosed; same local journey return regardless of chosen reader language.')
]
units = []
for lang, c in copy.items():
    for unit, rules, keys, judgment in groups:
        units.append({'locale':lang,'applies_to':[t['batch'] for t in intake['targets']], 'unit':unit,'rules':rules,'observed':{k:c[k] for k in keys},'judgment':judgment,'verdict':'MATCH'})

journey = []
transitions = []
for t in intake['targets']:
    rows = t['ordered_rows']
    journey.append({'batch':t['batch'],'locale':t['locale'],'ordered_observations':rows,'scope':'Current journey text/captions/alt read; original ad PNG retained, no new artwork/full-journey certification.', 'judgment':'Plant Operations-led preparation of unfinished work/output/loss records, same period and verification owner for Finance. Proof identifies named China integrated ERP+iMES case and15-to5-day close result; new destination preserves this bridge.'})
    notes = [
        'Month-end hook connects Operations record readiness to Finance collaboration.',
        'Clarifies unfinished work by lot/stage/source and verification role.',
        'Extends same-period review to completed output, scrap and loss.',
        'Clarifies confirmation owner, missing information and handoff timing.',
        'Common records basis brings Operations and Finance discussion together.',
        'Provider positioning remains manufacturing ERP to smart manufacturing.',
        'Proof identifies named China packaging/testing enterprise and integrated ERP+iMES.',
        'Reported month-close15-to5days remains attributed to case.',
        'Read-more asks for case context/solution/results; reader supplies them.',
    ]
    for a, b, note in zip(rows, rows[1:], notes):
        transitions.append({'batch':t['batch'],'from':a['index'],'to':b['index'],'observation':note,'verdict':'MATCH_TEXTUAL_CONTINUITY'})
    transitions.append({'batch':t['batch'],'from':10,'to':'destination','observed':copy[t['locale']]['lead'],'judgment':'New reader adds source-bound case context/mechanisms/result and Operations-Finance current-record questions, with consultation and exact local return. Does not convert historical full-journey findings to PASS.','verdict':'MATCH_DESTINATION_CONTINUITY'})

evidence = {x.name:sha(x) for x in sorted(R.iterdir()) if x.suffix in ('.png','.json')}
assert len([x for x in evidence if x.endswith('.png') and x != 'O3-preview.png']) == 24
prior = read(P / 'B4-B5-review/review-receipt.json')
receipt = {
 'revision':'O3-three-four-language-photo-v1','date':'2026-10-07','stage':'POSTGEN_ARTIFACT','format':'HTML; no ImageGen','reviewer':'root','independence':'SELF_REVIEW','execution_status':'SUCCESS',
 'scope':'Three destination readers, actual entry/return and adjacent current journey textual continuity only.',
 'message_anchor':prior['message_anchor'],'html_anchor':prior['html_anchor'],
 'persona':'FDI packaging/testing Operations plant managers, Finance collaborator; all four languages retain same persona. VI is not domestic VN campaign.',
 'audience':'Content hypothesis only; live targeting and entity-fit/decision authority UNKNOWN. Historical Finance-primary mismatch warning remains outside fresh destination scope.',
 'A5':'N/A: FDI business-value framing, no domestic supply-chain-entry readiness claim.',
 'unit_review':units,'journey_text_review':journey,'transitions':transitions,
 'locale_review':{'en':'Operations/Finance, unfinished work/cut-off and records handoff; no promise.', 'vi':'Sản phẩm dở dang, sản lượng/hao hụt, chốt kỳ and trách nhiệm bàn giao; consultation uses Quý Doanh Nghiệp.', 'zh-Hans':'工厂运营/财务、在制品、截止时点、产量与损耗、交接责任; simplified forms and visible glyphs inspected.', 'zh-Hant':'工廠營運/財務、在製品、截止時點、產量與耗損、交接職責; traditional terminology and visible glyphs inspected.', 'qualification':'Root semantic/render review, not independent native-market signoff.'},
 'proof':{'entity':'江苏中科智芯集成科技有限公司','geography':'China','solution':'Integrated ERP+iMES','metric':'Month-close duration15days to5days, published case; not ROI/promise.', 'source_path':'operations/linkedin-rmk-production-coordination/shared-releases/rmk-case06-harness-freeze-v2/public-content.json','source_sha256':sha(ROOT / 'operations/linkedin-rmk-production-coordination/shared-releases/rmk-case06-harness-freeze-v2/public-content.json'), 'photo_sha256':sha(P / 'B1-photo-research/case06-digiwin-visit-2020.jpeg'),'provenance_sha256':sha(P / 'B1-photo-research/provenance.json'),'rights':'UNKNOWN for public/paid reuse; internal preview only.'},
 'targets':[{k:t[k] for k in ('batch','locale','directory','reader_after_sha256','entry_after_sha256')} for t in intake['targets']], 'copy_sha256':intake['copy_sha256'],'intake_sha256':sha(P / 'O3-intake.json'),'evidence':evidence,
 'bounded_revision':{'preserved_files_checked':protected,'reader':'Three existing readers replaced, same routes; all4locales embedded.','index':'Only existing reader href supplies matching explicit lang.','unchanged':'All30ad PNG, journey.json, original captions/copy/README, B1-B5, historical receipts and frozen core.'},
 'render':{'complete_screens':24,'DOM_rows':36,'widths':[1280,390,320],'review':'All24full-page actual browser screenshots visually inspected: desktop editorial split, mobile single column, all sections/photo/caption/metric/CTA/source/footer; VI and both Chinese glyph/wrapping visible, no overlap/crop/overflow. White case result panel retains VN paper/blue hierarchy. 320is DOM overflow smoke, not full screenshot certification.','no_js':'Initial source inspected only; no actual browser JS-disabled run claimed.'},
 'interactions':{'rows':27,'review':'Each route absent/invalid defaults,4actual toggles/focus/URL/alt/result, refresh persistence, exact return with loaded ad, actual journey entry reviewed.'},
 'MSG-ANCHOR-01':'MESSAGE_ANCHOR_PASS','content_status':'SCOPED_SELF_REVIEW_COMPLETE / PO_PENDING',
 'historical_status':'Original Finance-audience/entity-fit warnings and ad-artwork/full-journey FAIL/CHANGES_REQUIRED/INSUFFICIENT_EVIDENCE remain historical scoped evidence; no retroactive PASS.',
 'pending':['PO review of3new destination revisions','Independent/native-market review not claimed','Live audience/entity-fit eligibility','Public/paid photo reuse rights','LDP/form/tracking/publish runtime'],
 'git':{'B4_B5_checkpoint':intake['base_checkpoint'],'current_O3':'Working-tree/untracked files on owned branch; uncommitted.','remote':'No merge/main integration/push/live.'},
 'docs_impact':'Reviewed impact map and scoped current/readiness/build/README/inventory; status synchronized. Message anchor/email/source register/budget/frozen core unchanged; no new proof or rights acceptance.'
}
assert sha(ROOT / 'operations/Vy_Email_Content_Anchor.md') == receipt['message_anchor']['sha256']
assert sha(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md') == receipt['message_anchor']['original_email_sha256']
assert sha(P / 'Destination_HTML_Anchor.md') == receipt['html_anchor']['sha256']
dump(R / 'review-receipt.json', receipt)

inventory = P / 'inventory.csv'
with inventory.open(encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f); fields = reader.fieldnames; rows = list(reader)
for row in rows:
    if row['Treatment'] == 'O3':
        t = next(t for t in intake['targets'] if t['locale'] == row['Locale'])
        row.update(State=t['batch'] + '_FOUR_LANGUAGE_PHOTO_READER_SELF_REVIEW_COMPLETE', Completion='IMPLEMENTED_SELF_REVIEW_PO_PENDING', OutputRoute=t['directory'] + '/case-reader.html?lang=' + t['locale'])
with inventory.open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=fields,lineterminator='\n',quoting=csv.QUOTE_ALL); writer.writeheader(); writer.writerows(rows)

note = '> **O3 destination closeout · 2026-10-07:** B4/B5 PO-approved checkpoint `9bc0bc6` saved local on owned FDI slice. Remaining3O3 readers rebuilt in place with VN Soft Structuralism + Editorial Split, same exact-case authentic2020 Digiwin visit photo,4toggles and journey defaults en/zh-Hans/zh-Hant. Actual24desktop/mobile screens +12small-width smoke states and27functional checks reviewed; fresh destination-only MSG-ANCHOR PASS/root SELF_REVIEW,3new revisions PO_PENDING. All8mapped readers now implemented (B1–B5 approved,3O3 pending), completing7additional HTMLs after B1;25conditional future coverage rows remain outside current mandate. O3 keeps Operations-led unfinished-work/output/loss record handoff to Finance and source-bound integrated ERP+iMES15→5-day month-close case; historical whole-journey/audience/entity-fit/artwork findings and photo-rights unknown preserved. O3 working files only, no new commit/main integration/push/live. [Review evidence](operations/fdi-destination-html/2026-10-07/O3-review/README.md). Docs impact reviewed: scoped current status, build/readiness and inventory synchronized; budget/source rights/frozen core unchanged. Earlier counts/status below are dated snapshots.\n\n'
for rel in ['CURRENT_STATE.md','README.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','operations/fdi-destination-html/2026-10-07/README.md']:
    file = ROOT / rel
    localnote = note
    if rel.startswith('operations/fdi-destination-html'):
        localnote = note.replace('operations/fdi-destination-html/2026-10-07/O3-review/README.md','O3-review/README.md')
    elif rel == 'operations/Pre_Ad_Readiness_Plan.md':
        localnote = note.replace('operations/fdi-destination-html/2026-10-07/O3-review/README.md','fdi-destination-html/2026-10-07/O3-review/README.md')
    elif rel.startswith('ads/linkedin/'):
        localnote = note.replace('operations/fdi-destination-html/2026-10-07/O3-review/README.md','../../operations/fdi-destination-html/2026-10-07/O3-review/README.md')
    file.write_text(localnote + file.read_text(encoding='utf-8'), encoding='utf-8')
with (P / 'O3-execution.md').open('a',encoding='utf-8') as f:
    f.write('\nCloseout: SUCCESS / destination-only SELF_REVIEW_COMPLETE / PO_PENDING. All planned render/functional/bounded-preservation checks completed; see O3-review/review-receipt.json. Three readers remain uncommitted for PO review.\n')
print('O3 closure:24 screenshots,36 render rows,27 functional rows; protected originals verified; scoped docs synchronized.')
