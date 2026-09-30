# AUDIT REQUIREMENT SPECIFICATION & EVALUATION RUBRIC
**Slice:** `slice/audit-automation-artifacts`  
**Ngày lập:** 2026-09-30  
**Người phê duyệt / Product Owner:** Bảo  
**Người điều phối / Lead Auditor:** Antigravity Coordinator (AGY)  
**Mục tiêu:** Thiết lập khung chuẩn đối chiếu (Audit Criteria & Acceptance Rubric) để audit toàn bộ các artifact được tạo ra từ chuỗi automation agent, đối chiếu trực tiếp với email chỉ đạo từ Sếp Vy và các chỉ đạo canonical của Bảo.

---

## 1. Nguồn Chỉ Đạo & Thứ Tự Ưu Tiên (Source Hierarchy)
1. Chỉ đạo trực tiếp của Bảo (Product Owner).
2. Email chỉ đạo/đóng góp của Sếp Vy (2026-09-29).
3. `Semiconductor_Work_Kickoff.md` v2.0 & `CURRENT_STATE.md`.
4. Design System & Tracking Contract (`MASTER.md`, `Semiconductor_Tracking_Contract.md`).

---

## 2. Danh Mục Các Trọng Điểm Kiểm Toán (5 Nhóm Tiêu Chí)

### Trọng điểm A: Định hướng ngành & Khách hàng mục tiêu (ICP & Target Accounts)
- [ ] **A1 (Định nghĩa ngành bán dẫn của Digiwin):**
  - Đã loại trừ / hạ ưu tiên các đại tập đoàn có hệ thống ERP/MES toàn cầu (Intel, Amkor, Hana Micron, Samsung) hay chưa?
  - Trọng tâm có đúng vào chuỗi cung ứng bán dẫn & điện tử phụ trợ: PCB, substrate, linh kiện, vật liệu đóng gói, gia công cơ khí chính xác cho thiết bị bán dẫn hay không?
- [ ] **A2 (Phân khúc FDI vs Nội địa):**
  - Có tách biệt rõ rệt 2 segment: FDI (Đài Loan/Trung Quốc) và Nội địa (Việt Nam) trong chiến lược và thông điệp không?
  - FDI: Nhắm theo Company List (100–300 công ty), thông điệp chuyên sâu kỹ thuật & quản trị (lot trace, yield, recipe, customer audit, ISO/chuẩn chuỗi cung ứng)?
  - Nội địa: Nhắm theo Industry/Job title, thông điệp trọng tâm: *"Đủ chuẩn tham gia vào chuỗi cung ứng bán dẫn"*?
- [ ] **A3 (Bảo vệ dữ liệu & Schema Audience):**
  - Tệp 100–300 công ty từ Lark / KCN có được thể hiện dưới dạng schema/metadata sanitized không? (Tuyệt đối không rò rỉ PII, phone, email cá nhân hoặc tài liệu mật lên git).

### Trọng điểm B: Cấu trúc Kênh, Quảng cáo & Ngân sách (Channels & Budget)
- [ ] **B1 (LinkedIn Ads Architecture & Budget):**
  - Ngân sách: Khóa cứng mức **600.000 VNĐ/ngày** (~23 USD/ngày).
  - Cấu trúc: Tối đa **2 campaign song song** (đảm bảo rule tối thiểu ~10 USD/ngày của LinkedIn: 1 FDI theo Company list, 1 Nội địa theo Job title).
  - Đã chuẩn bị quy định cài **LinkedIn Insight Tag** và Matched Audience từ Day 1 chưa?
  - Creative có đủ 4 locale (`vi`, `en`, `zh-Hans`, `zh-Hant`) cho các format (Static, Square, Carousel, Document PDF) chưa? CAR-03 có bị vi phạm bản quyền/claim khống không?
- [ ] **B2 (Google Search Ads Architecture & Budget):**
  - Ngân sách: Khóa cứng mức **250.000 VNĐ/ngày**.
  - Nguyên tắc điều phối: Nếu volume thấp, tuyệt đối không nới rộng từ khóa rác chỉ để tiêu hết tiền; có cơ chế xem xét chuyển phần dư sang LinkedIn.
  - Cài **Google Remarketing tag** từ Day 1.
  - Danh sách từ khóa: Đã chia thành 3 cụm ngôn ngữ (Tiếng Việt cho nội địa; Tiếng Anh & Tiếng Trung cho FDI) + 1 Ad group Brand *"Digiwin"*?
  - Có volume đối soát từ Keyword Planner (hoặc ghi rõ trạng thái `no displayed data` trung thực, không bịa số liệu)?
  - Danh sách Negative Keywords: Đã chặn triệt để intent rác: cổ phiếu, chứng khoán, tuyển dụng, việc làm, khóa học, là gì, luận văn, pdf...?
- [ ] **B3 (Tổng ngân sách & Kịch bản):**
  - Tổng ngân sách tới hết Mở rộng cấp 1: **35.000.000 VNĐ**.
  - Cấp 2 dự phòng: **43.750.000 VNĐ** (tách riêng, cần phê duyệt sau).
  - Có dự phòng phương án ngân sách thấp hơn 1 tr/ngày (LinkedIn chạy FDI, Google Search chạy VI, hoặc chạy luân phiên)?

