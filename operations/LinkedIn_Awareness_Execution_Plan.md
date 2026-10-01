# Kế hoạch thực thi research và content LinkedIn awareness

Ngày: 2026-10-01. Revision: v1.1 — carousel format và ERP semiconductor positioning selected. Product Owner: Bảo. Status: EXECUTION PLAN DRAFT — PLANNING ONLY.

**Selected artifact contract:** xem `LinkedIn_Carousel_Constraints_and_Awareness_Anchor.md` — platform constraints, narrative acceptance và formats MD/SVG/PNG/HTML/CSV. Hai carousel A/B, C tùy chọn, preview/QA từng ad. Mục tiêu chính: định vị Digiwin là ERP có chuyên môn và kinh nghiệm ngành semiconductor; claim cụ thể phải có evidence. Landing đúng route là đường đọc thêm, native awareness không phụ thuộc click.

## 1. Mandate và kết quả cần đạt

Bảo đã chốt định hướng tại `LinkedIn_Awareness_Adcopy_Optimization_Plan.md` v1.1, nằm trong local commit `90528af7fa0de989282425f1cb726479c8d8226b`. Lượt hiện tại chỉ lập kế hoạch thực thi; không chạy research mới, sản xuất ad, tạo preview, gọi reviewer, mở account hoặc commit. Approval định hướng không tự chọn một cohort/locale hoặc chấp thuận spend.

Kết quả của đợt thực thi offline được đề xuất: một bộ content có căn cứ, dễ review và tái dựng, gồm hai ad hoàn chỉnh cho cohort đã chọn (ba nếu dùng baseline C), preview, claim/source ledger và experiment proposal. Mỗi ad giúp đúng role nhận ra một tình huống, hiểu một cách nhìn và liên tưởng đúng chuyên môn với Digiwin. Hoàn thành production package không chứng minh awareness lift hoặc readiness live.

Owner: planner viết kế hoạch; executor được Bảo giao sau sở hữu production; auditor có nhiệm vụ read-only đối chiếu acceptance; Bảo quyết định business trade-offs. Không kích hoạt delegation/slice song song trong kế hoạch này. Không tự đặt deadline hoặc người duyệt ngoài Bảo.

## 2. Đầu vào đã có và các lựa chọn chưa chốt

Đã có: library 11 narrative, O4-Q/O4-O, hai loại phép thử, native LinkedIn baseline, cơ chế pin baseline, category/buying cue hypotheses, cue inventory acceptance, decision boundaries. Có creative/source register đa locale và hai audit v1.0 đã được thẩm định; audit không tự thành lệnh sửa hoặc xác nhận v1.1 đã PASS.

Các lựa chọn còn mở: Quality/Process hay Operations wave đầu; test cách kể cùng pain hay test gói; cặp POV; baseline C và locale. Format đã chọn carousel images + copy; association chính đã chọn ERP có chuyên môn/kinh nghiệm semiconductor, cụ thể hóa theo role trong brief. Trần planning 35 triệu đến Scale 1 là current ceiling; allocation/ngày chạy/thuế phí/live authority chưa chốt. Company List Building là snapshot ngày 30/09, không phải kết quả live ngày 01/10. Canonical landing locale đã có deployment note superseding snapshot cũ; carousel wave này có destination tới một LDP phù hợp để đọc thêm; không lấy click landing làm mục tiêu chính.

**Đề xuất để Bảo chọn ở checkpoint G1:** Quality/Process, O1/O4-Q, test cách kể cùng tình huống truy vết test bất thường, cùng carousel image format; không baseline C để giữ hai cells; VI dùng làm bản review nội bộ đầu. Đây là recommendation planning, chưa chọn thay Bảo và chưa xác lập ngôn ngữ delivery của cohort. Operations O2/O4-O là option thay thế ngang cấp; account feasibility có thể làm thay đổi shortlist khi được phép kiểm tra.

## 3. Work packages và dependency

