# KẾ HOẠCH TỔNG HỢP BÁO CÁO CẤP QUẢN LÝ (EXECUTIVE REPORTING SYNTHESIS PLAN)
**Dự án:** Semiconductor Paid Workspace — Chiến dịch Tiếp thị Số Bán Dẫn Digiwin  
**Worktree:** `D:\Digiwin_Semiconductor_Audit_Worktree`  
**Nhánh Git:** `slice/executive-reporting-pack`  
**Commit Gốc:** `9d1adc6` (Reconciled Audit & Technical Base)  
**Ngày lập:** 2026-09-30  
**Người lập kế hoạch / Coordinator:** Antigravity Coordinator (AGY)  
**Product Owner:** Bảo  

---

## 1. Bối Cảnh & Mục Tiêu

Hệ thống tài liệu và code hiện tại trong workspace (`S01`, `S04`, `Build Pack`, `Audit Reports`, `Excel 11 sheets`) được xây dựng chuyên sâu cho góc nhìn **kỹ thuật & vận hành nội bộ** (Technical & Operational Invariants). 

Mục tiêu của kế hoạch này là **chuyển hóa toàn bộ khối dữ liệu kỹ thuật và kết quả audit thành 2 bộ báo cáo quản lý (2-Tier Executive Decision Pack)**:
1. **Tier 1 (Báo cáo Chiến lược cho Regional CMO / Ban Giám Đốc Vùng):** Cung cấp bức tranh toàn cảnh (Strategic Big Picture), luận giải tính khả thi kinh doanh, cơ chế bảo toàn vốn (Capital Preservation), lộ trình thử nghiệm 8 tuần và các quyết định Go / No-Go cấp cao.
2. **Tier 2 (Báo cáo Đề xuất Thực thi cho Sếp Vy - Direct Marketing Manager):** Phản hồi chi tiết và chuẩn hóa các chỉ đạo trong email ngày 2026-09-29 của Sếp Vy (ngân sách 600k/250k, 2 campaign song song FDI vs Nội địa, thông điệp "Đủ chuẩn tham gia chuỗi cung ứng bán dẫn", đối soát lịch 8 tuần / 35 ngày paid, quy tắc underspend và tính trung thực của search volume).

---

