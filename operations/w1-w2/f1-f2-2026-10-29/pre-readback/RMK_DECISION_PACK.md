# P6 — Cấu hình RMK để Bảo quyết sớm

Revision 1 · 29/10/2026 · DECISION_PACK_READY / BAO_INPUT_NEEDED. Authority: Bảo giao P4–P7. Chỉ đề xuất: không tạo audience, không bật RMK, không dựng ad, không hứa platform backfill lịch sử. Root tự review; independent audit NOT_RUN. Nguồn: [01 decision pack](../../../linkedin-rmk-source-readiness/2026-10-08/01_RMK_Source_Rule_Decision_Pack.md), [03 fallback tree S0–S4](../../../linkedin-rmk-source-readiness/2026-10-08/03_RMK_Fallback_Decision_Tree.md), [SOURCE_REGISTRY](../SOURCE_REGISTRY.csv), [REPORT_ACCESS_MAP](REPORT_ACCESS_MAP.md), [PRELAUNCH_READBACK](PRELAUNCH_READBACK.md).

## Exact source keys (public stable keys; numeric IDs private)

| Key | Giá trị |
|---|---|
| Cohort | `F1F2-R5-EN-WAVE01` |
| Source ad F1 | `LI-wave01-F1-en-COLD-v1` · `utm_campaign=fdi_f1_en_cold_wave01` · `utm_content=f1_cold_v1` |
| Source ad F2 | `LI-wave01-F2-en-COLD-v1` · `utm_campaign=fdi_f2_en_cold_wave01` · `utm_content=f2_cold_v1` |
| Ad set | `DRAFT_REVIEW_R5_EN_F1_F2_WAVE01_DO_NOT_LAUNCH` (tên lịch sử, đang On/Scheduled), parent `VALIDATION_ONLY_VN_SEMICONDUCTOR_ABM_2026-09-14` |
| RMK ad (deferred) | `LI-wave01-F1/F2-en-EXPL-v1` (carousel 6) và `-PROOF-v1` (carousel 4), `utm_campaign=fdi_f1/f2_en_rmk_wave01` |
| Trạng thái audience | `NOT_VERIFIED_CREATED`; rule/lookback = `NOT_SELECTED`; reachable = UNKNOWN |

Nguồn bắt buộc: chỉ member tương tác với đúng hai ad cold này. Không dùng Page/organic/website/campaign khác; không gộp ngầm pool.

## Quan sát cần Bảo biết trước khi chọn

1. **Không suy tỷ lệ từ470+.** Đây là nhãn ước tính có dấu+, không phải tổng audience chính xác. Chưa biết mẫu số nên không tính tỷ lệ cần tương tác để đạt300reachable và không kết luận gần như không thể đạt. Có rủi ro pool nhỏ; cần actual source status/reachable sau lọc.
2. **Forecast native của chính ad set** (đọc 29/10 trong P1): 30 ngày spend $0–14, reach 71–170, tần suất 1,0–1,4; lưu ý của UI: dự báo là định hướng. Đây là forecast30ngày, không phải số thực W1 hay dự báo kích thước pool; không quy đổi sang kết quả7ngày hoặc dùng làm ngưỡng cảnh báo.
3. **Trạng thái hiện có:** source **NOT_VERIFIED_CREATED**, reachable **UNKNOWN**. Card D trong [W2_ACTION_CARDS](W2_ACTION_CARDS.md) HOLD vì chưa có evidence đủ gate, không vì đã biết dưới ngưỡng. Chỉ gán S2 khi thực sự Ready và dưới cổng sau lọc; C7 chỉ theo dữ liệu đọc được. Không hạ cổng 300 để “đủ”; thay đổi cold audience/ngân sách là quyết định riêng ngoài gói này.

## Quyết định cần Bảo chọn

