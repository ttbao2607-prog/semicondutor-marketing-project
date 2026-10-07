# Package v2 · danh sách nội dung và đầu việc cần rà

Đây là danh sách đầu vào để Bảo thiết kế lại package, **chưa phải execution plan**. Mọi dòng đều là đối tượng cần cân nhắc ghi vào package; không mặc định phải giữ toàn bộ hoặc giữ cách trình bày của v1. Những việc đang mở được liệt kê để package phản ánh đúng tình hình, không được kích hoạt bởi danh sách này.

Baseline tiến độ: [Main/worktree reconciliation07/10](../LinkedIn_Current_Progress_2026-10-07.md) tại main `196f26b`. Hai lane creative đang hoạt động có thể tiến thêm; refresh receipt lúc chọn nguồn v2. Lượt inventory này không có live-account readback hoặc audit artifact mới.

## Nội dung business và thông điệp

| ID | Nội dung/việc cần ghi vào package | Căn cứ hiện có và phần để Bảo đổi |
|---|---|---|
| V2-01 | Mục đích package, người đọc và những quyết định package cần hỗ trợ | V1 là manager package. Mục đích/người đọc/độ sâu cho v2 chờ chỉ đạo Bảo; chưa chọn dạng report, trình chiếu hoặc dashboard. |
| V2-02 | Định nghĩa thị trường và khách hàng mục tiêu: supply chain bán dẫn/điện tử, OSAT/Fabless/industrial supplier | Email Vy/anchor và kickoff. Không mặc định Intel/Amkor/Samsung là ERP prospects; entity/authority phù hợp cần evidence. |
| V2-03 | Hai pipeline VN nội địa và FDI, personas/decision makers và locale | VN readiness khác FDI operating value; English/zh-Hans/zh-Hant là creative locales, không suy thành3pool audience độc lập. |
| V2-04 | Message map, trigger vận hành, business value và proof theo từng journey | ROI có thể implicit; không ép ROI số. VN không hứa mua ERP là đủ chuẩn/audit/đơn hàng. Partner không lẫn SI/phần mềm. |
| V2-05 | Hướng cold/explanation/proof/reader và vai trò các kênh | Hiện hành Single image cold → new-ad member audience → Carousel RMK. Search tùy chọn có scope riêng. Nếu Bảo đổi hướng v2, ghi decision mới rõ; không lấy hướng cold Carousel cũ làm current. |
| V2-06 | Source/case attribution, phạm vi claim và quyền sử dụng | Named case/entity/geography, integrated ERP+iMES, nguồn/ngôn ngữ và authentic photo rights. Không trộn kết quả case vào Digiwin Vietnam hoặc claim mới. |

## Audience và tình hình triển khai

| ID | Nội dung/việc cần ghi vào package | Căn cứ hiện có và phần còn mở |
|---|---|---|
| V2-07 | Tệp công ty cung cấp ban đầu: nghiên cứu/sửa định danh đã làm, trạng thái hiện tại |424dòng đã rà;101supported/323investigated blockers; update existing Discovery1lần, saved filename verified. Last Updating06/10. Chỉ liệt kê pending processing/readback, không mở lại cleanup từ đầu. |
| V2-08 | Kết quả mapping/reach sau xử lý của tệp gốc | Readback mới chưa có tại baseline; kiểm historical wrong mappings/enriched rows và filtered reach.780/80%/member counts cũ phải gắn ngày/revision, không forecast như kết quả sau repair. |
| V2-09 | Contingency backup độc lập: Master203, R5-52 và điều kiện sử dụng | R5 Ready/>90%, Details0; VN English seniority/functions estimate460, không qualified buyers. Đề xuất recheck24h chưa schedule; không thay thế tệp gốc hoặc coi backup đã release. |
| V2-10 | Audience-to-persona/locale mapping và qualifying assumptions | Company Page match, pháp nhân/local employer, ICP/buyer authority, English setting và Chinese creative là những yếu tố riêng. Không trình bày match rate như tỷ lệ đúng khách hàng. |
| V2-11 | RMK từ chính ads mới: source, rule/lookback, size/eligibility và readiness | Route Single image đã chốt; exact production source/rule/window/count vẫn cần evidence. Không dùng existing Page pool/website RMK thay route mặc định. Không viết lại gap Carousel-engager cũ thành blocker mới. |
| V2-12 | Campaign/objective/targeting/placement/schedule và trạng thái build/release | List những setting cần quyết định/kiểm; chưa dựng cấu trúc hay lịch mới. Chưa publish/enable/spend; không đẩy công việc live bằng việc đóng package. |

