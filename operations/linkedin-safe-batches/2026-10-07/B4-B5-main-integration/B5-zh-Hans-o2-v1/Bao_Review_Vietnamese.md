# B5 O2 giản thể · diễn giải để Bảo kiểm

Persona: Operations phối hợp Quality tại entity FDI đóng gói/kiểm thử phù hợp. Không mặc định mọi OSAT có quyền mua ERP địa phương.

| Card | Ý nghĩa tiếng Việt |
|---|---|
| Cold | Cùng một lot, vì sao báo cáo trạng thái khác nhau? Trước bàn giao, kiểm công đoạn, thời điểm ghi nhận và người phụ trách hồ sơ. |
| O2-A1 | Trước quyết định bước tiếp, kiểm mỗi báo cáo đang mô tả công đoạn và thời điểm nào. |
| O2-A2 | So sánh trên cùng cơ sở. Nếu khác công đoạn/thời điểm, cả hai báo cáo có thể đều đúng. |
| O2-A3 | Hồ sơ nào là căn cứ bàn giao? Xác định hồ sơ nguồn và thông tin bên nhận cần. |
| O2-A4 | Ai xác nhận thông tin còn thiếu? Làm rõ thông tin thiếu, người kiểm nguồn và người xác nhận bước tiếp. |
| O2-A5 | Cơ sở chung cho bàn giao: lot, công đoạn, thời điểm, nguồn và người xác nhận. Nguồn giải pháp Đài Loan ERP/MES được ghi riêng. |
| Proof1 | Digiwin cung cấp giải pháp số cho sản xuất, gồm ERP và smart manufacturing. Nguồn giới thiệu công ty Digiwin Việt Nam. |
| Proof2 | Case đóng gói/kiểm thử tại Trung Quốc: 江苏中科智芯集成科技有限公司 triển khai integrated Digiwin ERP+iMES cho bài toán hồ sơ, quy trình và hiệu quả sản xuất. |
| Proof3 | Trong case Trung Quốc, MES liên kết lot, công vị, người vận hành và sản phẩm/vật liệu để truy xuất; ghi nhận và báo cáo bất thường theo cấp. |
| Proof4 | Đọc chi tiết liên kết hồ sơ, phân phối thay đổi tham số và ghi nhận bất thường; CTA dẫn tới reader giản thể có nguồn đúng case. |

ROI là giá trị vận hành ngầm qua cách đối chiếu và trách nhiệm bàn giao. Không hứa tự đồng bộ trạng thái, tăng yield hay bịa ROI tài chính. Reader giữ cơ chế ERP+iMES, SPC, ECN, liên kết hồ sơ và escalation đúng nguồn; không dùng kết quả chốt sổ làm proof cho bàn giao lot.

Proof3–4 tái dùng đúng byte từ B2; proof1–2 dựng mới vì B2 còn finding nguồn nhỏ. Proof2 lần đầu tự thêm skyline/pagodas ở footer, đã có một corrective bỏ phần ngoài storyboard. Kết luận cuối và giới hạn render đọc ở postgen-review.json; tài liệu này không thay receipt hoặc native-market certification.

B4 được Bảo duyệt offline; B5 chờ Bảo kiểm. Không bắt đầu B6 trước lượt duyệt kế tiếp. Không ZIP.
