# Anchor HTML đích FDI

ID: **FDI-DESTINATION-HTML-ANCHOR** · Revision **1.0** · 2026-10-07 · PO: Bảo.

Áp dụng cho các HTML expand cuối journey của pipeline FDI. Bổ sung yêu cầu sản xuất HTML; không thay thế VY-CONTENT-ANCHOR 1.0 hoặc email gốc, không sửa frozen ImageGen harness/guard. Chỉ đạo Bảo ngày 07/10: ưu tiên ảnh thật từ Digiwin; không có ảnh thật phù hợp mới generate ảnh minh họa.

## Hình ảnh — bắt buộc trước khi làm HTML

1. Tìm ảnh thật của đúng case trên website Digiwin trước, sau đó các bài do Digiwin đăng hoặc nguồn đăng lại có attribution Digiwin. Ghi URL trang, URL ảnh, đơn vị đăng/byline, ngày, tên pháp nhân, SHA256 và kích thước ảnh. Kiểm tra hình bằng mắt; tài khoản mang tên Digiwin chưa tự chứng minh quyền sở hữu tài khoản hoặc quyền tái sử dụng ảnh.
2. Ưu tiên ảnh thật phù hợp case và nội dung: hiện trường/nhà máy/hoạt động thực tế. Không lấy ảnh của khách hàng khác làm ảnh của case hiện tại. Stock photo, phối cảnh kiến trúc, screenshot phần mềm và infographic phải phân loại riêng; không gọi chúng là ảnh chụp thật của nhà máy.
3. Nếu tìm được ảnh thật phù hợp, dùng ảnh đó trong draft và ghi nguồn/ngày/bối cảnh đúng ở caption, alt của cả bốn ngôn ngữ. Giữ nguyên nội dung ảnh; không sửa logo, banner, con người hoặc bối cảnh để tạo bằng chứng mới. Giữ tỷ lệ, tránh cắt mất thông tin nhận diện. Nguồn ảnh và nguồn claim trong case có thể khác nhau; ảnh sự kiện không chứng minh hiệu quả triển khai hay vận hành hiện tại.
4. Chỉ khi đã ghi lại kết quả tìm kiếm và không có ảnh thật phù hợp/khả dụng mới chuyển sang ImageGen minh họa. Không dùng SVG tự vẽ làm hình hero mặc định để bỏ qua bước tìm ảnh. SVG icon/mũi tên giao diện vẫn được dùng. Minh họa phải ghi rõ là minh họa, không giả ảnh khách hàng, phần mềm hoặc proof.
5. Mọi ImageGen call/retry vẫn phải qua callable PREGEN guard hiện hành và semantic message/script review đúng revision theo AGENTS.md. Quy tắc fallback này không bỏ qua guard hoặc tự cấp release. Ảnh thật trong draft nội bộ không tự xác nhận quyền dùng cho public/paid; ghi đúng phạm vi quyền đã có evidence, unknown giữ unknown.
6. Sau đổi ảnh/caption phải tạo review mới gắn hash HTML và ảnh, kiểm tra actual desktop/mobile cả bốn locale, ảnh tải thành công, tỷ lệ và nguồn/alt. Receipt của bản SVG cũ chỉ là lịch sử, không chuyển PASS sang bản ảnh thật.

## Design và locale

Giữ chuẩn VN được Bảo chọn: Leonxinx Soft Structuralism + Editorial Split, CSS/layout của VN accepted reader làm authority. Mỗi HTML có vi/en/zh-Hans/zh-Hant toggle; lúc mở dùng locale của journey qua `?lang=`, fallback của B1 là en. Toggle cập nhật nội dung/title/alt/aria và URL nhưng giữ đường quay về journey ban đầu. Tiếng Việt là bản dịch cùng persona FDI, không chuyển sang audience nội địa.

## B1 — quyết định ảnh lần này

Chọn ảnh đoàn tham quan tháng 9/2020 từ bài trên Sohu có byline **鼎捷智造___new**. Banner trong ảnh thể hiện thương hiệu Digiwin và đúng pháp nhân 江苏中科智芯集成科技有限公司. Ghi chính xác nguồn là tài khoản trên Sohu, không gọi ảnh đang nằm trên domain Digiwin hay tự xác nhận ownership/licensing. Ảnh chỉ minh họa hoạt động tham quan lịch sử. Bộ case trên Digiwin Việt Nam hiện không có ảnh riêng ở panel case06. Ảnh tòa nhà ở bài đăng lại năm2025 có dấu hiệu phối cảnh nên không chọn làm ảnh thật. Xem [research và provenance](B1-photo-research/README.md).
