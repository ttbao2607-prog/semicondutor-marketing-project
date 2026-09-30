# BÁO CÁO PHƯƠNG ÁN THỰC THI CHIẾN DỊCH QUẢNG CÁO BÁN DẪN TẠI VIỆT NAM
# (DETAILED OPERATIONAL PROPOSAL — SEMICONDUCTOR DIGITAL PAID CAMPAIGN)

**Kính gửi:** Sếp Vy (Marketing Manager / Direct Marketing Lead)  
**Người đệ trình:** Bảo (Product Owner / Paid Project Lead)  
**Ngày lập báo cáo:** 2026-09-30  
**Tình trạng tài liệu:** Hồ sơ Đề xuất Kỹ thuật & Thực thi (Operational Proposal — Pending Review & Sign-off)  
**Tài liệu tham chiếu:** Email chỉ đạo ngày 2026-09-29 của Sếp Vy & Báo cáo kỹ thuật dự án  

> **Proposal boundary (30/09):** 35M là planning ceiling; lịch paid/phase và phân bổ 600k/250k/150k chưa duyệt. LI-CMP-* là mã kế hoạch. Điều kiện sàn, cấu trúc ngôn ngữ và targeting LinkedIn cần account-specific validation; các giá trị USD/sàn trong sơ đồ là giả định kế hoạch, không chứng minh eligibility. Chiến dịch chưa được cấp quyền chạy/spend.

---

## 1. Ma Trận Tiếp Thu & Đối Soát Chỉ Đạo Từ Email Ngày 2026-09-29

Kính gửi Sếp Vy, toàn bộ các định hướng chiến lược và lưu ý vận hành trong email chỉ đạo ngày 2026-09-29 của Sếp đã được đội ngũ dự án rà soát, nghiên cứu kỹ thuật và cụ thể hóa thành phương án thực thi chi tiết theo bảng đối chiếu dưới đây:

| STT | Ý kiến chỉ đạo từ Email của Sếp Vy | Giải pháp kỹ thuật & Phương án cụ thể đã thiết kế trong hồ sơ | Tình trạng sẵn sàng |
|:---:|---|---|:---:|
| **1** | **Ngân sách kênh:** Đề xuất LinkedIn ~600k/ngày, Google Search ~250k/ngày. | Khóa cứng khung đề xuất: LinkedIn 600.000 VNĐ/ngày, Google Search 250.000 VNĐ/ngày, Quỹ dự phòng kỹ thuật (Reserve) 150.000 VNĐ/ngày trong tổng hạn mức 1.000.000 VNĐ/ngày. | Đã hoàn thiện phương án |
| **2** | **Cấu trúc LinkedIn:** Tách biệt 2 nhóm đối tượng (FDI theo danh sách công ty vs Nội địa theo chức danh), tránh chia nhỏ quá nhiều nhóm gây vi phạm ngân sách sàn. | Tái cấu trúc thành **đúng 2 Campaign song song** (`LI-CMP-FDI-SEGMENT` và `LI-CMP-DOMESTIC-SEGMENT`), mỗi campaign nhận đúng 300.000 VNĐ/ngày (~11.5 USD/ngày), vượt ngưỡng sàn tối thiểu (~$10/ngày) của LinkedIn. | Đã hoàn thiện phương án |
| **3** | **Thông điệp Nội địa:** Nhấn mạnh thông điệp *"Đủ chuẩn tham gia vào chuỗi cung ứng bán dẫn"*, tập trung vào bài toán vượt qua kỳ audit của tập đoàn. | Soạn thảo 2 biến thể Headline đề xuất cho copy tiếng Việt: *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"* và *"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"*, làm nổi bật 4 bài toán: Truy xuất lot, Yield/SPC, Recipe, Audit report. | Đã sẵn sàng nội dung |
| **4** | **Lộ trình 4 Phase (7/21/28 ngày):** Khớp nối với trần 35 triệu VNĐ của dự án. | Xây dựng bảng ánh xạ 8 tuần dương lịch (56 ngày lịch): Phân bổ đúng 35 ngày paid (7d Phase 1 + 14d Phase 2 + 14d Phase 3) xen kẽ 21 ngày nghỉ đối soát, hoàn thành trước Tết. | Đã lập bảng lịch trình |
| **5** | **Đánh giá Search Terms:** Không vội vã đưa ra kết luận khi mẫu còn quá nhỏ (ví dụ 7/10 clicks ban đầu); cần đánh giá trên toàn bộ kỳ. | Áp dụng ngưỡng đề xuất **20 observed classified clicks** theo S04 để đánh giá tỷ lệ relevance trước khi xem xét phân bổ ngân sách; giữ đúng trạng thái proposal, không coi là điều kiện bắt buộc chặn mọi tối ưu từ khóa thông thường. | Đã đưa vào phương án đề xuất |
| **6** | **Tính trung thực số liệu Search:** Báo cáo đúng thực tế volume từ khóa, không ép số ảo. | Ghi nhận trung thực: Đa số từ khóa OSAT/Fabless tại Việt Nam hiển thị dấu gạch ngang (chưa có dữ liệu); 1 từ hiển thị 10 searches; áp dụng quy tắc Underspend Protection để bảo vệ ngân sách. | Đã đối soát minh bạch |

