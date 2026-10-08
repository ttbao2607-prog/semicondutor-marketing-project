"""One-off Phase 3 folder builder. Source worktrees are read-only."""
import argparse, hashlib, html, json, pathlib, re, shutil
from datetime import datetime, timezone

ROOT = pathlib.Path(__file__).resolve().parents[3]
MAIN = pathlib.Path('D:/Digiwin_Semiconducter_Workspace')
OUT = ROOT / 'deliverables/manager-package-v2/2026-10-07'
REC = pathlib.Path(__file__).parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
esc = html.escape

PROPOSAL = '''# Đề xuất paid ads cho chuỗi cung ứng bán dẫn

**Gửi:** Vy  
**Phụ trách paid:** Bảo  
**Ngày:** 07/10/2026

Bảo đề xuất ngân sách tối đa **11,7 triệu đồng, chưa thuế**, để tiếp cận đúng doanh nghiệp trong chuỗi cung ứng bán dẫn và điện tử, tạo sự quan tâm đến bài toán quản trị và dẫn người đọc vào nội dung giải thích, case và giải pháp Digiwin. Vy xem giúp Bảo phương án và ba điểm ở cuối để tổng hợp, trình lãnh đạo.

## Tiếp cận ai, bằng thông điệp nào?

Tập trung vào doanh nghiệp làm PCB, substrate, linh kiện, vật liệu đóng gói và gia công chính xác cho thiết bị. Nội dung và tệp tiếp cận tách riêng theo hai nhóm.

- **Nội địa, tiếng Việt:** ERP là bước chuẩn bị năng lực quản trị, hồ sơ, quy trình và dữ liệu để đáp ứng yêu cầu của khách hàng trong chuỗi cung ứng bán dẫn.
- **FDI, English/Chinese:** mở bằng vấn đề vận hành của người phụ trách, rồi làm rõ giá trị về thời gian, phối hợp, trách nhiệm và kiểm soát rủi ro. Bảo chọn ngôn ngữ theo nhóm người đọc.

LinkedIn bắt đầu bằng ảnh đơn cho người đọc mới. Khi tệp người đã tương tác với chính các quảng cáo mới đủ điều kiện, carousel giúp giải thích sâu hơn. Trang đọc case nối vấn đề của người đọc với cơ chế giải pháp và lời mời trao đổi nhu cầu.

## Ngân sách chưa thuế

| Khoản | Mức đề xuất | Cách sử dụng |
|---|---:|---|
| Đợt LinkedIn đầu | 5.600.000 đồng | Chọn một nhóm phù hợp và ít mẫu đại diện để tập trung ngân sách, quan sát phân phối và mức quan tâm. |
| LinkedIn tiếp theo | Tối đa 5.600.000 đồng | Tiếp tục phần hiệu quả, thay đoạn cần cải thiện hoặc dùng remarketing khi tệp đủ điều kiện. |
| Search tùy chọn | Tối đa 500.000 đồng | Thử từ khóa thương mại phù hợp trong phạm vi nhỏ, chi theo lượng tìm kiếm thực tế. |
| **Tổng** | **11.700.000 đồng** | Trần ngân sách cho toàn phương án. |

**6,1 triệu đồng giữ lại nằm trong tổng 11,7 triệu**, gồm LinkedIn tiếp theo và Search tùy chọn. Bảo quản lý, điều phối số tiền trên dashboard; kế toán xử lý thuế và thanh toán theo quy trình công ty.

## Chạy tuần đầu, review rồi chọn hướng tuần 2

Tuần 1 chạy đúng plan. Cuối tuần, Bảo review dữ liệu để chọn hướng tuần 2 trong trần ngân sách đề xuất.

Bảo xác định vấn đề nằm ở tệp tiếp cận, phân phối, đo lường hay từng đoạn nội dung. Đoạn nào yếu thì thay đúng đoạn đó, giữ phần đang hiệu quả. Hai luồng VN tuần 1/tuần 2 và thư viện FDI giúp Bảo đổi nội dung linh hoạt; tệp chính và tệp dự phòng giúp chọn cách tiếp cận phù hợp. Mỗi luồng giữ đúng người đọc, ngôn ngữ và thông điệp.

Quy mô tệp sau lọc quyết định phạm vi thử ban đầu. Khi mức tiếp cận hạn chế hoặc dữ liệu còn mỏng, Bảo thu hẹp phép thử, quan sát thêm hoặc giữ lại ngân sách theo chất lượng tín hiệu và mức chi thực tế.

## Đo gì để quyết định tiếp tục?

| Điều cần đánh giá | Dữ liệu theo dõi | Cách dùng khi review |
|---|---|---|
| Tiếp cận đúng doanh nghiệp và người phụ trách | Phân phối theo công ty, chức năng và cấp bậc | Đối chiếu quảng cáo có tới đúng nhóm cần tiếp cận. |
| Có cơ hội thấy và chú ý | Reach, impressions, frequency, CTR và engagement | Đọc mức tiếp cận, lặp lại và quan tâm trong cùng kỳ. |
| Người quan tâm có đi tiếp | Phiên có tương tác trên trang đọc và nội dung giải thích/case theo nguồn đo tương ứng | Chọn đoạn giúp người đọc tìm hiểu sâu hơn và đoạn cần điều chỉnh. |
| Sử dụng tiền có hợp lý | Chi dashboard, CPM/CPC và ngân sách còn lại | Quyết định phần tiếp tục, điều chỉnh hoặc giữ lại. |

Lead đã xác minh là tín hiệu thương mại bổ sung. Bảo đọc kết quả cùng lượng dữ liệu và độ tin cậy của kỳ review, rồi gửi Vy nhận định và đề xuất bước tiếp theo.

## Ba điểm Vy xem giúp Bảo

### 1. Mức đầu tư

**Vy thấy trần 11,7 triệu đồng, chưa thuế, phù hợp để trình cho phương án này chứ?**

Bảo đề xuất giữ mức này để triển khai đợt đầu và có ngân sách cho bước tiếp theo theo kết quả thực tế.

Vy có thể phản hồi: **Đồng ý / Góp ý mức đầu tư / Đề nghị dừng phương án**.

### 2. Cơ cấu sử dụng ngân sách

**Vy đồng ý cơ cấu 5,6 triệu cho đợt đầu và 6,1 triệu giữ lại trong cùng tổng ngân sách chứ?**

Phần giữ lại gồm tối đa 5,6 triệu LinkedIn tiếp theo và tối đa 0,5 triệu Search. Bảo điều chỉnh cách sử dụng theo dữ liệu trong trần được duyệt.

Vy có thể phản hồi: **Đồng ý / Góp ý cơ cấu chi / Đề nghị đổi cơ cấu**.

### 3. Cách đánh giá hiệu quả

**Vy đồng ý đánh giá đợt đầu theo đúng tệp, mức quan tâm, hành vi đi tiếp và chi phí, với lead đã xác minh là tín hiệu bổ sung chứ?**

Bảo dùng review cuối tuần 1 để chọn hướng tuần 2 và cách sử dụng ngân sách. Kết quả được đọc cùng độ tin cậy và lượng dữ liệu thực tế.

Vy có thể phản hồi: **Đồng ý / Góp ý tiêu chí đánh giá / Đề nghị đổi cách đánh giá**.
'''

