"""Owned metadata only; no shared canonical/Git index mutation."""
import hashlib,json,os,subprocess
from pathlib import Path
LANE=Path(__file__).resolve().parent
ROOT=LANE.parents[2]
MAIN=Path('D:/Digiwin_Semiconducter_Workspace')
def load(p):return json.loads(p.read_text('utf-8-sig'))
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True,encoding='utf-8').strip()
assert git('branch','--show-current')=='slice/linkedin-safe-fabless-parallel'
assert git('rev-parse','HEAD')=='b83d061b01313ba90bf9b3c07a2911360160a208'
files=['CURRENT_STATE.md','DOCS_IMPACT_MAP.md','operations/LinkedIn_Current_Progress_2026-10-07.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','drafts/S03_LinkedIn_Audience_Research.md','operations/linkedin-safe-batches/parallel-handoff-2026-10-07/README.md']
main_sha=subprocess.check_output(['git','rev-parse','HEAD'],cwd=MAIN,text=True).strip()
rows=[]
for name in files:
 p=MAIN/name;lines=p.read_text('utf-8-sig').splitlines()
 rows.append({'path':name,'sha256':sha(p),'relevant_lines':[{'line':i,'text':s} for i,s in enumerate(lines,1) if ('Fabless' in s or 'B18' in s or 'B20' in s or 'B21' in s or 'CANONICAL' in s)][:14]})
put(LANE/'B20-B21-docs-reviewed.json',{'main_local_sha':main_sha,'reviewer':'/root','review_scope':'Current state headers and relevant Fabless/creative/anchor/documentation rows; historical records retained. Prior full source/anchor readings retained.','files':rows,'outcome':'Owned draft closeout; canonical adopted count remains5/55. Concrete promotion proposal in B20-B21-docs-impact.md.'})
put(LANE/'B20-B21-source-supplement.json',{'observed_date':'2026-10-08','reviewer':'/root','scope':'Fresh official-source observations supplement Oct7 mappings; no broader claims.','sources':[{'url':'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/','refresh':'403 on fresh request; retained approved Oct7 source snapshot/mapping, no successful fresh read claim.','scope':'China Bright qualitative outsourcing challenges and integrated solution; no ERP-only/Vietnam result.'},{'url':'https://www.digiwin.com.tw/dsc/solution/semiconductor/index','refresh':'Successfully read official source Oct8; line223 separates ERP management and MES production.','scope':'Taiwan solution taxonomy, no measured outcome.'},{'url':'https://www.digiwin.com.vn/casestudies/huakun-electronic-viet-nam-san-xuat-thong-minh-digiwin-erp/','refresh':'Successfully read official source Oct8, lines162-167 narrow consulting/implementation support.','scope':'Vietnam consulting/implementation service only; no Fabless customer, staffing or language capability inferred.'}],'source_history_reconciliation':'B15 proof2 Simplified headline confirmed; old/main bytes unchanged. B21 uses B18 repaired Hant source. Proof3 legal-name suspicion withdrawn after native reinspection.'})
status=load(LANE/'B20-B21-current-status.json')
p=LANE/'ledger.json';ledger=load(p)
ledger['current_2026_10_08_b20_b21']={'status_file':'B20-B21-current-status.json','batches':status['batches'],'remaining_generation_queue':[],'generation_complete':True,'full_pipeline_complete':False,'b18_b19_checkpoint':'b83d061b01313ba90bf9b3c07a2911360160a208','b20_b21_working_files_uncommitted':True,'new_main_merge':False,'new_push':False,'live':False,'qualification':'Earlier ledger keys are dated history. B18-B21 full gate mobile evidence insufficient; B15 proof2 current acceptance qualification preserved.'}
put(p,ledger)
p=LANE/'README.md';old=p.read_text('utf-8-sig');marker='> **Current B20/B21 closeout, 2026-10-08:**'
if not old.startswith(marker):
 p.write_text(marker+' B20 zh-Hans F3 v3 and B21 zh-Hant F3 v1 each11selected;14calls=12original+2corrective,10same-locale raw reuses. Native/desktop640/feed333 scoped SELF_REVIEW PASS; B20 A5 closed. Full gates INSUFFICIENT_EVIDENCE / PARTIAL: B20 mobile0/11, B21 mobile1/11, both reader mobile visual missing. Queue generation9/9 complete,0remaining; this does not close acceptance. B18/B19 checkpoint b83d061b local only; B20/B21 new working files, no new main/push/live. [Closeout](B20-B21-closeout.md). All banners below are dated history, including earlier NOT_RUN/uncommitted snapshots.\n\n'+old,'utf-8')
raw=Path(os.environ['TEMP'])/'fabless-b20-b21-final-recovery.txt'
assert raw.exists()
actual=git('ls-remote','origin','refs/heads/main').split()[0]
subprocess.run(['git','merge-base','--is-ancestor','c5e719137fcdfdcfb6637d3012219d3ff11ade53',actual],cwd=ROOT,check=True)
report=raw.read_text('utf-8-sig')
report+='\nSUPPLEMENT — exact lane/remote interpretation\nActual remote main readback: '+actual+'\nCurrent source branch HEAD b83d061b is local only. B20/B21 are new uncommitted files; index unchanged. Canonical main local: '+main_sha+' (other-session changes), separate from actual remote.\nB13-B17 selected integration c5e71913 is an ancestor of actual remote main; unpublished source branch does not mean all historical selected artifacts are absent remote. Remote-tracking refs are cached observations, not a new push. No recovery/reflog or Git mutation performed except authorized earlier B18/B19 commit and skill fetch.\nSAFE CONCLUSION\nGeneration queue exhausted; native/desktop/feed reviewed; mobile visual incomplete. No new full PASS or adoption.\nNEXT ACTION\nRecommendation only: obtain missing mobile visual evidence or a PO scope decision before full acceptance; commit/integration/push require applicable authority.\n'
(LANE/'git-state-b20-b21-final.txt').write_text(report,'utf-8')
print('Owned metadata updated; actual remote',actual,'main local',main_sha)
