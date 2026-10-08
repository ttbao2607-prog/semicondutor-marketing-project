"""Assemble the reviewed ad-logic extension; historical builder is read-only."""
import hashlib, html, importlib.util, json, pathlib, re, subprocess

ROOT = pathlib.Path(__file__).resolve().parents[3]
REC = pathlib.Path(__file__).parent
OUT = ROOT/'deliverables/manager-package-v2/2026-10-07'
BASE = 'ecf87adc28cac2e39279824022ce98979efef142'
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
esc = html.escape
spec=importlib.util.spec_from_file_location('historical_builder',ROOT/'operations/manager-package-v2/phase3/build_package.py')
old=importlib.util.module_from_spec(spec);spec.loader.exec_module(old)

CSS='''
.logic-lead{max-width:850px}.logic-links{display:flex;gap:10px;flex-wrap:wrap;margin:24px 0}.logic-links a{padding:8px 13px;border:1px solid #cbd5e1;border-radius:8px;background:#fff;font-size:15px;min-height:44px;display:inline-flex;align-items:center;text-decoration:none}
.logic-flow{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin:22px 0}.logic-flow .step{background:#fff;padding:16px;border-radius:0 0 9px 9px;font-size:16px}.logic-flow p{margin:8px 0 0}.logic-number{color:#174db3;font-size:13px;font-weight:bold;letter-spacing:1px}
.logic-gallery{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin:20px 0}.logic-gallery figure{margin:0;min-width:0;background:#fff;border:1px solid #e2e8f0;border-radius:12px;overflow:hidden}.logic-gallery a{display:block}.logic-gallery img{width:100%;height:auto;display:block}.logic-gallery figcaption{padding:18px;font-size:16px;line-height:1.6}.logic-gallery b{display:block;margin-bottom:8px;font-size:17px}.logic-gallery figcaption p{margin:0}.logic-example{margin-top:30px;padding-top:20px;border-top:1px solid #cbd5e1}.logic-example h3{font-size:24px}.logic-section{scroll-margin-top:22px;margin-top:45px}.logic-mini h2{font-size:23px;margin-top:0}.logic-mini p{margin-bottom:10px}.logic-table th:first-child{width:40%}.logic-table caption{text-align:left;font-weight:bold;padding:0 0 12px}.logic-muted{font-size:15px;color:#475569}.logic-scope{border-left:3px solid #64748b;padding-left:16px}.logic-example .actions{margin-bottom:5px}
@media(max-width:760px){.logic-flow,.logic-gallery{grid-template-columns:1fr}.logic-gallery figure{max-width:440px;margin-inline:auto;width:100%}.logic-section{margin-top:34px}.logic-table,.logic-table thead,.logic-table tbody,.logic-table tr,.logic-table td,.logic-table caption{display:block;width:100%}.logic-table thead{position:absolute;width:1px;height:1px;overflow:hidden;clip-path:inset(50%)}.logic-table tr{background:#fff;border:1px solid #e2e8f0;border-radius:10px;margin:12px 0;padding:8px 0}.logic-table td{border:0;min-width:0;padding:8px 16px}.logic-table td:before{content:attr(data-label);display:block;color:#174db3;font-weight:bold;font-size:14px;margin-bottom:4px}.logic-mini{padding:18px}.logic-links{gap:8px}}
'''

def baseline(relative):
    path='deliverables/manager-package-v2/2026-10-07/'+relative
    return subprocess.check_output(['git','show',f'{BASE}:{path}'],cwd=ROOT).decode('utf-8')

def write(relative,text):
    (OUT/relative).write_text(text,encoding='utf-8',newline='\n')

def p(text,cls=''):
    return f'<p'+(f' class="{cls}"' if cls else '')+'>'+esc(text)+'</p>'

def nav(raw,prefix):
    needle=f'<a href="{prefix}01_De_xuat/de_xuat.html">Đề xuất</a>'
    assert raw.count(needle)==1
    return raw.replace(needle,needle+f'<a href="{prefix}01_De_xuat/logic_quang_cao.html">Logic quảng cáo</a>')

def markdown(text):
    # The historical renderer owns basic structure; add only local link support.
    raw=old.markdown(text)
    return re.sub(r'\[([^\]]+)\]\(([^)\s]+)\)',r'<a href="\2">\1</a>',raw)

