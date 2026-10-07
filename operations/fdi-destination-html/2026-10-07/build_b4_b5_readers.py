"""Build O2 handoff readers from approved VN layout; pin main dependencies."""
import hashlib
import html
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
PACKET = Path(__file__).parent
SOURCE = Path('D:/Digiwin_Semiconducter_Workspace')
BASE = ROOT / 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html'
TARGETS = [('B4', 'en', 'B4-en-o2-v1'), ('B5', 'zh-Hans', 'B5-zh-Hans-o2-v1')]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
if (PACKET / 'B4-B5-intake.json').exists():
    raise SystemExit('Intake exists; preserve original source pins. Do not rerun without revision-bound plan.')
base = BASE.read_text(encoding='utf-8')
packs = json.loads(re.search(r'<script type="application/json" id="reader-copy">(.*?)</script>', base, re.S)[1])
updates = {
 'en': {
  'title': 'A shared basis for the next lot handoff',
  'back': 'Back to the lot-handoff journey',
  'lead': 'Two status reports for the same lot may describe different stages or recording times. Before the next handoff, align the context, source record and confirmation owner. Explore how a named packaging and testing business connects production records with Digiwin ERP + iMES.',
  'articleLabel': 'Production records and lot handoffs',
  'valueTitle': 'Give Operations and Quality a shared basis for the next handoff',
  'valueLead': 'Use the case as a reference for these questions about your current lot-handoff workflow.',
  'v1Title': 'Compare the same lot, stage and recording time',
  'v1Body': 'Do the reports describe the same process stage and recording time? Different status reports may both be correct when their context differs.',
  'v1Prepare': 'Prepare two status reports for one lot, with the stage and recording time of each.',
  'v2Title': 'Identify the record that supports the handoff',
  'v2Body': 'Which source record supports the next step, and what information does the receiving team need?',
  'v2Prepare': 'Prepare the source record for one handoff and the receiving team’s information requirements.',
  'v3Title': 'Make the confirmation owner and next check clear',
  'v3Body': 'Who checks missing information, confirms the applicable parameter revision and follows up exceptions before a status update?',
  'v3Prepare': 'Prepare the confirmation roles and one example of a missing record, parameter change or exception.',
  'bridge': 'A shared view of lot context, source records and responsibilities can help teams identify where a handoff needs attention. Start the discussion with one actual handoff at your company.',
  'consultTitle': 'Bring one lot-handoff workflow to the discussion',
  'consultBody': 'Describe how Operations and Quality compare status reports, confirm the source record and assign the next check. We provide digital solutions for manufacturing, from ERP to smart manufacturing.',
  'cta': 'Discuss lot records and handoff responsibilities'
 },
 'vi': {
  'title': 'Cùng thông tin làm căn cứ bàn giao lô',
  'back': 'Quay về journey bàn giao lô',
  'lead': 'Hai báo cáo trạng thái của cùng một lô có thể phản ánh công đoạn hoặc thời điểm ghi nhận khác nhau. Trước lần bàn giao tiếp theo, cần thống nhất bối cảnh, hồ sơ nguồn và người xác nhận. Cùng chúng tôi xem cách một doanh nghiệp đóng gói, kiểm thử kết nối hồ sơ sản xuất bằng Digiwin ERP + iMES.',
  'articleLabel': 'Hồ sơ sản xuất và bàn giao lô',
  'valueTitle': 'Cùng cơ sở thông tin để Vận hành và Chất lượng bàn giao lô',
  'valueLead': 'Tham khảo case và các câu hỏi sau để rà soát quy trình bàn giao lô hiện tại.',
  'v1Title': 'Đối chiếu cùng lô, công đoạn và thời điểm ghi nhận',
  'v1Body': 'Các báo cáo có phản ánh cùng công đoạn và thời điểm ghi nhận không? Hai trạng thái khác nhau vẫn có thể cùng đúng khi bối cảnh khác nhau.',
  'v1Prepare': 'Hai báo cáo trạng thái của một lô, kèm công đoạn và thời điểm ghi nhận của từng báo cáo.',
  'v2Title': 'Xác định hồ sơ làm căn cứ bàn giao',
  'v2Body': 'Hồ sơ nguồn nào làm căn cứ cho bước tiếp theo, và đội tiếp nhận cần những thông tin gì?',
  'v2Prepare': 'Hồ sơ nguồn của một lần bàn giao và các thông tin đội tiếp nhận cần.',
  'v3Title': 'Làm rõ người xác nhận và bước kiểm tra tiếp theo',
  'v3Body': 'Ai kiểm tra thông tin còn thiếu, xác nhận phiên bản tham số áp dụng và theo dõi ngoại lệ trước khi cập nhật trạng thái?',
  'v3Prepare': 'Các vai trò xác nhận và một ví dụ về hồ sơ thiếu, thay đổi tham số hoặc ngoại lệ.',
  'bridge': 'Thống nhất bối cảnh lô, hồ sơ nguồn và trách nhiệm có thể giúp đội ngũ xác định điểm bàn giao cần chú ý. Quý Doanh Nghiệp có thể bắt đầu trao đổi từ một lần bàn giao thực tế.',
  'consultTitle': 'Trao đổi từ một quy trình bàn giao lô cụ thể',
  'consultBody': 'Quý Doanh Nghiệp có thể mô tả cách Vận hành và Chất lượng đối chiếu báo cáo trạng thái, xác nhận hồ sơ nguồn và phân công bước kiểm tra tiếp theo. Chúng tôi cung cấp giải pháp số cho sản xuất, từ ERP đến sản xuất thông minh.',
  'cta': 'Trao đổi về hồ sơ lô và trách nhiệm bàn giao'
 },
 'zh-Hans': {
  'title': '为下一次批次交接建立共同依据',
  'back': '返回批次交接内容',
  'lead': '同一批次的两份状态报告，可能对应不同工序或记录时间。下一次交接前，先对齐背景、来源记录与确认责任人。了解一家封装测试企业如何通过Digiwin ERP + iMES关联生产记录。',
  'articleLabel': '生产记录与批次交接',
  'valueTitle': '让生产运营与质量团队按共同依据交接批次',
  'valueLead': '参考该案例，通过以下问题梳理现行批次交接流程。',
  'v1Title': '对齐批次、工序与记录时间',
  'v1Body': '报告是否对应相同工序与记录时间？背景不同，两份状态报告可能都正确。',
  'v1Prepare': '同一批次的两份状态报告，以及各自的工序与记录时间。',
  'v2Title': '明确交接依据的来源记录',
  'v2Body': '下一步依据哪份来源记录？接收团队需要哪些信息？',
  'v2Prepare': '一次交接的来源记录，以及接收团队所需的信息。',
  'v3Title': '明确确认责任人与下一步核查',
  'v3Body': '更新状态前，由谁核查缺失信息、确认适用的参数版本并跟进异常？',
  'v3Prepare': '各项确认的负责角色，以及一项缺失记录、参数变更或异常实例。',
  'bridge': '对齐批次背景、来源记录与责任，有助于找出交接中需要关注的环节。欢迎从贵企业的一次实际交接开始交流。',
  'consultTitle': '从一项具体的批次交接流程开始',
  'consultBody': '贵企业可说明生产运营与质量团队如何比较状态报告、确认来源记录并安排下一步核查。我们提供制造业数字化方案，涵盖ERP与智能制造。',
  'cta': '交流批次记录与交接责任'
 },
 'zh-Hant': {
  'title': '為下一次批次交接建立共同依據',
  'back': '返回批次交接內容',
  'lead': '同一批次的兩份狀態報告，可能對應不同製程階段或紀錄時間。下一次交接前，先對齊背景、來源紀錄與確認負責人。了解一家封裝測試企業如何透過Digiwin ERP + iMES關聯生產紀錄。',
  'articleLabel': '生產紀錄與批次交接',
  'valueTitle': '讓營運與品質團隊依共同依據交接批次',
  'valueLead': '參考該案例，透過以下問題梳理現行批次交接流程。',
  'v1Title': '對齊批次、製程階段與紀錄時間',
  'v1Body': '報告是否對應相同製程階段與紀錄時間？背景不同，兩份狀態報告可能都正確。',
  'v1Prepare': '同一批次的兩份狀態報告，以及各自的製程階段與紀錄時間。',
  'v2Title': '釐清交接依據的來源紀錄',
  'v2Body': '下一步依據哪份來源紀錄？接收團隊需要哪些資訊？',
  'v2Prepare': '一次交接的來源紀錄，以及接收團隊所需的資訊。',
  'v3Title': '釐清確認負責人與下一步核查',
  'v3Body': '更新狀態前，由誰核查缺漏資訊、確認適用的參數版本並追蹤異常？',
  'v3Prepare': '各項確認的負責角色，以及一項缺漏紀錄、參數變更或異常實例。',
  'bridge': '對齊批次背景、來源紀錄與職責，有助於找出交接中需要關注的環節。歡迎從貴企業的一次實際交接開始交流。',
  'consultTitle': '從一項具體的批次交接流程開始',
  'consultBody': '貴企業可說明營運與品質團隊如何比較狀態報告、確認來源紀錄並安排下一步核查。我們提供製造業數位化方案，從ERP到智慧製造。',
  'cta': '交流批次紀錄與交接職責'
 }
}
for locale, changed in updates.items():
    assert all(k in packs[locale] for k in changed)
    packs[locale].update(changed)