| ID / giai đoạn | Việc cần làm và input | Output dự kiến / điều kiện hoàn thành | Dependency / quyền / stop |
|---|---|---|---|
| E0 — Khóa execution scope | Reconstruct Git, đọc current truth, đối chiếu approval v1.1 và revision inputs | Decision register: cohort, POV, loại test, association, locale, format, C có/không, phạm vi quyền | G1: Bảo chọn hoặc giao quyền chọn các options. Chưa có thì tiếp tục research/library được giao, không viết final pair như đã chọn |
| E1 — Research phục vụ nội dung | Phụ trách R1–R4 bên dưới, bắt đầu local rồi primary public khi được giao; R5 desk feasibility hỗ trợ E6, account validation thuộc E8 | Evidence register + gap log + recommended shortlist có căn cứ | Không mở account, outreach/PII hoặc infer buyer validation; thu hẹp claim nếu proof thiếu |
| E2 — Brief từng ad và pair contract | Inputs: E0 decisions, E1 evidence | Hai brief A/B; C nếu được chọn; source/association/cue/controls rõ; pin revision | G2: reviewer đối chiếu role, pain và loại test; thiếu product scope thì giữ hypothesis hoặc đổi wording trước final copy |
| E3 — Copy và storyboard | Inputs: accepted briefs; current creative tokens | Complete records, short/long body alternatives để review, headlines/image text/CTA/alt text và storyboard | Chỉ ghi paths của slice; không rewrite asset canonical hoặc thay brief material âm thầm |
| E4 — Rough previews và review | Inputs: E3, cue inventory, carousel contract đã chọn; account preview còn chờ gate | Preview và QA từng ad được chọn, gồm baseline C nếu có; treatment tương đương theo pair contract; issue log; claim/content/mobile/brand checks | G3: chốt bản copy dùng để render; reviewer native/product nếu có. Không giả làm target buyer |
| E5 — Production và localization chọn lọc | Inputs: copy đã chốt, source visual được phép dùng, format spec đã xác minh hoặc ghi unknown | Editable sources, rendered exports và QA evidence; locale chỉ cho shortlist được giao | G4: native/format review cho release tương ứng. Không dịch toàn bộ library hoặc sản xuất mọi format |
| E6 — Experiment proposal | Inputs: pair contract, content; phụ trách R5 desk feasibility từ official docs khi được giao | Experiment card, metric dictionary, decision rules, thiếu account inputs ghi rõ | Desk feasibility không thay account validation E8; chưa có baseline/budget thì card draft, không bịa sample hoặc gọi LIVE READY |
| E7 — Audit và handoff offline | Inputs: artifact manifest và E1–E6 | Findings reconciliation, status theo scope, docs sync, handoff pack | G5: independent inspection nếu được giao; không tự coi self-review là audit. Commit/merge/push cần mandate tương ứng |
| E8 — Live validation/test, future scope | Phụ trách phần account validation của R5, chỉ sau offline handoff và operational mandate riêng | Current account evidence, exact setup/test authorization, sau delivery có learning report | Được hoạch định để biết dependency; chưa thực hiện. Discovery audience không tự được attach; không enable/spend bằng approval plan |

Trình tự: E0 → E1 → E2 → E3 → E4 → E5 → E7. E6 có thể được soạn sau E2 rồi cập nhật bằng asset final; chỉ được chốt khi inputs tương ứng có thật. Research mức library không bị chặn bởi account Building nếu chưa cần account evidence. Mọi giai đoạn có gate chỉ chặn việc phụ thuộc gate đó, không chặn công việc độc lập đã được giao.

## 4. Research: câu hỏi, nguồn và stop rule

| Research | Câu hỏi phải trả lời | Nguồn ưu tiên / evidence cần ghi | Done / giới hạn |
|---|---|---|---|
| R1 — Role và tình huống | Role cần đưa ra quyết định gì? Thuật ngữ và dữ liệu nào thật sự liên quan? | Kickoff/S01/S03, official industry/process material; nếu reviewer ngành được giao, ghi review scope | Mỗi shortlisted POV có role/task/operating question/source và counterpoint; nguồn public không chứng minh mức phổ biến trong buyer VN |
| R2 — Category và buying cue | Khi nào tình huống công việc chuyển thành nhu cầu đánh giá giải pháp? | Existing source/brief, primary research về CEP; ghi reasoning và alternative explanation | Mỗi brief có category, operating situation, buying cue hypothesis, desired association; không gọi CEP validated khi chưa có buyer evidence |
| R3 — Product/proof/rights | Câu capability dự định viết có đúng offer/entity/territory không? | Official Digiwin materials, approved claim/governance registers và product reviewer nếu được giao | Mọi factual paid claim có exact wording/source/excerpt/date/scope/rights state; thiếu thì remove/narrow hoặc giữ internal unresolved; approval existing VI scope không bị mở lại vô cớ |
| R4 — Asset/format/brand | Tái dùng nguồn nào? Có thể giữ branding và test controls không? | Current source/final assets, design system; official current format docs khi execution được giao | Candidate manifest, revision/hash, cue inventory và spec verification date; official docs không tự xác nhận active-account capability |
| R5 — Account/measurement feasibility, future gate | Cohort/format/metric có khả dụng? Split có khả thi và budget có đủ? | E6: desk feasibility từ official docs khi được giao. E8: current UI validation chỉ với mandate account riêng. E1 chỉ phụ trách R1–R4 | Phân biệt doc-supported và account-observed; chưa access thì unknown. Không gọi company match là role delivery |

