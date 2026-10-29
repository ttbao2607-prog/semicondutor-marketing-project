# Q3 — Khả năng RMK thật trong UI và cấu hình để Bảo chọn

Revision 1 · observed 29/10/2026, kết thúc 12:26 +07 · **PARTIAL**. Authority: Bảo giao Claude thực hiện [contract](CLAUDE_EXECUTION_CONTRACT.md). Chỉ đọc. **Không tạo audience, không bật RMK, không dựng ad.** Audit độc lập NOT_RUN. Cập nhật [P6](RMK_DECISION_PACK.md) bằng evidence UI thật; P6 không bị sửa.

## Đã làm và side effect

Vào Campaign Manager → Audiences → Create audience → Retargeting audience → chọn nguồn "Single image" → Next, đọc form, rồi **Cancel**. Danh sách Matched Audiences trước và sau đều đúng **5 audience** (tất cả Company List). Có một lần bước đầu bị chuyển nhầm sang "Create video audience" (radio Single image chưa ghi nhận); bước đó có nút "Agree and create", tôi bấm **Cancel** ngay, không tạo gì. Lần thứ hai chọn đúng Single image. Không bấm "Agree and create" ở bất kỳ form nào.

## Quan sát thực (form "Create single image audience")

| Mục | Giá trị thực thấy |
|---|---|
| Các loại audience trong menu Create | Predictive, Matched, Retargeting (Retargeting: dựa trên engagement trước đó với Company Page, website, paid/organic content) |
| Nguồn retargeting member engagement | Company page, Conversation, Conversions API, Document, Event, Lead gen form, **Single image**, Video, Website; Company engagement: Organic & paid signals (New) |
| Rule ("How did they engage?") | **"Any interactions with your ad"** và **"People who performed chargeable clicks on your ad"** — cả hai có thật trong UI |
| Lookback ("When did they engage?") | 7, 14, 28, **30**, 60, 90, 180, 365 ngày trong quá khứ |
| Cách chọn nguồn | **theo ad set**, không theo từng ad: bảng "Which single image ad sets…" liệt kê 4 ad set Single Image (F1/F2 ad set — Not delivering/Scheduled; ba ad set Draft). Không có lựa chọn riêng `LI-wave01-F1…` hay `…F2…` |
| Tên audience | ô bắt buộc, giới hạn 200 ký tự |
| Mô tả xử lý | "It can take 48 hours (on a rare occasion, longer) for your audience to process and deliver. An ad set will start serving once the audience has processed." |
| Backfill, ngưỡng tối thiểu (gate 300), reachable | **không hiển thị** trong form |
| Hiện trạng | Matched Audiences chỉ có 5 Company List; **không có retargeting audience nào** (đọc 29/10). Tab "Saved" không đọc |

## Hệ quả cho P6 (so với đề xuất đã viết)

- **R1:** hai rule đều native-supported; mặc định **A (Any interactions)** có thật. Mức chênh pool giữa A và B chưa đo.
- **R2:** mốc 30 ngày có sẵn; hợp với mặc định. Lookback chưa là ràng buộc trong W1 (7 ngày) — như P6.
- **R3 đổi bản chất:** vì nguồn chọn theo **ad set**, F1 và F2 hiện cùng một ad set, nên pool native **tự động là một pool chung** của cả hai ad. Muốn mỗi ad một pool phải tách ad set (thay cấu trúc cold đang scheduled) — đó là quyết định cấu hình ngoài gói này, không đề xuất tự làm. Hệ quả giữ continuity A7: người click F1 có thể thấy carousel F2 và ngược lại; không hứa delivery tuần tự.
- **R4:** objective không nằm trong form tạo audience; vẫn quyết ở S4.
- **R5, R6:** không đổi. Form tạo audience mở được cả khi ad set mới "Not delivering/Scheduled" (ad set được liệt kê, selectability chưa thử bấm vì sẽ tiến tới tạo). **Chưa biết** nền tảng chỉ tích lũy từ lúc tạo hay backfill → R6 vẫn là rủi ro bị động; chưa có evidence để quyết ngoài mandate của Bảo.

## Lựa chọn Bảo chọn (đề xuất mặc định + phương án)

| # | Mặc định đề xuất | Phương án khác | Trade-off |
|---|---|---|---|
| R1 | A — Any interactions | B — Chargeable clicks | A rộng nhất, trộn tín hiệu yếu; B hẹp hơn, nhưng có thể dưới cổng; chưa đo mức chênh |
| R2 | 30 ngày | 7/14/28/60/90/180/365 | W1 chỉ 7 ngày nên dài hơn chỉ thêm tín hiệu cũ; không có số liệu hỗ trợ đổi |
| R3 | **Một pool theo ad set (đã là hiện trạng native)** | tách ad set cho F1/F2 | tách làm mỗi pool nhỏ hơn và đổi cấu trúc cold đang scheduled; không tự thực hiện |
| R6 | cấp/không cấp **mandate hẹp** tạo source audience trước 01/11 | tạo sau day 3 / sau W1 | nếu chỉ tích lũy từ lúc tạo thì tạo muộn mất tương tác W1; chưa biết có backfill hay không |

## Giữ nguyên

Source `NOT_VERIFIED_CREATED` (quan sát bổ sung: không có retargeting audience trong danh sách Matched; Saved tab chưa đọc), reachable `UNKNOWN`, rule/lookback `NOT_SELECTED`. Không suy pool từ 470+ hoặc forecast 30 ngày; không hứa backfill; không mượn Page/organic/campaign khác. **Gate 300 chưa xác minh trong UI hiện hành** (form không nêu): giữ là contract của repo, không hạ ngưỡng. Chỉ gán Ready/S2 sau actual native readback. Chọn source/timing không đồng nghĩa enable RMK; objective/release/nguồn tiền là quyết định sau.

## UNVERIFIED còn mở

Gate 300 trong UI; reachable sau lọc; backfill; hiển thị đúng ad F1/F2 trong thống kê ad set; tương thích tạo carousel RMK với nguồn Single image (chỉ thấy nguồn, chưa dựng ad).

## Cập nhật sau Q3 (29/10, Bảo cấp mandate)

Bảo chọn R1=Any interactions, R2=30 ngày, R3=pool chung theo ad set, R6=tạo ngay, và đã cho Claude tạo audience. Đã tạo `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D` (Building); xem [receipt](RMK_SOURCE_AUDIENCE_CREATED.md). Các dòng "Hiện trạng", "Giữ nguyên" và "không có retargeting audience" ở trên mô tả thời điểm đọc Q3 (12:xx), nay được receipt thay thế cho phần source; gate 300, reachable và backfill vẫn UNVERIFIED.

Docs impact reviewed: xem [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md).
