# Quyết định Bảo — ngân sách dashboard và review tuần

Record ID: **PACKAGE-V2-PO-DASHBOARD-WEEKLY-20261007**. Revision 1.0, 07/10/2026. Nguồn: chỉ đạo trực tiếp của Bảo trong phiên sau khi đọc tóm tắt Phase 1.

## Chỉ đạo gốc

> Tổng chi cứ ghi là chưa thuế nhé, phần này kế toán sẽ tự tính, Bảo theo dõi số tiền trên dashboard (cty có pipeline riêng để handle, marketer chỉ quản lý/coordinate với số tiền thao tác trên dashboard. Tuần đầu chạy đúng plan, hết tuần review, nếu fail vì các lý do thì Bảo đã có cnuẩn bị sẵn 2 pipeline (VN week1-2, hư khúc nào ghép khúc đó flexibly) và FDI rát nhiều asset để swap. Tệp matched audience cũng có chính tắc và backup >> Tuần 2 sẽ quyết định tùy data matrix ntn.

Giữ nguyên body do Bảo cung cấp, gồm lỗi gõ. “Chính tắc” được hiểu là tệp chính trong cặp tệp chính/backup; không đổi identity/source của hai audience.

## Quyết định áp dụng vào package

1. Ghi **11,7 triệu đồng ngân sách media, chưa thuế**. Marketer quản lý/coordinate các số tiền ads trên dashboard. Kế toán và pipeline riêng của công ty xử lý thuế/thanh toán; package không chờ số all-in hoặc tự thêm phần trăm thuế/đệm. Giữ đúng đơn vị/currency khi đọc dashboard; không tự tạo tỷ giá.
2. **Tuần 1 chạy đúng plan, review cuối tuần.** Đây là cadence đã chốt, thay cho weekly review chỉ là đề xuất trong skeleton trước. Package là kế hoạch; account/lịch live thực tế giữ scope triển khai riêng.
3. **Tuần 2 quyết định theo data matrix**: đọc delivery, đúng tệp, attention, đoạn giải thích/proof/reader, chi phí và độ tin cậy measurement rồi chọn hành động.
4. Bảo đã chuẩn bị khả năng điều chỉnh: **VN week1/week2**, **thư viện FDI**, **Matched Audience chính và backup**. Sửa/swap đoạn gặp vấn đề bằng asset phù hợp, giữ phần có tín hiệu tốt; không phải thay toàn journey theo tuần mặc định.
5. Sự sẵn có của hai audience không làm pending processing/mapping của từng tệp thành verified ready. Thực tế phân phối hoặc fit của asset/cấu hình được đọc bằng data matrix, không suy từ tồn tại thư viện.
6. Ghép/swap giữ audience/persona/locale, nguồn/case, product layer và continuity đúng anchor. Từng đoạn được thay và transition liên quan phải qua tiền/hậu kiểm hiện hành; không sửa frozen gates hoặc chuyển approval của một revision thành blanket approval cho tổ hợp mới.

## Quan hệ với ngân sách tham chiếu

Trần 11,7 triệu chưa thuế và cách biểu diễn 5,6 + tối đa5,6 + Search tối đa0,5 giữ nguyên. 6,1 triệu giữ lại nằm trong tổng. Mốc 400.000/ngày ×14ngày =5,6triệu là tham chiếu cũ; review sau tuần đầu không tự đổi cap, khẳng định đã chi2,8triệu, hoặc cấp thêm5,6triệu cho riêng tuần2. Việc dùng tiếp ngân sách do Bảo quyết định theo dữ liệu trong envelope.

## Phạm vi chốt

Chốt budget presentation/decision rights, cadence tuần1→review→tuần2 và flexible corrective/swap logic. Không nhận đây là acceptance toàn skeleton hoặc yêu cầu bắt đầu Phase2/3. Reader revision, metric nguồn/ngưỡng cụ thể và actual audience processing vẫn là execution inputs nội bộ, không thành loạt câu hỏi xin sếp duyệt.

Record này là source ưu tiên cho những phần bị thay thế trong Phase1. Message anchor Vy1.0, harness/anchor/process freeze và adapter DEVELOPING/NOT_FROZEN giữ nguyên. Main/source worktrees khác chỉ đọc; không commit/merge/push/live hoặc genảnh trong lượt cập nhật tài liệu này.