## Creative, demo, reader và thư viện

| ID | Nội dung/việc cần ghi vào package | Nguồn và trạng thái |
|---|---|---|
| V2-13 | Ma trận treatment/persona/locale và số selected artifacts | Ghi theo manifest/approval, phân biệt originals/correctives/reuse/finals; không ép quota nếu intake/proof không fit. Bảo quyết định giữ/bỏ/cách nhóm cho v2. |
| V2-14 | VN nội địa: baseline/week2 swap và reader | Week1v3 + week2-time-v2 và2single-HTML3language readers đã offline adopted trên main. Ghi Aplus scope đúng; tránh package trỏ trial/WONIK hoặc banner VN rebuild cũ. |
| V2-15 | OSAT FDI: selected journeys/candidates và render limits | B6–B12:7batch/70PNGfinal đã main; B1–B5/pilots có receipt riêng. OSAT generation closed. Không đếm70 là toàn bộ inventory OSAT hoặc nâng offline adoption thành whole technical PASS. |
| V2-16 | Fabless FDI: source candidates, final acceptance và batch còn thiếu | B13v5 checkpoint11selected; B14 corrective/review; B15–B21 chưa closed tại baseline. Cập nhật theo source receipt mới, không copy failed/history vào package final. |
| V2-17 | Partner FDI: supplier anchor, selected case và batch còn thiếu | B22 checkpoint10selected/root scoped PASS, creative-main chưa adopted; B23/B24 generated candidates chưa postgen closed; B25–B30 chưa chạy tại baseline. Không gán SI persona historical làm current. |
| V2-18 | FDI destination redesign và revision sẽ dùng trong package |10concrete4-toggle readers approved offline checkpoint `5b99984` còn source-only; main hiện revision trước. Bảo chọn/adopt revision rõ; reader B8+/Fabless/Partner mapping còn cần intake riêng. Không coi25conditional coverage rows là25HTML phải làm. |
| V2-19 | Journey entry/CTA/source/return mapping | Đúng audience/persona/proof/reader; incoming lang và original return context. Ghi khác biệt offline demo, reader route và production LDP; tránh ghép vì chung ngôn ngữ. |
| V2-20 | Cách xem demo và danh mục thư viện final | Điểm vào/preview/thumbnail/copy/caption/native headline/alt/source/prompts nếu cần cho operator. Chưa chọn sitemap, số trang hoặc clone library v1; chỉ finals được chọn với nguồn/revision rõ. |
| V2-21 | Evidence/acceptance/limitation của artifact | PO offline approval, technical render, root self-review, native-market/independence và live readiness tách riêng. Frozen harness không freeze adapter hoặc auto-accept mọi output. |

## Ngân sách, measurement và quản lý

