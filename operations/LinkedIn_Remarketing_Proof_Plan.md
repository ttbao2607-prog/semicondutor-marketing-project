# LinkedIn remarketing proof — branch goal và execution plan

Ngày: 2026-10-02 · Product Owner: Bảo · Status: `PLAN_ONLY / READY_FOR_PO_PLAN_REVIEW`.

Branch: `slice/linkedin-rmk-proof-plan`, tạo từ HEAD worktree `052b88bc0930729dab7b95493aaac4fcf8739ac7`. Checkpoint plan được xác định bằng containing commit; không merge main hoặc push. Main vẫn là canonical integration branch; tài liệu này là proposed slice, không tự thay thế quyết định canonical.

## 1. Mandate và goal của branch

Bảo yêu cầu lập plan trước cho hướng remarketing (RMK) dùng proof của Digiwin: thành công, case study, kinh nghiệm/uy tín quốc tế. Ghi goal/target, research cần trước khi làm, success criteria, nghiệm thu và boundary; commit checkpoint từ HEAD worktree hiện tại.

Business goal đề xuất: nối awareness “Digiwin thấu hiểu ngành” sang consideration “Digiwin có kinh nghiệm liên quan và bằng chứng đáng cân nhắc”. Target là người trong account/role semiconductor phù hợp đã có tương tác đủ điều kiện; chưa có evidence về tệp thực, intent mua hoặc thay đổi nhận thức. OSAT/Quality, Operations, Fabless và Supplier/Partner là các treatment ứng viên, không phải bốn campaign phải chạy.

Observable branch outcome: một proposal có thể review, xác định được proof nào dùng được cho persona/pain nào, cách nối proof tới bước tiếp theo, cách đo và điều kiện triển khai. Không coi việc tạo ảnh hay tăng CTR là bằng chứng business goal đã đạt.

Mandate hiện tại chỉ gồm plan và checkpoint tài liệu. Research sâu, viết production copy, tạo ảnh/demo và mọi live action là các phase sau, chưa được release bởi checkpoint này. Không tạo active persistent goal/tool automation.

## 2. Baseline, facts và unknown

| Nguồn tại base HEAD | Fact / giới hạn |
|---|---|
| `Semiconductor_Work_Kickoff.md`, mục 3–4 | RMK củng cố chuyên môn và dẫn tới bước tiếp theo; pain → proof → CTA; leads là tín hiệu cộng thêm. |
| `ads/linkedin/LinkedIn_Build_Pack.md`, Retargeting definition | Tài liệu ghi `LI-AUD-P1-ENGAGED-30D` có status Building, single-image/document engagement, reachable members >=300 và platform/UI eligibility. Đây là trạng thái được ghi trong tài liệu, chưa phải trạng thái account được chứng kiến; guardrail cần revalidate trước live. |
| `operations/LinkedIn_Awareness_Adcopy_Optimization_Plan.md`, mục 9 | Chữ Building chưa có live witness cho engagement audience; cấu trúc 3 segment ad sets và proposal 2 FDI/domestic campaigns chưa được reconciled thành kiến trúc live-approved. Company List discovery là nguồn khác, không phải tệp warm. |
| `operations/LinkedIn_Carousel_Governance_Record.md` | CAR-01 Taiwan/CAR-02 China/CAR-03 abstract/CAR-04 Vietnam approved offline v1. CAR-03 không có customer name/logo/result; văn phòng không chứng minh local deployment outcome. |
| `operations/Public_Source_Register.md` | PO approval 2026-09-29 cho case/claim đã có trong VI source và translation giữ đúng scope. Không suy rộng sang claim mới, logo/name mới hoặc translation riêng của 200+/700+ English carousel metrics. |
| `CURRENT_STATE.md`; `drafts/S04_Measurement_and_Budget.md` | 35m VND là ceiling planning qua Scale 1 trong 56 calendar days; channel split/paid-day schedule/tax-fees/spend chưa chốt. RMK không có allocation được duyệt. |
| Tracking contract / readiness | Website retargeting là scope riêng; Insight Tag đã từng observed không chứng minh audience readiness hoặc consent behavior. Native delivery và GA4 website behavior là hai measurement surfaces. |

Unknown cần giải quyết: proof cụ thể đủ source và quyền dùng; persona/pain ưu tiên; audience source có bao phủ awareness carousel images không; audience size/eligibility; objective/format/destination; locale; CTA/offer; allocation, review window và operational mandate. Không suy người xem đã đọc đủ carousel hoặc thấy ads theo thứ tự.

## 3. Creative hypothesis và target

Concept ứng viên: **Từ bài toán của bạn đến kinh nghiệm Digiwin đã tích lũy.**

