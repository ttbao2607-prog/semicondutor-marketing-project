"""Selective offline checkpoint import; never import generation runtime or failed assets."""
import hashlib,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE='39a3abdef3c5eb9bcd2b174d8fbc704529bc2002'
BASE='e0c84d30e9653560817d8ed8249e84436c8cd611'
OP='operations/linkedin-safe-batches/parallel-fabless-2026-10-07'
DEL='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def source(p):return git('show',SOURCE+':'+p)
def sha(b):return hashlib.sha256(b).hexdigest()
def read(p):return json.loads(source(p))
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
assert git('rev-parse','HEAD').decode().strip()==BASE
assert git('branch','--show-current').decode().strip()=='slice/linkedin-fabless-final-closeout-2026-10-08'
copied={}
def copy(p,role):
 if p in copied:return
 data=source(p);target=ROOT/p
 assert not target.exists() or target.read_bytes()==data,p
 target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
 copied[p]={'path':p,'source_checkpoint':SOURCE,'sha256':sha(data),'size':len(data),'role':role}
batches=[]
for batch,ops,out in [('B18','B18-zh-Hant-f2-v1','B18-zh-Hant-f2-v4'),('B19','B19-en-f3-v1','B19-en-f3-v1'),('B20','B20-zh-Hans-f3-v1','B20-zh-Hans-f3-v3'),('B21','B21-zh-Hant-f3-v1','B21-zh-Hant-f3-v1')]:
 final=DEL+'/'+out;base=OP+'/'+ops
 paths=git('ls-tree','-r','--name-only',SOURCE,'--',final).decode().splitlines()
 assert sum(p.endswith('.png') for p in paths)==11
 for p in paths:copy(p,'selected_final')
 r=read(base+'/postgen-review.json');m=read(final+'/manifest.json')
 assert r['artifact_verdict']==m['status']=='INSUFFICIENT_EVIDENCE'
 assert len(m['artwork'])==11
 for a in m['artwork']:
  assert sha(source(a['path']))==a['sha256']==sha(source(a['source']))
 for name in ['postgen-review.json','verification.json','proof-source-mapping.json','vietnam-team-source.json','semantic-review.json','reuse-review.json']:
  copy(base+'/'+name,'scoped_review')
 root_files=git('ls-tree','-r','--name-only',SOURCE,'--',base).decode().splitlines()
 for p in root_files:
  if p.rsplit('/',1)[0]==base and (p.endswith('.md') or p.endswith('/source-reuse-exclusions.json') or '/actual-corrective-' in p):copy(p,'scoped_decision_history')
  if p.rsplit('/',1)[0]==base+'/render-current' and p.endswith('.json'):copy(p,'render_dom_and_probe_observation')
 for x in r['render']['screenshots']+r['render'].get('mobile390_visual_screenshots',[]):copy(x['path'],'accepted_scope_capture')
 batches.append({'batch':batch,'locale':m['locale'],'selected':out,'cards':11,'technical_status':'INSUFFICIENT_EVIDENCE','native_desktop_feed':'PASS_SELF_REVIEW','mobile_visual_cards':1 if batch=='B21' else 0,'mobile_reader_visual':0,'postgen':base+'/postgen-review.json','counts':r['counts']})
for p in ['B18-B19-current-status.json','B20-B21-current-status.json','B20-B21-source-supplement.json']:
 copy(OP+'/'+p,'dated_source_checkpoint_status')
put(HERE/'selected-files.json',{'source_checkpoint':SOURCE,'main_base':BASE,'files':list(copied.values()),'batches':batches,'selected_png_positions':44,'png_transformations':0,'history_resolution':'Raw/failed/guard/spec references absent from main resolve at SOURCE:path on separately backed-up source branch.'})
anchor=[]
for p in ['operations/Vy_Email_Content_Anchor.md','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md']:
 main=(ROOT/p).read_bytes();src=source(p)
 assert main.replace(b'\r\n',b'\n')==src.replace(b'\r\n',b'\n')
 anchor.append({'path':p,'main_sha256':sha(main),'source_checkpoint_sha256':sha(src),'semantic_identity':'Exact bytes or newline-only; no anchor/source content change.'})
put(HERE/'main-anchor-binding.json',{'anchor_id':'VY-CONTENT-ANCHOR','anchor_revision':'1.0','source_checkpoint':SOURCE,'main_base':BASE,'reviewer':'/root','independence':'SELF_REVIEW','pins':anchor,'personas':'Operations/SCM decision influencer at eligible commercial outsourced-production Fabless FDI entity; local decision authority/eligibility not inferred from language.','locales':['zh-Hant','en','zh-Hans','zh-Hant'],'scope':'Integration/provenance binding only; existing scoped source judgments retained. Full artifact/message gate remains INSUFFICIENT_EVIDENCE due mobile visual gap. No generation, new semantic PASS or independent/live certification.'})
docs=['CURRENT_STATE.md','DOCS_IMPACT_MAP.md','README.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','drafts/S03_LinkedIn_Audience_Research.md','operations/LinkedIn_Current_Progress_2026-10-07.md','operations/LinkedIn_Report_Artifact_Index_2026-10-05.md','operations/Public_Source_Register.md','operations/Ad_Artifact_Editorial_QA_Gate.md','operations/LinkedIn_Awareness_Demo_and_Human_Audit_Runbook.md','operations/linkedin-safe-batches/parallel-handoff-2026-10-07/README.md']
review=[]
for name in docs:
 p=ROOT/name
 if p.exists():review.append({'path':name,'base_sha256':sha(p.read_bytes())})
put(HERE/'docs-reviewed.json',{'main_base':BASE,'reviewer':'/root','files':review,'scope':'Current Fabless/progress/proof/editorial/message/closure statements, not unrelated dated history. Current docs updated where affected; process/rights/budget unchanged.'})
url=git('remote','get-url','origin').decode().strip()
assert ('github.com' in url), 'Remote identity requires review'
print('Copied',len(copied),'files;',len(batches),'selected batches /44rawPNG; main anchor content matches; remote host github.com verified')
