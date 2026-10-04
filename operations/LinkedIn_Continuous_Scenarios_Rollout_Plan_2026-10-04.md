# Plan rollout tuần tự toàn bộ kịch bản — 04/10/2026

Trạng thái: QUEUE_COMPLETED_WITH_FINDINGS / execution PARTIAL / audit FAIL for whole-campaign creative criteria. Eight treatments passed (F3, P3, F1, F2, O2, O4-O, O1, O3); P1, P2 and O4-Q retain findings. Actual calls: 31 base + 7 corrections = 38; reused 20 assets; selected 40 passing cards. Evidence: operations/linkedin-imagegen-dogfood/continuous-rollout-2026-10-04/operator/queue-ledger.json. Result: operations/LinkedIn_Continuous_Scenarios_Rollout_Result_2026-10-04.md. No 11-treatment PASS. Bảo yêu cầu chuẩn bị một plan chạy xuyên suốt, xác nhận harness đã freeze và bỏ các điểm dừng chờ human duyệt. Queue local đã hoàn tất với findings; xem result và ledger cuối. Khi thực thi, không xin lại human approval từng copy, card, bộ hay wave trong phạm vi này. Internal source review, release/preflight và native/creative/render audit vẫn bắt buộc; parent tự quyết định chuyển bước bằng evidence.

## Mục tiêu và phạm vi

Hoàn tất queue Cold Awareness 10 base scenario IDs / 11 role treatments, mỗi treatment một quảng cáo tiếng Việt năm thẻ và reader public-only. F3 đã có exact set freeze; 10 treatment còn lại được xử lý hoặc requalify. Không thêm A/B hoặc bản dịch. Bảo đã chấp nhận harness; kết quả mới đạt audit được ghi AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE, không cần chờ exact-set human approval và không bịa rằng Bảo đã xem từng ảnh mới. Không suy ra buyer validation hoặc live acceptance.

Baseline local: slice/linkedin-harness-redesign-plan @ 04ac95f038b95d3e4207d1beda01c21ed1b80bad; implementation @ 3587fe7. Worktree RMK có merge 7730bd9, giữ lịch sử riêng. Checkout Cold chủ động ở checkpoint harness; merge RMK mới hơn không làm checkout Cold sai hoặc cần nhập ngược RMK. Không sửa worktree RMK trong rollout này.

Chuẩn: frozen mechanism; Sol visual family; native square minimum 1080, giữ bytes gốc; R2 campaign references và official logo; closing B anchor 016b69513d28bee0ab1b371e4ff5c8f4a86acb531a40125d72785622b01a7416 chỉ chuyển hierarchy/full-width source/body-sized source/CTA separation. Copy, composition, props và dữ liệu reference không được chuyển nguyên sang cohort khác. Không sửa gate/tests/anchor để vượt một finding.

## Queue cố định

| Thứ tự | Treatment | Cách thực hiện |
|---|---|---|
| 0 | F3 — bàn giao đối tác | Kiểm tra pins của exact frozen set; reuse, không generate mặc định. |
| 1 | P3 — bằng chứng audit | Requalify A1–A4; dùng closing B PO-accepted nếu exact copy/current criteria đạt. Nếu không, tạo closing mới theo chuẩn. |
| 2 | F1 — tiến độ sản phẩm/lot | Fresh source/copy review, closing trước, rồi đủ năm thẻ. |
| 3 | F2 — forecast gặp thực tế | Requalify selected dogfood five-card set, gồm A2 correction; không dùng failed base A2. |
| 4 | P1 — người chịu trách nhiệm | Fresh source/copy review và carousel năm thẻ. |
| 5 | P2 — ranh giới trước tích hợp | Fresh source/copy review và carousel năm thẻ. |
| 6 | O2 — một lot nhiều góc nhìn | Chọn đúng treatment từ Operations source, tạo/reuse theo current criteria. |
| 7 | O4-O — đặt câu hỏi vận hành | Copy và cards dành riêng treatment; không mặc nhiên chia sẻ opening/closing với O2. |
| 8 | O1 — quyết định chất lượng | Requalify selected dogfood five-card set theo current copy và source. |
| 9 | O4-Q — đặt câu hỏi chất lượng | Chọn đúng treatment Quality; cards dành riêng treatment. |
| 10 | O3 — cost từ shopfloor | Bound finance/product claims bằng source; thiếu proof thì dùng câu hỏi quản trị có căn cứ, không bịa capability/metric. |

Source origin: exact snapshots tại 1f476c31de4f8a7cfbcf5b5b8842fd35a2e7390f và reviewed source-copy trong all-scenarios-2026-10-03/source-review; đối chiếu working files và current editorial exceptions trước mỗi treatment. Legacy prompts/layout/alt/props không tự kế thừa. ERP/MES không cần parenthetical; OSAT/Fabless/WIP có giải thích first-mention phù hợp source cho mỗi ad độc lập. Native headline/caption/alt ở ngoài raster; artwork chỉ in exact approved artwork fields và official mark.

## Chu trình chạy tự chủ

