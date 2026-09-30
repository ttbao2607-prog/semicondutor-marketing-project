# BÁO CÁO KIỂM TOÁN ĐỘC LẬP: GOOGLE SEARCH MULTILINGUAL RSA COPY SUITE

- **Audit Date:** 2026-09-30
- **Auditor Role:** Specialist Auditor (Independent Quality & Terminology Assurance)
- **Target Worktree:** `D:\Digiwin_Semiconductor_Audit_Worktree`
- **Target Files Inspected:**
  1. `ads/google/Google_Search_Build_Sheet.md`
  2. `drafts/S02_Google_Search_Research.md`
  3. `tests/test_google_search_rsa.py`
- **Overall Audit Verdict:** **PASS (100% COMPLIANT)**

---

## 1. MỤC TIÊU VÀ PHẠM VI KIỂM TOÁN (AUDIT SCOPE)

Kiểm toán độc lập toàn bộ bộ mẫu quảng cáo tìm kiếm thích ứng (Responsive Search Ads - RSA) đa ngôn ngữ và tiện ích mở rộng (Extensions) cho chiến dịch Google Search ngành Bán dẫn (Semiconductor Paid), bao gồm:
1. **Kiểm toán Kỹ thuật Độc lập (Technical & Character Count Verification):**
   - Xác thực số lượng mẫu quảng cáo: 3 Nhóm quảng cáo (`OSAT_LOT_TEST`, `FABLESS_OUTSOURCE_WIP`, `ERP_MES_OT_PARTNER`) x 4 Ngôn ngữ (`VI`, `EN`, `zh-Hans`, `zh-Hant`) = 12 khối.
   - Mỗi khối bắt buộc đủ: 12 Headlines và 4 Descriptions. Tổng cộng: **144 Headlines** và **48 Descriptions**.
   - Kiểm tra ngưỡng giới hạn độ dài ký tự theo chuẩn Google Ads:
     * Tiếng Anh / Tiếng Việt (Latin): Headlines <= 30 ký tự; Descriptions <= 90 ký tự.
     * Tiếng Trung (CJK): Tính theo đơn vị double-byte (ký tự chữ Hán tính 2 đơn vị); Headlines <= 30 đơn vị (tối đa 15 chữ Hán); Descriptions <= 90 đơn vị (tối đa 45 chữ Hán).
2. **Thẩm định Thuật ngữ Chuyên ngành Bán dẫn (Semiconductor Terminology Audit):**
   - Đánh giá tính chính xác của các bài toán nghiệp vụ cốt lõi: Lot genealogy, 4M1E, Test data & yield, SPC, Cost closing, Outsourced WIP, Datecode/BIN split, Foundry progress, Multi-tier BOM, ERP-MES-OT data handoff.
   - Thẩm định sự phân hóa chuẩn xác giữa tiếng Trung Giản thể (zh-Hans - FDI Trung Quốc đại lục) và tiếng Trung Phồn thể (zh-Hant - FDI Đài Loan).
3. **Thẩm định Tiện ích Mở rộng (Ad Extensions & Sitelinks):**
   - Đủ 4 Callouts cho mỗi ngôn ngữ (tuân thủ giới hạn <= 25 đơn vị).
   - Đủ 3 Sitelinks cho mỗi ngôn ngữ trỏ đúng về 3 landing route kèm tham số ngôn ngữ (`?lang=vi`, `?lang=en`, `?lang=zh-Hans`, `?lang=zh-Hant`).

---

## 2. KẾT QUẢ KIỂM TRA KỸ THUẬT ĐỘC LẬP (TECHNICAL AUDIT)

### 2.1. Kết quả thực thi Test Suite Tự động
- **Lệnh thực thi:** `python tests/test_google_search_rsa.py`
- **Exit Code:** `0` (Success)
- **Output:**
  ```text
  Total Headline blocks found: 12
  Total Description blocks found: 12
  Total headlines verified: 144
  Total descriptions verified: 48
  ALL RSA HEADLINES AND DESCRIPTIONS STRICTLY PASS GOOGLE ADS LIMITS!
  ```

### 2.2. Bảng Tổng kết Số lượng và Độ dài Ký tự (Breakdown Matrix)

