"""Docs-only main reconciliation from observed local evidence. No active-source mutation."""
import datetime,hashlib,json,os,subprocess
from pathlib import Path
BASE=Path(__file__).resolve().parent; ROOT=BASE.parents[2]
def git(root,*a):return subprocess.check_output(['git',*a],cwd=root)
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v):p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode())
sources={
 'original_company_list':('D:/optimize-awareness-LinkedIn-adcopy',['operations/linkedin-closeout/2026-10-05/STATE.md','operations/linkedin-closeout/2026-10-05/slice-a/HANDOFF.md','operations/linkedin-closeout/2026-10-05/slice-a/FULL_MATCHING_RESEARCH_RESULT_20261006.md','operations/LinkedIn_PO_Direction_Budget_Checkpoint_2026-10-06.md','operations/LinkedIn_Worktree_Consolidation_Result_2026-10-06.md']),
 'backup_contingency':('D:/Digiwin_LinkedIn_Contingency_Audience',['operations/LinkedIn_Contingency_R5_52_Upload_2026-10-07.md','operations/LinkedIn_Contingency_R5_PostMatch_Check_2026-10-07.md']),
 'osat':('D:/LinkedIn_Safe_OSAT_2026-10-07',['operations/linkedin-safe-batches/parallel-osat-2026-10-07/ledger.json','operations/linkedin-safe-batches/parallel-osat-2026-10-07/B10-B12-main-integration/local-main-closeout.json']),
 'fabless':('D:/LinkedIn_Safe_Fabless_2026-10-07',['operations/linkedin-safe-batches/parallel-fabless-2026-10-07/ledger.json','operations/linkedin-safe-batches/parallel-fabless-2026-10-07/B14-zh-Hans-f1-v1/attempt-ledger.json']),
 'partner':('D:/LinkedIn_Safe_Partner_2026-10-07',['operations/linkedin-safe-batches/parallel-partner-2026-10-07/ledger.json','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B22-en-p1-v1/supplier-v3/postgen-review-v7.json','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B23-zh-Hans-p1-v1/attempt-ledger.json','operations/linkedin-safe-batches/parallel-partner-2026-10-07/B24-zh-Hant-p1-v1/attempt-ledger.json']),
 'fdi_html':('D:/LinkedIn_FDI_Destination_HTML_2026-10-07',['operations/fdi-destination-html/2026-10-07/README.md','operations/fdi-destination-html/2026-10-07/inventory.csv'])}
evidence={}
for lane,(s,files) in sources.items():
 r=Path(s);head=git(r,'rev-parse','HEAD').decode().strip();branch=git(r,'branch','--show-current').decode().strip()
 evidence[lane]=dict(worktree=s,branch=branch,head=head,dirty=bool(git(r,'status','--porcelain').strip()),files=[dict(path=f,sha256=sha(r/f),committed_at_head=(git(r,'show',head+':'+f)==(r/f).read_bytes()) if subprocess.run(['git','cat-file','-e',head+':'+f],cwd=r,stderr=subprocess.DEVNULL).returncode==0 else False) for f in files])
inventory=[]
for block in git(ROOT,'worktree','list','--porcelain').decode().strip().split('\n\n'):
 fields=dict(x.split(' ',1) for x in block.splitlines() if ' ' in x);r=Path(fields['worktree'])
 inventory.append(dict(worktree=str(r),head=fields.get('HEAD'),branch=fields.get('branch'),dirty=bool(git(r,'status','--porcelain').strip())))
put(BASE/'evidence.json',dict(observed_local_at=datetime.datetime.now().astimezone().isoformat(),main_baseline=git(ROOT,'rev-parse','HEAD').decode().strip(),remote_tracking_main=git(ROOT,'rev-parse','origin/main').decode().strip(),live_github_verified=False,live_account_readback=False,sources=evidence,worktree_inventory=inventory,scope='Sanitized progress metadata only; no raw account/company rows or credentials. Active source worktrees read-only.'))
docs=['CURRENT_STATE.md','README.md','DOCS_IMPACT_MAP.md','Semiconductor_Work_Kickoff.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','drafts/S03_LinkedIn_Audience_Research.md','drafts/S04_Measurement_and_Budget.md','operations/LinkedIn_Safe_Batch_Execution_Plan_2026-10-06.md','operations/LinkedIn_Report_Artifact_Index_2026-10-05.md','operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md']
snapshot=ROOT/'operations/LinkedIn_Current_Progress_2026-10-07.md';pre={}
for n in docs:
 p=ROOT/n;old=p.read_bytes();pre[n]=sha(p);rel=os.path.relpath(snapshot,p.parent).replace('\\','/')
 note='> **CURRENT LinkedIn progress reconciliation · 2026-10-07:** [Tiến độ đã đối chiếu main/worktrees và baseline package mới]('+rel+'). Cold Single image → new-ad member audience → Carousel RMK; media cap11,7triệu. Tệp công ty gốc424 đã nghiên cứu/sửa định danh và submit existing Discovery1lần, last Updating06/10; chờ mapping/reach readback, không restart cleanup. Contingency backup R5-52 là luồng riêng: Ready/>90% nhưng Details0, đề xuất recheck24h chưa schedule. VN creative và OSATB6–B12 selected offline đã trên main; Fabless/Partner đang sản xuất ở source, chưa creative-main;10FDI redesigned readers checkpoint5b99984 chưa-main. Package v6 là lịch sử ở source, chưa rebuild. Harness/anchor/process frozen, adapter DEVELOPING/NOT_FROZEN. Các banner/số liệu trước bên dưới chỉ là snapshot đúng revision, không current whole-project status. Chỉ docs sync, không live/push hay acceptance mới.\n\n'
 p.write_bytes(note.encode()+old)
put(BASE/'docs-impact.json',dict(canonical_updated=docs,preexisting_body_sha256=pre,current_progress_sha256=sha(snapshot),protected='Artifacts, frozen process/core/anchor, HISTORY/LOG/receipts and active-source worktrees unchanged.',package='Baseline only; no rebuild/ZIP/workbook mutation',instruction='Kiểm canonical main với các worktree, đồng bộ docs ở main cho tiến độ hiện tại nếu có contradicting, chuẩn bị Bảo tính làm lại package mới.',execution='SUCCESS_DOCS_ONLY',reviewer='ROOT_SELF_AUDIT'))
print('11 canonical entrypoints synchronized; local evidence pinned; package baseline created.')
