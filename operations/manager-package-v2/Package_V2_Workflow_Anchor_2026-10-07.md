> **Bảo clarification07/10 — revision1.1:** Package ghi11,7triệu media chưa thuế; Bảo theo dõi/coordinate tiền dashboard, kế toán/pipeline công ty xử lý thuế. Tuần1 chạy đúng plan, review cuối tuần; tuần2 theo data matrix, ghép/swap đúng đoạn bằng VNweek1/week2, assetFDI và audience chính/backup. [Decision record](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md). Workflow3phase và quyền Bảo giữ nguyên; không mở thêm câu hỏi thuế/kỹ thuật cho sếp.

# Package v2 · anchor workflow và cách viết

Anchor ID: PACKAGE-V2-WORKFLOW · revision1.1 · 07/10/2026. Nguồn: chỉ đạo trực tiếp của Bảo trong phiên. Đây là quyết định về workflow/nội dung package, được ghi nhận **trước khi lập plan**.

## Vấn đề v1 cần xử lý

1. Claim của agent về thao tác local, integrity và tự kiểm chứng xuất hiện quá nhiều trong package trình người duyệt.
2. Quá nhiều câu hỏi khiến người đọc khó quyết định.
3. Câu từ thiếu tự nhiên, lặp “chưa”, “không” và các lời phòng thủ lấy từ dữ liệu vận hành repo.

## Vai trò và mục đích package

Bảo sở hữu paid ads và quyết định toàn pipeline; sếp đã trao quyền tự chủ cả dự án. Package trình sếp cần một đề xuất rõ về **budget + logic sử dụng tiền + measurement**, đủ để **đồng ý / từ chối / góp ý**. Các quyết định triển khai thuộc Bảo được thể hiện thành phương án của Bảo, thay vì hỏi lại sếp từng lựa chọn.

## Workflow đã chốt

| Bước | Đầu ra cần đạt | Cách xử lý |
|---|---|---|
| **B1 — Làm data chuẩn từ repo, rồi chốt** | Bộ dữ liệu nguồn nhất quán làm căn cứ viết package | Đối chiếu đúng quyết định hiện hành, progress, audience, artifact, budget và measurement. Tách dữ kiện, giả định và vấn đề cần giải quyết trong hồ sơ nội bộ. Chốt dữ liệu với Bảo trước khi lọc câu hỏi và viết bản trình sếp. |
| **B2 — Lọc câu hỏi cần duyệt** | Khoảng **3–4 câu**, tập trung budget và logic/measurement giúp duyệt khoản đầu tư | Gộp các quyết định liên quan thành câu hỏi thực chất, có đề xuất rõ và căn cứ ngắn. Người duyệt có thể say yes/no/góp ý. Các câu hỏi kỹ thuật, quyền thao tác của agent, integrity, trạng thái Git hoặc claim an toàn được xử lý trong hồ sơ vận hành. |
| **B3 — Polish câu từ** | Bản trình bày tự nhiên, rõ ý, có lập trường và dễ quyết định | Chuyển dữ liệu nguồn đã chốt thành ngôn ngữ business. Viết đề xuất, lý do và cách đo trước; diễn đạt rành mạch phần nào cần ý kiến người duyệt. Loại lời phòng thủ và trạng thái kỹ thuật của agent khỏi câu chuyện. |

Hoàn thành/chốt B1–B2 rồi mới đến B3. Đây là workflow Bảo yêu cầu; lịch, task breakdown, người thực thi và execution plan sẽ được lập ở bước riêng sau chỉ đạo tiếp theo.

## Ranh giới giữa dữ liệu nội bộ và package trình sếp

- **Hồ sơ nội bộ:** SHA/hash, byte equality, local commit/main/push, self-review/independence, pre/post gates, tình trạng browser, provenance chi tiết và các lỗi cần xử lý. Những nội dung này phục vụ operator, không mặc định trở thành lời cam kết/câu hỏi trong package.
- **Package trình sếp:** đề xuất đầu tư, cách hoạt động của pipeline, vì sao mức chi hợp lý, hiệu quả đo bằng gì và điều kiện ra quyết định tiếp theo trong phạm vi Bảo đề xuất.
- **Bất định có ảnh hưởng thực chất đến budget/logic/measurement:** nêu ngắn, đúng mức, kèm cách xử lý hoặc hệ quả kinh doanh. Polish không biến dữ kiện còn thiếu thành đã xác minh và không loại bỏ rủi ro có thể đổi quyết định đầu tư.

## Quy tắc cho câu hỏi duyệt

- Khoảng3–4câu là mục tiêu cho package, không chuyển34mục inventory thành34câu hỏi.
- Mỗi câu hỏi phải có ảnh hưởng đến quyết định budget hoặc đánh giá khoản đầu tư, có đề xuất để người duyệt phản hồi.
- Các lựa chọn execution thuộc quyền tự chủ của Bảo được ghi là phương án vận hành; vấn đề dữ liệu/kỹ thuật cần giải quyết được giữ trong backlog nội bộ.
- Bộ22propositions/checkbox/acknowledgement của v1 là nguồn lịch sử, không được mang nguyên sang v2 hoặc dùng để giữ lại approval cũ.

## Quy tắc polish

- Giọng người làm paid ads trình một phương án đầu tư: chủ động, cụ thể, tự nhiên; tránh giọng agent báo cáo quyền hạn hoặc tự chứng nhận.
- Dùng câu khẳng định có căn cứ và đề xuất có lý do. Ví dụ giọng viết: “Đề xuất mức chi X để kiểm tra Y; đánh giá bằng Z.” Đây là mẫu diễn đạt, không phải con số hoặc câu hỏi đã chốt.
- Chuyển hạn chế kỹ thuật thành tác động/bước xử lý có nghĩa với người đọc khi thật sự cần. Tránh chuỗi “chưa… / không… / chưa đủ evidence…” làm nội dung chính.
- Giữ tên case, phạm vi giải pháp, số liệu, source và ý nghĩa đo lường chính xác. Ngôn ngữ quyết đoán không đồng nghĩa hứa kết quả chưa có căn cứ.

## Áp dụng vào worktree hiện tại

[Inventory34mục](Package_V2_Content_Inventory_2026-10-07.md) là danh sách nội dung nguồn để rà B1. Anchor này chốt workflow, quyền quyết định và cách truyền đạt; cấu trúc trình bày chi tiết, câu hỏi cụ thể, budget/phân bổ mới và plan vẫn để Bảo steering.

Anchor workflow package bổ sung, không thay message anchor VN/FDI của Vy hoặc nguồn business hiện hành. Tiền/hậu kiểm và evidence vẫn thực hiện ở hồ sơ nội bộ; việc giữ chúng ngoài package trình sếp không bỏ kiểm chứng.

Docs impact reviewed: current-progress, DOCS_IMPACT_MAP và content anchor/email đã đọc. Cập nhật README/inventory trong scope package v2 để chỉ rõ anchor mới. Không thay budget, account, artifact acceptance, frozen harness/anchor hoặc main canonical trong lượt ghi nhận này.
