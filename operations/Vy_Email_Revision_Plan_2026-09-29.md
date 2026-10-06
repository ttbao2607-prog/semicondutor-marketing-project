> **Main integration · 2026-10-06 — adapter DEVELOPING / NOT_FROZEN.** Bảo chỉ cho tích hợp checkpoint `ffb4fba` (anchor/gate và adapter draft) vào main local; adapter còn developing, chưa freeze/adopt/release. Core ImageGen frozen giữ nguyên scope riêng. [Phạm vi tích hợp và dependency](linkedin-locale-adapter/Main_Integration_2026-10-06.md): không đưa ảnh/viewer/input journey VI cũ lên main; full-journey dogfood, native EN/Chinese QA và creative acceptance còn pending. Các receipt/source-only status bên dưới giữ phạm vi checkpoint cũ, không chứng minh input/asset hiện có trên main. Không push/live.

> **Message anchor · 2026-10-06 — MSG-ANCHOR-01 bắt buộc.** Email gốc đã được Bảo cung cấp trực tiếp trong phiên; [anchor nội dung VN / FDI EN–Chinese](Vy_Email_Content_Anchor.md) tách định hướng audience/persona/message khỏi đề xuất vận hành và phần đã superseded. FDI tập trung business value/ROI có căn cứ; VN là ERP hỗ trợ chuẩn bị năng lực vào chuỗi. Phải đối chiếu anchor revision/SHA256 trước generation và hậu kiểm từng artifact/surface + toàn journey. FAIL → CHANGES_REQUIRED; thiếu review/binding/evidence → INSUFFICIENT_EVIDENCE; đều chặn SCRIPT_REVIEW_PASS và ready/accepted handoff. Core harness, artwork và receipt cũ giữ nguyên; không PASS hồi tố. Những ghi nhận email gốc chưa có và budget/schedule/proposal cũ bên dưới giữ nghĩa lịch sử, không thay trạng thái hiện hành. Bảo đã yêu cầu commit checkpoint local trên nhánh hiện tại; containing commit lưu anchor/gate và adapter draft. Không merge main/push/live; các ghi nhận chưa commit bên dưới là snapshot chuẩn bị.

# Kế hoạch xử lý email điều chỉnh — checkpoint 2026-09-29

**Ngày lập:** 2026-09-29

**Nguồn Git:** checkpoint gốc lập từ local `main` tại `bf6038d` (lúc đó chưa push); lần cập nhật này ở worktree `slice/vy-email-strategy-plan` tại base `a71acbc`. Đây là trạng thái file local, không phải xác nhận remote/GitHub.

**Trạng thái:** checkpoint kế hoạch sau các quyết định của Bảo. Các slice offline được làm trong worktree riêng; tài liệu này không xác nhận bản live, publish, account action hoặc spend. Tính đến audit offline 2026-09-29, cả ba route có candidate HTML/copy bốn locale và QA local; Cả ba HTML đã được kết hợp với source PageSpeed trong local integration commit `6fa842e`, với tracking regression và runtime bốn locale ở 320px/desktop đạt QA offline. LinkedIn đã có source-copy register, 9 static SVG/PNG và 3 PDF sáu trang được render/QA, cùng 12 carousel PNG candidate/prototype 1254×1254. B2B v2 có 9/9 biến thể offline `vi`/`zh-Hans`/`zh-Hant` trên OSAT/Fabless/Supplier; không suy có bản EN B2B mới. Workbook local có 11 sheet (7 sheet nguồn + 4 sheet thêm) và ghi rõ 56 ngày lịch/tối đa 35 ngày paid/trần 35 triệu. Các output này đã nằm trong local commit `6fa842e`; chưa có bằng chứng push GitHub hoặc đưa locale lên live, và original workspace local `main` đã tới docs commit `2099d9e` sau integration `6fa842e`; dùng `git worktree list` để kiểm trạng thái worktree hiện tại.
**Đối chiếu public PageSpeed (2026-09-29):** Ba URL live vẫn là bản tiếng Việt sau revision PageSpeed riêng. Bảo đã đóng scope đó ở `P4_P5_CLOSED_PARTIAL_ACCEPTANCE_FROZEN` dù Mobile live vẫn dưới 80; ba receipt revision còn PENDING. Locale và creative offline của plan này chưa sync live. Local integration `6fa842e` đã dùng semantic patch để giữ các đoạn PageSpeed publish/retry/closeout mới hơn; coordinator đã fast-forward local `main` tới `2099d9e` qua `6fa842e`; các bước closeout Git tiếp theo ghi trong `operations/Git_Consolidation_2026-09-30.md`.
**Ưu tiên nguồn:** chỉ đạo mới của Bảo > kickoff v2.0 > source brief. Email của Vy là đề xuất cần chuyển thành quyết định rõ, không tự coi là phê duyệt launch/budget.