Research method: chốt câu hỏi theo shortlist, ưu tiên reuse nguồn đã có, tìm primary public để lấp gap cụ thể. Ghi query/source/access date/excerpt, phạm vi hỗ trợ và điều không hỗ trợ; đánh dấu fact/hypothesis/inference/proposal. Source review khác product review và rights approval. Ngừng tìm khi đủ căn cứ cho wording đã chọn; nếu vẫn thiếu sau nguồn phù hợp, báo gap và proposal thu hẹp, không mở rộng research chỉ để “đủ số link”.

Buyer interviews, surveys, recruitment và native expert contact là option research riêng cần mandate; không phải prerequisite bắt buộc cho internal copy draft. Research không có interviews vẫn có thể SUCCESS cho mục tiêu desk evidence, với buyer prevalence/brand association unknown rõ ràng. Không dùng agent role-play làm buyer evidence.

## 5. Content cần sản xuất và acceptance

### Bộ wave đầu bắt buộc sau khi execution được giao

- **Decision register:** một phiên bản scope có owner/revision và lựa chọn Bảo; mọi thay đổi material có lý do và ảnh hưởng.
- **Evidence/claim ledger:** liên kết từng factual sentence với source, scope và allowed wording; illustrative situations ghi là minh họa, không gán case khách hàng.
- **Hai brief A/B:** role, operating question, category/cue hypothesis, association, học được gì, proof, narrative beats, test type và controls. C nếu chọn phải có exact path/revision/hash/locale và delta.
- **Hai complete ad records:** hook, primary text short/long alternatives, platform headline, image text, CTA, alt text, format/locale/destination nếu cần. Hai body alternatives là options biên tập, không tự thành bốn cells live; pin bản chọn trước comparison.
- **Storyboards và rough previews:** preview và QA từng ad được chọn, gồm baseline C nếu có; pin đúng revision của image/caption/headline/CTA trong manifest. Pin source của C không thay preview/QA. Mỗi preview thể hiện ad hoàn chỉnh, nhìn ra Digiwin và operating scope; treatment tương đương nếu test cách kể. Carousel images là format đã chọn; story và copy theo từng card. Document/static là nhánh thử format sau nếu được giao.
- **Sources và exports:** editable text/source, fonts/assets được phép dùng, export manifest với hash/dimensions/revision; kiểm tra chữ, accents/glyphs, clipping, contrast, mobile readability, claim consistency. Production dùng contract trong LinkedIn_Carousel_Constraints_and_Awareness_Anchor.md; public spec đã đối chiếu, active-account preview/release vẫn cần gate.
- **Experiment proposal:** question/hypothesis, variables/controls, metric/action mapping, metric definitions, sample/budget dependencies, confounds, stop rule, unknown và authorization scope.
- **QA/audit/handoff:** findings đối chiếu nguồn, evidence của closure, residuals, status từng lớp và docs impact.

Narrative acceptance: mỗi ad phải gắn Digiwin với hình ảnh ERP chuyên môn/kinh nghiệm ngành semiconductor trong scope có proof; mỗi ad một pain, phù hợp trách nhiệm role, có một ý hữu ích, brand association cụ thể; không dồn mọi acronym vào hook. Cách kể đủ khác để trả lời question của test. Test gói có manifest khác biệt; không gọi thuần storytelling nếu khác pain/cue/format. Branding pin logo/name/tokens/path/revision, mức nổi bật/placement tương đương khi cần; consistency không tự là proven distinctiveness.

Các nhánh sau: F1/F2, P1/P2, P3 domestic, O3 finance, B1 credibility; library brief có thể mở rộng khi được giao. Locale/format sau chỉ sản xuất cho narrative shortlist. P3 end-user và P1/P2 partner khác objective; không gộp chỉ vì chung route.

## 6. Acceptance gates và xử lý thiếu evidence

