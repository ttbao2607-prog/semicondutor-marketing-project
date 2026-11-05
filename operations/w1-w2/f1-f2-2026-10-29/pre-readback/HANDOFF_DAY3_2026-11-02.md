# Handoff — F1/F2 checkpoint ngày 3 (≈03–04/11/2026)

02/11/2026 · revision 1 · **HANDOFF_ONLY / NOT_STARTED**. Authority: Bảo (chat 02/11/2026) yêu cầu commit checkpoint kèm handoff cho agent sau. Tài liệu này không phải mandate live: lần đọc dưới đây là read-only theo mandate đọc hiện hành của Bảo; không Save/Launch/pause/enable, không đổi budget, lịch, targeting, creative.

## Trạng thái bàn giao (observed 02/11/2026, Claude in Chrome, read-only)

- Ad set `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH`: On/Active; USD10/ngày; ngày 11/1–11/7 (UI chỉ hiện ngày); Feed only; Expansion/LAN/Right Rail tắt; Việt Nam, English, R5-52, 4 functions, CXO–Manager.
- Cửa sổ 04/10–02/11 (không phải riêng một ngày): USD10.40, 47 impressions, 0 Clicks. F2 USD9.20/38 imp, F1 USD1.19/9 imp (F1 không đổi qua hai lần đọc cách nhau vài phút). Reach UNAVAILABLE (hiện "-"/"0" trong khi có impressions).
- RMK source `RMK-SRC-F1F2-R5-EN-WAVE01-ANY-30D`: Ready, count `<300`, chưa gắn ad set. Ready ≠ gate 300.
- Chi tiết: [STATUS_2026-11-02](STATUS_2026-11-02.md) (Update 1–5).

## Quyết định của Bảo đã ghi (02/11/2026) — [CRITERIA_DECISIONS](CRITERIA_DECISIONS.md) Revision 2

| Mục | Luật |
|---|---|
| K2 | không ngưỡng số; báo clicks + impressions từng ad kèm định nghĩa, kỳ, imbalance, hạn chế |
| K3 | cột **Clicks** đang hiển thị, khóa một định nghĩa (xem lưu ý dưới) |
| K4 | không so CTR F1 vs F2 nếu impressions lệch > 3:1 cùng kỳ |
| K7 | cảnh báo (chỉ cảnh báo) khi chi lũy kế < 50% của USD10 × ngày đủ điều kiện → C3 cho Bảo |
| K8 | cảnh báo (chỉ cảnh báo) khi frequency thực tế ≥ 2,0 trong 7 ngày, chỉ khi Reach > 0 |

K1, K5, K6, K9, K10 và W2 funding vẫn NOT_DECIDED. Hiện tại: **C7 INCONCLUSIVE**; cặp 38/9 đã thấy trước khi chọn luật nên không dùng để tuyên bố winner/loser. Hạn quyết W2: 08/11 06:45 giờ VN; không quyết thì lịch kết thúc, tiền giữ (card A). Cảnh báo K7/K8 chỉ tạo decision pack cho Bảo; agent không tự pause/enable, tăng budget hay nới audience.

## Việc cần làm ở checkpoint (read-only, một browser controller)

1. Đọc lại ad set + từng ad (cột Performance, cùng cửa sổ, ghi observed_at kèm timezone): spend, impressions, **Clicks**, CTR, CPM, Reach/frequency nếu đã hiển thị. Báo thô + hạn chế theo K2.
2. Áp K4 (3:1), K7 (50%), K8 (2,0 nếu Reach > 0); ghi rõ actual eligibility days. Nếu chạm cảnh báo → decision pack C3 cho Bảo, không tự xử lý.
3. Nếu Clicks > 0: GA4 (stream `G-MV5QWN0XVM`) Session campaign tìm `fdi_f1_en_cold_wave01` / `fdi_f2_en_cold_wave01`; đọc processed sessions theo treatment (K6 chưa chọn nên báo thô); kiểm **nguồn thực tế của click đầu tiên**: URL ad có `utm_source=linkedin`, tham số ad set có `utm_source=LinkedIn` (có thể trùng/lệch chữ hoa) → C1 nếu GA4 ghi nguồn sai/tách đôi. Chưa phải lỗi đã xác nhận.
4. Còn mở: nhãn review chính thức từng ad (UI chỉ hiện "Active"), giờ/timezone của lịch (07:00 → 06:45 VN không đọc được từ UI), RMK audience count/gate.
5. Cập nhật STATUS + banner CURRENT_STATE + pointer README; chạy documentation sync gate; không rewrite lịch sử.

## Lưu ý và bẫy

- **K3 vs Q2:** [Q2](FOLLOWUP_Q2_REPORT_MAP.md) ghi LinkedIn có cột "Clicks to landing page". Bảo chọn cột "Clicks" đang hiển thị (tất cả lượt bấm). Không tự đổi sang landing-page clicks; chỉ báo như số phụ có nhãn và hỏi Bảo nếu cần đổi (xem đính chính trong CRITERIA_DECISIONS).
- Cột Ad sets đã trả về Performance; Overview có gợi ý chung "Add creatives (3+)" của LinkedIn: không phải plan item, không làm.
- Khi vào editor chỉ thoát bằng Cancel/back, không Save and exit; không gõ vào ô. Screenshot đôi khi time-out, thử lại một lần rồi dùng get_page_text.
- Không copy raw account URL, numeric account/entity ID, ảnh/DOM thô vào repo; không PII.
- Không spawn child, không commit/push/merge khi chưa có lệnh của Bảo. Coordinator audit và merge.

## Chưa làm / không làm

Không chọn K2–K8 thay Bảo ngoài những gì đã ghi; không quyết W2; không bật RMK; không đổi `utm_source`; không pause/enable; independent audit NOT_RUN.

Docs impact reviewed: thêm handoff; canonical pointer cập nhật ở `CURRENT_STATE.md` và README W1/W2; không đổi ngân sách, creative, tracking, lịch hay anchor.

## Update 03/11/2026 — checkpoint Day-3 đã đọc

Bước 1–2 đã thực hiện (read-only) và ghi tại [STATUS_2026-11-03](STATUS_2026-11-03.md): K4 áp dụng, K7 không chạm, K8 chỉ là candidate (Reach lag); bước 3 (GA4) chưa làm vì Clicks = 0; bước 4 vẫn mở. Nhãn HANDOFF_ONLY / NOT_STARTED ở đầu file là snapshot ngày 02/11.