EMAIL = '''# Mail gửi Vy

**Tiêu đề:** Đề xuất paid ads chuỗi cung ứng bán dẫn – ngân sách 11,7 triệu chưa thuế

Vy ơi,

Bảo gửi Vy phương án paid ads cập nhật cho nhóm doanh nghiệp trong chuỗi cung ứng bán dẫn và điện tử. Hướng nội dung tách riêng: tiếng Việt tập trung vào chuẩn bị năng lực quản trị để tham gia chuỗi; English/Chinese mở từ vấn đề vận hành và giá trị đối với người phụ trách ở doanh nghiệp FDI.

Bảo đề xuất tổng ngân sách tối đa **11,7 triệu đồng, chưa thuế**: 5,6 triệu cho đợt LinkedIn đầu; 6,1 triệu giữ lại trong cùng tổng ngân sách, gồm tối đa 5,6 triệu LinkedIn tiếp theo và 0,5 triệu Search tùy chọn. Bảo theo dõi số tiền trên dashboard, kế toán xử lý thuế và thanh toán theo quy trình công ty.

Tuần 1 Bảo chạy đúng plan, review cuối tuần rồi chọn hướng tuần 2 theo dữ liệu. Bảo đã có hai luồng VN, thư viện FDI và tệp chính/dự phòng để thay đúng đoạn cần cải thiện, giữ phần đang hiệu quả.

Vy mở **BAT_DAU.html** trong thư mục để xem đề xuất, demo nội dung và file theo dõi. Bảo nhờ Vy xem giúp ba điểm để tổng hợp, trình lãnh đạo:

1. Trần đầu tư 11,7 triệu đồng, chưa thuế.
2. Cơ cấu 5,6 triệu đợt đầu và 6,1 triệu giữ lại trong cùng tổng ngân sách.
3. Đánh giá theo đúng tệp, mức quan tâm, hành vi đi tiếp và chi phí; lead đã xác minh là tín hiệu bổ sung.

Vy phản hồi đồng ý hoặc góp ý ngay dưới từng điểm giúp Bảo nhé. Bảo phụ trách triển khai và gửi Vy kết quả cùng đề xuất sau review tuần đầu.

Cảm ơn Vy,
Bảo
'''

