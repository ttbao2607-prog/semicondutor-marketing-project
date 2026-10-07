import hashlib,html,json,pathlib,re,zipfile,xml.etree.ElementTree as ET
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from datetime import datetime,timezone
root=pathlib.Path(__file__).resolve().parents[3]; rec=pathlib.Path(__file__).parent
folder=root/'deliverables/manager-package-v2/2026-10-07'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
class Surface(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.text=[];self.skip=0
    def handle_starttag(self,tag,attrs):
        if tag in ['script','style']:self.skip+=1
        a=dict(attrs)
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
    def handle_endtag(self,tag):
        if tag in ['script','style']:self.skip=max(0,self.skip-1)
    def handle_data(self,text):
        if not self.skip:self.text.append(text)
checks=[];issues=[];bindings=[];readerTexts=[]
def check(name,okay,detail=None):
    checks.append({'check':name,'pass':bool(okay),'detail':detail})
    if not okay:issues.append({'check':name,'detail':detail})
for p in sorted(x for x in folder.rglob('*') if x.is_file()):
    bindings.append({'path':str(p.relative_to(folder)).replace('\\','/'),'sha256':sha(p),'bytes':p.stat().st_size})
    check('deliverable type: '+str(p.relative_to(folder)),p.suffix in ['.html','.md','.png','.xlsx','.txt'])
    if p.suffix in ['.html','.md','.txt']:
        raw=p.read_text(encoding='utf-8');bad=re.findall(r'(?i)SELF_REVIEW|INSUFFICIENT_EVIDENCE|PO_PENDING|MESSAGE_ANCHOR|CHANGES_REQUIRED|SCRIPT_REVIEW_PASS|sha256|native leaf|git hash|D:[/\\]|local commit|debug|upstream|agent.operator|harness|adapter|developing|NOT_FROZEN|source-pinned|No form, tracking or simulated conversion',raw)
        check('no internal payload: '+str(p.relative_to(folder)),not bad,sorted(set(bad)))
        if p.suffix=='.html':
            s=Surface();s.feed(raw)
            for link in s.links:
                uri=urlsplit(link)
                if uri.scheme or uri.netloc or not uri.path:continue
                target=(p.parent/unquote(uri.path)).resolve()
                check('relative dependency '+str(p.relative_to(folder))+' → '+link,target.is_relative_to(folder) and target.exists())
            if p.name=='case-reader.html':readerTexts.append({'path':str(p.relative_to(folder)), 'text':' '.join(s.text)})
            check('no external script: '+str(p.relative_to(folder)),not re.search(r'<script[^>]+src=',raw))
provenance=json.loads((rec/'selected-provenance.json').read_text(encoding='utf-8'))
for x in provenance['selections']:
    check('selected hash '+x['path'],sha(root/x['path'])==x['sha256'])
    if x['kind']=='unchanged_png':check('source hash '+x['path'],sha(pathlib.Path(x['source']))==x['sha256'])
check('17 approved groups',len(provenance['groups'])==17)
check('170 selected placements',sum(x['kind']=='unchanged_png' for x in provenance['selections'])==170)
proposal=(folder/'01_De_xuat/De_xuat_paid_ads.md').read_text(encoding='utf-8')
check('exactly 3 investment feedback points',len(re.findall(r'^### [1-3]\. ',proposal,re.M))==3)
check('name voice, not seniority',not re.search(r'(?i)anh/chị|chị Vy|anh Vy|em gửi',proposal+(folder/'01_De_xuat/Mail_gui_Vy.md').read_text(encoding='utf-8')))
book=folder/'04_Theo_doi/Theo_doi_paid_ads.xlsx'
if book.exists():
    with zipfile.ZipFile(book) as z:
        sheets=z.read('xl/workbook.xml').decode('utf-8')
        check('workbook exactly 2 sheets',sum(x.tag.rsplit('}',1)[-1]=='sheet' for x in ET.fromstring(sheets).iter())==2)
        check('workbook no hidden sheets',not re.search(r'state="(?:hidden|veryHidden)"',sheets))
        check('workbook no external links',not any('externalLink' in n for n in z.namelist()))
        allxml='\n'.join(z.read(n).decode('utf-8') for n in z.namelist() if n.endswith('.xml'))
        check('workbook no sample inputs', 'Sample QA' not in allxml and 'sample QA' not in allxml)
        check('workbook no internal payload',not re.search(r'SELF_REVIEW|INSUFFICIENT_EVIDENCE|sha256|D:[/\\]|harness|adapter',allxml,re.I))
check('one xlsx',len(list(folder.rglob('*.xlsx')))==1)
check('no ZIP delivery',not list(folder.rglob('*.zip')))
(rec/'reader-transcripts.json').write_text(json.dumps(readerTexts,ensure_ascii=False,indent=2),encoding='utf-8')
(rec/'final-file-manifest.json').write_text(json.dumps({'revision':'package-v2-phase3-1.0','folder':str(folder),'files':bindings},ensure_ascii=False,indent=2),encoding='utf-8')
result={'artifact_revision':'package-v2-phase3-1.0','verified_utc':datetime.now(timezone.utc).isoformat(),'reviewer':'/root','independence':'SELF_REVIEW','checks':checks,'issues':issues,'status':'PASS_STATIC_SELECTION_AND_PORTABILITY' if not issues else 'CHANGES_REQUIRED','files':len(bindings),'bytes':sum(x['bytes'] for x in bindings)}
(rec/'verification.json').write_text(json.dumps(result,ensure_ascii=False,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='checks'},ensure_ascii=False))
raise SystemExit(bool(issues))
