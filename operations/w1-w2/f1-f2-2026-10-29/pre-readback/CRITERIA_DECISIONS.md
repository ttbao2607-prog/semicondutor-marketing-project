# P7b — Criteria decision sheet (chọn trước khi đọc kết quả)

Revision 2 · 02/11/2026 · K2/K3/K4/K7/K8 do Bảo chọn (K7/K8 chỉ cảnh báo); các tiêu chí còn lại UNSET/NOT_DECIDED (Revision 1 · 29/10/2026 · ALL_NUMERIC_CRITERIA_UNSET). Authority: Bảo giao P4–P7. Không có baseline hiệu suất, sample minimum hay ngưỡng CTR/frequency/CPM đã được duyệt ([METRICS](../METRICS.md)). Tài liệu này chỉ **đề xuất phương án kèm lý do** để Bảo chọn *trước* khi đọc số W1/W2, tránh chọn ngưỡng sau khi thấy số để hợp thức hóa winner. Đề xuất không là KPI đã duyệt và không phải industry benchmark. Root tự review; independent audit NOT_RUN.

Lỗi kỹ thuật thật (URL/locale/claim sai, targeting drift, measurement lỗi, vượt cap) **không cần ngưỡng số** để báo hoặc giữ tiền ([INCIDENT_CARDS](INCIDENT_CARDS.md)).

## Dữ kiện đầu vào cho việc chọn

- Audience cold 470+; forecast native 30 ngày: spend $0–14, reach 71–170, frequency 1,0–1,4 (P1, định hướng); W1 danh nghĩa USD70.
- Baseline reader/site: chỉ là context và bị nhiễm ([BASELINE](BASELINE.md)); không có baseline paid F1/F2.
- Hai ad dùng chung ngân sách/thuật toán, không đảm bảo equal rotation hay A/B.

## Bảng quyết định

| ID | Tiêu chí | Hiện tại | Phương án đề xuất | Lý do / nguồn | Bảo chọn |
|---|---|---|---|---|---|
| K1 | Checkpoint quan sát | Đề xuất ngày delivery3/7 | đọc/report ở checkpoint, không gán đủ mẫu theo số ngày | Data plan quy định cadence; thời gian không chứng minh đủ evidence để kết luận | NOT_DECIDED |
| K2 | Evidence để so hook | UNSET | báo clicks và impressions của từng ad, định nghĩa click, period, exposure imbalance và độ bất định; ghi mức chênh cần nhận diện trước test nếu muốn thiết kế phép so | Riêng25/50/100clicks không định nghĩa mẫu đủ cho CTR; chưa có assumptions/effect size/interval nên bỏ các lựa chọn đó, không thay bằng số mới | **CHỌN 02/11/2026 (Bảo):** không đặt ngưỡng số; chỉ báo clicks và impressions từng ad kèm định nghĩa click, kỳ, exposure imbalance và hạn chế. Chưa đủ cơ sở thì chỉ mô tả |
| K3 | Định nghĩa click dùng để so | UNSET | một loại duy nhất, ghi tên cột và khóa trước | “Clicks” vs landing page clicks chưa xác minh trong UI ([REPORT_ACCESS_MAP](REPORT_ACCESS_MAP.md)); đổi definition giữa kỳ làm so sánh vô nghĩa | **CHỌN 02/11/2026 (Bảo):** cột **Clicks** đang hiển thị trong Campaign Manager (đếm mọi lượt bấm, không phải landing page clicks); khóa một định nghĩa này cho cả F1/F2 và các kỳ so sánh, không đổi giữa kỳ. Reader sessions đọc riêng qua K6, không quy đổi click thành lead |
| K4 | Exposure imbalance giữa F1/F2 | UNSET | nếu impressions hai ad lệch quá một tỷ lệ Bảo chọn thì không so CTR | hai ad chia chung ngân sách; một ad ít phân phối không nên bị gọi là thua | **CHỌN 02/11/2026 (Bảo):** tỷ lệ **3:1**. Nếu impressions của ad nhiều hơn lớn hơn 3 lần ad còn lại trong cùng kỳ thì không so CTR F1 vs F2. Ngưỡng do Bảo chọn, không có cơ sở dữ liệu hay benchmark; chỉ có giá trị khi chọn trước khi đọc |
| K5 | CTR | UNSET | không đặt target CTR tuyệt đối; mô tả F1 vs F2 cùng kỳ kèm K2/K4 và limitations, không gọi causal winner từ shared-budget delivery | không có baseline paid nội bộ; không dùng benchmark ngoài như KPI | NOT_DECIDED |
| K6 | Reader engagement | UNSET | đọc processed sessions/engaged sessions theo `utm_content`; không đòi tỷ lệ cố định | HTTP 204 và clicks không bằng sessions; nguồn GA4 trễ và nhiễm QA | NOT_DECIDED |
| K7 | Pacing/under-delivery | UNSET | cảnh báo khi delivered thấp rõ so pacing, rồi đưa C3 cho Bảo; không tự tăng budget/nới audience | so actual spend/eligible delivery với kế hoạch cùng kỳ; không dùng forecast30ngày làm expected7ngày | **CHỌN 02/11/2026 (Bảo), chỉ làm cảnh báo:** cảnh báo khi chi lũy kế tại checkpoint < **50%** của (USD10/ngày × số ngày ad đủ điều kiện chạy; ghi actual eligibility days) → chuyển C3 cho Bảo. Ngưỡng do Bảo chọn, không có baseline nội bộ; không dùng forecast 30 ngày làm kỳ vọng 7 ngày; không tự tăng budget/nới audience |
| K8 | Frequency warning | UNSET | đọc actual frequency theo cùng scope/kỳ; đề xuất warning dựa trên diễn biến exposure thực và criteria Bảo chọn | forecast1,0–1,4 không là baseline thực hoặc ngưỡng7ngày | **CHỌN 02/11/2026 (Bảo), chỉ làm cảnh báo:** cảnh báo khi frequency thực tế ≥ **2,0** trong cửa sổ 7 ngày; chỉ tính khi Reach native hiển thị > 0 (nếu tự tính ghi DERIVED). Không phải lệnh dừng; forecast 1,0–1,4 không là baseline. Ngưỡng do Bảo chọn, không có cơ sở dữ liệu nội bộ |
| K9 | CPM/CPC ceiling | UNSET | không đặt ceiling; chỉ ghi giá trị thực | chưa có cơ sở nội bộ; không bịa FX (VND chỉ theo accounting basis) | NOT_DECIDED |
| K10 | Demographic coverage | UNSET | báo counts + phần unknown/suppressed; không dựng % “đúng tệp” nếu thiếu mẫu số | metric rule; report có thể ẩn dữ liệu nhỏ | NOT_DECIDED |
| K11 | Khi mẫu nhỏ | — | ghi INCONCLUSIVE (C7), card A/B | không kết luận fail từ thiếu lead; không kéo dài W1 tự động | mặc định đề xuất |
| K12 | Trộn kỳ / causal | — | so equal-length windows; không gán causal lift từ hai tuần khác thời điểm | METRICS | mặc định đề xuất |