CSS = '''*{box-sizing:border-box}html{scroll-behavior:smooth}body{margin:0;background:#f8fafc;color:#1e293b;font:17px/1.65 Arial,sans-serif}a{color:#174db3;text-decoration-thickness:1px;text-underline-offset:3px}a:hover{color:#103471}a:focus-visible,button:focus-visible,summary:focus-visible{outline:3px solid #ea580c;outline-offset:4px}header{background:white;border-bottom:1px solid #e2e8f0}nav{max-width:1120px;margin:auto;padding:18px 24px;display:flex;gap:22px;align-items:center;flex-wrap:wrap}nav strong{margin-right:auto;color:#1e293b}nav a{font-size:15px;min-height:44px;display:flex;align-items:center}main{max-width:1120px;margin:auto;padding:42px 24px 64px}h1{font-size:clamp(30px,4.2vw,49px);line-height:1.16;letter-spacing:-.9px;margin:12px 0 22px;max-width:860px}h2{font-size:27px;line-height:1.3;margin:36px 0 15px}h3{font-size:21px;line-height:1.4}p{margin:12px 0 20px}small,.muted{color:#475569}.eyebrow{font-size:13px;letter-spacing:1.4px;color:#174db3;font-weight:700;text-transform:uppercase}.lead{font-size:20px;max-width:880px}.card{background:white;border:1px solid #e2e8f0;border-radius:15px;padding:25px}.grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.two{grid-template-columns:repeat(2,1fr)}.stat{font-size:36px;font-weight:700;line-height:1.3;margin:8px 0}.button,button{font:inherit;display:inline-flex;align-items:center;justify-content:center;padding:10px 18px;min-height:44px;border:1px solid #cbd5e1;border-radius:8px;background:white;color:#1e293b;text-decoration:none;cursor:pointer}.button.primary{background:#2563eb;color:white;border-color:#2563eb}.actions{display:flex;flex-wrap:wrap;gap:12px;margin:24px 0}.table-wrap{overflow-x:auto;margin:18px 0 26px}table{border-collapse:collapse;width:100%;font-size:16px}th{background:#edf3fd;text-align:left}th,td{padding:15px 16px;border-bottom:1px solid #e2e8f0;vertical-align:top;min-width:145px}td:nth-child(2){min-width:175px}article.report{max-width:920px;margin:auto;background:white;border:1px solid #e2e8f0;padding:36px;border-radius:15px}article.report h1{font-size:36px}.flow{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.step{border-top:3px solid #2563eb;padding-top:16px}.step b{display:block;font-size:19px}.library{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}.thumb{width:100%;height:auto;aspect-ratio:1;object-fit:contain;border-radius:10px;background:#f1f5f9}.library h3{margin-bottom:8px}.filters{display:flex;gap:8px;flex-wrap:wrap;margin:22px 0}.filters button[aria-pressed=true],.stages button[aria-pressed=true]{background:#174db3;color:white}.feed{max-width:640px;margin:25px auto;background:white;border:1px solid #d5deeb;border-radius:12px;overflow:hidden}.feed.small{max-width:333px}.brand{padding:18px 20px;font-weight:700}.brand small{display:block;font-weight:400;font-size:13px}.caption{padding:0 20px 18px;white-space:pre-line}.art{display:block;width:100%;height:auto}.native{padding:16px 20px;font-weight:700}.controls{display:flex;gap:12px;align-items:center;justify-content:space-between;padding:16px 20px;flex-wrap:wrap}.controls span{font-size:14px;color:#475569}button:disabled{cursor:default;opacity:.4}.stages{display:flex;gap:8px;flex-wrap:wrap}.journey-heading{max-width:820px}.reading{padding:0 20px 20px}.note{border-left:3px solid #2563eb;padding:12px 20px;background:#edf3fd}footer{max-width:1120px;margin:auto;padding:18px 24px 34px;color:#475569;font-size:14px}li{margin:7px 0}[hidden]{display:none!important}@media(max-width:760px){.grid,.two,.flow,.library{grid-template-columns:1fr}main{padding:28px 16px 40px}nav{gap:8px 16px;padding:12px 16px}nav strong{width:100%}article.report{padding:21px 17px}article.report h1{font-size:29px}.card{padding:21px}.lead{font-size:18px}h2{font-size:24px}th,td{padding:12px}.controls{padding:12px}.stat{font-size:31px}}@media(prefers-reduced-motion:reduce){html{scroll-behavior:auto}}'''

