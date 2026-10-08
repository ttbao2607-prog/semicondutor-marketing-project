"""Record observed final-package review. Does not grant PO or live acceptance."""
import datetime,hashlib,json,pathlib,subprocess
root=pathlib.Path(__file__).resolve().parents[3]; rec=pathlib.Path(__file__).parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
load=lambda name:json.loads((rec/name).read_text(encoding='utf-8'))
pre=load('prepared-copy.json'); gate=load('pregen-review.json'); am=load('pregen-amendment.json'); actual=load('browser-evidence.json'); files=load('final-file-manifest.json'); static=load('verification.json'); workbook=load('workbook-verification.json')
assert static['status']=='PASS_STATIC_SELECTION_AND_PORTABILITY'
assert am['builder_sha256']==sha(rec/'build_package.py')
assert gate['prepared_copy_sha256']==sha(rec/'prepared-copy.json')
assert am['anchor_sha256']==sha(root/'operations/Vy_Email_Content_Anchor.md')==gate['anchor_sha256']
assert am['email_sha256']==sha(root/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md')==gate['email_sha256']
for f in files['files']:assert sha(root/'deliverables/manager-package-v2/2026-10-07'/f['path'])==f['sha256'],f['path']
desks={x['slug']:x for x in actual['journeyEvidence']}; mobiles={x['slug']:x for x in actual['mobileJourneyEvidence']}
dr={x['slug']:x for x in actual['readerEvidence']}; mr={x['slug']:x for x in actual['mobileReaderEvidence']}
assert len(desks)==len(mobiles)==len(dr)==len(mr)==17
unit_reviews=[]; journey_reviews=[]
preg_units={(x['group'],x['unit']):x for x in gate['units']}
for g in pre['groups']:
    slug=g['slug']; desktop=desks[slug]; mobile=mobiles[slug]
    assert desktop['lastDisabled']
    assert desktop['returnUrl'].endswith('/'+slug+'/index.html') and mobile['returnUrl'].endswith('/'+slug+'/index.html')
    assert len(desktop['cards'])==10 and len(mobile['stages'])==3 and mobile['feed333']==333
    for i,(r,c) in enumerate(zip(g['rows'],desktop['cards']),1):
        assert c['loaded'] and c['position']==str(i)+' / 10' and c['caption']==r['caption'] and c['headline']==r['headline'] and c['image']==r['image'],(slug,i)
        assert c['width']==c['scrollWidth'],(slug,i)
        obs=dict(preg_units[(g['id'],i)])
        obs.update({'actual_caption':c['caption'],'actual_headline':c['headline'],'actual_image':c['image'],
                    'png_identity':'Byte-preserved approved-main selection; current hash checked, no raster transform.',
                    'actual_desktop_capture':'operations/manager-package-v2/phase3/'+slug+'-card-'+str(i).zfill(2)+'.png',
                    'desktop_css_width':c['width'],'desktop_image_loaded':c['loaded'],
                    'scope':'Fresh package surface/context review; original native-image acceptance is reused by exact bytes, not retro-certified.'})
        unit_reviews.append(obs)
    assert all(s['width']==375 and s['scrollWidth']==375 and s['imageLoaded'] for s in mobile['stages']),slug
    assert dr[slug]['width']==dr[slug]['scrollWidth'] and mr[slug]['width']==mr[slug]['scrollWidth'],slug
    assert mr[slug]['width']==375
    journey_reviews.append({'group':g['id'],'persona':g['persona'],'locale':g['locale'],'family':g['family'],
      'surfaces':['cold 1','explanation 2–6','proof 7–10','same-family case reader','local return'],
      'desktop_reader_title':dr[slug]['title'],'mobile_reader_title':mr[slug]['title'],
      'reader_observed_text':mr[slug]['text'],'actual_return':desktop['returnUrl'],'mobile_stages':mobile['stages'],
      'feed333_css_width':mobile['feed333'],'verdict':'MESSAGE_ANCHOR_PASS',
      'A7':'Same decision unit and language throughout; O3 explicitly bridges Operations records to Finance; VN Aplus is China integrated-system reference for local readiness.'})
assert len(actual['vnReaderLocaleChecks'])==6
assert not any('source-pinned' in x['text'] for x in actual['readerEvidence']+actual['mobileReaderEvidence'])
assert len(workbook['tests'])==15 and all(x['actual']==x['expected'] for x in workbook['tests'])
receipt={'artifact_revision':'package-v2-phase3-1.0','stage':'POSTGEN_ARTIFACT','note':'Post-assembly review; no new ImageGen, only unchanged approved PNG reuse.',
 'reviewed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW',
 'anchor_id':'VY-CONTENT-ANCHOR','anchor_revision':'1.0','anchor_sha256':gate['anchor_sha256'],
 'email_record_id':'VY-MAIL-USER-20261006','email_sha256':gate['email_sha256'],
 'workflow_id':'PACKAGE-V2-WORKFLOW','workflow_revision':'1.1','workflow_sha256':gate['workflow_sha256'],
 'final_manifest_sha256':sha(rec/'final-file-manifest.json'),'browser_evidence_sha256':sha(rec/'browser-evidence.json'),
 'pregen_sha256':sha(rec/'pregen-review.json'),'pregen_amendment_sha256':sha(rec/'pregen-amendment.json'),
 'unit_reviews':unit_reviews,'journey_reviews':journey_reviews,'vn_reader_additional_locales':actual['vnReaderLocaleChecks'],
 'executive_review':{
  'A1':'Proposal: PCB, substrate, components, packaging materials, precision machining; not default targeting group-global core plants.',
  'A2':'Company/functional/seniority reports; Bảo picks relevant initial group; no global-enterprise purchase authority inferred.',
  'A3':'Distinct VN readiness and FDI operations; name voice Bảo/Vy in proposal and mail, buyer voice preserved in existing artifacts.',
  'A4':'FDI time, coordination, ownership and risk value remains implicit; no new quantified ROI requirement.',
  'A5':'ERP readiness supports records/process/data preparation, not guaranteed admission or audit pass.',
  'A6':'Named China integrated cases scoped in readers; no local ERP equipment-control guarantee.',
  'A7':'Single image → new-ad interactors when eligible → explanation/proof → same reader → return; simulation not forced delivery order.',
  'budget':'11.7m before tax;5.6m initial+6.1m held inside cap;next LinkedIn≤5.6m/Search≤0.5m. No additional week-2 tranche.',
  'cadence':'Week1 plan/end-week review/week2 from matrix; modular swaps and primary/backup audience remain Bảo execution.',
  'questions':'Exactly 3 investment feedback points, no stored answers or execution permissions. Vy reviews/aggregates for leadership.',
  'workbook':'2 visible tabs, blank actuals, 15 passing recalculation/blank/zero/partial-data tests; all sheets visually inspected. Native Excel not tested.',
  'payload':'213 deliverable files; no internal registers, QA, raw manifests, builder, workbook diagnostic, secret/private audience/account records or ZIP.'},
 'proof_ledger':[
  {'case':'Aplus / 常州欣盛半导体技术股份有限公司','geography':'China','solution':'DigiHua iMES + TOP GP','metric':'3 months whole-project go-live in week2 only','scope':'No local audit/admission/timetable guarantee.'},
  {'case':'江苏中科智芯集成科技有限公司','geography':'China','solution':'Integrated Digiwin ERP+iMES; MES/SPC/ECN/linked records/exception workflows','metric':'15→5-day month-close in O3 only','scope':'Reported named case result; no ERP-only/local deployment forecast.'}],
 'limitations':['Offline package review only; no live campaign, delivery, rights, instrumentation or new PO asset acceptance.',
                'Some documented AX captures are scaled. Exact PNG identity and prior approved selection preserved; no fresh native-market/artwork readability certification.',
                'Browser download and native Excel were not certified; XLSX export/XML readback/engine checks completed.',
                'Historical original viewers/receipts and technical limitations are not upgraded by package wrapper tests.'],
 'verdict':'MESSAGE_ANCHOR_PASS','package_status':'PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING'}
(rec/'post-assembly-review.json').write_text(json.dumps(receipt,ensure_ascii=False,indent=2),encoding='utf-8')
(rec/'Review_Receipt.md').write_text('''# Phase 3 final candidate review · 2026-10-07

Status: **PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING**. Root SELF_REVIEW. Bảo authorized proceeding from Phase 2 and named Vy as recipient; no budget response from Vy or final PO acceptance is fabricated.

Delivery is the ordinary [2026-10-07 folder](../../../deliverables/manager-package-v2/2026-10-07/BAT_DAU.html). Proposal/mail use names; the three investment feedback points, 11.7m before-tax cap, dashboard/accounting role and weekly cadence are preserved. Two VN and fifteen OSAT FDI journeys contain 170 unchanged approved-main PNG placements and seventeen local case readers. Fabless/Partner source candidates, failed/alternate/corrective directories and source-only redesigned FDI readers are excluded.

Evidence: [final selection](selected-provenance.json), [213-file binding](final-file-manifest.json), [static checks](verification.json), [actual browser observations](browser-evidence.json), [fresh per-unit/per-journey anchor review](post-assembly-review.json), [workbook engine checks](workbook-verification.json) and [bounded corrections](Review_Amendment.md). Actual desktop170 cards were observed loaded; mobile375 tested all17 journeys at3 stages, reader/return and feed333. Both VN readers'3language states were also checked on mobile. Every workbook tab was rendered and read;15 behavior checks passed, all sample inputs removed, and error scan matched0 entries.

Scope: actual package wrappers/reader routes/content and export were reviewed. Byte-preserved source PNG acceptance is reused; no new native artwork, independent/bilingual-market certification, paid-rights or live readiness is claimed. Some AX captures are scaled; original-viewer limitations remain historical/current at their own scope. Browser download/native Excel operation is unverified; local XLSX export/XML and Artifact Tool recalculation were checked.

Docs impact reviewed: CURRENT_STATE, DOCS_IMPACT_MAP, current LinkedIn progress, package workflow/plan/README and Phase1/2 records. Current package status updated only in this checkout; business/anchor/budget/runtime truth unchanged. Main, other source worktrees, Phase1/2 receipts, frozen core/process and adapter DEVELOPING/NOT_FROZEN were not modified. Phase2 is preserved as historical draft; Phase3 is the current delivery candidate. Local files only, not committed/main/GitHub. No email sent.
''',encoding='utf-8')
print(json.dumps({'status':receipt['package_status'],'message_anchor':receipt['verdict'],'units':len(unit_reviews),'journeys':len(journey_reviews),'files':len(files['files']),'workbook_behavior_checks':len(workbook['tests'])},ensure_ascii=False))
