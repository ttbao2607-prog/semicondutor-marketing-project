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

Với route đã được Bảo phê duyệt và có source docs, executor được phép import/tạo một draft HTML-to-LadiPage đặt tên rõ ràng, preview và ghi evidence đã sanitize mà không cần xin lại. Phạm vi chỉ là draft/preview; không public publish, domain, form/lead receiver, tracking/tag/container, campaign, credential hoặc PII.

HTML landing do agentic workflows sản xuất. Không giả định Ladipage import/publish được HTML tùy ý; phải chứng minh route thực trước. Reuse event/tag sau inventory, tránh duplicate; UTM/source phải kiểm tra xuyên route; không đưa PII vào URL, analytics parameter hoặc evidence; dùng dữ liệu giả có đánh dấu khi test.

Ba route semiconductor phải theo design system canonical tại `design-system/digiwin-semiconductor-marketing/MASTER.md` và page override tương ứng. Chỉ import LadiPage sau khi redesign hiện tại qua audit và được ghi là candidate mới. HTML sở hữu giao diện và nút CTA, không chứa form nhìn thấy/ẩn. CTA chỉ gọi `document.getElementById('OpenformWF2').click()` khi trigger tồn tại; click không phải submit/lead. OSAT giữ candidate `osat_cta_click` với `cta_location`; Fabless/Partner không phát CTA analytics event cho đến khi inventory cho phép reuse event có sẵn. LadiPage sở hữu popup/form bên ngoài HTML, field và nơi lưu dữ liệu; tên/nguồn event submit thành công chưa được xác minh và phải được inventory live xác nhận. Route HTML không phát `accepted_form` (tên chưa được source set xác minh); không tự tổng hợp hoặc đổi tên event success. Không tự tạo API/form; checklist binding/regression nằm trong `tracking/Semiconductor_Tracking_Contract.md` và `operations/LadiPage_Draft_Runbook.md`.

Các slice song song phải ghi owner, input/revision, dependency, output, acceptance, quyền đọc/ghi và stop condition. Một browser session chỉ có một controller; shared resource chỉ có một writer. Không tự tạo framework, scheduler, API integration hoặc kích hoạt slice khi chưa có mandate.

Google Ads evidence rule: banner cam “Xem xét mục tiêu của chiến dịch...” là informational/non-blocking. DOM/accessibility text một mình không đủ kết luận blocker; phải kiểm tra screenshot hiển thị và actual interaction, rồi escalate Coordinator/Auditor nếu còn nghi ngờ. Trạng thái sanitized ngày 2026-09-11: Campaigns, Ad groups, Settings và Keyword Planner functional; Keyword Planner có thể trả `OBSERVED_NO_DISPLAYED_DATA_IN_CURRENT_CONFIGURATION` khi không hiển thị metrics.

## Quy tắc public Git

Chỉ đưa nội dung marketing đã được sanitize lên public repository. `main` là canonical; baseline ban đầu là ngoại lệ duy nhất được ghi trực tiếp vào `main`. Các thay đổi sau đó dùng worktree và branch sở hữu theo dạng `slice/<slice>-<short-name>`; không tạo xung đột trực tiếp trên shared file. Coordinator audit diff và merge thay đổi đã được duyệt. Không commit secret, credential, token, cookie, browser/session state, PII, raw account/lead/audience data, private URL hoặc proof chưa xác minh.

## Quyền quyết định và kết thúc

Executor tự xử lý L0 trong phạm vi đã giao. Khi có trade-off material hoặc thiếu quyết định về budget envelope, đổi nền tảng, publication/permission hay business scope, dừng và gửi decision pack cho Bảo (L2); không đưa superior vào approval chain mặc định. Báo cáo phải tách fact, observed evidence, proposal và unknown; terminal token phải phản ánh đúng trạng thái.
