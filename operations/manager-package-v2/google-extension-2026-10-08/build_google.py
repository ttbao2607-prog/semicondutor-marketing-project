"""Bounded offline manager-package extension. Does not alter landing sources or accounts."""
from pathlib import Path
from html import escape
import re, hashlib, json

ROOT = Path(__file__).resolve().parents[3]
PACK = ROOT / 'deliverables/manager-package-v2/2026-10-07'
OUT = PACK / '06_Google'
LOCALES = ['vi', 'en', 'zh-Hans', 'zh-Hant']
NAMES = ['Tiếng Việt', 'English', '简体中文', '繁體中文']
TERMS = {
 'vi': ['"MES đóng gói kiểm thử bán dẫn"','[truy xuất lot kiểm thử bán dẫn]','"quản lý WIP gia công ngoài bán dẫn"','[theo dõi gia công ngoài bán dẫn]','"ERP sản xuất PCB"','[MES linh kiện bán dẫn]','[Digiwin Việt Nam bán dẫn]'],
 'en': ['"OSAT lot traceability software"','[semiconductor test data management]','"fabless outsourced WIP tracking"','[semiconductor subcontract production tracking]','"PCB manufacturing ERP"','[semiconductor components MES]','[Digiwin semiconductor Vietnam]'],
 'zh-Hans': ['"半导体封装测试 MES"','[半导体批次追溯]','"无晶圆厂外包生产在制品管理"','[芯片委外生产追踪]','"PCB制造ERP"','[半导体零部件MES]','[鼎捷 越南 半导体]'],
 'zh-Hant': ['"半導體封裝測試 MES"','[半導體批次追溯]','"無晶圓廠外包生產在製品管理"','[晶片委外生產追蹤]','"PCB製造ERP"','[半導體零組件MES]','[鼎捷 越南 半導體]']
}
NEG = {
 'vi':['tuyển dụng','việc làm','thực tập','khóa học','luận văn','cổ phiếu','chứng khoán'],
 'en':['semiconductor jobs','semiconductor internship','semiconductor course','semiconductor thesis','semiconductor stock price'],
 'zh-Hans':['招聘','求职','实习','培训课程','毕业论文','股票','股价'],
 'zh-Hant':['徵才','職缺','實習','培訓課程','畢業論文','股票','股價']
}
URLS = ['https://solutions.digiwin.com.vn/semiconductor-osat','https://solutions.digiwin.com.vn/fabless','https://solutions.digiwin.com.vn/supplierecosystem']
LABELS = ['OSAT','Fabless','Supplier']

