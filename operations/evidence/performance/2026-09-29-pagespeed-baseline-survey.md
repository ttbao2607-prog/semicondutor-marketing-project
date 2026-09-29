# Báo cáo khảo sát Baseline PageSpeed Insights (Slice P0) — 2026-09-29

**Thời điểm đo lường:** 2026-09-29T08:25:00+07:00 – 2026-09-29T08:29:00+07:00  
**Công cụ khảo sát:** Google PageSpeed Insights (`https://pagespeed.web.dev/`) — Lighthouse 13.5.0 Engine  
**Môi trường giả lập:**
- **Mobile:** Emulated Moto G Power, Lighthouse 4x CPU Throttling, Slow 4G Network
- **Desktop:** Emulated Desktop, Unthrottled/Standard Desktop Network
**Quy chế:** Read-only Survey. Không can thiệp mã nguồn live, không làm thay đổi tracking invariants.

---

## 1. Bảng điểm tổng hợp hiện trạng (Baseline Performance Matrix)

| Route Landing Page | URL cấu hình thực tế | Thiết bị | Performance Score | FCP | LCP | TBT | CLS | Speed Index | Đánh giá chung (Target >= 80) |
|---|---|---|---|---|---|---|---|---|---|
| **OSAT** | `/semiconductor-osat` | **Mobile** | **63** | 1.2 s | **18.8 s** | 480 ms | 0.000 | 2.5 s | 🔴 **FAIL** (LCP cực kỳ chậm: 18.8s) |
| | | **Desktop** | **51** | 0.4 s | 3.3 s | **620 ms** | **0.147** | 1.2 s | 🔴 **FAIL** (CLS > 0.1, TBT cao, LCP chậm) |
| **Fabless** | `/fabless` | **Mobile** | **57** | 1.3 s | **12.2 s** | **660 ms** | 0.000 | 3.2 s | 🔴 **FAIL** (LCP chậm: 12.2s, TBT 660ms) |
| | | **Desktop** | **76** | 0.5 s | 2.5 s | 250 ms | 0.000 | 1.1 s | 🟡 **TIỆM CẬN** (Cần tăng +4 điểm để đạt 80) |
| **Supplier / Partner** | `/supplierecosystem` | **Mobile** | **81** | 1.2 s | 1.9 s | **730 ms** | 0.000 | 1.8 s | 🟢 **PASS** (Đạt >= 80 nhưng TBT cao) |
| | | **Desktop** | **86** | 0.4 s | 1.1 s | 300 ms | 0.000 | 0.8 s | 🟢 **PASS** (Đạt chuẩn) |

---

## 2. Phân tích nguyên nhân gốc rễ (Root Cause Analysis)

### 2.1. Điểm nghẽn LCP (Largest Contentful Paint: 18.8s trên OSAT Mobile, 12.2s trên Fabless Mobile)
1. **LCP Request Discovery trễ do dùng CSS `background-image`:**
   * Thay vì dùng thẻ HTML `<img>` có độ ưu tiên cao, ảnh nền Hero được gọi qua thuộc tính CSS:
     ```css
     background: linear-gradient(...), url("https://lh3.googleusercontent.com/d/11hPIa9_gokq95NqWykyaDdq8Kl7RrThV") center center/cover no-repeat;
     ```
   * Trình duyệt chỉ phát hiện cần tải ảnh sau khi đã tải, parse xong HTML, biên dịch CSS và áp dụng style lên phần tử `#dw-osat-landing .hero`.
2. **Kích thước file ảnh Hero quá lớn và chưa nén hiện đại:**
   * File ảnh hero `11hPIa9_gokq95NqWykyaDdq8Kl7RrThV` có dung lượng lên đến **850,551 bytes (~850 KB)** ở định dạng JPEG gốc.
   * Trên đường truyền Mobile (Lighthouse 4G throttle), việc tải 850 KB tốn hơn 10 - 15 giây, kéo tụt điểm LCP xuống 18.8s.
   * Thiếu hoàn toàn thuộc tính `fetchpriority="high"` hoặc thẻ `<link rel="preload">`.

### 2.2. Điểm nghẽn TBT (Total Blocking Time: 480ms - 730ms) & Main-Thread Blocking
1. **SVG Filter `feTurbulence` data URI (Noise texture):**
   * Được nhúng trực tiếp dạng base64/SVG vào nhiều lớp thẻ glassmorphism kết hợp `backdrop-filter: blur(24px)`.
   * Trên thiết bị di động với GPU/CPU hạn chế, các bộ lọc này buộc trình duyệt phải rasterize lại liên tục khi cuộn trang, làm quá tải Main Thread và GPU compositing.
2. **CSS Animation chạy liên tục:**
   * Các keyframe animation như `@keyframes vaultLumenSpin` với CSS custom property `@property --vault-angle`, và `marquee-scroll` chạy vô hạn gây tiêu tốn CPU cycles.
3. **Thực thi đồng thời Third-party Scripts:**
   * GTM, GA4, và PopupX SDK nạp và khởi tạo trong quá trình hydration ban đầu, cạnh tranh CPU với các tác vụ hiển thị giao diện.

### 2.3. Điểm nghẽn CLS (Cumulative Layout Shift: 0.147 trên OSAT Desktop)
1. **Thiếu kích thước cố định cho hình ảnh/thành phần động:**
   * Một số thành phần hình ảnh (logo, diagram, thumbnail cards) chưa được định hình trước kích thước `aspect-ratio` hoặc `width`/`height` rõ ràng trong luồng render desktop, khiến layout bị dịch chuyển khi các tài nguyên này tải xong.

---

## 3. Hành động tối ưu cho các Slice tiếp theo

1. **Slice P1 (Tối ưu LCP & Media Packaging):**
   * Chuyển đổi toàn bộ ảnh hero và các diagram lớn sang định dạng WebP/AVIF với kích thước tối ưu hóa cho Mobile (max-width 480-750px) và Desktop (max-width 1440px).
   * Thêm thẻ `<link rel="preload" as="image" href="..." fetchpriority="high">` vào `<head>` của từng file HTML canonical.
   * Chuyển ảnh Hero sang phần tử tối ưu hoặc cung cấp responsive image sources.
2. **Slice P2 (Tối ưu TBT & CSS/GPU Compositing):**
   * Vô hiệu hóa hoặc thay thế bộ lọc inline SVG `feTurbulence` nặng nề trên mobile (`@media (max-width: 768px)`).
   * Bổ sung thuộc tính `content-visibility: auto` và `contain-intrinsic-size` cho các section below-the-fold (`#lot-map`, `#cas-ic-case`, `#resources`, v.v.) để trình duyệt không phải layout toàn bộ 4.000 dòng HTML cùng lúc.
   * Tối ưu hóa các CSS animation để giảm tải CPU khi ở background hoặc mobile.
3. **Slice P3 (Tối ưu CLS & Lazy Loading):**
   * Khai báo chính xác tỷ lệ `aspect-ratio` hoặc kích thước cho 100% hình ảnh trên trang.
   * Áp dụng `loading="lazy"` và `decoding="async"` cho toàn bộ ảnh below-the-fold.
4. **Slice P4 (Audit & Regression):**
   * Chạy regression test `tests/landing-tracking.test.cjs` bảo đảm 12/12 test PASS.
   * Kiểm tra lại điểm số PageSpeed để xác nhận tất cả 3 trang đều đạt **>= 80** trên cả Mobile và Desktop.