def markdown(text):
    def inline(s):
        return re.sub(r'\*\*(.*?)\*\*',r'<strong>\1</strong>',esc(s))
    blocks=[]; lines=text.strip().splitlines(); i=0
    while i<len(lines):
        line=lines[i].strip()
        if not line: i+=1; continue
        if line.startswith('|'):
            rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                row=lines[i].strip().strip('|').split('|'); i+=1
                if all(re.fullmatch(r'\s*[-:]+\s*',c) for c in row): continue
                tag='th' if not rows else 'td'
                rows.append('<tr>'+''.join(f'<{tag}>{inline(c.strip())}</{tag}>' for c in row)+'</tr>')
            blocks.append('<div class="table-wrap"><table>'+''.join(rows)+'</table></div>'); continue
        m=re.match(r'^(#{1,3}) (.*)',line)
        if m:
            n=len(m[1]); anchor=' id="ba-diem"' if m[2]=='Ba điểm Vy xem giúp Bảo' else ''
            blocks.append(f'<h{n}{anchor}>{inline(m[2])}</h{n}>'); i+=1; continue
        if line.startswith('- ') or re.match(r'^\d+\. ',line):
            ordered=not line.startswith('- '); items=[]
            while i<len(lines) and ((re.match(r'^\d+\. ',lines[i]) is not None) if ordered else lines[i].startswith('- ')):
                items.append('<li>'+inline(re.sub(r'^(?:- |\d+\. )','',lines[i]))+'</li>'); i+=1
            tag='ol' if ordered else 'ul'; blocks.append(f'<{tag}>'+''.join(items)+f'</{tag}>'); continue
        parts=[]
        while i<len(lines) and lines[i].strip() and not lines[i].startswith(('#','|','- ')):
            parts.append(inline(lines[i].strip())); i+=1
        blocks.append('<p>'+'<br>'.join(parts)+'</p>')
    return ''.join(blocks)

def page(title,body,prefix='',script='',lang='vi'):
    return f'<!doctype html><html lang="{lang}"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)} · Digiwin</title><style>{CSS}</style></head><body><header><nav><strong>Digiwin · Paid ads bán dẫn</strong><a href="{prefix}BAT_DAU.html">Bắt đầu</a><a href="{prefix}01_De_xuat/de_xuat.html">Đề xuất</a><a href="{prefix}02_Demo/index.html">Demo</a><a href="{prefix}03_Thu_vien/index.html">Thư viện</a></nav></header><main>{body}</main><footer>Bảo gửi Vy · 07/10/2026</footer>{script}</body></html>'

TITLES={'VN-W1':('Nội địa · Chuẩn bị năng lực quản trị','VN tuần 1'), 'VN-W2':('Nội địa · Chuẩn bị hệ thống và tiến độ','VN tuần 2'),
 'O1':('Quality · Đối chiếu kết quả theo lot','FDI · Quality'), 'O2':('Operations · Theo dõi vận hành theo lot','FDI · Operations'),
 'O3':('Operations và Finance · Hồ sơ cuối kỳ','FDI · Operations phối hợp Finance'),
 'O4-O':('Operations · Ba câu hỏi trước bàn giao','FDI · Operations phối hợp Quality'),
 'O4-Q':('Quality · Ba câu hỏi để đối chiếu kết quả','FDI · Quality phối hợp Operations')}
LANGS={'vi-VN':'Tiếng Việt','en':'English','zh-Hans':'中文 giản thể','zh-Hant':'中文 phồn thể'}

