# Đánh giá demo1-dogfood — Pressway Precision

Đã bỏ toàn bộ diagram, dữ liệu và controls của diagram khỏi anchor case06. Bốn bản nội dung đã được Bảo nhận xét “ổn” giữ đúng business fields; card metric Glassmorphism Elevated giữ kết quả 15 → 5 ngày. Anchor mới là `rmk-case06-anchor-v1`: 46.159 byte, SHA256 `db68a4441f12ea4923ec82514d9bf5ba5af7252b9dd329837fd6f93fc29f625a`.

Harness nháp đã chạy đúng một dogfood trên **Pressway Precision**: `rmk-pressway-dogfood-v1`, 39.731 byte, SHA256 `c92cd2b8ab52a1594051249b7624d7e6166f89dc44eef5e6199670664a28fe19`. Parent chấp nhận checkpoint của pilot với một điểm UX còn mở. Đây là đánh giá candidate trong phạm vi lần thử đầu; chưa freeze harness tổng quát hoặc cho phép nhân rộng. Receipt sau commit là nơi xác nhận toàn bộ DF1–DF7 và hai commit thực tế.

## Dogfood cho thấy điều gì

Pressway phù hợp để thử khả năng dùng lại vì là nhà máy nhựa mới ở Việt Nam, Workflow ERP, có nguồn gốc tiếng Việt và không dùng metric định lượng. Bản mở rộng giải thích ba nhu cầu bản địa hóa/quản lý và hai chi tiết triển khai: khấu trừ vật liệu, tái chế/vật liệu thay thế; liên kết đơn hàng–lệnh sản xuất và quản lý số lô. Đây là thông tin đọc thêm sau carousel, giữ scope chuẩn bị quy trình của nhà máy mới. Nguồn hỗ trợ các chi tiết này: [case Pressway của Digiwin Việt Nam](https://www.digiwin.com.vn/casestudies/erp-pressway-precision-case-study-vn/). Không đưa các claim một tháng/100% tồn kho của bài gốc vào payload đã duyệt.

Closing headline, lời hứa và CTA tiếng Việt khớp đúng card RMK-PRESS-4. Ba bản dịch giữ nhu cầu/quy trình và tên case, không biến kế hoạch thành kết quả đã đo. Nguồn được ghi đúng là tiếng Việt trong cả bốn ngôn ngữ. Route tương thích được giới hạn đúng tuple `RMK-PRESS / pressway-vn / rmk-fulfillment-content-v2`; query contract cũ vẫn giữ nguyên, chỉ artifact đang mở được bind vào release dogfood. Không suy từ tương thích offline thành public route LadiPage hay accepted ad/adapter pair.

## Harness được thiết kế như thế nào

| Lớp | Cơ chế | Giá trị kiểm soát |
|---|---|---|
| Nội dung | Schema public riêng; source map/claim ID/QA nằm trong sidecar nội bộ | Không đưa lời tự đánh giá hoặc claim an toàn của agent vào HTML |
| Shared truth | Parent xem nguồn, copy, bản dịch và frame; adopt exact manifest riêng cho từng case | Hai worktree tiêu thụ cùng case/claim/promise; child không tự đổi shared release |
| Output gate | Dựng lại toàn HTML từ template/router/app/logo/payload đã pin rồi so document hoàn chỉnh | Chặn chữ thừa, ARIA claim, JSON nội bộ, sai link/case, metric và locale bị thay |
| Metric | `metric:null` bỏ card và section `result` | Pressway không bị ép mang kết quả 15→5 của case06 |
| Render | Parent xem mobile, desktop, bốn locale và interaction; Bảo quyết định freeze | Hash/test chỉ chứng minh đúng dữ liệu/frame đã duyệt, không chứng minh copy mới tự đúng |

## Bằng chứng và giới hạn

- Parent đối chiếu 40 inventory pins, hai release copy byte-identical với owner và manifest độc lập. Cả hai HTML qua actual gate. Mỗi output có tám mutation negatives, swapped embedded locale và unknown internal fields được test qua gate; parent thêm bốn corruption probes và sai external manifest pin. Route suite gồm một compatibility, bốn toggle và sáu malformed controls.
- Render đã xem 320/390/414 và desktop. Không có tràn ngang ở các viewport đã đo; body mobile 17px, source CTA 48px, header language targets ít nhất44px. Bốn locale DOM khớp approved payload. Link Pressway được mở và xác nhận đúng URL/title của bài gốc. Reload/back, language, case/entry/section/UTM, duplicate identity/wrong case/wrong section được quan sát. Screenshot desktop ban đầu timeout; fresh tab chụp được, không dùng ảnh thất bại làm bằng chứng.
- **UX1 còn mở:** đổi ngôn ngữ bằng select ở cuối bài thay toàn article, nên focus bàn phím rơi về BODY. Nội dung/URL/history vẫn đúng. Đây là điểm cần sửa trước khi reuse/freeze rộng hơn; turn này chỉ ghi nhận, không chạy vòng sửa tiếp. Header toggle giữ focus. Reduced-motion CSS và focus-visible style có trong frame; chưa mô phỏng OS reduced-motion hoặc chứng nhận accessibility/touch trên thiết bị thật.
- Frame metric hiện là so sánh thời gian baseline/result. Một dogfood định tính không chứng minh mọi loại metric/ngành/copy dài đều tương thích. Chưa có buyer validation hoặc general harness freeze. Bảo chưa duyệt riêng Pressway demo1.
- Protected shared v1/11 files,117 inputs mỗi checkout, Cold/R4 và v4 lịch sử giữ nguyên. Raw v1 validator vẫn FAIL ba Markdown CRLF representations ở mỗi consumer; tracked blobs và normalized text khớp. Không sửa receipt cũ hay báo raw PASS.

## Carousel remarketing và điểm dừng

Ba nhóm Bright/Pressway/Phẩm Thuyên đã có12base original PNG1254×1254,0correction. Bright1 thêm “ERP”; Press3 thêm “Việt/Trung” ngoài text được duyệt; Pin4 đưa ảnh nhà xưởng vào blank folio. Ba nhóm chưa accepted toàn bộ. Pin1 rising-bar icon chỉ là design concern đã ghi, chưa nâng thành false outcome claim. O2/O4-O giữ vì proof-fit thiếu; R4 cũ được bảo toàn. Carousel mới vẫn chưa commit; turn này báo trạng thái chỉ, không chạy C1.

LDP namespace mới/harness/pilot và parent shared releases/evaluation/status được checkpoint bằng local commits riêng. Những draft v2–v4/coordination cũ ngoài scope vẫn chưa commit. Không push/merge/LadiPage/live. Dừng sau demo1 và đánh giá này: không thêm candidate, không correction, không nhân rộng.

LDP checkpoint đã tạo: `857965dadbce20ca53cca49db7d12eb34b77ca0b` trên `slice/linkedin-rmk-mobile-adapter`;42files gồm41files của namespace mới và một narrow Git-attributes delta bảo toàn raw pins. Owner evaluation nằm trong commit tiếp theo; receipt sau commit ghi SHA thực tế.
