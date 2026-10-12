# Discovery matched199 — kết quả quan sát và audit 11/10/2026

Đã mở đủ **199/199 numeric Page** và thực hiện nghiên cứu cho **199/199 đầu vào**. Coordinator ghép từng dòng, kiểm bằng chứng và phân loại: **30 đúng có bằng chứng /36 sai /133 chưa đủ bằng chứng để chốt danh tính hoặc phạm vi đơn vị**. Không còn dòng chưa bắt đầu trong tập199. Discovery giữ **CHANGES_REQUIRED**; đóng danh tính toàn bộ là **PARTIAL**, audit toàn mục tiêu **BLOCKED** bởi bằng chứng còn thiếu và chưa đọc lại được roster hiện hành.

Kết luận từng cặp gắn với **ma trận matched chụp ngày10/10**, đối chiếu About thực tế ngày11/10. Lần đọc lại bảng matched cuối phiên bị timeout hai lần khi bind tab đúng tài khoản/audience; chưa lấy được bảng để so sánh. Count199 đọc được đầu phiên không chứng minh roster không đổi. Không gắn nhãn kết quả này là hậu kiểm đầy đủ roster hiện hành.

## Phạm vi và tiến độ thực

| Việc | Kết quả quan sát/audit |
|---|---|
| Page đầu ra |199 body About đầy đủ,199 screenshot có đường dẫn tồn tại; numeric input join đủ/duy nhất |
| Công ty đầu vào |199 dòng đã có nghiên cứu/attempt hoặc review nguồn cũ được gắn đúng dòng; root bổ sung nghiên cứu khi provenance của một số attempt cần đối chiếu |
| Chốt đúng |30 cặp; danh tính công ty/đơn vị hoạt động trong phạm vi nêu ở ledger |
| Chốt sai |36 cặp, gồm2 negative controls cũ và34 cặp mới |
| Chưa chốt |133 cặp:112 thiếu/không rõ danh tính đầu vào;15 thiếu cầu nối phạm vi tập đoàn/đơn vị/nhà máy;6 thiếu corroboration của numeric Page |
| Chưa bắt đầu |0 trong tập199; không suy ra đã kiểm hết409 đầu vào hoặc unmatched93 |
| Độ mới roster |Chưa xác nhận exact roster hiện hành; hai bind timeout được lưu riêng |

“Chưa đủ bằng chứng” hiện tại là **đã quan sát/nghiên cứu nhưng chưa đủ căn cứ kết luận**. Trước vòng này,180 là phần chưa hoàn tất xác minh thực; nhãn cũ không thể được hiểu rằng180 công ty đã được nghiên cứu đầy đủ rồi nhưng không quan sát được. Page có thể đọc được trong tất cả199 trường hợp sau các correction; khoảng trống còn ở nguồn công ty, alias/pháp nhân, địa chỉ hoặc phạm vi đơn vị.

## Cách kết luận và giới hạn

Đúng cần nguồn công ty/cơ quan/issuer được đọc thực, hoặc nguồn cũ đủ chi tiết được review và gắn đúng đầu vào, cùng discriminator như domain công ty, tên pháp nhân địa phương và địa chỉ, hoặc alias được chứng minh. Tên gần giống, snippet tìm kiếm và cùng tập đoàn không đủ. Sai cần chứng cứ hai phía về tổ chức/đơn vị không tương thích. Trường hợp đầu vào chưa phân biệt được công ty thì vẫn ghi khoảng trống, dù Page đầu ra trông không phù hợp.

Một cặp cùng tập đoàn có thể sai pháp nhân tại Việt Nam: nguồn phân biệt công ty sản xuất và công ty bán hàng, trong khi đầu vào/đầu ra chọn hai công ty khác nhau. Page tập đoàn/global hoặc showcase không chứng minh tập nhân viên của công ty/nhà máy tại Việt Nam.

Kết luận đúng chỉ chứng minh danh tính giới hạn. Một số Page tự tạo/chưa được công ty quản lý hoặc có trường địa chỉ, ngày thành lập khác nguồn; các caveat giữ trong ledger. Không chứng minh Page ownership, mọi attribute, employee count, toàn bộ workforce, ICP, quyền quyết định ERP, persona, locale, khả năng phân phối hay readiness. Không nhận định company-page industry là chính xác chỉ vì match identity đúng.

## Đối chiếu kết quả cũ và nguồn được bảo toàn

Trong17 cặp cũ từng ghi đúng: **12 giữ được bằng chứng**, **5 tạm rút certification độc lập** vì hồ sơ cũ chủ yếu là Page/alias hoặc thiếu nội dung nguồn gốc đủ để xác minh độc lập. Không ghi5 cặp này là sai và không suy từ website timeout rằng công ty không tồn tại. Có18 cặp đúng mới, tổng30. Hai cặp sai cũ được xác nhận bằng Page thực và nguồn công ty; không nhầm với dòng quarantine lịch sử có tên gần giống.

