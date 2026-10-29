> **R5 draft probe completed · 28/10/2026 ~14:46 +07:** Đã lưu và mở lại đúng một draft R5 riêng, Draft/Off trong campaign VALIDATION_ONLY đang Paused; cấu hình Việt Nam/English + 4 Job Functions + Manager–CXO, Expansion/LAN off, hiển thị 470+. **Eligibility cấu hình draft VERIFIED_SCOPED**, thay NOT_VERIFIED trước đó; không chứng minh actual delivery hoặc toàn bộ audience/release PASS. Probe-only USD10/ngày, 29–30/10 (UI tối đa USD20); tab forecast nhãn 30-day hiển thị USD0–4 / reach19–76, không ngoại suy. Journey cụ thể và D6 production/native/proof/host/tracking còn mở; V4 CHANGES_REQUIRED. Không launch/spend. [Receipt và giới hạn](R5_DRAFT_ELIGIBILITY.md). Các notice cũ bên dưới là snapshot trước phép thử này; quyền tạo draft đã có và không phải launch mandate. Tài liệu mới chỉ local chưa commit/push; draft đã tồn tại trên LinkedIn.

# Plan gỡ blocker audience — 28/10/2026

Status: APPROVED_FOR_EXECUTION theo chỉ đạo Bảo trong phiên 28/10; kết quả hiện hành xem [readback](READBACK.md). Owner Bảo quyết định audience tuần 1. Input: [readback 20/10](../2026-10-20/README.md), V4 private 263 dòng SHA256 `5c0c5d9ce9580d0c60c0787403395f544a73087cf3e6bfb6a0ccee31cf65cccc`, và [anchor](../../Vy_Email_Content_Anchor.md). Bảo yêu cầu lưu plan trước khi làm.

## Quy trình và giới hạn

1. Read-only readback V4: status, matched/unmatched, toàn bộ matched Page nhìn thấy, so với nguồn private; không dùng member estimate làm chất lượng.
2. Rà 100% matched Page hiển thị: đúng entity/quan hệ có căn cứ, sai rõ, chưa chắc; kiểm phù hợp nhóm tuần 1 theo ICP và scope, không suy persona/FDI từ tên.
3. Nếu cần, làm candidate private và changelog, một vòng loại sai rõ và xử lý dòng chưa chắc theo evidence; không sửa theo phỏng đoán. Tối đa một lần cập nhật/tạo audience và một lần readback sau đó; không tạo V5 nếu V4 đã đạt. Đối chiếu exact candidate và thao tác với mandate/scope trước live write; không lặp upload.
4. Nếu V4 không đạt, kiểm R5 mapping, identity/ICP và điều kiện phân phối làm phương án dự phòng. Bảo chọn audience tuần 1; không tự nới targeting. Ghi evidence private, receipt sanitize, sync canonical.

## Tiêu chí đóng blocker audience — ngưỡng vận hành Bảo đồng ý, không phải ngưỡng LinkedIn

- Đã xem 100% matched Page được giao diện hiển thị; không còn Page sai rõ ràng trong audience đề xuất dùng.
- Chưa chắc không quá 5% số matched Page đã xem; tách rõ và không tính là đúng. Nếu vượt, xử lý hoặc trình Bảo quyết định rủi ro, không tự PASS.
- Ghi số matched, unmatched và nguồn chưa giải thích; không bắt buộc khớp 263/263, không suy dòng thiếu là đã xử lý.
- Có căn cứ phù hợp nhóm tuần 1, nêu giới hạn ICP/persona; không yêu cầu xác minh quyền mua của từng doanh nghiệp.
- Kiểm audience và điều kiện dự kiến có đủ khả năng sử dụng/phân phối bằng trạng thái, số và cảnh báo giao diện thực tế; nếu không đủ đưa lựa chọn thay thế, không tự nới targeting.
- Có receipt evidence, rủi ro và lựa chọn của Bảo (V4 hoặc R5). Đóng riêng audience; các blocker khác giữ trạng thái riêng.

## Stop conditions

Tối đa một vòng làm sạch và một lần readback sau cập nhật; nếu V4 đã đạt thì không cập nhật. Nếu vẫn 0/0, giao diện không đủ evidence, hoặc vòng này không đạt: INSUFFICIENT_EVIDENCE / CHANGES_REQUIRED; trình phương án R5 nếu đủ bằng chứng hoặc xử lý tiếp/Support. Không lặp upload hay chờ vô hạn. Không liên hệ Support khi chưa có chỉ đạo gửi thông điệp. Không campaign, spend, enable, thay đổi targeting, tải raw account/lead/PII vào Git. Audience choice của Bảo không cấp quyền launch.