## 1. Execution contract

**Goal.** Sau khi triển khai và được audit, bộ kế hoạch paid có một định nghĩa thị trường, hai nhánh FDI/nội địa rõ ràng, cấu trúc LinkedIn/Search có thể build, từ khóa và KPI có nguồn, ngân sách/lịch nhất quán, cùng **ba landing route OSAT/Fabless/Supplier và các asset LinkedIn liên quan có ba ngôn ngữ, bốn locale `vi/en/zh-Hans/zh-Hant`**. Mỗi locale phải giữ đúng claim được phép, CTA, tracking và route.

**Scope.** File này là plan/checklist trong branch riêng; các executor slice được giao riêng mới sửa canonical docs, HTML, asset hoặc workbook. Không truy cập/upload dữ liệu Lark; không tạo Matched/Predictive Audience; không sửa live account, tag, campaign, LadiPage, form hay spend. Branch PageSpeed do agent khác giữ là protected state.

**Measurement.** Một đầu việc chỉ `PASS` khi artifact thực tế và canonical docs không mâu thuẫn, bằng chứng QA được ghi, và các unknown không bị điền thành fact. Trạng thái cuối giai đoạn thực thi dùng đúng một trong `SUCCESS`, `PARTIAL`, `FAILURE`, `BLOCKED`; audit độc lập dùng `AUDIT_PASS`, `AUDIT_FAIL`, `INSUFFICIENT_EVIDENCE`.

**Audit target.** Auditor đối chiếu diff với `main`, ma trận route–language–asset, phép tính ngân sách, keyword/KPI register, checklist QA và `DOCS_IMPACT_MAP.md`. Review trạng thái file thực, không chỉ lời báo cáo executor.

## 2. Quyết định và phần còn mở

| ID | Quyết định | Vì sao cần chốt trước bước phụ thuộc |
|---|---|---|
| D1 | Định nghĩa chuỗi cung ứng bán dẫn được tính vào ICP; cách gắn FDI/nội địa với OSAT/Fabless/Supplier; có loại trừ tập đoàn có hệ thống chung theo tiêu chí nào | Giữ hai trục phân khúc nhất quán; không biến giả định trong email thành account fact |
| D2 — Bảo đã chốt | Ba ngôn ngữ/bốn locale: `vi`, `en`, `zh-Hans` cho China FDI, `zh-Hant` riêng cho Taiwan FDI | Cần native domain/market review riêng cho hai bản Trung; không gộp thành một bản ZH hoặc coi script conversion là QA |
| D3 — Bảo đã chốt | Mỗi route hiện có giữ một HTML/cùng URL, có bộ chọn ngôn ngữ ở đầu; tham số không chứa PII `lang=vi|en|zh-Hans|zh-Hant` chọn locale ban đầu từ quảng cáo | Còn QA runtime, giá trị sai/thiếu, ưu tiên lựa chọn người dùng/persistence, encoding, UTM/gclid, PopupX và hành vi trên trang live; không tạo URL route riêng |
| D4 | Phạm vi creative LinkedIn phải dịch: ba static concepts, sáu trang OSAT document, bốn carousel cards và các square exports; bản nào cần message adaptation theo FDI/nội địa thay vì dịch sát | Tránh xuất bản bản dịch sai audience hoặc claim |
| D5 — Bảo đã chốt trần; lịch paid còn mở | Trần **35 triệu đến hết Scale 1** trong **8 tuần lịch/56 ngày lịch**. Nếu dùng đơn giá 1 triệu/ngày và dùng hết trần thì tối đa 35 ngày paid; 56 ngày lịch không phải 56 ngày paid. Scale 2 **8,75 triệu** cần phê duyệt riêng | Phân bổ paid days theo phase, reserve và lịch giao thực tế còn cần thiết kế/duyệt; không suy trần là lệnh spend. Main cũ 28+8,75 và workbook địa phương cũ 35+8,75 là proposal lịch sử, không phải ngân sách cùng kỳ được cộng/tráo đổi |
| D6 | Đúng workbook Excel Vy nhận xét và quyền chỉnh sửa nó | `.xlsx` trên `main` là asset inventory, không phải nhật ký spend |
| D7 | Có mandate riêng cho inventory/research trong tài khoản Google/LinkedIn và cho publication sau khi draft được duyệt hay không | Plan không tự cấp quyền browser/account action, audience upload hoặc publish |