### Trọng điểm C: Lộ trình Triển khai & Phasing (Roadmap & Milestones)
- [ ] **C1 (Khung thời gian):**
  - Cam kết tối thiểu **8 tuần lịch (56 ngày lịch)**, rà soát hàng tuần, ra quyết định theo tháng.
  - Lịch chạy: Tháng 10 – Tháng 12, đánh giá kết thúc trước Tết Nguyên đán.
  - Tách bạch: 56 ngày lịch **không đồng nghĩa** với 56 ngày paid (tối đa ~35 ngày paid nếu chạy ngân sách trần 1 tr/ngày).
- [ ] **C2 (Các pha triển khai):**
  - Phase 1: Thử nghiệm kỹ thuật (7 ngày) — kiểm tra tracking, search term, pixel phân phối đúng tệp.
  - Phase 2: Xác nhận (21 ngày).
  - Phase 3: Tối ưu (4 tuần) — thay vì 2 chu kỳ 7 ngày ngắn.
  - Phase 4: Đánh giá xét Cấp 2.
  - Tiêu chí đánh giá kỹ thuật: Đánh giá search terms trên tổng thể kỳ quan sát (search terms report), không kết luận vội vàng dựa trên mẫu quá nhỏ (như 7/10 clicks).

### Trọng điểm D: Cấu trúc & Chất lượng File Excel Quản Lý (`.xlsx`)
- [ ] **D1 (Bảo toàn 7 sheet gốc & Thêm 4 sheet mới theo yêu cầu của Sếp Vy):**
  - Kiểm tra xem workbook có đầy đủ 11 sheet hay không?
  - Sheet thêm 1 (`07_Kenh_ngay` / Daily breakdown): Có đủ các cột: *Impression, Reach, Click, CTR, CPM/CPC, Engaged Sessions, Lead thô, Lead hợp lệ* theo từng kênh không?
  - Sheet thêm 2 (`08_Tu_khoa` / Keywords & Negatives): Có danh sách 3 ngôn ngữ (VI/EN/ZH) + Brand + Danh sách loại trừ không?
  - Sheet thêm 3 (`09_Audience_schema` / Target accounts): Có cấu trúc schema cho 100–300 công ty mục tiêu, phân loại FDI/Nội địa không?
  - Sheet thêm 4 (`10_KPI_dictionary` / KPI definitions): Định nghĩa rõ công thức, nguồn dữ liệu, baseline?
- [ ] **D2 (Toàn vẹn kỹ thuật):**
  - Không phá vỡ công thức tính toán ở các sheet tổng quan, chi tiêu, lộ trình.
  - Dữ liệu minh họa là mock/sanitized data, không chứa PII hoặc dữ liệu nhạy cảm.

### Trọng điểm E: Khung Đo Lường & KPI Chốt Trước Launch (Measurement & KPI Baseline)
- [ ] **E1 (Chốt KPI trước khi chạy):**
  - **LinkedIn:** Tỷ lệ hiển thị đúng công ty/chức năng/cấp bậc; Reach trong company list; Tần suất; CTR / Engagement.
  - **Google Search:** Core keyword impression share; Tỷ lệ search terms đúng chủ đề; Số phiên có tương tác (engaged sessions) trên Landing Page.
  - **Nhận diện (Brand awareness):** Đo baseline trước launch (lượng tìm kiếm "Digiwin", direct traffic, LinkedIn followers từ target accounts).
  - **Lead Management:** Tách biệt rõ ràng **Effective Lead Rate** (lead hợp lệ, đã xác minh) và Form thô (chỉ mang tính tham khảo, không ép KPI ở giai đoạn 1).
- [ ] **E2 (Landing Page & Tracking Invariants):**
  - Ba route HTML (OSAT, Fabless, Partner) giữ nguyên tính độc lập, hỗ trợ 4 locale (`vi`, `en`, `zh-Hans`, `zh-Hant`) qua tham số URL `lang=...`.
  - Giữ nguyên số lượng và ID của CTA: OSAT (2 CTA), Fabless (2 CTA), Partner (1 CTA duy nhất tại Header: `partner-cta-header`, loại bỏ hoàn toàn nút cam).
  - Không chứa form submit trực tiếp trong HTML source; giữ provider-free cho đến khi PopupX được tích hợp đúng quy trình.

---

## 3. Thang Đánh Giá & Phân Loại Kết Quả (Audit Verdict Rubric)
Mỗi artifact hoặc nhóm artifact sẽ được gán 1 trong các mức:
- `PASS` (Đạt đầy đủ, có bằng chứng đối soát khớp 100% với yêu cầu).
- `PARTIAL` (Đã cấu trúc đúng nhưng còn thiếu chi tiết nhỏ hoặc cần bổ sung dữ liệu offline).
- `FAIL` (Sai lệch nghiêm trọng so với chỉ đạo: sai ngân sách, sai cấu trúc campaign, lộ PII, vi phạm invariant CTA...).
- `BLOCKED / UNKNOWN` (Thiếu căn cứ thực tế từ tài khoản/nền tảng).
