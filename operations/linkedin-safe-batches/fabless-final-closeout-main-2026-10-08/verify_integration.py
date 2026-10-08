"""Verify actual integration bytes/coverage, without inventing visual acceptance."""
import hashlib,json,subprocess,os
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
SOURCE=Path('D:/LinkedIn_Safe_Fabless_2026-10-07')
def load(p):return json.loads(p.read_text('utf-8-sig'))
def sha(b):return hashlib.sha256(b).hexdigest()
def git(*a):return subprocess.check_output(['git',*a],cwd=ROOT)
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
sel=load(HERE/'selected-files.json');BASE=sel['main_base'];CP=sel['source_checkpoint']
assert git('rev-parse','HEAD').decode().strip()==BASE
assert git('rev-parse','HEAD').decode().strip()==subprocess.check_output(['git','rev-parse','main'],cwd=ROOT).decode().strip()
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=SOURCE).decode().strip()==CP
assert not subprocess.check_output(['git','status','--porcelain'],cwd=SOURCE).strip()
for f in sel['files']:assert sha((ROOT/f['path']).read_bytes())==f['sha256'],f['path']
pngs=[x for x in sel['files'] if x['role']=='selected_final' and x['path'].endswith('.png')]
assert len(pngs)==44
for x in pngs:assert Image.open(ROOT/x['path']).size==(1254,1254)
calls=0;shots=0;mobile=0
class Links(HTMLParser):
 def __init__(self):super().__init__();self.refs=[]
 def handle_starttag(self,tag,attrs):
  for k,v in attrs:
   if k in ['href','src'] and v:self.refs.append(v)
for b in sel['batches']:
 r=load(ROOT/b['postgen']);assert r['artifact_verdict']==r['message_anchor']=='INSUFFICIENT_EVIDENCE'
 assert len(r['unit_review'])==11 and r['counts']['selected']==11
 for f in r['subjects'].values():assert sha((ROOT/f['path']).read_bytes())==f['sha256']
 for a in r['attempt_verification']:
  calls+=1
  for key in ['native','guard','release','anchor_review']:
   f=a[key];assert sha((SOURCE/f['path']).read_bytes())==f['sha256']
 for s in r['render']['screenshots']:
  assert sha((ROOT/s['path']).read_bytes())==s['sha256'];shots+=1
 mobile+=len(r['render'].get('mobile390_visual_screenshots',[]))
 dest=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'/b['selected']
 for c in load(dest/'selected-copy.json')['cards']:assert (dest/c['image']).is_file()
 for name in ['index.html','case-reader.html']:
  p=dest/name;parser=Links();parser.feed(p.read_text('utf-8'))
  for ref in parser.refs:
   u=urlsplit(ref)
   if not u.scheme and not u.netloc and u.path:assert (p.parent/unquote(u.path)).is_file(),(p,ref)
assert calls==33 and shots==140 and mobile==1
frozen=load(SOURCE/'operations/message-anchor/freeze-2026-10-06/manifest.json')
pins=[]
for f in frozen['files']:
 assert sha((SOURCE/f['path']).read_bytes())==f['sha256']
 p=ROOT/f['path'];prior=git('ls-tree',BASE,'--',f['path']).decode().strip()
 if prior:
  before=git('show',BASE+':'+f['path'])
  baseline=Path('D:/Digiwin_Semiconducter_Workspace')/f['path']
  assert p.read_bytes()==baseline.read_bytes()
  assert git('hash-object',f['path']).decode().strip()==prior.split()[2]
  assert p.read_bytes().replace(b'\r\n',b'\n')==before.replace(b'\r\n',b'\n')
  pins.append({'path':f['path'],'main_state':'EXISTING_UNCHANGED','main_working_sha256':sha(p.read_bytes()),'main_git_blob_sha256':sha(before),'checkout_newlines_only':p.read_bytes()!=before})
 else:
  assert not p.exists();pins.append({'path':f['path'],'main_state':'ABSENT_REMAINS_ABSENT'})
