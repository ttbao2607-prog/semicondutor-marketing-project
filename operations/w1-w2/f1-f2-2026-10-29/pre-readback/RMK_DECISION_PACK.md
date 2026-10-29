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

1. **Số học về cổng 300.** Audience cold hiện là 470+ (UI forecast, ước tính). Pool RMK là tập con của những người thấy và tương tác với hai ad. Đạt 300 reachable sau lọc sẽ cần khoảng hai phần ba toàn audience tương tác; điều này gần như không thực tế với ad cold thường. “470+” là mức sàn hiển thị, không phải số chính xác, nên đây là suy luận thứ tự độ lớn, không phải dự báo.
2. **Forecast native của chính ad set** (đọc 29/10 trong P1): 30 ngày spend $0–14, reach 71–170, tần suất 1,0–1,4; lưu ý của UI: dự báo là định hướng. Nếu đúng hướng, delivery thấp hơn nhiều so với pacing USD10/ngày và pool tương tác sẽ rất nhỏ.
3. **Hệ quả:** mặc định kỳ vọng là **S2** (Ready nhưng dưới cổng) hoặc C7 dữ liệu mỏng; card D trong [W2_ACTION_CARDS](W2_ACTION_CARDS.md) nhiều khả năng là HOLD. Không hạ cổng 300 để “đủ”; thay đổi cold audience/ngân sách là quyết định riêng ngoài gói này.

## Quyết định cần Bảo chọn

| # | Quyết định | Phương án | Đề xuất mặc định (có lý do) | Trade-off | Input cần |
|---|---|---|---|---|---|
| R1 | Interaction rule | A Any interactions · B Chargeable clicks | **A** | A rộng nhất nên có cơ hội cao hơn tới cổng nhưng trộn tín hiệu mạnh/yếu; B chặt hơn, pool nhỏ hơn và với quy mô này gần như chắc không đạt cổng | chọn A hoặc B; định nghĩa “any interaction” phải đọc từ UI khi tạo |
| R2 | Lookback | 30 ngày (mặc định data plan) · dài hơn | **30 ngày** | W1 chỉ 7 ngày nên lookback chưa là ràng buộc trong W1; dài hơn thêm reach nhưng cũ hơn, làm yếu liên hệ với thông điệp tuần này | xác nhận các mốc UI có (chưa kiểm); không nêu số ngày như native-supported |
| R3 | Cấu trúc pool | Một pool chung cho hai ad · mỗi ad một pool | **Một pool chung** | tách đôi làm mỗi pool nhỏ hơn và càng khó đạt cổng, còn pool chung làm người click F1 có thể thấy carousel F2 (lệch persona liên tục A7) | quyết định ở S4 chọn carousel nào cho pool chung: theo treatment có tín hiệu tốt hơn, hoặc chạy cả hai theo thứ tự đã định |
| R4 | Objective RMK | Engagement · click tới reader | chưa chọn; quyết khi release | cả hai hợp lý, chưa kiểm releasable | giữ tới S4 |
| R5 | Chủ sở hữu source | Bảo · người ủy quyền | **Bảo** | — | xác nhận |
| R6 | **Thời điểm tạo source audience** | trước first delivery · tại check ngày 3 · tại W1 close | **Quyết sớm (trước 01/11) có thể tạo ngay khi Bảo cấp mandate hẹp** | nếu nền tảng chỉ tích lũy từ lúc tạo, tạo muộn mất tương tác W1; nếu có backfill thì không mất gì; **chưa biết nền tảng làm cái nào**, nên đây là rủi ro bị động | Bảo cấp hoặc không cấp mandate tạo source (chỉ tạo audience, không tạo ad/RMK); nếu không cấp thì RMK ở W1 bị coi là S0/S1 |

## Evidence cần khi đọc và fallback

| Tình huống | Đọc gì | Fallback (theo S0–S4) |
|---|---|---|
| Chưa tạo source | không có audience; reachable UNKNOWN | S0: giữ cold; không dựng RMK từ Page/organic; không hứa backfill |
| Đang processing | native status Processing | S1: đọc lại sau; không đánh giá kích thước trước khi Ready |
| Ready nhưng dưới 300 reachable | status Ready, số reachable sau lọc, thời điểm | S2: (a) tiếp tục cold; (b) quyết định nới rule/lookback trong lựa chọn UI; (c) bỏ RMK W2 và thay phần cold yếu; (d) Search chỉ khi Bảo chọn trong cap; không pool Page/organic, không chia nhỏ pool |
| ≥ 300 nhưng thiếu gate khác | URL/tracking/pacing/budget | S3: sửa gate trước |
| Đủ gate | tất cả | S4: Bảo chọn objective và release trong cap 5,6 triệu của đợt kế |

Gate 300 là contract của repo cần đối chiếu UI hiện hành; không là guarantee hiệu quả. Source choice/creation tách khỏi enable RMK: Ready/eligible/readback vẫn bắt buộc. Không đổi format cold để gom warm khi chưa có mandate.

## Việc Bảo cần trả lời

1. Chọn R1, R2, R3, R5 theo mặc định hoặc đổi.
2. Quyết R6: có cấp mandate tạo source audience trước 01/11 không.
3. R4 để đến S4.

Docs impact reviewed: no canonical update required (đề xuất chưa là quyết định; không đổi audience/message, cap, tracking).
