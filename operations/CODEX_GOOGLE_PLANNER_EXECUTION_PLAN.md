# KẾ HOẠCH THỰC THI KIỂM CHỨNG TỪ KHÓA TRÊN GOOGLE KEYWORD PLANNER
# (CODEX CHROME EXECUTION SPECIFICATION: MULTILINGUAL KEYWORD DISCOVERY)

**Người đệ trình:** Bảo (Product Owner / Paid Project Lead)  
**Đơn vị thực thi:** Codex Automation Agent (Chrome Browser Execution)  
**Tài liệu tham chiếu:** [`ads/google/Google_Search_Build_Sheet.md`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/ads/google/Google_Search_Build_Sheet.md), [`drafts/S02_Google_Search_Research.md`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/drafts/S02_Google_Search_Research.md)  
**Ranh giới vận hành (Trust Boundary):** **CHẾ ĐỘ TRA CỨU VÀ ĐỌC DỮ LIỆU ĐO LƯỜNG (QUERY & READ-ONLY METRICS). TUYỆT ĐỐI KHÔNG TẠO CHIẾN DỊCH, KHÔNG IMPORT TỪ KHÓA VÀO TÀI KHOẢN LIVE, KHÔNG KÍCH HOẠT NGÂN SÁCH (ZERO SPEND).**

---

## 1. Mục Tiêu & Ranh Giới Vận Hành (Scope & Boundaries)

### 1.1. Mục Tiêu
Sử dụng công cụ Google Keyword Planner trên trình duyệt Chrome để tra cứu thực nghiệm số liệu lưu lượng tìm kiếm lịch sử (Average monthly searches), mức độ cạnh tranh (Competition) và khung giá thầu ước tính (Top of page bid low/high range) tại thị trường Việt Nam cho **21 từ khóa ứng viên mới** thuộc 3 cụm ngôn ngữ còn thiếu:
1. **Cụm 1 (Tiếng Anh - EN):** 7 từ khóa.
2. **Cụm 2 (Tiếng Trung Giản thể - zh-Hans):** 7 từ khóa (FDI Trung Quốc đại lục).
3. **Cụm 3 (Tiếng Trung Phồn thể - zh-Hant):** 7 từ khóa (FDI Đài Loan).

### 1.2. Ranh Giới Nghiêm Ngặt (Strict Prohibitions)
1. **CẤM** bấm nút "Thêm từ khóa để tạo kế hoạch" (Add keywords to create plan) hoặc "Tạo chiến dịch" (Create campaign).
2. **CẤM** sửa đổi bất kỳ chiến dịch, nhóm quảng cáo, từ khóa, tiện ích hay cài đặt nào đang có trong tài khoản Google Ads.
3. **CẤM** nhập thông tin thanh toán, sửa đổi ngân sách hoặc bật kích hoạt phân phối quảng cáo.
4. **CẤM** tắt hoặc thay đổi cài đặt bảo mật tài khoản.

### 1.3. Tác Dụng Phụ Được Chấp Thuận Trước (Accepted Side-Effect)
Theo ghi nhận tại `AGENTS.md`, khi nhấp nút **"Nhận kết quả" (Get results)** trên Google Keyword Planner, hệ thống Google Ads sẽ **tự động tạo một mục kế hoạch nháp (Draft plan entry)** trong danh sách Planner dù người dùng không bấm lưu. Thao tác này được Product Owner Bảo **chấp thuận trước như một tác dụng phụ kỹ thuật không thể tránh khỏi** của Google Ads. Codex không cần xóa hay sửa các draft plan này.

---

## 2. Quy Trình Thao Tác Chi Tiết Trên Chrome (Step-by-Step Instructions)

Codex thực hiện tuần tự qua 3 phiên truy vấn độc lập:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│               QUY TRÌNH THỰC THI TRÊN GOOGLE KEYWORD PLANNER (CHROME)                   │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ Bước 1: Mở Google Ads ──> Tools and settings ──> Planning ──> Keyword Planner          │
│ Bước 2: Chọn 'Discover new keywords' (Khám phá các từ khóa mới)                        │
│ Bước 3: Thực hiện BATCH 1: Cụm Tiếng Anh (Location: Vietnam / Lang: English)           │
│ Bước 4: Thực hiện BATCH 2: Cụm Trung Giản thể (Location: Vietnam / Lang: Chinese Simp) │
│ Bước 5: Thực hiện BATCH 3: Cụm Trung Phồn thể (Location: Vietnam / Lang: Chinese Trad) │
│ Bước 6: Đọc dữ liệu, chụp màn hình bằng chứng và phân loại mã trạng thái định danh     │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

