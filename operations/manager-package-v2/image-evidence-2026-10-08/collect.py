"""Collect existing evidence without modifying images or the approved package."""
from pathlib import Path
import hashlib
import json
import shutil
from datetime import datetime, timezone

ROOT = Path('D:/LinkedIn_Package_V2_2026-10-07')
PUBLIC = ROOT / 'deliverables/manager-package-v2-evidence/2026-10-08'
PRIVATE = Path('D:/LinkedIn_Package_V2_Evidence_2026-10-08')
RECORD = ROOT / 'operations/manager-package-v2/image-evidence-2026-10-08'
CHECKPOINT = 'd521c5fdd6c4c29cc55bebdabb9edeea395c588b'

def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

def write(p, s):
    p.parent.mkdir(parents=True, exist_ok=True)
    pending = p.with_name(p.name + '.new')
    with pending.open('w', encoding='utf-8', newline='\n') as f:
        f.write(s)
    pending.replace(p)

def js(p, d):
    write(p, json.dumps(d, ensure_ascii=False, indent=2) + '\n')

def snapshot(folder):
    return [{'path': p.relative_to(folder).as_posix(), 'sha256': sha(p), 'bytes': p.stat().st_size}
            for p in sorted(folder.rglob('*')) if p.is_file() and not p.name.startswith('.~lock.')]

def unit(id_, source, target, date, title, caption, public=False):
    source = Path(source)
    assert source.is_file(), source
    return dict(id=id_, source=source.as_posix(), file=target, observed_date=date,
                title=title, caption=caption, sanitized_for_public_repo=public,
                source_sha256=sha(source), bytes=source.stat().st_size,
                copy_method='EXACT_BYTE_COPY; no crop, redaction, resampling or regeneration')

