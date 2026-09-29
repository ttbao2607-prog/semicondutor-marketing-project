# P4 Local PageSpeed Optimization Checkpoint — 2026-09-29

**Trạng thái:** `P4_LOCAL_OPTIMIZATION_PASS`. Toàn bộ 3 route Semiconductor đạt điểm Mobile $> 80$ trên Lighthouse 13.5.0 local static server. Dừng trước bước deploy theo chỉ đạo của Product Owner (Bảo sẽ dùng Codex deploy).

---

## 1. Quyền sở hữu & Ranh giới trách nhiệm (Ownership & Invariants)

* **Product Owner:** Bảo (sở hữu quyết định triển khai, deploy qua Codex, closeout receipt).
* **Executor:** Gemini (thực thi tối ưu hóa cục bộ tại mã nguồn HTML, triệt tiêu forced reflows, đo lường Lighthouse local, bảo toàn 100% invariants).
* **Ranh giới bất biến (Protected Invariants):**
  1. *Measurement Invariant:* GTM container `GTM-NGT54TM9`, GA4 `G-20TL63SYLQ`, micro-events `section_view` và `section_engagement_time`. Test `tests/landing-tracking.test.cjs` đạt **12/12 PASS**.
  2. *Conversion Invariant:* Giữ nguyên số lượng & ID nút CTA (OSAT: 2, Fabless: 2, Partner: 1), PopupX trigger bridge nguyên vẹn.
  3. *Visual & Content Invariant:* Không thay đổi UX/UI, không thay đổi layout/typography/glassmorphism, không có lỗi console.
  4. *Deployment Boundary:* Dừng trước deploy; không tác động LadiPage Builder.

---

## 2. Các đòn bẩy kỹ thuật đã thực hiện (Technical Levers)

1. **OSAT (`landing/osat-route/osat-lot-test-traceability.html`):**
   * Triệt tiêu forced reflow: Thay thế `panel.offsetHeight;` tại hàm cập nhật trạm (`renderStationDispatch`) và kiểm tra phân hạng (`handleBinClick`) bằng `requestAnimationFrame`. Giảm thời gian nghẽn forced reflow từ **115.5 ms** về **0 ms**.
   * Hoãn truy vấn layout lúc nạp: Chuyển `updateScroll()` và `sendHeight()` (vốn đọc `scrollHeight` và `getBoundingClientRect().height`) vào `requestAnimationFrame` thay vì chạy đồng bộ tại DOMContentLoaded.
2. **Partner (`landing/partner-route/supplier-ecosystem-flat.html`):**
   * Chuyển lệnh `sendHeight()` lúc khởi tạo sang `requestAnimationFrame(sendHeight)` để tránh kích hoạt layout query đồng bộ.
3. **Fabless (`landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`):**
   * Đã tối ưu sẵn ở P1–P3, giữ nguyên cấu trúc source sạch.

---

## 3. Ma trận kết quả đo lường cục bộ (Lighthouse 13.5.0)

Đo lường độc lập trên HTTP server nội bộ (port 8088):

| Route | Mode | Score | FCP | LCP | TBT | CLS | Speed Index |
| :--- | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **OSAT** | **MOBILE** | **87** | 2.0s | 3.6s | 140 ms | 0.000 | 2.0s |
| **OSAT** | **DESKTOP** | **95** | 0.5s | 1.5s | 0 ms | 0.000 | 0.6s |
| **Fabless** | **MOBILE** | **82** | 1.7s | 4.7s | 110 ms | 0.004 | 1.7s |
| **Fabless** | **DESKTOP** | **96** | 0.4s | 1.4s | 0 ms | 0.000 | 0.7s |
| **Partner** | **MOBILE** | **93** | 2.1s | 2.9s | 50 ms | 0.000 | 2.1s |
| **Partner** | **DESKTOP** | **96** | 0.5s | 1.4s | 0 ms | 0.000 | 0.7s |

*Tất cả 3 route trên Mobile đều đạt $> 80$ (82–93). Desktop đạt 95–96. Tracking test suite đạt 12/12 PASS.*

---

## 4. Candidate SHA-256 Hashes cho Codex Deploy

| Route | Canonical Path | SHA-256 Checksum |
| :--- | :--- | :--- |
| **OSAT** | `landing/osat-route/osat-lot-test-traceability.html` | `5FC2F85466DC29952059255FD6899A9A2FAC2F64E9A1B50E9D84C64460C82EA2` |
| **Fabless** | `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html` | `8FAD9EA264655AA3D49CDD784A827286192FD4A6F14EFF80A6FD1FE554EEE893` |
| **Partner** | `landing/partner-route/supplier-ecosystem-flat.html` | `B0A2609BEA0D06C92C240B428B1888DDF882FD6B2EC941DD1B73B237037EB5A8` |
