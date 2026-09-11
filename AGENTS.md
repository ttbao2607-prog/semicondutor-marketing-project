# Hướng dẫn vận hành workspace Semiconductor Paid

## Thứ tự nguồn

Ưu tiên theo thứ tự: chỉ đạo mới của Bảo > `Semiconductor_Work_Kickoff.md` v2.0 > `Semiconductor - Website & Ads.md` > tài liệu này.

## Phạm vi và vai trò

Đây là workspace marketing paid, không phải code project. Paid độc lập với backlog Website/Vikky; chỉ reuse nguồn/proof khi phù hợp và có căn cứ.

- Bảo là Product Owner, sở hữu paid ads, creative, landing, measurement, budget và quyết định vận hành.
- Coordinator/Auditor điều phối và audit, không tự làm routine mutation.
- Executor là leaf; không tạo, điều phối hoặc delegate task/executor khác.

Inventory hiện tại gồm các file marketing đã được kiểm tra trong repository; các trạng thái account/quyền, Ladipage publish route, tracking/form/CRM, quyền dùng proof và budget đều là unknown cho đến khi có evidence trực tiếp.

## Phase A và trust boundary

Được phép nghiên cứu và tạo draft nội bộ có evidence. Cho đến khi có operational mandate cụ thể, cấm browser login, credential/PII collection, live-account activity, publish/stage/enable/spend, submit form và audience upload.

Không bịa số liệu, budget, capability hoặc kết quả. Tên case và claim chỉ là lead pending verification; live asset không được chứa placeholder hoặc claim chưa đủ scope/quyền dùng.

HTML landing do agentic workflows sản xuất. Không giả định Ladipage import/publish được HTML tùy ý; phải chứng minh route thực trước. Reuse event/tag sau inventory, tránh duplicate; UTM/source phải kiểm tra xuyên route; không đưa PII vào URL, analytics parameter hoặc evidence; dùng dữ liệu giả có đánh dấu khi test.

Các slice song song phải ghi owner, input/revision, dependency, output, acceptance, quyền đọc/ghi và stop condition. Một browser session chỉ có một controller; shared resource chỉ có một writer. Không tự tạo framework, scheduler, API integration hoặc kích hoạt slice khi chưa có mandate.

## Quy tắc public Git

Chỉ đưa nội dung marketing đã được sanitize lên public repository. `main` là canonical; baseline ban đầu là ngoại lệ duy nhất được ghi trực tiếp vào `main`. Các thay đổi sau đó dùng worktree và branch sở hữu theo dạng `slice/<slice>-<short-name>`; không tạo xung đột trực tiếp trên shared file. Coordinator audit diff và merge thay đổi đã được duyệt. Không commit secret, credential, token, cookie, browser/session state, PII, raw account/lead/audience data, private URL hoặc proof chưa xác minh.

## Quyền quyết định và kết thúc

Executor tự xử lý L0 trong phạm vi đã giao. Khi có trade-off material hoặc thiếu quyết định về budget envelope, đổi nền tảng, publication/permission hay business scope, dừng và gửi decision pack cho Bảo (L2); không đưa superior vào approval chain mặc định. Báo cáo phải tách fact, observed evidence, proposal và unknown; terminal token phải phản ánh đúng trạng thái.
