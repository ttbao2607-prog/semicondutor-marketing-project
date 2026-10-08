"""Verify final package selection/portability and unchanged protected payload."""
import hashlib, html, json, pathlib, re, subprocess
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.parse import unquote, urlsplit

ROOT=pathlib.Path(__file__).resolve().parents[3];REC=pathlib.Path(__file__).parent
OUT=ROOT/'deliverables/manager-package-v2/2026-10-07';BASE='ecf87adc28cac2e39279824022ce98979efef142'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
def original(relative):
    return subprocess.check_output(['git','show',BASE+':deliverables/manager-package-v2/2026-10-07/'+relative],cwd=ROOT).decode('utf-8').replace('\r\n','\n')
class Surface(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.text=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ['style','script']:self.skip+=1
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for k in ['href','src']:
            if k in a:self.links.append(a[k])
    def handle_endtag(self,tag):
        if tag in ['style','script']:self.skip=max(0,self.skip-1)
    def handle_data(self,s):
        if not self.skip:self.text.append(s)
checks=[]
def check(label,value):checks.append({'check':label,'pass':bool(value)})
prior=json.loads((ROOT/'operations/manager-package-v2/phase3/final-file-manifest.json').read_text(encoding='utf-8'))
changed={'BAT_DAU.html','DOC_TRUOC.txt','01_De_xuat/De_xuat_paid_ads.md','01_De_xuat/de_xuat.html','01_De_xuat/Mail_gui_Vy.md','01_De_xuat/mail_gui_Vy.html','02_Demo/index.html','03_Thu_vien/index.html'}
protected=[x for x in prior['files'] if x['path'] not in changed]
for x in protected:check('protected byte '+x['path'],sha(OUT/x['path'])==x['sha256'])
check('205 protected files',len(protected)==205)
final=[];surfaces={}
for p in sorted(x for x in OUT.rglob('*') if x.is_file()):
    relative=str(p.relative_to(OUT)).replace('\\','/');final.append({'path':relative,'sha256':sha(p),'bytes':p.stat().st_size})
    check('delivery file type '+relative,p.suffix in ['.html','.md','.txt','.png','.xlsx'])
    if p.suffix=='.html':
        s=Surface();s.feed(p.read_text(encoding='utf-8'));surfaces[p.resolve()]=s
    if p.suffix in ['.md','.html','.txt']:
        raw=p.read_text(encoding='utf-8')
        check('no internal payload '+relative,not re.search(r'SELF_REVIEW|INSUFFICIENT_EVIDENCE|MESSAGE_ANCHOR|CHANGES_REQUIRED|sha256|NOT_FROZEN|source-pinned|D:[/\\]|native leaf|git hash|harness',raw,re.I))
for p,s in surfaces.items():
    for link in s.links:
        u=urlsplit(link)
        if u.scheme or u.netloc or not u.path and not u.fragment:continue
        target=(p.parent/unquote(u.path)).resolve() if u.path else p
        check('relative dependency '+str(p.relative_to(OUT))+' → '+link,target.is_relative_to(OUT) and target.exists())
        if u.fragment and target in surfaces:check('fragment '+link,unquote(u.fragment) in surfaces[target].ids)
proposal=(OUT/'01_De_xuat/De_xuat_paid_ads.md').read_text(encoding='utf-8')
before=original('01_De_xuat/De_xuat_paid_ads.md')
check('same three investment questions',proposal.split('## Ba điểm Vy xem giúp Bảo',1)[1]==before.split('## Ba điểm Vy xem giúp Bảo',1)[1])
check('summary before budget',proposal.index('## Logic quảng cáo')<proposal.index('## Ngân sách chưa thuế'))
check('question count three',len(re.findall(r'^### [1-3]\. ',proposal,re.M))==3)
check('unchanged budget and measurement block',proposal.split('## Ngân sách chưa thuế',1)[1]==before.split('## Ngân sách chưa thuế',1)[1])
mail=(OUT/'01_De_xuat/Mail_gui_Vy.md').read_text(encoding='utf-8');oldmail=original('01_De_xuat/Mail_gui_Vy.md')
check('same mail feedback points',mail.split('1. Trần đầu tư',1)[1]==oldmail.split('1. Trần đầu tư',1)[1])
check('name voice',not re.search(r'anh/chị|chị Vy|anh Vy|em gửi',mail+proposal,re.I))
content=json.loads((REC/'prepared-copy.json').read_text(encoding='utf-8'))['copy']
logic_path=(OUT/'01_De_xuat/logic_quang_cao.html').resolve();text=' '.join(surfaces[logic_path].text)
md=(OUT/'01_De_xuat/Logic_quang_cao.md').read_text(encoding='utf-8')
def strings(value):
    if isinstance(value,str):yield value
    elif isinstance(value,list):
        for x in value:yield from strings(x)
    elif isinstance(value,dict):
        for key,x in value.items():
            if key not in ['id','image','alt','journey','reader']:yield from strings(x)
for key in ['title','lead','audience','hypotheses','visual','journey','matrix']:
    for value in strings(content[key]):
        check('logic exact copy '+value[:65],value in text and value in md)
check('five logic sections',len(surfaces[logic_path].ids)==7)
check('six illustrations',len(re.findall(r'<img ',logic_path.read_text(encoding='utf-8')))==6)
check('seven matrix cases',len(content['matrix']['rows'])==7)
table_lines=[line for line in md.splitlines() if line.startswith('|')]
check('Markdown matrix is one contiguous nine-line table',len(table_lines)==9 and '\n'.join(table_lines) in md)
binding=json.loads((REC/'source-bindings.json').read_text(encoding='utf-8'))
for x in binding['illustrations']:check('illustration preserved '+x['path'],sha(OUT/x['path'])==x['sha256'])
for x in binding['sources']:
    if x['id']=='main_current':
        # Other lanes may advance main while this bounded package is reviewed.
        # Verify the captured source at its exact commit, not the moving checkout.
        snapshot=REC/'main-current-at-source-capture.md'
        blob=subprocess.check_output(['git','-C',str(pathlib.Path(x['path']).parent),'show',binding['git']['main_head']+':CURRENT_STATE.md'])
        check('dated main source exact captured bytes',snapshot.exists() and sha(snapshot)==x['sha256'])
        check('dated main source matches captured commit',snapshot.exists() and snapshot.read_bytes().replace(b'\r\n',b'\n')==blob.replace(b'\r\n',b'\n'))
    else:
        check('bound source current '+x['id'],sha(pathlib.Path(x['path']))==x['sha256'])
gate=json.loads((REC/'pregen-review.json').read_text(encoding='utf-8'))
for filename,key in [('prepared-copy.json','prepared_copy_sha256'),('build_extension.py','builder_sha256'),('source-bindings.json','source_bindings_sha256'),('Pregen_Review.md','review_record_sha256')]:check('pregen binding '+filename,sha(REC/filename)==gate[key])
check('215 final files',len(final)==215)
check('only two new files',{x['path'] for x in final}-{x['path'] for x in prior['files']}=={'01_De_xuat/logic_quang_cao.html','01_De_xuat/Logic_quang_cao.md'})
check('no ZIP',not list(OUT.rglob('*.zip')))
issues=[x for x in checks if not x['pass']]
manifest={'revision':'package-v2-ad-logic-1.1','folder':str(OUT),'files':final}
(REC/'final-file-manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
result={'revision':manifest['revision'],'verified_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW','checks':checks,'issues':issues,'status':'PASS_STATIC_SCOPE_AND_PORTABILITY' if not issues else 'CHANGES_REQUIRED','files':len(final),'protected_files':len(protected),'changed_existing':len(changed),'new':2}
(REC/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False));raise SystemExit(bool(issues))
