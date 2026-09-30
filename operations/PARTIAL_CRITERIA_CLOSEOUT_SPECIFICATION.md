# TIÊU CHUẨN ĐÓNG PASS CLOSEOUT CHO CÁC TIÊU CHÍ PARTIAL (CLOSEOUT ACCEPTANCE CONTRACT)
**Worktree:** `D:\Digiwin_Semiconductor_Audit_Worktree`  
**Branch:** `slice/audit-automation-artifacts`  
**Ngày lập:** 2026-09-30  
**Người phê duyệt / Product Owner:** Bảo  
**Người điều phối / Coordinator:** Antigravity Coordinator (AGY)  
**Mục tiêu:** Định nghĩa chuẩn xác nhận nghiệm thu đóng (PASS Closeout Criteria) cho 5 tiêu chí còn ở mức `PARTIAL` (A1, A2, B1, C2, D1) tương ứng với 5 Actionable GAPs đã ghi nhận trong Báo cáo Kiểm toán `AUTOMATION_ARTIFACTS_AUDIT_REPORT_2026-09-30.md`. Bất kỳ Subagent nào thực thi sửa đổi phải đáp ứng đầy đủ điều kiện nghiệm thu cơ học dưới đây trước khi Coordinator ký PASS.

---

## 1. Bảng Tiêu Chuẩn Nghiệm Thu Closeout Chi Tiết

### Tiêu chuẩn Closeout 1: GAP-01 & Tiêu chí A1 (Khóa danh sách loại trừ đại tập đoàn trong ICP)
* **Mục tiêu:** Chuyển quyết định D1 từ trạng thái pending/proposal sang trạng thái chính thức được áp dụng vào tài liệu chiến lược và targeting.
* **Điều kiện PASS Closeout:**
  1. File `drafts/S01_Proof_and_Message.md` phải có mục ghi nhận phê duyệt D1: Khẳng định rõ loại trừ 4 đại tập đoàn có hệ thống sản xuất chung toàn cầu: Intel, Samsung, Hana Micron, Amkor.
  2. Tập trung 100% vào chuỗi cung ứng & công nghiệp phụ trợ: PCB, Substrate, Vật liệu đóng gói, Linh kiện, Gia công cơ khí chính xác cho thiết bị bán dẫn.
  3. File `ads/linkedin/LinkedIn_Build_Pack.md` phải có dòng cấu hình nhắm mục tiêu: `Excluded Companies: Intel, Samsung Electronics, Hana Micron, Amkor Technology` trong bảng thiết lập Campaign/Ad set.
* **Kiểm tra cơ học (Verification command):**
  - Kiểm tra chuỗi `"Excluded Companies"` hoặc `"Loại trừ tập đoàn lớn"` trong cả 2 file `S01_Proof_and_Message.md` và `LinkedIn_Build_Pack.md`.

---

### Tiêu chuẩn Closeout 2: GAP-02 & Tiêu chí A2 (Bổ sung Headline tiếng Việt nội địa chuyên sâu)
* **Mục tiêu:** Đưa thông điệp của Sếp Vy *"Đủ chuẩn tham gia vào chuỗi cung ứng bán dẫn"* thành Headline quảng cáo chính thức cho phân khúc Nội địa.
* **Điều kiện PASS Closeout:**
  1. File `drafts/S01_Proof_and_Message.md` (Mục phân khúc nội địa) và file `ads/linkedin/LinkedIn_Build_Pack.md` (Ad Copy tiếng Việt) phải có ít nhất 2 biến thể Headline chính thức sử dụng cụm thông điệp: *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"* hoặc *"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"*.
  2. Thông điệp phải làm nổi bật các yêu cầu audit của khách hàng tập đoàn: truy xuất lot, kiểm soát yield & chất lượng, quản lý recipe, đáp ứng audit tiêu chuẩn.
* **Kiểm tra cơ học (Verification command):**
  - Kiểm tra sự xuất hiện của chuỗi `"chuỗi cung ứng bán dẫn"` đi kèm `"đủ chuẩn"` hoặc `"chuẩn hóa"` trong `ads/linkedin/LinkedIn_Build_Pack.md`.

---

### Tiêu chuẩn Closeout 3: GAP-03 & Tiêu chí B1 (Tái cấu trúc LinkedIn Ads thành 2 Campaign song song)
* **Mục tiêu:** Đảm bảo cấu trúc tài khoản đáp ứng trần ngân sách 600.000 VNĐ/ngày (~23 USD/ngày) và điều kiện tối thiểu ~$10/ngày của LinkedIn.
* **Điều kiện PASS Closeout:**
  1. File `ads/linkedin/LinkedIn_Build_Pack.md` phải tái cấu trúc từ "3 ad set theo route" thành **chính xác 2 Campaign song song**:
     - **Campaign 1 (FDI Segment):** Ngân sách 300.000 VNĐ/ngày (~11.5 USD/ngày). Ngôn ngữ: Tiếng Anh (EN) & Tiếng Trung (zh-Hans/zh-Hant). Nhắm mục tiêu: Matched Audience (Company List 100-300 FDI) + Seniority/Function kỹ thuật/vận hành.
     - **Campaign 2 (Domestic Segment):** Ngân sách 300.000 VNĐ/ngày (~11.5 USD/ngày). Ngôn ngữ: Tiếng Việt (VI). Nhắm mục tiêu: Ngành phụ trợ điện tử/bán dẫn + Chức danh (Giám đốc nhà máy, QA/QC, Vận hành, IT) + Loại trừ sinh viên/tìm việc.
  2. Bảng phân bổ ngân sách hiển thị rõ: 300.000 + 300.000 = 600.000 VNĐ/ngày (đáp ứng rule tối thiểu ~10 USD/ngày của LinkedIn).
