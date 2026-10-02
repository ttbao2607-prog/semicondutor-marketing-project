"""Bounded offline vector pilot; preserves all cold assets. Stdlib only."""
from pathlib import Path
import json, hashlib, base64, textwrap, html, csv, subprocess
OUT=Path(__file__).resolve().parent
ROOT=OUT.parents[2]
caption='Digiwin chia sẻ tài liệu ngành tại Đài Loan cho nhóm chất lượng OSAT (đóng gói và kiểm thử thuê ngoài) đang cân nhắc cách quản trị thông tin.'
source='Nguồn: tài liệu ngành bán dẫn Digiwin tại Đài Loan.'
items=[
('Khi rà soát kiểm thử bất thường','Bạn cần xem căn cứ gì khi cân nhắc một nhà cung cấp cho bài toán quản trị thông tin?', 'Bắt đầu từ bài toán chất lượng', 'HỒ SƠ · NGỮ CẢNH · NGƯỜI PHỤ TRÁCH'),
('Một nguồn để tìm hiểu Digiwin','Tài liệu ngành tại Đài Loan của Digiwin đặt ERP (hoạch định nguồn lực doanh nghiệp) và MES (quản lý thực thi sản xuất) trong bối cảnh bán dẫn.', 'Tài liệu ngành tại Đài Loan', 'ERP · MES · BÁN DẪN'),
('Đọc rõ phạm vi của bằng chứng','Đây là tài liệu ngành tại Đài Loan. Khi cân nhắc giải pháp, bạn vẫn cần đối chiếu với quy trình và yêu cầu thực tế của nhà máy mình.', 'Đối chiếu với nhà máy của bạn', 'ĐÀI LOAN · BỐI CẢNH NGÀNH'),
('Từ góc nhìn ngành đến câu hỏi cụ thể','Hồ sơ cần đối chiếu nằm ở đâu? Ai phụ trách thông tin? Phần nào cần đánh giá thêm cùng nhóm kỹ thuật?', 'Mang theo câu hỏi của nhóm', 'HỒ SƠ → NGƯỜI PHỤ TRÁCH → ĐÁNH GIÁ'),
('Tìm hiểu theo bài toán của bạn','Đọc thêm góc nhìn của Digiwin về quản trị thông tin trong đóng gói và kiểm thử bán dẫn.', 'Đọc thêm về bài toán OSAT', 'TÌM HIỂU THÊM')]
logo_path=ROOT/'operations/linkedin-awareness-execution/production-r3/dependencies/digiwin-logo.webp'
logo='data:image/webp;base64,'+base64.b64encode(logo_path.read_bytes()).decode()
records=[]
def lines(text,width,size,x,y,weight='400',color='#1e293b'):
 return ''.join(f'<text x="{x}" y="{y+i*size*1.34}" font-family="Arial,sans-serif" font-size="{size}" font-weight="{weight}" fill="{color}">{html.escape(t)}</text>' for i,t in enumerate(textwrap.wrap(text,width)))
for i,(title,body,native,cue) in enumerate(items,1):
 svg=f'''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1080" height="1080" viewBox="0 0 1080 1080"><rect width="1080" height="1080" fill="#f8fafc"/><rect x="0" y="0" width="18" height="1080" fill="#0891b2"/><image x="76" y="52" width="230" height="80" href="{logo}"/><text x="940" y="106" font-family="Arial" font-size="30" fill="#475569">{i}/5</text><text x="76" y="188" font-family="Arial" font-size="25" fill="#475569">GÓC NHÌN QUẢN TRỊ BÁN DẪN</text>{lines(title,28,58,76,280,'700')}{lines(body,37,46,76,490)}<rect x="76" y="790" width="928" height="76" rx="12" fill="#e9eff8"/>{lines(cue,49,26,100,836,'700','#075985')}{lines(source if i in (2,3) else 'Digiwin · Góc nhìn quản trị thông tin',43,34,76,932,'400','#475569')}<path d="M76 992 H1004" stroke="#cbd5e1" stroke-width="2"/></svg>'''
 (OUT/f'R{i}.svg').write_text(svg,encoding='utf-8')
 records.append(dict(id=f'R{i}',caption=caption,image_headline=title,image_body=body,native_headline=native,alt=f'{title}. {body}',cue=cue,source=source if i in (2,3) else '',sequence=f'{i}/5',destination='https://solutions.digiwin.com.vn/semiconductor-osat?lang=vi',image='data:image/svg+xml;base64,'+base64.b64encode(svg.encode()).decode()))
for rec in records:
 png=OUT/(rec['id']+'.png')
 if png.exists():rec['image']='data:image/png;base64,'+base64.b64encode(png.read_bytes()).decode()
