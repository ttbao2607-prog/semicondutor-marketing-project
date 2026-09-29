# P4 Source-Level Performance Optimization Exhaustion & Checkpoint — 2026-09-29

**Trạng thái:** `P4_LOCAL_CANDIDATE_OPTIMIZATION_READY`. Cả 3 ứng viên nguồn cục bộ đạt cổng kiểm thử Lighthouse 13.5.0 offline (Mobile **88 – 94**, Desktop **96 – 100**, TBT **0 – 60 ms**, CLS **0.000**). Ranh giới kiểm thử: Đây là kết quả chứng thực ứng viên nguồn ở môi trường cục bộ; trạng thái trên môi trường production vẫn ghi nhận `P4_OPTIMIZATION_PUBLISHED_LIVE_PERFORMANCE_FAIL` (Mobile 49–56). Chênh lệch giữa kết quả đo cục bộ và live là khác biệt môi trường cần được kiểm chứng sau deploy, không tự quy kết nhân quả. Dừng trước bước deploy theo đúng chỉ đạo của Product Owner (Bảo sẽ dùng Codex deploy).

---

## 1. Ranh giới bất biến nghiêm ngặt (Hard Invariants Preserved)

Tuân thủ tuyệt đối chỉ đạo của Product Owner:
1. **Local Source Tracking Invariant Gate (12/12 PASS):**
   * Giữ nguyên vẹn mã nguồn các thành phần đo lường thuộc quyền sở hữu của HTML canonical: script runtime observer micro-events `section_view` và `section_engagement_time` (`__dgwAwarenessSectionInitV1`), danh sách Section IDs, CTA IDs và tính chất inert của CTA.
   * Cổng hồi quy tự động: [`tests/landing-tracking.test.cjs`](file:///D:/Digiwin_Semiconducter_Workspace/tests/landing-tracking.test.cjs) đạt **12/12 PASS**.
   * *Ranh giới phạm vi:* Mã nguồn HTML canonical không chứa container snippet GTM (`GTM-NGT54TM9`) hay cấu hình GA4 (`G-20TL63SYLQ`); các thành phần này cùng với dispatch mạng bên ngoài (Google Ads, Meta Pixel/CAPI, LinkedIn Tag) và consent mode thuộc hạ tầng LadiPage trên production live, tiếp tục kế thừa trạng thái ghi nhận ở Phase 5 (`PASS WITH SCOPE EXCLUSION`), không thuộc phạm vi và không được kiểm chứng bởi bài test nguồn 12/12 này.
2. **Conversion & CTA Invariant:**
   * Giữ nguyên số lượng & ID CTA: OSAT (2: `osat-cta-header`, `osat-cta-terminal`), Fabless (2: `fabless-cta-header`, `fabless-cta-terminal`), Partner (1: `partner-cta-header` với nhãn `Tư Vấn`).
   * PopupX trigger bridge contract (`data-ldp-native-form-popup-trigger`) không đổi.
3. **100% Visual Fidelity Preserved — Zero UX/UI Mutation:**
   * **Partner:** Đã hoàn nguyên (revert) toàn bộ các can thiệp hình ảnh. Khôi phục nguyên vẹn `filter: blur(2.5px) brightness(0.86) contrast(1.06)` của backdrop và giữ nguyên reveal animation ban đầu `[{ opacity: .7, transform: 'translateY(12px)' }, { opacity: 1, transform: 'translateY(0)' }]`. Không làm thay đổi bất kỳ pixel hay hiệu ứng thị giác nào so với bản canonical đã duyệt.
   * **OSAT & Fabless:** Giữ nguyên giao diện Dark Glassmorphism, cấu trúc bento grid, responsive breakpoint behavior, nội dung bằng chứng (proofs/citations) và ngôn ngữ hiển thị.
4. **Deploy Boundary:**
   * Dừng tuyệt đối trước deploy; không tác động LadiPage Builder hay live server.

---

## 2. Chi tiết các cải thiện mã nguồn đã thực hiện (Exhausted Source-Level Levers)

### A. Route 1: OSAT (`landing/osat-route/osat-lot-test-traceability.html`)
1. **Khớp nối Media Query Preload và CSS:** Sửa media query của thẻ `<link rel="preload">` trong `<head>` từ `max-width: 640px` thành `max-width: 768px` (cho ảnh `=w600-rw`) và `min-width: 769px` (cho ảnh `=w1200-rw`), loại bỏ việc tải thừa 2 ảnh trên dải màn hình 641px–768px.
2. **Triệt tiêu lớp phủ Scanline CPU-heavy trên Mobile Hero:** Bổ sung `#dw-osat-landing .hero::after{display:none!important}` vào `@media(max-width:768px)` để loại bỏ việc rasterize lớp scanline lặp vô tận trên khung hình 1,300px mobile.
3. **Cô lập Layout Marquee Ticker:** Thêm thuộc tính `contain: paint` vào `.hero-marquee-section` để GPU cô lập animation trượt marquee, không kích hoạt relayout lên hero container và thẻ bento.
4. **Triệt tiêu Forced Reflow:** Thay thế `panel.offsetHeight` bằng `requestAnimationFrame` và hoãn `updateScroll` / `sendHeight` khi khởi tạo trang.

### B. Route 2: Fabless (`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`)
1. **Khớp nối Media Query Preload:** Khớp chính xác media query của preload hero image trong `<head>` thành `max-width: 768px` và `min-width: 769px`.
2. **Triệt tiêu Scanline Overlay trên Mobile Hero:** Thêm `.hero::after{display:none!important}` vào `@media(max-width:768px)`.
3. **Cô lập Layout Marquee Ticker:** Thêm `contain: paint` vào `.hero-marquee-section`.

### C. Route 3: Supplier / Partner (`landing/partner-route/supplier-ecosystem-flat.html`)
1. **Bảo toàn 100% Visual Fidelity:** Hoàn nguyên toàn bộ backdrop filter và reveal animation ban đầu; không can thiệp visual styling hay media query ảnh nền.
2. **Triệt tiêu Layout Query đồng bộ:** Hoãn lệnh `updateScroll()` gọi lúc DOMContentLoaded sang `requestAnimationFrame(updateScroll)` để loại trừ việc đọc `getBoundingClientRect().top` của toàn bộ thanh điều hướng khi vừa nạp trang.

---

## 3. Ma trận kiểm thử hiệu năng & hồi quy độc lập (Lighthouse 13.5.0)

Raw reports được lưu trữ đầy đủ tại: [`operations/evidence/performance/raw-reports/`](file:///D:/Digiwin_Semiconducter_Workspace/operations/evidence/performance/raw-reports/) (`osat-mobile.json`, `osat-desktop.json`, `fabless-mobile.json`, `fabless-desktop.json`, `partner-mobile.json`, `partner-desktop.json`, `summary.json`).

| Route | Chế Độ | Điểm Hiệu Năng | FCP | LCP | TBT | CLS | Speed Index | Raw File | Kết Luận |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: | :--- | :---: |
| **OSAT** | **MOBILE** | **88** | 2.2s | 3.6s | **0 ms** | **0.000** | 2.2s | `osat-mobile.json` | **LOCAL PASS (>80)** |
| **OSAT** | **DESKTOP** | **96** | 0.5s | 1.4s | **0 ms** | **0.000** | 0.6s | `osat-desktop.json` | **LOCAL PASS** |
| **Fabless** | **MOBILE** | **91** | 1.9s | 3.3s | **0 ms** | **0.000** | 1.9s | `fabless-mobile.json` | **LOCAL PASS (>80)** |
| **Fabless** | **DESKTOP** | **96** | 0.5s | 1.4s | **0 ms** | **0.000** | 0.6s | `fabless-desktop.json` | **LOCAL PASS** |
| **Partner** | **MOBILE** | **94** | 2.1s | 2.8s | **60 ms** | **0.000** | 2.1s | `partner-mobile.json` | **LOCAL PASS (>80)** |
| **Partner** | **DESKTOP** | **100** | 0.6s | 0.7s | **0 ms** | **0.000** | 0.6s | `partner-desktop.json` | **LOCAL PASS** |

* Cổng hồi quy tracking [`tests/landing-tracking.test.cjs`](file:///D:/Digiwin_Semiconducter_Workspace/tests/landing-tracking.test.cjs): **12/12 PASS**.
* Điểm Mobile trung bình: **91.0/100**; Desktop trung bình: **97.3/100**. TBT tối đa: **60 ms**. CLS: **0.000**.
* *Lưu ý về môi trường live:* Điểm số trên là kết quả chạy cục bộ tại `127.0.0.1` với mô hình giả lập (simulated throttling). Môi trường cục bộ không tải các script và tài nguyên live bên thứ ba; do đó, sự chênh lệch với điểm live Mobile trước đó (49–56) là khác biệt môi trường cần điều tra thêm trên production chứ chưa có đủ chứng cứ kết luận nhân quả. Receipts deploy hiện tại vẫn giữ trạng thái `P4_OPTIMIZATION_PUBLISHED_LIVE_PERFORMANCE_FAIL` cho tới khi có kết quả deploy và đo đạc mới từ Codex.

---

## 4. Danh tính Candidate & Mã Checksum SHA-256 Sẵn Sàng Bàn Giao Cho Codex Deploy

Toàn bộ thay đổi nằm trong commit checkpoint `P4-mobile-gemini-c1` trên branch [`slice/landing-pagespeed-optimization`](file:///D:/Digiwin_Semiconducter_Workspace):

| Route | Canonical Path | SHA-256 Checksum |
| :--- | :--- | :--- |
| **OSAT** | [`landing/osat-route/osat-lot-test-traceability.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/osat-route/osat-lot-test-traceability.html) | `C3DE1AD2D879D8C1CD2DB2774858DC6517D80C009BC57BC46F3D89F9FDD28DCB` |
| **Fabless** | [`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/fabless-route/fabless-outsourced-popupx-basic-flat.html) | `F44F4EFCC661253979412A738BEA7EA17D55FFAB24331CAAE9547E61712779E5` |
| **Partner** | [`landing/partner-route/supplier-ecosystem-flat.html`](file:///D:/Digiwin_Semiconducter_Workspace/landing/partner-route/supplier-ecosystem-flat.html) | `214B472FE412D3C853474D0C817DC3AD2ED654FCD53A0F3B376903A87CEBB59D` |
