> **Phase 3 current 07/10:** Bảo yêu cầu chuyển sang Phase3 từ bản split Phase2 và gửi Vy, xưng tên Bảo–Vy. [Package thư mục thường](../../deliverables/manager-package-v2/2026-10-07/BAT_DAU.html) đã dựng; **PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING**. Proposal/mail,3điểm đầu tư, demo/library/readers/workbook và actual source/render/formula reviews ghi tại [Phase3](phase3/README.md). Phase1 checkpoint4030d40; Phase2/3 được checkpoint local theo mandate “commit local codex”; xem [phạm vi checkpoint](Checkpoint_Phase2_Phase3_2026-10-07.md). Main/push/live, email transmission và acceptance cuối giữ mandate riêng.

# Package v2 · plan3phase

Trạng thái hiện tại: **PHASE3_PREPARED / BAO_FINAL_REVIEW_PENDING**. Plan checkpoint7796bc6 và Phase1 checkpoint4030d40 giữ nguyên. Bảo cho phép dùng bản split/3câu Phase2 để làm Phase3; recipient là Vy, xưng tên. Không có response thay Vy/lãnh đạo. Khi plan được lập ban đầu, ba phase chưa thực thi. Workflow/inventory vẫn là source contract, không số câu hỏi.

Mục tiêu: package trình sếp có đề xuất budget rõ, logic dùng tiền và measurement hợp lý để đồng ý/từ chối/góp ý; dữ liệu nguồn đủ integrity, phần quyết định của Bảo và evidence vận hành được giữ ở hồ sơ nội bộ. Bảo có autonomy paid ads và toàn pipeline. Mandate hiện tại kích hoạt Phase3 offline package construction, không thay quyết định budget hiện hành.

## Phạm vi và nơi lưu

- Worktree/branch: `D:/LinkedIn_Package_V2_2026-10-07` / `slice/linkedin-package-v2-inventory`.
- Owner điều phối và quyết định: Bảo. Agent hiện tại lập plan/kiểm trong scope được giao; không spawn hoặc điều phối agent khác từ plan này.
- Read: main canonical, source worktrees liên quan, package v1 và receipts đã sanitize. Các snapshot/progress phải có ngày và revision; worktrees đang làm có thể tiến thêm.
- Internal outputs dự kiến: `operations/manager-package-v2/phase1/`, `phase2/`, `phase3/`. Package để trình sếp dự kiến: `deliverables/manager-package-v2/`; cấu trúc trang/format chi tiết được xác định theo steering của Bảo trong khi dựng skeleton.
- Học topology/content hữu ích từ v1; không clone mặc định22questions, engine, formulas, pilot wording, filename count hoặc layout cũ. Bảo quyết định các thay đổi business; dữ kiện hiện hành không tự bị hủy vì viết v2.
- Phạm vi thực thi sau này là draft/offline. Main merge, push, live-account readback/mutation, campaign/spend và deployment giữ theo mandate riêng.

## Phase1 — Data chuẩn, full integrity, skeleton

**Kết quả cần đạt:** một bộ data có thể truy về nguồn, kèm skeleton đủ nội dung để Bảo chốt dữ liệu. Đây là bản làm việc nội bộ, còn thể hiện đầy đủ status/assumptions/constraints; chưa polish thành bản trình sếp.

**Các việc thực hiện:**

1. Recovery main và worktrees, refresh tiến độ cần dùng; rà34mục theo inventory. Đánh dấu phần sử dụng, không sử dụng hoặc cần Bảo bổ sung, có lý do và nguồn.
2. Lập source register và data register. Mỗi dữ kiện cần source path/commit hoặc working-file hash, ngày observation, scope/revision, giá trị/đơn vị, loại fact/decision/assumption/pending, và nơi dùng trong skeleton. Bản observed/account snapshot không được trình như realtime.
3. Đối chiếu quyết định hiện hành, số liệu và tính toán. Tách Discovery424 gốc với contingency backup; không mở lại cleanup đã hoàn tất. Tách selected final khỏi raw attempt, main khỏi source-only, offline approval khỏi technical/live scope. Budget/media cap, tiền giữ lại, giải ngân và thuế/phí có đơn vị/ý nghĩa riêng.
4. Pin manifest/receipt và kiểm file cần reuse. Nếu copy asset thì kiểm byte/hash và completeness của dependencies; xử lý newline khác biệt minh bạch. Case/claim/entity/locale/reader/return mapping giữ scope nguồn. Không import private account/company/lead data vào public package.
5. Dựng skeleton từ data đã đối chiếu: đề xuất investment/pipeline; audience; creative/reader; budget/logic; measurement; những quyết định cần cân nhắc. V1 là nguồn học về cách đưa report/demo/library/workbook/căn cứ vào cùng gói, không quyết định cấu trúc v2.
6. Tổng hợp contradictions và assumptions ảnh hưởng decision. Chỗ chưa có dữ kiện được ghi trong internal register và đưa Bảo chốt, không tự bịa số hay chuyển hết thành câu hỏi hỏi sếp.