def render_logic(c):
    md=[f"# {c['title']}",'**Bảo gửi Vy · Cập nhật 08/10/2026**',c['lead']]
    body='<p class="eyebrow">Cách tiếp cận · Bảo gửi Vy</p><h1>'+esc(c['title'])+'</h1>'+p(c['lead'],'lead logic-lead')
    body+='<div class="logic-links" aria-label="Nội dung trang">'+''.join(f'<a href="#{i}">{label}</a>' for i,label in [('tep','Chọn tệp'),('gia-thuyet','Hai giả thuyết'),('hinh-anh','Ví dụ hình ảnh'),('diem-cham','Mạch tiếp cận'),('du-lieu','Quyết định theo dữ liệu')])+'</div>'
    a=c['audience'];md += ['## '+a['title'],a['intro']]
    body+='<section id="tep" class="logic-section"><h2>'+esc(a['title'])+'</h2>'+p(a['intro'])+'<div class="logic-flow">'
    for i,(label,text) in enumerate(a['steps'],1):
        body+=f'<div class="step"><span class="logic-number">LỚP {i}</span><b>{esc(label)}</b>{p(text)}</div>';md += [f'{i}. **{label}:** {text}']
    body+='</div><div class="grid two">'
    for title,text in [a['primary'],a['backup']]:
        body+='<div class="card"><h3>'+esc(title)+'</h3>'+p(text)+'</div>';md += ['### '+title,text]
    body+='</div>'+p(a['dated'],'logic-muted')+p(a['locale'])+'</section>';md += [a['dated'],a['locale']]
    h=c['hypotheses'];body+='<section id="gia-thuyet" class="logic-section"><h2>'+esc(h['title'])+'</h2><div class="grid two">';md += ['## '+h['title']]
    for title,text,value in [h['vn'],h['fdi']]:
        body+='<div class="card"><h3>'+esc(title)+'</h3>'+p(text)+p(value,'logic-scope')+'</div>';md += ['### '+title,text,value]
    body+='</div>'+p(h['localization'])+'</section>';md += [h['localization']]
    v=c['visual'];body+='<section id="hinh-anh" class="logic-section"><h2>'+esc(v['title'])+'</h2>'+p(v['intro'])+p(v['anchor']);md += ['## '+v['title'],v['intro'],v['anchor']]
    for e in v['examples']:
        body+=f'<article id="vi-du-{e["id"]}" class="logic-example"><h3>{esc(e["title"])}</h3>'+p(e['intro'])+'<div class="logic-gallery">';md += ['### '+e['title'],e['intro']]
        for f in e['frames']:
            body+=f'<figure><a href="{esc(f["image"])}" aria-label="{esc("Mở ảnh đầy đủ: "+f["label"])}"><img src="{esc(f["image"])}" width="1254" height="1254" alt="{esc(f["alt"])}"></a><figcaption><b>{esc(f["label"])}</b>{p(f["text"])}</figcaption></figure>'
            md += [f'![{f["alt"]}]({f["image"]})',f'**{f["label"]}**',f['text']]
        body+='</div>'+p(e['value'],'logic-scope')+f'<div class="actions"><a class="button" href="{e["journey"]}">Xem toàn luồng</a><a class="button" href="{e["reader"]}">Đọc case</a></div></article>'
        md += [e['value'],f'[Xem toàn luồng]({e["journey"]}) · [Đọc case]({e["reader"]})']
    body+='</section>'
    j=c['journey'];body+='<section id="diem-cham" class="logic-section"><h2>'+esc(j['title'])+'</h2><div class="flow">';md += ['## '+j['title']]
    for title,text in j['steps']:
        body+='<div class="step"><b>'+esc(title)+'</b>'+p(text)+'</div>';md += [f'**{title}**',text]
    body+='</div>'+p(j['continuity'])+'</section>';md += [j['continuity']]
    m=c['matrix'];body+='<section id="du-lieu" class="logic-section"><h2>'+esc(m['title'])+'</h2>'+p(m['intro'])+'<table class="logic-table"><caption>Review cuối tuần 1 → lựa chọn tuần 2</caption><thead><tr><th scope="col">Tín hiệu quan sát</th><th scope="col">Hướng xử lý của Bảo</th></tr></thead><tbody>';md += ['## '+m['title'],m['intro']]
    table=['| Tín hiệu quan sát | Hướng xử lý của Bảo |','|---|---|']
    for signal,action in m['rows']:
        body+=f'<tr><td data-label="Tín hiệu">{esc(signal)}</td><td data-label="Hướng xử lý">{esc(action)}</td></tr>';table += [f'| {signal} | {action} |']
    body+='</tbody></table>'
    md.append('\n'.join(table))
    for key in ['learning','change','close']:
        body+=p(m[key]);md += [m[key]]
    body+='<div class="actions"><a class="button primary" href="de_xuat.html#ba-diem">Xem 3 điểm đầu tư</a><a class="button" href="../02_Demo/index.html">Mở demo</a></div></section>'
    md += ['[Xem 3 điểm đầu tư](de_xuat.html#ba-diem) · [Mở demo](../02_Demo/index.html)']
    return body,'\n\n'.join(md)+'\n'

