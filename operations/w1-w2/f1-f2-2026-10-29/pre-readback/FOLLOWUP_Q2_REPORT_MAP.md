# Q2 — Đóng đường đọc metric

Revision 1 · observed 29/10/2026, kết thúc 12:26 +07 · **PARTIAL**. Authority: Bảo giao Claude thực hiện [contract](CLAUDE_EXECUTION_CONTRACT.md). Chỉ đọc/điều hướng LinkedIn Campaign Manager và GA4. Không lưu preset cột, không đổi account/property setting, không export, không tạo custom dimension/tag. Audit độc lập NOT_RUN. Property/account/stream numeric ID private.

**Mức evidence:** DOM/text trang tại thời điểm đọc; không screenshot, không raw bundle riêng, số liệu chép tay từ text hiển thị. Cập nhật [P2](REPORT_ACCESS_MAP.md) bằng bản mới này, không sửa bản cũ.

## Bản đồ metric → nguồn (cập nhật)

| Metric | Report / filter | Join key | Definition cần ghi | Timezone / window / lag | Availability (quan sát 29/10) |
|---|---|---|---|---|---|
| Spend, impressions, clicks | LinkedIn Campaign Manager, danh sách Ads / Ad sets, cột Performance; chọn range trùng W1 | tên ad `LI-wave01-F1/F2-en-COLD-v1`, ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH` | "Clicks" là cột General performance; currency USD (ô budget) | timezone tài khoản **UNVERIFIED** (xem dưới) | cột có, giá trị 0 trong 30/09–29/10 (prelaunch) |
| **Reach, frequency** | cùng bảng, **Customize columns → General performance columns**: "Reach", "Average frequency", "Cost per 1,000 member accounts reached", "Audience penetration" | ad set (reach không cộng giữa hai ad) | native column; không tự tính trừ khi ghi DERIVED | như trên | **VERIFIED có sẵn** trong danh sách cột; chưa mở giá trị vì chưa delivery |
| **Loại click** | cùng bảng: "Clicks" (General performance), "Clicks to landing page", "Clicks to LinkedIn pages", "Clicks to member profile", "Total social actions", "Total engagement", "Engagement rate", "Average CTR", cùng nhóm Viral | ad / ad set | **Khóa readback:** dùng "Clicks to landing page" làm click vào reader; ghi riêng "Clicks" (tổng) và "Total engagement"; không đổi định nghĩa giữa kỳ. Định nghĩa chính xác của từng cột LinkedIn chưa đọc tooltip → ghi tên cột, không suy | — | **VERIFIED có** các cột này |
| Attribution | preset "Attribution model" (New) trong menu Columns | — | chưa mở; không đổi | — | tồn tại, không dùng |
| Demographics | nút "Professional demographics" trên danh sách | ad set | counts + unknown/suppressed | chỉ sau delivery | đường vào có; EXPECTED_NO_PAID_DATA |
| Reader sessions, engaged sessions, avg engagement time | GA4 → Reports → Acquisition → Traffic acquisition; dimension picker → Traffic source → **Session campaign**; search `fdi_` | utm_campaign `fdi_f1_en_cold_wave01` / `fdi_f2_en_cold_wave01` ([registry](../SOURCE_REGISTRY.csv)) | Sessions, Engaged sessions, Engagement rate, Average engagement time per session, Event count, Key events (cột có sẵn trong báo cáo) | property reporting time zone **Vietnam (GMT+07:00)**, currency VND (Admin → Property details); báo cáo đã xử lý, dữ liệu đọc được đến 28/10 | **VERIFIED:** đổi được sang Session campaign; tìm `fdi_` trong 01–28/10/2026 → "No data available" = `EXPECTED_NO_PAID_DATA` (chưa chứng minh attribution) |
| Reader page views | GA4 → Pages and screens, search `semiconductor-case-reader` | page path | Views, Active users | như trên | P2 đã đọc; lượt này không đọc lại |
| Treatment F1 vs F2, **utm_content** | **Không** nằm trong picker của báo cáo Traffic acquisition: nhóm Session-scoped chỉ có Session campaign, campaign ID, default channel group, medium, source, source/medium, source platform. Không có "Session manual ad content" | tách bằng utm_campaign (đã khác nhau F1/F2: `fdi_f1_…` / `fdi_f2_…`) | — | — | **utm_content chưa có đường lọc đã xác minh** trong báo cáo chuẩn; Explorations/custom dimension chưa thử → UNVERIFIED. Không cần dimension `t` nếu campaign đã tách F1/F2 |

## GA4 identity

- Property "Digiwin Organic Website (SEO)", account `鼎捷軟件(越南)`; stream web "My Website Organic SEO", URL `https://www.digiwin.com.vn`; Admin ghi "Receiving traffic in past 48 hours".
- **Measurement ID `G-MV5QWN0XVM` (đọc ở trang chi tiết stream) khớp với `MID` trong [tracking/semiconductor-reader-bridge.js](../../../../tracking/semiconductor-reader-bridge.js).** Đây là xác nhận đúng stream theo bridge; chưa chứng minh có session paid.
- Property chứa traffic tổng và pilot khác (Paid Social `blogspot_pilot_rmk`, `blogspot_pilot_awareness` thấy trong 01–28/10). **Không đọc tổng property và không dùng channel group Paid Social làm proxy F1/F2**; lọc campaign `fdi_`.

## LinkedIn timezone

Không đọc được. Hai đường dẫn cài đặt tài khoản thử (`/settings`, `/account-settings`) đều trả "The page you are looking for could not be found"; menu "Account settings" tồn tại trong thanh điều hướng nhưng không được mở thêm theo giới hạn vòng lặp. Timezone nguồn LinkedIn vẫn **UNVERIFIED**; readback phải ghi timezone bằng cách đọc nguồn trước, không giả định trùng GMT+07:00 của GA4.

## Đã thử và kết quả

1. LinkedIn danh sách ad set/ads: bật được cột, mở "Customize columns", đọc nhóm cột (General performance, Engagement, Conversions and leads, …), đóng bằng Dismiss (không lưu view).
2. GA4 Traffic acquisition: đổi dimension sang Session campaign, search `fdi_` → không dữ liệu.
3. GA4 Admin: Property details (time zone, currency) và Data streams (stream, Measurement ID) đọc được.
4. GA4 nhóm Session-scoped: không có Session manual ad content.

## Giới hạn

Trước delivery, EXPECTED_NO_PAID_DATA là hợp lệ nhưng không chứng minh paid attribution, không chứng minh `utm_content`/treatment tách được. Không đòi LinkedIn clicks = GA4 sessions; HTTP 204 từ bridge không phải bằng chứng GA4 đã xử lý. Thiếu report/processing chưa phải lỗi tracking. Thay đổi UI hiển thị (đổi dimension, search) chỉ nằm trong phiên xem, không lưu report. Tab GA4 mở bằng điều hướng đã đóng cuối phiên.

Docs impact reviewed: xem [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md).