**Outputs:** `source-register`, `data-register`, `asset/claim-register`, `reconciliation-notes` và skeleton nội bộ. Định dạng cụ thể dùng mức tối giản phù hợp dữ liệu; không dựng framework/scheduler.

**Điều kiện hoàn tất:** mọi số liệu/claim/decision được dùng có nguồn và scope; phép tính kiểm lại; input reuse đúng revision;34mục có disposition; material contradiction có resolution hoặc được Bảo chấp nhận như assumption rõ ràng. **Bảo chốt data và skeleton trước Phase2.** Skeleton đủ integrity không được tự gọi là package final hoặc acceptance của artifact mới.

## Phase2 — Phần Bảo và phần hỏi sếp

**Kết quả cần đạt:** bản trình sếp chỉ giữ khoảng3–4câu duyệt cần thiết, với budget + logic + measurement đủ quyết định; phần thuộc Bảo và operator nằm ở hồ sơ riêng.

**Các việc thực hiện:**

1. Rà từng đoạn, câu hỏi, control và dữ liệu trong skeleton, gán disposition vào một bảng content split:

| Nhóm | Xử lý trong bản trình sếp | Nơi giữ |
|---|---|---|
| **Sếp quyết định budget/đầu tư** | Giữ câu hỏi, đề xuất của Bảo, lý do và cách đo | Executive package |
| **Bảo quyết định execution/pipeline** | Bỏ câu hỏi xin duyệt; chỉ giữ phần giải thích cần thiết cho investment logic, viết thành phương án Bảo đề xuất | Decision/action register nội bộ; business rationale cần thiết còn ở executive package |
| **Agent/operator integrity và kỹ thuật** | Loại khỏi phần trình sếp | Source/evidence/QA records nội bộ |
| **Data thiếu hoặc mâu thuẫn** | Xử lý với Bảo trước; chỉ giữ tác động kinh doanh material và cách xử lý khi cần cho người duyệt | Internal issues register, với executive note ngắn nếu thực sự ảnh hưởng decision |

2. Gộp còn khoảng3–4câu về khoản đầu tư: mức chi/envelope; logic sử dụng hoặc giải ngân; measurement để đánh giá và ra quyết định tiếp theo. Đây là các chủ đề để viết câu hỏi từ data chốt, không phải câu hỏi hay allocation đã chọn sẵn. Mỗi câu có đề xuất, căn cứ ngắn và phản hồi đồng ý/từ chối/góp ý.
3. Bảo review content split và bộ câu hỏi. Không hỏi sếp chọn locale/asset/rule/lookback/tag/tracking setting, chấp nhận self-review/hash/Git status hoặc cấp quyền thao tác agent. Các chi tiết đó do Bảo xử lý trong quyền đã giao.
4. Tạo bản executive tách khỏi internal source. “Ẩn/xóa phần Bảo” nghĩa là loại khỏi nội dung bàn giao: không chỉ CSS-hide hoặc giấu tab nhưng vẫn để câu hỏi/agent notes trong DOM, JavaScript/JSON payload, hidden sheets, exports hay package files. Hồ sơ gốc vẫn được giữ ngoài deliverable để bảo toàn integrity.
5. Loại approval/answers cũ nếu reuse engine hoặc form của v1. Internal34mục không được xuất thành34câu hỏi;22propositions v1 không làm acceptance contract của v2.