def prepare():
    assets=json.loads((ROOT/'operations/manager-package-v2/phase1/asset-register.json').read_text(encoding='utf-8'))['assets']
    groups=[]; decoder=json.JSONDecoder()
    for asset in assets:
        if asset['adoption']!='MAIN_PO_OFFLINE_ADOPTED': continue
        base=pathlib.PurePosixPath(asset['images'][0]['path']).parent.parent
        src=MAIN/base
        viewer=(src/'index.html').read_text(encoding='utf-8')
        if asset['segment']=='VN_DOMESTIC':
            raw=decoder.raw_decode(viewer.split('const stages=',1)[1])[0]
            rows=[dict(c,caption=st['caption'],stage=['cold','explanation','proof'][i]) for i,st in enumerate(raw) for c in st['cards']]
            family='VN-W1' if asset['id']=='ASSET-VN-W1' else 'VN-W2'
            reader='case-aplus.html'
        elif asset['id'].startswith('ASSET-O3'):
            rows=json.loads((src/'journey.json').read_text(encoding='utf-8'))['rows']
            rows=[dict(x['copy'],stage=x['stage'],caption=x['caption'],image=x['image']) for x in rows]
            family='O3'; reader='case-reader.html'
        else:
            m=re.search(r'const data\s*=\s*',viewer)
            rows=decoder.raw_decode(viewer[m.end():])[0]
            num=int(asset['id'].split('B')[1]); family='O1' if num<=3 else 'O2' if num<=6 else 'O4-O' if num<=9 else 'O4-Q'
            reader='case-reader.html'
        assert len(rows)==10,asset['id']
        images={pathlib.PurePosixPath(x['path']).name:x for x in asset['images']}
        clean=[]
        for row in rows:
            pin=images[pathlib.PurePosixPath(row['image']).name]
            assert sha(MAIN/pin['path'])==pin['sha256'],pin['path']
            clean.append({'stage':row['stage'],'caption':row['caption'],'headline':row.get('native_headline') or row.get('headline',''),
                          'alt':row.get('alt',''), 'image':'assets/'+pathlib.PurePosixPath(pin['path']).name,
                          'source_image':pin['path'],'sha256':pin['sha256'], 'body':row.get('body','')})
        slug=asset['id'].removeprefix('ASSET-').lower()
        groups.append({'id':asset['id'],'slug':slug,'family':family,'title':TITLES[family][0],'persona':TITLES[family][1],
                       'locale':asset['locale'],'language':LANGS[asset['locale']],'source_dir':str(base),'reader_name':reader,
                       'reader_sha256':sha(src/reader),'viewer_sha256':sha(src/'index.html'),'rows':clean})
    assert len(groups)==17
    pre={'artifact_revision':'package-v2-phase3-1.0','prepared_utc':datetime.now(timezone.utc).isoformat(),
         'proposal':PROPOSAL,'email':EMAIL,'groups':groups,
         'inputs':{p:sha(ROOT/p) for p in ['deliverables/manager-package-v2/phase2/De_xuat_dau_tu_paid_ads.md',
                    'operations/Vy_Email_Content_Anchor.md','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md',
                    'operations/manager-package-v2/Package_V2_Workflow_Anchor_2026-10-07.md',
                    'operations/manager-package-v2/phase1/asset-register.json']}}
    (REC/'prepared-copy.json').write_text(json.dumps(pre,ensure_ascii=False,indent=2),encoding='utf-8')
    transcript=['# Planned copy transcript · internal', '\n'+PROPOSAL,'\n'+EMAIL]
    seen=set()
    for g in groups:
        transcript.append('\n## '+g['id']+' · '+g['title']+' · '+g['language'])
        for i,r in enumerate(g['rows'],1):
            key=(r['caption'],r['headline'],r['body'])
            if key in seen: transcript.append(f'{i}. Exact previously listed copy; image bound separately.'); continue
            seen.add(key)
            transcript.append(f"{i}. {r['stage']} · {r['headline']}\n\n{r['caption']}\n\n{r['body']}")
    (REC/'Copy_Review_Transcript.md').write_text('\n\n'.join(transcript),encoding='utf-8')
    print(json.dumps({'prepared_groups':len(groups),'selected_placements':sum(len(g['rows']) for g in groups),'copy_transcript':str(REC/'Copy_Review_Transcript.md')},ensure_ascii=False))

