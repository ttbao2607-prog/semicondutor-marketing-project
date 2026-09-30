# TIÊU CHUẨN ĐÓNG PASS CLOSEOUT CHO CÁC TIÊU CHÍ PARTIAL (CLOSEOUT ACCEPTANCE CONTRACT)
**Worktree:** `D:\Digiwin_Semiconductor_Audit_Worktree`  
**Branch:** `slice/audit-automation-artifacts`  
**Ngày lập:** 2026-09-30  
**Người phê duyệt / Product Owner:** Bảo  
**Người điều phối / Coordinator:** Antigravity Coordinator (AGY)  
**Mục tiêu:** Định nghĩa chuẩn xác nhận nghiệm thu đóng (PASS Closeout Criteria) cho 5 tiêu chí còn ở mức `PARTIAL` (A1, A2, B1, C2, D1) tương ứng với 5 Actionable GAPs đã ghi nhận trong Báo cáo Kiểm toán `AUTOMATION_ARTIFACTS_AUDIT_REPORT_2026-09-30.md`. Bất kỳ Subagent nào thực thi sửa đổi phải đáp ứng đầy đủ điều kiện nghiệm thu cơ học dưới đây trước khi Coordinator ký PASS.

---

## 1. Bảng Tiêu Chuẩn Nghiệm Thu Closeout Chi Tiết

### Tiêu chuẩn Closeout 1: GAP-01 & Tiêu chí A1 (Hoàn thiện hồ sơ đề xuất loại trừ đại tập đoàn trong ICP - Chờ PO phê duyệt)
* **Mục tiêu:** Xây dựng phương án đề xuất kinh doanh chi tiết (Decision Pack) về việc loại trừ 4 đại tập đoàn và tập trung chuỗi phụ trợ, sẵn sàng trình Product Owner Bảo phê duyệt (L2); không tự ý biến proposal thành approved decision khi chưa có mandate.
* **Căn cứ & Gate phê duyệt:**
  - **PO Approval Gate (Bắt buộc):** Quyết định D1 thuộc thẩm quyền kinh doanh của PO Bảo (`AGENTS.md`). Kiểm tra chuỗi văn bản thuần túy không chứng minh sự đồng thuận kinh doanh. Bất kỳ tài liệu chiến lược hay targeting nào chỉ được chuyển trạng thái sang `APPROVED` sau khi có evidence phê duyệt trực tiếp bằng văn bản từ Bảo.
  - Khi chưa có quyết định phê duyệt: Các tài liệu phải thể hiện rõ ràng đây là **phương án dự thảo / đề xuất kỹ thuật (Proposal / Working Draft)**.
* **Điều kiện hoàn thiện hồ sơ đề xuất:**
  1. File `drafts/S01_Proof_and_Message.md` phải trình bày phương án rõ ràng: Khảo sát và đề xuất loại trừ 4 đại tập đoàn có hệ thống sản xuất chung toàn cầu (Intel, Samsung, Hana Micron, Amkor), kèm trạng thái `proposal / pending PO approval`.
  2. Định hướng đề xuất tập trung 100% vào chuỗi cung ứng & công nghiệp phụ trợ: PCB, Substrate, Vật liệu đóng gói, Linh kiện, Gia công cơ khí chính xác cho thiết bị bán dẫn.
  3. File `ads/linkedin/LinkedIn_Build_Pack.md` phải có dòng cấu hình nhắm mục tiêu dự thảo: `Excluded Companies (Proposed): Intel, Samsung Electronics, Hana Micron, Amkor Technology` trong bảng thiết lập Campaign/Ad set, ghi chú rõ chờ quyết định phê duyệt của Bảo trước khi import lên Ads Manager.
* **Kiểm tra cơ học & Gate check:**
  - Kiểm tra tính nhất quán giữa `drafts/S01_Proof_and_Message.md` và `ads/linkedin/LinkedIn_Build_Pack.md` về trạng thái proposal của danh sách Excluded Companies.
  - Bắt buộc kiểm tra evidence xác nhận từ Bảo trước khi ký CLOSEOUT ở cấp độ kinh doanh.

---