### Chi tiết thiết lập từng Batch:

### BATCH 1: Kiểm Tra Cụm Tiếng Anh (English - EN)
1. **Cấu hình truy vấn (Targeting Settings):**
   - **Địa điểm (Location):** `Vietnam` (Việt Nam) — Đảm bảo đã xóa các quốc gia khác.
   - **Ngôn ngữ (Language):** `English` (Tiếng Anh).
   - **Mạng tìm kiếm (Network):** `Google`.
   - **Khoảng thời gian (Date Range):** `12 tháng qua` (Last 12 months, ví dụ: 09/2025 – 08/2026 hoặc gần nhất).
   - **Loại trừ ý tưởng người lớn (Adult ideas):** `Bật / Excluded`.
2. **Danh sách 7 từ khóa hạt giống (Seed Keywords):**
   ```text
   OSAT lot traceability software
   semiconductor test data management
   fabless outsourced WIP tracking
   semiconductor subcontract production tracking
   semiconductor ERP MES integration
   MES integration partner Vietnam
   Digiwin semiconductor Vietnam
   ```
3. **Thao tác:** Dán danh sách 7 từ khóa vào ô nhập -> Nhấp **"Nhận kết quả" (Get results)**.

---

### BATCH 2: Kiểm Tra Cụm Tiếng Trung Giản Thể (Simplified Chinese - zh-Hans)
1. **Cấu hình truy vấn (Targeting Settings):**
   - **Địa điểm (Location):** `Vietnam` (Việt Nam).
   - **Ngôn ngữ (Language):** `Chinese (simplified)` (Tiếng Trung giản thể / 中文(简体)).
   - **Mạng tìm kiếm (Network):** `Google`.
   - **Khoảng thời gian (Date Range):** `12 tháng qua`.
   - **Loại trừ ý tưởng người lớn:** `Bật / Excluded`.
2. **Danh sách 7 từ khóa hạt giống (Seed Keywords):**
   ```text
   半导体封装测试 MES
   半导体批次追溯
   无晶圆厂外包生产在制品管理
   芯片委外生产追踪
   半导体工厂 ERP MES 集成
   越南半导体 MES 集成合作伙伴
   鼎捷 越南 半导体
   ```
3. **Thao tác:** Dán danh sách 7 từ khóa vào ô nhập -> Nhấp **"Nhận kết quả" (Get results)**.

---

### BATCH 3: Kiểm Tra Cụm Tiếng Trung Phồn Thể (Traditional Chinese - zh-Hant)
1. **Cấu hình truy vấn (Targeting Settings):**
   - **Địa điểm (Location):** `Vietnam` (Việt Nam).
   - **Ngôn ngữ (Language):** `Chinese (traditional)` (Tiếng Trung phồn thể / 中文(繁體)).
   - **Mạng tìm kiếm (Network):** `Google`.
   - **Khoảng thời gian (Date Range):** `12 tháng qua`.
   - **Loại trừ ý tưởng người lớn:** `Bật / Excluded`.
2. **Danh sách 7 từ khóa hạt giống (Seed Keywords):**
   ```text
   半導體封裝測試 MES
   半導體批次追溯
   無晶圓廠委外生產在製品管理
   晶片委外生產追蹤
   半導體工廠 ERP MES 整合
   越南半導體 MES 系統整合夥伴
   鼎捷 越南 半導體
   ```
3. **Thao tác:** Dán danh sách 7 từ khóa vào ô nhập -> Nhấp **"Nhận kết quả" (Get results)**.

---

## 3. Tiêu Chí Phân Loại Trạng Thái Định Danh (Deterministic Status Criteria)