(PACKET / 'B4-B5-copy-v1.json').write_text(json.dumps(packs, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
intake = {'source_worktree': str(SOURCE), 'source_commit': subprocess.check_output(['git', '-C', str(SOURCE), 'rev-parse', 'HEAD']).decode().strip(), 'base_checkpoint': subprocess.check_output(['git', '-C', str(ROOT), 'rev-parse', 'HEAD']).decode().strip(), 'base_reader_sha256': sha(BASE), 'copy_sha256': sha(PACKET / 'B4-B5-copy-v1.json'), 'targets': []}
for batch, locale, folder in TARGETS:
    relative = 'deliverables/linkedin-safe-batches/2026-10-07/' + folder
    source = SOURCE / relative
    target = ROOT / relative
    assert not target.exists(), 'Existing owned destination: inspect before overwriting.'
    originals = {}
    for p in source.rglob('*'):
        if p.is_file():
            name = p.relative_to(source)
            out = target / name
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_bytes(p.read_bytes())
            originals[str(name).replace('\\', '/')] = sha(p)
    selected = json.loads((target / 'selected-copy.json').read_text(encoding='utf-8-sig'))
    record = {'batch': batch, 'locale': locale, 'directory': relative, 'source_files_sha256': originals, 'ordered_source_cards': selected['cards'], 'photo_provenance': 'B1-photo-research/provenance.json'}
    output = re.sub(r'(<script type="application/json" id="reader-copy">).*?(</script>)', lambda m: m[1] + json.dumps(packs, ensure_ascii=False) + m[2], base, flags=re.S)
    output = output.replace('<html lang="en">', f'<html lang="{locale}">', 1)
    pack = packs[locale]
    output = re.sub(r'<title>.*?</title>', '<title>' + html.escape(pack['title']) + ' | Digiwin</title>', output, count=1)
    output = re.sub(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)', lambda m: m[1] + html.escape(pack[m[2]]) + m[3], output)
    def attr(m):
        tag = m[0]
        name, key = m[1].split(':')
        value = name + '="' + html.escape(pack[key], quote=True) + '"'
        tag, count = re.subn(r'\b' + re.escape(name) + r'="[^"]*"', value, tag, count=1)
        return tag if count else tag[:-1] + ' ' + value + '>'
    output = re.sub(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>', attr, output)
    output = re.sub(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+("[^>]*>)', lambda m: m[1] + str(m[2] == locale).lower() + m[3], output)
    output = output.replace("if (!allowed.includes(locale)) locale = 'en';", f"if (!allowed.includes(locale)) locale = '{locale}';")
    (target / 'case-reader.html').write_text(output, encoding='utf-8')
    entry = target / 'index.html'
    changed, count = re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"', f'href="case-reader.html?lang={locale}"', entry.read_text(encoding='utf-8-sig'))
    assert count == 1
    entry.write_text(changed, encoding='utf-8')
    record.update(reader_after_sha256=sha(target / 'case-reader.html'), entry_after_sha256=sha(entry))
    intake['targets'].append(record)
(PACKET / 'B4-B5-intake.json').write_text(json.dumps(intake, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print('B4/B5 readers built; source dependencies pinned; O2 four-language pack written.')
