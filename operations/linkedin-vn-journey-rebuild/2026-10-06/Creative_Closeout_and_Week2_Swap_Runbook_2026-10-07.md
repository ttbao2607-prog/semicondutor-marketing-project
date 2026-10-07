# VN creative closeout và hướng dẫn swap tuần 2

Ngày 2026-10-07 · Owner quyết định: Bảo · Trạng thái: **CREATIVE_CLOSED / OFFLINE_ADOPTED**. Đây là hướng dẫn chuẩn bị quyết định; không phải lệnh kích hoạt ad, thay audience, chi tiền hoặc publish LadiPage.

Creative VN đã hoàn tất và được Bảo duyệt: week1 v3 và week2-time-v2, mỗi bộ 1 Cold + 5 RMK + 4 evidence; hai trang case có UI Leonxinx, nội dung value và toggle VI / English / 简体中文 trong một HTML mỗi week. Main đã nhận hai reader tại commit `c869982`. Ngôn ngữ bổ sung là bản dịch cùng journey VN, không phải adaptation FDI. Adapter English/Chinese vẫn DEVELOPING / NOT_FROZEN.

## Bộ dùng hiện hành

| Bộ | Vai trò | Artifact canonical |
|---|---|---|
| Week1 v3 | Authority ngành → cơ chế chuẩn bị quản trị → case Aplus | [Demo](../../../deliverables/linkedin-vn-journey/2026-10-06-v3/index.html), [reader](../../../deliverables/linkedin-vn-journey/2026-10-06-v3/case-aplus.html) |
| Week2-time-v2 | Hook Cold khác week1 → phạm vi/data/ERP cùng hiện trường → proof thời gian Aplus | [Demo](../../../deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2/index.html), [reader](../../../deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2/case-aplus.html) |

Hai bộ đều dùng Aplus Semiconductor tại Trung Quốc. Proof **toàn dự án tích hợp iMES + TOP GP go-live trong 3 tháng** là kết quả riêng của case; không phải thời gian từ buổi tư vấn đầu tiên đến qua audit, không cam kết triển khai theo deadline của Quý Doanh Nghiệp và không quy mọi cơ chế cho ERP riêng lẻ. Hình là minh họa. WONIK/EasyFlow.NET và các plan warm đầu tiên là lịch sử thử nghiệm, không phải bộ swap hiện hành.

Thông tin nguồn/acceptance: [week1](journey-v3/Main_V3_Integration_2026-10-06.json), [week2](week2-main-integration/README.md), [hai reader](ldp-value-main-integration/README.md). Bản copy và native image nằm cùng demo; operator chọn đúng bộ và đối chiếu inventory actual ad trước khi tác động tài khoản. Storyboard carousel không chứng minh format đủ điều kiện tạo audience RMK, cũng không đảm bảo người xem đọc tuần tự.

## Review theo package, không swap tự động

Giữ mốc ngày 3 kiểm vận hành, ngày 7 review ban đầu, ngày 14 tổng hợp. Ngày 8 là thời điểm có thể swap sau quyết định của Bảo; thiếu mẫu thì tiếp tục ghi **UNDETERMINED**, không mặc định tuần1 fail. Không dùng tỷ lệ dự đoán cũ hoặc lead thô để tự đặt ngưỡng thất bại cho awareness.

Giữ trần media **11,7 triệu**. Dự phòng tuần2 nằm trong đợt đầu **5,6 triệu**; không tự giải ngân **6,1 triệu** giữ lại hoặc tăng daily budget. Lịch trên là cửa sổ review, không chứng minh đủ learning hay warm audience.

Trước quyết định, ghi kỳ đo, raw counts và mẫu số, spend, impressions/reach/frequency đúng scope, clicks và CTR/engagement đúng definition, phân phối vào công ty/chức năng/cấp bậc, tình trạng đo lường. Baseline và criteria cần được Bảo chốt theo dữ liệu thực; hiện tài liệu này không tạo ngưỡng số mới.

## Quyết định theo chặng

