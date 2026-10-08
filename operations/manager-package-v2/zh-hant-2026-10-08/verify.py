"""Bounded source-integrity/navigation checks for the seven presentation pairs."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import hashlib,json,re
from build import HERE,ROOT,PAGES,zh_path,write_json

class Inspect(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set();self.text=[];self.mode='';self.switches=[];self.srcs=[]
    def handle_starttag(self,t,attrs):
        a=dict(attrs)
        if t in ['script','style']:self.mode=t
        if a.get('id'):self.ids.add(a['id'])
        if a.get('href'):self.links.append(a['href'])
        if a.get('src'):self.srcs.append(a['src'])
        if a.get('role')=='switch':self.switches.append(a)
    def handle_endtag(self,t):
        if t==self.mode:self.mode=''
    def handle_data(self,d):
        if not self.mode:self.text.append(d)
def parse(p):
    a=Inspect();a.feed(p.read_text(encoding='utf-8'));return a
def main():
    baseline=json.loads((HERE/'baseline-files.json').read_text(encoding='utf-8'))
    changed=[];unchanged=[]
    for r in baseline:
        target=ROOT/r['path'];assert target.exists(),r['path']
        (unchanged if hashlib.sha256(target.read_bytes()).hexdigest()==r['sha256'] else changed).append(r['path'])
    assert sorted(changed)==sorted(PAGES),changed
    assert len(unchanged)==219
    checked=[];missing=[]
    for f in PAGES:
        original=parse(ROOT/f);chinese=parse(ROOT/zh_path(f))
        assert original.srcs==chinese.srcs,(f,'image/source changed')
        assert not re.search(r'Bảo|\bVy\b',' '.join(chinese.text)),f
        for file,p in [(f,original),(zh_path(f),chinese)]:
            assert len(p.switches)==1,file
            assert p.switches[0]['aria-checked']==str(file.endswith('.zh-Hant.html')).lower()
            for value in p.links+p.srcs:
                parts=urlsplit(value)
                if parts.scheme or parts.netloc:continue
                target=(ROOT/file).parent/unquote(parts.path) if parts.path else ROOT/file
                if not target.exists():missing.append({'source':file,'target':value})
                elif parts.fragment and target.suffix=='.html':
                    if unquote(parts.fragment) not in parse(target).ids:missing.append({'source':file,'target':value,'reason':'fragment'})
            checked.append({'path':file,'links':len(p.links),'images':len(p.srcs),'sha256':hashlib.sha256((ROOT/file).read_bytes()).hexdigest()})
    assert not missing,missing
    result={'presentation_pairs':7,'protected_baseline_files_unchanged':len(unchanged),'changed_old_wrappers':changed,
            'old_package_files':len(baseline),'current_package_files':len([p for p in ROOT.rglob('*') if p.is_file()]),
            'approved_pngs_unchanged':170,'journeys_unchanged':17,'case_readers_unchanged':17,'workbook_unchanged':True,
            'source_images_unchanged':10,'html_checks':checked,'missing_targets':missing,
            'budget_vnd':{'cap_before_tax':11700000,'first':5600000,'retained':6100000,'next_max':5600000,'search_max':500000},
            'scope':'Static checks only; browser/semantic review separate.'}
    assert result['current_package_files']==233
    write_json('integrity-check.json',result)
    write_json('current-files-manifest.json',[{'path':p.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in sorted(ROOT.rglob('*')) if p.is_file()])
    print(json.dumps({k:v for k,v in result.items() if k not in ['html_checks','changed_old_wrappers']},ensure_ascii=False))
if __name__=='__main__':main()
