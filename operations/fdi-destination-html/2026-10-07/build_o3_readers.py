"""Build three O3 existing routes; preserve original journey/assets."""
import hashlib, html, json, re, subprocess
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
P = Path(__file__).parent
BASE = ROOT / 'deliverables/linkedin-safe-batches/2026-10-06/B1-en-o1-v2/case-reader.html'
TARGETS = [('O3-EN','en','en-osat-candidate1-v4'),('O3-Hans','zh-Hans','zh-Hans-osat-candidate2-v2'),('O3-Hant','zh-Hant','zh-Hant-osat-candidate3-v1')]
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert not (P/'O3-intake.json').exists(), 'Preserve intake; new revision required before rerun.'
base = BASE.read_text(encoding='utf-8')
packs = json.loads(re.search(r'<script type="application/json" id="reader-copy">(.*?)</script>',base,re.S)[1])
updates = {
'en': {
'title':'Bring factory records into the month-end discussion', 'back':'Back to the month-end records journey',
'lead':'Before the cut-off, which lot records does Finance still need from Operations? Align unfinished work, completed output and losses for the same period, then clarify who confirms the handoff. Explore a named packaging and testing case using integrated Digiwin ERP + iMES.',
'articleLabel':'Factory records and month-end coordination',
'resultTitle':'Reported month-close duration','resultValue':'15 days → 5 days',
'resultNote':'Digiwin Vietnam reports this change for 江苏中科智芯集成科技有限公司 in China, using integrated ERP + iMES. This is a case result, not a promised close time or a calculation of financial ROI.',
'valueTitle':'Give Operations and Finance a shared basis before the cut-off',
'valueLead':'Use the case as a reference for these questions about your current month-end records and handoff.',
'v1Title':'Locate unfinished work by lot at cut-off',
'v1Body':'For each lot, which production stage and source record support the unfinished quantity, and who can verify it?',
'v1Prepare':'Prepare one lot’s unfinished-work record, its cut-off time and the role that confirms it.',
'v2Title':'Reconcile output and losses for the same period',
'v2Body':'Which records explain completed output, scrap and losses for the period under review with Finance?',
'v2Prepare':'Prepare output and loss records for one period, including the source and unresolved differences.',
'v3Title':'Agree who confirms the handoff to Finance',
'v3Body':'Who checks the factory records, confirms the figures and resolves missing information before the handoff?',
'v3Prepare':'Prepare the confirmation roles, handoff time and one example of a record waiting for review.',
'bridge':'Clearer record sources and confirmation responsibilities can help teams identify where month-end coordination needs attention. The reported close-time result is a reference for discussion, not a forecast for another factory.',
'consultTitle':'Bring one month-end record handoff to the discussion',
'consultBody':'Describe how Operations prepares unfinished-work, output and loss records, and how the handoff to Finance is confirmed. We provide digital solutions for manufacturing, from ERP to smart manufacturing.',
'cta':'Discuss month-end records and handoff ownership'
},
'vi': {
'title':'Cùng hồ sơ sản xuất cho trao đổi cuối tháng','back':'Quay về journey hồ sơ cuối tháng',
'lead':'Trước thời điểm chốt kỳ, Tài chính còn cần Vận hành cung cấp hồ sơ lô nào? Đối chiếu sản phẩm dở dang, sản lượng hoàn thành và hao hụt trong cùng kỳ, rồi làm rõ người xác nhận bàn giao. Tham khảo case một doanh nghiệp đóng gói, kiểm thử sử dụng giải pháp tích hợp Digiwin ERP + iMES.',
'articleLabel':'Hồ sơ sản xuất và phối hợp cuối tháng',
'resultTitle':'Thời gian khóa sổ tháng được công bố','resultValue':'15 ngày → 5 ngày',
'resultNote':'Digiwin Việt Nam công bố kết quả này cho 江苏中科智芯集成科技有限公司 tại Trung Quốc, với giải pháp tích hợp ERP + iMES. Đây là kết quả của case, không phải cam kết thời gian khóa sổ hay phép tính ROI tài chính.',
'valueTitle':'Cùng căn cứ để Vận hành và Tài chính trao đổi trước chốt kỳ',
'valueLead':'Tham khảo case và các câu hỏi sau để rà soát hồ sơ cuối tháng cùng quy trình bàn giao hiện tại.',
'v1Title':'Xác định sản phẩm dở dang theo lô tại thời điểm chốt kỳ',
'v1Body':'Với từng lô, công đoạn và hồ sơ nguồn nào làm căn cứ cho số lượng chưa hoàn thành, và ai có thể xác nhận?',
'v1Prepare':'Hồ sơ sản phẩm dở dang của một lô, thời điểm chốt kỳ và vai trò xác nhận.',
'v2Title':'Đối chiếu sản lượng và hao hụt trong cùng kỳ',
'v2Body':'Hồ sơ nào giải thích sản lượng hoàn thành, phế phẩm và hao hụt của kỳ đang trao đổi với Tài chính?',
'v2Prepare':'Hồ sơ sản lượng và hao hụt của một kỳ, kèm nguồn và các chênh lệch chưa làm rõ.',
'v3Title':'Thống nhất người xác nhận bàn giao cho Tài chính',
'v3Body':'Ai kiểm tra hồ sơ sản xuất, xác nhận số liệu và làm rõ thông tin thiếu trước khi bàn giao?',
'v3Prepare':'Các vai trò xác nhận, thời điểm bàn giao và một ví dụ về hồ sơ đang chờ kiểm tra.',
'bridge':'Làm rõ nguồn hồ sơ và trách nhiệm xác nhận có thể giúp đội ngũ tìm ra điểm phối hợp cuối tháng cần chú ý. Kết quả thời gian khóa sổ trong case là cơ sở tham khảo để trao đổi, không phải dự báo cho một nhà máy khác.',
'consultTitle':'Trao đổi từ một lần bàn giao hồ sơ cuối tháng',
'consultBody':'Quý Doanh Nghiệp có thể mô tả cách Vận hành chuẩn bị hồ sơ sản phẩm dở dang, sản lượng và hao hụt, cùng cách xác nhận bàn giao cho Tài chính. Chúng tôi cung cấp giải pháp số cho sản xuất, từ ERP đến sản xuất thông minh.',
'cta':'Trao đổi về hồ sơ cuối tháng và trách nhiệm bàn giao'
},
'zh-Hans': {
'title':'让工厂记录成为月末讨论的依据','back':'返回月末记录核对内容',
'lead':'结账截止前，财务还需要工厂运营提供哪些批次记录？先对齐同一期间的在制品、完工产量与损耗，再明确交接确认责任人。了解一家封装测试企业采用Digiwin ERP + iMES一体化方案的案例。',
'articleLabel':'工厂记录与月末协作',
'resultTitle':'案例公布的月结时间','resultValue':'15天 → 5天',
'resultNote':'Digiwin越南公布了中国企业江苏中科智芯集成科技有限公司的这一结果，方案为ERP + iMES一体化方案。这是该案例的结果，不是结账时间承诺或财务ROI计算。',
'valueTitle':'让工厂运营与财务在截止前有共同讨论依据',
'valueLead':'参考该案例，通过以下问题梳理现行月末记录与交接流程。',
'v1Title':'截止时，按批次确认在制品',
'v1Body':'各批次的未完工数量依据哪道工序与哪份来源记录？由谁核实？',
'v1Prepare':'一个批次的在制品记录、截止时间与确认角色。',
'v2Title':'核对同一期间的产量与损耗',
'v2Body':'与财务讨论当期数据时，哪些记录说明完工产量、报废与损耗？',
'v2Prepare':'一个期间的产量与损耗记录，注明来源及尚未核清的差异。',
'v3Title':'明确交给财务前的确认责任',
'v3Body':'交接前，由谁核查工厂记录、确认数据并核清缺失信息？',
'v3Prepare':'各项确认的负责角色、交接时间与一份待核查记录。',
'bridge':'明确记录来源与确认责任，有助于找出月末协作中需要关注的环节。案例公布的月结时间可供讨论参考，不是对另一家工厂的预测。',
'consultTitle':'从一次月末记录交接开始交流',
'consultBody':'贵企业可说明工厂运营如何准备在制品、产量与损耗记录，以及如何确认与财务的交接。我们提供制造业数字化方案，涵盖ERP与智能制造。',
'cta':'交流月末记录与交接责任'
},
'zh-Hant': {
'title':'讓工廠紀錄成為月底討論的依據','back':'返回月底紀錄核對內容',
'lead':'結帳截止前，財務還需要工廠營運提供哪些批次紀錄？先對齊同一期間的在製品、完工產量與耗損，再釐清交接確認負責人。了解一家封裝測試企業採用Digiwin ERP + iMES整合方案的案例。',
'articleLabel':'工廠紀錄與月底協作',
'resultTitle':'案例公布的月結時間','resultValue':'15天 → 5天',
'resultNote':'Digiwin越南公布了中國企業江苏中科智芯集成科技有限公司的這項結果，方案為ERP + iMES整合方案。這是該案例的結果，不是結帳時間承諾或財務ROI計算。',
'valueTitle':'讓工廠營運與財務在截止前有共同討論依據',
'valueLead':'參考該案例，透過以下問題梳理現行月底紀錄與交接流程。',
'v1Title':'截止時，依批次確認在製品',
'v1Body':'各批次的未完工數量依據哪道製程與哪份來源紀錄？由誰核實？',
'v1Prepare':'一個批次的在製品紀錄、截止時間與確認角色。',
'v2Title':'核對同一期間的產量與耗損',
'v2Body':'與財務討論當期資料時，哪些紀錄說明完工產量、報廢與耗損？',
'v2Prepare':'一個期間的產量與耗損紀錄，註明來源及尚未核清的差異。',
'v3Title':'釐清交給財務前的確認職責',
'v3Body':'交接前，由誰核查工廠紀錄、確認資料並核清缺漏資訊？',
'v3Prepare':'各項確認的負責角色、交接時間與一份待核查紀錄。',
'bridge':'釐清紀錄來源與確認職責，有助於找出月底協作中需要關注的環節。案例公布的月結時間可供討論參考，不是對另一家工廠的預測。',
'consultTitle':'從一次月底紀錄交接開始交流',
'consultBody':'貴企業可說明工廠營運如何準備在製品、產量與耗損紀錄，以及如何確認與財務的交接。我們提供製造業數位化方案，從ERP到智慧製造。',
'cta':'交流月底紀錄與交接職責'
}}
for lang, u in updates.items():packs[lang].update(u)
(P/'O3-copy-v1.json').write_text(json.dumps(packs,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
intake={'base_checkpoint':subprocess.check_output(['git','-C',str(ROOT),'rev-parse','HEAD']).decode().strip(),'base_reader_sha256':sha(BASE),'copy_sha256':sha(P/'O3-copy-v1.json'),'targets':[]}
for batch,locale,folder in TARGETS:
 relative='deliverables/linkedin-locale-dogfood/2026-10-06/'+folder;d=ROOT/relative
 originals={str(p.relative_to(d)).replace('\\','/'):sha(p) for p in d.rglob('*') if p.is_file()}
 journey=json.loads((d/'journey.json').read_text(encoding='utf-8-sig'))
 record={'batch':batch,'locale':locale,'directory':relative,'original_files_sha256':originals,'ordered_rows':journey['rows']}
 output=re.sub(r'(<script type="application/json" id="reader-copy">).*?(</script>)',lambda m:m[1]+json.dumps(packs,ensure_ascii=False)+m[2],base,flags=re.S)
 marker='<div class="systems">'
 outcome='<div class="case-outcome"><h3 data-i18n="resultTitle"></h3><p class="case-result" data-i18n="resultValue"></p><p data-i18n="resultNote"></p></div>'
 assert marker in output;output=output.replace(marker,outcome+marker,1)
 output=output.replace('</style>','.case-outcome{margin:28px 0;padding:24px;background:#fff;border:1px solid #e7e7ed;border-radius:20px;box-shadow:0 6px 22px #171a2b06}.case-outcome h3{font-size:18px;margin:0 0 12px}.case-result{font-size:clamp(30px,4vw,46px);font-weight:800;letter-spacing:-1.2px;color:#0052ff;line-height:1.2;margin:12px 0}.case-outcome p:last-child{font-size:14px;line-height:1.7;margin-bottom:0}</style>',1)
 pack=packs[locale];output=output.replace('<html lang="en">',f'<html lang="{locale}">',1)
 output=re.sub(r'<title>.*?</title>','<title>'+html.escape(pack['title'])+' | Digiwin</title>',output,count=1)
 output=re.sub(r'(<[a-z][^>]*\bdata-i18n="([^"]+)"[^>]*>)[^<]*(</[a-z]+>)',lambda m:m[1]+html.escape(pack[m[2]])+m[3],output)
 def attr(m):
  tag=m[0];name,key=m[1].split(':');value=name+'="'+html.escape(pack[key],quote=True)+'"';tag,count=re.subn(r'\b'+re.escape(name)+r'="[^"]*"',value,tag,count=1);return tag if count else tag[:-1]+' '+value+'>'
 output=re.sub(r'<[a-z][^>]*\bdata-i18n-attr="([^"]+)"[^>]*>',attr,output)
 output=re.sub(r'(<button[^>]*data-locale="([^"]+)"[^>]*aria-pressed=")[^"]+("[^>]*>)',lambda m:m[1]+str(m[2]==locale).lower()+m[3],output)
 output=output.replace("if (!allowed.includes(locale)) locale = 'en';",f"if (!allowed.includes(locale)) locale = '{locale}';")
 (d/'case-reader.html').write_text(output,encoding='utf-8')
 entry=d/'index.html';content,count=re.subn(r'href="case-reader\.html(?:\?lang=[^"]+)?"',f'href="case-reader.html?lang={locale}"',entry.read_text(encoding='utf-8-sig'));assert count==1;entry.write_text(content,encoding='utf-8')
 record.update(reader_after_sha256=sha(d/'case-reader.html'),entry_after_sha256=sha(entry));intake['targets'].append(record)
(P/'O3-intake.json').write_text(json.dumps(intake,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Three O3 readers built; month-close15 to5 result retained with source/entity/integrated scope.')