if __name__ == '__main__':
    gate=json.loads((REC/'pregen-review.json').read_text(encoding='utf-8'))
    assert gate['verdict']=='MESSAGE_ANCHOR_PASS'
    for filename,key in [('prepared-copy.json','prepared_copy_sha256'),('build_extension.py','builder_sha256'),('source-bindings.json','source_bindings_sha256')]:
        assert sha(REC/filename)==gate[key],filename
    c=json.loads((REC/'prepared-copy.json').read_text(encoding='utf-8'))['copy']
    body,md=render_logic(c)
    raw=old.page(c['title'],body,prefix='../').replace('</style>',CSS+'</style>').replace('07/10/2026','08/10/2026')
    write('01_De_xuat/logic_quang_cao.html',nav(raw,'../'));write('01_De_xuat/Logic_quang_cao.md',md)
    proposal=baseline('01_De_xuat/De_xuat_paid_ads.md')
    insert='## Logic quảng cáo và cách điều chỉnh\n\n'+'\n\n'.join(c[k] for k in ['proposal_summary','proposal_hypothesis','proposal_matrix'])+'\n\n[Xem logic quảng cáo, hai ví dụ hình ảnh và matrix tuần 2](logic_quang_cao.html).\n\n'
    assert proposal.count('## Ngân sách chưa thuế')==1
    proposal=proposal.replace('## Ngân sách chưa thuế',insert+'## Ngân sách chưa thuế').replace('**Ngày:** 07/10/2026','**Ngày:** 08/10/2026')
    write('01_De_xuat/De_xuat_paid_ads.md',proposal)
    write('01_De_xuat/de_xuat.html',nav(old.page('Đề xuất paid ads', '<article class="report">'+markdown(proposal)+'</article>',prefix='../').replace('07/10/2026','08/10/2026'),'../'))
    mail=baseline('01_De_xuat/Mail_gui_Vy.md');needle='Vy mở **BAT_DAU.html**'
    assert mail.count(needle)==1
    mail=mail.replace(needle,c['mail_line']+'\n\n'+needle).replace('để xem đề xuất, demo nội dung và file theo dõi.','để xem đề xuất, logic quảng cáo, demo nội dung và file theo dõi.')
    write('01_De_xuat/Mail_gui_Vy.md',mail)
    write('01_De_xuat/mail_gui_Vy.html',nav(old.page('Mail gửi Vy','<article class="report">'+markdown(mail)+'</article>',prefix='../').replace('07/10/2026','08/10/2026'),'../'))
    home=baseline('BAT_DAU.html');needle='<div class="grid">'
    summary='<section class="note logic-mini"><h2>Vì sao chọn tệp này, nội dung này?</h2>'+p(c['home_line'])+'<a href="01_De_xuat/logic_quang_cao.html">Xem logic quảng cáo và hai ví dụ</a></section>'
    home=home.replace(needle,summary+needle,1).replace('</style>',CSS+'</style>').replace('07/10/2026','08/10/2026')
    home=home.replace('<a class="button primary" href="01_De_xuat/de_xuat.html">Xem phương án và ngân sách</a>','<a class="button primary" href="01_De_xuat/logic_quang_cao.html">Xem logic quảng cáo</a><a class="button" href="01_De_xuat/de_xuat.html">Xem phương án và ngân sách</a>')
    write('BAT_DAU.html',nav(home,''))
    for relative in ['02_Demo/index.html','03_Thu_vien/index.html']:
        raw=baseline(relative);note='<p class="note">Xem <a href="../01_De_xuat/logic_quang_cao.html">logic quảng cáo</a> để hiểu cách chọn tệp, vai trò từng nội dung và hướng điều chỉnh theo dữ liệu.</p>'
        raw=raw.replace('<main>','<main>'+note,1).replace('07/10/2026','08/10/2026');write(relative,nav(raw,'../'))
    write('DOC_TRUOC.txt','Mở BAT_DAU.html để xem logic quảng cáo, đề xuất và 3 điểm góp ý, demo, thư viện và file theo dõi.\nPhần logic quảng cáo có hai ví dụ VN/FDI và cách chọn hành động tuần 2 theo dữ liệu.\nGiữ nguyên toàn bộ thư mục khi chuyển cho Vy để ảnh và các đường dẫn mở đúng.\nNội dung mail nằm ở 01_De_xuat/Mail_gui_Vy.md.\n')
    print('Built ad-logic page and bounded package entrypoint updates. Images/journeys/readers/XLSX unchanged.')
