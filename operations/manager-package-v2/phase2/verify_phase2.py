"""One-off Phase 2 evidence checks; semantic verdict comes from actual reading."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,subprocess
P=Path(__file__).resolve().parent
R=P.parents[2]
BASE='4030d40d727668918bf079fd730d2071268a9004'
EXEC='deliverables/manager-package-v2/phase2/De_xuat_dau_tu_paid_ads.md'
def git(*args):return subprocess.check_output(['git','-C',str(R),*args]).decode('utf-8').strip()
def blob(rel):return subprocess.check_output(['git','-C',str(R),'show',BASE+':'+rel])
def sha(b):return hashlib.sha256(b).hexdigest()
def read(rel):return (R/rel).read_text(encoding='utf-8')
def save(name,d): (P/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
checks=[]
def check(name,ok,evidence):checks.append({'check':name,'pass':bool(ok),'evidence':evidence})
data=json.loads(blob('operations/manager-package-v2/phase1/data-register.json'))
d={x['id']:x for x in data['data']}
executive=read(EXEC)
split=read('operations/manager-package-v2/phase2/Content_Split_Register.md')
routing=read('operations/manager-package-v2/phase2/Data_Routing_and_Source_Mapping.md')
receipt=read('operations/manager-package-v2/phase2/Review_Receipt.md')
check('Baseline commit is current local checkpoint',git('rev-parse','HEAD')==BASE,BASE)
check('Phase 1 files preserved',not git('diff','--name-only',BASE,'--','operations/manager-package-v2/phase1'),'No rewrite of historical inputs/receipts')
check('All 34 inventory items routed exactly once',re.findall(r'^\| (V2-\d{2}) \|',split,re.M)==['V2-'+str(i).zfill(2) for i in range(1,35)],'Content split including DROP_DEFAULT items')
check('Skeleton S1-S10 covered',all(re.search(r'^\| S'+str(i)+r'\b',split,re.M) for i in range(1,11)),'Every source section has executive/internal disposition')
check('40 baseline data rows routed exactly once',re.findall(r'^\| (D\d{2}) \|',routing,re.M)==list(d),'Routing preserves all original records')
check('Three questions each with proposal and choices',len(re.findall(r'^### [123]\. ',executive,re.M))==3 and executive.count('Đề xuất của Bảo:')==3 and executive.count('Phản hồi:')==3 and executive.count('?')==3,'No other question/control in the business file')
amount=lambda s:int(re.search(r'\d[\d.]*',s).group().replace('.',''))
rows=[x.split('|')[1:-1] for x in executive.splitlines() if x.startswith('|')]
budget={row[0].strip('* ') : amount(row[1]) for row in rows if ' đồng' in row[1]}
expected={k:amount(d[i]['value_scope']) for k,i in [('Đợt LinkedIn đầu','D09'),('LinkedIn tiếp theo','D10'),('Search tùy chọn','D11'),('Tổng','D08')]}
check('Executive budget matches baseline units/amounts',budget==expected,budget)
check('Cap arithmetic and held portion',budget.get('Tổng')==sum(v for k,v in budget.items() if k!='Tổng') and budget.get('LinkedIn tiếp theo',0)+budget.get('Search tùy chọn',0)==amount(d['D12']['value_scope']),'5.6+5.6+0.5=11.7; held6.1 included')
check('Pre-tax/dashboard basis retained','chưa thuế' in executive and 'Bảo quản lý số tiền trên dashboard' in executive,'Accounting remains separate; no new all-in requirement')
check('Weekly cadence is method, not another approval question','Tuần 1 chạy đúng plan, review cuối tuần; tuần 2 quyết định theo data matrix.' in executive and 'Bảo điều chỉnh theo dữ liệu trong trần được duyệt.' in executive,'Semantic review confirms decisions remain with Bao')
files=[x.relative_to(R).as_posix() for x in (R/'deliverables/manager-package-v2').rglob('*') if x.is_file()]
check('Actual deliverable payload is only business Markdown',files==[EXEC],files)
leaks=re.findall(r'(?i)(?:SELF_REVIEW|INSUFFICIENT_EVIDENCE|DEVELOPING|NOT_FROZEN|SHA256|4030d40|git status|SCRIPT_REVIEW_PASS|\.json\b|operations/|D:/|<!--|<script|[a-f0-9]{64})',executive)
check('No operator payload or integrity markers in executive',not leaks,leaks)
check('Source assumptions presented as proposal',executive.count('Đề xuất của Bảo:')==3 and 'EXECUTIVE_PROPOSAL' in routing,'D09-D11/D34 classification retained in mapping, not silently promoted')
check('Business consequence of reach/data uncertainty preserved','Quy mô tệp sau lọc ảnh hưởng phạm vi thử ban đầu.' in executive and 'Khi dữ liệu mỏng' in executive,'No numeric audience forecast or automatic fail')
check('Anchor semantic review is fresh and self-declared','MESSAGE_ANCHOR_PASS' in receipt and 'SELF_REVIEW' in receipt and 'package-v2-phase2-1.0' in receipt,'Actual content review; no independent/native/artwork acceptance')
anchor=json.loads(blob('operations/manager-package-v2/phase1/message-bindings.json'))
for name in ['anchor','email','workflow']:
 x=anchor[name]
 check(name+' current bytes match source used',sha((R/x['path']).read_bytes())==x['sha256'],x['sha256'])
broken=[]
for f in [R/EXEC,*P.glob('*.md')]:
 for target in re.findall(r'\]\(([^)]+)\)',f.read_text(encoding='utf-8')):
  target=target.strip('<>').split('#')[0]
  # These two outputs are emitted later in this same invocation.
  if f.parent==P and target in ['bindings.json','verification.json']:continue
  if target and '://' not in target and not target.startswith('D:') and not (f.parent/target).is_file():broken.append([f.name,target])
check('Current Markdown links resolve',not broken,broken)
changed=git('diff','--name-only').splitlines()
allowed=['CURRENT_STATE.md','operations/LinkedIn_Current_Progress_2026-10-07.md','operations/manager-package-v2/README.md','operations/manager-package-v2/Package_V2_Three_Phase_Plan_2026-10-07.md']
check('Tracked changes in owned docs scope',all(p in allowed for p in changed),changed)
check('Staging area empty after checkpoint',not git('diff','--cached','--name-only'),'Phase 2 working files not committed')
main=subprocess.check_output(['git','-C','D:/Digiwin_Semiconducter_Workspace','rev-parse','HEAD']).decode().strip()
check('Canonical main unchanged since recovery',main=='196f26b9f3064fca8fe6b3b50b5707c2b54b65af',main)
reviewed=['Content_Split_Register.md','Data_Routing_and_Source_Mapping.md','Bao_Decision_Action_Register.md','Authority_and_Execution_Contract.md','README.md','Review_Receipt.md']
bindings={'artifact_revision':'package-v2-phase2-1.0','stage':'INTERNAL_CONTENT_REVIEW','reviewed_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW','baseline_commit':BASE,
 'anchor':anchor['anchor'],'anchor_content_id':anchor['anchor_content_id'],'anchor_revision':anchor['anchor_revision'],'email':anchor['email'],'workflow':anchor['workflow'],
 'executive':{'path':EXEC,'sha256':sha((R/EXEC).read_bytes())},'internal_files':[{'path':(P/f).relative_to(R).as_posix(),'sha256':sha((P/f).read_bytes())} for f in reviewed],
 'source_files':[{'path':p,'sha256':sha(blob(p)),'commit':BASE} for p in ['operations/manager-package-v2/phase1/data-register.json','operations/manager-package-v2/phase1/source-register.json','operations/manager-package-v2/phase1/Package_V2_Skeleton_Phase1.md','operations/manager-package-v2/phase1/Claim_Register.md','operations/manager-package-v2/phase1/Inventory_Disposition.md','operations/manager-package-v2/phase1/Week1_Review_Week2_Data_Matrix.md']],
 'related_notices':[{'path':p,'sha256':sha((R/p).read_bytes())} for p in allowed],
 'question_state':'PROPOSED_UNANSWERED','render_scope':'N/A internal Markdown; no new artwork/UI','semantic_evidence':'Review_Receipt.md','message_verdict':'MESSAGE_ANCHOR_PASS_INTERNAL_MARKDOWN_SCOPE'}
save('bindings.json',bindings)
result={'revision':'phase2-verification-1.0','reviewed_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW','execution_status':'SUCCESS' if all(x['pass'] for x in checks) else 'PARTIAL','bounded_result':'PASS_INTERNAL_STRUCTURE_AND_DATA_CHECKS' if all(x['pass'] for x in checks) else 'CHANGES_REQUIRED','phase_status':'PHASE2_PREPARED / BAO_SPLIT_REVIEW_PENDING','phase3':'NOT_STARTED','questions':'PROPOSED_UNANSWERED','baseline_commit':BASE,'checks':checks}
save('verification.json',result)
print(json.dumps({'result':result['bounded_result'],'checks':len(checks),'failures':[x for x in checks if not x['pass']]},ensure_ascii=False))
raise SystemExit(0 if all(x['pass'] for x in checks) else 1)
