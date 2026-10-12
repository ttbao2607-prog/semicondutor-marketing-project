# Execution contract — vòng sửa Discovery tiếp theo

Revision: 1.0 · 11/10/2026 · Planner: root Codex · Owner quyết định: Bảo.

**PLAN_ONLY.** Bảo yêu cầu lập và commit plan; các bước bên dưới chưa thực hiện. Commit plan không cấp quyền spawn, sửa CSV, thao tác audience hoặc chạy campaign. Chỉ resume execution khi Bảo yêu cầu thực hiện, đối chiếu mandate còn hiệu lực tại từng bước.

## Goal

Tạo một candidate Discovery có từng thay đổi/ngoại lệ truy ngược được về source row và bằng chứng đúng entity/đơn vị, để Bảo quyết định scope và exact file. Nếu sau đó được cấp quyền upload, chứng minh tệp đã lưu đúng và output matching mới đã được đối chiếu. Không dùng trạng thái Building/Ready hoặc tỷ lệ match làm tiêu chí chất lượng danh tính.

## Baseline và input

- Nhánh: `slice/linkedin-audience-reconcile-2026-10-11`; source checkpoint `7577833855abdaf45c3002d97dd5090f4c1b6671`. [Audit](../full-identity-audit/README.md), [summary](../full-identity-audit/SUMMARY.json), [khuyến nghị](../commit-checkpoint/NEXT_ACTION_VI.md).
- Ma trận 10/10 gồm 199 matched; About quan sát 11/10. Kết luận 30 đúng / 36 sai / 133 gaps: 112 input identity, 15 unit/factory scope, 6 Page corroboration. Cả 199 đã được quan sát/nghiên cứu; current roster chưa xác nhận do hai bind timeout. Discovery CHANGES_REQUIRED, identity closure PARTIAL, full audit BLOCKED.
- Raw matrix, source-row join, captures và company evidence ở kho private; chỉ aggregate/receipt/hash đã sanitize vào Git. Auditor phải kiểm actual evidence, không nhận narrative/attempt/snippet là proof.
- Master424, approved409, quarantine15 và R5-52 giữ nguyên. Pin theo [evidence receipt](../full-identity-audit/EVIDENCE_RECEIPT.json). Bảo toàn thứ tự/duplicates/10 fields, đặc biệt 11 input/12 cell identifier đã cải thiện; không trừ 36 matched pairs khỏi 409 source rows.
- Audit 199 không chứng minh toàn bộ 409/unmatched93. Proposal407/17 cũ không còn đủ và không được dùng làm candidate mặc định. 30 đúng chỉ là identity reference, chưa là ready audience.

## Scope và owners

Root giữ Coordinator/final Auditor: duy trì contract, phân công khi có execution/delegation mandate, ghép ledger và quyết định evidence disposition. Executor được giao bounded read/research hoặc candidate preparation sau mandate; leaf không delegate. Chỉ một browser controller, một writer cho shared candidate/ledger. Chưa cấp worker/task trong lượt plan này; cấu hình runtime phải được xác nhận khi thực sự admission, không kế thừa chứng nhận của audit trước.

Week1/Discovery là scope sửa chính. Week2/R5 là backup riêng: giữ snapshot52/0 và giới hạn full identity audit chưa hoàn tất. Không tự dùng R5 thay Discovery, gộp hai nguồn hay mở thêm upload.

Không đổi ngân sách, campaign, creative, landing, tracking, frozen core/adapter; không public raw audience/account/PII. Không loại dòng chỉ vì chưa đủ bằng chứng, không nhận global/group Page làm local employer khi thiếu scope proof. Entity đúng không tự chứng minh hoạt động phù hợp chuỗi cung ứng bán dẫn/điện tử, quyền mua ERP, FDI/persona/locale hoặc journey readiness.

## Plan và dependency

| Stage | Việc dự kiến / owner | Output và điều kiện chuyển bước |
|---|---|---|
| P1 — Fresh roster | Executor browser đọc đúng account/audience trong read-only mandate; root đối chiếu source input + Page từng dòng với matrix pin. | Private roster hash/time/identity, exact diff. Chỉ reuse bằng chứng cho cặp không đổi. Timeout hoặc thiếu roster → ghi gap, không giả unchanged; offline repair có thể tiếp tục nhưng current-roster audit chưa PASS. |
| P2 — Known wrong | Executor research tìm exact replacement cho 36 cặp sai; kiểm legal name/domain/address/local unit và canonical Page alias/redirect. Root join về source rows/duplicate. | Mỗi cặp có replacement đủ proof hoặc exception nêu rõ không có Page/nguồn; reason, source passage, capture/ref, input/output IDs, required action. Không tự cách ly; phương án scope do Bảo quyết định. |
| P3 — Gaps | Executor nghiên cứu 15 unit/factory + 6 Page bridge trước nếu có nguồn; 112 input-identity cần discriminator công ty/cơ quan. | Ledger cho toàn133: VERIFIED_CORRECT, VERIFIED_WRONG hoặc UNRESOLVED có evidence/reason/next dependency. Không biến hết lượt tìm kiếm thành PASS. Evidence conflicts trả root reconcile. |
| P4 — Candidate nội bộ | Một writer sau preparation mandate; root audit diff và coverage. Phụ thuộc P2/P3 disposition; P1 gap phải còn rõ nếu chưa đóng. | Candidate private duy nhất, row-level changelog, candidate hash/row count, exact retention và exception/coverage report. Giải thích toàn source được chọn, cả phần409/unmatched ngoài audit199; không mở research toàn source một cách im lặng. Source gốc giữ nguyên. |
| P5 — Decision pack | Root gửi Bảo candidate/scope/options và unresolved consequences, kèm audit verdict. | Bảo quyết định exact retained/quarantined scope và file. Acceptance của Bảo ghi riêng với evidence verdict; không hồi tố identity PASS cho unresolved. Đây là điểm quyết định sau khi proposal đã cụ thể/reviewable. |
| P6 — Upload có điều kiện | Chỉ sau exact-file/scope approval và upload mandate. Một operator cập nhật existing Discovery một lần. | Preflight đúng identity/template/file hash; filename/status thực sau save/reopen và processing checkpoint. Không retry/generate duplicate tự động. Xung đột quy tắc upload/current account phải ghi evidence trước hành động. |
| P7 — Output audit | Readback sau xử lý trong mandate; root ghép output mới với exact candidate và source. | Current roster/captures, row-level reconciliation, known-wrong regression controls, new errors/gaps và source coverage. Kết luận quality theo evidence; persona/locale/reach/journey/campaign release vẫn gate riêng. |