## 3. Workstream và đầu ra

| Slice / owner | Input, dependency | Output và acceptance | Quyền đọc/ghi; stop condition |
|---|---|---|---|
| S1 — Strategy / một writer tài liệu | Email, kickoff, S01, S03; phụ thuộc D1 | ICP criteria; ma trận FDI/nội địa × OSAT/Fabless/Supplier; account-source register `verified / candidate / unknown`. Không ghi tên account chưa xác minh như khách hàng | Đọc nguồn sanitized; ghi strategy draft. Dừng nếu định nghĩa ngành hoặc quyền dùng nguồn không rõ |
| S2 — Channel architecture / một writer build packs | S1, evidence account hiện có; D3/D4 | LinkedIn hai hướng tách biệt; Search VN chính, FDI nhỏ EN/zh-Hans/zh-Hant theo thị trường và brand group chỉ khi query/landing phù hợp; cấu trúc object là draft. Có mapping audience → copy → route/locale → KPI | Ghi build packs, không tạo object live. Dừng nếu platform/placement/size/permissions unknown trở thành điều kiện bắt buộc |
| S3 — Keyword research / một writer S02 | S1, S2, Planner evidence cũ; D7 nếu cần research live | Register VI/EN/zh-Hans/zh-Hant theo intent, route, match type, displayed volume + cấu hình/ngày hoặc `no displayed data`; negative taxonomy gồm đầu tư, tuyển dụng, học tập; brand terms tách riêng | Nghiên cứu offline trước. Không bịa volume, không tạo thêm Planner draft nếu chưa có mandate chấp nhận side effect |
| S4 — Landing localization / một writer mỗi route | Ba canonical HTML, design system và page overrides, tracking contract; D2/D3 đã chốt, native/scope QA | OSAT, Fabless, Supplier mỗi route có `vi/en/zh-Hans/zh-Hant` customer copy trong một HTML; mobile/desktop QA; claim và CTA đúng scope; link quảng cáo giải đúng locale. Ba HTML/copy candidate bốn locale đã kết hợp với PageSpeed và qua QA tracking/runtime local; native review và live handoff còn mở | Ghi source/draft trong branch riêng khi được giao. Case/claim đã có trong VI được Bảo duyệt dịch/dùng; không nới số liệu, thực thể, địa lý, thời gian, quan hệ hoặc source. Trước live sync đọc `$ladipage-operator` `revise_existing_page`, đối chiếu PENDING receipt/page identity và preflight |
| S5 — LinkedIn localization / một writer creative pack | S1, S2, S4, carousel governance/proof; D2/D4 | Asset matrix `concept × locale × segment × format`; source-copy register có bốn locale cho ba SVG concept, sáu trang document và bốn carousel cards. 9 static SVG/PNG, 3 PDF sáu trang và 12 carousel PNG candidate/prototype đã render/QA offline; B2B v2 có 9/9 biến thể offline `vi`/`zh-Hans`/`zh-Hant` trên ba concept; không có bản EN B2B mới. Native review, account-format check và live gate còn mở | Chỉ asset offline trong branch khi được giao. Không upload/attach/publish; case/claim có trong VI được Bảo duyệt dịch/dùng trong scope gốc, không tự thêm customer/logo hoặc claim mới |
| S6 — KPI, budget, schedule / một writer S04 | S1–S3, tracking contract; D5 trần đã chốt, lịch paid còn mở | KPI dictionary với numerator/denominator/source/baseline/decision rule; technical check 7 ngày tách khỏi search-term evidence quan sát; 35 triệu đến Scale 1 trải 8 tuần lịch, paid-day schedule theo phase còn mở; Scale 2 8,75 triệu gate riêng; weekly review/monthly decision | Ghi plan/scorecard. Không đổi live budget/tag/conversion hoặc suy test traffic là campaign result |
| S7 — Workbook / một writer workbook | S6, D6 | Workbook local 11 sheet (giữ 7 sheet nguồn, thêm 4 sheet) có daily log theo kênh, keyword/negative, account/audience metadata, KPI dictionary và đối soát 56 ngày lịch/tối đa 35 ngày paid/trần 35 triệu; đã QA bảo toàn công thức/table nguồn bằng dữ liệu giả. Lịch paid thực tế còn mở | Chỉ workbook được xác định. Không lưu raw Lark, lead/PII, private URLs hay audience export vào public repo |
| S8 — Docs sync & audit / coordinator, auditor | S1–S7, `DOCS_IMPACT_MAP.md` | Canonical docs phản ánh trạng thái thật; diff, artifact QA và contradiction review. HISTORY/LOG giữ nguyên quan sát cũ | Coordinator review/merge sau khi duyệt; không commit/push/merge theo plan này |

