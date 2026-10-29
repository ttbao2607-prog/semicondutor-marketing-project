# P7c — Incident card

Revision 1 · 29/10/2026 · REVIEW_ONLY_NO_AUTONOMOUS_ACTION. Authority: Bảo giao P4–P7. Mỗi card đi theo chuỗi: **bằng chứng chính xác → phạm vi ảnh hưởng → đề xuất pause/sửa → kiểm phục hồi → rollback**. Workflow này không có quyền pause/enable; chỉ báo Bảo ngay và đề xuất. Mọi thay đổi cần mandate đúng thao tác. Không thêm gate CRM/rep tin nhắn/lead-validation. Root tự review; independent audit NOT_RUN. Giá trị “expected” lấy từ [PRELAUNCH_READBACK](PRELAUNCH_READBACK.md).

## I1 — URL / locale / claim sai

- **Bằng chứng:** URL đích của ad lệch `…/semiconductor-case-reader?t=F1|F2&lang=en` (kèm UTM `fdi_f1|f2_en_cold_wave01`, `f1|f2_cold_v1`) hoặc reader mở sai ngôn ngữ/treatment; hoặc nội dung/claim khác nguồn đã chấp nhận (ROI%, outcome mới, Bright ngoài scope); chụp màn hình và text đã sanitize.
- **Phạm vi:** theo ad (F1 hoặc F2) hay cả hai; số click đã đi lệch.
- **Đề xuất:** Bảo quyết pause ad ảnh hưởng, sửa bounded (URL/copy), không đổi audience hay budget.
- **Kiểm phục hồi:** mở lại ad đã lưu, đối chiếu URL/UTM, kiểm reader đúng locale/treatment và CTA contact-vn/return.
- **Rollback:** URL/creative nguồn đã pin (B13 v5, B16 v2).

## I2 — Targeting drift

- **Bằng chứng:** audience đã lưu khác expected: Vietnam recent/permanent; Job Functions (Engineering, IT, Operations, QA) AND Seniority (CXO, Director, Manager, VP) AND company list R5; audience expansion tắt; Feed only (Right Rail, LAN tắt); English. Forecast thay đổi chỉ là observation cần điều tra; không chứng minh targeting drift khi saved settings không đổi.
- **Phạm vi:** ad set (một ad set chung).
- **Đề xuất:** báo Bảo; nếu drift đang làm chi sai, đề xuất pause ad set; sửa đúng mệnh đề lệch; mọi đổi scope là quyết định của Bảo.
- **Kiểm phục hồi:** mở lại settings đã lưu, đối chiếu từng trường ở bảng READBACK; demographics report khi có.
- **Rollback:** khôi phục đúng giá trị đã lưu trong receipt.

## I3 — Review / delivery hold

- **Bằng chứng:** nhãn Rejected/hold/Not delivering sau thời điểm Scheduled bắt đầu (01/11 07:00 VN), lý do native hiển thị, thời điểm; phân biệt “Not delivering – Scheduled” trước 01/11 (bình thường) với sau.
- **Phạm vi:** ad F1, F2 hoặc cả ad set; số ngày eligible bị mất.
- **Đề xuất:** ghi nguyên nhân hiển thị; chuẩn bị next action cụ thể (khiếu nại/sửa); không bấm enable/relaunch theo suy đoán; không tự kéo dài lịch.
- **Kiểm phục hồi:** readback trạng thái sau xử lý, ghi actual first delivery.
- **Rollback:** nếu sửa creative, giữ bản gốc.

## I4 — Điều tra measurement và xác nhận lỗi

- **Tín hiệu cần điều tra:** click LinkedIn có nhưng GA4 `fdi_*` chưa có session, query treatment không đọc được hoặc QA contamination. Riêng các dấu hiệu này chưa chứng minh tracking hỏng: kiểm click definition, đúng property/campaign/window/timezone, processing/consent và scope. Có thể dùng campaign/content thay chiều `t` nếu đã xác minh đường lọc.
- **Bằng chứng lỗi xác nhận:** saved destination/UTM sai so contract, dispatch sai stream hoặc failure tái hiện trên route bằng paired QA có đánh dấu; ghi expected/actual, evidence và scope. Không đề xuất pause chỉ vì report thiếu hoặc hai hệ đếm khác nhau.
- **Phạm vi:** có thể là report-only hoặc route/measurement thật; phải xác minh, không mặc định không ảnh hưởng delivery/entry.
- **Đề xuất:** đối soát route/UTM/stream; nếu lỗi entry/đo lường thật, trình Bảo pause phần ảnh hưởng và sửa kỹ thuật bounded (không sửa hook để chữa tracking); tách synthetic QA khỏi paid.
- **Kiểm phục hồi:** recheck cùng window, processing status rõ; không coi HTTP 204 là processed.
- **Rollback:** không thay đổi creative; nếu sửa tracking thì theo contract.

## I5 — Rủi ro ngân sách

- **Bằng chứng:** spend/pacing vượt kỳ vọng so USD10/ngày chia sẻ (nominal USD70 W1); delivery sau 08/11 06:45; ad set hoặc campaign khác bật và có spend. **Watch item hiện có (P1 OBS-1):** campaign `Test` (Brand Awareness) On/Active và ad “Images Carousale Test” On/Active (chưa đối chiếu ad thuộc campaign nào), spend 30 ngày $0; chưa đọc budget/lịch; và `RSCH-TH-WEBINAR-FORECAST-1027` đang On/Scheduled — ngoài scope F1/F2 nhưng Bảo cần quyết định có đọc thêm hay xử lý.
- **Phạm vi:** tổng chi vs cap 11,7 triệu; không tự dùng FX.
- **Đề xuất:** báo Bảo ngay; đề xuất pause phần gây chi sai; không tự tăng daily/nới audience.
- **Kiểm phục hồi:** spend readback cùng timezone/currency; ghi accounting basis.
- **Rollback:** giữ lịch cũ hết hạn; không dùng reserve nếu chưa có quyết định.

## Nguyên tắc chung

- Lỗi integrity/delivery thật được báo ngay, không đợi hết W1 hay đợi numeric threshold.
- Ghi vào [DECISION_LOG.csv](../DECISION_LOG.csv) khi Bảo quyết (ở lượt này chưa sửa).
- Không đưa raw account/lead/member data hay numeric ID vào Git.

Docs impact reviewed: current canonical pointers updated for P1–P7 execution/corrections. See [audit closeout](AUDIT_FIX_CLOSEOUT.md).