## 2. Cấu Trúc Hai Bộ Tài Liệu Executive

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   HỒ SƠ TRÌNH DUYỆT CẤP QUẢN LÝ (EXECUTIVE PACK)                       │
├──────────────────────────────────────────┬─────────────────────────────────────────────┤
│ 1. TIER 1: REGIONAL CMO BRIEF             │ 2. TIER 2: SẾP VY OPERATIONAL PROPOSAL      │
│ (Chiến lược, Vốn, Thị trường, Quyết định) │ (Cấu trúc Campaign, Copy, Phasing, Ngân sách)│
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ • File: `docs/exec/CMO_STRATEGIC_BRIEF.md`│ • File: `docs/exec/VY_OPERATIONAL_PLAN.md`  │
│ • Độ dài: 1-2 trang A4 / 4-5 slides tóm tắt│ • Độ dài: 3-4 trang chi tiết nghiệp vụ      │
│ • Khán giả: Regional CMO, C-level        │ • Khán giả: Sếp Vy (Marketing Manager)      │
│ • Trọng tâm:                             │ • Trọng tâm:                                │
│   - Tại sao là Bán dẫn & Lúc này?        │   - Đối chiếu chỉ đạo email 2026-09-29      │
│   - Cơ chế bảo vệ ngân sách (Trần 35M)   │   - 2 Campaign LinkedIn (FDI vs Nội địa)    │
│   - Khung thời gian: 8 tuần trước Tết    │   - Thông điệp vendor audit tiếng Việt      │
│   - KPI: Không chạy theo lead rác         │   - Lịch 35 ngày paid / 56 ngày lịch        │
│   - 3 Quyết định Go/No-Go cần ký         │   - Quy tắc underspend & Volume trung thực  │
└──────────────────────────────────────────┴─────────────────────────────────────────────┘
```

---

## 3. Nội Dung Chi Tiết Từng Tài Liệu

### 3.1. Tài liệu 1: `docs/exec/CMO_STRATEGIC_BRIEF.md` (Dành cho Regional CMO)

* **Phần 1: Executive Summary & Strategic Rationale (Tại sao là Bán dẫn?):**
  - Cơ hội làn sóng dịch chuyển bán dẫn vào Việt Nam (sản xuất chip, kiểm thử đóng gói OSAT, thiết kế vi mạch Fabless, và đặc biệt là chuỗi cung ứng linh kiện phụ trợ).
  - Vị thế Digiwin: Đã có năng lực thực tế về MES/ERP công nghiệp điện tử tại Đài Loan/Trung Quốc và một số nhà máy phụ trợ tại Việt Nam; cần xác lập vị thế thương hiệu đón đầu chu kỳ 2026–2027.
* **Phần 2: Budget Envelope & Capital Preservation Rule (Kiểm soát rủi ro tài chính):**
  - **Trần ngân sách Cấp 1 cam kết:** **35.000.000 VNĐ** (~1,350 USD) cho toàn bộ đợt thử nghiệm.
  - **Nguyên tắc Bảo toàn vốn (Capital Guard):** Áp dụng cơ chế **Underspend Protection** — Không ép tiêu hết ngân sách ngày; nếu nhu cầu tìm kiếm thực tế thấp, giữ nguyên tiền trong tài khoản, tuyệt đối không mở rộng từ khóa ngoài ngành để tiêu tiền vô ích.
* **Phần 3: Pilot Roadmap & Phasing (Khung thời gian 8 tuần):**
  - 8 tuần lịch dương (Tháng 10 - Tháng 12/2026), kết thúc nghiệm thu và đóng chiến dịch trước Tết Nguyên Đán.
  - Phân bổ thông minh: Tối đa 35 ngày chạy quảng cáo (paid days) xen kẽ các ngày nghỉ đối soát kỹ thuật (pause days) để phân tích chất lượng dữ liệu.
* **Phần 4: High-Level Success Metrics (KPI Đo lường giá trị thực):**
  - Không cam kết và không đánh giá trên số lượng form thô (Raw Leads) để tránh rác.
  - Đánh giá dựa trên: Tỷ lệ thâm nhập tệp tài khoản mục tiêu (Target Account Reach >= 60%), Tỷ lệ tương tác sâu trên Landing Page (Engaged Sessions >= 50%), và Tỷ lệ chuyển đổi nhu cầu thực tế (Effective Lead Rate).
* **Phần 5: Decision Request (Điểm xin phê duyệt của CMO):**
  1. Phê duyệt hạn mức ngân sách thử nghiệm Giai đoạn 1: **35.000.000 VNĐ**.
  2. Phê duyệt nguyên tắc định vị: Tập trung vào phân khúc Nhà máy FDI và Doanh nghiệp phụ trợ nội địa; loại trừ 4 đại tập đoàn có hệ thống toàn cầu đóng kín (Intel, Samsung, Hana Micron, Amkor).
  3. Phê duyệt triển khai bộ tài nguyên đa ngôn ngữ (Landing Page & Creative 4 locales).

---

### 3.2. Tài liệu 2: `docs/exec/VY_OPERATIONAL_PLAN.md` (Dành cho Sếp Vy)

* **Phần 1: Ma trận Phản hồi & Tiếp thu Chỉ đạo Email 2026-09-29:**
  - Bảng đối soát từng chỉ đạo của Sếp Vy (Ngân sách ngày, cấu trúc chiến dịch, thông điệp phụ trợ, lộ trình tuần, search term audit) và giải pháp kỹ thuật tương ứng đã hoàn thiện.
* **Phần 2: Cấu trúc Chiến dịch LinkedIn Ads (2 Parallel Campaigns - 600k/ngày):**
  - Giải quyết triệt để bài toán sàn chi tiêu LinkedIn (~$10/ngày) bằng cách tái cấu trúc thành đúng 2 Campaign song song:
    * **Campaign 1 (FDI Segment - `LI-CMP-FDI-SEGMENT`):** 300.000 VNĐ/ngày. Nhắm 100–300 nhà máy FDI qua Company List + Job Function kỹ thuật/vận hành (EN, zh-Hans, zh-Hant).
    * **Campaign 2 (Domestic Segment - `LI-CMP-DOMESTIC-SEGMENT`):** 300.000 VNĐ/ngày. Nhắm các doanh nghiệp phụ trợ nội địa (PCB, Substrate, Cơ khí chính xác, Vật liệu) qua Job Titles cấp quản lý (VI).
* **Phần 3: Chiến lược Thông điệp & Bộ Copy "Đủ chuẩn tham gia chuỗi cung ứng bán dẫn":**
  - Thiết kế 2 biến thể Headline chính thức cho phân khúc nội địa:
    * *Biến thể 1:* **"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"** (Nhấn mạnh năng lực đạt chuẩn vendor).
    * *Biến thể 2:* **"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"** (Nhấn mạnh vượt qua audit của khách hàng tập đoàn).
  - Làm nổi bật 4 bài toán kỹ thuật mà vendor phụ trợ bắt buộc phải giải quyết: Truy xuất lot (Lot Traceability), Kiểm soát yield & chất lượng SPC, Quản lý recipe thiết bị, Báo cáo audit tức thì.
* **Phần 4: Kế hoạch Google Search Ads & Trung thực Báo cáo Volume (250k/ngày):**
  - Ngân sách đề xuất: 250.000 VNĐ/ngày.
  - Báo cáo trung thực kết quả Keyword Planner: Đa số từ khóa OSAT/Fabless tại Việt Nam hiển thị dấu gạch ngang (không có dữ liệu lịch sử); duy nhất 1 cụm có volume 10 searches/tháng.
  - Giải pháp: Chạy 28 từ khóa tuyển chọn chia 4 cụm ngôn ngữ + Brand Digiwin, kết hợp danh mục 24 từ khóa phủ định (Negative) chặn rác tuyển dụng/chứng khoán; tiền không tiêu hết sẽ giữ lại (underspend).
* **Phần 5: Lịch Trình Đối Soát 8 Tuần Lịch (56 Ngày Lịch / 35 Ngày Paid):**
  - Lập bảng ánh xạ chi tiết theo từng tuần từ Tuần 1 (Tháng 10) đến Tuần 8 (Tháng 12):
    * *Phase 1 (Tuần 1–2):* 7 ngày paid (trong 14 ngày lịch) — Khởi động kỹ thuật & rà soát dữ liệu.
    * *Phase 2 (Tuần 3–5):* 14 ngày paid (trong 21 ngày lịch) — Xác nhận mức độ tương tác & thu thập tối thiểu 20 clicks search terms phân loại.
    * *Phase 3 (Tuần 6–8):* 14 ngày paid (trong 21 ngày lịch) — Tối ưu hóa chuyển đổi, tổng kết trước Tết.
  - Tổng số ngày paid = 35 ngày (khớp trần 35M); số ngày nghỉ đối soát = 21 ngày.
* **Phần 6: Sẵn Sàng Kỹ Thuật (Landing Page & Tracking):**
  - Xác nhận 3 Landing Page canonical (OSAT, Fabless, Partner) đã hoàn tất tích hợp bộ chuyển đổi 4 ngôn ngữ mượt mà.
  - Bảo toàn 100% invariants: Không chứa form thô, Partner đúng 1 CTA header, tracking band đo lường chuẩn xác, 12/12 unit tests pass.

---

## 4. Chuẩn PASS & Tiêu Chí Kiểm Toán Đóng (Audit Acceptance Gates)

Để đảm bảo sau khi viết xong, 2 tài liệu này đạt chất lượng cao nhất và sẵn sàng trình bày ngay, việc kiểm toán sẽ đối soát theo 5 tiêu chuẩn PASS sau:

| Mã Gate | Tên Tiêu Chuẩn Nghiệm Thu | Điều Kiện Đạt Chuẩn (PASS Invariants) |
|:---:|---|---|
| **GATE-01** | **Executive Tone & Separation** | Bản CMO không chứa thuật ngữ lập trình/DOM/CSS/regex; tập trung vào P&L, thị trường, rủi ro và quyết định. Bản Vy tập trung vào logic triển khai, cấu trúc ad set, copy và phasing. |
| **GATE-02** | **Budget & Number Integrity** | Khớp số liệu 100%: Trần Cấp 1 = 35.000.000 VNĐ; Phân bổ ngày đề xuất: LinkedIn 600k (300k/300k), Search 250k, Reserve 150k. Tổng số ngày paid = 35 ngày, tổng thời gian lịch = 56 ngày (8 tuần). |
| **GATE-03** | **Campaign & Naming Alignment** | Định danh campaign khớp chính xác với Build Pack: `LI-CMP-FDI-SEGMENT` và `LI-CMP-DOMESTIC-SEGMENT`. Tên riêng đối tác nội địa giữ nguyên tiếng Việt (`Khang Đạt`, `Nhật Tân`, `Phẩm Thuyên`, `Pinquan`). |
| **GATE-04** | **Honest Evidence Classification** | Không tự ý tuyên bố volume tìm kiếm là cao; ghi nhận trung thực hiện trạng thiếu dữ liệu tìm kiếm hiển thị của Google Keyword Planner. Các nội dung chiến lược D1, ngân sách, ngày nghỉ đều ghi rõ là `đề xuất dự thảo (proposal)` chờ phê duyệt. |
| **GATE-05** | **Actionable Decision Request** | Cuối mỗi tài liệu phải có danh mục các điểm đề xuất hành động cụ thể (Call to Action / Decision Points) để người đọc ký duyệt hoặc phản hồi ngay, không để tình trạng lơ lửng. |

---

## 5. Lộ Trình Triển Khai (Execution Steps)

1. **Bước 1 (Soạn thảo):** Viết file `docs/exec/CMO_STRATEGIC_BRIEF.md`.
2. **Bước 2 (Soạn thảo):** Viết file `docs/exec/VY_OPERATIONAL_PLAN.md`.
3. **Bước 3 (Self-Audit):** Chạy kiểm tra đối soát 5 Gate nghiệm thu (Gate 1 đến Gate 5).
4. **Bước 4 (Báo cáo):** Tổng hợp diff và báo cáo Bảo kiểm tra trước khi tạo commit checkpoint trên branch `slice/executive-reporting-pack`.