1. Preflight toàn queue: Git recovery, verify frozen bytes/reference/gate/tests, 65 regression/closing checks, inventory nguồn và reuse candidates. Ghi pin baseline và protected prior assets. Tạo namespace operations/linkedin-imagegen-dogfood/continuous-rollout-2026-10-04/{treatment}/{common,operator,worker,public}; một writer mỗi namespace, không overwrite historical runs.
2. Một treatment tại một thời điểm. Parent review exact source/copy và rights/claim scope, tự hoàn thiện draft trong scope; pin revision, contract/review/release/spec trước dispatch. Không chờ human ký copy hoặc release. Review độc lập với worker draft; không dùng worker tự khai làm bằng chứng. Nếu dùng child: một native leaf gpt-6.1-sol/low, effective runtime admission/acceptance phải được kiểm tra; không silent fallback. Plan không tự spawn trong lượt chuẩn bị.
3. Reuse là bước ưu tiên: requalify exact current copy, logo, reference style, pending-state, source readability và public projection. Candidate chưa đạt bị loại; failed historical bytes giữ nguyên. Ưu tiên selected F3/F2/O1 và P3 anchor đúng điều kiện, không regenerate chỉ để tạo mới.
4. Khi cần ảnh mới: closing trước bằng contract riêng mang full-five copy và release card cuối ONLY; campaign contract cho A1–A4 không mang closing reference. Parent gọi ImageGen qua fresh preflight/dispatch binding, giữ receipt và original native bytes. Audit closing trước khi chi thêm bốn base cards. Source xuất hiện một lần, full-width, cỡ bằng hoặc lớn hơn body, đọc không zoom ở image khoảng 317–333px; giảm diện tích ảnh trước khi giảm chữ.
5. Audit agent toàn bộ native text/punctuation/source/labels/logo/CTA, nền không microglyph/record IDs/metrics/ticks/seals bịa; semiconductor scene và integrated diagrams đúng card meaning. Native container/dimension/hash PASS không thay visual/semantic audit. Render reader đủ năm vị trí ở desktop1280x900/mobile390x844, kiểm tra story bốn transitions, cross-family coherence, overflow và navigation. Caption/alt/public reader không rò internal notes.
6. Finding trong scope: một targeted correction/treatment, fresh release và check lại toàn bộ ảnh/copy/render bị ảnh hưởng. Không hỏi human cho correction trong envelope. Nếu closing vẫn fail sau correction, hold treatment đó trước A1–A4; nếu một card khác vẫn fail, ghi CHANGES_REQUIRED. Tiếp tục treatment kế tiếp, không đóng cả queue vì một creative failure.
7. Per-treatment receipt: attempted/base/correction/reused/selected counts, copy and asset hashes, source/review/release/native/render evidence, PASS hoặc lỗi còn mở. Update queue ledger sau mỗi treatment. Không tự commit từng wave: user authorization commit checkpoint trước đây không phải blanket authorization cho commit tương lai. Dùng durable files trong named existing branch; checkpoint tiếp theo chỉ khi được cấp quyền commit.
8. Sau queue: tổng hợp tất cả 11 treatments, selected readers, unresolved findings và actual calls. PASS bộ chỉ khi mọi tiêu chí có evidence; hoàn tất campaign chỉ khi 11/11 treatment đạt, execution PARTIAL nếu còn treatment chưa đạt. Không dừng xin human duyệt giữa waves, không gắn WAITING_FOR_PO_REVIEW cho phạm vi đã được miễn.

## Envelope và điều kiện dừng

Trần tối đa 46 base calls cho 10 treatment còn lại (P3 closing1 +9x5), cộng tối đa10 targeted corrections (một/treatment); reuse giảm actual calls, trần không phải mục tiêu tiêu thụ. Nếu F2/O1 selected dogfood được reuse, base ceiling thực tế giảm xuống36 trước reuse P3 và các bộ khác. Các budget cũ đã consumed là historical; fresh run có ledger riêng, không giả vờ refund/rewrite previous calls. F3 không nằm generation budget mặc định.

Creative/source gap của một treatment: hold riêng, tiếp tục queue và báo cuối. Có thể hoàn thiện source-bound management wording trong scope khi proof thiếu; không tự nâng claim. Hỏng shared gate/pins, runtime không được xác minh, tool/access unavailable hoặc nguy cơ overwrite protected state: dừng phần phụ thuộc, làm phần độc lập còn có thể làm và báo điều kiện cụ thể. Không retry vô hạn, không nới audit để đạt PASS. Material scope change vượt plan hoặc exhausted envelope không tự giải quyết bằng additional unbounded calls.

Phạm vi local creative only. Không account/campaign/spend/publish/landing/tracking/audience upload, push/merge/Git history rewrite hoặc chỉnh global model/config. Cold và RMK chạy ở worktree/output riêng; harness baseline shared chỉ có một owner nâng cấp, thay đổi harness cần mandate riêng.

## Verification của plan và kết quả

Plan acceptance: đủ11 role treatments, không human approval checkpoint, queue tuần tự, bounded correction, source/native/render/story review và ledger cuối; freeze/failed history được bảo toàn; docs canonical phản ánh đúng mandate mới. Audit target là queue completeness, current mandate consistency và protected byte equality, không creative quality chưa được thực thi. Plan preparation SUCCESS là lịch sử chuẩn bị; current execution PARTIAL / QUEUE_COMPLETED_WITH_FINDINGS theo queue ledger. Actual creative/render findings và calls được ghi trong ledger; không có whole-campaign PASS.

Docs impact: cập nhật dated override trong CURRENT_STATE, README, Build Pack, readiness, Demo/Human Audit Runbook, Execution Plan, Remaining Scenarios, Harness Redesign Plan và prior All-Scenarios Plan; thêm current continuous_rollout trong status JSON. Historical PO-per-set approval, stopped/consumed và failed audit statements giữ nguyên theo ngày, bị mandate này supersede cho forward continuous workflow. Kết quả F3/F2/O1 và parent audit cũ không sửa.
