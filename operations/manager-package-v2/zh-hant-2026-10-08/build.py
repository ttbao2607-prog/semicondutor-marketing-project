"""Build static offline locale counterparts. Only seven presentation wrappers change."""
from pathlib import Path, PurePosixPath
from html.parser import HTMLParser
from html import escape, unescape
from urllib.parse import urlsplit, unquote
import hashlib, json, posixpath, re, sys, subprocess
from copy_deck import COPY, ALTS

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
ROOT = REPO / 'deliverables/manager-package-v2/2026-10-07'
PAGES = ['BAT_DAU.html', '01_De_xuat/de_xuat.html', '01_De_xuat/logic_quang_cao.html',
         '01_De_xuat/mail_gui_Vy.html', '02_Demo/index.html', '03_Thu_vien/index.html',
         '05_Evidence/evidence.html']

def sha(data): return hashlib.sha256(data).hexdigest()
def zh_path(path): return str(PurePosixPath(path).with_suffix('.zh-Hant.html'))
def write_json(name, value):
    (HERE/name).write_text(json.dumps(value, ensure_ascii=False, indent=2)+'\n', encoding='utf-8', newline='\n')

class Localizer(HTMLParser):
    def __init__(self, source):
        super().__init__(convert_charrefs=True)
        self.source=source; self.mode=''; self.edits=[]; self.missing=[]; self.nodes=0
        self.starts=[0]+[m.end() for m in re.finditer('\n',source)]
    def text_offset(self):
        line,col=self.getpos(); return self.starts[line-1]+col
    def attr(self, value):
        if value=='':return value
        if value in ALTS:return ALTS[value]
        if value in COPY:return COPY[value]
        for prefix, translated in [('Mở ảnh đầy đủ: ','開啟完整圖片：'), ('Xem ảnh lớn: ','放大圖片：')]:
            if value.startswith(prefix) and value[len(prefix):] in COPY:
                return translated+COPY[value[len(prefix):]]
        self.missing.append('ATTR '+value);return value
    def handle_starttag(self, tag, attrs):
        if tag in ['style','script']:self.mode=tag
        raw=self.get_starttag_text()
        def replace(m):return m.group(1)+m.group(2)+escape(self.attr(unescape(m.group(3))),quote=True)+m.group(2)
        updated=re.sub(r'((?:alt|aria-label|title|placeholder)\s*=\s*)([\"\'])(.*?)\2',replace,raw)
        if updated!=raw:self.edits.append((self.text_offset(),self.text_offset()+len(raw),updated))
    def handle_endtag(self, tag):
        if tag==self.mode:self.mode=''
    def handle_data(self, data):
        if self.mode or not data.strip():return
        key=data.strip();self.nodes+=1
        if key not in COPY:
            self.missing.append(key);return
        leading=data[:len(data)-len(data.lstrip())];trailing=data[len(data.rstrip()):]
        start=self.text_offset(); end=self.source.find('<',start)
        if end<0:end=len(self.source)
        self.edits.append((start,end,leading+escape(COPY[key],quote=False)+trailing))
    def result(self):
        s=self.source
        for a,b,new in sorted(self.edits,reverse=True):s=s[:a]+new+s[b:]
        return s

CSS='''<style id="package-locale-style">
.package-language-switch{display:inline-flex!important;align-items:center;gap:9px;min-height:44px;padding:4px 8px;border:1px solid #cbd5e1;border-radius:24px;background:#fff;color:#334155!important;text-decoration:none;white-space:nowrap;font:600 13px/1.3 Arial,"Microsoft JhengHei",sans-serif;max-width:100%}
.package-language-switch:focus-visible{outline:3px solid #ea580c;outline-offset:3px}.package-language-switch:hover{background:#f1f5f9}
.package-language-switch .language-track{display:block;position:relative;width:32px;height:20px;border-radius:12px;background:#64748b;flex:none}
.package-language-switch .language-track:after{content:"";position:absolute;top:3px;left:3px;width:14px;height:14px;border-radius:50%;background:#fff}
.package-language-switch[aria-checked="true"] .language-track{background:#174db3}.package-language-switch[aria-checked="true"] .language-track:after{left:15px}
.package-language-switch[aria-checked="false"] .language-vi,.package-language-switch[aria-checked="true"] .language-zh{color:#174db3}
.locale-evidence-toolbar{max-width:1140px;margin:auto;padding:18px 28px 0;display:flex;align-items:center;justify-content:space-between;gap:14px;flex-wrap:wrap}.locale-evidence-toolbar>a:first-child{color:#174db3;font-size:15px;min-height:44px;display:flex;align-items:center}
html[lang="zh-Hant"] body{font-family:"Microsoft JhengHei","PingFang TC","Noto Sans TC",Arial,sans-serif;line-height:1.75}html[lang="zh-Hant"] h1,html[lang="zh-Hant"] h2,html[lang="zh-Hant"] h3{letter-spacing:0;line-height:1.4}
@media(max-width:600px){.locale-evidence-toolbar{padding:14px 20px 0}.package-language-switch{font-size:12px;gap:7px}}
</style>'''
JS='''<script id="package-locale-script">
document.querySelectorAll('.package-language-switch').forEach(link=>{
link.addEventListener('keydown',event=>{if(event.key===' '){event.preventDefault();link.click();}});
link.addEventListener('click',()=>{const target=new URL(link.getAttribute('href'),location.href);target.search=location.search;target.hash=location.hash;link.href=target.href;});
});
</script>'''