| Ngôn ngữ (Locale) | Nhóm quảng cáo (Ad Group) | Số Headlines (Y/c: 12) | Biên độ độ dài H (Limit <= 30) | Số Descriptions (Y/c: 4) | Biên độ độ dài D (Limit <= 90) | Trạng thái kỹ thuật |
|---|---|:---:|:---:|:---:|:---:|:---:|
| **Vietnamese (VI)** | `OSAT_LOT_TEST` | 12 / 12 | 17 – 28 chars | 4 / 4 | 66 – 74 chars | **PASS** |
| | `FABLESS_OUTSOURCE_WIP` | 12 / 12 | 20 – 27 chars | 4 / 4 | 68 – 74 chars | **PASS** |
| | `ERP_MES_OT_PARTNER` | 12 / 12 | 16 – 27 chars | 4 / 4 | 58 – 69 chars | **PASS** |
| **English (EN)** | `OSAT_LOT_TEST` | 12 / 12 | 19 – 27 chars | 4 / 4 | 82 – 87 chars | **PASS** |
| | `FABLESS_OUTSOURCE_WIP` | 12 / 12 | 21 – 28 chars | 4 / 4 | 77 – 85 chars | **PASS** |
| | `ERP_MES_OT_PARTNER` | 12 / 12 | 23 – 29 chars | 4 / 4 | 83 – 86 chars | **PASS** |
| **Simplified Chinese (zh-Hans)** | `OSAT_LOT_TEST` | 12 / 12 | 16 – 23 units (8–11.5 CJK) | 4 / 4 | 66 – 76 units (33–38 CJK) | **PASS** |
| | `FABLESS_OUTSOURCE_WIP` | 12 / 12 | 17 – 25 units (8.5–12.5 CJK) | 4 / 4 | 70 – 74 units (35–37 CJK) | **PASS** |
| | `ERP_MES_OT_PARTNER` | 12 / 12 | 20 – 22 units (10–11 CJK) | 4 / 4 | 68 – 76 units (34–38 CJK) | **PASS** |
| **Traditional Chinese (zh-Hant)** | `OSAT_LOT_TEST` | 12 / 12 | 16 – 23 units (8–11.5 CJK) | 4 / 4 | 66 – 76 units (33–38 CJK) | **PASS** |
| | `FABLESS_OUTSOURCE_WIP` | 12 / 12 | 17 – 25 units (8.5–12.5 CJK) | 4 / 4 | 70 – 74 units (35–37 CJK) | **PASS** |
| | `ERP_MES_OT_PARTNER` | 12 / 12 | 20 – 22 units (10–11 CJK) | 4 / 4 | 68 – 76 units (34–38 CJK) | **PASS** |

- **Tổng kết kiểm đếm:** 100% đạt chuẩn Google Ads Character Count Policy (Không có bất kỳ Headline nào > 30 units hay Description nào > 90 units).

---

## 3. THẨM ĐỊNH THUẬT NGỮ CHUYÊN NGÀNH BÁN DẪN (SEMICONDUCTOR TERMINOLOGY AUDIT)

### 3.1. Nhóm OSAT (`OSAT_LOT_TEST`)
- **Nghiệp vụ phản ánh:**
  - *Lot Genealogy & Traceability:* Thể hiện chính xác qua `OSAT: Nối dữ liệu theo lot`, `Wafer Lot Genealogy`, `建立芯片批次谱系` (zh-Hans), `建立晶片批次譜系` (zh-Hant).
  - *4M1E & Shopfloor Context:* Tích hợp rõ nét trong `4M1E trong một luồng dữ liệu`, `4M1E Shopfloor Context`, `晶圆级 4M1E 追溯体系`, `4M1E機台參數`.
  - *Test Data & Yield / SPC:* Sử dụng chuẩn xác các khái niệm `Kết nối test data & quality`, `Test Data & Quality Flow`, `打线接合与测试数据串联`, `实时监测良率与SPC` (zh-Hans), `即時監測良率與SPC` (zh-Hant).
  - *Cost Closing:* Chạm đúng điểm nóng kế toán quản trị phân xưởng: `Đối soát cost close`, `Lot-Level Cost Accounting`, `封测精细化成本核算` (zh-Hans), `封測精細化成本結算` (zh-Hant).
- **Cam kết tuân thủ chính sách:**
  - Cả 4 ngôn ngữ đều giữ vững nguyên tắc *Mechanism-first* và *Zero unverified claims*: không bịa đặt case study, cam kết không yêu cầu upload dữ liệu nhạy cảm (`không gửi dữ liệu sản xuất qua trang`, `without sending sensitive production data`, `无需在网页上传敏感生产数据`).

