"""One-off Phase 1 source/selection capture. No account access or asset mutation."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, struct, subprocess, zipfile
import xml.etree.ElementTree as ET

OUT = Path(__file__).resolve().parent
ROOTS = {
 'package': OUT.parents[2],
 'main': Path('D:/Digiwin_Semiconducter_Workspace'),
 'company': Path('D:/optimize-awareness-LinkedIn-adcopy'),
 'backup': Path('D:/Digiwin_LinkedIn_Contingency_Audience'),
 'fabless': Path('D:/LinkedIn_Safe_Fabless_2026-10-07'),
 'partner': Path('D:/LinkedIn_Safe_Partner_2026-10-07'),
 'readers': Path('D:/LinkedIn_FDI_Destination_HTML_2026-10-07'),
 'osat': Path('D:/LinkedIn_Safe_OSAT_2026-10-07'),
}
def git(root,*args,raw=False):
 p=subprocess.run(['git','-C',str(root),*args],capture_output=True)
 if p.returncode: return None
 return p.stdout if raw else p.stdout.decode('utf-8',errors='replace').strip()
def sha(b): return hashlib.sha256(b).hexdigest()
def read(p): return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,data): (OUT/name).write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
STAMP = datetime.now(timezone.utc).isoformat()
repos={}
for name,root in ROOTS.items():
 repos[name]={'path':root.as_posix(),'head':git(root,'rev-parse','HEAD'),'branch':git(root,'branch','--show-current'),
              'dirty_status':git(root,'status','--short'), 'captured_utc':STAMP}
repos['main']['remote_tracking_main']=git(ROOTS['main'],'rev-parse','refs/remotes/origin/main')
repos['main']['ahead_behind_tracking']=git(ROOTS['main'],'rev-list','--left-right','--count','main...origin/main')
save('git-state.json',{'date':'2026-10-07','remote_note':'Tracking refs after earlier recovery fetch; not a live GitHub verification or push.','repositories':repos})

sources=[]
def pin(sid,owner,rel,purpose):
 p=ROOTS[owner]/rel
 assert p.is_file(), f'Missing {owner}/{rel}'
 b=p.read_bytes(); blob=git(ROOTS[owner],'show','HEAD:'+rel,raw=True)
 rec={'id':sid,'owner':owner,'path':rel,'absolute_path':p.as_posix(),'head_at_capture':repos[owner]['head'],
      'captured_utc':STAMP,'bytes':len(b),'sha256':sha(b),'purpose':purpose,
      'state':'COMMITTED_BYTES' if blob==b else 'COMMITTED_NEWLINE_ONLY' if blob is not None and blob.replace(b'\r\n',b'\n')==b.replace(b'\r\n',b'\n') else 'WORKING_FILE_DIFF' if blob is not None else 'UNTRACKED_WORKING_FILE',
      'git_blob_sha256':sha(blob) if blob is not None else None,
      'last_path_commit':git(ROOTS[owner],'log','-1','--format=%H','--',rel)}
 sources.append(rec);return rec

specs=[
 ('SRC-WORKFLOW','package','operations/manager-package-v2/Package_V2_Workflow_Anchor_2026-10-07.md','PO autonomy and three phases'),
 ('SRC-PLAN','package','operations/manager-package-v2/Package_V2_Three_Phase_Plan_2026-10-07.md','Phase 1 execution contract'),
 ('SRC-INVENTORY','package','operations/manager-package-v2/Package_V2_Content_Inventory_2026-10-07.md','34-item scope'),
 ('SRC-ANCHOR','main','operations/Vy_Email_Content_Anchor.md','VY-CONTENT-ANCHOR v1.0; A1-A7'),
 ('SRC-MAIL','main','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md','Original supplied body; dated record, no mailbox access'),
 ('SRC-PROGRESS','main','operations/LinkedIn_Current_Progress_2026-10-07.md','Main reconciliation baseline; active lanes refreshed below'),
 ('SRC-CURRENT','main','CURRENT_STATE.md','Canonical entrypoint'),
 ('SRC-DOCMAP','main','DOCS_IMPACT_MAP.md','Documentation impact'),
 ('SRC-KICKOFF','main','Semiconductor_Work_Kickoff.md','Source priority and project scope'),
 ('SRC-BUDGET','main','operations/LinkedIn_PO_Direction_Budget_Checkpoint_2026-10-06.md','Current media cap and Single image route; later progress supersedes creative status'),
 ('SRC-S01','main','drafts/S01_Proof_and_Message.md','Proof/message and scope'),
 ('SRC-S04','main','drafts/S04_Measurement_and_Budget.md','Metric definitions; top current notices supersede old envelope and schedule'),
 ('SRC-TRACKING','main','tracking/Semiconductor_Tracking_Contract.md','Existing production scoped QA and event ownership'),
 ('SRC-READINESS','main','operations/Pre_Ad_Readiness_Plan.md','Current operational handoff; historical bodies remain revision-bound'),
 ('SRC-RMK','main','operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md','New-ad cohort collection contract; old Carousel route historical'),
 ('SRC-SEARCH','main','ads/google/Google_Search_Build_Sheet.md','Keyword/negative/brand structure'),
 ('SRC-PLANNER','main','drafts/S02_Google_Search_Research.md','Historical scoped Planner results; no demand-zero inference'),
 ('SRC-RIGHTS','main','operations/Public_Source_Register.md','Existing approved VI cases/translations vs additional claims/imagery'),
 ('SRC-COMPANY','company','operations/linkedin-closeout/2026-10-05/STATE.md','Original424 research completed, submitted once, pending mapping/reach'),
 ('SRC-COMPANY-RESULT','company','operations/linkedin-closeout/2026-10-05/slice-a/FULL_MATCHING_RESEARCH_RESULT_20261006.md','424-row/101-row/105-field integrity and readback'),
 ('SRC-BACKUP','backup','operations/LinkedIn_Contingency_R5_PostMatch_Check_2026-10-07.md','Ready summary vs Details0, exact unsaved estimates'),
 ('SRC-BACKUP-UPLOAD','backup','operations/LinkedIn_Contingency_R5_52_Upload_2026-10-07.md','Single upload and Master203 observation'),
 ('SRC-VN-CLOSEOUT','main','operations/linkedin-vn-journey-rebuild/2026-10-06/Creative_Closeout_and_Week2_Swap_Runbook_2026-10-07.md','Two accepted VN journeys; Aplus claim and swap'),
 ('SRC-VN-W1','main','operations/linkedin-vn-journey-rebuild/2026-10-06/journey-v3/caption-context-v1/selected-manifest.json','Week1 selected image provenance; acceptance supplied by later closeout'),
 ('SRC-VN-W2','main','operations/linkedin-vn-journey-rebuild/2026-10-06/week2-main-integration/selection.json','Week2 PO accepted selection; case HTML later superseded by approved readers'),
 ('SRC-VN-READERS','main','operations/linkedin-vn-journey-rebuild/2026-10-06/ldp-value-main-integration/PO_Selection.json','Current two 3-language readers mapping'),
 ('SRC-OSAT-CLOSEOUT','main','operations/linkedin-safe-batches/parallel-osat-2026-10-07/B10-B12-main-integration/approved-selected-evidence.json','OSAT completion70 B6-B12; final30 selection'),
 ('SRC-FABLESS-LEDGER','fabless','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/ledger.json','B14/B15 local checkpoint461a752; old working flags reconciled with Git; full mobile/render gate pending'),
 ('SRC-FABLESS-B13-REVIEW','fabless','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5/postgen-review-capture-reconciled.json','Render gate scope/pending'),
 ('SRC-FABLESS-B14','fabless','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/B14-zh-Hans-f1-v1/attempt-ledger.json','13 attempts incl2 blank-paper corrections; working native reviews'),
 ('SRC-FABLESS-B15','fabless','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/B15-zh-Hant-f1-v1/attempt-ledger.json','12 attempts incl1category correction; working native reviews'),
 ('SRC-PARTNER-LEDGER','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/ledger.json','30 selected/43 calls; committed flag stale after checkpoint'),
 ('SRC-PARTNER-ANCHOR','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/partner-ldp-content-anchor-v1.md','Industrial supplier and approved LDP proof scope'),
 ('SRC-PARTNER-B22','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B22-en-p1-v1/supplier-v3/postgen-review-v7.json','Selected v7 review actual434/feed333/desktop'),
 ('SRC-PARTNER-B23','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B23-zh-Hans-p1-v1/postgen-review-final-v1.json','Final scoped review; no PO asset acceptance'),
 ('SRC-PARTNER-B24','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B24-zh-Hant-p1-v1/postgen-review-final-v1.json','Final scoped review; no PO asset acceptance'),
 ('SRC-READERS-INVENTORY','readers','operations/fdi-destination-html/2026-10-07/inventory.csv','10concrete four-language readers and25conditional rows'),
 ('SRC-READERS-STATUS','readers','operations/fdi-destination-html/2026-10-07/README.md','PO offline checkpoint approval, source-only'),
 ('SRC-LEGACY-STATUS','company','operations/manager-package/2026-10-06/linkedin-sync/README.md','Old v6 topology/limitations; not current data'),
 ('SRC-LEGACY-PLAN','company','deliverables/manager-package/2026-10-05/01_Bao_cao/KE_HOACH_QUAN_LY_VA_TRIEN_KHAI_CHIEN_DICH.md','Legacy plan/demo/library relationships'),
 ('SRC-LEGACY-BUDGET','company','deliverables/manager-package/2026-10-05/01_Bao_cao/DE_XUAT_NGAN_SACH_VA_CAC_QUYET_DINH_CAN_PHE_DUYET.md','Reference pacing rationale; not re-adopted allocation'),
 ('SRC-LEGACY-QUESTIONS','company','deliverables/manager-package/2026-10-05/01_Bao_cao/BO_CAU_HOI_QUYET_DINH_CAN_THONG_NHAT.md','22questions historical; no carry-over answers/engine'),
 ('SRC-LEGACY-WORKBOOK','company','deliverables/manager-package/2026-10-05/04_Theo_doi/Theo_doi_chien_dich.xlsx','Read-only structure/formula snapshot; actuals not populated'),
]
for spec in specs: pin(*spec)
pin('SRC-PO-WEEKLY','package','operations/manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md','Direct PO decision: pre-tax dashboard budget, week1 review, week2 data-based swaps')
pin('SRC-WEEK2-MATRIX','package','operations/manager-package-v2/phase1/Week1_Review_Week2_Data_Matrix.md','Internal qualitative review/action matrix; not observed delivery or numeric thresholds')
for bn in ['B25-en-p2-v1','B26-zh-Hans-p2-v1']:
 pin('SRC-PARTNER-'+bn[:3],'partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/'+bn+'/postgen-review-final-v1.json','P2 factory IT scoped source SELF_REVIEW; local checkpointa09035d, not PO asset acceptance')
pin('SRC-PARTNER-P2-CLOSEOUT','partner','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B25-B26-closeout-report.md','20selected=12new+8reuse;16calls; old working-file text reconciled with actual Git')
for bn in ['B14-zh-Hans-f1-v1','B15-zh-Hant-f1-v1']:
 pin('SRC-FABLESS-'+bn[:3]+'-REVIEW','fabless','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/'+bn+'/postgen-review.json','Current selected native/feed/main SELF_REVIEW; full mobile gate pending')

assets=[]; warnings=[]
def verify_file(owner,rel,expected=None):
 p=ROOTS[owner]/rel
 if not p.is_file(): return {'path':rel,'exists':False,'pin_result':'MISSING'}
 b=p.read_bytes(); h=sha(b)
 match='MATCH' if h==expected else 'NO_EXPECTED_HASH' if expected is None else 'MISMATCH'
 if expected and h!=expected and sha(b.replace(b'\r\n',b'\n'))==expected: match='NEWLINE_ONLY_LF_PIN'
 record={'path':rel,'exists':True,'bytes':len(b),'sha256':h,'expected_sha256':expected,'pin_result':match}
 if p.suffix.lower()=='.png':
  assert b[:8]==b'\x89PNG\r\n\x1a\n', rel
  record['dimensions']=list(struct.unpack('>II',b[16:24]))
 return record
def collect_manifest(sid,owner,rel,segment,locale,treatment,adoption,authority):
 pin(sid,owner,rel,'Selected candidate provenance, not global acceptance')
 m=read(ROOTS[owner]/rel); entries=m.get('artwork',m.get('files',m.get('active_selected',m.get('selected',[]))))
 checked=[]
 for e in entries:
  if 'artwork' in m: target=e
  elif 'files' in m: target={'path':(Path(rel).parent/e['selected_image']).as_posix(),'sha256':e['sha256']}
  elif 'active_selected' in m: target=e['asset']
  else:
   target=e.get('demo_asset',e.get('native'))
   if target and target['path'].startswith('operations/'):
    target={**target,'path':('deliverables/linkedin-vn-journey/2026-10-06-v3/assets/'+Path(target['path']).name)}
  v=verify_file(owner,target['path'],target.get('sha256'));v['card_id']=e.get('card_id')
  checked.append(v)
 surfaces=[]
 folder=Path(rel).parent if rel.startswith('deliverables/') else Path('deliverables/linkedin-vn-journey/2026-10-06-v3' if sid=='ASSET-VN-W1' else 'deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2')
 for name,key in [('index.html','viewer_sha256'),('case-reader.html','reader_sha256'),('case-aplus.html','reader_sha256'),('selected-copy.json','copy_sha256'),('selected-prompts.json','prompts_sha256')]:
  if (ROOTS[owner]/folder/name).is_file(): surfaces.append(verify_file(owner,(folder/name).as_posix(),m.get(key)))
 assets.append({'id':sid,'owner':owner,'manifest_path':rel,'manifest_revision':m.get('revision'),
  'manifest_recorded_status':m.get('status',m.get('current_status',m.get('artifact_verdict'))),
  'segment':segment,'locale':locale,'treatment':treatment,'adoption':adoption,'acceptance_source':authority,
  'selected_png_count':len(checked),'images':checked,'surfaces':surfaces,'copied_to_v2':False})

collect_manifest('ASSET-VN-W1','main',specs[23][2],'VN_DOMESTIC','vi-VN','IC700/Aplus week1','MAIN_PO_OFFLINE_ADOPTED','SRC-VN-CLOSEOUT + SRC-VN-READERS; manifest PO_PENDING is historical')
collect_manifest('ASSET-VN-W2','main',specs[24][2],'VN_DOMESTIC','vi-VN','Aplus week2 time','MAIN_PO_OFFLINE_ADOPTED','SRC-VN-CLOSEOUT + SRC-VN-READERS')
for mf in sorted(ROOTS['main'].glob('deliverables/linkedin-safe-batches/**/manifest.json')):
 bn=mf.parent.name; match=re.match(r'B(\d+)-',bn)
 if match and 1<=int(match[1])<=12:
  locale='zh-Hans' if 'zh-Hans' in bn else 'zh-Hant' if 'zh-Hant' in bn else 'en'
  collect_manifest('ASSET-'+bn.split('-')[0],'main',mf.relative_to(ROOTS['main']).as_posix(),'FDI',locale,bn.split(locale+'-')[-1],'MAIN_PO_OFFLINE_ADOPTED','SRC-PROGRESS + batch selective integration receipt; technical status separate')
for bn in ['B13-en-f1-v5','B14-zh-Hans-f1-v1','B15-zh-Hant-f1-v2']:
 collect_manifest('ASSET-'+bn.split('-')[0],'fabless','deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/'+bn+'/manifest.json','FDI','zh-Hans' if 'Hans' in bn else 'zh-Hant' if 'Hant' in bn else 'en','F1','SOURCE_REVIEW_DRAFT_RENDER_PENDING','SRC-FABLESS-LEDGER + selected reviews; B14/B15 checkpoint local461a752; no final render closeout')
for bn in ['B22-en-p1-v1/supplier-v7','B23-zh-Hans-p1-v1','B24-zh-Hant-p1-v1']:
 collect_manifest('ASSET-'+bn.split('-')[0],'partner','deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/'+bn+'/selected-origin-manifest.json','FDI','zh-Hans' if 'Hans' in bn else 'zh-Hant' if 'Hant' in bn else 'en','P1 industrial supplier','SOURCE_SCOPED_ROOT_REVIEW_PO_ASSET_PENDING','SRC-PARTNER-'+bn[:3]+'; Git4a17968 supersedes old uncommitted text')
for bn in ['B25-en-p2-v1','B26-zh-Hans-p2-v1']:
 collect_manifest('ASSET-'+bn.split('-')[0],'partner','deliverables/linkedin-safe-batches/parallel-partner-2026-10-07/'+bn+'/selected-origin-manifest.json','FDI','zh-Hans' if 'Hans' in bn else 'en','P2 industrial supplier factory IT/record ownership','SOURCE_SCOPED_ROOT_REVIEW_PO_ASSET_PENDING','SRC-PARTNER-'+bn[:3]+' + SRC-PARTNER-P2-CLOSEOUT; Git a09035d supersedes old uncommitted text')

pin('SRC-O3-ADOPTION','main','operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/manifest.json','PO accepted selected candidate1/candidate3')
pin('SRC-O3-HANS-ADOPTION','main','operations/linkedin-locale-dogfood/2026-10-06/candidate2-main-integration/selection.json','PO selected candidate2 main adoption')
for bn in ['en-osat-candidate1-v4','zh-Hans-osat-candidate2-v2','zh-Hant-osat-candidate3-v1']:
 folder=Path('deliverables/linkedin-locale-dogfood/2026-10-06')/bn
 rel=(folder/'journey.json').as_posix();sid='ASSET-O3-'+bn.split('-osat')[0]
 pin(sid,'main',rel,'O3 selected main journey provenance')
 m=read(ROOTS['main']/rel)
 images=[{**verify_file('main',(folder/r['image']).as_posix(),r['sha256']),'card_id':r.get('card_id',r.get('copy',{}).get('card_id',str(r.get('index'))))} for r in m['rows']]
 assets.append({'id':sid,'owner':'main','manifest_path':rel,'manifest_revision':m.get('revision'),
  'segment':'FDI','locale':bn.split('-osat')[0],'treatment':'O3 Operations-to-Finance records bridge',
  'adoption':'MAIN_PO_OFFLINE_ADOPTED','acceptance_source':'SRC-O3-ADOPTION / SRC-O3-HANS-ADOPTION; historical technical findings separate',
  'selected_png_count':len(images),'images':images,'surfaces':[verify_file('main',(folder/n).as_posix()) for n in ['index.html','case-reader.html']],'copied_to_v2':False})

reader_rows=[]
with (ROOTS['readers']/specs[36][2]).open(encoding='utf-8-sig',newline='') as f:
 for row in csv.DictReader(f):
  if row['Completion']!='PO_APPROVED_OFFLINE_CHECKPOINT':continue
  rel=row['OutputRoute'].split('?')[0]
  sid='HTML-'+row['Treatment']+'-'+row['Locale']
  rec=pin(sid,'readers',rel,'Four-language redesigned destination, PO offline source checkpoint only')
  current=verify_file('main',rel)
  reader_rows.append({'id':sid,'treatment':row['Treatment'],'incoming_locale':row['Locale'],'toggle_languages':row['RequiredToggleLanguages'].split('|'),
   'source':rec,'main_revision':current,'source_differs_from_main':rec['sha256']!=current.get('sha256'),
   'adoption':'SOURCE_PO_OFFLINE_CHECKPOINT_NOT_MAIN','same_case_photo_paid_rights':'Not inferred from URL/public source or offline design approval'})
save('reader-register.json',{'readers':reader_rows,'concrete_count':len(reader_rows),'conditional_inventory_rows':25,'note':'Conditional rows are coverage/intake slots, not mandatory output count; no reader copy/adoption in v2.'})

# Pin receipts for already-adopted OSAT batches; do not import old attempts.
for p in sorted(ROOTS['main'].glob('operations/linkedin-safe-batches/**/approved-selected-evidence.json')):
 rel=p.relative_to(ROOTS['main']).as_posix()
 if rel!=specs[26][2]: pin('SRC-ADOPTION-'+p.parent.name,'main',rel,'PO selected integration scope and technical limitations')

for owner in ['fabless']:
 for bn in ['B14-zh-Hans-f1-v1','B15-zh-Hant-f1-v1']:
  d=read(ROOTS[owner]/('operations/linkedin-safe-batches/parallel-fabless-2026-10-07/'+bn+'/attempt-ledger.json'))
  warnings.append({'batch':bn,'attempt_count':len(d['attempts']),
    'correctives':[{'card':x['card_id'],'observations':x['observations'],'rendered':x.get('rendered')} for x in d['attempts'] if x.get('kind')=='corrective'],
    'meaning':'Native finding closure observed in owner record; final rendered/whole-journey review not inferred'})

# Read-only XLSX structure/formulas. Preserve blanks; no engine/export/recalculation claim.
wbpath=ROOTS['company']/specs[-1][2]
ns={'m':'http://schemas.openxmlformats.org/spreadsheetml/2006/main','r':'http://schemas.openxmlformats.org/officeDocument/2006/relationships'}
workbook={'source_id':'SRC-LEGACY-WORKBOOK','analysis':'READ_ONLY_ZIP_XML_EXTRACTION','native_excel_recalculation':'NOT_RUN','sheets':[]}
with zipfile.ZipFile(wbpath) as z:
 shared=[''.join(si.itertext()) for si in ET.fromstring(z.read('xl/sharedStrings.xml'))] if 'xl/sharedStrings.xml' in z.namelist() else []
 rels={el.attrib['Id']:el.attrib['Target'] for el in ET.fromstring(z.read('xl/_rels/workbook.xml.rels'))}
 for s in ET.fromstring(z.read('xl/workbook.xml')).find('m:sheets',ns):
  target=rels[s.attrib['{'+ns['r']+'}id']];target=target.lstrip('/') if target.startswith('/') else 'xl/'+target
  tree=ET.fromstring(z.read(target));cells=[];formulas=[]
  for c in tree.findall('.//m:c',ns):
   v=c.find('m:v',ns);f=c.find('m:f',ns);inline=c.find('m:is',ns)
   value=v.text if v is not None else ''.join(inline.itertext()) if inline is not None else None
   if c.attrib.get('t')=='s' and value is not None:value=shared[int(value)]
   if f is not None:formulas.append({'cell':c.attrib['r'],'formula':f.text,'cached_value':value})
   if value is not None:cells.append({'cell':c.attrib['r'],'value':value,'type':c.attrib.get('t','n')})
  dimension=tree.find('m:dimension',ns)
  workbook['sheets'].append({'name':s.attrib['name'],'dimension':dimension.attrib.get('ref') if dimension is not None else None,'cells':cells,'formulas':formulas})
save('legacy-workbook-inspection.json',workbook)
save('source-register.json',{'revision':'phase1-source-register-1.0','captured_utc':STAMP,'source_classification':'Repository evidence only; dated observations, no new live readback','sources':sources})
save('asset-register.json',{'revision':'phase1-asset-register-1.0','captured_utc':STAMP,'assets':assets,'active_lane_observations':warnings,
 'scope':'PNG bytes/dimensions and selected pins; no fresh visual, locale, native-market, paid-rights or whole-journey certification. No assets copied.'})
bad=[{'asset':a['id'],**i} for a in assets for i in a['images']+a['surfaces'] if i['pin_result'] in ['MISSING','MISMATCH']]
save('input-checks.json',{'source_count':len(sources),'selection_groups':len(assets),'png_count':sum(a['selected_png_count'] for a in assets),'pin_issues':bad})
print(json.dumps({'sources':len(sources),'groups':len(assets),'pngs':sum(a['selected_png_count'] for a in assets),'pin_issues':bad,'workbook_sheets':[(s['name'],len(s['formulas'])) for s in workbook['sheets']]},ensure_ascii=False))
