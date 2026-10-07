"""Record actual scoped observations; does not award missing visual evidence a pass."""
from pathlib import Path
import hashlib, json, csv, io
ROOT = Path(__file__).resolve().parents[3]
PACK = Path(__file__).parent
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
receipt = {
 'revision':'b1-four-language-reader-v1','date':'2026-10-07',
 'branch':'slice/linkedin-fdi-destination-html','writer':'root','reviewer':'root','independence':'SELF_REVIEW',
 'execution_status':'PARTIAL','implementation':'COMPLETE_FOR_PILOT','render_gate':'DESKTOP_VI_FULL_REVIEW_PENDING',
 'message_anchor':{'id':'VY-CONTENT-ANCHOR','revision':'1.0','path':'operations/Vy_Email_Content_Anchor.md','sha256':sha('operations/Vy_Email_Content_Anchor.md'),
 'email_record':'VY-MAIL-USER-20261006','email_sha256':sha('operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),
 'stage':'POSTGEN_ARTIFACT','verdict':'INSUFFICIENT_EVIDENCE'},
 'scope':{'segment':'FDI','persona':'Quality/QA with Operations','journey':'O1/B1','locales':['vi','en','zh-Hans','zh-Hant'],
 'note':'All four reader languages translate the same FDI journey; VI is not a domestic adaptation. Adjacent selected B1 script reviewed, not a fresh full ten-image journey certification.'},
 'bindings':{p:sha(p) for p in [
 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html',
 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/index.html',
 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/selected-copy.json',
 'deliverables/linkedin-vn-journey/2026-10-06-v3/case-aplus.html',
 'operations/linkedin-rmk-production-coordination/shared-releases/rmk-case06-harness-freeze-v2/public-content.json',
 'operations/fdi-destination-html/2026-10-07/B1-copy-v1.json']},
 'units':[
 {'surface':'hero/illustration','keys':['title','lead','figure','figureSource'],'observation':'Unexpected result -> lot/context/next owner. Neutral connected-record vector, visibly labelled conceptual, not a customer site or product screenshot.'},
 {'surface':'business context','keys':['contextTitle','contextBody'],'observation':'Exact legal name 江苏中科智芯集成科技有限公司, China, integrated ERP+iMES and three source problems retained.'},
 {'surface':'four mechanism entries','keys':['m0Title','m0Body','m1Title','m1Body','m2Title','m2Body','m3Title','m3Body'],'observation':'All four profiles reuse frozen project_details verbatim. SPC/ECN/linked records/exception escalation, no ERP-only causality or test-result outcome added.'},
 {'surface':'three review questions','keys':['v1Title','v1Body','v1Prepare','v2Title','v2Body','v2Prepare','v3Title','v3Body','v3Prepare','bridge'],'observation':'Clearly reader questions and proposed preparation, not customer outcomes. Value is shared information and review ownership, no invented ROI/payback/quality guarantee.'},
 {'surface':'consultation','keys':['consultLabel','consultTitle','consultBody','next','cta'],'observation':'Digiwin supplier voice; one workflow as next step; existing external VI contact route disclosed, no form submission.'},
 {'surface':'source/return/toggle','keys':['sourceLabel','sourceLink','sourceHint','sourceLang','back','langLabel'],'observation':'Chinese source language disclosed in each profile; proper name and source UI literals retained in original script. English journey return unchanged after language switch; all four buttons title/text/aria/SVG accessible label switch.'}
 ],
 'A1':'Packaging/testing is explicit reference-case context, not an assertion of all target-account relevance.',
 'A2':'Local buying/system authority remains unknown; reader asks about actual workflow and does not assert fit of any live account.',
 'A3':'FDI Quality/QA + Operations throughout all translations; VI Quý Doanh Nghiệp, zh-Hant 品質/營運/紀錄 versus zh-Hans 质量/运营/记录. Legal source name remains Simplified Chinese intentionally.',
 'A4':'Business-value bridge is shared review basis and responsibilities; no numeric return or universal outcome.',
 'A5':'N/A: FDI reader in four display languages, not domestic readiness narrative.',
 'A6':'Mechanisms bound to published integrated case snapshot; no fabricated software UI, charts, metrics or standalone ERP capability.',
 'A7':'O1 next review -> China linked-record reference -> current-workflow questions -> consultation; source and return navigation are distinct. Browser clicked reader -> original English journey -> reader and observed lang=en.',
 'editorial':'No internal approval/process language on reader; scope carried by named case, geography, integrated solution and attribution. Existing viewer historical banner not rewritten.',
 'observed_render':{'desktop_full':['en at1422x1000','zh-Hans at1422x1000','zh-Hant at1280x900'],
 'desktop_vi':'Hero observed at1422x1000; full-page/section screenshot attempts repeatedly timed out. Full desktop VI layout review NOT certified.',
 'mobile_full':'All four observed at434x938; single-column hierarchy, glyphs, CTA wrap and source visible. No horizontal overflow.',
 'smoke':'Actual320x844 all four valid lang, invalid and missing fallback -> en; zero text/attribute parity mismatch; embedded logo loaded; one pressed button.',
 'function':'Toggle changes URL through replaceState; reload preserves locale; button focus retained on observed toggle; return index remains English. Actual source journey click reopened English.',
 'viewport_note':'Browser zoom means requested dimensions differ from actual. Observed1280 achieved via1152 override; observed320 via288; do not label434 as390 certification.'},
 'source_recheck':{'historical_snapshot':'Frozen public-content unchanged; new mechanisms reused, historical rights/scope retained.',
 'removed_detail_link':'https://www.digiwin.com/erp/15454.html now serves a different MES article (observed web fetch). Removed from new reader only; frozen source and historical receipts not edited.',
 'collection_live':'web fetch403; browser destination was not revalidated. Source href/snapshot bound only; no live source-navigation certification.'},
 'remaining':['Full VI desktop visual review','Independent/native-market review and PO acceptance','Live source-collection availability','LadiPage/runtime/deployment scope'],
 'preservation':'B1 ten original PNGs, captions, proof scope, frozen core and prior receipt verdicts retained. New reader replaces local B1 path only; index changes just ?lang=en entry.',
 'git':'Working files only on this slice, no staging/commit/merge/push/live.',
 'docs_impact':'Current-state/README/build/readiness updated in this slice for new trial, preserve historical PO adoption and MSG verdicts.'
}
(PACK/'B1-review/review-receipt.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
note='''# B1 · Four-language Leonxinx reader trial

Implemented O1/B1 destination at the existing `case-reader.html` route. Same accepted VN Soft Structuralism + Editorial Split CSS, embedded Digiwin logo, neutral code-native records illustration, four-language content and `?lang=en` on the English journey link. Direct opening falls back to English; valid URL lang wins; toggles update same URL, refresh retains choice, return stays the original English journey.

Status: implementation complete for pilot; execution PARTIAL / final MSG-ANCHOR INSUFFICIENT_EVIDENCE because full VI desktop visual evidence is incomplete. Full-page screenshots observed EN/zh-Hans/zh-Hant desktop and all four mobile; VI desktop hero observed. Browser screenshot timeouts are recorded, not counted as visual PASS. All four320px entry/parity/overflow checks passed. Native-market/independent/PO/live acceptance not claimed.

The old Chinese detail URL15454 now opens a different MES article and is omitted from this revision. Case collection href and frozen case snapshot are retained; source live availability not certified (web403). Frozen source and historical receipts are untouched. New questions/value bridge are qualitative reader preparation, not new customer outcome claims. No ImageGen call.

See `review-receipt.json`, `runtime-checks.json`, captured PNGs, and parent `B1-copy-v1.json`. Default B1 entry: `deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html?lang=en`. Only B1 is implemented; remaining destinations remain pending. New reader is not retrospectively covered by prior B1 offline adoption.

Docs impact reviewed: scoped trial addenda update current/README/build/readiness and owned inventory. Changes remain local unstaged/uncommitted in slice/linkedin-fdi-destination-html; not main or GitHub/live.
'''
(PACK/'B1-review/README.md').write_text(note,encoding='utf-8',newline='\n')
for doc,prefix in [('CURRENT_STATE.md',''),('README.md',''),('operations/Pre_Ad_Readiness_Plan.md','../'),('ads/linkedin/LinkedIn_Build_Pack.md','../../')]:
    path=ROOT/doc
    link=prefix+'operations/fdi-destination-html/2026-10-07/B1-review/README.md'
    add=f'> **B1 destination trial · 2026-10-07:** O1/B1 reader rebuilt offline in dedicated `slice/linkedin-fdi-destination-html`: accepted VN Leonxinx layout, four toggles vi/en/zh-Hans/zh-Hant, journey entry defaults English via `?lang=en`. Reader/entry working files only; not main integration, PO acceptance or publish. Full4mobile and EN/Chinese desktop render observed; VI desktop full render still pending after screenshot timeouts, final MSG-ANCHOR INSUFFICIENT_EVIDENCE. Historical B1 PNG/PO adoption/whole-journey verdicts retained. Old15454 detail link omitted after source mismatch; collection live availability not certified. [Trial/evidence]({link}).\n\n'
    path.write_text(add+path.read_text(encoding='utf-8-sig'),encoding='utf-8',newline='\n')
inventory=PACK/'inventory.csv'
rows=list(csv.DictReader(io.StringIO(inventory.read_text(encoding='utf-8-sig'))))
for row in rows:
    if row['Treatment']=='O1' and row['Locale']=='en':
        row['State']='B1_FOUR_LANGUAGE_TRIAL_IMPLEMENTED'
        row['Completion']='IMPLEMENTED_RENDER_REVIEW_PARTIAL'
        row['OutputRoute']='deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html?lang=en'
with inventory.open('w',encoding='utf-8',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
plan=PACK/'README.md'
text=plan.read_text(encoding='utf-8-sig')
text=text.replace('Status: PREPARATION_READY / HTML_NOT_IMPLEMENTED.', 'Status: B1_TRIAL_IMPLEMENTED / B1_RENDER_REVIEW_PARTIAL; other destinations NOT_IMPLEMENTED. See [B1 trial receipt](B1-review/README.md).')
text=text.replace('## Actionable existing destinations — all NOT DONE under this design mandate','## Actionable existing destinations — B1 trial implemented; others NOT DONE')
plan.write_text(text,encoding='utf-8',newline='\n')
print('Recorded scoped PARTIAL review, fresh source/hash binding, inventory and canonical trial addenda.')
