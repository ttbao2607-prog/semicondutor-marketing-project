# P2 — Bản đồ đường lấy báo cáo W1

Revision 1 · observed 29/10/2026 · COMPLETE_WITH_GAPS. Authority: mandate đọc live P1–P3 của Bảo (chat 29/10/2026). Chỉ đọc/điều hướng báo cáo trong LinkedIn Campaign Manager và GA4; không sửa tag, GA4 config/dimension/stream, campaign, không export, không tạo integration. Bộ lọc chỉ nằm trong URL/phiên xem, không lưu thành report. Root tự review; independent audit NOT_RUN. Property/account/stream IDs và link phiên riêng giữ private.

## Kết quả ngắn

- **GA4:** đọc được. Property tên “Digiwin Organic Website (SEO)”, stream web `www.digiwin.com.vn`. Measurement ID của stream khớp ID trong [reader bridge](../../../../tracking/semiconductor-reader-bridge.js) của repo, và trang `/semiconductor-case-reader` có xuất hiện trong báo cáo Pages and screens. Property này cũng chứa traffic website tổng và các pilot khác, nên **luôn phải lọc theo campaign/trang**, không đọc tổng property.
- **Lọc theo campaign F1/F2:** báo cáo Traffic acquisition đổi sang chiều Session campaign được; lọc `fdi_` cho 01–28/10/2026 → không dòng nào = `EXPECTED_NO_PAID_DATA` (ads chưa delivery). Chứng minh đường lọc dùng được, không chứng minh đã attributed.
- **LinkedIn:** list ad/ad set có preset cột Performance, Delivery, Engagement, Conversions & leads, Top conversions, Video, Talent leads, cùng Customize columns; có nút Professional demographics và Export. Chưa mở demographics vì chưa có delivery.

## Bảng metric → nguồn

| Metric | Nguồn / report | Filter / cách lọc | Identity / join key | Definition cần ghi | Availability / lag | Cách đọc lại |
|---|---|---|---|---|---|---|
| Trạng thái, review, delivery | LinkedIn Campaign Manager → Ads/Ad sets | theo tên ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH`, hai ad `LI-wave01-F1/F2-en-COLD-v1` | tên + stable key; numeric ID private | nhãn On/Off và Status (Active, Not delivering – Scheduled…) | ngay; Active ≠ đã duyệt/đã delivery | mở lại list; ghi observed_at |
| Impressions, spend, CPM | LinkedIn list, preset Performance/Delivery | time range trùng window W1; chọn daily hoặc cumulative, không cộng lẫn | ad / ad set | currency USD, before-tax chưa xác minh | thường trong ngày; có thể chỉnh sau | cùng window, ghi extracted_at |
| Reach, frequency | LinkedIn, preset Delivery hoặc Customize columns (chưa mở để xác nhận cột có sẵn) | theo ad set; reach không cộng giữa hai ad | ad set | native hay DERIVED (impressions/reach) | cùng lag | xác nhận cột trước readback đầu |
| Clicks, CTR | LinkedIn, preset Performance | theo ad | ad | “Clicks” trong list Performance; phân biệt với landing page clicks/link clicks nếu có cột riêng — chưa xác minh trong UI | cùng lag | khoá definition trước khi so sánh kỳ |
| Demographics (company/function/seniority) | LinkedIn → Professional demographics | theo ad set/ad, đúng date range | ad set/ad | counts + unknown/suppressed; không dựng % đúng khi thiếu mẫu số | chỉ có sau delivery; có ngưỡng ẩn dữ liệu nhỏ | mở sau delivery; UNAVAILABLE nếu bị ẩn |
| Reader sessions/engagement | GA4 → Reports → Acquisition → Traffic acquisition, chiều Session campaign | search term `fdi_` hoặc tên campaign | utm_campaign `fdi_f1_en_cold_wave01`, `fdi_f2_en_cold_wave01`; utm_content `f1_cold_v1`, `f2_cold_v1` ([registry](../SOURCE_REGISTRY.csv)) | Sessions, Engaged sessions, Avg engagement time theo GA4 | báo cáo đã xử lý thường trễ; số ngày gần nhất có thể chưa đủ (dữ liệu mới nhất đọc được là 28/10 vào 29/10) | cùng window, ghi processed hay không |
| Reader page views | GA4 → Pages and screens | search `semiconductor-case-reader` | page path `/semiconductor-case-reader` | Views, Active users, Avg engagement time | như trên | như trên |
| Treatment F1 vs F2 | GA4 | **UNVERIFIED:** URL có `t=F1/F2&lang=en` nhưng chưa kiểm GA4 có hiển thị query/param `t` thành chiều lọc hay không | utm_content `f1_cold_v1` / `f2_cold_v1` là khoá dự kiến từ registry, đường lọc dimension chưa xác minh; Session campaign đã mở được nhưng chưa có paid rows | — | — | nếu không có chiều `t`, dùng utm_content/campaign để tách |

## Phân biệt cần giữ

- Link click hay all-click trên LinkedIn ≠ session GA4; không quy 1:1. HTTP 204 từ bridge không phải bằng chứng GA4 đã xử lý.
- Kênh “Paid Social” trong GA4 hiện chứa traffic của pilot khác (campaign `blogspot_pilot_*`); **không dùng channel group làm proxy F1/F2**, phải lọc theo campaign.
- Timezone/currency: GA4 và LinkedIn mỗi nơi có timezone riêng; timezone của tài khoản LinkedIn chưa đọc → UNVERIFIED. Ghi timezone từng nguồn khi readback.

## Trạng thái

| Nguồn | Trạng thái |
|---|---|
| LinkedIn status/delivery | READABLE |
| LinkedIn demographics | EXPECTED_NO_PAID_DATA (chưa có delivery); đường vào có |
| LinkedIn Reach/frequency/click-definition cột | UNVERIFIED (chưa mở Customize columns) |
| GA4 campaign `fdi_` | READABLE, 0 dòng (EXPECTED_NO_PAID_DATA) |
| GA4 reader page | READABLE |
| GA4 chiều `t` (treatment) | UNVERIFIED |
| Timezone LinkedIn | UNVERIFIED |

## Giới hạn

Chụp ảnh màn hình trong editor LinkedIn và trang GA4 bị treo nhiều lần; các giá trị đọc qua accessibility tree/DOM, báo cáo GA4 qua text của bảng. Không có export, nên số liệu chép tay từ bảng hiển thị; khi readback thật cần ghi extracted_at.

Docs impact reviewed: current canonical pointers updated for P1–P7 execution/corrections. See [audit closeout](AUDIT_FIX_CLOSEOUT.md). Không đổi tracking contract, tag hay audience/message.
