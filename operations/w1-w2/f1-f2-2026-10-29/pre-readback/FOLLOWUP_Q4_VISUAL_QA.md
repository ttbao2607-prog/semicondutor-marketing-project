# Q4 — QA bổ sung carousel desktop và reader mobile

Revision 1 · 29/10/2026 · **PARTIAL**. Authority: Bảo giao Claude thực hiện [contract](CLAUDE_EXECUTION_CONTRACT.md). Review nội bộ, không phải native-ready/live-ready; không tạo ad, không generate/crop/sửa ảnh, không sửa source. Audit độc lập NOT_RUN. Quyền dùng exact paid assets đã được Bảo chấp nhận ([PO acceptance](../../../pre-ad-readiness/2026-10-29/f1-f2-cycle/PO_PAID_ASSET_ACCEPTANCE.md)); không hỏi lại.

## Phương pháp và giới hạn thật

- **Không có screenshot trình duyệt**: mọi lệnh chụp ảnh timeout 30 giây (cả trang LinkedIn, GA4 và loopback). Thay bằng: (a) đọc trực tiếp ảnh gốc 1254×1254 hạ xuống 500 px (cỡ gần feed desktop) trong contact sheet lưu ngoài repo; (b) đo DOM bằng iframe cùng origin. Đây **không** là native preview và không là chụp màn hình thiết bị.
- **Viewport:** `resize_window` không đổi `innerWidth` (vẫn 1424), nên mobile đo bằng iframe rộng 390 và 360 px, cao 844 px trên loopback; không phải thiết bị thật.
- **Không mở reader công khai.** Bridge chỉ gửi GA4 khi hostname là `solutions.digiwin.com.vn` và path `/semiconductor-case-reader`; nguồn không có tham số đánh dấu QA, và theo contract không được thêm UTM campaign mới. Cách bridge xử lý UTM (đọc từ `tracking/semiconductor-reader-bridge.js`): tại reader, `acquisitionURL()` giữ `t`, `lang`, `entry` và `utm_*` hợp lệ làm `page_location` gửi GA4, nên acquisition thuộc về URL reader; `context()` còn sao chép `utm_*` sang các tham số cấu hình `bridge_*` (utm_content → `bridge_card`). Chỉ **link đi contact-vn** mới bỏ `utm_*` và thay bằng metadata `bridge_*` (`bridge_origin`, `bridge_treatment`, `bridge_locale`…). Vì vậy mở bản public sẽ tạo session GA4 thật mà không tách được khỏi property chung (không có đánh dấu QA). Đây là mô tả cơ chế, không phải phát hiện lỗi tracking runtime. Vì vậy transition reader → contact-vn và return **không quan sát lại**, giữ FROM_EXISTING_EVIDENCE (29/10). Không có contamination do lượt này.
- Server loopback `127.0.0.1:8765` chỉ phục vụ thư mục `deliverables` của worktree, đã tắt sau khi đo.

## Nguồn và pin

| Mục | Giá trị |
|---|---|
| Reader | `deliverables/unified-case-reader/unified-case-reader.html`, SHA256 `04429f539c394f0506679725740a2a52dd81af37ff36b70d8e4dc5c1a103f1d8`, commit gần nhất chạm file `a31ea233` |
| F1 carousel | `B13-en-f1-v5/selected-copy.json` revision `b13-review-copy-v5-six-explanation`, SHA256 bắt đầu `dd81344218d7` |
| F2 carousel | `B16-en-f2-v2/selected-copy.json` revision `b16-review-copy-en-v2`, SHA256 bắt đầu `d5cc4ac186b8` |
| Cả hai JSON | 0 ký tự lỗi U+FFFD |
| Anchor | `operations/Vy_Email_Content_Anchor.md` VY-CONTENT-ANCHOR r1.0, SHA256 đọc `6621d53c845939730ebcb1f59bbf85fb8a0d9acb156e5236e7387c0e69867ac5` (khớp pin contract) |
| Email gốc | `operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md` VY-MAIL-USER-20261006, SHA256 đọc `c5a6f35533e7a8b3b439ec4d9a260611fcdd2f67ddb0f046a3e33d28c6316d2b` (khớp) |

## Carousel — kết quả

**Cấu trúc xác nhận:** mỗi bộ có cold + 6 explanation + 4 proof; cold không thuộc bốn carousel. Mọi PNG là 1254×1254, `alt` = "Illustration: <native_headline>" cho cả 22 thẻ, headline ≤ 45 ký tự (max 42), intro 181 (F1 explanation), 219 (F2 explanation), 129 (F1 proof), 171 (F2 proof) ký tự — khớp [P5](CAROUSEL_QA.md). **16 ảnh duy nhất** (explanation 11 + proof 5), không phải 20: A6 (`8D2D935B`), proof 1 (`07D462C4`), proof 3 (`76CC1590`), proof 4 (`0D045BD1`) dùng chung F1/F2; proof 2 khác layout (`34D81860` F1, `A8F0A88C` F2).

**Đối chiếu headline trong ảnh với `native_headline`** (đọc trực tiếp cả 16 ảnh duy nhất): khớp từng thẻ, thứ tự 1/6→6/6 và 1/4→4/4 đúng.