| Gate | Điều kiện qua | Nếu chưa qua |
|---|---|---|
| G1 — Scope chosen | Record cohort, cặp POV, association, test type, locale/format và C decision | PLANNED/READY_FOR_DECISION; desk work độc lập vẫn có thể được giao |
| G2 — Brief ready | Role fit, cue/category hypotheses, evidence boundaries, pair contract; C pinned nếu có | NEEDS_REVISION nếu brief sai; BLOCKED nếu input bắt buộc unavailable; không dựng final claim thiếu proof |
| G3 — Copy ready for preview | Wording/source alignment; một pain; desired association; copy phiên bản chọn rõ | Sửa issue có evidence; đừng gọi buyer validated khi chỉ self-review |
| G4 — Offline production ready | Render/source match, cue inventory, layout/mobile/glyph QA, native review ở scope locale release cần có | Có thể handoff PARTIAL nếu output internal dùng được nhưng native/product/format gap còn material |
| G5 — Offline handoff accepted | Manifest, QA, reconciled audit nếu được giao, experiment draft có unknown, docs synced | Nếu audit chưa performed, báo đúng; không tuyên bố AUDIT_PASS. Scope đã chốt yêu cầu independent audit thì thiếu audit chưa đạt final SUCCESS |
| G6 — Live test authorized | Account-specific eligibility/settings/formats/metrics, budget/dates/tax basis, exact authority và test card finalized | LIVE_NOT_AUTHORIZED hoặc BLOCKED nếu mandate đã có nhưng dependency fail; offline SUCCESS không tự qua G6 |

Critical là defect khiến named output/decision không đáng tin: unsupported factual live claim, sai role/association so với scope, thiếu asset promised, privacy/rights violation, uncontrolled test được mô tả như causal test. Material là gap làm thay đổi interpretation/release feasibility; minor là polish không làm sai decision. Audit severity phải reconcile với stage, nguồn và exceptions. Không đóng finding chỉ vì thêm checkbox.

## 7. Status model: execution, audit và learning tách riêng

### Task lifecycle và terminal execution status

| Status | Định nghĩa và evidence |
|---|---|
| PLANNED | Đã có task/scope, chưa bắt đầu; không gọi chưa được giao là BLOCKED |
| READY_FOR_DECISION | Có options/evidence đủ để Bảo chọn, dependent action còn chờ quyết định cụ thể |
| IN_PROGRESS | Đang thực hiện, nêu output đã có và next dependency; chưa terminal |
| READY_FOR_REVIEW | Artifact đủ để kiểm tra acceptance; chưa đồng nghĩa accepted |
| SUCCESS | Mọi critical criterion của scope được giao đạt, evidence/source/manifest tồn tại, docs impact hoàn tất; nếu scope yêu cầu audit thì audit đã đủ. Ghi qualified milestone, ví dụ SUCCESS — OFFLINE_CONTENT_PACKAGE |
| PARTIAL | Có subset hữu ích được chứng minh nhưng còn critical deliverable/gate chưa đạt; liệt kê phần đạt, thiếu, owner/action tiếp |
| FAILURE | Đã thực hiện nhưng critical criterion không đạt hoặc có material regression/unintended outcome; không dùng cho việc chưa thử |
| BLOCKED | External input/access/decision/reviewer/resource cần thiết cản scope đã được giao; nêu observed evidence và việc độc lập còn làm được |

Một execution scope chốt bằng đúng một terminal status; mỗi work package có thể có status riêng. Gate waiting có thể là READY_FOR_DECISION trong planning; chỉ BLOCKED khi nó chặn execution đã được giao. Mọi record kèm scope, input revision, output/evidence, missing items, next action/owner nếu đã được giao và authorization. Không dùng “PASS” chung cho toàn dự án.

### Audit verdict

- AUDIT_PASS: independent inspection hỗ trợ mọi critical criterion trong audit scope, có evidence.
- AUDIT_FAIL: xác nhận criterion critical chưa đạt/material unintended result; ghi phạm vi bị ảnh hưởng.
- INSUFFICIENT_EVIDENCE: chưa đủ để kết luận, không đổi unknown thành failure.
- NOT_PERFORMED: chưa audit. Self-review ghi riêng, không đổi tên thành independent audit.

### Learning outcome sau live test (future scope)

- INSUFFICIENT_DATA/HOLD: delivery thiếu hoặc không comparable; vẫn có thể SUCCESS cho việc thu thập/báo cáo đúng mandate.
- REVISE: bằng chứng content/role/attribution có vấn đề trong review scope.
- CONTINUE_TEST: có descriptive signal nhưng chưa đủ cho decision đã định trước.
- PROPOSE_EXPANDED_DELIVERY_TEST: evidence hỗ trợ tranche học tiếp; cần authority trong envelope, không chứng minh brand lift.
- BRAND_EFFECT_UNKNOWN: chưa nghiên cứu memory/association phù hợp; luôn report riêng với execution result.

