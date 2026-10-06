# Candidate2 giản thể — corrective v2

Đã tạo lại duy nhất card9: nguồn tên doanh nghiệp và Trung Quốc lớn hơn body, đặt trực tiếp trong khối nội dung. Giữ 9 ảnh còn lại nguyên byte; card10 không cần sửa. Tổng lượt mới: 1 ImageGen, pregen wrapper và native check PASS.

Reader đổi câu phủ định kiểu hậu kiểm thành quy thuộc tích cực cho doanh nghiệp Trung Quốc, giải pháp tích hợp ERP + iMES và kết quả công bố 15→5 ngày. Không thêm claim/ROI mới. Script review ban đầu đã bỏ sót câu reader này; phát hiện khi đọc DOM thực sau dispatch, sửa có receipt mới, không rewrite lịch sử.

Root SELF_REVIEW: native và desktop/feed đủ10card, đọc nguồn card9 rõ; 9 transition giữ đúng FDI operations → Finance → China integrated case. Không còn finding cần mutate ảnh. Paper bands/lines là formatting không có dữ liệu/charts, ghi nonblocking fidelity limitation; không tuyên bố prompt fidelity tuyệt đối.

**PARTIAL / INSUFFICIENT_EVIDENCE:** mobile chỉ card1 đủ trang; card2 thấy artwork nhưng frame không ổn định; cards3–10 chưa đủ actual review. Reader text/URLs qua DOM; visual desktop/mobile chưa đủ. Browser screenshot timeout nhiều lần và compositor clipping sau viewport override, vẫn lỗi sau reset/tab mới. Không gọi toàn journey PASS, không gent thêm để xử lý lỗi browser. Bước còn lại: chạy actual mobile2–10 và reader desktop/mobile trong phiên preview ổn định.

Harness/anchor/freeze/code và historical artifacts giữ nguyên; adapter DEVELOPING. Bản v2 mới chưa PO accepted, chưa commit/merge/push; main không thay đổi bởi task này. Thư mục thường, không ZIP.

Evidence: `dispatch-check.json`, `native-check.json`, `browser-review.json`, `postgen-anchor-editorial-review.json`, `protected-inputs-check.json`, `final-file-check.json`. Không có saved screenshot file được bịa; screenshot thực nằm trong tool responses.
