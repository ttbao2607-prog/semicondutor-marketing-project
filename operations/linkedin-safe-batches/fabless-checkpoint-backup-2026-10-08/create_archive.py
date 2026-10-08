"""Archive full owned snapshot without importing oversized unrelated Git ancestry."""
import hashlib,json,subprocess,tarfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE='10a94d37ec9b28d91b2d2860202497feea4bf494'
CP='39a3abdef3c5eb9bcd2b174d8fbc704529bc2002'
OP='operations/linkedin-safe-batches/parallel-fabless-2026-10-07'
DEL='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
assert git('branch','--show-current').decode().strip()=='slice/linkedin-fabless-checkpoint-backup-2026-10-08'
assert git('rev-parse','HEAD').decode().strip()=='4d085bf25ddcb15c31a748a92ac4c49f6052bd57'
objects={}
for row in git('ls-tree','-r',SOURCE).decode().splitlines():
 head,name=row.split('\t',1);mode,kind,oid=head.split()
 if kind=='blob':objects[name]=(mode,oid)
expected={p:oid for p,(mode,oid) in objects.items() if p.startswith((OP+'/',DEL+'/'))}
assert expected and all(objects[p][0]=='100644' for p in expected)
def digest(data):return hashlib.sha256(data).hexdigest()
def blob(data):return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
copied=[];references=set();total=0
proc=subprocess.Popen(['git','archive','--format=tar',SOURCE,'--',OP,DEL],cwd=ROOT,stdout=subprocess.PIPE)
with tarfile.open(fileobj=proc.stdout,mode='r|') as tar:
 for member in tar:
  if member.isdir():continue
  assert member.isfile() and member.name in expected
  data=tar.extractfile(member).read();assert blob(data)==expected[member.name]
  target=(ROOT/member.name).resolve();assert target.is_relative_to(ROOT)
  target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
  copied.append({'path':member.name,'sha256':digest(data),'source_git_blob':expected[member.name],'size':len(data)})
  total+=len(data)
  if member.name.endswith('.json'):
   def walk(x):
    if isinstance(x,str) and x in objects and x not in expected:references.add(x)
    elif isinstance(x,dict):
     for v in x.values():walk(v)
    elif isinstance(x,list):
     for v in x:walk(v)
   try:walk(json.loads(data))
   except (UnicodeDecodeError,json.JSONDecodeError):pass
assert proc.wait()==0 and {x['path'] for x in copied}==set(expected)
freeze_path='operations/message-anchor/freeze-2026-10-06/manifest.json'
frozen=json.loads(git('show',CP+':'+freeze_path))
references.update(x['path'] for x in frozen['files']);references.add(freeze_path)
context=[]
for p in sorted(references):
 assert Path(p).suffix.lower() in ['.png','.webp','.jpg','.jpeg','.svg','.md','.json','.py','.html','.txt'],p
 data=git('show',SOURCE+':'+p)
 name=digest(p.encode())[:16]+'-'+Path(p).stem[:56]+Path(p).suffix
 target=HERE/'source-context-flat'/name;target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(data)
 context.append({'original_path':p,'archive_path':target.relative_to(ROOT).as_posix(),'sha256':digest(data),'source_git_blob':objects[p][1],'size':len(data)})
assert max(x['size'] for x in copied+context)<100*1048576
for x in copied:assert digest((ROOT/x['path']).read_bytes())==x['sha256']
for x in context:assert digest((ROOT/x['archive_path']).read_bytes())==x['sha256']
value={'archive_role':'Full Fabless file snapshot, not original Git ancestry or marketing-ready release','source_closeout_commit_local':SOURCE,'final_production_checkpoint_local':CP,'selected_main_integration':'4d085bf25ddcb15c31a748a92ac4c49f6052bd57','archive_branch':'slice/linkedin-fabless-checkpoint-backup-2026-10-08','owned_files':copied,'source_context_files':context,'counts':{'owned_files':len(copied),'owned_bytes':total,'context_files':len(context),'generation_batches':9,'selected_positions_including_reuse':99,'remaining_generation_batches':0},'original_source_ancestry':'Local retained unchanged; not pushed because13historical ancestral blobs exceed100MiB. No history rewrite/LFS migration.','verification':'Every archived file matches source Git blob and SHA256; source context mapped; archive files below100MiB. Actual remote ref readback still required.','technical_acceptance':'Unchanged: B18-B21 mobile visual INSUFFICIENT_EVIDENCE; B15 proof2 CHANGES_REQUIRED; raw failed attempts remain failed; no independent/live certification.'}
(HERE/'archive-files.json').write_text(json.dumps(value,ensure_ascii=False,indent=2)+'\n','utf-8')
print('Archived',len(copied),'owned files,',round(total/1048576,1),'MiB;',len(context),'direct/frozen context files; exact source Git blob/SHA256 verified')