Hypothesis: proof liên quan cùng bài toán giúp người đã tương tác hiểu lý do cân nhắc Digiwin hơn nội dung chỉ giới thiệu độ lớn thương hiệu. Đây là giả thuyết marketing, chưa buyer/performance validated.

| Proof lane | Job | Evidence tối thiểu / giới hạn |
|---|---|---|
| Case thành công liên quan | Chứng minh kinh nghiệm trong bài toán gần với người xem | Entity, bối cảnh, pain, Digiwin role, solution/deployment scope, result nếu có, period/baseline/denominator, source và usage decision. Nếu thiếu result chỉ gọi là implementation/experience case, không gọi thành công. |
| Kinh nghiệm ngành quốc tế | Bảo chứng chiều sâu và phạm vi kinh nghiệm | Nguồn company-controlled; ghi đúng Taiwan/China/entity/product/scope/date. Số khách hàng không chứng minh kết quả; hiện diện quốc tế không tự thành ranking/award/endorsement. |
| Hiện diện Việt Nam | Nối tới khả năng trao đổi tại địa phương | Evidence về hiện diện/hoạt động cụ thể; không suy team size, service availability, response SLA hay semiconductor outcome. |

Đề xuất ưu tiên case liên quan làm trung tâm, kinh nghiệm quốc tế làm nền, hiện diện Việt Nam làm điểm nối. Nếu không có case đủ evidence, trình lane kinh nghiệm ngành thay thế và ghi rõ thiếu case; không lấp bằng testimonial, số liệu hay case tổng hợp giả.

Narrative rough ứng viên, chưa khóa format/card count: bài toán → case/bối cảnh tương tự → vai trò/phạm vi/kết quả có evidence → kinh nghiệm ngành bổ trợ → bước tiếp phù hợp. Carousel 5 card là một option; single-image hoặc document có thể phù hợp hơn sau research. Mỗi ad tự đủ context, acronym và OSAT/Fabless được giải thích lần đầu theo first-mention rule, không giả định lượt tiếp xúc trước.

## 4. Research bắt buộc trước production

| ID | Câu hỏi / phương pháp | Output và gate |
|---|---|---|
| R1 — Inventory | Rà VI landing/creative, source brief, governance và source register ở revision pin; phân biệt approved existing claim với candidate mới. | Proof ledger và source-map, không sửa artifact lịch sử. Mỗi record có ID, source path/hash hoặc URL/access date/excerpt, entity, market, product, pain/persona, relationship, outcome, rights/approval scope, allowed wording và unknown. |
| R2 — Verify proof | Mở nguồn official Digiwin gốc; phân biệt solution page, customer relationship, implementation case và measured outcome. Đối chiếu số, đơn vị, thời gian, baseline và attribution. | Mỗi claim phân loại usable-within-existing-scope / requires-PO-decision / unsupported-remove. Nguồn inaccessible không coi verified. Không ép có đủ ba lane. |
| R3 — Rights | Map từng case/name/logo/photo/quote tới quyết định hiện có; không phủ định approval VI đã ghi, cũng không mở rộng approval. | Rights matrix; unknown làm hold claim bị ảnh hưởng. PO xử lý material rights/scope decision; không tự nhắn khách hàng hoặc thu thập thông tin cá nhân. |
| R4 — Audience/format | Tra docs LinkedIn official hiện hành về retargeting sources, carousel-image engagement, document/single-image, windows, eligibility/min size, objective/format/placement. | Route memo có URL/date và phân biệt documented vs account-observed. Không mặc định carousel nuôi `LI-AUD-P1-ENGAGED-30D`; platform docs chưa đủ để xác nhận tệp account. |
| R5 — Relevance | Match case và pain tới role/segment trong source brief; xác định tình huống kích hoạt, nhu cầu phát sinh, proof phù hợp và liên kết mong muốn với Digiwin. Role/pain tự nó chưa chứng minh tình huống buyer nhớ tới nhà cung cấp. | Shortlist có rationale, trigger hypothesis và gaps; đề xuất một persona/pain/pilot locale, không chia nhỏ audience khi chưa có size evidence. Tình huống mua là giả thuyết đến khi có buyer evidence; buyer validation không phải gate bắt buộc trước draft. |
| R6 — Measurement/destination | Review native reporting, existing route measurement và CTA; phân biệt nhu cầu tìm hiểu qua case với nhu cầu trao đổi khi đang đánh giá giải pháp, đề xuất bước tiếp phù hợp cho nội dung được chọn. | Measurement memo, source-of-truth cho từng metric, destination/offer và trade-off. Hai nhu cầu là content hypotheses, không phải hai nhóm intent đã xác minh trong tệp; không bắt buộc hai CTA trong một ad hoặc chia audience. Website route/tag/form thay đổi phải có mandate riêng. |