Không thấy uplift hoặc không có winner không tự là execution FAILURE. Tăng CTR không tự là content SUCCESS về brand-memory. Một test được triển khai/báo cáo đúng và cho kết quả không kết luận được có thể SUCCESS cho learning execution, với INSUFFICIENT_DATA cho business question. Mọi kết luận nhân quả cần thiết kế/evidence tương ứng.

## 8. Measurement và live handoff dự kiến

Offline: kiểm completeness từng record, source-to-copy, pair equivalence theo test type, advertiser attribution self-check và visual QA. Product/native/buyer review ghi người/role/phạm vi khi thực sự có và được phép ghi; public evidence sanitize, không PII. Không đặt điểm tổng có trọng số để che một critical gap.

Live future: chọn metric khả dụng từ Campaign Manager; ghi numerator/denominator/window/timezone/currency/latency/unclassified share. Đúng tệp, reach/frequency, interaction và cost báo riêng; comprehension/brand recall cần research tương ứng. Không infer company×role giao nhau từ marginal reports. Sample/precision và spend cap được predeclare từ baseline/available budget, chưa có thì deferred unknown; không bịa threshold. Descriptive test có confounds phải báo trước và sau.

Live handoff cần current account identity/rights, formats/settings/CTA/metric availability, audience eligibility, carousel destination đúng route và locale, approved allocation/date/tax basis, test design và operational mandate. Baseline expansion/LAN OFF giữ theo nguồn; không silently chuyển website/Lead Gen. Account architecture 2 FDI/domestic campaign vs 3 segment ad sets cần reconcile ở account gate, không tự resolve bằng copy plan.

## 9. Paths, ownership và audit target

Proposed output root: `operations/linkedin-awareness-execution/` với `decision-register.md`, `evidence-register.md`, `briefs.md`, `ad-records.md`, `experiment-card.md`, `qa-and-handoff.md`; selected visual sources/exports trong thư mục slice riêng dưới `assets/linkedin/awareness-optimization/`. Đây là path plan, chưa tạo outputs. Có thể gộp file nếu dễ review; không xây framework/scheduler hoặc schema quá mức.

Execution writer đọc canonical/source docs nhưng chỉ ghi outputs được giao. Canonical build pack/register thay đổi khi selected output được duyệt, có owner riêng. Shared resource một writer; browser một controller. Nếu sau này cho delegation, slice contract phải thêm owner, input SHA/revision, dependency, read/write paths, output, acceptance và stop; plan này không spawn executor.

Audit target: kiểm actual selected records/previews/ledger/experiment card và gate evidence; đối chiếu tests type, O4 alignment, C pin, buying cue hypothesis, branding cues và decision boundary. Audit findings là claims cần thẩm định. Re-audit changed findings/dependencies; không bắt chạy lại mọi check hoặc áp hai skill dogfood tự động khi chưa invoked.

## 10. Documentation impact và trạng thái lượt này

Canonical CURRENT_STATE ghi nhận Bảo đã chốt v1.1 và đang ở planning-only execution stage. Plan v1.1 cần status addendum giữ lịch sử audit/hash, không rewrite hai audit. Format và positioning selection được đồng bộ sang build pack, Pre_Ad_Readiness và source plan; chưa đổi audience/budget/live truth; S01/S03/S04 chưa cần đổi ICP/KPI/budget proposals thành selected; selected format không tự là LIVE READY. Khi execution tạo/approve content, review theo DOCS_IMPACT_MAP và update statements stale trước handoff/commit.

Tiêu chí hoàn thành lượt lập plan: work packages/dependencies rõ; research questions/source/done/limits rõ; content deliverables và acceptance rõ; execution/audit/learning statuses rõ; scope planning-only và decisions pending rõ; docs approval synchronized.

**Terminal lượt này: SUCCESS — EXECUTION PLAN PREPARED FOR REVIEW.** E0–E8 chưa bắt đầu; content/research execution chưa được thực hiện. Independent audit execution plan: NOT_PERFORMED. File mới và addenda hiện là working-tree changes local, chưa stage/commit/merge/push. Quyền commit trước đó chỉ cho lần sửa v1.1, không tự áp cho các file mới lượt này.