**Outputs:** content-split register, decision/action register của Bảo, bản executive có3–4câu hỏi và source mapping từ bản này về Phase1.

**Điều kiện hoàn tất:** mỗi câu thực sự đổi quyết định đầu tư; executive đủ budget/logic/measurement; không có execution approvals thuộc Bảo hoặc agent integrity claims lọt vào package/payload/exports; vật chứng và assumptions material vẫn được giữ đúng mức. **Bảo chốt phần tách và câu hỏi trước Phase3.**

## Phase3 — Polish và finalize

**Kết quả cần đạt:** package tự nhiên, có lập trường, dễ xem và dễ quyết định, với nội dung/số liệu giữ đúng bản đã chốt.

**Các việc thực hiện:**

1. Viết lại theo giọng Bảo trình phương án paid ads: đề xuất → lý do → cách đo → quyết định cần người duyệt. Câu ngắn, business language, tránh jargon và chuỗi “chưa/không/insufficient evidence” của agent.
2. Kiểm semantic toàn gói và từng surface: headline/report/questions/captions/CTA/demo/workbook hoặc export được chọn. Bất định material nêu ngắn, có hệ quả/cách xử lý; không polish thành kết quả đã xác minh, số ROI hoặc cam kết vượt scope.
3. Đối chiếu final text/numbers/claims với data chốt Phase1 và split chốt Phase2. Nếu polish đổi số liệu, phạm vi claim hoặc decision thì trả phần đó về bước chốt tương ứng; không hợp thức hóa bằng việc viết hay hơn.
4. Hoàn thiện các format Bảo chọn, dùng folder thường. Kiểm link/assets/locale/reader/return, budget totals và formula nếu có workbook, export parity và hành vi decision UI nếu có. Dùng skill phù hợp khi thực sự dựng/QA HTML, tài liệu hoặc spreadsheet.
5. Review bản render thực ở desktop và màn hình hẹp cho các surface được giao; kiểm cả export/share bundle, không chỉ source. Rà lần cuối để agent notes/internal claims/questions không lọt qua metadata hoặc file đi kèm. Kiểm grammar/ngữ nghĩa bằng đọc thực tế, không chỉ keyword scan chữ “chưa/không”.
6. Ghi final selection/provenance/review trong hồ sơ nội bộ, review DOCS_IMPACT_MAP và sync docs liên quan theo state thật; handoff Bảo duyệt package final. Không đưa các claim nội bộ này thành nội dung xin sếp đồng ý.

**Outputs:** executive package final trong thư mục thường, internal review/change record, selected-file manifest và hướng mở gói ngắn gọn.

**Điều kiện hoàn tất:** business narrative tự nhiên;3–4câu có thể trả lời; data/decision fidelity đúng; package thể hiện autonomy của Bảo; rendered/export checks đủ theo format thực; không internal contamination; Bảo duyệt final. Lỗi render/wording quay về corrective trong Phase3; material data/decision change quay về phần chốt tương ứng.

## Audit target và trạng thái

| Phase | Bằng chứng cần kiểm | Nội dung audit |
|---|---|---|
|1| Registers + source pins + skeleton + record Bảo chốt | Full integrity, scope/units/current decisions, contradictions và completeness |
|2| Content split + executive questions + actual deliverable/payload | Đúng quyền Bảo/sếp, khoảng3–4câu, không rò phần đã ẩn/xóa, vẫn đủ căn cứ đầu tư |
|3| Final renders/exports + data comparison + review record | Natural semantics, factual fidelity, journey/links/calculations và bundle đúng selection |

Review responsibility không đồng nghĩa có agent độc lập: khai đúng reviewer/independence thực tế; không spawn chỉ vì bảng audit. Execution và audit status ghi ở internal record, không làm claim trong executive package. Việc lập plan không chứng minh các phase đã chạy.

Docs impact tại checkpoint plan và Phase1 giữ trong Git/source records. Phase2 split/3questions là historical baseline cho mandate Phase3. Phase3 package/current-state/progress/owned README đã sync ở checkout riêng; historical Phase1/2 receipts giữ nguyên. Business/anchor/cap/cadence và frozen scopes không đổi. Bảo final review còn pending; main merge/push/live/email transmission giữ mandate riêng.
