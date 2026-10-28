# Readback audience — 28/10/2026

**Execution PARTIAL · V4 CHANGES_REQUIRED · R5 mapping 51/52 verified, reach estimate observed · audience choice / final delivery readiness OPEN.** [Plan và acceptance](PLAN.md). Self-review, chưa có independent audit. Không upload, sửa audience, tạo campaign, thay targeting hay spend.

## V4 observed

Trong Business Manager hiện có, tài khoản Active; V4 Ready, Details hiển thị **111 matched / 12 unmatched**. Đọc 3 trang: **50 + 50 + 11 = 111** matched rows; input/LinkedIn Page được lưu private. Nguồn V4 263 dòng có SHA256 khớp plan. Chênh lệch 263 − 111 − 12 = **140 dòng chưa giải thích**; không suy nguyên nhân hoặc định danh chúng. Ready, match rate và member estimate không chứng minh identity/ICP.

Có nhiều cặp tên input và Page khác rõ về tên/ngữ cảnh. Đã tạo candidate sơ bộ private 244 dòng, loại 19 cặp khác entity mạnh: 18 input đối chiếu chính xác, một input đối chiếu duy nhất sau chuẩn hóa dấu và dấu câu; SHA256 `e258119904061daf08ff806b8fcc8d9675bcf745790586497d1e280f00823997`. Bảng thay đổi private có input và Page. Đây là **PRELIMINARY / NOT_UPLOADED**, không phải danh sách đã xác nhận sạch: cần xác minh 19 cặp và các cặp còn nghi ngờ. Chưa phân loại đủ 111 thành đúng/sai/chưa chắc theo acceptance; chưa chứng minh ≤5% chưa chắc hoặc không còn sai. Không tự upload candidate này.

## R5 observed

Ready, Details **52 matched / 0 unmatched**; đọc 50 + 2 dòng. 51/52 cặp trùng tên sau đối chiếu không phân biệt hoa thường; so tên không chứng minh identity/ICP hay quan hệ entity. Tính phù hợp nhóm tuần 1, targeting và phân phối chưa kiểm đủ; không đề xuất R5 PASS chỉ dựa trên 52/52. Cả hai bảng raw, tên và candidate ở kho private, không vào Git.

## Snapshot rà ban đầu theo yêu cầu Bảo

Trạng thái R5 dưới đây là snapshot trước retry; kết quả hiện hành ở mục sau.

Đã tạo bảng triage private cho đủ 111 dòng: 19 cặp khác entity mạnh cần xác minh, 11 cặp trùng tên sau chuẩn hóa vẫn chưa xác minh identity, 81 cặp còn lại cần đối chiếu quan hệ/entity. Đây là phân loại **bảo thủ theo tên và ngành hiển thị**, không phải kết luận 81 sai hoặc 11 đúng. Chưa đủ để tính ngưỡng 5% acceptance.

Hồ sơ R5 ở worktree contingency ghi 52 Page đã được sàng lọc với evidence nguồn chính về hoạt động Việt Nam/chuỗi điện tử-bán dẫn và binding Page, có audit phạm vi riêng; không chứng minh entity sử dụng ERP, buyer, locale hay campaign readiness. Readback 28/10 bổ sung 52/0, nhưng chưa so từng Page ID của readback với binding cũ và chưa đo lại targeting thực tế. Probe 07/10 từng hiển thị 460 với bộ lọc English/Vietnam/function/seniority cụ thể và Vietnamese <300; đó là snapshot cấu hình cũ, không phải dự báo hiện tại hay khả năng chạy tuần 1 đã chốt. Hồ sơ R5 nằm trong worktree contingency local, chưa nhập nhánh này.

## Snapshot đối chiếu R5 trước retry — 28/10

Snapshot này được cập nhật bởi mục R5 sau retry bên dưới.

CSV R5 trong worktree contingency có SHA256 `fe730e1bff87c0295d820ebbf8763f5e42e64c48d0d1dc72c07409083c4bbb34`, khớp audit 07/10. Readback 52 dòng có đủ 52 URL input duy nhất và tập URL trùng đúng tập nguồn; có 52 numeric Page ID khác nhau; 51/52 tên input và tên matched bằng nhau khi bỏ phân biệt hoa thường. Tên trùng chỉ là tín hiệu, không chứng minh binding. Hai Page INTECH trùng tên được mở riêng và xác minh numeric ID trên Page tương ứng đúng từng URL input; dòng tên khác còn cần kiểm.