Sau khi tra cứu mỗi Batch, Codex **bắt buộc phải phân loại kết quả vào chính xác 1 trong 5 mã trạng thái kỹ thuật sau**, tuyệt đối không đưa ra nhận xét cảm tính:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                   HỆ THỐNG MÃ TRẠNG THÁI NGHIỆM THU ĐỊNH DANH (STATUS ENUM)             │
├───────────────────────────────────────┬────────────────────────┬───────────────────────┤
│ Mã Trạng Thái (Deterministic Code)    │ Điều Kiện Kỹ Thuật     │ Phân Loại Bằng Chứng  │
├───────────────────────────────────────┼────────────────────────┼───────────────────────┤
│ 1. PLANNER_METRICS_OBSERVED           │ Có số liệu Volume > 0  │ CÓ DỮ LIỆU THỰC TẾ    │
│                                       │ và Bid hiển thị        │ (Observed Metrics)    │
├───────────────────────────────────────┼────────────────────────┼───────────────────────┤
│ 2. PLANNER_NO_DISPLAYED_DATA_DASHES   │ Toàn bộ hàng hiển thị  │ CHƯA CÓ SỐ LIỆU       │
│                                       │ dấu gạch ngang (-)     │ (No Displayed Data)   │
├───────────────────────────────────────┼────────────────────────┼───────────────────────┤
│ 3. PLANNER_LOW_VOLUME_FLAGGED         │ Google gắn nhãn cảnh   │ CẢNH BÁO LƯU LƯỢNG    │
│                                       │ báo 'Low search volume'│ THẤP TỪ GOOGLE ADS    │
├───────────────────────────────────────┼────────────────────────┼───────────────────────┤
│ 4. PLANNER_DOM_FALSE_SIGNAL_NON_BLOCK │ Báo 'Turn off ad block'│ TÍN HIỆU GIẢ TRONG DOM│
│                                       │ nhưng UI vẫn chạy tốt  │ (Non-blocking Signal) │
├───────────────────────────────────────┼────────────────────────┼───────────────────────┤
│ 5. PLANNER_AUTH_OR_ACCESS_BLOCKED     │ Yêu cầu đăng nhập lại /│ BỊ CHẶN QUYỀN TRUY CẬP│
│                                       │ 2FA / Thiếu quyền      │ (Blocked / Auth error)│
└───────────────────────────────────────┴────────────────────────┴───────────────────────┘
```

### Diễn giải chi tiết từng mã:

#### 1. `PLANNER_METRICS_OBSERVED`
- **Điều kiện:** Có ít nhất 1 từ khóa hiển thị giá trị số thực tế ở cột *Số lượt tìm kiếm trung bình hàng tháng (Avg. monthly searches)* (ví dụ: `10`, `50`, `100`...) và/hoặc hiển thị khung giá thầu đầu trang.
- **Ý nghĩa:** Có bằng chứng thực nghiệm về nhu cầu tìm kiếm tự nhiên của người dùng tại Việt Nam bằng ngôn ngữ tương ứng.
- **Bằng chứng:** Ghi lại giá trị số chính xác và chụp ảnh màn hình bảng kết quả.

#### 2. `PLANNER_NO_DISPLAYED_DATA_DASHES`
- **Điều kiện:** Toàn bộ 7 từ khóa hạt giống đều hiển thị dấu gạch ngang (`-`) ở tất cả các cột: *Avg. monthly searches, Three-month change, YoY change, Competition, Top of page bid*. Bảng ý tưởng từ khóa liên quan không có dữ liệu.
- **Ý nghĩa:** Phân loại chuẩn `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION`. **TUYỆT ĐỐI KHÔNG SUY DIỄN NHU CẦU BẰNG 0** (do cỡ mẫu cấu hình hẹp hoặc Google chưa công bố dữ liệu).
- **Bằng chứng:** Chụp ảnh màn hình hiển thị toàn bộ dấu gạch ngang của 7 hàng từ khóa.

#### 3. `PLANNER_LOW_VOLUME_FLAGGED`
- **Điều kiện:** Giao diện Google hiển thị nhãn cảnh báo trực tiếp màu vàng/cam hoặc dòng chữ *"Lượng tìm kiếm thấp (Low search volume)"*.
- **Ý nghĩa:** Xác nhận từ khóa có nguy cơ bị đóng băng hiển thị nếu đưa vào chiến dịch live.

#### 4. `PLANNER_DOM_FALSE_SIGNAL_NON_BLOCKING`
- **Điều kiện:** Trình thu thập accessibility/DOM thấy chuỗi text *"Turn off ad blockers"*, nhưng trên ảnh chụp màn hình thực tế **hoàn toàn không có hộp thoại/modal che phủ** và người dùng vẫn thao tác nhập từ khóa/nhận kết quả bình thường.
- **Xử lý:** Phân loại là tín hiệu giả không chặn (`OBSERVED_DOM_FALSE_SIGNAL_NON_BLOCKING`), tiếp tục thực thi và không coi là lỗi cản trở.

#### 5. `PLANNER_AUTH_OR_ACCESS_BLOCKED`
- **Điều kiện:** Trình duyệt gặp màn hình yêu cầu xác thực 2 bước (2FA), mật khẩu hết hạn, hoặc tài khoản Google Ads bị từ chối quyền truy cập Keyword Planner.
- **Xử lý:** Dừng thao tác và báo cáo ngay để PO Bảo xử lý phiên đăng nhập.

---

## 4. Biên Bản Bàn Giao Nghiệm Thu (Evidence Receipt Template)

Sau khi Codex thực thi xong cả 3 Batch, Codex tạo file báo cáo nghiệm thu tại:  
`operations/CODEX_GOOGLE_PLANNER_DISCOVERY_RECEIPT.md` theo mẫu chuẩn sau:

```markdown
# BIÊN BẢN NGHIỆM THU TRA CỨU GOOGLE KEYWORD PLANNER ĐA NGÔN NGỮ