### Tiêu chuẩn Closeout 2: GAP-02 & Tiêu chí A2 (Bổ sung Headline tiếng Việt nội địa chuyên sâu)
* **Mục tiêu:** Đưa thông điệp của Sếp Vy *"Đủ chuẩn tham gia vào chuỗi cung ứng bán dẫn"* thành Headline quảng cáo chính thức cho phân khúc Nội địa.
* **Điều kiện PASS Closeout:**
  1. File `drafts/S01_Proof_and_Message.md` (Mục phân khúc nội địa) và file `ads/linkedin/LinkedIn_Build_Pack.md` (Ad Copy tiếng Việt) phải có ít nhất 2 biến thể Headline chính thức sử dụng cụm thông điệp: *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"* hoặc *"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"*.
  2. Thông điệp phải làm nổi bật các yêu cầu audit của khách hàng tập đoàn: truy xuất lot, kiểm soát yield & chất lượng, quản lý recipe, đáp ứng audit tiêu chuẩn.
* **Kiểm tra cơ học (Verification command):**
  - Kiểm tra sự xuất hiện của chuỗi `"chuỗi cung ứng bán dẫn"` đi kèm `"đủ chuẩn"` hoặc `"chuẩn hóa"` trong `ads/linkedin/LinkedIn_Build_Pack.md`.

---

### Tiêu chuẩn Closeout 3: GAP-03 & Tiêu chí B1 (Hoàn thiện phương án đề xuất cấu trúc LinkedIn Ads 2 Campaign song song - Chờ PO phê duyệt)
* **Mục tiêu:** Xây dựng phương án cấu trúc tài khoản giải quyết bài toán trần ngân sách 600.000 VNĐ/ngày (~23 USD/ngày) và điều kiện sàn ~$10/ngày của LinkedIn, sẵn sàng trình Bảo duyệt.
* **Căn cứ & Gate phê duyệt:**
  - Cấu trúc tài khoản và phân bổ ngân sách kênh LinkedIn cần PO Bảo phê duyệt chính thức trước khi triển khai trực tiếp.
* **Điều kiện hoàn thiện hồ sơ đề xuất:**
  1. File `ads/linkedin/LinkedIn_Build_Pack.md` tái cấu trúc rõ ràng thành **phương án 2 Campaign song song**:
     - **Campaign 1 (FDI Segment):** Đề xuất 300.000 VNĐ/ngày (~11.5 USD/ngày). Ngôn ngữ: Tiếng Anh (EN) & Tiếng Trung (zh-Hans/zh-Hant). Nhắm mục tiêu: Matched Audience (Company List 100-300 FDI) + Seniority/Function kỹ thuật/vận hành.
     - **Campaign 2 (Domestic Segment):** Đề xuất 300.000 VNĐ/ngày (~11.5 USD/ngày). Ngôn ngữ: Tiếng Việt (VI). Nhắm mục tiêu: Ngành phụ trợ điện tử/bán dẫn + Chức danh (Giám đốc nhà máy, QA/QC, Vận hành, IT) + Loại trừ sinh viên/tìm việc.
  2. Bảng phân bổ ngân sách hiển thị rõ ràng phương án: 300.000 + 300.000 = 600.000 VNĐ/ngày (đáp ứng rule tối thiểu ~10 USD/ngày của LinkedIn), ghi chú rõ ràng trạng thái "Đề xuất chờ Bảo duyệt".
* **Kiểm tra cơ học (Verification command):**
  - Đếm số lượng campaign trong `LinkedIn_Build_Pack.md` = 2. Tổng ngân sách ngày đề xuất = 600.000 VNĐ.

---

### Tiêu chuẩn Closeout 4: GAP-04 & Tiêu chí C2 (Lập phương án đề xuất Calendar Dates ánh xạ 35 ngày paid vào 56 ngày lịch - Chờ PO phê duyệt)
* **Mục tiêu:** Xây dựng mô hình khớp nối lộ trình 4 Phase (7 ngày kỹ thuật, 21 ngày xác nhận, 28 ngày tối ưu) của Sếp Vy trong khung lịch Tháng 10 - Tháng 12 với trần 35 ngày paid của Bảo, sẵn sàng trình phê duyệt.
* **Căn cứ & Gate phê duyệt:**
  - Quy định ngày nghỉ đối soát và phân bổ ngày paid theo tuần là phương án vận hành kỹ thuật, không tự ý áp đặt làm quy định bắt buộc khi Bảo chưa chuẩn thuận.
* **Điều kiện hoàn thiện hồ sơ đề xuất:**
  1. File `drafts/S04_Measurement_and_Budget.md` và/hoặc sheet `02_Lo_trinh` trong Excel có bảng đối soát tuần dương lịch chi tiết dạng đề xuất kỹ thuật:
     - Giai đoạn 1 (Tuần 1 - Tuần 2): Kỹ thuật 7 ngày paid (trong 14 ngày lịch).
     - Giai đoạn 2 (Tuần 3 - Tuần 5): Xác nhận 14 ngày paid (trong 21 ngày lịch).
     - Giai đoạn 3 (Tuần 6 - Tuần 8): Tối ưu 14 ngày paid (trong 21 ngày lịch).
     - Tổng số ngày paid = 7 + 14 + 14 = 35 ngày paid (khớp trần 35.000.000 VNĐ).
     - Tổng thời gian lịch = 56 ngày lịch (8 tuần), kết thúc trước Tết Nguyên đán.