| # | Quyết định | Phương án | Đề xuất mặc định (có lý do) | Trade-off | Input cần |
|---|---|---|---|---|---|
| R1 | Interaction rule | A Any interactions · B Chargeable clicks | **A** | A rộng nhất nên có cơ hội cao hơn tới cổng nhưng trộn tín hiệu mạnh/yếu; B có thể cho pool nhỏ hơn; mức chênh và khả năng đạt cổng chưa đo | chọn A hoặc B; định nghĩa “any interaction” phải đọc từ UI khi tạo |
| R2 | Lookback | 30 ngày (mặc định data plan) · dài hơn | **30 ngày** | W1 chỉ 7 ngày nên lookback chưa là ràng buộc trong W1; dài hơn thêm reach nhưng cũ hơn, làm yếu liên hệ với thông điệp tuần này | xác nhận các mốc UI có (chưa kiểm); không nêu số ngày như native-supported |
| R3 | Cấu trúc pool | Một pool chung cho hai ad · mỗi ad một pool | **Một pool chung** | tách đôi làm mỗi pool nhỏ hơn và càng khó đạt cổng, còn pool chung làm người click F1 có thể thấy carousel F2 (lệch persona liên tục A7) | quyết định ở S4 chọn carousel có continuity phù hợp pool; nếu chạy cả hai phải kiểm từng ad tự có ngữ cảnh, không bảo đảm người xem thấy theo thứ tự |
| R4 | Objective RMK | Engagement · click tới reader | chưa chọn; quyết khi release | cả hai hợp lý, chưa kiểm releasable | giữ tới S4 |
| R5 | Chủ sở hữu source | Bảo · người ủy quyền | **Bảo** | — | xác nhận |
| R6 | **Thời điểm tạo source audience** | trước first delivery · tại check ngày 3 · tại W1 close | **Quyết sớm (trước 01/11) có thể tạo ngay khi Bảo cấp mandate hẹp** | nếu nền tảng chỉ tích lũy từ lúc tạo, tạo muộn mất tương tác W1; nếu có backfill thì không mất gì; **chưa biết nền tảng làm cái nào**, nên đây là rủi ro bị động | Bảo cấp hoặc không cấp mandate tạo source (chỉ tạo audience, không tạo ad/RMK); nếu chưa có mandate/evidence thì giữ NOT_VERIFIED_CREATED và chưa enable; không tự gán Processing/Ready |

## Evidence cần khi đọc và fallback

| Tình huống | Đọc gì | Fallback (theo S0–S4) |
|---|---|---|
| Chưa tạo source | không có audience; reachable UNKNOWN | SOURCE_UNVERIFIED: xác minh có audience hay chưa; chưa enable, giữ lịch cold hiện hữu. S0 trong cây gốc nói cold chưa delivery, không đồng nghĩa chưa tạo source. Không dùng Page/organic; không hứa backfill |
| Đang processing | native status Processing | S1: đọc lại sau; không đánh giá kích thước trước khi Ready |
| Ready nhưng dưới 300 reachable | status Ready, số reachable sau lọc, thời điểm | S2: (a) tiếp tục cold; (b) quyết định nới rule/lookback trong lựa chọn UI; (c) bỏ RMK W2 và thay phần cold yếu; (d) Search chỉ khi Bảo chọn trong cap; không pool Page/organic, không chia nhỏ pool |
| ≥ 300 nhưng thiếu gate khác | URL/tracking/pacing/budget | S3: sửa gate trước |
| Đủ gate | tất cả | S4: Bảo chọn objective, nguồn tiền sau đối soát và release trong envelope được quyết định; không mặc định W2 dùng reserve |

Gate 300 là contract của repo cần đối chiếu UI hiện hành; không là guarantee hiệu quả. Source choice/creation tách khỏi enable RMK: Ready/eligible/readback vẫn bắt buộc. Không đổi format cold để gom warm khi chưa có mandate.

## Việc Bảo cần trả lời

1. Chọn R1, R2, R3, R5 theo mặc định hoặc đổi.
2. Quyết R6: có cấp mandate tạo source audience trước 01/11 không.
3. R4 để đến S4.

Docs impact reviewed: current canonical pointers updated for P1–P7 execution/corrections; proposal remains undecided, no account change. See [audit closeout](AUDIT_FIX_CLOSEOUT.md).