- **Thời điểm thực hiện (Timestamp):** [YYYY-MM-DD HH:MM UTC+7]
- **Tài khoản Google Ads ID:** [Đã che 4 số cuối]
- **Cấu hình chung:** Địa điểm: Việt Nam | Mạng: Google | Kỳ: 12 tháng gần nhất

---

### KẾT QUẢ TỪNG BATCH

#### 1. Batch 1: Tiếng Anh (English - EN)
- Cấu hình ngôn ngữ: `English`
- **Mã Trạng Thái (Deterministic Status):** `[CHỌN 1 TRONG 5 MÃ Ở MỤC 3]`
- Số từ khóa có số liệu hiển thị: [Số lượng / 7]
- Chi tiết số liệu quan sát:
  * `OSAT lot traceability software`: [Số lượng hoặc `-`]
  * `semiconductor test data management`: [Số lượng hoặc `-`]
  * `fabless outsourced WIP tracking`: [Số lượng hoặc `-`]
  * `semiconductor subcontract production tracking`: [Số lượng hoặc `-`]
  * `semiconductor ERP MES integration`: [Số lượng hoặc `-`]
  * `MES integration partner Vietnam`: [Số lượng hoặc `-`]
  * `Digiwin semiconductor Vietnam`: [Số lượng hoặc `-`]
- Ảnh chụp màn hình: `outputs/evidence/google_planner_en_[timestamp].png`

#### 2. Batch 2: Tiếng Trung Giản Thể (zh-Hans)
- Cấu hình ngôn ngữ: `Chinese (simplified)`
- **Mã Trạng Thái (Deterministic Status):** `[CHỌN 1 TRONG 5 MÃ Ở MỤC 3]`
- Số từ khóa có số liệu hiển thị: [Số lượng / 7]
- Chi tiết số liệu quan sát: [Liệt kê từng từ kèm số liệu hoặc `-`]
- Ảnh chụp màn hình: `outputs/evidence/google_planner_zh_hans_[timestamp].png`

#### 3. Batch 3: Tiếng Trung Phồn Thể (zh-Hant)
- Cấu hình ngôn ngữ: `Chinese (traditional)`
- **Mã Trạng Thái (Deterministic Status):** `[CHỌN 1 TRONG 5 MÃ Ở MỤC 3]`
- Số từ khóa có số liệu hiển thị: [Số lượng / 7]
- Chi tiết số liệu quan sát: [Liệt kê từng từ kèm số liệu hoặc `-`]
- Ảnh chụp màn hình: `outputs/evidence/google_planner_zh_hant_[timestamp].png`

---

### TỔNG KẾT VẬN HÀNH CHO PO BẢO
- Nhận định về nguy cơ Low Search Volume: [Có / Không / Chưa xác minh]
- Khuyến nghị về việc áp dụng quy tắc Underspend Protection cho các nhóm từ khóa này.
```
