# P3 — Baseline trước chạy

Revision 1 · extracted 29/10/2026, trước actual first delivery (lịch 01/11) · COMPLETE_WITH_GAPS. Authority: mandate đọc live P1–P3 của Bảo. Đọc từ GA4 (chỉ đọc), không có export. Baseline này là **context site/reader**, không chứng minh causal lift của F1/F2 và không phải KPI. Số trong [BASELINE.csv](BASELINE.csv). Root tự review; independent audit NOT_RUN.

## Kỳ đo và nguồn

- **Matched reference window:** 22/10 – 28/10/2026 (7 ngày đầy đủ, cùng độ dài W1); cutoff 28/10 vì dữ liệu GA4 mới nhất đọc được vào 29/10 là hết 28/10. Window này không trộn kỳ khác. Cửa sổ dài hơn 01–28/10 chỉ dùng làm tham chiếu.
- **Nguồn:** GA4 property “Digiwin Organic Website (SEO)” (stream `www.digiwin.com.vn`, chứa cả trang reader). Timezone/currency theo property (hiển thị ₫; không dùng cho spend). Trạng thái dữ liệu: đã xử lý trong báo cáo chuẩn; số của 28/10 có thể còn đổi nhẹ.
- Retrieval trước delivery nên nhãn là PREFLIGHT (không phải RETROSPECTIVE). Nếu muốn khoá sát hơn, đọc lại ngày 31/10 cho 25–31/10; chưa làm.

## Số đọc được (22–28/10/2026)

| Chỉ số | Giá trị | Ghi chú |
|---|---|---|
| Sessions (cả property) | 1,382 | engaged sessions 865, engagement rate 62.59%, avg engagement time 28s/session |
| Kênh: Direct | 590 | 42.69% |
| Kênh: Paid Social | 325 | **không phải F1/F2**; chủ yếu campaign `blogspot_pilot_*` (01–28/10: `blogspot_pilot_rmk` 257 sessions, `blogspot_pilot_awareness` 153) |
| Kênh: Organic Search | 318 | |
| Kênh: Unassigned / Referral / Organic Social / Email | 68 / 40 / 20 / 13 | còn kênh khác bị cắt khi đọc |
| Reader `/semiconductor-case-reader` | 6 views, 1 active user, avg engagement 14m 58s, 15 events, 4 key events | một user duy nhất; hầu chắc là QA/thử nghiệm nội bộ — xem contamination |
| Session campaign `fdi_*` (F1/F2) | 0 sessions (01–28/10) | EXPECTED_NO_PAID_DATA; chưa delivery, không là “0 đã đo” cho kết quả |

Tham chiếu 01–28/10: page views 7,118, active users 3,727 (báo cáo Pages and screens); sessions 4,406 (Traffic acquisition); 24 giá trị session campaign.

## Chưa thu thập / UNKNOWN

| Mục | Trạng thái | Lý do |
|---|---|---|
| Brand search (Search Console) | NOT_COLLECTED | chưa đọc nguồn; chưa có chỉ dẫn quyền |
| Follower/Page analytics LinkedIn | NOT_COLLECTED | chưa đọc lượt này |
| Direct traffic đúng scope reader | UNKNOWN | “Direct” là toàn property, không riêng trang reader |
| Baseline paid F1/F2 | NONE | chưa phát sinh; không gán 0 |

## Contamination

- **Test nội bộ:** reader có 6 views từ một user trong chính window baseline; chưa tách được là QA hay người thật → coi là có contamination, **không dùng làm baseline hành vi reader thật**.
- **Paid Social khác:** pilot `blogspot_pilot_*` làm số Paid Social tăng, không liên quan F1/F2; khi readback phải lọc theo campaign, không theo channel group.
- Property là website tổng; traffic organic/direct đến từ nhiều trang. Không lấy organic làm paid.

## Giới hạn

Không đòi mua công cụ hay sửa tracking để điền đủ. Số nhập tay từ bảng GA4 hiển thị, không từ export. Một số dòng channel group bị cắt khi đọc (chỉ lấy 7 kênh đầu). Baseline brand/site rộng chỉ là context.

Docs impact reviewed: no canonical update required.