def table(headers, rows):
 return '<div class="table-wrap"><table class="logic-table"><thead><tr>'+''.join('<th scope="col">'+h+'</th>' for h in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td data-label="'+escape(headers[i],quote=True)+'">'+v+'</td>' for i,v in enumerate(row))+'</tr>' for row in rows)+'</tbody></table></div>'

def download_blocks(zh):
 blocks=[]
 for loc,name in zip(LOCALES,NAMES):
  groups = ['OSAT · 封裝測試','Fabless · 委外生產','工業供應商 · 工廠管理','品牌 · 獨立觀察'] if zh else ['OSAT · đóng gói, kiểm thử','Fabless · gia công ngoài','Supplier · quản trị nhà máy','Thương hiệu · đọc riêng']
  rows=[]
  for i,t in enumerate(TERMS[loc]):
   status = ('新增假設，待查量' if zh else 'Giả thuyết bổ sung, chờ tra volume') if i in (4,5) or loc=='vi' else ('已有查詢紀錄；未顯示指標' if zh else 'Có ghi nhận tra cứu; chỉ số hiển thị dấu gạch ngang')
   # VI was checked in the original September inquiry; other locales in the four-locale extension.
   rows.append([groups[min(i//2,3)],'<code lang="'+loc+'">'+escape(t)+'</code>',status])
  blocks.append('<details'+(' open' if loc==('zh-Hant' if zh else 'vi') else '')+'><summary>'+name+'</summary>'+table(['意圖群組','起始關鍵字','研究依據'] if zh else ['Nhóm ý định','Từ khóa khởi đầu','Căn cứ nghiên cứu'],rows)+'<div class="actions"><a class="button" href="Tu_khoa/'+loc+'.txt" download>'+('下載關鍵字' if zh else 'Tải tệp từ khóa')+'</a><a class="button" href="Loai_tru/'+loc+'.txt" download>'+('下載排除詞建議' if zh else 'Tải tệp loại trừ đề xuất')+'</a></div></details>')
 return ''.join(blocks)

def landing_cards(zh):
 titles=['OSAT · 封裝與測試','Fabless · IC 設計與委外生產','工業供應商 · PCB、零組件、材料'] if zh else ['OSAT · đóng gói và kiểm thử','Fabless · thiết kế IC, gia công ngoài','Supplier · PCB, linh kiện, vật liệu']
 intents=['批次追溯、測試資料與在製品進度。','委外在製品、交期、批次與成本協調。','工廠 ERP／MES、品質資料與設備資訊串接。'] if zh else ['Truy xuất lot, dữ liệu kiểm thử và tiến độ WIP.','WIP gia công ngoài, lịch giao, lot và phối hợp giá thành.','ERP/MES nhà máy, dữ liệu chất lượng và kết nối thông tin thiết bị.']
 purposes=['讓品質與營運能依同一批次核對資料，再說明 ERP 與 iMES 各自的角色。','串起 Foundry／OSAT 的資訊，讓計畫、訂單與成本判斷有共同依據。','從工廠管理問題切入，依實際需求說明 ERP、MES 與設備資料各層的作用。'] if zh else ['Đưa chất lượng và vận hành về cùng dữ liệu lot, rồi giải thích vai trò của ERP và iMES.','Nối thông tin Foundry/OSAT để người phụ trách phối hợp kế hoạch, đơn hàng và giá thành.','Mở từ bài toán nhà máy, phân biệt lớp ERP, MES và dữ liệu thiết bị theo nhu cầu cụ thể.']
 cards=[]
 for i in range(3):
  links=''.join('<a href="'+URLS[i]+'?lang='+loc+'" target="_blank" rel="noopener">'+name+'</a>' for loc,name in zip(LOCALES,NAMES))
  cards.append('<article class="card landing"><a href="Anh/'+LABELS[i]+'.png"><img src="Anh/'+LABELS[i]+'.png" alt="'+('現行落地頁營運內容截圖：' if zh else 'Ảnh chụp phần nội dung vận hành của trang đích: ')+LABELS[i]+'" width="1521" height="728"></a><h3>'+titles[i]+'</h3><p><b>'+('搜尋需求：' if zh else 'Ý định tìm kiếm: ')+'</b>'+intents[i]+'</p><p>'+purposes[i]+'</p><div class="locale-links" aria-label="'+('開啟線上落地頁' if zh else 'Mở trang đích trực tuyến')+'">'+links+'</div></article>')
 return '<div class="grid">'+''.join(cards)+'</div>'

VI = '''<p class="eyebrow">Google Search · từ nhu cầu đến quyết định</p><h1>Đón người đang tìm<br>giải pháp cho nhà máy</h1><p class="lead">LinkedIn giúp Digiwin được nhớ đến qua một vấn đề quản trị. Google Search bổ sung một điểm chạm khác: người đã chủ động tìm cách xử lý vấn đề đó, được dẫn vào đúng trang và đúng ngôn ngữ.</p>
<div class="grid"><section class="card"><small>Search tùy chọn · chưa thuế</small><div class="stat">≤ 500.000đ</div><p>Nằm trong trần 11,7 triệu đồng của toàn phương án.</p></section><section class="card"><small>Nội dung đón người tìm kiếm</small><div class="stat">3 trang đích</div><p>OSAT, Fabless và nhà cung ứng công nghiệp.</p></section><section class="card"><small>Chuẩn bị theo người đọc</small><div class="stat">4 ngôn ngữ</div><p>Việt, English, giản thể và phồn thể; chọn từng nhóm để thử.</p></section></div>
<div class="logic-links"><a href="#hypothesis">Giả thuyết</a><a href="#landing">3 trang đích</a><a href="#keywords">Từ khóa theo ngôn ngữ</a><a href="#tracking">Tracking</a><a href="#probe">Phép thử Search</a><a href="#measurement">Đo và quyết định</a></div>
<section id="hypothesis" class="logic-section"><h2>1. Tìm đúng vấn đề trước khi mở rộng</h2><p>Giả thuyết của Bảo: truy vấn có cả bối cảnh sản xuất và nhu cầu quản lý sẽ đưa người phù hợp tới nội dung Digiwin tốt hơn từ khóa “bán dẫn” quá rộng. Bảo thử ít nhóm, đọc truy vấn thực tế rồi chọn phần đáng tiếp tục.</p><div class="grid two"><article class="card"><h3>Nội địa · chuẩn bị năng lực quản trị</h3><p>Tiếng Việt nối ERP, hồ sơ, quy trình và dữ liệu với việc chuẩn bị đáp ứng yêu cầu của khách hàng trong chuỗi bán dẫn. Nội dung giúp người phụ trách hiểu cần chuẩn bị gì khi bước vào chuỗi.</p></article><article class="card"><h3>FDI · giải quyết việc vận hành</h3><p>English/Chinese đi từ lot, WIP, chất lượng hoặc phối hợp gia công ngoài tới giá trị về thời gian, trách nhiệm và kiểm soát rủi ro. Ngôn ngữ được chọn theo người đọc.</p></article></div><p>Tệp công ty chính/dự phòng phục vụ LinkedIn. Với Search, Bảo chọn theo ý định truy vấn và thị trường Việt Nam; ngôn ngữ tìm kiếm là một tín hiệu về nội dung cần phục vụ, còn vai trò và loại doanh nghiệp được xác minh khi có thông tin phù hợp.</p></section>
<section id="landing" class="logic-section"><h2>2. Ba trang đích theo ba bài toán</h2><p>Cả ba trang hiện có bản Việt, English, giản thể và phồn thể. Quảng cáo dẫn thẳng tới ngôn ngữ phù hợp; mỗi trang nối câu hỏi vận hành với cơ chế giải pháp, nội dung tham khảo và tư vấn.</p>{{LANDINGS}}<p class="logic-muted">Ảnh chụp nội dung trang hiện hành ngày 08/10/2026, mở được trong thư mục này. Các liên kết ngôn ngữ mở toàn bộ trang trực tuyến và cần Internet. Nhóm Supplier ở phép thử này là nhà cung ứng công nghiệp trong chuỗi bán dẫn/điện tử.</p></section>
<section id="keywords" class="logic-section"><h2>3. Bộ từ khóa nhỏ, tách theo ngôn ngữ</h2><p>Mỗi ngôn ngữ có hai từ khóa khởi đầu cho mỗi bài toán và một từ khóa thương hiệu. Dấu ngoặc kép là đề xuất đối sánh cụm từ; ngoặc vuông là đề xuất đối sánh chính xác. Từ khóa thương hiệu được đọc riêng với nhu cầu giải pháp.</p><p>Tra cứu trước đây phần lớn hiển thị dấu gạch ngang ở các chỉ số. Bảo dùng dữ liệu này để giữ phép thử nhỏ; lượng nhu cầu thực tế sẽ được đọc qua phân phối và truy vấn trong kỳ chạy. Hai từ khóa Supplier mỗi ngôn ngữ được bổ sung để tập trung vào nhà máy PCB và linh kiện.</p>{{KEYWORDS}}<p class="note">Loại trừ đề xuất tập trung vào tuyển dụng, học tập và chứng khoán. Bảo rà ngữ cảnh trước khi áp dụng; giữ lại các từ mang ý nghĩa nghiệp vụ như ERP, MES, test, chất lượng và truy xuất.</p><p class="logic-muted">Tệp tải xuống là danh mục để chọn và rà trước khi chạy. <a href="../05_Evidence/evidence.html#planner">Xem ảnh nghiên cứu Keyword Planner</a>.</p></section>
<section id="tracking" class="logic-section"><h2>4. Tracking nối quảng cáo với hành vi đọc</h2><p>Ba trang đã có đo phần nội dung được xem và thời gian đọc. Bảo dùng lại hệ thống này, ghép dữ liệu theo nguồn Google, campaign, trang đích, ngôn ngữ quảng cáo và cùng kỳ đo để review.</p><div class="flow"><div class="step"><b>Quảng cáo → đúng trang</b><p>Link mang ngôn ngữ đích, UTM và mã nhấp Google khi có; phân biệt nhóm ý định và mẫu quảng cáo.</p></div><div class="step"><b>Trang → nội dung được đọc</b><p>GA4 theo dõi phiên, phiên có tương tác; sự kiện section ghi phần nội dung đã xem và thời gian chú ý.</p></div><div class="step"><b>Dữ liệu → hành động</b><p>Đối chiếu chi phí, truy vấn và mức đọc theo cùng nhóm, rồi chọn phần tiếp tục hoặc cần sửa.</p></div></div><details><summary>Những việc Bảo kiểm trước khi bật probe</summary><ol><li>Kiểm link quảng cáo tới đúng trang và ngôn ngữ, giữ nguồn Google xuyên hành trình.</li><li>Đối chiếu phiên và các sự kiện nội dung trên cả ba route; dùng tag hiện có.</li><li>Kiểm cách đọc nguồn, campaign, ngôn ngữ quảng cáo và kỳ đo trong báo cáo.</li><li>Khi đưa lead vào đánh giá, đối chiếu gửi form thành công, nơi nhận và lead hợp lệ. Click nút tư vấn được đọc là bước quan tâm.</li></ol><p class="logic-muted">Sự kiện nội dung đang dùng: <code>section_view</code> và <code>section_engagement_time</code>. Đây là dữ liệu mức đọc; mục tiêu chuyển đổi dùng cho đấu giá cần được chọn theo kết quả kinh doanh đã kiểm chứng.</p></details></section>
<section id="probe" class="logic-section"><h2>5. Search probe trong phần ngân sách tùy chọn</h2><p>Sau review tuần 1, Bảo chọn thời điểm dùng Search theo dữ liệu và phần ngân sách giữ lại. Mức tối đa là 500.000 đồng, chưa thuế, nằm trong tổng 11,7 triệu.</p><ol class="probe-list"><li><b>Chọn một giả thuyết.</b> Một nhóm ý định, một ngôn ngữ và trang đích tương ứng; có thể bắt đầu từ OSAT, Fabless hoặc Supplier theo cơ sở ưu tiên lúc review.</li><li><b>Chạy phạm vi hẹp.</b> Ưu tiên exact/phrase, Google Search tại Việt Nam; chọn mức chi và giá thầu theo tín hiệu thực tế. Tách nhu cầu giải pháp khỏi từ khóa Digiwin.</li><li><b>Đọc điều người dùng thực sự gõ.</b> Rà toàn bộ truy vấn hiển thị trong nhóm và kỳ đo, phân loại đúng ý định, không phù hợp và chưa rõ; kiểm hành vi đọc sau click trong cùng nhóm báo cáo.</li><li><b>Review rồi mới chuyển nhóm.</b> Tiếp tục phần có tín hiệu phù hợp, sửa đúng khâu yếu hoặc giữ lại ngân sách khi dữ liệu mỏng. Lượng tìm kiếm thấp là lý do quan sát thêm, giữ phạm vi phù hợp và chi theo nhu cầu thực tế.</li></ol></section>
<section id="measurement" class="logic-section"><h2>6. Đo chất lượng nhu cầu, mức đọc và chi phí</h2><p>Bảo ghi lượng dữ liệu thực tế cùng mỗi tỷ lệ. Truy vấn đúng ý định là nhu cầu quản lý/giải pháp gắn với hoạt động nhà máy; tuyển dụng, học thuật và chứng khoán được xếp riêng. Truy vấn chưa đủ ngữ cảnh giữ ở nhóm “chưa rõ”.</p>{{METRICS}}<p class="logic-muted">Search terms report chỉ hiển thị một phần truy vấn. Vì vậy, tỷ lệ đúng ý định luôn đi kèm độ bao phủ. Dữ liệu truy vấn và GA4 được đối chiếu ở cùng nhóm và kỳ đo; hành vi từng người dùng được đọc theo phạm vi dữ liệu có thể quan sát.</p><h3>Tín hiệu nào dẫn đến hành động nào?</h3>{{DECISIONS}}<p>Lead đã xác minh là tín hiệu thương mại bổ sung. Khi dữ liệu còn ít, Bảo báo cả số quan sát, độ bao phủ và phần cần theo dõi thêm để quyết định tiếp tục, điều chỉnh hoặc giữ ngân sách.</p></section>
<details class="sources"><summary>Cách đọc chỉ số · tài liệu Google</summary><ul><li><a href="https://support.google.com/google-ads/answer/2472708?hl=en" target="_blank" rel="noopener">Search terms report</a>: đọc truy vấn tạo ra quảng cáo, trong phạm vi Google hiển thị.</li><li><a href="https://support.google.com/analytics/answer/12798876?hl=en" target="_blank" rel="noopener">Phiên có tương tác trong GA4</a>: dùng định nghĩa và cấu hình của hệ thống đo đang áp dụng.</li><li><a href="https://support.google.com/google-ads/answer/11461796?hl=en" target="_blank" rel="noopener">Mục tiêu chuyển đổi chính/phụ</a>: phân biệt dữ liệu quan sát và mục tiêu được dùng cho đấu giá.</li></ul></details><div class="actions"><a class="button primary" href="../01_De_xuat/de_xuat.html#ba-diem">Về ngân sách và 3 điểm góp ý</a><a class="button" href="../01_De_xuat/logic_quang_cao.html">Logic LinkedIn và nội dung</a></div>'''

ZH = '''<p class="eyebrow">Google Search · 從需求到決策</p><h1>接住正在尋找<br>工廠管理解決方案的人</h1><p class="lead">LinkedIn 透過具體管理問題，建立對 Digiwin 的品牌聯想。Google Search 則承接另一種情境：讀者已主動尋找解決方法，我會引導他們進入對應主題與語言的落地頁。</p>
<div class="grid"><section class="card"><small>選用 Search 預算 · 未稅</small><div class="stat">≤ 50 萬越盾</div><p>包含在整體 1,170 萬越盾上限內。</p></section><section class="card"><small>承接搜尋需求的內容</small><div class="stat">3 個落地頁</div><p>OSAT、Fabless 與工業供應商。</p></section><section class="card"><small>依讀者選擇版本</small><div class="stat">4 種語言</div><p>越文、英文、簡體與繁體；逐組選擇測試。</p></section></div>
<div class="logic-links"><a href="#hypothesis">內容假設</a><a href="#landing">3 個落地頁</a><a href="#keywords">各語言關鍵字</a><a href="#tracking">追蹤設定</a><a href="#probe">搜尋測試</a><a href="#measurement">衡量與決策</a></div>
<section id="hypothesis" class="logic-section"><h2>1. 先找到對的問題，再考慮擴大</h2><p>我的假設是：同時帶有生產情境與管理需求的查詢，比「半導體」這類廣泛詞更能帶來適合閱讀 Digiwin 內容的人。我會先測試少量群組，依實際搜尋字詞選擇值得延續的部分。</p><div class="grid two"><article class="card"><h3>本土企業 · 準備管理能力</h3><p>越文內容將 ERP、文件、流程與數據，連結到因應半導體供應鏈客戶要求的準備，幫助負責人了解需要建立哪些能力。</p></article><article class="card"><h3>外資企業 · 解決營運問題</h3><p>英文與中文從批次、在製品、品質或委外協作切入，再說明時間、責任分工與風險控管的價值。語言依實際讀者選擇。</p></article></div><p>主要與備用公司名單用於 LinkedIn。Search 則依查詢意圖及越南市場選擇投放；搜尋語言協助判斷應提供的內容，企業類型與職務角色會在取得適當資訊後分別確認。</p></section>
<section id="landing" class="logic-section"><h2>2. 三類問題，三個落地頁</h2><p>三個現行頁面均有越文、英文、簡體與繁體版本。廣告直接連到對應語言，頁面再串起營運問題、解決機制、參考內容與諮詢。</p>{{LANDINGS}}<p class="logic-muted">截圖為 2026/10/08 現行頁面的營運內容，可在本資料夾內開啟。各語言連結開啟完整線上頁面，需要網路。本次 Supplier 測試聚焦半導體／電子供應鏈的工業供應商。</p></section>
<section id="keywords" class="logic-section"><h2>3. 依語言準備小型關鍵字組</h2><p>每種語言為每類問題準備兩個起始關鍵字，另有一個品牌詞。雙引號表示建議採用詞組比對，方括號表示完全比對。品牌搜尋與解決方案需求分開判讀。</p><p>先前查量紀錄多數以橫線顯示指標，因此我會維持小範圍測試，再由實際投遞與查詢了解需求。各語言的兩個 Supplier 詞為新增假設，聚焦 PCB 與零組件工廠。</p>{{KEYWORDS}}<p class="note">排除詞建議集中於求職、學習與證券。我會先檢查語境，再套用排除；ERP、MES、測試、品質與追溯等業務用語則保留。</p><p class="logic-muted">下載檔案供投放前選擇與檢視。<a href="../05_Evidence/evidence.zh-Hant.html#planner">查看 Keyword Planner 研究截圖</a>。</p></section>
<section id="tracking" class="logic-section"><h2>4. 讓廣告來源接上閱讀行為</h2><p>三個頁面已具備內容區塊瀏覽與閱讀時間追蹤。我會沿用現有系統，以 Google 來源、廣告活動、落地頁、廣告語言及同一期間，對照各組數據。</p><div class="flow"><div class="step"><b>廣告 → 對應頁面</b><p>連結帶入目標語言、UTM，以及可用的 Google 點擊識別碼；區分意圖群組與廣告版本。</p></div><div class="step"><b>頁面 → 閱讀內容</b><p>GA4 觀察工作階段與互動工作階段；區塊事件記錄看過的內容及注意時間。</p></div><div class="step"><b>數據 → 行動</b><p>在同一群組對照花費、查詢與閱讀情況，再決定延續或改善哪些環節。</p></div></div><details><summary>啟動測試前，我會核對的項目</summary><ol><li>廣告連結進入正確頁面及語言，並保留 Google 來源資訊。</li><li>核對三個頁面的工作階段與內容事件，沿用現有標籤。</li><li>確認報表能依來源、廣告活動、廣告語言與期間判讀。</li><li>評估潛在客戶時，核對表單送出成功、接收位置與資料有效性。諮詢按鈕點擊作為初步關注訊號。</li></ol><p class="logic-muted">目前內容事件為 <code>section_view</code> 與 <code>section_engagement_time</code>，用來觀察閱讀程度；競價使用的轉換目標，則依已核對的商業結果選定。</p></details></section>
<section id="probe" class="logic-section"><h2>5. 在選用預算內進行搜尋測試</h2><p>第一週檢視後，我會依數據與保留預算，選擇啟用 Search 的時機。最高 50 萬越盾，未稅，包含在整體 1,170 萬越盾內。</p><ol class="probe-list"><li><b>選一個假設。</b> 一組意圖、一種語言及對應落地頁；依檢視時的優先依據，從 OSAT、Fabless 或 Supplier 選擇。</li><li><b>維持小範圍。</b> 優先使用完全／詞組比對，在越南投放 Google Search；依實際訊號選擇花費節奏與出價。Digiwin 品牌搜尋另行觀察。</li><li><b>讀實際查詢。</b> 檢視同群組、同期間顯示的全部查詢，分成符合意圖、不適合及待釐清，再以同組報表檢查點擊後的閱讀行為。</li><li><b>檢視後再換下一組。</b> 延續適合的部分、改善薄弱環節，或在數據少時保留預算。搜尋量低時，我會延長觀察、維持合適範圍，依實際需求花費。</li></ol></section>
<section id="measurement" class="logic-section"><h2>6. 衡量需求品質、閱讀程度與成本</h2><p>每個比率都會附上實際觀察量。符合意圖的查詢須連結工廠營運與管理／解決方案需求；求職、學術及證券另行分類。語境不足的查詢保留為「待釐清」。</p>{{METRICS}}<p class="logic-muted">Search terms report 顯示部分查詢，因此意圖符合率會同時附上涵蓋率。查詢與 GA4 數據按相同群組及期間對照；個別使用者行為則依可觀察的資料範圍判讀。</p><h3>不同訊號，對應不同調整</h3>{{DECISIONS}}<p>經確認的潛在客戶是補充的商業訊號。數據少時，我會一併報告觀察量、涵蓋率與需持續追蹤的部分，再決定延續、調整或保留預算。</p></section>
<details class="sources"><summary>指標說明 · Google 文件</summary><ul><li><a href="https://support.google.com/google-ads/answer/2472708?hl=en" target="_blank" rel="noopener">Search terms report</a>：依 Google 顯示範圍，閱讀觸發廣告的查詢。</li><li><a href="https://support.google.com/analytics/answer/12798876?hl=en" target="_blank" rel="noopener">GA4 互動工作階段</a>：依現行衡量系統的定義與設定判讀。</li><li><a href="https://support.google.com/google-ads/answer/11461796?hl=en" target="_blank" rel="noopener">主要與次要轉換動作</a>：區分觀察資料與競價使用的目標。</li></ul></details><div class="actions"><a class="button primary" href="../01_De_xuat/de_xuat.zh-Hant.html#ba-diem">回到預算與三項確認事項</a><a class="button" href="../01_De_xuat/logic_quang_cao.zh-Hant.html">LinkedIn 與內容策略</a></div>'''

METRICS = [
 ['Truy vấn có đúng nhu cầu?','Click từ truy vấn đúng ý định ÷ click của toàn bộ truy vấn hiển thị đã rà.','Google Ads · ghi cả click, số truy vấn và nhóm chưa rõ.'],
 ['Đã nhìn thấy bao nhiêu dữ liệu?','Click trong Search terms report ÷ tổng click Search của cùng campaign và kỳ.','Độ bao phủ giúp giới hạn kết luận của tỷ lệ đúng ý định.'],
 ['Người vào có đọc?','Phiên, phiên có tương tác, tỷ lệ tương tác; phần nội dung được xem và thời gian đọc.','GA4 · cùng nguồn, campaign, trang đích, ngôn ngữ quảng cáo và kỳ đo.'],
 ['Chi phí có hợp lý?','Chi dashboard, CPC; chi phí/phiên có tương tác = chi cùng nhóm ÷ số phiên có tương tác, khi dữ liệu đã đối chiếu và có phiên.','Đọc cùng chất lượng truy vấn và mức đọc; số thiếu dữ liệu được ghi rõ.'],
 ['Có cơ hội tiếp cận nhu cầu lõi?','Impressions và impression share của nhóm từ khóa lõi, khi có dữ liệu.','Đọc trong phạm vi từ khóa đã chọn, kết hợp khả năng phân phối và ngân sách.']]
METRICS_ZH = [
 ['查詢是否符合需求？','符合意圖的查詢點擊 ÷ 已檢視可見查詢的全部點擊。','Google Ads · 同時記錄點擊、查詢量與待釐清群組。'],
 ['可觀察資料有多少？','Search terms report 點擊 ÷ 同活動、同期間的 Search 總點擊。','涵蓋率用來界定意圖符合率的解讀範圍。'],
 ['進站後是否閱讀？','工作階段、互動工作階段、互動率，以及瀏覽的區塊和閱讀時間。','GA4 · 來源、活動、落地頁、廣告語言與期間一致。'],
 ['成本是否合理？','後台花費、CPC；同群組數據已核對且有互動工作階段時，以同組花費 ÷ 互動工作階段數，計算每次互動工作階段成本。','與查詢品質及閱讀程度一起判讀，清楚註明資料缺漏。'],
 ['核心需求的曝光機會？','核心關鍵字群的曝光與曝光比重，以可取得的資料為準。','依所選關鍵字範圍，結合投遞情況與預算判讀。']]
DECISIONS = [
 ['查詢偏離需求','收斂關鍵字、比對方式與排除詞。'],['查詢適合，閱讀偏弱','檢查廣告承諾、語言與落地頁內容銜接。'],['來源或數據有落差','先核對衡量資料，再評估內容。'],['查詢與閱讀訊號適合，成本可接受','在上限內延續，或選下一組測試。'],['投遞低或樣本少','延長觀察、縮小範圍或保留預算。']]
DECISIONS_VI = [
 ['Truy vấn lệch nhu cầu','Thu hẹp từ khóa, cách đối sánh và loại trừ.'],['Truy vấn phù hợp, mức đọc yếu','Kiểm lời hứa quảng cáo, ngôn ngữ và mạch nội dung trang đích.'],['Nguồn hoặc số liệu lệch nhau','Đối chiếu đo lường trước khi đánh giá nội dung.'],['Truy vấn và mức đọc phù hợp, chi phí chấp nhận được','Tiếp tục trong trần hoặc chọn nhóm thử tiếp theo.'],['Phân phối thấp hoặc mẫu mỏng','Quan sát thêm, thu hẹp phạm vi hoặc giữ lại ngân sách.']]

def write_txt():
 for loc,name in zip(LOCALES,NAMES):
  groups=['OSAT','Fabless','Supplier / industrial factory','Digiwin brand / report separately']
  head={
   'vi':'BỘ TỪ KHÓA THỬ · '+name+'\nChọn từng nhóm trước khi chạy; thị trường Việt Nam. Dấu " ": cụm từ; [ ]: chính xác.\nSupplier là nhà cung ứng công nghiệp. Từ khóa thương hiệu được đo riêng.\nBộ từ Việt này là đề xuất để chọn thử, chờ tra volume riêng. Nghiên cứu trước đó dùng các cụm khác; không gán số liệu cũ cho từ mới.\n',
   'en':'SEARCH PROBE KEYWORDS · English\nSelect one intent group before launch; Vietnam market. Quotation marks: proposed phrase match; brackets: proposed exact match.\nSupplier means industrial manufacturers. Report brand demand separately.\nSupplier terms are new hypotheses pending volume research. Other seeds have recorded Planner checks with dashes shown for metrics.\n',
   'zh-Hans':'搜索测试关键词 · 简体中文\n投放前选择一个意图组；越南市场。双引号：建议词组匹配；方括号：建议完全匹配。\nSupplier指工业供应商。品牌需求单独衡量。\nSupplier词为新增假设，待查量；其余词有Planner查询记录，指标显示横线。\n',
   'zh-Hant':'搜尋測試關鍵字 · 繁體中文\n投放前選擇一個意圖群組；越南市場。雙引號：建議詞組比對；方括號：建議完全比對。\nSupplier指工業供應商。品牌需求分開衡量。\nSupplier詞為新增假設，待查量；其餘詞有Planner查詢紀錄，指標顯示橫線。\n'}[loc]
  body=head
  for i,g in enumerate(groups):
   body+='\n'+g+'\n'+('\n'.join(TERMS[loc][i*2:i*2+2]))+'\n'
   if i<3: body+=URLS[i]+'?lang='+loc+'\n'
  body+= {'vi':'\nThương hiệu: chọn trang theo ý định truy vấn. Dữ liệu chưa hiển thị không có nghĩa nhu cầu bằng 0.\n','en':'\nBrand: select the destination by query intent. Missing displayed metrics do not imply zero demand.\n','zh-Hans':'\n品牌词：依查询意图选择页面。未显示指标不等于零需求。\n','zh-Hant':'\n品牌詞：依查詢意圖選擇頁面。未顯示指標不等於零需求。\n'}[loc]
  OUT.joinpath('Tu_khoa').mkdir(exist_ok=True)
  OUT.joinpath('Tu_khoa',loc+'.txt').write_text(body,encoding='utf-8-sig')
  note={'vi':'LOẠI TRỪ ĐỀ XUẤT · Tiếng Việt\nRà ngữ cảnh truy vấn và chọn cách đối sánh trước khi áp dụng. Giữ các từ nghiệp vụ ERP, MES, WIP, test, chất lượng và truy xuất.\n','en':'PROPOSED NEGATIVES · English\nReview query context and match type before applying. Retain business terms ERP, MES, WIP, test, quality and traceability.\n','zh-Hans':'排除词建议 · 简体中文\n应用前检查查询语境及匹配方式。保留ERP、MES、在制品、测试、质量与追溯等业务用语。\n','zh-Hant':'排除詞建議 · 繁體中文\n套用前檢查查詢語境及比對方式。保留ERP、MES、在製品、測試、品質與追溯等業務用語。\n'}[loc]
  OUT.joinpath('Loai_tru').mkdir(exist_ok=True)
  OUT.joinpath('Loai_tru',loc+'.txt').write_text(note+'\n'+'\n'.join(NEG[loc])+'\n',encoding='utf-8-sig')

def main():
 OUT.mkdir(exist_ok=True)
 base=(PACK/'BAT_DAU.html').read_text(encoding='utf-8-sig')
 styles=''.join(re.findall(r'<style[^>]*>.*?</style>',base,re.S))
 script=re.search(r'<script id="package-locale-script">.*?</script>',base,re.S).group()
 extra='<style>.landing{padding:0;overflow:hidden}.landing img{width:100%;height:auto;display:block}.landing h3,.landing p,.landing .locale-links{margin:18px 21px}.landing h3{font-size:20px}.locale-links{display:flex;gap:8px;flex-wrap:wrap}.locale-links a{display:inline-flex;align-items:center;min-height:44px;padding:5px 10px;border:1px solid #cbd5e1;border-radius:7px;font-size:14px}details{margin:18px 0;background:white;border:1px solid #e2e8f0;border-radius:12px;padding:18px 22px}summary{font-weight:bold;color:#174db3;cursor:pointer;min-height:28px}details p:last-child{margin-bottom:4px}code{font:inherit;overflow-wrap:anywhere}.probe-list li{padding:5px 0}.sources{font-size:15px}.logic-section{scroll-margin-top:24px}nav{gap:9px 18px}nav strong{white-space:nowrap}table td{overflow-wrap:anywhere}@media(min-width:761px){.landing img{aspect-ratio:1521/728;object-fit:contain}.logic-table th:first-child{width:24%}}</style>'
 for zh,body in [(False,VI),(True,ZH)]:
  suffix='.zh-Hant' if zh else ''
  switch='<a class="package-language-switch" href="index'+('' if zh else '.zh-Hant')+'.html" role="switch" aria-checked="'+str(zh).lower()+'" aria-label="'+('切換至越南文' if zh else 'Chuyển sang tiếng Trung phồn thể')+'"><span class="language-vi" lang="vi" aria-hidden="true">Tiếng Việt</span><span class="language-track" aria-hidden="true"></span><span class="language-zh" lang="zh-Hant" aria-hidden="true">繁體中文</span></a>'
  paths=['../BAT_DAU'+suffix+'.html','../01_De_xuat/de_xuat'+suffix+'.html','../01_De_xuat/logic_quang_cao'+suffix+'.html','index'+suffix+'.html','../02_Demo/index'+suffix+'.html','../03_Thu_vien/index'+suffix+'.html']
  names=['開始','提案','廣告策略','Google Search','內容示例','素材庫'] if zh else ['Bắt đầu','Đề xuất','Logic quảng cáo','Google Search','Demo','Thư viện']
  nav='<header><nav><strong>Digiwin · '+('廣告投放提案' if zh else 'Paid ads bán dẫn')+'</strong>'+''.join('<a href="'+p+'"'+(' aria-current="page"' if i==3 else '')+'>'+n+'</a>' for i,(p,n) in enumerate(zip(paths,names)))+switch+'</nav></header>'
  body=body.replace('{{LANDINGS}}',landing_cards(zh)).replace('{{KEYWORDS}}',download_blocks(zh)).replace('{{METRICS}}',table(['評估問題','衡量方式','資料來源與用途'] if zh else ['Điều cần đánh giá','Cách đo','Nguồn và cách dùng'],METRICS_ZH if zh else METRICS)).replace('{{DECISIONS}}',table(['觀察訊號','我的調整'] if zh else ['Tín hiệu quan sát','Bảo điều chỉnh'],DECISIONS if zh else DECISIONS_VI))
  html='<!doctype html><html lang="'+('zh-Hant' if zh else 'vi')+'"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>Google Search · Digiwin</title>'+styles+extra+'</head><body>'+nav+'<main>'+body+'</main><footer>'+('Digiwin · 廣告投放提案 · 2026/10/08' if zh else 'Bảo gửi Vy · 08/10/2026')+'</footer>'+script+'</body></html>'
  OUT.joinpath('index'+suffix+'.html').write_text(html,encoding='utf-8')
 write_txt()
 # Only wrappers change; original journeys, readers, images, workbook and evidence stay intact.
 wrappers=['BAT_DAU','01_De_xuat/de_xuat','01_De_xuat/logic_quang_cao','01_De_xuat/mail_gui_Vy','02_Demo/index','03_Thu_vien/index']
 for key in wrappers:
  for zh in [False,True]:
   suffix='.zh-Hant' if zh else ''
   f=PACK/(key+suffix+'.html'); s=f.read_text(encoding='utf-8-sig')
   prefix='' if '/' not in key else '../'
   google=prefix+'06_Google/index'+suffix+'.html'
   navlink='<a href="'+google+'">Google Search</a>'
   assert navlink not in s
   s=s.replace('<a class="package-language-switch"',navlink+'<a class="package-language-switch"',1)
   if key=='BAT_DAU':
    block='<section class="note logic-mini"><h2>'+('Google Search · 接住主動搜尋的需求' if zh else 'Google Search · đón nhu cầu chủ động')+'</h2><p>'+('三個落地頁、各語言關鍵字、追蹤設定及小型測試的衡量方式，串起查詢到決策。' if zh else 'Ba trang đích, từ khóa theo ngôn ngữ, tracking và cách đo phép thử nhỏ nối từ truy vấn tới quyết định.')+'</p><a href="'+google+'">'+('查看 Google Search 方案' if zh else 'Xem phương án Google Search')+'</a></section>'
    s=s.replace('<h2>'+('兩組受眾，兩種內容方向' if zh else 'Hai nhóm, hai hướng nội dung')+'</h2>',block+'<h2>'+('兩組受眾，兩種內容方向' if zh else 'Hai nhóm, hai hướng nội dung')+'</h2>')
   elif key=='01_De_xuat/de_xuat':
    block='<h2>'+('Google Search · 承接解決方案需求' if zh else 'Google Search · bắt nhu cầu tìm giải pháp')+'</h2><p>'+('Search 以小型測試承接主動尋找工廠管理解決方案的人。OSAT、Fabless 與工業供應商各有落地頁及四種語言版本；我會逐組選擇關鍵字，對照實際查詢、閱讀程度與成本。最高 50 萬越盾包含在整體預算內。' if zh else 'Search dùng phép thử nhỏ để đón người chủ động tìm giải pháp quản lý nhà máy. OSAT, Fabless và Supplier có ba trang đích với bốn ngôn ngữ; Bảo chọn từng nhóm từ khóa, đọc truy vấn thực tế, mức đọc và chi phí. Tối đa 500.000 đồng nằm trong tổng ngân sách.')+' <a href="'+google+'">'+('查看 Google Search 方案與衡量方式' if zh else 'Xem phương án Google Search và cách đo')+'</a>。</p>'
    if not zh: block=block.replace('</a>。</p>','</a>.</p>')
    marker=re.search(r'<h2[^>]*>[^<]*(?:Ngân sách|預算)[^<]*</h2>',s)
    assert marker, f
    s=s[:marker.start()]+block+s[marker.start():]
   elif key=='01_De_xuat/logic_quang_cao':
    block='<section id="google" class="logic-section"><h2>'+('6. Search · 承接已出現的需求' if zh else '6. Search · nối với nhu cầu đang có')+'</h2><p>'+('LinkedIn 建立品牌與管理問題的聯想，Search 則觀察主動搜尋該問題的人。我的假設是具體工廠意圖能帶來適合的閱讀；以查詢符合率、資料涵蓋率、閱讀程度與成本，決定延續或調整。' if zh else 'LinkedIn xây liên tưởng về Digiwin và bài toán quản trị; Search quan sát người đang chủ động tìm giải pháp cho bài toán đó. Giả thuyết là ý định nhà máy cụ thể sẽ đưa người phù hợp vào đọc; tỷ lệ truy vấn đúng ý định, độ bao phủ, mức đọc và chi phí giúp Bảo chọn tiếp tục hay điều chỉnh.')+'</p><a href="'+google+'">'+('查看三個落地頁、關鍵字與搜尋測試' if zh else 'Xem ba trang đích, từ khóa và phép thử Search')+'</a></section>'
    s=s.replace('</main>',block+'</main>')
   elif key=='01_De_xuat/mail_gui_Vy':
    para='<p>'+('我也補上 Google Search 方案，包含三個落地頁、各語言關鍵字、追蹤與測試衡量方式，說明如何運用選用的 50 萬越盾預算。' if zh else 'Bảo cũng bổ sung tab Google Search: ba trang đích, bộ từ khóa theo ngôn ngữ, tracking và cách đo probe, để Vy thấy cách sử dụng phần Search tùy chọn 500.000 đồng.')+' <a href="'+google+'">Google Search</a></p>'
    marker='<p>你可以開啟' if zh else '<p>Vy mở'
    assert marker in s, f
    s=s.replace(marker,para+marker,1)
   f.write_text(s,encoding='utf-8')
 # Text proposal mirrors the reader's essential Google logic.
 proposal=PACK/'01_De_xuat/De_xuat_paid_ads.md'
 s=proposal.read_text(encoding='utf-8-sig')
 s=s.replace('## Ngân sách chưa thuế','## Google Search · bắt nhu cầu tìm giải pháp\n\nSearch dùng phép thử nhỏ để đón người chủ động tìm giải pháp quản lý nhà máy. OSAT, Fabless và Supplier có ba trang đích với bốn ngôn ngữ; Bảo chọn từng nhóm từ khóa, đọc truy vấn thực tế, mức đọc và chi phí. Tối đa 500.000 đồng nằm trong tổng ngân sách.\n\n[Xem ba trang đích, từ khóa, tracking và cách đo Search probe](../06_Google/index.html).\n\n## Ngân sách chưa thuế')
 proposal.write_text(s,encoding='utf-8')
 logic=PACK/'01_De_xuat/Logic_quang_cao.md'
 with logic.open('a',encoding='utf-8') as f: f.write('\n\n## 6. Search · nối với nhu cầu đang có\n\nLinkedIn xây liên tưởng về Digiwin và bài toán quản trị; Search quan sát người đang chủ động tìm giải pháp cho bài toán đó. Bảo dùng truy vấn thực tế, độ bao phủ, hành vi đọc và chi phí để chọn tiếp tục hay điều chỉnh từng nhóm nhỏ.\n\n[Xem ba trang đích, từ khóa theo ngôn ngữ, tracking và cách đo probe](../06_Google/index.html).\n')
 mail=PACK/'01_De_xuat/Mail_gui_Vy.md'
 s=mail.read_text(encoding='utf-8-sig'); s=s.replace('Vy mở **BAT_DAU.html**','Bảo cũng bổ sung tab Google Search: ba trang đích, bộ từ khóa theo ngôn ngữ, tracking và cách đo probe, để Vy thấy cách sử dụng phần Search tùy chọn 500.000 đồng.\n\nVy mở **BAT_DAU.html**')
 mail.write_text(s,encoding='utf-8')
 doc=PACK/'DOC_TRUOC.txt'
 with doc.open('a',encoding='utf-8') as f: f.write('\nTab Google Search có ba trang đích, từ khóa theo ngôn ngữ, tracking và cách đo probe. Ảnh xem trước nằm trong thư mục; các trang đích đầy đủ mở trực tuyến và cần Internet.\n')
 print(json.dumps({'google_files':len(list(OUT.rglob('*.*'))),'package_files':len([p for p in PACK.rglob('*') if p.is_file()])}))

if __name__=='__main__': main()