Public official-web research là route đề xuất cho R2/R4 khi phase research được release. Live-account read-only inventory cần mandate riêng ghi account/profile/resource/controller; không browser login, upload, attach hoặc tạo audience để “nghiên cứu”. Trước Chrome/LadiPage action đọc local guidance và skill áp dụng. Không invent new tracking threshold/event, không dùng `accepted_form` chưa verified.

## 5. Execution slices và gates

Không kích hoạt slice/delegate trong plan này. Coordinator quản lý contract/audit; executor được giao là leaf và một writer cho mỗi output. Bảo quyết định business scope. Auditor độc lập với writer khi khả dụng; chưa assign reviewer, không claim independent audit từ tự kiểm tra.

| Slice / owner khi được giao | Input / dependency | Output / acceptance | Read/write và stop |
|---|---|---|---|
| P0 — parent planner, mandate hiện tại | Base HEAD + canonical docs | Plan, current-state discoverability, local checkpoint; criteria mục 6 | Write đúng hai file của checkpoint; stop nếu dirty/shared-writer conflict. |
| P1 — assigned research executor | P0 review/research release; R1–R6 | Proof ledger, rights matrix, platform route memo, shortlist; mọi claim traced, unknown explicit | Read local/public approved sources; write folder riêng `operations/linkedin-rmk-proof/`; không account action. Hold affected item khi evidence/rights thiếu. |
| P2 — assigned strategy executor | P1 + PO chọn persona/pain/lane/locale/offer | Creative brief, audience/architecture options, measurement/test proposal, decision pack | Write slice-owned draft; không sửa canonical account architecture, budget hoặc source approval. Stop material trade-off. |
| P3 — assigned creative executor | PO chọn brief + production mandate | Copy/storyboard và bounded offline pilot; source-map, manifest, pinned demo, desktop/mobile QA, human receipt | Dùng canonical design system + page override phù hợp; giữ awareness assets frozen. Áp dụng demo/human-audit runbook cho carousel; format khác cần scope riêng. Không fullbatch trước pilot acceptance. |
| P4 — auditor + Bảo | Exact P3 revision | Audit evidence và explicit revision-bound content decision | Auditor read-only; correction cùng writer. Revised claim/copy/image/order/locale/destination invalidates dependent acceptance. |
| P5 — separately authorized operator | Content acceptance + account evidence + approved measurement/budget/live mandate | Account build QA/launch/reporting theo contract riêng | Một browser controller; một account-object writer. Không bắt đầu bởi plan/content acceptance. |

## 6. Success criteria và nghiệm thu

### Checkpoint plan hiện tại

- Goal/business target và observable branch outcome rõ; facts/proposals/unknown tách biệt.
- Research có câu hỏi, nguồn, output và gate trước production; case/result/rights/audience gaps được ghi nhận.
- Plan có owner/dependency/output/acceptance/read-write/stop; không tự release production/live.
- Tiêu chí content, measurement và live readiness dưới đây có thể audit; không bịa KPI/budget.
- Docs-impact reviewed; diff chỉ gồm plan và current-state note; sanitized, không thay source/PNG/receipt/history.
- Branch parent đúng base HEAD; containing commit tồn tại, worktree sạch sau commit; không merge/push.

P0 execution terminal chỉ `SUCCESS` khi toàn bộ tiêu chí trên đạt; `PARTIAL` nếu còn gap có ý nghĩa, `BLOCKED` nếu external dependency ngăn completion, `FAILURE` nếu material unintended change. Checkpoint không phải PO plan/content approval. Review độc lập mục tiêu: kiểm tra actual files/diff/base-parent/commit và tiêu chí trên, verdict `AUDIT_PASS`, `AUDIT_FAIL` hoặc `INSUFFICIENT_EVIDENCE`; nếu chưa có reviewer phải ghi pending.

### Content acceptance sau research/production

- 100% factual claims có source-map và scope/rights disposition; không unknown claim lọt vào customer-facing asset.
- Mỗi proof liên quan tới pain/persona và giải thích Digiwin role; outcome không biến thành guarantee/cross-market inference.
- Không dùng award/ranking/“uy tín quốc tế” như factual superlative thiếu evidence; ưu tiên bằng chứng cụ thể.
- Ad hiểu được khi gặp độc lập; first-mention clarity và locale terminology được review; caption/headline/body/CTA thống nhất.
- Trước pilot offline, chốt một câu hỏi học hỏi chính về nội dung. Human review kiểm tra người xem nhận đúng Digiwin là advertiser, hiểu vai trò Digiwin trong case và giới hạn proof. Ghi câu trả lời/nhầm lẫn cùng revision, loại người review và giới hạn mẫu; logo/màu nhất quán chưa chứng minh buyer recognition. PO/editorial review không được báo thành buyer validation.
- Exact copy/image records pin revision/hash; rendered desktop/mobile không clipping, proof qualification và nguồn thiết yếu đọc được; không chỉ dựa vào native PNG hoặc source inspection.
- Explicit PO human content decision gắn revision; mechanical QA không thay buyer validation hoặc live approval.