P1–P5 là kế hoạch chuẩn bị proposal; P6–P7 là downstream có điều kiện, không được kích hoạt chỉ vì plan đã commit. Tại lượt này P1–P7 đều **NOT_STARTED**.

## Measurement và evidence

| AC | Tiêu chí để Auditor đánh giá | Bằng chứng tối thiểu |
|---|---|---|
| AC1 Freshness | Roster được gắn đúng audience/source và exact diff với pin; chỉ gọi current closure khi đọc đủ. | Capture/time/hash + per-pair diff; aggregate count không đủ. |
| AC2 Wrong closure | Mọi cặp known-wrong có replacement đủ proof hoặc exception/scope disposition rõ; không còn known-wrong bị âm thầm retained như đúng. | Hai phía input/output, legal/domain/address/unit bridge; row join và PO scope decision khi cần. |
| AC3 Gaps honest | 133 dòng đều có reasoned disposition; chưa đủ proof vẫn unresolved và hiện rõ trong decision pack. | Actual primary-source passages/captures, attempt ledger, unit/corroboration limits; không chỉ URL/snippet. |
| AC4 Preservation | Source gốc không đổi; candidate changes đúng approved/prepared scope, source partition/dedup có giải thích, identifier cải thiện được giữ hoặc sửa có bằng chứng/mandate mới. | SHA256/source row mapping; field-level diff/order/duplicate/coverage checks. |
| AC5 Reviewable proposal | Exact candidate private + changelog + scope/options đủ để Bảo quyết định; ICP/decision unit/persona/locale tách khỏi identity. | Hash/row count/coverage/exception report + anchor receipt + audit report. |
| AC6 Conditional upload | Chỉ upload khi exact mandate đủ; một lần đúng target/file và saved filename verified. | Mandate, preflight hash/identity, toast + reload/reopen readback. Action success không thay quality PASS. |
| AC7 Output quality | Actual new roster được ghép với candidate, các negative controls không bị che và toàn bộ gaps/coverage được báo. | Current mapping + evidence reconciliation; không dùng Ready/>90% làm identity proof. |

Auditor kiểm resulting state độc lập với lời Executor: actual file/diff/source passage/capture và live readback khi có. Root SELF có thể kiểm evidence; không gọi đó là independent-agent review nếu chưa có reviewer khác. Không spawn reviewer trong plan-only. Verdict của mỗi stage: AUDIT_PASS / AUDIT_FAIL / INSUFFICIENT_EVIDENCE, kèm criterion và gap; PO decision là trường riêng.

Tại exit của execution thực, chọn đúng một status SUCCESS / PARTIAL / FAILURE / BLOCKED theo execution-contract cho scope stage đã được cấp quyền, và báo audit verdict riêng. Không đánh dấu plan chưa chạy là execution FAILURE/BLOCKED; current full-identity audit BLOCKED là baseline lịch sử, không là kết quả P1–P7 mới. SUCCESS của proposal không đồng nghĩa SUCCESS của upload/audience/release.

## Stop, adaptation và rollback

Sai target/hash, thiếu mandate, conflict evidence hoặc semantic scope chưa rõ: dừng affected action, giữ source/capture cũ, root reconcile và ghi deviation trước khi đổi plan. Không đổi tiêu chí đo thành đạt match rate hay generic Page. Browser không đọc được cho phép offline investigation trong scope, không current-certification.

Candidate là file mới private; rollback preparation bằng cách bỏ candidate, source gốc vẫn nguyên. Sau upload được cấp quyền, không tự upload source cũ để rollback: ghi trạng thái thực và đề xuất phương án để Bảo quyết định vì một upload khác là live mutation. Không delete audience/campaign hoặc làm Git history rewrite để che finding.

## Docs và handoff

Docs impact reviewed: no canonical update required. Đây là plan cụ thể hóa hướng đã commit, chưa đổi trạng thái audience, source hay operating decision. CURRENT_STATE, DOCS_IMPACT_MAP, build/readiness và S03 đã được kiểm; lịch sử và receipts giữ nguyên. Khi execution đổi state thực, cập nhật canonical docs theo impact map trước PASS/handoff.

MSG-ANCHOR-01 yêu cầu internal-document review với anchor VY-CONTENT-ANCHOR1.0 và email source hiện hành, ghi exact plan hash; không mang PASS content cũ sang new candidate/persona/locale. [Receipt của plan](MESSAGE_ANCHOR_REVIEW.md). File CSV/ledger/captures raw sẽ ở private; public handoff chỉ sanitized aggregates/limitations/hashes.

Plan delivery hoàn tất khi exact plan/receipt nằm trong local commit trên nhánh đã nêu và đối chiếu Git object khớp, working tree sạch; SHA thực gửi Bảo ở final response. Chưa push/merge hoặc thực hiện P1–P7.