| Thẻ | Quan sát desktop (≈500 px) | Disposition |
|---|---|---|
| F1-A1 … A4, A6 | chữ rõ, không cắt, bố cục ổn | OK |
| F1-A3 | dòng cuối thân bài chạm sát hộp wafer ở góc phải | OK, lưu ý nhỏ |
| F1-A5 | khối nguồn Taiwan ("ERP and MES for management and production") + pill; icon tài liệu | OK; giữ quy cho tài liệu Taiwan |
| F2-A1 | dòng "partners." chạm vùng ảnh nền | OK, lưu ý nhỏ |
| F2-A2, A3, A4, A6 | chữ rõ | OK |
| **F2-A5** | footer dày 5 dòng, dòng sát nhau; icon đầu là chấm tròn xanh thay vì icon tài liệu như F1-A5 | giữ CQ-1; **chữ nhỏ và dày nhất bộ, vẫn đọc được ở 500 px**, cần native preview |
| Proof 1, 3, 4 | rõ; tên pháp nhân Trung ở proof 3–4 (và 2) hiển thị trong carousel EN như P5 đã ghi | OK |
| Proof 2 | F1 có ảnh tài liệu có dòng; F2 giấy trơn, thân bài 3 dòng; cùng copy | OK, khác layout |

**Gap mới:** B13 có trang `audit-640.html`, `audit-333.html`, `compact-review.html` (11 ảnh tải được); **B16 (F2) không có viewer review nào ngoài `index.html` (chỉ thẻ cold) và `case-reader.html`**. Vì vậy không có "desktop viewer F2" để QA; QA F2 dựa trên ảnh gốc ở 500 px. Native preview vẫn NOT_RUN (chưa có draft carousel; không tạo ad).

## Reader F1/F2 mobile (loopback, English)

| Treatment | Viewport (iframe) | scrollWidth vs viewport | Ảnh | h1 | CTA |
|---|---|---|---|---|---|
| F1 | 390×844 | 375 ≤ 390, không tràn | 2/2 tải | "Three questions before the next partner production update" | "Discuss partner reports and update responsibilities" |
| F1 | 360×844 | 345 ≤ 360, không tràn | 2/2 | như trên | như trên |
| F2 | 390×844 | 375 ≤ 390, không tràn | 2/2 | "Three questions before the next outsourcing plan" | "Discuss demand changes and partner information" |
| F2 | 360×844 | 345 ≤ 360, không tràn | 2/2 | như trên | như trên |

Không phần tử nào vượt mép phải. Font nhỏ nhất F1 = 12 px. Khối CTA: "The next step opens Digiwin Vietnam’s consultation request page in Vietnamese." (đọc đủ ở F2; F1 cùng khối nhưng text đọc bị cắt ở "The ne…" do giới hạn in, không xác minh riêng). CTA trỏ `https://www.digiwin.com.vn/contact-vn/`; trên loopback bridge không chạy nên href chưa được decorate bridge (đúng thiết kế). `bridge_treatment`/`return` chỉ có hiệu lực trên host public; **không quan sát lại** (xem trên).

Một lần capture F1 390 px ở P5 có cờ `hasWarning:true` chưa rõ nghĩa; lượt này **không đo cờ đó** (không có trong phép đo), nên vẫn mở — kiểm lại khi dựng native.

## Transition

| Bước | Disposition |
|---|---|
| cold → reader trực tiếp | FROM_EXISTING_EVIDENCE |
| cold → explanation | OK (review nội dung; hook nối thẳng card 1) |
| explanation → proof Bright | OK có lưu ý (nhãn "from China" rõ; proof dùng chung F1/F2) |
| proof → reader đúng treatment | reader mobile đúng treatment: h1 và CTA khác nhau F1/F2 (đo mới trên loopback); public path FROM_EXISTING_EVIDENCE |
| reader → contact-vn có notice tiếng Việt và return | notice tiếng Việt có trong khối CTA (đo mới); chuyển trang và return FROM_EXISTING_EVIDENCE, **không re-test** để tránh traffic không đánh dấu |

## Finding

| ID | Mức | Finding | Đề xuất bounded (không tự sửa) |
|---|---|---|---|
| CQ-1 | thấp | F2-A5 chữ dày, dòng sát | native preview xác nhận; nếu muốn sửa cần mandate regen một thẻ |
| CQ-6 | thông tin | B16 thiếu viewer desktop/audit như B13 | nếu cần evidence desktop F2 ngang F1, tạo viewer review riêng (docs/HTML nội bộ, không đổi PNG) |
| CQ-7 | thông tin | F2-A5 icon đầu là chấm tròn, khác F1-A5 | giữ; ghi nhận |
| CQ-8 | thông tin | không có screenshot trình duyệt trong môi trường này | lần dựng native dùng phiên chụp được ảnh |

## Fresh MSG-ANCHOR-01 receipt (artifact nội bộ, stage POSTGEN docs-only)

Branch FDI / English / Fabless; F1 Operations dùng outsourced production, F2 Planning (demand change, lot replan). A1: giữ bán dẫn chuỗi cung ứng, không mở rộng; A2: không suy qualified buyer từ English hay R5. A3: không đổi segment/locale. A4: không có ROI%/tiết kiệm; giá trị là chuẩn bị quyết định chung. A5: VN N/A. A6: Bright Power China và Taiwan source giữ đúng scope; không năng lực MES tại Việt Nam. A7: cold → explanation/proof → reader đúng treatment → contact-vn notice/return giữ, riêng phần public không re-test. Review: Claude self-review; reviewer độc lập chưa có. **MESSAGE_ANCHOR_PASS cho bản QA nội bộ này**, không phải native/live/release và không cấp PASS hồi tố cho review cũ. Không thay đổi artifact, nên không đổi manifest/pins.

Docs impact reviewed: xem [FOLLOWUP_CLOSEOUT](FOLLOWUP_CLOSEOUT.md).