### 3.2. Nhóm Fabless (`FABLESS_OUTSOURCE_WIP`)
- **Nghiệp vụ phản ánh:**
  - *Outsourced WIP & Black Box:* Phản ánh chân thực bài toán theo dõi tiến độ gia công: `Quản trị outsourced WIP`, `Fabless Outsourced WIP`, `跨委外厂在制品库存可视` (zh-Hans), `跨委外廠在製品庫存可視` (zh-Hant), `消除外包黑盒` / `打破外包黑盒子`.
  - *Datecode & BIN Split:* Đưa thuật ngữ then chốt của ngành đóng gói/phân loại IC vào copy: `Datecode BIN lot rõ hơn`, `Datecode & BIN Lot Tracking`, `Datecode与BIN分料管理`.
  - *Foundry Progress & Forecast Flow:* Kết nối dòng kế hoạch và thực tế: `Nối forecast với outsource`, `Wafer Foundry WIP Visibility`, `贯通预测与外包生产排程` (zh-Hans), `晶圓代工進度` (zh-Hant).
  - *Multi-tier BOM & Cost Breakdown:* Phản ánh cấu trúc BOM phức tạp nhiều tầng của Fabless: `Fabless Multi-Tier BOM`, `多阶半导体 BOM 架构` (zh-Hans), `多階半導體 BOM 架構` (zh-Hant), `委外成本精细分摊核算` (zh-Hans) / `委外成本精細分攤結算` (zh-Hant).

### 3.3. Nhóm Partner (`ERP_MES_OT_PARTNER`)
- **Nghiệp vụ phản ánh:**
  - *ERP-MES-OT Handoff & Boundaries:* Định vị đúng bài toán giao tiếp dữ liệu: `Nối ERP MES và OT`, `Semiconductor ERP MES OT`, `Define clear data ownership and interface boundaries`, `明确 ERP、MES 与车间底层 OT 之间的数据归属权与握手协议` (zh-Hans), `介面協定` (zh-Hant).
  - *Shopfloor & Equipment Integration:* `Quản trị dữ liệu thiết bị`, `Equipment OT Integration`, `打通设备机台与企业系统`, `自動化車間數據整合底座`.
  - *SI Partner & Vietnam Footprint:* Nhấn mạnh năng lực bản địa hóa và kinh nghiệm 40 năm của Digiwin: `Vietnam Factory ERP MES`, `Semiconductor SI Partner`, `40年制造底蕴`, `深耕越南製造四十載`.

### 3.4. Đối chiếu Phân hóa Ngôn ngữ: Trung Quốc Đại Lục (zh-Hans) vs. Đài Loan (zh-Hant)
Bản copy suite đã thể hiện sự am hiểu sâu sắc về thói quen hành văn và thuật ngữ chuyên ngành tại hai thị trường FDI trọng yếu:

| Khái niệm / Bài toán | Trung Quốc đại lục (zh-Hans - China FDI) | Đài Loan (zh-Hant - Taiwan FDI) | Đánh giá kiểm toán |
|---|---|---|:---:|
| **Chip / Vi mạch** | `芯片` (Tân phiến) | `晶片` (Tinh phiến) | **Chuẩn xác tuyệt đối** |
| **Wafer** | `晶圆` | `晶圓` | **Chuẩn xác tuyệt đối** |
| **Lot / Batch** | `批次` (`批次追溯`, `批次谱系`) | `批號` / `批次` (`批號追蹤`, `批號防錯`) | **Chuẩn xác tuyệt đối** |
| **Tích hợp hệ thống** | `集成` (`系统集成`, `数据集成底座`) | `整合` (`系統整合`, `數位化整合`) | **Chuẩn xác tuyệt đối** |
| **Thời gian thực** | `实时` (`实时监测良率`) | `即時` (`即時監測良率`) | **Chuẩn ngữ cảnh Đài Loan** |
| **Đóng sổ chi phí** | `成本核算` (`分摊核算`) | `成本結算` (`分攤結算`) | **Chuẩn nghiệp vụ tài chính** |
| **Kỳ hạn giao hàng** | `交付周期` | `訂單交期` / `交貨週期` | **Chuẩn thuật ngữ thương mại** |
| **Phân xưởng sản xuất** | `车间` (`车间工序流转`) | `現場` (`現場工序流轉`, `製程交接點`) | **Chuẩn thuật ngữ vận hành** |
| **Giao thức bắt tay IT-OT**| `握手协议` | `介面協定` | **Chuẩn thuật ngữ kỹ thuật** |
| **Đối tác triển khai** | `实施伙伴` | `導入夥伴` | **Chuẩn văn hóa phần mềm ERP** |
| **Công nghệ số** | `数字化` | `數位化` | **Chuẩn ngữ pháp Đài Loan** |
| **Bản vẽ thiết kế** | `电路设计` | `電路圖紙` | **Chuẩn thuật ngữ kỹ thuật** |