## 4. Checklist thực thi và nghiệm thu

### A. Chuẩn bị và khóa nguồn

- [ ] Preflight lặp lại cho slice tương lai: dùng `git-state-recovery`, ghi đúng local `main` SHA, worktree/branch và ownership trước khi sửa. Các slice Vy cũ đã được bảo toàn và tích hợp.
- [ ] Preflight lặp lại cho slice tương lai: đọc `CURRENT_STATE.md`, `DOCS_IMPACT_MAP.md` và canonical docs liên quan; ghi current truth và unknown. Docs consolidation 2026-09-30 đã đối chiếu.
- [x] Ghi D2/D3 đã chốt; D5 có trần 35 triệu/8 tuần lịch nhưng paid-day schedule còn mở. D1/D4/D6 và D7 xử lý theo dependency thực tế, không suy quyết định thành live mandate.
- [x] Đối chiếu danh mục asset LinkedIn theo bốn locale, gồm source copy, export và format placement; coverage matrix 4 × asset phải tách copy khỏi file đã render/QA.
- [x] Giữ nghiên cứu Lark/Matched/Predictive Audience ngoài scope này; target-account sheet chỉ là schema/metadata cho tới khi có nguồn và quyền rõ.

### B. Strategy, kênh và từ khóa

- [x] Viết định nghĩa ICP và quy tắc FDI/nội địa; đánh dấu ngành lân cận và điều kiện loại trừ.
- [x] Mapping FDI/nội địa vào ba route hiện có và content priorities; không tự đổi 50–60/25–30/15–20 thành spend split.
- [x] LinkedIn FDI và nội địa có objective, audience hypothesis, language, decision maker, message/proof và KPI riêng; không gộp kết quả hai nhóm để suy account coverage.
- [x] Google có VN core, EN/zh-Hans/zh-Hant FDI test theo thị trường và Digiwin brand candidate; từng keyword có intent, locale, route, match type và trạng thái volume/source.
- [x] Negative keyword được phân theo intent và kiểm tra không vô tình loại các cụm MES/ERP/traceability có thể phù hợp.

