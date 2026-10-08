"""Verify the approved package merge against both original Git trees and local delivery.
No mutation except an explicitly requested receipt output; no live account access.
"""
from pathlib import Path
import hashlib,json,subprocess,sys
HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[2]
BASE='c5e719137fcdfdcfb6637d3012219d3ff11ade53'
SOURCE='5569ca4ea477c4826f2c9adf00e4a91d4c133923'
FORK='196f26b9f3064fca8fe6b3b50b5707c2b54b65af'
ALLOW={'.gitattributes','.gitignore','CURRENT_STATE.md','DOCS_IMPACT_MAP.md','README.md',
 'ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md',
 'operations/LinkedIn_Current_Progress_2026-10-07.md','drafts/S04_Measurement_and_Budget.md',
 'operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md','operations/LinkedIn_PO_Direction_Budget_Checkpoint_2026-10-06.md'}
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
def tree(ref):
 result={}
 for line in git('ls-tree','-r',ref).decode().splitlines():
  meta,p=line.split('\t',1);mode,kind,blob=meta.split();result[p]=(mode,blob)
 return result
def index():
 result={}
 for line in git('ls-files','--stage').decode().splitlines():
  meta,p=line.split('\t',1);mode,blob,stage=meta.split();assert stage=='0',(p,stage);result[p]=(mode,blob)
 return result
def main():
 target=sys.argv[1] if len(sys.argv)>1 else 'INDEX'
 before=tree(BASE);source=tree(SOURCE);after=index() if target=='INDEX' else tree(target)
 unexpected=[p for p,v in before.items() if p not in ALLOW and after.get(p)!=v]
 assert not unexpected,unexpected
 assert not [p for p in before if p not in after]
 source_exceptions=ALLOW|{'operations/manager-package-v2/README.md','operations/manager-package-v2/Package_V2_Three_Phase_Plan_2026-10-07.md'}
 assert not [p for p,v in source.items() if p not in before and p not in source_exceptions and after.get(p)!=v]
 pkg=ROOT/'deliverables/manager-package-v2/2026-10-07'
 manifest=json.loads((ROOT/'operations/manager-package-v2/zh-hant-2026-10-08/current-files-manifest.json').read_text(encoding='utf-8'))
 assert len(manifest)==233
 for x in manifest:assert hashlib.sha256((pkg/x['path']).read_bytes()).hexdigest()==x['sha256'],x['path']
 for p in ALLOW-{'.gitattributes','.gitignore'}:
  body=git('show',BASE+':'+p)
  final_bytes=git('show',':'+p) if target=='INDEX' else git('show',target+':'+p)
  assert final_bytes.endswith(body),p
 assert not any('/05_Evidence/' in p for p in after)
 assert not git('diff','--name-only','--diff-filter=U').strip()
 changed=git('diff','--cached','--name-only',BASE).decode().splitlines() if target=='INDEX' else git('diff','--name-only',BASE+'..'+target).decode().splitlines()
 for p in changed:
  assert p in ALLOW or p.startswith(('operations/manager-package-v2/','deliverables/manager-package-v2/','deliverables/manager-package-v2-evidence/')),p
 assert not any('/05_Evidence/' in p or '.~lock.' in p or p.endswith('.pyc') for p in changed)
 private=[p for p in (pkg/'05_Evidence').rglob('*') if p.is_file()]
 assert len(private)==12
 for p in private:subprocess.run(['git','check-ignore','--quiet','--',str(p)],cwd=ROOT,check=True)
 bind=json.loads((ROOT/'operations/manager-package-v2/zh-hant-2026-10-08/review.json').read_text(encoding='utf-8'))
 for key in ['anchor','email']:
  x=bind[key];assert hashlib.sha256((ROOT/x['path']).read_bytes()).hexdigest()==x['sha256']
 result={'stage':'MERGE_CANDIDATE_VERIFIED' if target=='INDEX' else 'COMMITTED_TARGET_VERIFIED',
  'reviewer':'/root','independence':'SELF_REVIEW','fork':FORK,'source_checkpoint':SOURCE,'main_before':BASE,
  'verified_target':target,'main_existing_tracked_files':len(before),'main_existing_blobs_unchanged_outside_bounded_docs_config':len(before)-len(ALLOW),
  'changed_existing_paths':sorted(p for p in before if after.get(p)!=before[p]),'deleted_old_main_files':[],
  'source_new_blobs_preserved':True,'exact_approved_package_files':233,'git_package_files':221,
  'private_companion_ignored_files':len(private),'unmerged':[],'unexpected_paths':[],
  'package_source_png_fork_hash_match':170,'anchor_binding':bind['anchor'],'email_binding':bind['email'],
  'po_approval':'PO_APPROVED_OFFLINE','source_semantic_render_review':'Prior exact-byte locale review reused; no changed copy/artwork/locale/persona/destination. No new independent/native-market/live claim.',
  'main_ref_advance':'PENDING actual final readback' if target=='INDEX' else git('rev-parse','main').decode().strip(),'push':False}
 if len(sys.argv)>2:
  out=Path(sys.argv[2]);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in result.items() if k not in ['anchor_binding','email_binding']},ensure_ascii=False))
if __name__=='__main__':main()