def main():
    assert not PRIVATE.exists(), 'Destination already exists; inspect before rerun.'
    original_manifest = json.loads((RECORD.parent / 'ad-logic-2026-10-08/final-file-manifest.json').read_text(encoding='utf-8'))
    package = ROOT / 'deliverables/manager-package-v2/2026-10-07'
    assert snapshot(package) == original_manifest['files'], 'Approved package differs before collection.'
    if not (RECORD / 'intake-public-files.json').exists():
        js(RECORD / 'intake-public-files.json', {'revision': 'evidence-v1-before-image-addition', 'files': snapshot(PUBLIC)})

    planner = []
    for id_, tag, filename, language, time in [
        ('IMG-P01', 'English', 'google_planner_en_2026-09-30_13-54-41.png', 'English', '13:54'),
        ('IMG-P02', 'Chinese_gian_the', 'google_planner_zh_hans_2026-09-30_13-57-22.png', 'Chinese (simplified)', '13:57'),
        ('IMG-P03', 'Chinese_phon_the', 'google_planner_zh_hant_2026-09-30_13-59-07.png', 'Chinese (traditional)', '13:59'),
    ]:
        planner.append(unit(id_, ROOT / 'outputs/evidence' / filename,
            '03_Ngan_sach_va_do_luong/Anh_Planner/' + tag + '_2026-09-30.png', '2026-09-30',
            'Keyword Planner · ' + language,
            f'Ảnh chụp 30/09/2026, khoảng {time} UTC+7. Bộ lọc hiển thị: Việt Nam, {language}, Google, Sep 2025–Aug 2026. Bảy dòng từ khóa có dấu gạch ngang ở các cột chỉ số. Đây là kết quả của cấu hình truy vấn này; không suy nhu cầu bằng 0, CPC hoặc hiệu quả quảng cáo. Mép trái ảnh gốc cắt một phần tên từ khóa; đọc bảng seed trong biên bản kèm theo.', True))

    source424 = Path('D:/LinkedIn_Audience_Research_Evidence_2026-10-05')
    source52 = Path('D:/LinkedIn_Closeout_Private_2026-10-07/r5-upload')
    raw = [
        unit('IMG-L01', source424 / 'linkedin-final424-saved-file-20261006.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/01_Tep_chinh_file_da_luu_2026-10-06.jpg', '2026-10-06',
            'Tệp chính · file identity-repair đã lưu',
            'Modal Edit list audience hiển thị đúng tên CSV identity_repair_424_20261006_final. Biên bản 06/10 ghi đây là readback file đã lưu sau lượt update. Riêng ảnh này không chứng minh kết quả matching mới; nội dung từng công ty nằm ở hồ sơ nghiên cứu, không được đưa vào kho này.'),
        unit('IMG-L02', source424 / 'linkedin-final424-updating-20261006.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/02_Tep_chinh_Updating_2026-10-06.jpg', '2026-10-06',
            'Tệp chính · Updating tại checkpoint 06/10',
            'Danh sách audience hiển thị Updating. Con số 80% trên ảnh thuộc snapshot cũ trong lúc update; không dùng làm kết quả matching của file 424 đã sửa. Đọc cùng biên bản 06/10; đây không phải lượt kiểm trạng thái mới ngày 08/10.'),
        unit('IMG-L03', source52 / 'details-zero.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/03_Backup_Ready_va_Details_2026-10-07.jpg', '2026-10-07',
            'Backup 52 · Ready và Details trên cùng ảnh',
            'Ảnh hiển thị Ready, >90%, 444.274 members, đồng thời 0 Companies, Matched(0), Unmatched(0). Tệp đã có summary nhưng chưa có hàng công ty để đối soát mapping. 444.274 là số summary của tệp, không phải reach đã lọc Việt Nam hoặc số buyer đủ điều kiện; Details trống cũng không chứng minh có 0 công ty match.'),
        unit('IMG-L04', source52 / 'vn-en-8200.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/04_Chon_Company_List_R5_2026-10-07.jpg', '2026-10-07',
            'Bộ lọc · chọn đúng Company List R5',
            'Ảnh hiển thị Company List R5-52 được chọn trong editor tạm. Biên bản kèm ghi cấu hình R5 AND Việt Nam, English có estimate ổn định 8.200; ảnh này không hiển thị con số 8.200. Tên file lưu gốc không thay cho bằng chứng nhìn thấy trên ảnh.'),
        unit('IMG-L05', source52 / 'vn-functions-5000.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/05_Narrow_Job_Functions_2026-10-07.jpg', '2026-10-07',
            'Bộ lọc · thêm lớp Job Functions',
            'Ảnh hiển thị Company List AND Job Functions: Engineering, Information Technology, Operations, Quality Assurance; các chức năng nằm trong nhóm ANY/OR. Biên bản ghi estimate ổn định 5.000 cho bước này, nhưng con số đó không nằm trong viewport ảnh. Lớp seniority ở bước kế tiếp được ghi trong biên bản, chưa có ảnh chọn đầy đủ từng seniority trong bộ đã tìm thấy.'),
        unit('IMG-L06', source52 / 'vn-lead-460.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/06_Estimate_460_English_2026-10-07.jpg', '2026-10-07',
            'Bộ lọc · estimate 460 với English',
            'Ảnh hiển thị 460 Potential LinkedIn members reached, Location Vietnam, Profile Language English. Biên bản ghi đây là cấu hình R5 + bốn functions + Manager/Director/VP/CXO; các lớp function/seniority không cùng nằm trong viewport này. Đây là estimate editor chưa Apply/Save, không phải delivered reach. Helper English trên ảnh nói có thể nhắm các ngôn ngữ profile khác, ngoại trừ Sponsored Messaging.'),
        unit('IMG-L07', source52 / 'vn-vi-lead.jpg',
            '02_Tep_khach_hang/Anh_LinkedIn/07_Estimate_duoi_300_Vietnamese_2026-10-07.jpg', '2026-10-07',
            'Bộ lọc · đối chiếu Vietnamese',
            'Ảnh hiển thị <300, Location Vietnam và Profile Language Vietnamese. Biên bản ghi giữ các lớp function/seniority cuối rồi đổi ngôn ngữ. Đây là đối chiếu estimate tạm; không chứng minh hai tệp VN/FDI độc lập, bốn tệp theo locale hoặc quy mô buyer thực tế.'),
    ]
    archive = json.loads(Path('D:/LinkedIn_Closeout_Private_2026-10-05/matching-repair/CURRENT_IDENTITY_REPAIR_MANIFEST.json').read_text(encoding='utf-8-sig'))
    pinned = {x['id']: x['sha256'] for x in archive['items']}
    assert raw[0]['source_sha256'] == pinned['SAVED_FILENAME']
    assert raw[1]['source_sha256'] == pinned['UPDATING_READBACK']

    anchor = ROOT / 'operations/Vy_Email_Content_Anchor.md'
    email = ROOT / 'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'
    common = dict(revision='image-evidence-v2', reviewer='/root', independence='SELF_REVIEW',
        anchor_id='VY-CONTENT-ANCHOR', anchor_revision='1.0', anchor_sha256=sha(anchor),
        email_record_id='VY-MAIL-USER-20261006', email_sha256=sha(email),
        package_checkpoint=CHECKPOINT, reviewed_utc=datetime.now(timezone.utc).isoformat(),
        scope='Existing source screenshots and internal captions only; no new creative, account access or live recheck.')
    write(RECORD / 'Execution_Contract.md', '''# Bổ sung ảnh evidence · 08/10/2026

Mandate: Bảo yêu cầu rà repo để có ảnh bằng chứng thực trong kho evidence. Root thực hiện, không delegate.

Output: thêm ba ảnh Planner đã sanitize vào kho repo; tạo một thư mục thường ngoài Git gom cùng nguồn văn bản và bảy ảnh LinkedIn gốc có thông tin tài khoản. Ảnh giữ nguyên byte, không crop/chỉnh/generate. Approved package 215 file và receipts cũ giữ nguyên.

Acceptance: mỗi ảnh đã xem trực tiếp; caption phân biệt pixel nhìn thấy với thông tin từ biên bản; mốc 30/09, 06/10, 07/10 không thành live state 08/10. Copy SHA256 khớp nguồn, toàn bộ link tương đối mở được, package khớp manifest. Không đưa raw LinkedIn/account data vào Git. Không commit/merge/push, truy cập tài khoản hay gửi mail.

Audit target: source pixels + dated source receipts + resulting folder + approved package manifest. Root SELF_REVIEW; không có independent audit hoặc chứng nhận mapping/buyer/ROI mới.
''')
    js(RECORD / 'pregen-review.json', dict(common, stage='PREGEN_SCRIPT / ARCHIVED_IMAGE_COLLECTION',
        verdict='MESSAGE_ANCHOR_PASS',
        anchor_dispositions={
            'A1': 'No new ICP claim; audience hypotheses remain those of dated records.',
            'A2': 'Platform Ready/count not represented as customer fit or decision authority.',
            'A3': 'VN/FDI and creative locales not inferred from profile-language estimates.',
            'A4': 'No new ROI/result promise; editor estimates not delivery results.',
            'A5': 'Approved VN ERP/readiness message unchanged.',
            'A6': 'No new solution capability or source-case claim.',
            'A7': 'Each image tied to dated context/companion record; package unchanged.'},
        units=[{k:v for k,v in x.items() if k != 'source'} for x in planner + raw],
        raw_destination='outside Git only', postgen='NOT_RUN_AT_PREGEN'))

    # Public collection: sanitized existing images and their original dated receipt.
    for u in planner:
        target = PUBLIC / u['file']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(u['source'], target)
    receipt_source = ROOT / 'operations/CODEX_GOOGLE_PLANNER_DISCOVERY_RECEIPT.md'
    receipt_file = '03_Ngan_sach_va_do_luong/06_Planner_EN_Chinese_Bien_ban_2026-09-30.txt'
    shutil.copyfile(receipt_source, PUBLIC / receipt_file)
    write(PUBLIC / '03_Ngan_sach_va_do_luong/Anh_Planner/DOC_TRUOC.txt',
        'Ba ảnh chụp kết quả Keyword Planner ngày 30/09/2026, đã có trong repo. Giữ nguyên ảnh nguồn.\n'
        'Cấu hình: Việt Nam / Google / Sep 2025–Aug 2026; English, Chinese simplified và traditional.\n'
        'Dấu gạch ngang là không có metric hiển thị ở truy vấn này, không phải nhu cầu bằng 0.\n'
        'Đọc ../06_Planner_EN_Chinese_Bien_ban_2026-09-30.txt để xem seed đầy đủ.\n')
    public_gallery = '# Ảnh bằng chứng · 30/09/2026\n\nBa ảnh chụp giao diện Planner có sẵn trong repo. [Biên bản và seed đầy đủ](' + receipt_file + ').\n\n'
    for u in planner:
        public_gallery += '## ' + u['title'] + '\n\n' + u['caption'] + '\n\n![' + u['title'] + '](' + u['file'] + ')\n\n'
    public_gallery += ('Ảnh LinkedIn của tệp chính/backup và bộ lọc có thông tin tài khoản. Bản đầy đủ được gom riêng trên máy ở '
                       '`D:/LinkedIn_Package_V2_Evidence_2026-10-08/`, không nằm trong Git. '
                       'Ba ảnh ở nhóm 06 chỉ để đối chiếu bản trình bày package.\n')
    write(PUBLIC / '00_ANH_BANG_CHUNG.md', public_gallery)
    # Keep the original collection/index as a dated snapshot; current entry point is new.
    write(PUBLIC / 'BAT_DAU.txt',
        'Bổ sung ảnh evidence ngày 08/10/2026: mở 00_ANH_BANG_CHUNG.md để xem ba ảnh Planner thực.\n'
        'Bản đầy đủ gồm 10 ảnh LinkedIn/Planner nằm ở D:/LinkedIn_Package_V2_Evidence_2026-10-08/.\n'
        '00_MUC_LUC.md, DOC_TRUOC.txt và _truy_xuat_nguon.json giữ snapshot lần gom đầu (23 evidence).\n'
        'Mô tả ảnh trong snapshot đầu chỉ nói ba ảnh package; bổ sung Planner được ghi riêng ở _truy_xuat_anh.json.\n')
    js(PUBLIC / '_truy_xuat_anh.json', dict(revision='image-evidence-v2-public-supplement',
        supplements='_truy_xuat_nguon.json (evidence-v1 retained)', entries=planner,
        companion=dict(file=receipt_file, source=receipt_source.as_posix(),
            source_sha256=sha(receipt_source), sha256=sha(PUBLIC / receipt_file), kind='EXACT_BYTE_COPY')))
    # Complete local handoff, including original account screenshots, remains outside Git.
    shutil.copytree(PUBLIC, PRIVATE, ignore=shutil.ignore_patterns('.~lock.*'))
    for u in raw:
        target = PRIVATE / u['file']
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(u['source'], target)
    write(PRIVATE / '02_Tep_khach_hang/Anh_LinkedIn/DOC_TRUOC.txt',
        'Bảy ảnh chụp LinkedIn gốc, ngày 06–07/10/2026, giữ nguyên byte.\n'
        'Có thông tin tài khoản trong ảnh; thư mục đầy đủ này được giữ ngoài Git để Bảo/Vy tra cứu nội bộ.\n'
        'Mở ../../00_ANH_BANG_CHUNG.md để đọc chú thích trước khi diễn giải số liệu.\n'
        'Cấu hình bộ lọc đầy đủ và estimates 8.200/5.000 cần đọc cùng biên bản 03; không hiện đủ trên từng ảnh.\n')
    gallery = '''# Ảnh bằng chứng · LinkedIn và Google Planner

Bộ ảnh gốc từ các lượt làm đã lưu ngày 30/09, 06/10 và 07/10/2026. Mỗi ảnh bên dưới có mốc và ngữ cảnh riêng. Tệp ảnh giữ nguyên byte; phần chú thích được thêm ngày 08/10.

Ảnh LinkedIn có thông tin tài khoản, vì vậy bộ đầy đủ này nằm ngoài Git và dành cho Bảo/Vy tra cứu nội bộ. Mở [mục lục nguồn](00_MUC_LUC.md) để xem các tài liệu liên quan.

## Tệp chính 424 và backup 52

Đọc cùng [tệp chính 06/10](02_Tep_khach_hang/01_Tep_chinh_424_Ket_qua_2026-10-06.txt), [backup upload](02_Tep_khach_hang/02_Backup_52_Upload_2026-10-07.txt) và [mapping/bộ lọc 07/10](02_Tep_khach_hang/03_Backup_52_Mapping_va_bo_loc_2026-10-07.txt).

'''
    for u in raw:
        gallery += '### ' + u['title'] + '\n\n' + u['caption'] + '\n\n![' + u['title'] + '](' + u['file'] + ')\n\n'
    gallery += '## Google Keyword Planner\n\n[Biên bản và bảng seed đầy đủ](' + receipt_file + ').\n\n'
    for u in planner:
        gallery += '### ' + u['title'] + '\n\n' + u['caption'] + '\n\n![' + u['title'] + '](' + u['file'] + ')\n\n'
    write(PRIVATE / '00_ANH_BANG_CHUNG.md', gallery)
    write(PRIVATE / 'DOC_TRUOC.txt',
        'Mở 00_ANH_BANG_CHUNG.md để xem 10 ảnh chụp bằng chứng thực và chú thích.\n'
        'Mở 00_MUC_LUC.md để tra cứu 6 nhóm nguồn bằng văn bản.\n'
        'Bản đầy đủ này có ảnh LinkedIn chứa thông tin tài khoản; giữ ngoài Git, dùng nội bộ Bảo/Vy.\n'
        'Package Bảo đã duyệt được giữ nguyên; không có link tự động từ package vào kho này.\n')
    write(PRIVATE / 'BAT_DAU.txt',
        'Mở 00_ANH_BANG_CHUNG.md để xem 10 ảnh bằng chứng thực; 00_MUC_LUC.md để tra nguồn văn bản.\n'
        'Bộ đầy đủ này có ảnh tài khoản LinkedIn, giữ ngoài Git để Bảo/Vy tra cứu nội bộ.\n')
    local_index = PRIVATE / '00_MUC_LUC.md'
    s = local_index.read_text(encoding='utf-8').replace(
        'Kho tra cứu riêng khi Vy cần nguồn giải thích.',
        'Mở [ảnh bằng chứng](00_ANH_BANG_CHUNG.md) để xem 10 ảnh: tệp chính, backup, bộ lọc và Planner.\n\nKho tra cứu riêng khi Vy cần nguồn giải thích.').replace(
        'Ảnh chụp dùng để đối chiếu bản trình bày offline.',
        'Ảnh Planner và LinkedIn là bằng chứng truy vấn/trạng thái/bộ lọc thực theo ngày; ảnh nhóm 06 dùng đối chiếu bản trình bày offline.')
    write(local_index, s)
    js(PRIVATE / '_truy_xuat_anh.json', dict(revision='image-evidence-v2-complete-local',
        supplements='_truy_xuat_nguon.json (23 original evidence entries retained)',
        package_checkpoint=CHECKPOINT, local_only=True, entries=raw + planner,
        companion=dict(file=receipt_file, source=receipt_source.as_posix(), source_sha256=sha(receipt_source),
                       sha256=sha(PRIVATE / receipt_file), kind='EXACT_BYTE_COPY')))
    js(RECORD / 'public-files-manifest.json', {'revision': 'image-evidence-v2', 'files': snapshot(PUBLIC)})
    # Only image IDs/hashes enter the public record; local archive paths stay in the outside-Git catalog.
    js(RECORD / 'collection-result.json', dict(revision='image-evidence-v2',
        public_folder=PUBLIC.relative_to(ROOT).as_posix(), complete_local_folder=PRIVATE.as_posix(),
        public_file_count=len(snapshot(PUBLIC)), complete_local_file_count=len(snapshot(PRIVATE)),
        original_evidence_entries=23, added_sanitized_images=3, added_dated_receipt=1,
        complete_local_images_added=10, raw_linkedin_images_outside_git=7,
        sources=[{k:v for k,v in x.items() if k != 'source'} for x in planner + raw],
        excluded=[dict(source='source-research/page16.png', reason='PDF render has incomplete Chinese labels; BPS source discrepancy and relevance not resolved. Not included as evidence for current package claims.')]))
    js(PRIVATE / '_danh_muc_file.json', {'revision': 'image-evidence-v2-complete-local', 'files': snapshot(PRIVATE)})
    assert snapshot(package) == original_manifest['files'], 'Approved package changed.'
    print(json.dumps({'public_files': len(snapshot(PUBLIC)), 'complete_local_files': len(snapshot(PRIVATE)),
                      'source_images': len(planner + raw), 'package_unchanged_files': len(snapshot(package))}))

if __name__ == '__main__':
    main()