### C. Ba ngôn ngữ/bốn locale trên ba landing route

- [x] Offline: ba route giữ một HTML/top switch, `lang=vi|en|zh-Hans|zh-Hant`; missing/invalid fallback, switch override, URL parameter preservation và 320px/desktop runtime đã QA trên candidate hợp nhất. Không tạo route URL theo ngôn ngữ.
- [ ] Live/ad-entry: kiểm canonical metadata, persistence policy, exact destination, PopupX/UTM handoff và các URL public sau mandate.
- [ ] Lập glossary `vi/en/zh-Hans/zh-Hant` cho lot, yield, recipe, traceability, audit, WIP, substrate, PCB và proof; reviewer phù hợp kiểm riêng China/Taiwan trước live.
- [x] OSAT: bốn locale cho mọi customer-visible copy, diagram text, CTA, metadata và thông báo tương tác; giữ hai CTA cùng semantic và `osat_cta_click` candidate theo contract; candidate HTML/copy đã kết hợp PageSpeed và qua QA tracking/runtime local; native/live gate còn mở.
- [x] Fabless: bốn locale cho cùng các thành phần, gồm case/claim VI đã duyệt dịch; giữ hai CTA; offline HTML/copy candidate đã qua QA local, không suy là live; không thêm CTA analytics event khi chưa inventory cho phép.
- [x] Supplier/Partner: bốn locale; **chỉ một** header CTA với ID `partner-cta-header`, label VI `Tư Vấn` và bản dịch được review; candidate HTML/copy offline đã qua QA local; không thêm nút cam hay CTA analytics event.
- [x] Cả ba route giữ HTML source provider-free, không thêm form/SDK/callback/analytics dispatch ngoài contract; PopupX/form do LadiPage sở hữu.
- [x] Offline: 3 route × 4 locale × 320px/desktop runtime, localized title/H1/lang, CTA inventory 2/2/1, no JS error/overflow và tracking regression 12/12.
- [ ] Native/production: kiểm glyph, line wrap, keyboard/focus, detail toggles, PopupX, GTM/section events, pagehide và end-to-end UTM/source trên public routes khi được phép.
- [ ] Nếu đồng bộ ba trang LadiPage hiện có, chạy đúng lifecycle `revise_existing_page`: receipt/page match → preflight → bounded semantic patch → save/reopen → publish cùng URL → public/protected invariants → closeout. Publication cần mandate tương ứng; không suy từ Basic import cũ.

### D. LinkedIn asset `vi/en/zh-Hans/zh-Hant`

- [x] Audit coverage matrix bốn locale cho ba static concepts OSAT/Fabless/Partner, OSAT document 6 trang, bốn carousel cards, square và b2b derivatives; 9 static SVG/PNG, 3 PDF sáu trang và 12 carousel PNG candidate/prototype đã render/QA offline; B2B v2 có 9/9 biến thể offline `vi`/`zh-Hans`/`zh-Hant`; không có bản EN B2B mới. Account-format/native review vẫn mở.
- [ ] Mỗi bản ngôn ngữ có headline/body/CTA/alt text hoặc metadata khi format hỗ trợ; bảo toàn nghĩa pain → mechanism → proof; không dịch nguyên văn nếu decision maker khác cần thông điệp khác.
- [x] CAR-03 tiếp tục proof abstract, không thêm customer name/logo. Bảo đã duyệt dịch/dùng case/claim có sẵn trong VI; giữ source, geography, entity, date, metric và scope. Claim mới/rộng hơn và 200+/700+ chỉ có trong carousel English v1 cần quyết định riêng.
- [ ] QA từng export: chữ không cắt, font hiển thị đúng, hierarchy, contrast, mobile preview, file size/dimensions theo active account specification khi có evidence.
- [ ] Đối chiếu quảng cáo từng locale với `lang` trên đúng landing URL và UTM/gclid; không để EN/zh-Hans/zh-Hant dẫn mặc định vào VI hoặc sai script.

### E. KPI, tiền, lịch và workbook

