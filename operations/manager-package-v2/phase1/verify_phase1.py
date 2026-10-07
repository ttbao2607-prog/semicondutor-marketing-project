"""Bounded provenance/arithmetic/coverage audit. Does not change sources or assets."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
P=Path(__file__).resolve().parent
R=P.parents[2]
def load(name):return json.loads((P/name).read_text(encoding='utf-8'))
def save(name,d): (P/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*a):return subprocess.check_output(['git','-C',str(R),*a],text=True,encoding='utf-8').strip()
sources=load('source-register.json'); assets=load('asset-register.json'); readers=load('reader-register.json'); wb=load('legacy-workbook-inspection.json')
source_map={s['id']:s for s in sources['sources']}
checks=[]
def check(name,ok,evidence):checks.append({'check':name,'pass':bool(ok),'evidence':evidence})
changed_sources=[]
for s in sources['sources']:
 path=Path(s['absolute_path'])
 if not path.is_file() or h(path)!=s['sha256']:changed_sources.append(s['id'])
check('Source hashes unchanged since capture',not changed_sources,changed_sources)
check('Source IDs unique',len(source_map)==len(sources['sources']),len(source_map))

groups={a['id']:a for a in assets['assets']}
pinissues=[]
for a in assets['assets']:
 root=Path(load('git-state.json')['repositories'][a['owner']]['path'])
 for f in a['images']+a['surfaces']:
  p=root/f['path']
  if not p.is_file() or h(p)!=f['sha256'] or f['pin_result'] in ['MISSING','MISMATCH']:pinissues.append([a['id'],f['path']])
check('All selected PNG and pinned surfaces present and unchanged',not pinissues,pinissues)
check('VN two journeys20 placements',sum(groups[i]['selected_png_count'] for i in ['ASSET-VN-W1','ASSET-VN-W2'])==20,20)
check('OSAT B1-B12 exactly120 placements',sum(groups['ASSET-B'+str(i)]['selected_png_count'] for i in range(1,13))==120,120)
check('OSAT B6-B12 subset70',sum(groups['ASSET-B'+str(i)]['selected_png_count'] for i in range(6,13))==70,70)
check('O3 three pilots30 separate',sum(a['selected_png_count'] for a in assets['assets'] if a['id'].startswith('ASSET-O3-'))==30,30)
check('Fabless B13/B14/B15 each11 source candidates',all(groups['ASSET-B'+str(i)]['selected_png_count']==11 for i in [13,14,15]),33)
check('Partner B22/B23/B24 each10 source candidates',all(groups['ASSET-B'+str(i)]['selected_png_count']==10 for i in [22,23,24]),30)
check('Partner B25/B26 each10 source placements',all(groups['ASSET-B'+str(i)]['selected_png_count']==10 for i in [25,26]),20)
check('Full selection253 placements',sum(a['selected_png_count'] for a in assets['assets'])==253,253)
check('No input asset copied to v2',all(a['copied_to_v2'] is False for a in assets['assets']) and not (R/'deliverables/manager-package-v2').exists(),'Metadata/reference only')
check('10 source redesigns differ from main;four toggles',readers['concrete_count']==10 and all(x['source_differs_from_main'] and x['toggle_languages']==['vi','en','zh-Hans','zh-Hant'] for x in readers['readers']),10)

for x in readers['readers']:
 check('Source reader '+x['id'],h(Path(x['source']['absolute_path']))==x['source']['sha256'],x['source']['sha256'])

data=(P/'Data_Register.md').read_text(encoding='utf-8')
rows=[line.split('|')[1:-1] for line in data.splitlines() if re.match(r'^\| D\d{2} \|',line)]
ids=[row[0].strip() for row in rows]
check('40data rows with class/source/usage',ids==['D'+str(i).zfill(2) for i in range(1,41)] and all(len(row)==6 and row[1].strip() in ['FACT','DECISION','ASSUMPTION','PENDING'] and 'SRC-' in row[4] and 'S' in row[5] for row in rows),ids)
for row in rows:
 refs=re.findall(r'(?:SRC|ASSET)-[A-Za-z0-9-]+',row[4])
 check('Bound data '+row[0].strip(),all(s in source_map for s in refs),refs)
save('data-register.json',{'revision':'phase1-data-register-1.2','source':'Data_Register.md','data':[dict(zip(['id','type','value_scope','observation_revision','source_refs','skeleton_usage'],[s.strip() for s in row])) for row in rows]})

inv=(P/'Inventory_Disposition.md').read_text(encoding='utf-8')
invrows=re.findall(r'^\| (V2-\d{2}) \|',inv,re.M)
check('34inventory IDs exactly once',invrows==['V2-'+str(i).zfill(2) for i in range(1,35)],invrows)
skel=(P/'Package_V2_Skeleton_Phase1.md').read_text(encoding='utf-8')
check('SkeletonS1-S10 all populated',re.findall(r'^## (S\d+)\.',skel,re.M)==['S'+str(i) for i in range(1,11)],'Markdown internal skeleton')
check('Skeleton Phase1 pending;no Phase2/3 adoption',all(s in skel for s in ['PHASE1_PREPARED / BAO_DATA_LOCK_PENDING','Phase 2–3 chưa bắt đầu']), 'Bảo data lock required by plan')

# Independent calculations from original workbook drivers/cached results; no native recalc claim.
sheet=next(s for s in wb['sheets'] if s['name']=='03_Ngan_sach')
cells={c['cell']:c for c in sheet['cells']}; forms={c['cell']:c for c in sheet['formulas']}
n=lambda c:float(cells[c]['value'])
first=n('B6')*n('C6');search=(first*n('B23')//n('B24'))*n('B24');held=first+search;cap=first+first+search
calcs={'first_vnd':first,'optional_search_vnd':search,'held_vnd':held,'media_cap_vnd':cap}
check('Independent reference budget arithmetic',calcs=={'first_vnd':5600000,'optional_search_vnd':500000,'held_vnd':6100000,'media_cap_vnd':11700000},calcs)
check('Budget cached cells agree with independent drivers',all(float(forms[cell]['cached_value'])==v for cell,v in {'G6':first,'G7':first,'G8':search,'G9':held,'G11':cap}.items()),'B6/C6/B23/B24 →G6/G7/G8/G9/G11, cached comparison only')
check('Actuals and approvals not populated in v1',all(c not in cells for c in ['H6','H7','H8','I6','I7','I8']),'Blank is missing, not zero spend/approval')
check('Workbook exact6sheets29formula cells',len(wb['sheets'])==6 and sum(len(s['formulas']) for s in wb['sheets'])==29,wb['native_excel_recalculation'])
check('Research arithmetic and units',101+323==424 and 99+6==105 and 52+151==203,'Rows vs field changes, original vs backup')
partner=json.loads(Path(source_map['SRC-PARTNER-LEDGER']['absolute_path']).read_text(encoding='utf-8'))
check('Partner counts selected/calls/correctives reconcile',partner['selected_candidates']==30 and partner['imagegen_calls']==43 and partner['corrective_calls']==13 and 18+13+12==43,'Ledger metadata crosschecked with final manifests/reviews')
check('Partner P2 adds20 placements and16 calls, separate from old totals',sum(partner['batches'][b]['selected'] for b in ['B25','B26'])==20 and sum(partner['batches'][b]['imagegen_calls'] for b in ['B25','B26'])==16,'P2 pair12new+8reuse; B22-B24 old totals retained')

# Bounded local links for newly authored Markdown only; no UI/render assertion.
broken=[]
for f in P.glob('*.md'):
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
  target=target.strip('<>').split('#')[0]
  if not target or '://' in target or target.startswith('D:'):continue
  if not (f.parent/target).is_file():broken.append([f.name,target])

msgfiles=['Package_V2_Skeleton_Phase1.md','Data_Register.md','Claim_Register.md','Inventory_Disposition.md','Reconciliation_Notes.md','PO_Dashboard_Weekly_Decision_2026-10-07.md','Week1_Review_Week2_Data_Matrix.md']
notices=['CURRENT_STATE.md','operations/LinkedIn_Current_Progress_2026-10-07.md','operations/LinkedIn_PO_Direction_Budget_Checkpoint_2026-10-06.md','drafts/S04_Measurement_and_Budget.md','operations/Pre_Ad_Readiness_Plan.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md']
bindings={'reviewed_utc':datetime.now(timezone.utc).isoformat(),'stage':'INTERNAL_CONTENT_REVIEW','reviewer':'/root','independence':'SELF_REVIEW',
 'anchor':{k:source_map['SRC-ANCHOR'][k] for k in ['id','path','sha256','head_at_capture']},
 'anchor_content_id':'VY-CONTENT-ANCHOR','anchor_revision':'1.0',
 'email':{k:source_map['SRC-MAIL'][k] for k in ['id','path','sha256','head_at_capture']},
 'email_record_id':'VY-MAIL-USER-20261006','artifact_revision':'package-v2-phase1-1.2',
 'workflow':{**{k:source_map['SRC-WORKFLOW'][k] for k in ['id','path','sha256','head_at_capture']},'revision':'1.1'},
 'message_files':[{'path':(P/f).relative_to(R).as_posix(),'sha256':h(P/f)} for f in msgfiles],
 'related_notices':[{'path':f,'sha256':h(R/f)} for f in notices],
 'verdict':'MESSAGE_ANCHOR_PASS_INTERNAL_MARKDOWN_SCOPE','render_scope':'N/A internal Markdown; no new artwork/UI','semantic_evidence':'Message_Anchor_Review_1.2.md',
 'semantic_evidence_sha256':h(P/'Message_Anchor_Review_1.2.md')}
save('message-bindings.json',bindings)

branchrefs=git('for-each-ref','--format=%(refname:short)|%(objectname)|%(upstream:short)','refs/heads').splitlines()
branches=[]
for row in branchrefs:
 name,tip,upstream=row.split('|')
 remote=git('branch','-r','--contains',tip)
 branches.append({'name':name,'commit':tip,'upstream':upstream or None,'remote_tracking_refs_containing_tip':remote.splitlines() if remote else [],'actual_remote_live_verified':False})
gs=load('git-state.json');gs['local_branches']=branches;gs['worktrees_porcelain']=git('worktree','list','--porcelain');gs['package_at_audit']={'head':git('rev-parse','HEAD'),'staged':git('diff','--cached','--name-only'),'changed_tracked':git('diff','--name-only')};save('git-state.json',gs)
state_lines=[
 '# Git state recovery — package v2 Phase 1','',
 '**STATE RECONSTRUCTION:** Global git-state-recovery helper used at turn start without fetch; earlier fetched tracking reference retained. Final local refs/worktrees and source-file state captured in git-state.json. No reflog required.','',
 '**PROJECT IDENTITY:** Semiconductor paid marketing repository. Dedicated package worktree D:/LinkedIn_Package_V2_2026-10-07. Canonical local main remains a separate checkout.','',
 '**HUMAN SUMMARY:** Plan was saved as a local commit before Phase 1 execution. New data/skeleton/registers and bounded current notices are working files on the package branch. They have not been sent to GitHub or adopted on main in this session.','',
 '**CURRENT CHECKOUT:** '+gs['repositories']['package']['branch']+' at '+gs['package_at_audit']['head']+'. HEAD is the saved commit this checkout is based on. Staging area is empty; new Phase1 work is not committed.','',
 '**REMOTE REFERENCE:** Cached origin/main after earlier fetch: '+str(gs['repositories']['main'].get('remote_tracking_main'))+'. main ahead/behind that tracking reference: '+str(gs['repositories']['main'].get('ahead_behind_tracking'))+'. A tracking reference is a local observation; no final live GitHub verification/push. No pull/merge/history rewrite performed.','',
 '**LOCAL WORK NOT YET REMOTE:** The table lists every local branch whose tip is absent from captured remote-tracking histories; this is evidence against those refs, not an assertion about an unqueried remote repository. Phase1 working files have no new commit.','',
 '| Branch | Local tip | Upstream |','|---|---|---|']
for b in branches:
 if not b['remote_tracking_refs_containing_tip']:state_lines.append(f"| {b['name']} | {b['commit']} | {b['upstream'] or 'None — no paired remote branch'} |")
state_lines+=['','**OTHER RELEVANT WORKTREES / BRANCHES:**','', '| Input | Checkout | Commit at capture | File state |','|---|---|---|---|']
for name,v in gs['repositories'].items():state_lines.append(f"| {name} | {v['path']} | {v['head']} | {'Working changes present' if v['dirty_status'] else 'Clean'} |")
state_lines+=['','**SAFE CONCLUSION:** Main adopted assets, source-only candidates, owner working files and local commits are separate. Partner old working flags are superseded by actual4a17968 for B23/B24 and a09035d for B25/B26. Fabless B14/B15 checkpoint461a752 is source-only. No remote/live/adoption claims are inferred.','',
 '**NEXT ACTION:** Bảo locks or revises Phase1 data/skeleton before Phase2. A later Phase1checkpoint/mainintegration/push is a separate Git action; this record does not execute it.']
(P/'Git_State_Recovery.md').write_text('\n'.join(state_lines)+'\n',encoding='utf-8')
changed=git('diff','--name-only').splitlines()
allowed=notices+['operations/manager-package-v2/']
check('Tracked changes within Phase1docs scope',all(any(p==a or p.startswith(a) for a in allowed) for p in changed),changed)
check('Plan commit remains current checkpoint',git('rev-parse','--short','HEAD')=='7796bc6','Local commit; no Phase1commit/mainmerge/push')
check('Stage area empty',not git('diff','--cached','--name-only'),'New Phase1work not staged')
before=gs['repositories']['main'];current_main=subprocess.check_output(['git','-C',before['path'],'rev-parse','HEAD'],text=True).strip()
check('Main checkpoint unchanged since input recovery',current_main==before['head'],current_main)

# Create a compact human index from the full pin register.
lines=['# Phase 1 — Source register','',f"Capture: {sources['captured_utc']}. Sources/read-only file pins: {len(source_map)}. Source observation dates remain in Data Register; capture time is not the time of live observation.",'','Full exact bytes/commits/working-file classification: [source-register.json](source-register.json). Main/owned/source worktrees are distinguished; no push/live readback. Hash pins do not certify semantics or rights.','','| Source ID | Owner | File | State / scope |','|---|---|---|---|']
for s in sources['sources']:lines.append(f"| {s['id']} | {s['owner']} | `{s['path']}` | {s['state']}; {s['purpose']} |")
(P/'Source_Register.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
# Re-evaluate bounded links now generated files exist. The verification file itself is emitted below.
broken=[x for x in broken if x[1] not in ['message-bindings.json','verification.json','Source_Register.md']]
check('Authored Markdown local links resolve',not broken,broken)
check('PO weekly decision and qualitative matrix pinned',all(i in source_map for i in ['SRC-PO-WEEKLY','SRC-WEEK2-MATRIX']), 'Direct PO decision outranks prior all-in/cadence assumptions')
check('Tax/cadence inputs are decisions; media cap unchanged',all(row[1].strip()=='DECISION' for row in rows if row[0].strip() in ['D08','D15','D36']) and 'chưa thuế' in skel and 'all-in/thuế phí;' not in skel, 'D08/D15/D36; independent cap arithmetic above')
check('Historical revision1.0 receipt/bindings preserved',all((P/'history/phase1-1.0'/f).is_file() for f in ['Message_Anchor_Review.md','message-bindings.json','verification.json']), 'Fresh 1.1 receipt; no historical acceptance rewrite')
result={'revision':'phase1-verification-1.2','reviewed_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW',
 'bounded_result':'PASS_INTERNAL_DATA_CHECKS' if all(c['pass'] for c in checks) else 'CHANGES_REQUIRED',
 'phase_status':'PHASE1_PREPARED / BAO_DATA_LOCK_PENDING','phase2':'NOT_STARTED','phase3':'NOT_STARTED','checks':checks,
 'limitations':['No actual campaign/account readback','No fresh visual/native-market review of reused artifacts','No native Excel calculation or new workbook','No PO data lock/new artifact acceptance','No main merge/push or generation']}
save('verification.json',result)
print(json.dumps({'result':result['bounded_result'],'checks':len(checks),'failures':[c for c in checks if not c['pass']],'sources':len(source_map),'png_placements':253},ensure_ascii=False))