## Bảo đã chọn — 02/11/2026

Bảo đồng ý ba lựa chọn K2/K3/K4 (đề xuất của Claude, kèm giải thích tác động) trước checkpoint ngày 3 và trước khi đọc số tiếp theo. Chỉ đạo này chỉ ghi quy ước đọc số: không đổi ngân sách, lịch, targeting, creative hay trạng thái ad.

- K2: không đặt ngưỡng số; báo clicks + impressions từng ad với định nghĩa, kỳ, exposure imbalance và hạn chế.
- K3: cột Clicks đang hiển thị, khóa một định nghĩa.
- K4: không so CTR F1 vs F2 khi impressions lệch hơn 3:1 trong cùng kỳ.
- Đính chính K3: [Q2](FOLLOWUP_Q2_REPORT_MAP.md) ghi LinkedIn có thêm cột "Clicks to landing page"; ở bước chọn K3 ngày 02/11 điều này chưa được nêu (cột lý do K3 bên trên viết "chưa xác minh trong UI" là snapshot cũ). Lựa chọn của Bảo là cột **Clicks** đang hiển thị và giữ nguyên; muốn đổi sang "Clicks to landing page" cần Bảo quyết định lại trước khi đọc số kế tiếp, không đổi giữa kỳ. Có thể báo "Clicks to landing page" như số phụ có nhãn, không làm cơ sở so sánh.
- K7 (bổ sung 02/11/2026, chỉ cảnh báo): chi lũy kế < 50% của USD10 × ngày đủ điều kiện → C3 cho Bảo.
- K8 (bổ sung 02/11/2026, chỉ cảnh báo): frequency thực tế ≥ 2,0 trong 7 ngày, chỉ khi Reach > 0.
- K7/K8 chỉ tạo cảnh báo và decision pack cho Bảo; agent không được tự pause/enable, tăng budget hay nới audience. Không đổi trạng thái ad. Hôm nay Reach hiển thị UNAVAILABLE nên K8 chưa áp dụng được; chưa có dấu hiệu chạm K7 ở cấp ad set (F1 đứng yên không thuộc K7).
- Lưu ý khi chọn: cặp 38/9 impressions (≈4:1, đọc 02/11) đã nhìn thấy trước khi chọn. Với cả 2:1 và 3:1 cặp này đều không được so; số này **không** được dùng để tuyên bố winner/loser. Lần đọc đầu tiên áp dụng luật là checkpoint ngày 3.
- K1, K5, K6, K9, K10 vẫn NOT_DECIDED; K11/K12 giữ mặc định đề xuất. Reading hiện tại vẫn C7 INCONCLUSIVE. W2 funding vẫn NOT_DECIDED, hạn quyết 08/11 06:45 giờ VN (không quyết thì lịch kết thúc, card A).

## Cách dùng

Bảo điền cột “Bảo chọn” (kèm ngày) **trước** phép thử/lần đọc áp dụng. Giá trị chọn sau khi đã thấy số phải gắn nhãn RETROSPECTIVE và không dùng để tuyên bố winner. Nếu chưa chọn, báo số thô/limitations và C7.

Docs impact reviewed: current canonical pointers updated for P1–P7 execution/corrections. See [audit closeout](AUDIT_FIX_CLOSEOUT.md).