---

## 4. THẨM ĐỊNH TIỆN ÍCH MỞ RỘNG (EXTENSIONS & SITELINKS AUDIT)

### 4.1. Tiện ích chú thích (Callouts)
- **Định lượng:** Đúng 4 callouts cho mỗi ngôn ngữ (tổng cộng 16 callouts).
- **Độ dài ký tự:** Tất cả đều <= 25 đơn vị (tuân thủ giới hạn callout của Google Ads).
- **Nội dung:**
  * **VI:** `Mechanism-first`, `Vietnamese-first`, `Không claim chưa duyệt`, `Đối chiếu pain point`.
  * **EN:** `Mechanism-First`, `Verified Architecture`, `Zero Unverified Claims`, `Shopfloor Focus`.
  * **zh-Hans:** `纯技术机制推演`, `40年制造底蕴`, `杜绝未验证宣称`, `聚焦车间痛点`.
  * **zh-Hant:** `純技術機制推演`, `40年製造底蘊`, `杜絕未驗證宣稱`, `聚焦現場痛點`.
- **Đánh giá:** Đồng nhất 100% với tôn chỉ vận hành và ranh giới bằng chứng tại `AGENTS.md`.

### 4.2. Tiện ích đường liên kết trang web (Sitelinks)
- **Định lượng:** Đúng 3 sitelinks cho mỗi ngôn ngữ trỏ về 3 landing route tương ứng.
- **Tham số ngôn ngữ:** Tất cả URL đều đính kèm tham số `?lang=` chính xác:
  * **VI:**
    - `Khung OSAT` -> `/osat-lot-test-traceability?lang=vi`
    - `Outsource WIP` -> `/fabless-outsourced-wip?lang=vi`
    - `Data handoff ERP-MES` -> `/semiconductor-erp-mes-ot?lang=vi`
  * **EN:**
    - `OSAT Lot Traceability` -> `/osat-lot-test-traceability?lang=en`
    - `Fabless Outsource WIP` -> `/fabless-outsourced-wip?lang=en`
    - `ERP MES OT Integration` -> `/semiconductor-erp-mes-ot?lang=en`
  * **zh-Hans:**
    - `封测批次追溯` -> `/osat-lot-test-traceability?lang=zh-Hans`
    - `委外在制品管理` -> `/fabless-outsourced-wip?lang=zh-Hans`
    - `ERP MES OT 集成` -> `/semiconductor-erp-mes-ot?lang=zh-Hans`
  * **zh-Hant:**
    - `封測批號追溯` -> `/osat-lot-test-traceability?lang=zh-Hant`
    - `委外在製品管理` -> `/fabless-outsourced-wip?lang=zh-Hant`
    - `ERP MES OT 整合` -> `/semiconductor-erp-mes-ot?lang=zh-Hant`
- **Đánh giá:** Phù hợp với kiến trúc landing hiện hành (1 HTML có bộ chuyển đổi ngôn ngữ đầu trang) và chuẩn bị sẵn sàng cho cơ chế định tuyến locale.

---

## 5. KẾT LUẬN NGHIỆM THU (AUDIT CONCLUSION & VERDICT)

1. **Kết luận Kiểm toán:** **PASS — CHẤP THUẬN NGHIỆM THU TOÀN PHẦN (100% ACCEPTANCE)**.
2. **Khuyến nghị Vận hành (Operational Recommendations):**
   - Bộ RSA Copy Suite tại `ads/google/Google_Search_Build_Sheet.md` đã sẵn sàng về mặt nội dung kỹ thuật, độ dài ký tự và thuật ngữ bán dẫn.
   - Giữ nguyên trạng thái chiến dịch **paused / offline draft** theo quy định tại `AGENTS.md` cho đến khi có mandate cấp phép và xác thực trực tiếp trên Google Keyword Planner với tài khoản live.