copy={'revision':'quality-rmk-r1','locale':'vi','format':'carousel-image/vector-offline-pilot','status':'OFFLINE_DRAFT_HUMAN_PENDING','records':[{k:v for k,v in r.items() if k!='image'} for r in records]}
(OUT/'copy-vi.json').write_text(json.dumps(copy,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(OUT/'copy-vi.md').write_text('# Quality RMK R1 exact copy\n\nCaption: '+caption+'\n\n'+'\n\n'.join(f"## {r['id']}\n\nHeadline: {r['image_headline']}\n\nBody: {r['image_body']}\n\nNative headline: {r['native_headline']}\n\nCue: {r['cue']}\n\nSource: {r['source']}" for r in records),encoding='utf-8')
template=(ROOT/'operations/linkedin-awareness-execution/r2-complete-carousel/template.html').read_text(encoding='utf-8')
template=template.replace("['A','B']","['R']").replace("group==='A'?'A · O1 · Tình huống':'B · O4-Q · Ba câu hỏi'","'RMK · Quality · Nguồn ngành Đài Loan'")
start=template.index('<header class="review">');end=template.index('<main class="workspace"')
template=template[:start]+'''<header class="review"><h1>Quality RMK R1 · Pilot offline 5 card</h1><p class="intro">Nối cold O1/O4-Q tới tài liệu ngành Digiwin tại Đài Loan. Proof bổ trợ chuyên môn, không phải case chứng minh xử lý kiểm thử bất thường. Pilot vector gốc; PNG export 1080 vuông. Chưa native account QA.</p><div class="tools"><button data-mode="desktop" aria-pressed="true">Desktop 640</button><button data-mode="mobile" aria-pressed="false">Mobile 390</button><button id="reset">Về card đầu</button></div></header><details class="limits"><summary>Phạm vi review và nguồn</summary>PR01, tài liệu ngành Digiwin tại Đài Loan. Không số liệu, customer logo, kết quả hay guarantee. Tệp RMK trực tiếp từ cold carousel chưa verified. Destination và social bất hoạt. Bảo review advertiser, phạm vi nguồn và liên quan pain; chưa buyer/live approval.</details>'''+template[end:]
template=template.replace('width:32px;height:32px','width:44px;height:44px').replace('.dot{width:9px;height:9px','.dot{width:24px;height:24px')
template=template.replace('__COPY_JSON__',json.dumps({'records':records},ensure_ascii=False).replace('</','<\\/')).replace('__LOGO_URI__',logo)
template=template.replace('</script></body>','''const q=new URLSearchParams(location.search);if(q.get('mode')==='mobile')document.querySelector('[data-mode="mobile"]').click();if(q.has('card'))states.forEach(s=>s.set(Number(q.get('card'))-1));
const checks=[];for(const s of states){for(let n=0;n<5;n++){s.set(n);checks.push({card:n+1,ordinal:document.querySelector('.ordinal').textContent,prevDisabled:document.querySelectorAll('.arrow')[0].disabled,nextDisabled:document.querySelectorAll('.arrow')[1].disabled})}s.set(Number(q.get('card')||1)-1)}document.documentElement.dataset.qa=JSON.stringify(checks);
</script></body>''')
(OUT/'index.html').write_text(template,encoding='utf-8')
inputs=['operations/linkedin-awareness-execution/r2-complete-carousel/copy-vi.json','operations/linkedin-awareness-execution/r2-complete-carousel/rendered-copy.json','operations/linkedin-awareness-execution/r2-complete-carousel/human-review-receipt.md','operations/linkedin-rmk-proof/proof-ledger.md','operations/linkedin-rmk-proof/source-map.json','operations/linkedin-rmk-proof/implementation-manifest.json']
pins=[{'path':p,'revision':subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),'workspace_sha256':hashlib.sha256((ROOT/p).read_bytes()).hexdigest()} for p in inputs]
(OUT/'source-map.json').write_text(json.dumps({'revision':'quality-rmk-r1','inputs':pins,'proof_id':'PR01','official_url':'https://www.digiwin.com.tw/dsc/solution/semiconductor/index','observed_in_research':'2026-10-02','reopen_attempt':'2026-10-02 web fetch timed out; retained prior research observation, not fresh retrieval','allowed_scope':'metric-free Taiwan semiconductor ERP/MES context; no result/customer marks','artwork':'repo-native original vector, no photos or simulated product screen'},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (OUT/'manifest.csv').open('w',encoding='utf-8',newline='') as f:
 w=csv.writer(f);w.writerow(['path','sha256','bytes'])
 for p in sorted(OUT.iterdir()):
  if p.name in ['manifest.csv','human-review-receipt.md'] or p.is_dir():continue
  w.writerow([p.name,hashlib.sha256(p.read_bytes()).hexdigest(),p.stat().st_size])
assert len(caption)<=150
print('Built 5 SVG cards + exact copy + self-contained demo + input source pins. Caption',len(caption))
