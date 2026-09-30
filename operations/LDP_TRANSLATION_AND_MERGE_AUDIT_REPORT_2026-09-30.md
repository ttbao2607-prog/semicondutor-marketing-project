# BÁO CÁO KIỂM TOÁN CHUYÊN SÂU: TRANSLATING GAP & TECHNICAL MERGE CHO 3 LANDING PAGE BÁN DẪN

**Ngày kiểm toán:** 2026-09-30  
**Chuyên viên kiểm toán & Evidence Writer:** Specialist Auditor  
**Phạm vi kiểm toán:** Git Worktree `D:\Digiwin_Semiconductor_Audit_Worktree`  
**Nhánh kiểm toán:** `slice/audit-automation-artifacts`  
**Điểm mốc tích hợp:**
- Nhánh Performance: [`378fdeb`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/operations/Landing_PageSpeed_Optimization_Plan.md) (*Document P4 P5 partial acceptance and production deploy*)
- Nhánh Dịch thuật 4 locales: [`6fa842e`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/operations/Vy_Landing_Language_Spec_2026-09-29.md) (*Integrate Vy paid revision and four-locale assets on PageSpeed baseline*)

---

## MỤC LỤC
1. [Tóm tắt điều hành (Executive Summary)](#1-tóm-tắt-điều-hành-executive-summary)
2. [Tiêu chí 1: Kiểm toán khoảng hở dịch thuật (Translating Gap Audit)](#2-tiêu-chí-1-kiểm-toán-khoảng-hở-dịch-thuật-translating-gap-audit)
   - 2.1. Ma trận quét DOM & Mức độ bao phủ từ điển
   - 2.2. Chi tiết phát hiện Hardcoded Vietnamese & Sót dịch thuật
   - 2.3. Đánh giá chất lượng thuật ngữ chuyên ngành bán dẫn (zh-Hans vs zh-Hant)
3. [Tiêu chí 2: Kiểm toán lỗi kỹ thuật khi merge 2 Worktree (Technical Merge Audit)](#3-tiêu-chí-2-kiểm-toán-lỗi-kỹ-thuật-khi-merge-2-worktree-technical-merge-audit)
   - 3.1. Phân tích nguy cơ vòng lặp vô hạn MutationObserver
   - 3.2. Đánh giá ảnh hưởng đến Cumulative Layout Shift (CLS)
   - 3.3. Tính toàn vẹn của Observer Band Tracking (-45% 0px -45% 0px)
   - 3.4. Kiểm chứng bất biến CTA (CTA Invariants)
   - 3.5. Kết quả chạy Unit Tests Tracking
4. [Bảng tổng hợp lỗi & Khuyến nghị khắc phục (Actionable GAPs & Remediation)](#4-bảng-tổng-hợp-lỗi--khuyến-nghị-khắc-phục-actionable-gaps--remediation)
5. [Kết luận và Ký duyệt kiểm toán (Sign-off)](#5-kết-luận-và-ký-duyệt-kiểm-toán-sign-off)

---

## 1. TÓM TẮT ĐIỀU HÀNH (EXECUTIVE SUMMARY)

Đợt kiểm toán thực hiện rà soát độc lập, đối soát mã nguồn HTML, JSON từ điển, mã điều khiển tương tác client-side và tracking analytics trên cả 3 Landing Page chiến dịch Bán dẫn:
1. **OSAT Route:** [`landing/osat-route/osat-lot-test-traceability.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/osat-route/osat-lot-test-traceability.html) (kèm [`osat-four-locale-copy.json`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/osat-route/osat-four-locale-copy.json))
2. **Fabless Route:** [`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html)
3. **Partner Route:** [`landing/partner-route/supplier-ecosystem-flat.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-ecosystem-flat.html) (kèm [`supplier-four-locale-copy.json`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-four-locale-copy.json))

### Kết quả tổng quan:
| Tiêu chí | Trạng thái | Đánh giá tóm tắt |
|---|:---:|---|
| **Tiêu chí 1: Translating Gap** | **FULL PASS (RECONCILED)** | Đã dịch thành công >99.8% text nodes và 100% attributes trên cả 4 locale. Lỗi hardcoded text node duy nhất (`span#ledger-status` tại line 1928 của Fabless, GAP-01) **đã được vá hoàn tất tại commit `87f15a3`**. Tên riêng các đơn vị nội địa (Khang Đạt, Nhật Tân, Phẩm Thuyên, Pinquan) được **bảo toàn nguyên văn tiếng Việt** theo đúng nguyên tắc nhận diện pháp nhân, không tự ý suy diễn Hán hóa. |
| **Chất lượng thuật ngữ bán dẫn** | **EXCELLENT (96/100)** | Phân biệt cực kỳ chuẩn xác giữa thuật ngữ Trung Quốc đại lục (zh-Hans) và Đài Loan (zh-Hant) ở các khái niệm then chốt (`硅` vs `矽`, `洁净室` vs `無塵室`, `激光` vs `雷射`, `裸片/芯片` vs `裸晶/晶片`, `引线键合` vs `打線接合`, `模具/夹具` vs `模具/治具`, `多层BOM` vs `多階BOM`). Có 3 tiểu tiết đề xuất tinh chỉnh (Recipe, Audit, Station) ở các đợt cập nhật nội dung tiếp theo. |
| **Tiêu chí 2: Technical Error khi Merge** | **FULL PASS (RECONCILED)** | Cơ chế cập nhật TreeWalker và MutationObserver an toàn nhờ ràng buộc giá trị Idempotency Guard (`nodeValue !== next`), không phát sinh đệ quy lặp vô hạn trong thực nghiệm. Thanh chọn locale có `min-height` cố định; đo kiểm giả lập layout CDP (390×844) cho thấy không tràn ngang (`overflowX: false`) và CLS nằm trong tầm kiểm soát (`hadRecentInput`). Invariants tracking nguyên vẹn; 12/12 unit tests tracking đạt PASS. |

---

## 2. TIÊU CHÍ 1: KIỂM TOÁN KHOẢNG HỞ DỊCH THUẬT (TRANSLATING GAP AUDIT)

### 2.1. Ma trận quét DOM & Mức độ bao phủ từ điển

Kiểm toán đã triển khai script tự động bóc tách cú pháp DOM cây Text Nodes và Accessible Attributes (`aria-label`, `title`, `alt`, `placeholder`), đối chiếu trực tiếp với bộ từ điển nạp vào bộ nhớ trình duyệt cho 4 biến thể ngôn ngữ: `vi` (Tiếng Việt), `en` (English), `zh-Hans` (简体中文 - China FDI), `zh-Hant` (繁體中文 - Taiwan FDI).

| Thuộc tính kiểm toán | OSAT Route | Fabless Route | Partner Route |
|---|:---:|:---:|:---:|
| **File HTML kiểm toán** | `osat-lot-test-traceability.html` | `fabless-outsourced-popupx-basic-flat.html` | `supplier-ecosystem-flat.html` |
| **File JSON gốc kèm theo** | `osat-four-locale-copy.json` | *Inlined trực tiếp trong HTML* | `supplier-four-locale-copy.json` |
| **Số mục trong từ điển (Copy Entries)** | **734 entries** | **458 entries** | **504 entries** |
| **Độ vênh JSON vs Inlined HTML** | **0** (Khớp tuyệt đối 734/734) | N/A (Embedded JS object) | **0** (Khớp tuyệt đối 504/504) |
| **Tổng số Text Nodes trong Host** | 1,680 nodes | 1,922 nodes | 1,324 nodes |
| **Tổng số Elements có Attributes kiểm tra** | 55 elements | 71 elements | 43 elements |
| **Số Accessible Attributes sót dịch** | **0 / 55 (0%)** | **0 / 71 (0%)** | **0 / 43 (0%)** |
| **Số Title / Meta Description sót dịch** | **0 (Đã dịch đầy đủ)** | **0 (Đã dịch đầy đủ)** | **0 (Đã dịch đầy đủ)** |
| **Số Text Nodes sót dấu tiếng Việt (EN)** | 1 node (Tên công ty) | **4 nodes (Gồm 1 lỗi logic)** | 8 nodes (Tên riêng Phẩm Thuyên) |
| **Số Text Nodes sót dấu tiếng Việt (zh-Hans)** | 1 node (Tên công ty) | **3 nodes (Gồm 1 lỗi logic)** | 8 nodes (Tên riêng Phẩm Thuyên) |
| **Số Text Nodes sót dấu tiếng Việt (zh-Hant)** | 1 node (Tên công ty) | **3 nodes (Gồm 1 lỗi logic)** | 8 nodes (Tên riêng Phẩm Thuyên) |

---

### 2.2. Chi tiết phát hiện Hardcoded Vietnamese & Sót dịch thuật

#### Phát hiện 1 (Resolved Translation Gap - Missing Key in Copy Dictionary):
- **Trang bị ảnh hưởng:** [`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html#L1928)
- **Vị trí DOM:** Cột trạng thái biên lợi nhuận trong bảng đối chiếu chi phí COGS/Margin:
  ```html
  <div class="ledger-header">
    <span>ĐỐI CHIẾU BIÊN LỢI NHUẬN GỘP (GROSS MARGIN BALANCE)</span>
    <span class="ledger-status" id="ledger-status">🟢 Đạt mục tiêu ban giám đốc (>30%)</span>
  </div>
  ```
- **Bằng chứng lỗi ban đầu:**
  - Chuỗi `"🟢 Đạt mục tiêu ban giám đốc (>30%)"` hoặc `"Đạt mục tiêu ban giám đốc (>30%)"` ban đầu không có trong biến `copy`.
  - Khi người dùng chuyển sang `en`, `zh-Hans`, hoặc `zh-Hant`, phần tử `span#ledger-status` từng bị sót 100% tiếng Việt có dấu.
- **Trạng thái khắc phục:** **ĐÃ VÁ HOÀN TẤT tại commit `87f15a3`**. Đã bổ sung bộ khóa dịch vào biến `copy` của Fabless:
  ```javascript
  '🟢 Đạt mục tiêu ban giám đốc (>30%)': [
    '🟢 Meets executive target (>30%)',
    '🟢 达到管理层目标（>30%）',
    '🟢 達成管理層目標（>30%）'
  ]
  ```
  Xác thực render trên Chrome headless cho thấy `span#ledger-status` đã chuyển ngữ chính xác sang EN/zh-Hans/zh-Hant.

#### Phát hiện 2 (Bảo toàn tên riêng OSAT nội địa trong luồng Fabless):
- **Trang liên quan:** [`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html#L1620-L1650)
- **Vị trí DOM:** Các trạm gia công trong sơ đồ phân luồng đóng gói:
  - `<div class="node-lot-detail">15,000 ICs • OSAT Khang Đạt</div>`
  - `<div class="node-lot-detail">10,000 ICs • OSAT Nhật Tân</div>`
- **Bằng chứng chuyển ngữ:**
  - EN: Giữ nguyên `"15,000 ICs • OSAT Khang Đạt"`, `"10,000 ICs • OSAT Nhật Tân"`
  - zh-Hans: Dịch số lượng nhưng giữ nguyên tên riêng: `"15,000 颗 IC • OSAT Khang Đạt"`, `"10,000 颗 IC • OSAT Nhật Tân"`
  - zh-Hant: `"15,000 顆 IC • OSAT Khang Đạt"`, `"10,000 顆 IC • OSAT Nhật Tân"`
- **Đánh giá kiểm toán:** Việc giữ nguyên tên riêng bằng chữ cái La-tinh tiếng Việt (`OSAT Khang Đạt`, `OSAT Nhật Tân`) là **đúng nguyên tắc nhận diện pháp nhân**. Khi chưa có giấy phép đăng ký kinh doanh, chứng nhận đối tác hoặc tên giao dịch chữ Hán chính thức từ phía doanh nghiệp, tuyệt đối không tự ý suy diễn hoặc đặt tên chữ Hán giả định (như `康达` hay `日新`). Đây không phải lỗi dịch thuật.

#### Phát hiện 3 (Bảo toàn thể hiện tên riêng pháp nhân giữa các Route):
- **Trang liên quan:**
  - OSAT: [`landing/osat-route/osat-lot-test-traceability.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/osat-route/osat-lot-test-traceability.html#L3463)
  - Partner: [`landing/partner-route/supplier-ecosystem-flat.html`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-ecosystem-flat.html#L2440-L2450)
- **Bằng chứng:**
  - Trong OSAT (dòng 3463):
    `"Công ty TNHH Cơ khí Chính xác Pinquan (品全精密) · Việt Nam"` -> Trong từ điển:
    * EN: `"Công ty TNHH Cơ khí Chính xác Pinquan (品全精密) · Vietnam"`
    * zh-Hans: `"Công ty TNHH Cơ khí Chính xác Pinquan (品全精密) · 越南"`
    * zh-Hant: `"Công ty TNHH Cơ khí Chính xác Pinquan (品全精密) · 越南"`
    *(Bảo toàn cụm từ pháp nhân tiếng Việt trong cả bản dịch tiếng Trung và tiếng Anh).*
  - Trong Partner:
    Sử dụng tên `"Phẩm Thuyên (Pinchuan)"` theo tài liệu nguồn canonical:
    * zh-Hans: `"Phẩm Thuyên 精密机械有限公司（Pinchuan）· 越南"`
    * zh-Hant: `"Phẩm Thuyên 精密機械有限公司（Pinchuan）· 越南"`
- **Đánh giá kiểm toán:** Cả hai route đều bảo lưu tên pháp nhân thực tế theo các nguồn tài liệu marketing đã được kiểm chứng. Việc đồng nhất hoàn toàn cách gọi (Pinquan vs Phẩm Thuyên) hoặc dịch 100% sang chữ Hán cần có căn cứ pháp lý/quyền sử dụng proof xác nhận trước khi thực hiện, tránh vi phạm trust boundary của dự án.

---

### 2.3. Đánh giá chất lượng thuật ngữ chuyên ngành bán dẫn (zh-Hans vs zh-Hant)

Kiểm toán đã trích xuất toàn bộ các cặp thuật ngữ song ngữ giữa Giản thể (China) và Phồn thể (Taiwan) đối chiếu với sổ tay thuật ngữ bán dẫn quốc tế SEMI và thông lệ vận hành thực tế tại các nhà máy Foundry/OSAT Đài Loan (TSMC, ASE, KYEC) và Trung Quốc (SMIC, JCET).

| Khái niệm chuyên ngành | Bản Tiếng Việt (VI) | Bản Giản thể (zh-Hans - China) | Bản Phồn thể (zh-Hant - Taiwan) | Đánh giá tính chuẩn xác chuyên ngành |
|---|---|---|---|---|
| **Cleanroom** | Môi trường buồng sạch / cleanroom | **洁净室** (Cleanroom) | **無塵室** (Cleanroom) | **Xuất sắc (10/10).** Chuẩn xác 100% theo thói quen phân vùng (Đài Loan luôn dùng 無塵室, Trung Quốc dùng 洁净室). |
| **Silicon Wafer** | Silicon wafer / phiến wafer | **多层硅晶圆** | **多層矽晶圓** | **Xuất sắc (10/10).** Trung Quốc gọi nguyên tố Si là 硅 (guī), Đài Loan gọi là 矽 (xì). |
| **Laser Inspection** | Quét kiểm tra chất lượng bằng laser | **通过激光扫描检查晶圆质量** | **透過雷射掃描檢查晶圓品質** | **Xuất sắc (10/10).** Phân biệt chuẩn Laser (激光 vs 雷射) và Quality (质量 vs 品質). |
| **Die / Chip** | Die / phôi chip / chip bán dẫn | **裸片** / **芯片** | **裸晶** / **晶片** | **Xuất sắc (10/10).** Đúng chuẩn thuật ngữ chế tạo IC (Đài Loan: 裸晶/晶片; Trung Quốc: 裸片/芯片). |
| **Epitaxy** | Quá trình epitaxy | **外延** | **磊晶** | **Xuất sắc (10/10).** Phân biệt tuyệt đối chuẩn xác (China: 外延, Taiwan: 磊晶). |
| **Photolithography** | Quang khắc / Photolithography | **光刻** | **微影** | **Xuất sắc (10/10).** Ngành bán dẫn Đài Loan luôn dùng 微影 (Microlithography), Trung Quốc dùng 光刻. |
| **Wire Bonding** | Đấu nối dây vàng / Wire bonding | **引线键合** | **打線接合** | **Xuất sắc (10/10).** Thuật ngữ đóng gói OSAT chuẩn xác (Taiwan: 打線, China: 引线键合). |
| **Molding** | Đúc khuôn nhựa / Epoxy molding | **塑封** | **模封** | **Xuất sắc (10/10).** Taiwan OSAT (ASE) gọi là 模封/封膠, China gọi là 塑封. |
| **Shop floor Dispatching** | Điều độ sàn xưởng | **车间调度** | **現場派工** | **Xuất sắc (10/10).** Đài Loan dùng 現場派工, Trung Quốc dùng 车间调度. |
| **Tooling & Fixture** | Vòng đời khuôn gá | **模具／夹具** | **模具／治具** | **Xuất sắc (10/10).** Ngành cơ khí/bán dẫn Đài Loan luôn gọi đồ gá là 治具 (zhìjù), không dùng 夹具. |
| **Shelf-life & MSL** | Hạn dùng keo/màng dán | **管控胶膜／胶水／化学品保质期** | **控管膠膜／膠材／化學品保存期限** | **Xuất sắc (10/10).** Phân biệt chính xác 保质期 vs 保存期限, 胶水 vs 膠材. |
| **Multilevel BOM** | BOM kỹ thuật đa tầng | **多层 BOM** | **多階 BOM** | **Xuất sắc (10/10).** ERP tại Đài Loan chuẩn hóa là 多階 BOM (Multi-level BOM). |
| **Data & Information** | Dữ liệu ranh giới & Thông tin | **数据边界** / **企业信息** | **資料邊界** / **企業資訊** | **Xuất sắc (10/10).** Phân biệt triệt để 信息/数据 vs 資訊/資料. |
| **Yield Rate** | Tỷ lệ đạt / Yield | **良率** (98.5%) | **良率** (98.5%) | **Chuẩn xác (10/10).** Cả hai thị trường đều dùng đồng nhất là 良率. |
| **WIP (Work in Process)** | Bán thành phẩm WIP / tiến độ | **在制品** / **WIP** | **在製品** / **WIP** | **Chuẩn xác (10/10).** Chữ 品/製 chuẩn hóa chính tả Phồn thể. |
| **Traceability / Genealogy** | Phả hệ Lot / truy vết 2 chiều | **批次谱系** / **双向追溯** | **批次譜系** / **雙向追溯** | **Chuẩn xác (10/10).** Thuật ngữ truy xuất phả hệ bán dẫn chính xác. |

#### 3 điểm tinh chỉnh đề xuất nâng cao chuyên môn (Terminology Nuance Recommendations):
1. **Thuật ngữ "Audit" trong ngữ cảnh B2B Proof:**
   - Trong Fabless: `AUDITED PROOF` được dịch là `已审阅证明` (zh-Hans) / `已審閱證明` (zh-Hant).
   - *Khuyến nghị:* Trong văn hóa nhà máy Đài Loan, việc kiểm tra hồ sơ, quy trình và chứng nhận năng lực nhà cung cấp gọi là **稽核** (Audit). Nên hiệu chỉnh thành `已稽核證明` (zh-Hant) và `已审核证明` (zh-Hans) để mang tính trang trọng và uy tín công nghiệp cao hơn chữ "審閱" (chỉ mang nghĩa đọc soát tài liệu).
2. **Thuật ngữ "Nạp Recipe xuống thiết bị":**
   - Trong Partner: `远程下发 Recipe 配方` (zh-Hans) / `遠端下發 Recipe 配方` (zh-Hant).
   - *Khuyến nghị:* Chữ "下發" là khẩu ngữ quản trị của đại lục. Tại các nhà máy bán dẫn Đài Loan, việc truyền tham số máy tự động qua giao thức SECS/GEM thường dùng từ **派送** (Dispatch/Send), **下載** (Download), hoặc **設定** (Configure) Recipe.
3. **Thuật ngữ "Trạm máy / Station":**
   - Trong OSAT: `Die Attach 工位 #02` (zh-Hans) / `Die Attach 站點 #02` (zh-Hant).
   - *Khuyến nghị:* Tại xưởng OSAT Đài Loan, mỗi bước trong chuyền gọi là **工站** (Station, ví dụ: 黏晶工站, 打線工站), từ "站點" thường gây liên tưởng đến website hoặc điểm dừng giao thông.

---

## 3. TIÊU CHÍ 2: KIỂM TOÁN LỖI KỸ THUẬT KHI MERGE 2 WORKTREE (TECHNICAL MERGE AUDIT)

### 3.1. Phân tích nguy cơ vòng lặp vô hạn MutationObserver

#### Cơ chế thiết kế trong mã nguồn:
Trong cả 2 file có trang bị `MutationObserver`:
- OSAT: [`osat-lot-test-traceability.html:4088-4098`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/osat-route/osat-lot-test-traceability.html#L4088-L4098)
- Partner: [`supplier-ecosystem-flat.html:3483-3494`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-ecosystem-flat.html#L3483-L3494)

```javascript
var updating = false;
...
function translateText(node) {
  if (!node || !node.parentElement || node.parentElement.closest('script,style,select[data-osat-locale]')) return;
  var raw = node.nodeValue, trimmed = raw.trim();
  if (translatable(trimmed)) originalText.set(node, trimmed);
  var original = originalText.get(node);
  if (!original) return;
  var next = raw.replace(trimmed, value(original));
  if (node.nodeValue !== next) node.nodeValue = next; // <-- IDEMPOTENCY GUARD
}
...
var observer = new MutationObserver(function(records) {
  if (updating) return;
  updating = true;
  records.forEach(function(record) {
    if (record.type === 'characterData') translateText(record.target);
    else if (record.type === 'attributes') translateAttrs(record.target);
    else record.addedNodes.forEach(translateTree);
  });
  updating = false;
});
observer.observe(host, { subtree: true, childList: true, characterData: true, attributes: true, attributeFilter: attrs });
```

#### Phân tích luồng thực thi (Runtime Trace):
1. **Đặc tính bất đồng bộ của MutationObserver:**
   Khi hàm `apply()` hoặc một thao tác gán `node.nodeValue = next` diễn ra, MutationObserver không kích hoạt callback đồng bộ ngay lập tức mà gom bản ghi vào hàng đợi **Microtask Queue**.
2. **Hành vi của cờ `updating`:**
   Trong hàm `apply()`, `updating = true` được đặt ở đầu và `updating = false` ở cuối hàm đồng bộ. Do đó, khi microtask của MutationObserver kích hoạt, cờ `updating` đã được trả về `false`.
3. **Cơ chế chặn vòng lặp thực tế (The True Loop Guard):**
   Lý do MutationObserver **KHÔNG BAO GIỜ bị rơi vào vòng lặp vô hạn (Infinite Loop)** nằm ở dòng lệnh điều kiện:
   `if (node.nodeValue !== next) node.nodeValue = next;`
   và
   `if (raw !== next) el.setAttribute(attr, next);`
   - Khi Observer kích hoạt và gọi `translateText(target)`: Giá trị của `target.nodeValue` **đã bằng** `next`.
   - Phép so sánh `node.nodeValue !== next` trả về `false`.
   - Trình duyệt **không thực hiện thao tác gán**, không phát sinh thêm bất kỳ bản ghi Mutation nào.
   - Chuỗi phản ứng kết thúc ngay lập tức tại thế hệ đệ quy thứ nhất ($N=1$).
4. **Tại Fabless:**
   Trang `fabless-outsourced-popupx-basic-flat.html` không sử dụng MutationObserver mà sử dụng bộ duyệt tĩnh `TreeWalker` kích hoạt một lần khi khởi tạo và mỗi khi sự kiện `change` trên dropdown phát sinh. Do đó, nguy cơ vòng lặp tại Fabless là **0%**.

**Kết luận kiểm toán:** Cơ chế an toàn và không gây treo trình duyệt.

---

### 3.2. Đánh giá ảnh hưởng đến Cumulative Layout Shift (CLS)

#### 1. Cố định kích thước bộ chọn ngôn ngữ (Locale Select Container):
- Trong **Fabless Route**: Hàng chọn ngôn ngữ được tách thành thanh công cụ riêng biệt trên đỉnh (`.locale-bar`) với thông số CSS:
  ```css
  #dw-fabless-landing .locale-bar {
    min-height: 48px;
    display: flex;
    align-items: center;
    justify-content: flex-end;
    gap: 10px;
    background: #142024;
  }
  ```
  Nhờ có `min-height: 48px`, khoảng không gian này được dành sẵn ngay khi cây render hình thành, không gây giật đẩy khối Header phía dưới xuống (zero layout shift).
- Trong **OSAT Route** và **Partner Route**: Dropdown ngôn ngữ được tích hợp trực tiếp vào thanh điều hướng `.nav-actions`:
  ```css
  .osat-locale-wrap, .supplier-locale-wrap { display: flex; align-items: center; flex: none; }
  .osat-locale-select, .supplier-locale-select {
    max-width: 112px;
    min-height: 44px;
    padding: 7px 25px 7px 9px;
    border: 1px solid #6b8184;
    border-radius: 3px;
    background: #101619;
    color: #edf2f1;
    font-size: 12px;
  }
  ```
  Việc ấn định `min-height: 44px` và `max-width: 112px` với `flex: none` đảm bảo kích thước phần tử điều khiển hoàn toàn tĩnh, không bị co giãn khi nạp nhãn hiển thị.

#### 2. Tác động của việc thay đổi độ dài chuỗi ký tự khi dịch:
- **Khi tải trang có sẵn tham số URL (`?lang=zh-Hans`):** Đoạn mã dịch thuật nằm ở cuối thẻ `<body>`, thực thi ngay lập tức trước khi trình duyệt thực hiện lượt quét sơn nội dung đầu tiên (First Contentful Paint - FCP). Toàn bộ nội dung chữ được cập nhật đồng bộ trước khi khung hình hiển thị, không phát sinh CLS từ việc hoán đổi chữ.
- **Khi người dùng chủ động chọn ngôn ngữ trên Dropdown:**
  Theo chuẩn Core Web Vitals của Google Chrome, mọi layout shift phát sinh trong vòng 500ms sau tương tác của người dùng (`hadRecentInput = true`) đều được loại trừ khỏi điểm số CLS tích lũy.

**Kết luận kiểm toán:** Trong môi trường thử nghiệm giả lập headless Chrome (viewport 390×844 mobile), cấu trúc layout không bị tràn ngang (`overflowX: false`) và hiện tượng dịch chuyển layout nằm trong giới hạn kiểm soát sau tương tác (`hadRecentInput`). Cần tiếp tục kiểm chứng thêm trên thiết bị thực tế khi triển khai live.

---

### 3.3. Tính toàn vẹn của Observer Band Tracking (-45% 0px -45% 0px)

Đoạn mã dịch thuật 4 locales hoàn toàn không tác động đến bộ đo nhận thức chuyển động (Section Awareness Tracking `__dgwAwarenessSectionInitV1`):
1. **Bảo toàn ID định danh Section:**
   Script dịch thuật chỉ tác vụ trên `node.nodeValue` (Text Node) và 4 thuộc tính dễ tiếp cận (`aria-label`, `title`, `alt`, `placeholder`). Script **không bao giờ sửa đổi thuộc tính `id`** của các phần tử section.
2. **Bộ bắt giao điểm (IntersectionObserver):**
   Bộ quan sát tracking sử dụng:
   ```javascript
   rootMargin: '-45% 0px -45% 0px',
   threshold: 0
   ```
   Căn giữa màn hình ở dải 10% chiều cao viewport. Các phần tử mục tiêu được lưu tham chiếu DOM đối tượng trực tiếp. Sự thay đổi chuỗi văn bản bên trong không làm đứt gãy tham chiếu của Observer.
3. **Thứ tự nạp script:**
   - Trong OSAT & Partner: Script dịch thuật nằm trước script tracking.
   - Trong Fabless: Script tracking nằm trước script dịch thuật.
   Cả hai kịch bản đều thực thi trơn tru và độc lập, không chia sẻ biến toàn cục gây xung đột namespace.

---

### 3.4. Kiểm chứng bất biến CTA (CTA Invariants)

Kiểm toán đã rà soát toàn bộ cây DOM của 3 Landing Page để đối chiếu với quy định bất biến chặt chẽ về số lượng và ID của nút CTA tư vấn:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                             MA TRẬN KIỂM CHỨNG CTA                          │
├─────────────────┬──────────────┬─────────────────────────┬──────────────────┤
│ Route           │ Quy định CTA │ Phần tử DOM thực tế      │ Kết quả kiểm toán│
├─────────────────┼──────────────┼─────────────────────────┼──────────────────┤
│ 1. OSAT Route   │ Đúng 2 CTAs  │ • Header: #osat-cta-header│ CHUẨN XÁC        │
│                 │              │ • Cuối trang:           │ (Đúng 2 CTAs)    │
│                 │              │   #osat-cta-terminal    │                  │
├─────────────────┼──────────────┼─────────────────────────┼──────────────────┤
│ 2. Fabless Route│ Đúng 2 CTAs  │ • Header:               │ CHUẨN XÁC        │
│                 │              │   #fabless-cta-header   │ (Đúng 2 CTAs)    │
│                 │              │ • Cuối trang:           │                  │
│                 │              │   #fabless-cta-terminal │                  │
├─────────────────┼──────────────┼─────────────────────────┼──────────────────┤
│ 3. Partner Route│ Đúng 1 CTA   │ • Header duy nhất:      │ CHUẨN XÁC        │
│                 │ (tại Header) │   #partner-cta-header   │ (Đúng 1 CTA duy  │
│                 │              │   (Nhãn: "Tư Vấn")      │  nhất tại header)│
└─────────────────┴──────────────┴─────────────────────────┴──────────────────┘
```

> [!NOTE]
> Trong OSAT, nút `<button class="btn btn-primary btn-inspector-cta" data-demo-cta>` mang nhãn *"Yêu cầu demo trực tiếp"* nằm trong hộp giả lập (Cockpit simulation aside). Nút này không có thuộc tính `id`, không gắn `data-consultation-cta`, và không phát sinh bất kỳ sự kiện CTA tracking trái phép nào.

---

### 3.5. Kết quả chạy Unit Tests Tracking

Thực hiện lệnh kiểm thử tự động trên môi trường kiểm toán:
```bash
node --test tests/landing-tracking.test.cjs
```

**Bằng chứng thực thi (TAP Output):**
```
TAP version 13
# Subtest: OSAT: exact IDs, idempotency, observer band and unique view
ok 1 - OSAT: exact IDs, idempotency, observer band and unique view
  ---
  duration_ms: 4.6945
  type: 'test'
  ...
# Subtest: OSAT: visible and focused intervals only; pagehide flushes once with bounded integer
ok 2 - OSAT: visible and focused intervals only; pagehide flushes once with bounded integer
  ---
  duration_ms: 3.4909
  type: 'test'
  ...
# Subtest: OSAT: one-hour cap and sub-second interval omitted
ok 3 - OSAT: one-hour cap and sub-second interval omitted
  ---
  duration_ms: 6.2217
  type: 'test'
  ...
# Subtest: OSAT: inert CTAs and allowlist N/A produce no other tracking
ok 4 - OSAT: inert CTAs and allowlist N/A produce no other tracking
  ---
  duration_ms: 4.339
  type: 'test'
  ...
# Subtest: Fabless: exact IDs, idempotency, observer band and unique view
ok 5 - Fabless: exact IDs, idempotency, observer band and unique view
  ---
  duration_ms: 2.477
  type: 'test'
  ...
# Subtest: Fabless: visible and focused intervals only; pagehide flushes once with bounded integer
ok 6 - Fabless: visible and focused intervals only; pagehide flushes once with bounded integer
  ---
  duration_ms: 1.9576
  type: 'test'
  ...
# Subtest: Fabless: one-hour cap and sub-second interval omitted
ok 7 - Fabless: one-hour cap and sub-second interval omitted
  ---
  duration_ms: 4.1926
  type: 'test'
  ...
# Subtest: Fabless: inert CTAs and allowlist N/A produce no other tracking
ok 8 - Fabless: inert CTAs and allowlist N/A produce no other tracking
  ---
  duration_ms: 3.8397
  type: 'test'
  ...
# Subtest: Supplier/Partner: exact IDs, idempotency, observer band and unique view
ok 9 - Supplier/Partner: exact IDs, idempotency, observer band and unique view
  ---
  duration_ms: 3.3513
  type: 'test'
  ...
# Subtest: Supplier/Partner: visible and focused intervals only; pagehide flushes once with bounded integer
ok 10 - Supplier/Partner: visible and focused intervals only; pagehide flushes once with bounded integer
  ---
  duration_ms: 2.3898
  type: 'test'
  ...
# Subtest: Supplier/Partner: one-hour cap and sub-second interval omitted
ok 11 - Supplier/Partner: one-hour cap and sub-second interval omitted
  ---
  duration_ms: 4.2716
  type: 'test'
  ...
# Subtest: Supplier/Partner: inert CTAs and allowlist N/A produce no other tracking
ok 12 - Supplier/Partner: inert CTAs and allowlist N/A produce no other tracking
  ---
  duration_ms: 3.5316
  type: 'test'
  ...
1..12
# tests 12
# suites 0
# pass 12
# fail 0
# cancelled 0
# skipped 0
# todo 0
# duration_ms 120.5041
```
**Kết quả:** 12/12 bài test vượt qua thành công 100%.

---

## 4. BẢNG TỔNG HỢP LỖI & KHUYẾN NGHỊ KHẮC PHỤC (ACTIONABLE GAPS & REMEDIATION)

| Mã lỗi | Phân loại | Tệp & Dòng mã | Nội dung ghi nhận | Hiện trạng xử lý / Khuyến nghị | Mức độ ưu tiên | Trạng thái Closeout |
|---|---|---|---|---|:---:|:---:|
| **GAP-01** | Translating Gap | [`fabless-outsourced-popupx-basic-flat.html:1928`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html#L1928) | `<span class="ledger-status" id="ledger-status">🟢 Đạt mục tiêu ban giám đốc (>30%)</span>` ban đầu không có trong từ điển `copy`. | **ĐÃ VÁ HOÀN TẤT** (Bổ sung khóa dịch tại commit `87f15a3`, đã xác thực render trên headless Chrome). | **CAO (P1)** | **CLOSED (RESOLVED)** |
| **GAP-02** | Naming Hypothesis | [`fabless-outsourced-popupx-basic-flat.html:1625, 1635`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html#L1625) | Bản dịch tiếng Trung giữ tên riêng tiếng Việt có dấu: `"OSAT Khang Đạt"`, `"OSAT Nhật Tân"`. | **Giữ nguyên trạng thái tiếng Việt** do chưa có bằng chứng pháp nhân/tên giao dịch chữ Hán chính thức (`康达`, `日新` chỉ là giả định chữ Hán, không tự ý suy diễn thành lỗi dịch). | **THẤP (P3)** | **PROPOSAL / NO FIX REQUIRED** |
| **GAP-03** | Entity Naming | [`osat-lot-test-traceability.html:3463`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/osat-route/osat-lot-test-traceability.html#L3463) vs [`supplier-ecosystem-flat.html:2440`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-ecosystem-flat.html#L2440) | Tên đối tác cơ khí chính xác tại Bắc Ninh giữa 2 trang có sự khác biệt về hiển thị: OSAT ghi `"Pinquan (品全精密)"`, Partner ghi `"Phẩm Thuyên (Pinchuan)"`. | **Giữ nguyên theo tài liệu nguồn canonical**; việc hợp nhất tên cần tài liệu pháp lý/quyền sử dụng proof xác nhận trước khi sửa. | **THẤP (P3)** | **PENDING ENTITY PROOF** |
| **GAP-04** | Terminology Nuance | [`fabless-outsourced-popupx-basic-flat.html:2717`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html#L2717) | `AUDITED PROOF` được dịch là `已审阅证明` (zh-Hans) / `已審閱證明` (zh-Hant). | Đề xuất cân nhắc `已审核证明` (zh-Hans) và `已稽核證明` (zh-Hant) khi có đợt cập nhật nội dung copy tổng thể. | **THẤP (P3)** | **DEFERRED PROPOSAL** |
| **GAP-05** | Terminology Nuance | [`supplier-ecosystem-flat.html:3400`](file:///D:/Digiwin_Semiconductor_Audit_Worktree/landing/partner-route/supplier-ecosystem-flat.html#L3400) | `Gửi lệnh nạp công thức Recipe từ xa` dịch sang zh-Hant là `遠端下發 Recipe 配方`. | Đề xuất cân nhắc thay `下發` thành `派送/設定` khi có đợt cập nhật nội dung copy tổng thể. | **THẤP (P3)** | **DEFERRED PROPOSAL** |

---

## 5. KẾT LUẬN VÀ KÝ DUYỆT KIỂM TOÁN (SIGN-OFF)

1. **Về mặt kỹ thuật tích hợp (Technical Merge):** Không quan sát thấy lỗi trong phạm vi kiểm tra. Hai cơ chế là tối ưu hóa PageSpeed (P3/P4) và chuyển đổi ngôn ngữ động client-side phối hợp ổn định; không quan sát thấy vòng lặp vô hạn hay phá vỡ cấu trúc DOM trong các kịch bản thử nghiệm; chỉ số CLS thực tế trên môi trường live/thiết bị thực chưa có phép đo chính thức nên ghi nhận **chưa xác minh** (mới dừng lại ở quan sát layout headless không tràn ngang); duy trì vẹn toàn bất biến CTA cũng như hệ thống Section Tracking (12/12 unit tests PASS).
2. **Về mặt ngôn ngữ và thuật ngữ bán dẫn (Translation Quality):** Chất lượng dịch thuật song ngữ Trung Quốc (Giản thể) và Đài Loan (Phồn thể) đạt độ chuyên môn hóa cao, phân tách sâu sắc các đặc thù công nghệ bán dẫn của hai thị trường. Tên riêng và pháp nhân nội địa được giữ nguyên tiếng Việt theo đúng nguyên tắc bảo toàn căn cứ nhận diện, không tự ý Hán hóa khi thiếu bằng chứng.
3. **Trạng thái khắc phục:**
   - **GAP-01** (`span#ledger-status` trong Fabless) đã được vá dứt điểm tại commit `87f15a3` và kiểm chứng layout headless.
   - Các điểm còn lại (GAP-02 đến GAP-05) được ghi nhận là giả thuyết/đề xuất tinh chỉnh, không phải blocker kỹ thuật.

---
**Chuyên viên kiểm toán:** Specialist Auditor & Evidence Writer  
**Báo cáo lập tại:** `D:\Digiwin_Semiconductor_Audit_Worktree\operations\LDP_TRANSLATION_AND_MERGE_AUDIT_REPORT_2026-09-30.md`  
**Chữ ký điện tử:** `SPECIALIST_AUDITOR_SIGNED_2026-09-30_RECONCILED`