def build():
    gate=json.loads((REC/'pregen-review.json').read_text(encoding='utf-8'))
    assert gate['verdict']=='MESSAGE_ANCHOR_PASS' and gate['prepared_copy_sha256']==sha(REC/'prepared-copy.json')
    pre=json.loads((REC/'prepared-copy.json').read_text(encoding='utf-8'))
    for p,digest in pre['inputs'].items(): assert sha(ROOT/p)==digest,p
    groups=pre['groups']; (OUT/'01_De_xuat').mkdir(parents=True,exist_ok=True)
    (OUT/'04_Theo_doi').mkdir(exist_ok=True); (OUT/'02_Demo').mkdir(exist_ok=True); (OUT/'03_Thu_vien').mkdir(exist_ok=True)
    def write(path,text):
        p=OUT/path; p.parent.mkdir(parents=True,exist_ok=True); p.write_text(text,encoding='utf-8')
    write('01_De_xuat/De_xuat_paid_ads.md',PROPOSAL)
    write('01_De_xuat/Mail_gui_Vy.md',EMAIL)
    write('01_De_xuat/de_xuat.html',page('Đề xuất gửi Vy','<article class="report">'+markdown(PROPOSAL)+'</article>','../'))
    write('01_De_xuat/mail_gui_Vy.html',page('Mail gửi Vy','<article class="report">'+markdown(EMAIL)+'</article>','../'))
    home='''<p class="eyebrow">Đề xuất gửi Vy · 07/10/2026</p><h1>Tiếp cận doanh nghiệp<br>trong chuỗi cung ứng bán dẫn</h1><p class="lead">Bảo đề xuất tập trung đúng tệp, mở bằng vấn đề quản trị và dẫn người quan tâm tới nội dung giải thích, case và giải pháp Digiwin.</p><div class="grid"><section class="card"><small>Trần đầu tư · chưa thuế</small><div class="stat">11,7 triệu</div><p>Cho toàn phương án LinkedIn và Search tùy chọn.</p></section><section class="card"><small>Đợt LinkedIn đầu</small><div class="stat">5,6 triệu</div><p>Một nhóm phù hợp, ít mẫu đại diện để tập trung ngân sách.</p></section><section class="card"><small>Giữ lại trong cùng trần</small><div class="stat">6,1 triệu</div><p>Chọn bước tiếp theo theo dữ liệu và mức chi thực tế.</p></section></div><div class="actions"><a class="button primary" href="01_De_xuat/de_xuat.html">Xem phương án và ngân sách</a><a class="button" href="01_De_xuat/de_xuat.html#ba-diem">3 điểm Vy xem giúp Bảo</a></div><h2>Hai nhóm, hai hướng nội dung</h2><div class="grid two"><section class="card"><h3>Doanh nghiệp nội địa</h3><p>Tiếng Việt mở bằng việc chuẩn bị năng lực quản trị, hồ sơ và dữ liệu để đáp ứng yêu cầu của khách hàng trong chuỗi bán dẫn.</p></section><section class="card"><h3>Doanh nghiệp FDI</h3><p>English/Chinese mở từ vấn đề vận hành, rồi nối tới giá trị về thời gian, phối hợp, trách nhiệm và kiểm soát rủi ro.</p></section></div><h2>Từ lần đầu thấy đến tìm hiểu sâu</h2><div class="flow"><div class="step"><b>1. Ảnh đơn</b><p>Đặt vấn đề với người đọc mới.</p></div><div class="step"><b>2. Carousel</b><p>Giải thích cho người đã tương tác với chính các quảng cáo mới, khi tệp đủ điều kiện.</p></div><div class="step"><b>3. Trang đọc case</b><p>Làm rõ cơ chế và mở cuộc trao đổi về nhu cầu phù hợp.</p></div></div><p class="note">Tuần 1 chạy đúng plan. Review cuối tuần để chọn hướng tuần 2 theo dữ liệu, trong trần ngân sách đề xuất.</p><h2>Xem cùng phương án</h2><div class="grid"><section class="card"><h3>Demo nội dung</h3><p>Xem luồng VN và FDI từ ảnh đơn tới case.</p><a class="button" href="02_Demo/index.html">Mở demo</a></section><section class="card"><h3>Thư viện để thay nội dung</h3><p>Hai luồng VN và các chủ đề OSAT bằng English, giản thể, phồn thể.</p><a class="button" href="03_Thu_vien/index.html">Mở thư viện</a></section><section class="card"><h3>Theo dõi và review</h3><p>Ngân sách, chi dashboard và dữ liệu theo từng kỳ.</p><a class="button" href="04_Theo_doi/Theo_doi_paid_ads.xlsx">Mở file theo dõi</a></section></div><div class="actions"><a href="01_De_xuat/mail_gui_Vy.html">Xem nội dung mail</a><a href="01_De_xuat/De_xuat_paid_ads.md">Bản đề xuất dạng văn bản</a></div>'''
    write('BAT_DAU.html',page('Paid ads chuỗi cung ứng bán dẫn',home))
    cards=[]; demo=[]; selected=[]
    for g in groups:
        prefix='03_Thu_vien/'+g['slug']+'/'
        for r in g['rows']:
            target=OUT/prefix/r['image']; target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copyfile(MAIN/r['source_image'],target)
            assert sha(target)==r['sha256']
            selected.append({'path':str(target.relative_to(ROOT)).replace('\\','/'),'source':str(MAIN/r['source_image']).replace('\\','/'),'sha256':r['sha256'],'group':g['id'],'kind':'unchanged_png'})
        reader=(MAIN/g['source_dir']/g['reader_name']).read_text(encoding='utf-8')
        assert sha(MAIN/g['source_dir']/g['reader_name'])==g['reader_sha256']
        # Preserve case scope/locale. Remove the English pilot's operator footer from this business package.
        reader=reader.replace('case-aplus.html','case-reader.html')
        reader=reader.replace('../'+pathlib.PurePosixPath(g['source_dir']).name+'/index.html','index.html')
        reader=re.sub(r'href="index\.html(?:\?[^"#]*)?(?:#[^"]*)?"','href="index.html"',reader)
        if g['family']=='O3' and g['locale']=='en':
            reader=reader.replace('Published case result for the named China business. It does not establish a guaranteed close time, a Vietnam deployment or ERP-only causality.',
                                  'Reported for this China case using an integrated Digiwin ERP + iMES solution.')
            reader=re.sub(r'<p[^>]*>Offline English reading prepared from the existing source-pinned case content\. No form, tracking or simulated conversion\.</p>','',reader)
        write(prefix+'case-reader.html',reader)
        selected.append({'path':str((OUT/prefix/'case-reader.html').relative_to(ROOT)).replace('\\','/'),'source':str(MAIN/g['source_dir']/g['reader_name']).replace('\\','/'),'source_sha256':g['reader_sha256'],'sha256':sha(OUT/prefix/'case-reader.html'),'group':g['id'],'kind':'case_reader_with_local_return','editorial_change':'O3 English operator footer removed; scope restated as reported China ERP+iMES case result.' if g['family']=='O3' and g['locale']=='en' else 'Local return route only.'})
        data=[{k:r[k] for k in ['stage','caption','headline','alt','image']} for r in g['rows']]
        script='''<script>const data=DATA;let index=0;const el=id=>document.getElementById(id);function render(){const r=data[index];el('art').src=r.image;el('art').alt=r.alt;el('caption').textContent=r.caption;el('native').textContent=r.headline;el('position').textContent=(index+1)+' / '+data.length;el('original').href=r.image;el('prev').disabled=index===0;el('next').disabled=index===data.length-1;document.querySelectorAll('[data-stage]').forEach(b=>b.setAttribute('aria-pressed',String(b.dataset.stage===r.stage)))}el('prev').onclick=()=>{if(index>0)index--;render()};el('next').onclick=()=>{if(index<data.length-1)index++;render()};document.querySelectorAll('[data-stage]').forEach(b=>b.onclick=()=>{index=data.findIndex(r=>r.stage===b.dataset.stage);render()});el('size').onclick=()=>{let small=el('feed').classList.toggle('small');el('size').textContent=small?'Xem cỡ lớn':'Xem trong feed 333px';el('size').setAttribute('aria-pressed',String(small))};render();</script>'''.replace('DATA',json.dumps(data,ensure_ascii=False).replace('</','<\\/'))
        body=f'''<div class="journey-heading"><p class="eyebrow">{esc(g['persona'])} · {esc(g['language'])}</p><h1>{esc(g['title'])}</h1><p>Chọn từng chặng hoặc dùng “Tiếp” để xem nội dung. Thứ tự này minh họa cách nối thông điệp; phân phối quảng cáo thực tế phụ thuộc hành vi người đọc.</p></div><div class="stages"><button data-stage="cold" aria-pressed="true">1. Ảnh đơn</button><button data-stage="explanation" aria-pressed="false">2. Giải thích</button><button data-stage="proof" aria-pressed="false">3. Case</button><button id="size" aria-pressed="false">Xem trong feed 333px</button></div><article class="feed" id="feed"><div class="brand">Digiwin<small>Được tài trợ · Mô phỏng</small></div><p class="caption" id="caption" lang="{g['locale']}"></p><img id="art" class="art" width="1254" height="1254" alt=""><div class="native" id="native" lang="{g['locale']}"></div><div class="reading"><a class="button" href="case-reader.html">Đọc case và cơ chế giải pháp</a></div><div class="controls"><button id="prev">Trước</button><span id="position" aria-live="polite"></span><button id="next">Tiếp</button></div></article><div class="actions"><a href="../index.html">Về thư viện</a><a id="original" href="{data[0]['image']}">Mở ảnh gốc</a></div>'''
        write(prefix+'index.html',page(g['title'],body,'../../',script))
        card=f'''<section class="card" data-locale="{g['locale']}"><img class="thumb" loading="lazy" width="1254" height="1254" src="{g['slug']}/{data[0]['image']}" alt="{esc(data[0]['alt'])}"><small>{esc(g['language'])} · 10 ảnh</small><h3>{esc(g['title'])}</h3><p>{esc(g['persona'])}</p><a class="button" href="{g['slug']}/index.html">Xem luồng nội dung</a></section>'''
        cards.append(card)
        if g['id'] in ['ASSET-VN-W1','ASSET-B1']:
            demo.append(card.replace('src="'+g['slug']+'/', 'src="../03_Thu_vien/'+g['slug']+'/').replace('href="'+g['slug']+'/', 'href="../03_Thu_vien/'+g['slug']+'/'))
    write('02_Demo/index.html',page('Demo nội dung','<p class="eyebrow">Nội dung đại diện</p><h1>Hai luồng để Vy xem cách tiếp cận</h1><p class="lead">Một luồng VN về chuẩn bị năng lực quản trị và một luồng FDI về đối chiếu dữ liệu chất lượng. Mỗi luồng gồm ảnh đơn, carousel giải thích, case và trang đọc.</p><div class="library two">'+''.join(demo)+'</div><div class="actions"><a class="button" href="../03_Thu_vien/index.html">Xem các chủ đề và ngôn ngữ khác</a></div>','../'))
    filters='<div class="filters">'+''.join(f'<button data-filter="{value}" aria-pressed="{str(value=="all").lower()}">{label}</button>' for value,label in [('all','Tất cả'),*LANGS.items()])+'</div>'
    js='''<script>document.querySelectorAll('[data-filter]').forEach(b=>b.onclick=()=>{const value=b.dataset.filter;document.querySelectorAll('[data-locale]').forEach(c=>c.hidden=value!=='all'&&c.dataset.locale!==value);document.querySelectorAll('[data-filter]').forEach(x=>x.setAttribute('aria-pressed',String(x===b)))});</script>'''
    write('03_Thu_vien/index.html',page('Thư viện nội dung','<p class="eyebrow">Nội dung theo nhóm người đọc</p><h1>Thư viện để chọn và thay đúng đoạn</h1><p class="lead">Hai luồng VN tuần 1/tuần 2 và các chủ đề OSAT cho FDI. Bảo chọn nội dung theo vấn đề của kỳ review, người phụ trách và ngôn ngữ phù hợp.</p>'+filters+'<div class="library">'+''.join(cards)+'</div>','../',js))
    write('DOC_TRUOC.txt','Mở BAT_DAU.html để xem đề xuất, 3 điểm góp ý, demo, thư viện và file theo dõi.\nGiữ nguyên toàn bộ thư mục khi chuyển cho Vy để ảnh và các đường dẫn mở đúng.\nNội dung mail nằm ở 01_De_xuat/Mail_gui_Vy.md.\n')
    (REC/'selected-provenance.json').write_text(json.dumps({'revision':'package-v2-phase3-1.0','groups':[{k:v for k,v in g.items() if k!='rows'} for g in groups],'selections':selected},ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps({'folder':str(OUT),'groups':len(groups),'png_placements':len([x for x in selected if x['kind']=='unchanged_png']),'files_so_far':len(list(OUT.rglob('*')))},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--prepare',action='store_true'); parser.add_argument('--build',action='store_true'); args=parser.parse_args()
    if args.prepare: prepare()
    if args.build: build()