* **Kiểm tra cơ học (Verification command):**
  - Kiểm tra bảng ánh xạ ngày paid và tuần lịch dương trong tài liệu ngân sách và lộ trình, bảo đảm ghi rõ trạng thái đề xuất kỹ thuật.

---

### Tiêu chuẩn Closeout 5: GAP-05 & Tiêu chí D1 (Đồng bộ toàn bộ 28 từ khóa + Brand + Negative vào Excel với phân loại evidence chuẩn xác)
* **Mục tiêu:** Hoàn thiện sheet `08_Tu_khoa` trong file Excel thành cơ sở dữ liệu từ khóa đầy đủ 100%, phân loại trung thực evidence theo đúng nguyên tắc kiểm toán.
* **Điều kiện hoàn thành:**
  1. Sheet `08_Tu_khoa` trong `docs/plans/Digiwin_Semiconductor_Theo_doi_ngan_sach.xlsx` phải chứa:
     - Đầy đủ **28 từ khóa ứng viên** từ `drafts/S02_Google_Search_Research.md` chia 4 cụm: Tiếng Việt (VI), Tiếng Anh (EN), Tiếng Trung Giản thể (zh-Hans), Tiếng Trung Phồn thể (zh-Hant).
     - Đầy đủ nhóm từ khóa Thương hiệu (Brand): "Digiwin", "Đỉnh Trí", "Dingjie".
     - Đầy đủ danh mục Negative Keywords (Loại trừ): cổ phiếu, chứng khoán, tuyển dụng, việc làm, khóa học, là gì, luận văn, pdf, v.v.
     - **Phân loại Volume trung thực theo evidence:**
       * Đối với các từ khóa ứng viên chưa thực hiện truy vấn: Ghi nhận rõ ràng `Unknown / Not queried` (hoặc cấu hình `Not queried`), tuyệt đối không gán nhầm dấu gạch ngang `- (no displayed data)` của Google Keyword Planner.
       * Đối với truy vấn thực tế đã quan sát ngày 2026-09-14 (`electronics manufacturing ERP`): Giữ nguyên số liệu quan sát `10` và ghi nhận cấu hình Planner thực tế.
       * Đối với từ khóa loại trừ (Negative): Ghi nhận `N/A (Negative)`.
* **Kiểm tra cơ học (Verification command):**
  - Chạy script Python đọc OpenPyXL kiểm tra sheet `08_Tu_khoa`: Số dòng dữ liệu >= 56 dòng, xác thực các cell volume được phân loại chính xác giữa `Unknown / Not queried`, `10`, và `N/A (Negative)`.

---

## 2. Quy Trình Vận Hành & Nghiệm Thu (Coordinator Gate & PO Approval)

1. **Chuẩn bị và hoàn thiện hồ sơ kỹ thuật:** Các Writer hoàn thiện các tài liệu, cấu hình build pack và workbook theo các tiêu chuẩn kỹ thuật trên.
2. **Kiểm tra cơ học độc lập:** Coordinator chạy script kiểm tra cơ học, đối soát cấu trúc file, kiểm tra tính toàn vẹn công thức Excel và cú pháp Markdown.
3. **Phân định rõ ràng giữa Kỹ thuật (Technical Readiness) và Quyết định kinh doanh (Business Approval):**
   - Việc vượt qua kiểm tra cơ học chỉ chứng nhận tài liệu **SẴN SÀNG TRÌNH PHÊ DUYỆT (Proposal Ready / Technical Pass)**.
   - **Tuyệt đối không tự ý ký "FULL PASS CLOSEOUT" khi chưa có phê duyệt trực tiếp của Product Owner Bảo.** Các quyết định chiến lược như: loại trừ 4 đại tập đoàn (D1), trần và phân bổ ngân sách 600k/250k, cấu trúc campaign song song và ngày nghỉ đối soát bắt buộc phải có evidence phê duyệt bằng văn bản từ Bảo.
4. **Báo cáo và trình duyệt:** Coordinator tổng hợp báo cáo kiểm toán, nêu rõ trạng thái thực tế (đề xuất đã hoàn thiện vs quyết định đã được duyệt), giữ diff minh bạch và trình PO Bảo xem xét quyết định.