| ID | Nội dung/việc cần ghi vào package | Căn cứ hiện có và phần để Bảo đổi |
|---|---|---|
| V2-22 | Budget envelope, phần giữ lại, giải ngân và tổng chi phí | Media cap11,7triệu hiện hành;5,6+≤5,6+Search≤0,5 là tham chiếu cũ có scope, không allocation v2 được chọn.6,1giữ lại nằm trong tổng. Phân bổ, daily, thời lượng, thuế/phí chờ Bảo. |
| V2-23 | Forecast/assumptions và ý nghĩa sample/data sufficiency | Dựa fresh filtered reach/currency/objective/evidence, không estimate generic hoặc780cũ; không suy14ngày là learning đủ. Chưa đặt thresholds/forecast mới. |
| V2-24 | KPI, baseline và nguồn đọc measurement | Account/role distribution, reach/frequency/CTR/engagement, brand signals, LDP interaction, verified leads nếu scope cần; Bảo chọn KPI/định nghĩa ưu tiên v2. Không bịa baseline hoặc chỉ tính raw form. |
| V2-25 | Tracking/destination readiness và scope đã QA | Existing3route LDP/tracking có scoped prior acceptance; destination reader/campaign mapping mới là scope riêng. Không ghi tất cả tracking chưa làm, cũng không coi prior QA là PASS cho route mới. |
| V2-26 | Quy tắc đánh giá/đi tiếp/dừng/swap/reallocation | V1 có management decisions và observation windows. V2 liệt kê chủ đề để Bảo đổi; chưa tạo decision engine, automation, thresholds hoặc cadence mới. |
| V2-27 | Workbook/sổ theo dõi chi tiêu và hiệu quả | Các trường cần rà: planned/actual/remaining, per-channel delivery metrics, audience/account register, keyword/exclusions nếu Search, KPI definitions, qualified vs raw leads. Chưa sửa XLSX/sheet/formula hoặc giữ nguyên logic v1 làm requirement. |
| V2-28 | Roles/decision rights, nhật ký thay đổi và việc còn pending | Bảo PO, người thực thi/reviewer, approval/version/date, owner của các open items. Chưa phân công, dựng workflow hoặc lịch thực hiện. |

## Những phần của package v1 cần Bảo quyết định giữ/bỏ/đổi

| ID | Thành phần cần rà cho v2 | Ghi chú |
|---|---|---|
| V2-29 | Ba report cũ: quản lý/triển khai; ngân sách/quyết định; bộ câu hỏi thống nhất | Ba file MD/HTML là nguồn tham khảo, không phải outline v2 đã chốt. Nội dung cũ chứa processing/creative snapshots cần refresh nếu reuse. |
| V2-30 | Bộ câu hỏi/decision-config/receipt và block pilot do Bảo viết | V1 có22propositions và version-bound acknowledgement. Không mặc định giữ22ID, nhóm/owner, câu chữ, checkbox hoặc logic khi Bảo đổi nhiều; không carry-forward câu trả lời/approval cũ sang v2. |
| V2-31 | Home/navigation, bảng tiến độ, demo selection và report exports | Chưa chọn bố cục, format xuất, số màn hình hay design system package mới. HTML/PDF/Word/slide chỉ là các định dạng có thể cần xác định sau. |
| V2-32 | Folder delivery, source provenance, offline portability và chất lượng file | Ưu tiên thư mục thường theo Bảo; không ZIP làm mặc định. Danh sách cần có link/assets/font/locale/readability/copy/reader/measurement scope checks khi triển khai; chưa có implementation/QA plan. |
| V2-33 | Dữ liệu nào được chia sẻ trong package và phần operator-only | Chỉ sanitized summaries/proof có scope; raw company/account/lead/credential/private URLs không đưa vào public package. Danh sách trạng thái Git local/main/source-only là operator context nếu Bảo cần; không mặc định đưa kỹ thuật vào report người đọc. |
| V2-34 | Change register v1 → v2 và danh sách ý kiến mới của Bảo | Ghi giữ/bỏ/đổi/bổ sung cho các ID trên khi Bảo steering. Chưa có đề xuất redesign, tradeoff chọn sẵn hoặc yêu cầu điền form. |

## Phần hiện chưa có quyết định v2

Mục đích/người đọc, cấu trúc package, cách kể chuyện, report/question topology, demo selection, workbook/decision logic, budget split, timeline, KPI/threshold/cadence và format xuất đều để Bảo thay đổi. Các decision hiện hành ở main chỉ là baseline có căn cứ, không bị tự hủy và cũng không biến thành cấu trúc v2 bắt buộc.

Kết quả rà: danh sách34mục để trao đổi; không có phase, ưu tiên, deadline, dự toán công sức, execution sequence hoặc task activation. Commit đầu giữ worktree/danh sách/nguồn; main không đổi.