---

## 2. Cấu Trúc Chiến Dịch LinkedIn Ads (2 Parallel Campaigns Architecture)

Để giải quyết triệt để bài toán sàn ngân sách tối thiểu của LinkedIn (~10 USD/ngày/campaign) trong khi vẫn bám sát trần ngân sách 600.000 VNĐ/ngày (~23 USD/ngày) theo gợi ý của Sếp, dự án đề xuất cấu trúc tài khoản thành **chính xác 2 Campaign độc lập chạy song song**:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               TỔNG NGÂN SÁCH LINKEDIN ADS ĐỀ XUẤT: 600.000 VNĐ/NGÀY                    │
├──────────────────────────────────────────┬─────────────────────────────────────────────┤
│ CAMPAIGN 1: PHÂN KHÚC FDI                 │ CAMPAIGN 2: PHÂN KHÚC NỘI ĐỊA               │
│ Mã kế hoạch: `LI-CMP-FDI-SEGMENT`                 │ Mã kế hoạch: `LI-CMP-DOMESTIC-SEGMENT`               │
├──────────────────────────────────────────┼─────────────────────────────────────────────┤
│ • Ngân sách ngày: 300.000 VNĐ (~11.5 USD)│ • Ngân sách ngày: 300.000 VNĐ (~11.5 USD)   │
│ • Điều kiện sàn LinkedIn: Đạt (>= $10)   │ • Điều kiện sàn LinkedIn: Đạt (>= $10)      │
│ • Ngôn ngữ: EN, zh-Hans, zh-Hant         │ • Ngôn ngữ: Vietnamese (VI)                 │
│ • Đối tượng: Matched Audience (100-300   │ • Đối tượng: Ngành công nghiệp phụ trợ bán  │
│   nhà máy FDI) kết hợp Chức năng kỹ      │   dẫn (PCB, Substrate, Cơ khí chính xác)    │
│   thuật, Sản xuất, Vận hành, IT/MES      │   kết hợp Chức danh: Giám đốc nhà máy,      │
│ • Doanh nghiệp loại trừ: Intel, Samsung, │   Quản lý QA/QC, Vận hành, IT Trưởng        │
│   Hana Micron, Amkor Technology          │ • Doanh nghiệp loại trừ: Intel, Samsung,    │
│ • Loại trừ khác: Sinh viên, tuyển dụng   │   Hana Micron, Amkor Technology             │
│ • Tài nguyên: B2B Static Cards & OSAT    │ • Loại trừ khác: Sinh viên, tìm việc        │
│   6-Page PDF Document Ad (3 ngôn ngữ)    │ • Tài nguyên: B2B Static Cards tiếng Việt   │
└──────────────────────────────────────────┴─────────────────────────────────────────────┘
```

---

## 3. Chiến Lược Thông Điệp & Bản Thiết Kế Copy Tiếng Việt Chuyên Sâu

Dành riêng cho phân khúc Doanh nghiệp Phụ trợ Nội địa, nội dung quảng cáo được xây dựng bám sát nỗi đau vận hành khi tham gia chuỗi cung ứng toàn cầu:

### 3.1. Hai Biến Thể Headline Trọng Tâm (Proposed Headline Variants)
* **Headline Biến thể 1 (Trực diện chuẩn vendor):**
  > **"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"**
* **Headline Biến thể 2 (Chuẩn hóa quy trình vượt qua kỳ audit):**
  > **"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"**

### 3.2. Bốn Trụ Cột Yêu Cầu Audit Được Nhấn Mạnh Trong Nội Dung
Mỗi bài quảng cáo và tài liệu giới thiệu đều tập trung giải quyết 4 tiêu chuẩn bắt buộc mà các nhà sản xuất bán dẫn Tier-1 đòi hỏi ở nhà cung cấp:
1. **Truy xuất Lot thời gian thực (Lot Traceability):** Số hóa phả hệ lot, liên kết nguyên vật liệu và thông số 4M1E qua từng công đoạn gia công, hỗ trợ tra cứu nguồn gốc hai chiều tức thì.
2. **Kiểm soát Yield & Chất lượng:** Quản lý dữ liệu đo kiểm theo thời gian thực, áp dụng biểu đồ kiểm soát SPC để phát hiện sớm biến động lỗi và tối ưu tỷ lệ thành phẩm.
3. **Quản lý Recipe chuẩn xác:** Khóa và phân phối tham số thiết bị tự động, giảm thiểu tối đa rủi ro do thao tác nạp công thức thủ công.
4. **Sẵn sàng báo cáo Audit:** Hỗ trợ tổng hợp lịch sử sản xuất để chuẩn bị báo cáo cho các đợt đánh giá của đối tác; thời gian thực hiện phụ thuộc phạm vi và dữ liệu.

---

## 4. Kế Hoạch Google Search Ads & Đối Soát Volume Thực Tế

* **Hạn mức ngân sách ngày đề xuất:** **250.000 VNĐ/ngày**.
* **Báo cáo trung thực kết quả Keyword Planner (Ngày 2026-09-14):**
  - Đợt kiểm tra thực tế cho thấy các từ khóa thuần túy về OSAT và Fabless tại thị trường Việt Nam hiển thị dấu gạch ngang (`- / no displayed data`), đồng nghĩa với việc **không có metric hiển thị trong cấu hình đã kiểm tra; mức demand thực tế ghi nhận là chưa xác minh**.
  - Duy nhất một cụm từ khóa liên quan đến phụ trợ điện tử (`electronics manufacturing ERP`) có dữ liệu lịch sử ghi nhận ở mức khiêm tốn: **10 lượt tìm kiếm/tháng**.
* **Giải pháp triển khai thực tế của Digiwin:**
  - **Bộ từ khóa chọn lọc:** Triển khai danh mục **28 từ khóa ứng viên** chia theo 4 cụm ngôn ngữ (VI cho nội địa; EN, zh-Hans, zh-Hant cho FDI) và nhóm từ khóa Thương hiệu Digiwin.
  - **Danh mục 24 từ khóa loại trừ (Negative Keywords):** Thiết lập bộ lọc nhằm ngăn chặn tối đa các tìm kiếm không liên quan gây lãng phí ngân sách: tuyển dụng (`tuyển dụng`, `việc làm`, `job`), giáo dục (`khóa học`, `là gì`, `luận văn`, `pdf`), chứng khoán (`cổ phiếu`, `stock`), phần mềm bẻ khóa (`crack`, `download`).
  - **Quy tắc Underspend Protection:** Nếu khối lượng tìm kiếm thực tế trong ngày không đủ lớn, **số tiền còn lại sẽ được bảo lưu trong tài khoản**, tuyệt đối không nới lỏng từ khóa để tiêu hết 250k. Khoản tiền dư chỉ được cân nhắc điều chuyển sang LinkedIn khi có bằng chứng hiệu quả rõ ràng và quyết định phê duyệt.
* **Nguyên tắc đánh giá Search Term Report (Đề xuất theo S04):** Không vội vàng đưa ra quyết định phân bổ ngân sách chỉ dựa trên cỡ mẫu quá nhỏ (ví dụ 7–10 clicks đầu tiên); giữ đúng phạm vi đề xuất (proposal) **20 observed classified clicks** để đánh giá tỷ lệ relevance trước khi cân nhắc phân bổ ngân sách, không áp đặt thành điều kiện cứng nhắc bắt buộc cho mọi tối ưu từ khóa thông thường.

---

## 5. Lịch Trình Ánh Xạ 8 Tuần Lịch (56 Ngày Lịch / 35 Ngày Paid)

Để dung hòa giữa lộ trình 4 Phase theo gợi ý của Sếp Vy và trần ngân sách 35.000.000 VNĐ của dự án, kế hoạch đã lập bảng ánh xạ chi tiết theo từng tuần lịch dương (Tháng 10 - Tháng 12/2026):

| Tuần Lịch | Giai đoạn (Phase) | Số ngày Paid đề xuất | Số ngày Nghỉ đề xuất | Trọng tâm công việc & Đối soát kỹ thuật |
|:---:|---|:---:|:---:|---|
| **Tuần 1** | **Giai đoạn 1: Khởi động Kỹ thuật** | 4 ngày paid | 3 ngày nghỉ | Kích hoạt hệ thống, kiểm tra hiển thị quảng cáo, theo dõi tag đo lường. |
| **Tuần 2** | **Giai đoạn 1: Đo lường Baseline** | 3 ngày paid | 4 ngày nghỉ | Tổng kết Phase 1 (đủ 7 ngày paid). Đo lường baseline nhận thức ban đầu. |
| **Tuần 3** | **Giai đoạn 2: Xác nhận Tương tác** | 5 ngày paid | 2 ngày nghỉ | Đẩy mạnh phân phối, theo dõi tỷ lệ tiếp cận doanh nghiệp mục tiêu. |
| **Tuần 4** | **Giai đoạn 2: Sàng lọc Dữ liệu** | 5 ngày paid | 2 ngày nghỉ | Rà soát báo cáo tìm kiếm Search Terms, cập nhật thêm từ khóa phủ định. |
| **Tuần 5** | **Giai đoạn 2: Đánh giá Chất lượng** | 4 ngày paid | 3 ngày nghỉ | Tổng kết Phase 2 (đủ 14 ngày paid). Theo dõi thu thập mẫu clicks phân loại hướng tới mốc đề xuất 20 clicks để đánh giá relevance. |
| **Tuần 6** | **Giai đoạn 3: Tối ưu Hóa Chuyển đổi** | 5 ngày paid | 2 ngày nghỉ | Tối ưu hóa mẫu quảng cáo có tương tác sâu, điều chỉnh phân bổ ngân sách. |
| **Tuần 7** | **Giai đoạn 3: Khai thác Nhu cầu Thực** | 5 ngày paid | 2 ngày nghỉ | Kiểm soát tỷ lệ lead hợp lệ (Effective Lead Rate), lọc bỏ liên hệ rác. |
| **Tuần 8** | **Giai đoạn 3: Tổng kết & Nghiệm thu** | 4 ngày paid | 3 ngày nghỉ | Tổng kết Phase 3 (đủ 14 ngày paid). Hoàn tất toàn bộ chiến dịch trước Tết. |
| **TỔNG** | **8 Tuần (56 Ngày Lịch Dương)** | **35 Ngày Paid** | **21 Ngày Nghỉ** | **Tổng chi tiêu tối đa: 35.000.000 VNĐ (Khớp trần 100%).** |

---

## 6. Trạng Thái Kỹ Thuật (Landing Page & Tracking Invariants)

Hồ sơ tài nguyên phục vụ chiến dịch đã được chuẩn bị trên môi trường nội bộ và vượt qua kiểm toán tự động:
1. **Ba Trang Đích Canonical Đa Ngôn Ngữ (Checkpoint deployment 30/09):**
   - Đã tích hợp hoàn chỉnh bộ chọn 4 ngôn ngữ (`vi`, `en`, `zh-Hans`, `zh-Hant`) trên cả 3 route: OSAT, Fabless và Partner dưới dạng **candidate offline** trong repository.
   - *Phân định ranh giới hiện trạng:* Checkpoint `operations/evidence/locale/2026-09-30-four-locale-production-deployment.md` ghi nhận 4 locale đã publish và public verified ở ba URL cũ. Slice này không kiểm live lại; native terminology, ad-entry QA và readiness chạy quảng cáo vẫn cần xác nhận riêng.
   - Tên riêng các đối tác phụ trợ nội địa được giữ nguyên tiếng Việt (`Khang Đạt`, `Nhật Tân`, `Phẩm Thuyên`, `Pinquan`) nhằm đảm bảo tính pháp lý và nhận diện thương hiệu thực tế.
2. **Tuân Thủ Bất Biến Tracking & Không Chứa Form Rác:**
   - Các trang đích được thiết kế độc lập, không gắn form thu thập dữ liệu thô chưa kiểm soát.
   - Nút kêu gọi hành động (CTA) được chuẩn hóa bất biến: OSAT đúng 2 CTA, Fabless đúng 2 CTA, Partner duy nhất 1 CTA tại Header (`partner-cta-header`).
   - Hệ thống theo dõi nhận thức vùng hiển thị (Section Awareness Tracking) hoạt động ổn định trên test suite, đạt **12 / 12 Unit Tests PASS**.

---

## 7. Các Điểm Đề Xuất Tham Vấn Ý Kiến Chỉ Đạo Của Sếp Vy

Kính trình Sếp Vy xem xét và cho ý kiến định hướng chuyên môn về 3 nội dung thực thi sau để Product Owner (Bảo) hoàn thiện phương án vận hành:
1. **Góp ý Cấu trúc 2 Campaign LinkedIn song song:** Ý kiến về phương án phân bổ 300k cho FDI (`LI-CMP-FDI-SEGMENT`) và 300k cho Nội địa (`LI-CMP-DOMESTIC-SEGMENT`).
2. **Góp ý 2 Biến thể Headline tiếng Việt:** Định hướng về bộ copy xoay quanh thông điệp *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"*.
3. **Góp ý Bảng Lịch trình 8 Tuần / 35 Ngày Paid:** Xem xét nhịp chạy xen kẽ ngày nghỉ đối soát để đảm bảo trần ngân sách 35 triệu VNĐ.

---
*Báo cáo phương án thực thi được lập bởi Product Owner dự án Semiconductor Paid, kính trình Sếp Vy xem xét.*
