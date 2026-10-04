# Kết quả checkpoint carousel và HTML expand · 2026-10-04

Đã lưu toàn bộ checkpoint ban đầu trên ba nhánh local, rồi hoàn thành ba bộ carousel còn lại và freeze harness HTML revision2 trong phạm vi đã kiểm chứng.

## Carousel

Bright/case04, Pressway, Phẩm Thuyên: mỗi bộ đủ bốn card, kiểm tra native text/source/story và reader mobile/desktop. Chỉ dựng lại Bright1, Press3, Pin4: bỏ nhãn ERP thừa, bỏ Việt/Trung ngoài copy, folio trống hoàn toàn. Chín ảnh gốc dùng lại giữ nguyên byte. Ba lần ImageGen builtin thực tế; không dùng reserve. Sửa reader nav tràn320px ở phiên bản riêng; nút44px, keyboard Enter/arrow/Home/End đã kiểm tra. Đây là acceptance offline của parent, chưa suy ra buyer/live/PO creative acceptance.

## HTML và freeze

Hai bản v2: case06 48,533 byte; Pressway 41,619 byte. Nội dung bốn locale đã duyệt giữ nguyên, không diagram hay prose QA nội bộ. Source select/header giữ focus; section/hash/back/forward có target focus. Test mô phỏng v1 đã bỏ sót BODY reset; parent phát hiện trong Chrome và child sửa revision2, giữ nguyên bằng chứng lỗi. Actual whole-document/source projection và owner manifest hash reject prose/claim/code/source/locale sai; schema17 negatives và route negatives pass. Parent thêm sáu corruption/owner-pin probes.

Render kiểm tra CSS320/390/414, desktop thực tế1422px (emulation yêu cầu1280, browser scaling hiện hữu); bốn locale, source links mở đúng trang gốc, malformedtuple reject, reduced motion auto/0s. Freeze exact engine/app/template/router/tests/build/check cùng hai owner releases. Hỗ trợ duration comparison theo ngày hoặc qualitative null; dữ liệu case mới vẫn cần source/promise/locale adoption độc lập. Không phải cơ chế tự chứng nhận claim.

## Chuẩn bị rollout

Queue deduplicate chín Cold rows thành bốn case. Case06 và Pressway có HTML v2; case04 và Phẩm Thuyên chưa có expanded HTML bốn locale. O3 chưa được adopt binding R4; O2/O4-O giữ proof hold. Card cuối giữ đúng entry/case/contract/promise; /rmk-case còn là route logical, chưa có host/LadiPage hoặc kiểm chứng cặp ad→adapter. Chưa chạy HTML hàng loạt.

Cold11/55 và R4 đã freeze giữ nguyên. Shared contract11files và117frozen inputs mỗi checkout không đổi; sáu Markdown CRLF raw mismatch lịch sử vẫn ghi FAIL, tracked blobs/ngữ nghĩa unchanged. Mọi bản lỗi và release bị gate từ chối được giữ.

## Git

Checkpoint toàn bộ trước sửa: parent fd89d7f, carousel ba61f9f, HTML0999798. Commit cuối ghi trong postcommit receipt. Tất cả chỉ trên máy này; không push/merge, chưa xác minh remote live. Parent audit độc lập nguồn/cơ chế/native/render; hai writer runtime Sol6.1/low đã xác minh. Không spawn auditor thứ ba trong giới hạn hai leaf của phiên này.
