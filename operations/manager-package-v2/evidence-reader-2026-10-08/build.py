"""Build a portable reader from preserved evidence images. No image editing."""
from pathlib import Path
import base64
import hashlib
import html
import json
import shutil
from datetime import datetime, timezone

ROOT = Path('D:/LinkedIn_Package_V2_2026-10-07')
ARCHIVE = Path('D:/LinkedIn_Package_V2_Evidence_2026-10-08')
OUTPUT = Path('D:/LinkedIn_Evidence_Cho_Vy_2026-10-08')
RECORD = ROOT / 'operations/manager-package-v2/evidence-reader-2026-10-08'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(p, value):
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', encoding='utf-8', newline='\n') as f:
        f.write(value)

def save(p, value):
    write(p, json.dumps(value, ensure_ascii=False, indent=2) + '\n')

def main():
    assert not OUTPUT.exists(), 'Inspect existing reader before replacing it.'
    catalog = json.loads((ARCHIVE / '_truy_xuat_anh.json').read_text(encoding='utf-8'))
    source = {x['id']: x for x in catalog['entries']}
    groups = [
        ('tep-chinh', 'Tệp chính 424 công ty', 'Đối chiếu tên tệp đã lưu và trạng thái xử lý trên LinkedIn ngày 06/10/2026.', [
            ('IMG-L01', 'Tệp 424 công ty đã lưu', 'Tên tệp hiển thị trên LinkedIn khớp bản 424 công ty đã bổ sung định danh.', 'LinkedIn Campaign Manager · 06/10/2026'),
            ('IMG-L02', 'Trạng thái xử lý: Updating', 'LinkedIn hiển thị Updating. Mức 80% trên ảnh là số cũ trong lúc hệ thống xử lý bản thay thế.', 'LinkedIn Campaign Manager · 06/10/2026'),
        ]),
        ('backup', 'Tệp dự phòng 52 công ty và bộ lọc', 'Số thành viên dưới đây là ước tính của LinkedIn trong lần kiểm tra ngày 07/10/2026.', [
            ('IMG-L03', 'Tệp dự phòng đã ở trạng thái Ready', 'Màn hình hiển thị Ready, tỷ lệ khớp >90% và 444.274 thành viên. Phần chi tiết vẫn hiện 0 Companies, Matched(0), Unmatched(0), chưa có hàng công ty để đối soát.', 'LinkedIn Campaign Manager · 07/10/2026'),
            ('IMG-L04', 'Chọn đúng tệp công ty dự phòng', 'Bộ lọc chọn Company List R5-52. Đây là tệp nền để tiếp tục thu hẹp theo vai trò và cấp bậc.', 'LinkedIn Campaign Manager · 07/10/2026'),
            ('IMG-L05', 'Thu hẹp theo chức năng công việc', 'Giữ người thuộc tệp công ty và làm một trong bốn chức năng: Engineering, Information Technology, Operations hoặc Quality Assurance.', 'LinkedIn Campaign Manager · 07/10/2026'),
            ('IMG-L06', 'Ước tính với ngôn ngữ English', 'Màn hình hiển thị 460 thành viên với địa bàn Việt Nam và ngôn ngữ English. Phần hướng dẫn của LinkedIn cho biết lựa chọn English có thể tiếp cận cả hồ sơ dùng ngôn ngữ khác, ngoại trừ Sponsored Messaging.', 'LinkedIn Campaign Manager · 07/10/2026'),
            ('IMG-L07', 'Đối chiếu với ngôn ngữ Vietnamese', 'Khi chuyển sang Vietnamese ở bước lọc cuối, màn hình hiển thị dưới 300 thành viên tại Việt Nam.', 'LinkedIn Campaign Manager · 07/10/2026'),
        ]),
        ('planner', 'Kết quả tra cứu Keyword Planner', 'Cấu hình: Việt Nam · Google · 09/2025–08/2026. Dấu gạch ngang thể hiện chỉ số không được hiển thị trong truy vấn này; không thể diễn giải thành nhu cầu bằng 0.', [
            ('IMG-P01', 'Tra cứu bằng tiếng Anh', 'Bảy từ khóa trong cấu hình English đều hiển thị dấu gạch ngang tại các cột chỉ số.', 'Google Keyword Planner · 30/09/2026'),
            ('IMG-P02', 'Tra cứu bằng tiếng Trung giản thể', 'Bảy từ khóa trong cấu hình Chinese (simplified) đều hiển thị dấu gạch ngang tại các cột chỉ số.', 'Google Keyword Planner · 30/09/2026'),
            ('IMG-P03', 'Tra cứu bằng tiếng Trung phồn thể', 'Bảy từ khóa trong cấu hình Chinese (traditional) đều hiển thị dấu gạch ngang tại các cột chỉ số.', 'Google Keyword Planner · 30/09/2026'),
        ]),
    ]
    units = []
    for _, _, _, cards in groups:
        for id_, title, caption, credit in cards:
            entry = source[id_]
            p = ARCHIVE / entry['file']
            assert sha(p) == entry['source_sha256']
            units.append(dict(id=id_, title=title, caption=caption, credit=credit,
                              image_sha256=sha(p), archived_file=entry['file']))
    bindings = dict(revision='evidence-reader-v3', reviewer='/root', independence='SELF_REVIEW',
        reviewed_utc=datetime.now(timezone.utc).isoformat(), anchor_id='VY-CONTENT-ANCHOR',
        anchor_revision='1.0', anchor_sha256=sha(ROOT / 'operations/Vy_Email_Content_Anchor.md'),
        email_record_id='VY-MAIL-USER-20261006',
        email_sha256=sha(ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),
        scope='Bảo/Vy evidence reader, Vietnamese explanatory captions; not new advertising or buyer targeting.',
        protected_package_checkpoint='d521c5fdd6c4c29cc55bebdabb9edeea395c588b')
    write(RECORD / 'Execution_Contract.md', '''# Evidence reader correction · 08/10/2026

Goal: Bảo/Vy open a portable HTML and see all ten genuine evidence images with short natural captions. No Git/local-path/reviewer/hash/process language in the reader or reader folder.

Scope: new clean outside-Git reader folder, ten exact original image copies, embedded HTML images. Technical source records remain separate in operations. Original evidence/source receipts and approved package unchanged. Root owns work; no delegation, Git mutation, new account activity or image editing.

Acceptance: all ten embedded image bytes match archived originals; actual desktop and 375px browser render loads every image; zoom and close work; navigation and layout usable; rendered text has no internal implementation jargon/absolute paths; package manifest still matches 215 files. Source date and meaning stay within MSG-ANCHOR-01. Independent audit target is final HTML pixels/behavior plus archived bytes; reviewer is root SELF_REVIEW, not an independent agent.
''')
    save(RECORD / 'pregen-review.json', dict(bindings, stage='PREGEN_SCRIPT / EVIDENCE_READER',
        verdict='MESSAGE_ANCHOR_PASS', units=units, actual_render='POSTGEN_NOT_RUN',
        anchor_dispositions={
            'A1': 'No new ICP assertion; screenshots describe existing list configuration.',
            'A2': 'Ready/count does not certify entity customer fit; detail limitation stated.',
            'A3': 'English/Vietnamese estimates not represented as independent FDI/domestic pools.',
            'A4': 'No new ROI or delivery-result claim; figures explicitly estimates.',
            'A5': 'VN ERP readiness marketing message unchanged; this is a source-image reader.',
            'A6': 'No solution capability added.',
            'A7': 'Dated source→caption→zoom navigation consistent for all ten units.'}))
    OUTPUT.mkdir()
    body = []
    copied = []
    for section_id, heading, description, cards in groups:
        body.append(f'<section id="{section_id}"><div class="section-heading"><h2>{html.escape(heading)}</h2><p>{html.escape(description)}</p></div>')
        for id_, title, caption, credit in cards:
            entry = source[id_]
            src = ARCHIVE / entry['file']
            target = OUTPUT / 'Anh' / Path(entry['file']).name
            target.parent.mkdir(exist_ok=True)
            shutil.copyfile(src, target)
            mime = 'image/png' if src.suffix == '.png' else 'image/jpeg'
            data = 'data:' + mime + ';base64,' + base64.b64encode(src.read_bytes()).decode('ascii')
            body.append(f'''<article class="evidence-card">
<header class="card-header"><p class="credit">{html.escape(credit)}</p><h3>{html.escape(title)}</h3><p class="caption">{html.escape(caption)}</p></header>
<button class="image-button" type="button" data-image="{id_}" aria-label="Xem ảnh lớn: {html.escape(title, quote=True)}"><img id="{id_}" src="{data}" alt="{html.escape(title, quote=True)}"></button>
<div class="card-actions"><button class="expand" type="button" data-image="{id_}">Xem ảnh lớn <span aria-hidden="true">↗</span></button></div></article>''')
            copied.append(dict(id=id_, file=target.relative_to(OUTPUT).as_posix(), sha256=sha(target)))
        body.append('</section>')
    page = '''<!doctype html><html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Ảnh đối chiếu kế hoạch quảng cáo</title>
<style>
:root{--ink:#183047;--muted:#536779;--blue:#086da3;--line:#dbe4eb;--paper:#f3f6f9}*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:90px}body{margin:0;background:var(--paper);color:var(--ink);font:16px/1.6 "Segoe UI",Arial,sans-serif}button,a{-webkit-tap-highlight-color:transparent}button{font:inherit;cursor:pointer}button:focus-visible,a:focus-visible{outline:3px solid #e9a72c;outline-offset:4px}.hero{max-width:1140px;margin:auto;padding:48px 28px 30px}.eyebrow{margin:0 0 8px;color:var(--blue);font-size:13px;font-weight:700;letter-spacing:.08em;text-transform:uppercase}h1{margin:0 0 12px;font-size:clamp(28px,4vw,42px);line-height:1.2;letter-spacing:-.025em}.intro{max-width:760px;margin:0 0 18px;color:var(--muted)}.meta{display:flex;flex-wrap:wrap;gap:8px}.meta span{background:#e7eff5;border-radius:6px;padding:5px 11px;font-size:13px}.nav-wrap{position:sticky;top:0;z-index:3;background:rgba(255,255,255,.97);border-block:1px solid var(--line)}nav{max-width:1140px;margin:auto;padding:12px 28px;display:flex;gap:10px;flex-wrap:wrap}nav a{color:var(--ink);font-size:14px;font-weight:600;text-decoration:none;padding:6px 12px;border:1px solid var(--line);border-radius:6px}nav a:hover{background:#e8f3fa;border-color:#90bad0}main{max-width:1140px;margin:auto;padding:0 28px 40px}section{padding-top:36px}.section-heading{margin:0 0 22px}.section-heading h2{font-size:25px;line-height:1.3;margin:0 0 8px}.section-heading p{color:var(--muted);max-width:920px;margin:0}.evidence-card{background:white;border:1px solid var(--line);border-radius:12px;overflow:hidden;margin:0 0 24px;box-shadow:0 2px 8px #15334e06}.card-header{padding:22px 24px 18px}.credit{font-size:12px;color:var(--muted);margin:0 0 5px;font-weight:600}h3{font-size:20px;margin:0 0 8px;line-height:1.35}.caption{margin:0;color:#3e5366;max-width:980px}.image-button{display:block;width:100%;border:0;padding:0;background:#edf2f6;cursor:zoom-in}.image-button img{display:block;width:100%;height:auto}.card-actions{padding:10px 20px;border-top:1px solid var(--line);display:flex;justify-content:flex-end}.expand{color:var(--blue);border:0;background:transparent;padding:5px;font-size:14px;font-weight:600}footer{padding:22px 28px 32px;max-width:1140px;margin:auto;color:var(--muted);font-size:13px;border-top:1px solid var(--line)}dialog{padding:0;border:0;border-radius:10px;width:calc(100vw - 32px);max-width:1800px;height:calc(100vh - 32px);max-height:1100px;background:#f2f5f8;color:var(--ink)}dialog::backdrop{background:#0c1b2acc}.dialog-bar{height:64px;display:flex;align-items:center;gap:12px;padding:10px 18px;background:white;border-bottom:1px solid var(--line)}.dialog-bar h2{font-size:16px;line-height:1.3;margin:0;flex:1}.dialog-bar button{border:1px solid var(--line);border-radius:5px;background:white;padding:7px 12px;font-size:13px}.image-stage{height:calc(100% - 64px);overflow:auto;display:flex;align-items:flex-start;justify-content:center;padding:14px}.image-stage img{display:block;width:auto;height:auto;max-width:100%;max-height:100%;object-fit:contain}.image-stage.native{display:block}.image-stage.native img{max-width:none;max-height:none}.dialog-close{font-weight:700;color:var(--ink)}@media(max-width:600px){html{scroll-padding-top:112px}.hero{padding:28px 18px 22px}nav{padding:10px 14px;gap:6px}nav a{font-size:12px;padding:6px 9px}main{padding:0 14px 26px}section{padding-top:28px}.section-heading h2{font-size:22px}.section-heading p{font-size:14px}.card-header{padding:18px 16px 16px}h3{font-size:18px}.caption{font-size:14px}.evidence-card{border-radius:9px;margin-bottom:18px}.card-actions{padding:8px 12px}dialog{width:calc(100vw - 12px);height:calc(100dvh - 16px)}.dialog-bar{height:auto;min-height:72px;padding:10px;flex-wrap:wrap;gap:7px}.dialog-bar h2{flex-basis:100%;font-size:14px}.dialog-bar button{padding:5px 10px}.image-stage{height:calc(100% - 94px);padding:8px}footer{padding:20px 18px}}@media print{nav,.card-actions,dialog{display:none}.hero{padding-top:10px}body{background:white}.evidence-card{break-inside:avoid;box-shadow:none}main{padding-inline:0}}
</style></head><body>
<header class="hero"><p class="eyebrow">Hồ sơ tham khảo · LinkedIn & Google</p><h1>Ảnh đối chiếu kế hoạch quảng cáo</h1><p class="intro">Các ảnh chụp giúp đối chiếu tệp khách hàng, cách thu hẹp audience và kết quả tra cứu từ khóa. Chọn ảnh để xem lớn và đọc rõ nội dung.</p><div class="meta"><span>10 ảnh chụp</span><span>30/09–07/10/2026</span><span>Tệp khách hàng · Bộ lọc · Từ khóa</span></div></header>
<div class="nav-wrap"><nav aria-label="Nhóm bằng chứng"><a href="#tep-chinh">Tệp chính</a><a href="#backup">Tệp dự phòng & bộ lọc</a><a href="#planner">Keyword Planner</a></nav></div>
<main>''' + ''.join(body) + '''</main><footer>Bảo · Hồ sơ tham khảo kế hoạch quảng cáo · 08/10/2026</footer>
<dialog id="viewer" aria-labelledby="viewer-title"><div class="dialog-bar"><h2 id="viewer-title"></h2><button id="size-toggle" type="button">Cỡ gốc</button><button id="close-viewer" class="dialog-close" type="button">Đóng ×</button></div><div id="image-stage" class="image-stage"><img id="viewer-image" alt=""></div></dialog>
<script>
const viewer=document.getElementById('viewer'),stage=document.getElementById('image-stage'),photo=document.getElementById('viewer-image'),toggle=document.getElementById('size-toggle');let opener;
document.querySelectorAll('[data-image]').forEach(button=>button.addEventListener('click',()=>{opener=button;const image=document.getElementById(button.dataset.image);photo.src=image.src;photo.alt=image.alt;document.getElementById('viewer-title').textContent=image.alt;stage.classList.remove('native');toggle.textContent='Cỡ gốc';viewer.showModal();}));
document.getElementById('close-viewer').addEventListener('click',()=>viewer.close());
toggle.addEventListener('click',()=>{const native=stage.classList.toggle('native');toggle.textContent=native?'Vừa khung':'Cỡ gốc';});
viewer.addEventListener('close',()=>{photo.removeAttribute('src');if(opener)opener.focus();});
viewer.addEventListener('click',e=>{if(e.target===viewer)viewer.close();});
</script></body></html>'''
    write(OUTPUT / 'BAT_DAU.html', page)
    save(RECORD / 'reader-files-manifest.json', dict(revision='evidence-reader-v3',folder=OUTPUT.as_posix(),
        files=[dict(path=p.relative_to(OUTPUT).as_posix(),sha256=sha(p),bytes=p.stat().st_size)
               for p in sorted(OUTPUT.rglob('*')) if p.is_file()], images=copied))
    save(RECORD / 'source-caption-plan.json', dict(bindings,units=units))
    print(json.dumps({'reader':(OUTPUT / 'BAT_DAU.html').as_posix(),'files':11,'images':len(units),'html_bytes':len(page.encode('utf-8'))}))

if __name__ == '__main__':
    main()