### Business test proposal và live readiness

- Trước launch chốt hypothesis, primary metric, denominator, review window/sample sufficiency, cost envelope, decision rule và owner. Chưa đủ dữ liệu để đặt CTR/CPL lift hoặc frequency cap bằng số trong plan này.
- Pilot offline kiểm tra hiểu nội dung/proof, attribution về Digiwin và render; không đo hiệu quả RMK. Live test phải có câu hỏi học hỏi chính và tiêu chí delivery riêng. Consumption/progression chỉ hỗ trợ kết luận hành vi; muốn kết luận buyer nhớ Digiwin trong tình huống mua cần nghiên cứu liên kết brand–tình huống phù hợp, không mặc định thêm nghiên cứu đó làm gate cho draft.
- Delivery guardrail: source audience eligible, actual reachable size và targeting overlap/exclusion được UI evidence xác nhận. Nếu thiếu carousel-source route hoặc tệp quá nhỏ, hold RMK; không mở tệp sai ICP cho đủ số.
- Attention: metric native phù hợp format thực (document engagement/consumption nếu available); progression: destination interaction có measurement verified. Leads/qualified leads là optional, nguồn rõ.
- Nếu test hai cách kể, giữ audience/offer/proof/locale/destination và delivery settings có thể so sánh; đổi nhiều yếu tố phải gọi package test, không suy causal effect của riêng proof.
- Báo frequency/fatigue, spend và audience quality cùng attention/progression. Warm-vs-cold CTR hoặc pre/post tự nó không chứng minh incremental impact.
- Nhận thức/tin tưởng thương hiệu chỉ được claim có research phù hợp; behavioral metrics là proxy. Kết quả ít mẫu báo inconclusive, không gọi winner.
- Budget nằm trong ceiling đã ghi nhưng allocation/pacing/tax-fees và quyền spend phải được PO chốt; không mặc định dùng reserve 150k/ngày hay lịch cũ.

## 7. Protected state và handoff

Không sửa awareness scenarios/copy/images/demo/manifest/receipts; không overwrite CAR-01–04 hoặc promotes RMK thành canonical creative. Không sửa landing, PopupX/form/receiver, GTM/GA4/Insight Tag, campaign/audience/account settings, organic backlog. Không login, credential/PII collection, audience upload, form submit, publish/stage/enable/spend hoặc gửi message bên ngoài. Không secret/private URL/raw account/lead data trong Git.

Decision pack sau P1/P2 phải để Bảo chọn persona/pain, proof lane và claims đủ scope, pilot locale/format, offer/destination, test question, budget và route mandate nếu cần. Evidence thiếu chỉ hold phần liên quan; không rewrite lịch sử để khớp proposal.

Docs impact: đã review `CURRENT_STATE.md`, `DOCS_IMPACT_MAP.md`, kickoff, build pack, readiness, proof governance/register và measurement baseline liên quan. Chỉ current-state discoverability cần note mới. Build pack/readiness/governance/tracking/budget giữ nguyên vì chưa có adoption, proof approval hoặc operational transition. Khi phase sau đổi current truth, sync đúng canonical docs trong impact map trước PASS/commit/handoff.

Checkpoint review: parent self-review content/diff và Git persistence; independent audit chưa thực hiện. Trạng thái research/production/live: `NOT_STARTED / NOT_RELEASED`.

## 8. Plan refinement checkpoint (2026-10-02)

Bảo authorized cải tiến plan theo thẩm định audit rồi commit và dừng. Tiếp thu trigger hypothesis ở R5, hai nhu cầu bước tiếp ở R6, kiểm tra attribution/role trong human review, phân biệt offline learning với live measurement và wording audience theo cấp evidence. Đây là refinement của plan, không xác nhận intent/tình huống mua, buyer recognition hoặc audience readiness. Không thêm buyer-research gate bắt buộc trước draft; không release research/production/live. Containing commit là checkpoint refinement; audit dogfood được dùng làm input phản biện, không tự coi mọi nhận định là blocker hoặc independent acceptance của revision mới.
