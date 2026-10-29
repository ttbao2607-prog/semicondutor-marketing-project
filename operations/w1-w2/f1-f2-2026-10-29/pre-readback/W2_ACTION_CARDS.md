# P7a — Bốn action card cho quyết định cuối W1

Revision 1 · 29/10/2026 · DRAFT_FOR_BAO / NOT_DECIDED. Authority: Bảo giao P4–P7. Đây là phương án để Bảo chọn, không phải lệnh: không tự nối W1 sang W2, không dùng reserve, không pause/enable. Trường chưa có dữ liệu giữ `NOT_DECIDED`; không đủ điều kiện thì `HOLD`. Root tự review; independent audit NOT_RUN. Nối với [DECISION_LOG.csv](../DECISION_LOG.csv) (cột `primary_scenario`, `keep`, `change`, `bao_decision`, `operator`, `budget_currency_and_remaining`, `start_end_timezone`, `next_check`, `rollback`), [SCENARIOS.csv](../SCENARIOS.csv), [CRITERIA_DECISIONS](CRITERIA_DECISIONS.md) và [INCIDENT_CARDS](INCIDENT_CARDS.md).

## Khung chung

- **Cap:** 11,7 triệu VND trước thuế; đợt đầu 5,6 triệu; giữ lại 6,1 triệu (tối đa 5,6 triệu cho đợt LinkedIn kế và 0,5 triệu cho Search tùy chọn). Mọi chi cho W2 lấy từ phần giữ lại và chỉ khi Bảo ghi quyết định cụ thể; actual accounting basis và số còn lại điền khi có, không dùng FX tự suy. W1 là daily pacing USD10 chia sẻ, danh nghĩa USD70, không phải lifetime cap.
- **Lịch:** W1 kết thúc 08/11 06:45 giờ VN và không tự nối. Không có quyết định thì để lịch kết thúc, giữ tiền.
- **Đề xuất cho mọi phương án có chạy tiếp:** cửa sổ mới cùng độ dài 7 ngày để so equal-length; ngày bắt đầu do Bảo chốt, không nối tự động.

## Chọn card nào (gợi ý theo scenario chính)

| Tình huống đọc được | Card gợi ý |
|---|---|
| C7 dữ liệu mỏng, hoặc C3 delivery thấp rõ ràng | **A** (hoặc **B** nếu Bảo muốn thêm thời gian quan sát) |
| C1/C2/C3 sạch và tín hiệu đủ đọc, C4/C5 không có vấn đề | **B** |
| C4 (đúng tệp nhưng ít chú ý) | **C** thay hook/visual |
| C5 (có quan tâm nhưng đọc tiếp yếu) | **C** thay đoạn chuyển/explanation/reader sau khi kiểm link/đo lường |
| C6 (RMK) với S4 đạt đủ gate | **D** |
| Lỗi tích hợp thật (C1, URL/locale/claim, targeting, budget) | không phải card; dùng [INCIDENT_CARDS](INCIDENT_CARDS.md) ngay, không chờ hết W1 |

Lưu ý từ P1/P6: forecast native của ad set là spend 30 ngày $0–14 và reach 71–170 (định hướng), nên khả năng cao W1 thiếu dữ liệu (C7) và RMK dưới cổng. Nới audience hay ngân sách là quyết định L2 riêng, không nằm trong bốn card.

## Card A — Giữ hết lịch, giữ tiền

- **Trigger:** C7; hoặc C3 chưa đủ cơ sở; hoặc Bảo không muốn đổi gì; hoặc không có quyết định trước 08/11.
- **Giữ:** tất cả creative/audience/URL hiện có và toàn bộ phần giữ lại 6,1 triệu; không chi thêm.
- **Đổi:** không.
- **Source/asset:** không cần asset mới.
- **Prerequisite:** ghi INCONCLUSIVE + raw counts + limitations vào decision log.
- **Budget/date:** không phát sinh. W1 hết lịch thì kết thúc.
- **Owner:** Bảo quyết; operator chỉ ghi nhận.
- **Rollback / exit:** không có thay đổi để hoàn tác; có thể mở lại card B/C sau với ngày mới.
- **Recheck:** đọc lại report đã xử lý sau lag (cùng window W1) và ghi thời điểm; đổi kết luận chỉ khi có evidence mới.

## Card B — Tiếp tục cold, scope giữ nguyên