- [ ] Chốt KPI trước chạy: LinkedIn đúng account/function/seniority (trong giới hạn report), reach trong list nếu có list hợp lệ, frequency, CTR/engagement; Search impression share core terms, search-term relevance và engaged sessions; brand baseline; effective lead rate tách raw lead.
- [x] Với mỗi KPI ghi source, numerator/denominator, kỳ đo, baseline hoặc `unknown`, threshold/proposal, minimum data và quy tắc khi report bị ẩn/thiếu.
- [x] Giai đoạn 7 ngày kiểm tra kỹ thuật; đánh giá search terms trên tập quan sát của kỳ với cỡ mẫu/coverage công bố, không dùng `7/10` như kết luận vững khi chỉ có 10 click.
- [x] Ghi trần Bảo chọn: 35 triệu đến Scale 1 qua 56 ngày lịch; historical 1 triệu/ngày cho tối đa 35 ngày paid, không suy 56 triệu. 28+8,75 và 35+8,75 là proposal lịch sử.
- [ ] Thiết kế/duyệt lịch paid days, reserve, thuế/phí, phase allocation và Scale 2 gate; chưa có quyền spend.
- [ ] Ghi cách giữ tiền Search chưa tiêu và điều kiện đề xuất chuyển sang LinkedIn; không mở rộng keyword chỉ để tiêu hết.
- [x] Đã xác định workbook nguồn local và tạo bản 11 sheet (7 sheet nguồn + 4 sheet thêm) với daily metrics, keyword/negative, account/audience schema, KPI dictionary và note 56/35; QA bảo toàn công thức/table nguồn bằng dữ liệu giả. Còn đối chiếu lịch paid thực tế và quyết định thuế/phí; không dùng dữ liệu Lark/lead thật trong public artifact.

### F. Gate cuối

- [x] Review `DOCS_IMPACT_MAP.md`; cập nhật chỉ canonical docs có current truth đổi, giữ HISTORY/LOG nguyên nghĩa lịch sử.
- [x] Offline integration: ma trận route × 4 locale, asset inventory, tracking 12/12, workbook/source preservation và docs contradictions được audit.
- [ ] Live/native/operational: lịch paid days, account format, claim wording, exact ad links/UTM, PopupX và public runtime còn gate riêng.
- [x] Ghi riêng fact, observed evidence, proposal, unknown và terminal status; chỉ PASS khi implementation/artifact và canonical truth khớp.
- [ ] Trước commit, merge, push hoặc hành động live, báo diff/evidence và xin đúng authorization còn thiếu từ Bảo.

## 5. Tài liệu chịu tác động dự kiến

- Strategy/ICP: `Semiconductor_Work_Kickoff.md`, `drafts/S01_Proof_and_Message.md`, `drafts/S03_LinkedIn_Audience_Research.md`, `operations/Pre_Ad_Readiness_Plan.md`.
- Search/LinkedIn: `drafts/S02_Google_Search_Research.md`, `ads/google/Google_Search_Build_Sheet.md`, `ads/linkedin/LinkedIn_Build_Pack.md`, `assets/linkedin/source/` và export đã được duyệt trong `assets/linkedin/final/`.
- Landing/localization: ba canonical HTML dưới `landing/`, `design-system/digiwin-semiconductor-marketing/MASTER.md` và page overrides, `tracking/Semiconductor_Tracking_Contract.md`, `operations/LadiPage_Draft_Runbook.md`.
- Measurement/budget/status: `drafts/S04_Measurement_and_Budget.md`, `drafts/S04A_Management_Budget_Scenarios.md`, `drafts/S04B_Executive_Budget_Recommendation.md`, `CURRENT_STATE.md`, `README.md` và đúng workbook khi xác định được.

**Phạm vi tại lúc lập plan ban đầu:** chưa thay đổi các file trên, asset HTML/PNG/PDF hay workbook. Các slice offline sau checkpoint đã tạo candidate local như trạng thái đầu file; public LadiPage, GTM/GA4, Campaign Manager và Google Ads không được thay đổi theo plan này.