Trong khi mở Page liên tiếp, LinkedIn trả **HTTP 429** trên Page tiếp theo; ngừng truy cập lặp. Chưa đối chiếu đầy đủ 52 URL nguồn sang numeric Page ID và chưa có ước lượng targeting mới. R5 vì vậy **INSUFFICIENT_EVIDENCE**, không PASS. Ước lượng 460 trước đây chỉ là snapshot 07/10 ở một bộ lọc cụ thể. Không tự nới targeting hoặc tạo/sửa audience. Raw readback và bảng đối chiếu lưu private.

## R5 sau retry Company Page và probe reach — 28/10

Bảo xác nhận Claude đã dừng thao tác phiên Chrome. HTTP 429 ở Company Page trước đó đã hết tại lần thử lại; Campaign Manager vẫn truy cập được. Browser là Chrome extension profile ASEAN, không phải headless. R5: **51/52** Page input URL khi mở có numeric Company ID khớp numeric Page được LinkedIn trả trong matched table; **1/52 (1,92%)** không hiện link employee chứa ID, giữ UNKNOWN, không coi là sai hay đúng. Hai Page tên giống nhau và trường hợp khác tên đã kiểm ID riêng. 52/52 input URLs khớp tập nguồn R5 đã audit; 52/0 matched/unmatched. Bằng chứng chi tiết ở kho private. Trong phạm vi quan sát **không phát hiện mismatch; 1 unknown ≤5%**. Đây là đánh giá mapping scoped, không chứng minh buying authority hoặc customer fit từng entity.

Trình New audience hiển thị thông báo tạo draft khi mở; chọn R5 và thử cấu hình trong editor, không Apply. Vietnam recent/permanent + English: **8.300**; thêm Job Functions Engineering OR IT OR Operations OR Quality Assurance: **5.100**; thêm AND Job Seniorities Manager OR Director OR VP OR CXO: **470**. Chuyển Vietnamese cùng các bộ lọc: **<300**. Các giá trị ổn định hiển thị 28/10 là potential reach estimate, không phải thực giao hàng hay dự báo buyer. English theo mô tả UI bao gồm các profile language ở location (trừ Sponsored Messaging). Đây là cấu hình tham chiếu từ 07/10, không tự thành targeting hoặc locale đã được Bảo chốt; chưa kiểm acceptance thực trong ad-set editor. Không bật predicted audience. Đã Cancel editor, chọn **Do not save** ở hộp thoại rời trang, quay về Saved Audiences; danh sách hiển thị 7 audience có sẵn trước và sau, không có New audience. Không lưu cấu hình, không gắn ad set, không đổi matched list, không spend.

**Đánh giá:** R5 là candidate tốt nhất cho thử nghiệm nhắm nhóm English tham chiếu; bước chọn nhóm/locale tuần 1, D6 và xác thực eligibility trong workflow được phép vẫn mở. Không khẳng định R5 phù hợp Vietnamese với bộ lọc này, hoặc đã đóng toàn bộ blocker audience. V4 giữ CHANGES_REQUIRED. Receipt mapping/forecast không là native review, content approval hay release.

## Tiếp theo

Hoàn tất phân loại 111 cặp V4 và xác minh cặp chưa rõ bằng nguồn; rà input đã đối chiếu bằng chuẩn hóa và candidate; đánh giá R5 theo nhóm tuần 1 và kiểm giao diện theo điều kiện mục tiêu cụ thể. Plan chỉ cho tối đa một vòng làm sạch, một lần upload và readback. Phải hoàn thành candidate có thể review và đối chiếu mandate cụ thể trước live write; Bảo chọn audience theo kết quả. Không coi khoảng cách 140 là phải giải quyết hết để dừng.

Docs impact reviewed: entrypoint audience hiện hành ghi readback 28/10; không nâng readiness hoặc thay các gate khác.