assert len(pins)==24
sync=load(HERE/'docs-synchronization.json')
for row in sync['changes']:
 p=ROOT/row['path'];before=(Path('D:/Digiwin_Semiconducter_Workspace')/row['path']).read_bytes();after=p.read_bytes()
 assert before.replace(b'\r\n',b'\n')==git('show',BASE+':'+row['path']).replace(b'\r\n',b'\n')
 assert sha(before)==row['before_sha256'] and sha(after)==row['after_sha256']
 body=after.split(b'\n\n',1)[1]
 if row['path']=='operations/LinkedIn_Current_Progress_2026-10-07.md':
  keep=lambda data:[s for s in data.splitlines(keepends=True) if not s.startswith(b'| Fabless FDI |')]
  assert keep(before)==keep(body)
  assert sum(s.startswith(b'| Fabless FDI |') for s in body.splitlines())==2
 else:assert body==before
rel='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B15-zh-Hant-f1-v3/assets/09-rmk-bright-2.png'
data=(ROOT/rel).read_bytes();assert data==git('show',BASE+':'+rel)
put(HERE/'b15-proof2-current-qualification.json',{'reviewer':'/root','independence':'SELF_REVIEW','review_scope':'Actual native image viewed fresh on integration turn; prior reported finding reconciled against current main bytes','path':rel,'sha256':sha(data),'observed_headline_prefix':'来自中国的','approved_zh_Hant_prefix':'來自中國的','current_verdict':'CHANGES_REQUIRED','status_effect':'Affected proof2 cannot inherit prior blanket Hant PASS; B15 current whole-set Hant acceptance qualified. Prior receipts/bytes retained as history; no repair/new generation.','proof3_legal_name_suspicion':'NOT_CONFIRMED / WITHDRAWN; original legal entity may remain Simplified by source policy.'})
changed=git('diff','--name-only').decode().splitlines()
assert sorted(changed)==sorted(x['path'] for x in sync['changes'])
new=git('ls-files','--others','--exclude-standard').decode().splitlines()
whitelist={x['path'] for x in sel['files']}
prefix=HERE.relative_to(ROOT).as_posix()+'/'
assert all(p in whitelist or p.startswith(prefix) or p=='operations/linkedin-safe-batches/parallel-fabless-2026-10-07/README.md' for p in new)
assert all('/corrective-v' not in p and '/release/' not in p and '/canary/' not in p for p in new)
put(HERE/'integration-validation.json',{'execution_status':'SUCCESS_PREMERGE_LOCAL_PREPARATION','verification':'ROOT_BYTE_AND_STATE_SELF_INSPECTION','independent_agent_audit':'NOT_RUN','source_checkpoint':CP,'main_base':BASE,'imported_files_verified':len(sel['files']),'selected_native_png':44,'png_size':[1254,1254],'png_transformations':0,'source_imagegen_attempts_fresh_guard_release_hashes_verified':33,'accepted_desktop_feed_reader_screenshots':140,'accepted_mobile_cold_screenshots':1,'other_mobile_reader_visual':0,'selected_total_on_main':99,'generation_batches':9,'remaining_generation_batches':0,'technical_acceptance':'B18-B21 INSUFFICIENT_EVIDENCE/PARTIAL; B15 proof2 CHANGES_REQUIRED; no full/independent/live PASS','protected_inventory':pins,'source_frozen_pins_verified':24,'canonical_updates':len(sync['changes']),'non_fabless_progress_rows_and_other_doc_bodies_unchanged':True,'unrelated_main_files_unchanged':True,'viewers_local_assets_reader_return_targets':'All exist; mechanical dependency check only, no new browser render claim','push_status':'NOT_YET_PERFORMED; actual remote readback required after authorized merge/push'})
print('PASS integration byte/scope checks:',len(sel['files']),'imports,44rawPNG,33attempt guards,140desktop/feed/reader shots+1mobile cold; protected24 and other-lane docs unchanged')