def inject(s, page, chinese):
    counterpart=PurePosixPath(page).name if chinese else PurePosixPath(zh_path(page)).name
    label='切換為越南文' if chinese else 'Chuyển sang tiếng Trung phồn thể'
    switch=f'<a class="package-language-switch" href="{counterpart}" role="switch" aria-checked="{str(chinese).lower()}" aria-label="{label}"><span class="language-vi" lang="vi" aria-hidden="true">Tiếng Việt</span><span class="language-track" aria-hidden="true"></span><span class="language-zh" lang="zh-Hant" aria-hidden="true">繁體中文</span></a>'
    if page.startswith('05_Evidence/'):
        home='../BAT_DAU.zh-Hant.html' if chinese else '../BAT_DAU.html'
        back='← 返回提案首頁' if chinese else '← Về trang bắt đầu'
        s=s.replace('<body>',f'<body><div class="locale-evidence-toolbar"><a href="{home}">{back}</a>{switch}</div>',1)
    else:s=s.replace('</nav></header>',switch+'</nav></header>',1)
    return s.replace('</head>',CSS+'</head>',1).replace('</body>',JS+'</body>',1)

def localize(source,page):
    p=Localizer(source);p.feed(source)
    if p.missing:raise ValueError((page,p.missing))
    s=p.result().replace('<html lang="vi">','<html lang="zh-Hant">',1)
    def href(m):
        value=unescape(m.group(2));parts=urlsplit(value)
        if parts.scheme or parts.netloc or not parts.path:return m.group()
        resolved=posixpath.normpath(posixpath.join(posixpath.dirname(page),unquote(parts.path)))
        if resolved not in PAGES:return m.group()
        path=posixpath.relpath(zh_path(resolved),posixpath.dirname(page) or '.')
        return m.group(1)+path+('?' + parts.query if parts.query else '')+('#'+parts.fragment if parts.fragment else '')+m.group(3)
    s=re.sub(r'(href=")(.*?)(")',href,s)
    if page=='01_De_xuat/de_xuat.html':
        old='<p><strong>收件人：</strong> 你<br><strong>投放負責人：</strong> 我<br><strong>日期：</strong> 2026/10/08</p>'
        assert old in s
        s=s.replace(old,'<p class="eyebrow">越南市場 · 2026/10/08</p>',1)
    if page=='01_De_xuat/mail_gui_Vy.html':
        s=s.replace('<p>謝謝你！<br>我</p>','<p>謝謝你！</p>',1)
        s=s.replace('<strong>提案首頁</strong>','<a href="../BAT_DAU.zh-Hant.html">提案首頁</a>',1)
    if page.startswith('05_Evidence/'):
        s=s.replace("'Cỡ gốc'","'原始尺寸'").replace("'Vừa khung'","'符合視窗'")
    return inject(s,page,True),p.nodes

def main():
    baseline=HERE/'baseline-files.json'
    if baseline.exists(): records=json.loads(baseline.read_text(encoding='utf-8'))
    else:
        records=[{'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p.read_bytes())} for p in sorted(ROOT.rglob('*')) if p.is_file()]
        assert len(records)==226
        write_json('baseline-files.json',records)
    sources={}
    baseline_hashes={x['path']:x['sha256'] for x in records}
    # Rebuild from the exact checkpoint; private companion has its approved local source outside Git.
    for p in PAGES:
        data=(Path('D:/LinkedIn_Evidence_Cho_Vy_2026-10-08/BAT_DAU.html').read_bytes()
              if p.startswith('05_Evidence/') else subprocess.check_output(
                  ['git','show','686f55f733dcb510735a137315973bfebdc94b9b:deliverables/manager-package-v2/2026-10-07/'+p],cwd=REPO))
        assert sha(data)==baseline_hashes[p],p
        sources[p]=data.decode('utf-8')
    results={p:localize(s,p) for p,s in sources.items()}
    write_json('deck-check.json',{'pages':[{'path':p,'text_nodes':n,'unmapped':[]} for p,(_,n) in results.items()],
        'copy_deck_sha256':sha((HERE/'copy_deck.py').read_bytes()),'artwork':'NOT_GENERATED','postgen':'POSTGEN_NOT_RUN'})
    if '--build' not in sys.argv:print('DECK_CHECK_OK',len(results));return
    receipt=json.loads((HERE/'pregen-review.json').read_text(encoding='utf-8'))
    assert receipt['verdict']=='MESSAGE_ANCHOR_PASS'
    assert receipt['copy_deck_sha256']==sha((HERE/'copy_deck.py').read_bytes())
    for p in PAGES:
        (ROOT/p).write_text(inject(sources[p],p,False),encoding='utf-8',newline='\n')
        (ROOT/zh_path(p)).write_text(results[p][0],encoding='utf-8',newline='\n')
    write_json('build-result.json',{'presentation_pairs':7,'checkpoint':'686f55f733dcb510735a137315973bfebdc94b9b','locale':'zh-Hant','live':False,'commit_locale_changes':False})
    print('BUILT',len(results),'presentation pairs')

if __name__=='__main__':main()