* **Kiểm tra cơ học (Verification command):**
  - Đếm số lượng campaign trong `LinkedIn_Build_Pack.md` = 2. Tổng ngân sách ngày = 600.000 VNĐ.

---

### Tiêu chuẩn Closeout 4: GAP-04 & Tiêu chí C2 (Lập bảng Calendar Dates ánh xạ 35 ngày paid vào 56 ngày lịch)
* **Mục tiêu:** Khớp nối hoàn hảo lộ trình 4 Phase (7 ngày kỹ thuật, 21 ngày xác nhận, 28 ngày tối ưu) của Sếp Vy trong khung lịch Tháng 10 - Tháng 12 với trần 35 ngày paid của Bảo.
* **Điều kiện PASS Closeout:**
  1. File `drafts/S04_Measurement_and_Budget.md` và/hoặc sheet `02_Lo_trinh` trong Excel phải có bảng đối soát tuần dương lịch:
     - Giai đoạn 1 (Tuần 1 - Tuần 2): Kỹ thuật 7 ngày paid (trong 14 ngày lịch).
     - Giai đoạn 2 (Tuần 3 - Tuần 5): Xác nhận 14 ngày paid (trong 21 ngày lịch).
     - Giai đoạn 3 (Tuần 6 - Tuần 8): Tối ưu 14 ngày paid (trong 21 ngày lịch).
     - Tổng số ngày paid = 7 + 14 + 14 = 35 ngày paid (khớp trần 35.000.000 VNĐ).
     - Tổng thời gian lịch = 56 ngày lịch (8 tuần), kết thúc trước Tết Nguyên đán.
* **Kiểm tra cơ học (Verification command):**
  - Kiểm tra bảng ánh xạ ngày paid và tuần lịch dương trong tài liệu ngân sách và lộ trình.

---

### Tiêu chuẩn Closeout 5: GAP-05 & Tiêu chí D1 (Đồng bộ toàn bộ 28 từ khóa + Brand + Negative vào Excel)
* **Mục tiêu:** Biến sheet `08_Tu_khoa` trong file Excel từ dạng 7 dòng mẫu thành cơ sở dữ liệu từ khóa đầy đủ 100%.
* **Điều kiện PASS Closeout:**
  1. Sheet `08_Tu_khoa` trong `docs/plans/Digiwin_Semiconductor_Theo_doi_ngan_sach.xlsx` phải chứa:
     - Đầy đủ **28 từ khóa ứng viên** từ `drafts/S02_Google_Search_Research.md` chia 4 cụm: Tiếng Việt (VI), Tiếng Anh (EN), Tiếng Trung Giản thể (zh-Hans), Tiếng Trung Phồn thể (zh-Hant).
     - Đầy đủ nhóm từ khóa Thương hiệu (Brand): "Digiwin", "Đỉnh Trí", "Dingjie".
     - Đầy đủ danh mục Negative Keywords (Loại trừ): cổ phiếu, chứng khoán, tuyển dụng, việc làm, khóa học, là gì, luận văn, pdf, v.v.
     - Volume đối soát trung thực: Ghi rõ số liệu hoặc đánh dấu rõ ràng `no displayed data` (dấu gạch ngang từ Google Keyword Planner), tuyệt đối không bịa số.
* **Kiểm tra cơ học (Verification command):**
  - Chạy script Python đọc OpenPyXL kiểm tra sheet `08_Tu_khoa`: Số dòng từ khóa >= 28 + nhóm Brand + nhóm Negative (tổng số dòng dữ liệu > 35 dòng).

---

## 2. Quy Trình Vận Hành & Nghiệm Thu (Coordinator Gate)

1. **Commit Checkpoint Tiêu Chuẩn:** Coordinator commit file này vào branch `slice/audit-automation-artifacts` để làm cơ sở pháp lý.
2. **Spawn Subagent:** Coordinator spawn các Writer Subagent (Model `flash`) để tiến hành cập nhật sửa đổi đúng theo 5 tiêu chuẩn trên.
3. **Auditing & Verification:** Coordinator chạy script kiểm tra cơ học và đọc diff thực tế của các file được chỉnh sửa.
4. **Final PASS Sign-off:** Khi tất cả 5 tiêu chuẩn đều thỏa mãn điều kiện cơ học, Coordinator cập nhật trạng thái audit report từ `PARTIAL ACCEPTANCE` thành `FULL PASS CLOSEOUT` và báo cáo anh Bảo.
