# P7b — Criteria decision sheet (chọn trước khi đọc kết quả)

Revision 1 · 29/10/2026 · ALL_NUMERIC_CRITERIA_UNSET. Authority: Bảo giao P4–P7. Không có baseline hiệu suất, sample minimum hay ngưỡng CTR/frequency/CPM đã được duyệt ([METRICS](../METRICS.md)). Tài liệu này chỉ **đề xuất phương án kèm lý do** để Bảo chọn *trước* khi đọc số W1/W2, tránh chọn ngưỡng sau khi thấy số để hợp thức hóa winner. Đề xuất không là KPI đã duyệt và không phải industry benchmark. Root tự review; independent audit NOT_RUN.

Lỗi kỹ thuật thật (URL/locale/claim sai, targeting drift, measurement lỗi, vượt cap) **không cần ngưỡng số** để báo hoặc giữ tiền ([INCIDENT_CARDS](INCIDENT_CARDS.md)).

## Dữ kiện đầu vào cho việc chọn

- Audience cold 470+; forecast native 30 ngày: spend $0–14, reach 71–170, frequency 1,0–1,4 (P1, định hướng); W1 danh nghĩa USD70.
- Baseline reader/site: chỉ là context và bị nhiễm ([BASELINE](BASELINE.md)); không có baseline paid F1/F2.
- Hai ad dùng chung ngân sách/thuật toán, không đảm bảo equal rotation hay A/B.

## Bảng quyết định

| ID | Tiêu chí | Hiện tại | Phương án đề xuất | Lý do / nguồn | Bảo chọn |
|---|---|---|---|---|---|
| K1 | Số ngày eligible-delivery tối thiểu để đọc | UNSET | 3 ngày để cảnh báo, 7 ngày để kết luận | checkpoint đề xuất của data plan (ngày delivery 3/7) | NOT_DECIDED |
| K2 | Tối thiểu mẫu mỗi ad để so hook | UNSET | một trong: 25 / 50 / 100 clicks mỗi ad | với đếm click kiểu Poisson, sai số tương đối xấp xỉ 1/√n: 25 click ≈ 20%, 50 ≈ 14%, 100 ≈ 10%. Càng ít click càng chỉ nên coi là tín hiệu định hướng | NOT_DECIDED |
| K3 | Định nghĩa click dùng để so | UNSET | một loại duy nhất, ghi tên cột và khóa trước | “Clicks” vs landing page clicks chưa xác minh trong UI ([REPORT_ACCESS_MAP](REPORT_ACCESS_MAP.md)); đổi definition giữa kỳ làm so sánh vô nghĩa | NOT_DECIDED |
| K4 | Exposure imbalance giữa F1/F2 | UNSET | nếu impressions hai ad lệch quá một tỷ lệ Bảo chọn thì không so CTR | hai ad chia chung ngân sách; một ad ít phân phối không nên bị gọi là thua | tỷ lệ NOT_DECIDED |
| K5 | CTR | UNSET | không đặt target CTR tuyệt đối; chỉ so F1 vs F2 cùng kỳ khi qua K2/K4 | không có baseline paid nội bộ; không dùng benchmark ngoài như KPI | NOT_DECIDED |
| K6 | Reader engagement | UNSET | đọc processed sessions/engaged sessions theo `utm_content`; không đòi tỷ lệ cố định | HTTP 204 và clicks không bằng sessions; nguồn GA4 trễ và nhiễm QA | NOT_DECIDED |
| K7 | Pacing/under-delivery | UNSET | cảnh báo khi delivered thấp rõ so pacing, rồi đưa C3 cho Bảo; không tự tăng budget/nới audience | forecast native báo spend 30 ngày $0–14 so với danh nghĩa USD70/tuần | ngưỡng NOT_DECIDED |
| K8 | Frequency warning | UNSET | cảnh báo khi frequency tăng bất thường so forecast 1,0–1,4 | audience nhỏ, dễ lặp | ngưỡng NOT_DECIDED |
| K9 | CPM/CPC ceiling | UNSET | không đặt ceiling; chỉ ghi giá trị thực | chưa có cơ sở nội bộ; không bịa FX (VND chỉ theo accounting basis) | NOT_DECIDED |
| K10 | Demographic coverage | UNSET | báo counts + phần unknown/suppressed; không dựng % “đúng tệp” nếu thiếu mẫu số | metric rule; report có thể ẩn dữ liệu nhỏ | NOT_DECIDED |
| K11 | Khi mẫu nhỏ | — | ghi INCONCLUSIVE (C7), card A/B | không kết luận fail từ thiếu lead; không kéo dài W1 tự động | mặc định đề xuất |
| K12 | Trộn kỳ / causal | — | so equal-length windows; không gán causal lift từ hai tuần khác thời điểm | METRICS | mặc định đề xuất |

## Cách dùng

Bảo điền cột “Bảo chọn” (kèm ngày) **trước** phép thử/lần đọc áp dụng. Giá trị chọn sau khi đã thấy số phải gắn nhãn RETROSPECTIVE và không dùng để tuyên bố winner. Nếu chưa chọn, báo số thô/limitations và C7.

Docs impact reviewed: no canonical update required.
