from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
import json,hashlib,re,subprocess
from PIL import Image

ROOT=Path(__file__).resolve().parents[3]
PACK=ROOT/'deliverables/manager-package-v2/2026-10-07'
OUT=Path(__file__).parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
base=json.loads((ROOT/'operations/manager-package-v2/zh-hant-2026-10-08/current-files-manifest.json').read_text(encoding='utf-8-sig'))
changed=[x['path'] for x in base if sha(PACK/x['path'])!=x['sha256']]
assert len(changed)==16,changed
assert all(x.endswith(('.html','.md','.txt')) for x in changed)
assert not any(x.startswith('05_Evidence/') or x.endswith('.xlsx') or x.count('/')>1 and x.startswith('03_Thu_vien/') for x in changed)

class Reader(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=set();self.text=[];self.skip=False
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t in ['script','style']:self.skip=True
  self.links += [a[k] for k in ['href','src'] if k in a]
  if 'id' in a:self.ids.add(a['id'])
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=False
 def handle_data(self,s):
  if not self.skip:self.text.append(s)

readers={}
for f in PACK.rglob('*.html'):
 p=Reader();p.feed(f.read_text(encoding='utf-8-sig'));readers[f.resolve()]=p
missing=[];checked=0
for f,p in readers.items():
 for u in p.links:
  v=urlsplit(u)
  if v.scheme or v.netloc:continue
  target=(f.parent/unquote(v.path)).resolve() if v.path else f
  checked+=1
  if not target.exists():missing.append([f.relative_to(PACK).as_posix(),u,'file'])
  elif v.fragment and target in readers and unquote(v.fragment) not in readers[target].ids:missing.append([f.relative_to(PACK).as_posix(),u,'fragment'])
assert not missing,missing
pattern=re.compile(r'\b(?:git|github|worktree|checkpoint|harness|adapter|canonical|SHA256|SELF_REVIEW|CHANGES_REQUIRED|INSUFFICIENT_EVIDENCE|codex|agent|integrity|pregen|postgen|localhost)\b|(?<![A-Za-z])[A-Z]:[\\/]|file://|operations/|本機路徑|內部審核',re.I)
suspects=[]
new=sorted(f for f in (PACK/'06_Google').rglob('*') if f.is_file())
for f in [PACK/x for x in changed]+new:
 if f.suffix not in ['.html','.txt','.md']:continue
 s=' '.join(readers[f.resolve()].text) if f.suffix=='.html' else f.read_text(encoding='utf-8-sig')
 for m in pattern.finditer(s):suspects.append({'file':f.relative_to(PACK).as_posix(),'term':m.group()})
assert not suspects,suspects
images=[]
for f in (PACK/'06_Google/Anh').glob('*.png'):
 with Image.open(f) as im:im.load();images.append({'path':f.relative_to(PACK).as_posix(),'size':im.size})
questions=[]
for suf in ['', '.zh-Hant']:
 rel='deliverables/manager-package-v2/2026-10-07/01_De_xuat/de_xuat'+suf+'.html'
 old=subprocess.check_output(['git','show','ff95e9f86cc5f9ce99e14dcf70988ae49bd3391d:'+rel],cwd=ROOT).decode('utf-8-sig');cur=(ROOT/rel).read_text(encoding='utf-8-sig')
 pat=r'<h2[^>]*id="ba-diem".*?</article>'
 a=re.search(pat,old,re.S);b=re.search(pat,cur,re.S)
 assert a and b,rel
 assert a.group().replace('\r\n','\n')==b.group().replace('\r\n','\n')
 questions.append(rel)
manifest=[{'path':f.relative_to(PACK).as_posix(),'sha256':sha(f),'size':f.stat().st_size} for f in sorted(PACK.rglob('*')) if f.is_file()]
result={'package_files':len(manifest),'old_files_unchanged':len(base)-len(changed),'changed_old_files':changed,'new_google_files':[f.relative_to(PACK).as_posix() for f in new],'relative_links_checked':checked,'missing':missing,'internal_term_findings':suspects,'budget_question_sections_unchanged':questions,'new_images_decoded':images,'protected':'All17originaljourneys/readers170adPNGs/workbook/privateevidence unchanged byte-for-byte','technical_scope':'Static references/closure and byte comparison; not live campaign or file:// browser test.'}
(OUT/'static-review.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
(OUT/'package-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