| Evidence đã xác minh | Hướng xử lý cần Bảo quyết định | Bộ thay thế |
|---|---|---|
| Lỗi approval/delivery/targeting/measurement | Đóng lỗi vận hành trước; thay creative không thay thế điều tra nguyên nhân | Giữ dự phòng offline |
| Delivery đúng tệp, measurement hợp lệ, mẫu đủ theo criteria đã chốt; Cold week1 yếu | Có thể thay Cold, giữ warm week1 khi continuity phù hợp | Cold week2; phải đối chiếu lại source IDs/rule nếu đang gom audience từ ad |
| Cold có tín hiệu, nhưng warm cho thấy cần lời giải cụ thể về phạm vi và thời gian | Có thể giữ Cold đang có tín hiệu, chuyển RMK + evidence như một cặp | 5 RMK + 4 evidence của week2 Aplus; dùng reader week2 |
| Có evidence cần đổi cả hướng message và Bảo duyệt thay toàn bộ | Swap full pipeline, ghi rõ đây là thay nhiều yếu tố | Toàn bộ 10 ảnh/copy week2-time-v2 và reader week2 |
| Thiếu baseline/mẫu/coverage hoặc chưa đủ warm eligibility | Không kết luận fail/winner; không tự mở RMK | UNDETERMINED; dự phòng vẫn offline |

Giữ audience/objective/bid/placement/budget khi chỉ quyết định thay creative; mọi thay đổi khác cần scope riêng. So sánh hai tuần là iteration theo thời gian, không tự nhận causal lift hoặc A/B winner. Nếu giữ Cold week1 và đổi warm week2, kiểm caption giới thiệu Aplus trước proof, destination đúng reader và case scope không bị đứt.

RMK chỉ vận hành sau khi owner closeout LinkedIn chung xác minh actual source ads/format, audience IDs, rule/lookback, trạng thái đủ điều kiện và quy mô sử dụng tại tài khoản. Không giả pool Page/website thay pool ad; không giả Cold mới tự thuộc rule cũ. Bảo duyệt artwork không đồng nghĩa đã có operational release.

## Log quyết định — để trống đến khi có evidence live

| Trường cần ghi | Giá trị hiện tại |
|---|---|
| Kỳ đo / raw counts / baseline / coverage | Chưa có trong slice creative này |
| Chặng yếu và evidence | Chưa xác minh live |
| Ad nguồn / replacement asset IDs / nội dung giữ hoặc đổi | Điền từ inventory thực khi đề xuất swap |
| Audience IDs / rules / readiness / format eligibility | Owner closeout LinkedIn chung xác minh |
| Spend thực / ngân sách đợt đầu còn lại | Chưa xác minh live |
| Quyết định Bảo / operator / thời điểm / follow-up | Chưa có quyết định swap thật |

## Việc bàn giao còn mở ngoài slice creative

1. **LDP runtime**: hai HTML chạy local; chưa xác minh route import/upload, inline script/toggle, giao diện, source/back/contact sau khi triển khai. Contact hiện vẫn là trang yêu cầu tư vấn Digiwin Việt Nam; không có test submit/lead delivery trong slice này.
2. **LinkedIn live**: audience RMK/format eligibility, inventory ad, measurement và criteria review thuộc closeout vận hành chung; không ghi đã đóng từ artwork.
3. **Remote backup**: main adoption là local; không suy commit = push hoặc origin/main = GitHub thực. Push chỉ theo mandate riêng.

Các limitation category/source nhỏ trên mobile và hình minh họa giữ trong receipt của bộ được duyệt; không chuyển thành task gent mới hoặc technical/live PASS. Frozen core/budget/FDI artifact không đổi.

Docs impact reviewed: tài liệu này là current swap handoff Aplus; plan WONIK và receipt cũ giữ lịch sử, không rewrite acceptance hồi tố. Root SELF_REVIEW đối chiếu artifact/selection/anchor/package hiện có, không independent audit. Source planning/evidence được checkpoint trên nhánh lưu trữ trước khi bỏ worktree; giữ branch để khôi phục.