- **Trigger:** C1–C3 sạch; dữ liệu W1 đủ đọc theo criteria Bảo chọn trước ([CRITERIA_DECISIONS](CRITERIA_DECISIONS.md)), hoặc Bảo chọn cho thêm thời gian quan sát (C7).
- **Giữ:** audience R5 EN, hai ad, USD10 shared, Reach / Maximum delivery, Feed only, URL/UTM hiện có.
- **Đổi:** chỉ ngày/ngân sách (mới). Không sửa creative.
- **Source/asset:** như W1.
- **Prerequisite:** ad set vẫn không bị reject/hold (readback); ngày bắt đầu mới do Bảo chốt; lịch cũ đã kết thúc hoặc đã được đặt lại bằng thao tác được ủy quyền.
- **Budget/date đề xuất (chưa chốt):** 7 ngày, USD10/ngày chia sẻ như W1, chi từ phần giữ lại; số VND thực theo accounting basis khi có.
- **Owner:** Bảo quyết; operator thực hiện khi có mandate.
- **Rollback / exit:** pause ad set; giữ lịch hết hạn; tiền chưa chi vẫn giữ.
- **Recheck:** checkpoint ngày delivery 3 và 7 (đề xuất, không tự động); so equal-length với W1.

## Card C — Thay một đoạn

- **Trigger:** C4 hoặc C5, sau khi C1–C3 sạch và criteria đã chọn trước.
- **Giữ:** audience, objective/bid/budget/locale, đoạn đang có tín hiệu; chỉ một biến đổi.
- **Đổi (chọn một):** (1) hook hoặc visual cold F1 hoặc F2 — theo [COLD_OPTIONS](COLD_OPTIONS.md), hiện `BRIEF_ONLY`; (2) đoạn explanation/proof hoặc reader — chỉ sau khi đã kiểm link/tải/đo lường.
- **Source/asset:** brief trong COLD_OPTIONS; chưa có PNG swap-ready; generation/adaptation/upload là việc riêng sau quyết định và gate MSG-ANCHOR-01 + native QA.
- **Prerequisite:** quyết định của Bảo về đúng đoạn đổi và criteria; asset mới qua gate; `utm_content` mới để tách đọc.
- **Budget/date đề xuất (chưa chốt):** như B, cửa sổ 7 ngày bắt đầu sau khi native QA xong.
- **Owner:** Bảo chọn; agent/operator theo mandate riêng.
- **Rollback / exit:** quay về creative gốc B13 v5/B16 v2 (ad gốc để Off, không xóa); F3 là đổi tình huống, không tính là swap.
- **Recheck:** readback sau đổi, cùng độ dài cửa sổ; mẫu mỏng sang C7.

## Card D — RMK sau gate

- **Trigger:** C6; S4 đạt đủ gate ([RMK_DECISION_PACK](RMK_DECISION_PACK.md)).
- **Giữ:** persona, chủ đề, English; source chỉ từ hai ad cold.
- **Đổi:** thêm carousel RMK (explanation 6 / proof 4) cho pool; không đổi format cold.
- **Source/asset:** `LI-wave01-F1/F2-en-EXPL-v1`, `-PROOF-v1` (đã được Bảo chấp nhận paid asset), QA nội bộ ở [CAROUSEL_QA](CAROUSEL_QA.md) (chưa native).
- **Prerequisite:** source Ready/eligible; ≥ 300 reachable sau lọc trong UI hiện hành; dựng và native preview; URL/tracking/pacing/budget đã kiểm; Bảo chọn R1–R5 và objective.
- **Budget/date đề xuất (chưa chốt):** trong cap 5,6 triệu của đợt kế; ngày Bảo chốt.
- **Owner:** Bảo; operator dựng khi có mandate.
- **Rollback / exit:** pause ad RMK; giữ pool; quay lại cold hoặc giữ tiền.
- **Recheck:** delivery/eligibility readback; không enable chỉ vì đã hết tuần hay thư viện có ảnh.
- **Dự báo:** nhiều khả năng HOLD vì dưới cổng; ghi S-state thực tế.

## Mẫu điền decision log (đề xuất, chưa điền)

`decision_id=W1_CLOSE_01`, `primary_scenario`/`secondary_scenarios` theo đọc thật, `keep`/`change` theo card, `bao_decision=NOT_DECIDED` cho tới khi Bảo ghi, `execution_state=NOT_EXECUTED`. Không sửa DECISION_LOG.csv ở lượt này.

Docs impact reviewed: no canonical update required.