Giữ nguyên master424, approved409, quarantine15, R5-52, thứ tự và toàn bộ10 field đầu vào;11 dòng cải thiện identifier/12 cell không bị sửa hoặc bỏ. Eight receipts của vòng đối soát ban đầu giữ nguyên byte/hash như lịch sử. Phương án407/17 cũ chỉ là đề xuất dựa trên2 sai; **không còn đủ để xử lý36 sai**. Không tính giảm409 bằng cách trừ số Page sai: quan hệ input/output có duplicate/projection và cần join nguồn trước khi đề xuất phạm vi.

## Hai pipeline

**Week1 / Discovery:**409 là tệp đã upload theo mandate trước; Ready/>90% là trạng thái xử lý của nền tảng. Ma trận10/10 gồm199 matched/93 unmatched; count fresh Details11/10 là199 công ty và794.946 thành viên. Những con số này không phải độ chính xác identity, không phải toàn bộ409 đã được quan sát, và không chứng minh employer/persona/locale. Vòng này xử lý199 matched, chưa mở scope sang nghiên cứu toàn409/unmatched93.

**Week2 / R5 backup:**pipeline52 công ty riêng; snapshot đối soát trước trong cùng ngày đã đọc52 matched/0 unmatched, Details52 và444.625 thành viên. Vòng199 không thay cho audit identity toàn52. Unsaved reach probe cùng ngày: R5 AND Vietnam English8.200 → thêm Eng/IT/Ops/QA5.000 → thêm Manager/Director/VP/CXO460; full filters Vietnamese dưới300. Đây là forecast của configuration được quan sát, không là buyer-fit/FDI/locale PASS. Đã thoát Do not save ở vòng trước; inventory khi đó Saved5/Matched4. Vòng child này không đọc lại được inventory cuối phiên, nên không giả định fresh final readback.

## Next action đã khoanh vùng

1. Đọc lại exact roster hiện hành khi browser bind hoạt động, so sánh numeric URL + uploaded company từng dòng với pinned matrix; chỉ re-audit dòng thay đổi.
2. Với36 wrong: lập phương án exact Page thay thế hoặc ngoại lệ không có Page, đối chiếu source-row/duplicate trước khi đề xuất sửa identifier/quarantine. Ledger riêng đã ghi từng cặp, bằng chứng và required recheck; chưa có replacement CSV được chứng nhận.
3. Với133 gaps: ưu tiên legal/domain/address từ nguồn công ty/cơ quan cho112, xác định đơn vị/factory scope cho15, và bridge của6 Page. Không tự chấp nhận Page tập đoàn hoặc loại dòng.
4. Chỉ sau khi proposal đủ bằng chứng và Bảo quyết định scope/file mới xem xét upload; không tạo/upload/save/apply audience hoặc chạy ads trong vòng này. R5 giữ lane backup riêng.

## Orchestration, audit và lưu trữ

Hai native first-generation leaves theo yêu cầu Bảo dùng **gpt-6-luna / high / fork_turns:none**, được kiểm admission và paired acceptance từ primary runtime records; không fallback hay Work Local handoff. A sở hữu browser/read-only Page capture; B sở hữu official-source research; root là Coordinator/final Auditor. **AUDIT_MODE=SELF**: hai child slots dành cho hai luồng thu bằng chứng, không có child reviewer thứ ba; root review không được gọi là independent-agent/PO acceptance.

Các lỗi checkpoint (About bị cắt, parser địa chỉ/industry, snippet bị nâng thành proof, redirect trường học/showcase, provenance nguồn) đã đối chiếu/correct trên cùng worker và giữ capture cũ. Runtime gate PASS chỉ xác nhận model/effort, không là identity/audience PASS. Một số child attempt text mô tả ý định hơn là nguyên văn query; root dùng actual tool calls/returns và bổ sung bounded primary discovery cho các finding thiếu binding, không dùng narrative làm proof.

Raw input, tên công ty, account/numeric URLs, screenshot và runtime/source tool returns giữ ở kho private ngoài public repository. Public package chỉ gồm aggregate, scope, sanitized receipts và hash pins. [Summary](SUMMARY.json), [audit](SELF_REVIEW.json), [evidence bindings](EVIDENCE_RECEIPT.json), [docs review](DOCS_REVIEW.json), [anchor review](MESSAGE_ANCHOR_REVIEW.md), [Git state](GIT_STATE.md). Source contract và child plans là các file cùng thư mục.

Work giữ trên `slice/linkedin-audience-reconcile-2026-10-11` tại baseline `f266e11d68d9818232674f4473dc23d687efeca9`. Báo cáo và canonical notices là working files chỉ trên máy, chưa staged/commit/push/merge. Actual remote main đã kiểm cùng SHA. Không đổi source CSV/audience/campaign/budget/creative/landing/tracking hoặc frozen core/adapter.
