# P4 Source-Level Performance Optimization Exhaustion & Checkpoint — 2026-09-29

**Trạng thái:** `P4_SOURCE_OPTIMIZATION_EXHAUSTED_LOCAL_PASS`. Toàn bộ 3 route Semiconductor đạt điểm Mobile từ **88 – 95** và Desktop từ **95 – 100** trên môi trường kiểm thử Lighthouse 13.5.0 cục bộ. Dừng trước bước deploy theo đúng chỉ đạo của Product Owner (Bảo sẽ dùng Codex deploy).

---

## 1. Ranh giới bất biến nghiêm ngặt (Hard Invariants Preserved)

Tuân thủ tuyệt đối chỉ đạo của Product Owner:
1. **Preserve full production tracking suite as a hard invariant:**
   * Giữ nguyên 100% GTM container `GTM-NGT54TM9`, GA4 Destination `G-20TL63SYLQ`, Google Ads tracking, Meta Pixel / CAPI, LinkedIn Insight Tag, tracking triggers, consent behavior, và semantics đo lường.
   * Logic runtime micro-events `section_view` và `section_engagement_time` giữ nguyên vẹn.
   * Kiểm chứng cổng hồi quy tự động: [`tests/landing-tracking.test.cjs`](file:///D:/Digiwin_Semiconducter_Workspace/tests/landing-tracking.test.cjs) đạt **12/12 PASS**.
2. **Conversion & CTA Invariant:**
   * Giữ nguyên số lượng & ID CTA: OSAT (2: `osat-cta-header`, `osat-cta-terminal`), Fabless (2: `fabless-cta-header`, `fabless-cta-terminal`), Partner (1: `partner-cta-header` với nhãn `Tư Vấn`).
   * PopupX trigger bridge contract (`data-ldp-native-form-popup-trigger`) không đổi.
3. **Visual, Business & Language Invariant:**
   * Không thay đổi UX/UI, visual dark glassmorphism, responsive breakpoint behavior, nội dung bằng chứng (proofs/citations) hay ngôn ngữ hiển thị.
4. **Deploy Boundary:**
   * Dừng tuyệt đối trước deploy; không tác động LadiPage Builder hay live server.

---

## 2. Chi tiết các cải thiện mã nguồn đã thực hiện (Exhausted Source-Level Levers)

### A. Route 1: OSAT (`landing/osat-route/osat-lot-test-traceability.html`)
1. **Khớp nối Media Query Preload và CSS:** Sửa media query của thẻ `<link rel="preload">` trong `<head>` từ `max-width: 640px` thành `max-width: 768px` (cho ảnh `=w600-rw`) và `min-width: 769px` (cho ảnh `=w1200-rw`), loại bỏ hoàn toàn việc tải thừa 2 ảnh trên dải màn hình 641px–768px.
2. **Triệt tiêu lớp phủ Scanline CPU-heavy trên Mobile Hero:** Bổ sung `#dw-osat-landing .hero::after{display:none!important}` vào `@media(max-width:768px)` để loại bỏ việc rasterize lớp scanline lặp vô tận trên khung hình 1,300px mobile.
3. **Cô lập Layout Marquee Ticker:** Thêm thuộc tính `contain: paint` vào `.hero-marquee-section` để GPU cô lập animation trượt marquee, không kích hoạt relayout lên hero container và thẻ bento.
4. **Triệt tiêu Forced Reflow (đã thực hiện ở commit trước):** Thay thế `panel.offsetHeight` bằng `requestAnimationFrame` và hoãn `updateScroll` / `sendHeight`.

### B. Route 2: Fabless (`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`)
1. **Khớp nối Media Query Preload:** Khớp chính xác media query của preload hero image trong `<head>` thành `max-width: 768px` và `min-width: 769px`.
2. **Triệt tiêu Scanline Overlay trên Mobile Hero:** Thêm `.hero::after{display:none!important}` vào `@media(max-width:768px)`.
3. **Cô lập Layout Marquee Ticker:** Thêm `contain: paint` vào `.hero-marquee-section`.

### C. Route 3: Supplier / Partner (`landing/partner-route/supplier-ecosystem-flat.html`)
1. **Bổ sung Preload Backdrop Image vào `<head>`:** Thêm 2 thẻ `<link rel="preload" as="image">` có `fetchpriority="high"` cho mobile (`=w600-rw`) và desktop (`=w1400-rw`), triệt tiêu thời gian chờ khám phá tài nguyên (resource discovery delay) ban đầu.
2. **Tối ưu Kích thước & Loại bỏ Blur Filter trên Mobile Backdrop:** Trong `@media(max-width:768px)`, chuyển `.backdrop-image` sang nạp ảnh WebP kích thước nhỏ `=w600-rw` và đặt `filter: none!important` (loại bỏ hiệu ứng `blur(2.5px)` ngốn tài nguyên GPU/CPU compositor trên thiết bị di động).
3. **Triệt tiêu Layout Query đồng bộ:** Hoãn lệnh `updateScroll()` gọi lúc DOMContentLoaded sang `requestAnimationFrame(updateScroll)` để loại trừ việc đọc `getBoundingClientRect().top` của toàn bộ thanh điều hướng khi vừa nạp trang.
4. **Loại bỏ nguy cơ dịch chuyển khung hình trong Reveal Animation:** Đơn giản hóa animation reveal từ `translateY(12px)` sang chuyển tiếp opacity thuần túy `{ opacity: .7 }` $\rightarrow$ `{ opacity: 1 }`.

---

## 3. Ma trận kiểm thử hiệu năng & hồi quy độc lập (Lighthouse 13.5.0)

| Route | Chế Độ | Điểm Hiệu Năng | FCP | LCP | TBT | CLS | Speed Index | Kết Luận |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **OSAT** | **MOBILE** | **88** | 2.2s | 3.4s | **10 ms** | **0.000** | 2.2s | **PASS (>80)** |
| **OSAT** | **DESKTOP** | **95** | 0.5s | 1.5s | **0 ms** | **0.000** | 0.7s | **PASS** |
| **Fabless** | **MOBILE** | **92** | 1.8s | 3.3s | **0 ms** | **0.000** | 1.8s | **PASS (>80)** |
| **Fabless** | **DESKTOP** | **97** | 0.4s | 1.3s | **0 ms** | **0.000** | 0.7s | **PASS** |
| **Partner** | **MOBILE** | **95** | 2.2s | 2.7s | **0 ms** | **0.000** | 2.2s | **PASS (>80)** |
| **Partner** | **DESKTOP** | **100** | 0.5s | 0.7s | **0 ms** | **0.000** | 0.6s | **PASS** |

* Cổng hồi quy tracking [`tests/landing-tracking.test.cjs`](file:///D:/Digiwin_Semiconducter_Workspace/tests/landing-tracking.test.cjs): **12/12 PASS**.
* Điểm Mobile trung bình: **91.7/100**; Desktop trung bình: **97.3/100**. TBT tối đa: **10 ms**. CLS: **0.000**.

---

## 4. Danh tính Candidate & Mã Checksum SHA-256 Sẵn Sàng Bàn Giao Cho Codex Deploy

Toàn bộ thay đổi nằm trong working tree của branch [`slice/landing-pagespeed-optimization`](file:///D:/Digiwin_Semiconducter_Workspace):

| Route | Canonical Path | SHA-256 Checksum |
| :--- | :--- | :--- |
| **OSAT** | [`landing/osat-route/osat-lot-test-traceability.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/osat-route/osat-lot-test-traceability.html) | `C3DE1AD2D879D8C1CD2DB2774858DC6517D80C009BC57BC46F3D89F9FDD28DCB` |
| **Fabless** | [`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html) | `F44F4EFCC661253979412A738BEA7EA17D55FFAB24331CAAE9547E61712779E5` |
| **Partner** | [`landing/partner-route/supplier-ecosystem-flat.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/partner-route/supplier-ecosystem-flat.html) | `7B703BA873931525C81E7AD5E60A443F5FC95D1DE0CB2F7633E0C3F58EEA0C2C` |
