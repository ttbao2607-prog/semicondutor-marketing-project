> **Main integration · 2026-10-06 — adapter DEVELOPING / NOT_FROZEN.** Bảo chỉ cho tích hợp checkpoint `ffb4fba` (anchor/gate và adapter draft) vào main local; adapter còn developing, chưa freeze/adopt/release. Core ImageGen frozen giữ nguyên scope riêng. [Phạm vi tích hợp và dependency](../operations/linkedin-locale-adapter/Main_Integration_2026-10-06.md): không đưa ảnh/viewer/input journey VI cũ lên main; full-journey dogfood, native EN/Chinese QA và creative acceptance còn pending. Các receipt/source-only status bên dưới giữ phạm vi checkpoint cũ, không chứng minh input/asset hiện có trên main. Không push/live.

> **Message anchor · 2026-10-06 — MSG-ANCHOR-01 bắt buộc.** Email gốc đã được Bảo cung cấp trực tiếp trong phiên; [anchor nội dung VN / FDI EN–Chinese](../operations/Vy_Email_Content_Anchor.md) tách định hướng audience/persona/message khỏi đề xuất vận hành và phần đã superseded. FDI tập trung business value/ROI có căn cứ; VN là ERP hỗ trợ chuẩn bị năng lực vào chuỗi. Phải đối chiếu anchor revision/SHA256 trước generation và hậu kiểm từng artifact/surface + toàn journey. FAIL → CHANGES_REQUIRED; thiếu review/binding/evidence → INSUFFICIENT_EVIDENCE; đều chặn SCRIPT_REVIEW_PASS và ready/accepted handoff. Core harness, artwork và receipt cũ giữ nguyên; không PASS hồi tố. Những ghi nhận email gốc chưa có và budget/schedule/proposal cũ bên dưới giữ nghĩa lịch sử, không thay trạng thái hiện hành. Bảo đã yêu cầu commit checkpoint local trên nhánh hiện tại; containing commit lưu anchor/gate và adapter draft. Không merge main/push/live; các ghi nhận chưa commit bên dưới là snapshot chuẩn bị.

> **PO pivot VI → English · 2026-10-06 — VI_DOMESTIC_CHANGES_REQUIRED / EN_ADAPTATION_DEFERRED.** Bảo xác nhận bộ VI hiện tại sai hướng cho tệp nội địa và cần build lại: ERP bán dẫn là cầu nối về năng lực quản trị để doanh nghiệp chuẩn bị tham gia chuỗi cung ứng bán dẫn. Không hứa mua ERP là đạt chuẩn, vượt audit hoặc có đơn hàng. Giữ skeleton, hình/demo và receipt hiện có làm nguồn cho chuyển chuỗi asset sang English ở task sau; hiện chưa dịch/adapt/generate EN, chưa có EN acceptance.

> [Quyết định và handoff pivot](../operations/LinkedIn_VI_EN_Message_Pivot_2026-10-06.md) là trạng thái hiện hành về audience/message, bao gồm 11 carousel/55 card, 4 bộ case/16 card và demo journey 3 luồng. Các ghi nhận PASS/READY bên dưới giữ phạm vi revision cũ và kỹ thuật, không chứng minh bộ hiện tại phù hợp cho VI nội địa hoặc đã sẵn sàng EN. Format Single image cold → Carousel RMK và trần media 11,7 triệu giữ nguyên; task này chỉ đồng bộ tài liệu và commit local, không đổi asset, audience, account hoặc live.

# S01 — Proof & message

**Status:** draft only; no live validation  
**Owner:** Executor in this batch  
**Objective:** create a safe claims register and message map for one possible OSAT-first route, while keeping unverified case names, numbers and usage rights out of live copy.

## Source boundary

- Local: `Semiconductor_Work_Kickoff.md` v2.0, sections 1, 4, 5; `Semiconductor - Website & Ads.md`, sections “Nguồn gốc và hệ thông điệp” and “Digital Ads — Bảo”.
- Public read-only: Digiwin industry overview PDF, https://www.digiwin.com/digiwin2023/img/top4_16.pdf (accessed 2026-09-11). It is a general company/industry-overview lead only; it does not corroborate the named cases below and does not establish current entity scope, permission to reuse, metric definitions or Vietnam applicability.

## Fact / proposal / unknown

**Facts from the local brief:** OSAT is the paid priority; pains include 4M1E, test data, lot, traceability, audit, WIP and cost close. Fabless and supplier/SI are secondary message branches. The brief explicitly says listed cases and claims need verification.

**Proposal:** first safe route is mechanism-only: “connect operational data across lot/test/quality/cost so teams can investigate traceability and close the operational loop,” with no customer result, percentage, customer name or “100+/200+” claim.

**Unknown:** proof permission, exact entity, geography, date, baseline, unit, implementation scope, source excerpt/page ownership, current product capability and final CTA/route.

## Provisional ICP and account-source framework — S1 draft, 2026-09-29

This section translates the Vy email revision plan into **proposals for Bảo's D1 decision**, not an approved target-account definition. The local kickoff establishes the three business routes and their priority bands. It does not establish an FDI/domestic split, a list of target companies, or a rule excluding conglomerates. Bảo directly observed in this session that the Lark pipeline appears to contain mostly other industries and very limited semiconductor presence; the underlying dataset is unavailable here, so its contents and counts remain unverified. This observation is context for the proposed research boundary, not an approved account decision.

**Candidate inclusion test.** A company belongs in a research universe only when a dated, attributable source establishes (1) its specific semiconductor-supply-chain activity, (2) its relevant Vietnam operating or decision footprint, and (3) a plausible operational pain aligned to one of the three paid routes. A company can be a research candidate without being a verified target account or Digiwin customer. Adjacent electronics manufacturing, generic software distribution, broad industrial automation and investment-only entities require specific semiconductor relevance before inclusion. Job title, ownership origin, company size and language alone are insufficient.

**Two independent axes.** Assign the business route from the evidenced activity and pain: OSAT/factory; commercially operating IC design/Fabless; or Supplier/SI/automation/materials-equipment with a relevant integration or partner problem. Assign `FDI`, `domestic`, or `unknown` separately from evidence of the relevant Vietnam entity's ownership/control and operating context; do not infer it from brand, language, headquarters, or contact nationality. A mixed group or subsidiary stays `unknown` until the entity and decision unit are resolved. Multiple activities may create multiple route hypotheses, but the research register must identify a primary route before building an audience. The kickoff's 50–60% OSAT, 25–30% Fabless and 15–20% Supplier/Partner bands remain content-priority guidance, **not** FDI/domestic shares, account counts, spend shares or delivery targets.

| Provisional axis | OSAT / factory | Fabless commercialization | Supplier / Partner |
|---|---|---|---|
| FDI | Candidate Vietnam operating entity with evidenced packaging, test or factory operations; investigate lot/test/quality/WIP pain. | Candidate Vietnam decision or operating unit with evidenced outsourced production/commercial operations; investigate outsource WIP and forecast visibility. | Candidate Vietnam supplier or integration unit serving a verified semiconductor workflow; investigate ERP–MES–OT handoff and partner fit. |
| Domestic | Candidate locally controlled operating entity with evidenced packaging, test or factory activity; use the same pain test without assuming scale. | Candidate locally controlled commercial IC-design entity with evidenced outsourced operations; exclude design-only research without relevant operating pain. | Candidate locally controlled supplier/SI with evidenced semiconductor customer workflow; distinguish end-user need from partner objective. |

These cells are **research hypotheses**, not six approved audiences. FDI/domestic can inform source discovery and message adaptation after D1, but does not change the three route identities or prove platform targeting/eligibility. A conglomerate with a shared system is neither automatically included nor excluded: first identify the legal operating entity, whether semiconductor operations have their own decision unit and pain, and whether a shared system already addresses that pain. Bảo must decide the exclusion rule and whether such an entity is addressable before it enters a production audience.

### Account-source status register (no account list)

| Source class | Present evidence | Status | Permitted use / promotion gate |
|---|---|---|---|
| Kickoff v2.0 and local source brief | Three route categories, priority bands and pain vocabulary; case names are unverified leads | `verified` for brief provenance and route intent only; `unknown` for account identity, current customer relationship and rights | Define research criteria and message hypotheses; cannot promote a named case to target/customer/proof without entity, date, activity, scope and usage-right review. |
| S03 sanitized LinkedIn research | Company/role configuration was externally observed; raw account/audience evidence is outside this public repository | `verified` for the recorded UI observation only; `unknown` for specific company match, account-role delivery and production eligibility | Inform later platform feasibility; cannot establish any account's ICP fit or delivery. |
| Public ecosystem or company-controlled source to be collected | No account-specific source entered in this S1 draft | `candidate` source class; individual accounts remain `unknown` | Add a research record only with URL/title, publisher, observation date, exact legal entity, Vietnam footprint, semiconductor activity, route rationale and FDI/domestic evidence; verify independently before targeting or public claim. |
| Vy email propositions and Bảo's direct session observation | Revision plan records D1 questions. Bảo observed that the Lark pipeline appears mostly other industries with very limited semiconductor presence; dataset access and account evidence are unavailable here. | `candidate` proposal; observation provenance confirmed, underlying dataset and D1 decision `unknown` | Ask Bảo to settle D1; do not derive a customer list, exclusion, ownership fact or quantitative share from the observation. |

**D1 decision status (Proposal pending Bảo's explicit sign-off).** Dựa trên định hướng của Sếp Vy, nhóm chiến lược đề xuất phương án (proposal) về ICP, danh sách loại trừ và thông điệp nội địa như sau để Bảo xem xét và phê duyệt:

### Đề xuất phương án D1 — Quy tắc loại trừ tập đoàn lớn & Phân khúc nội địa (Chờ Bảo duyệt)

1. **Đề xuất loại trừ tập đoàn lớn (Proposed Excluded Companies):**
   - **Danh sách đề xuất loại trừ:** `Intel`, `Samsung Electronics`, `Hana Micron`, `Amkor Technology`.
   - **Căn cứ đề xuất:** Các tập đoàn FDI Tier-1 này thường vận hành trên hệ thống ERP/MES toàn cầu của tập đoàn mẹ, khó là khách hàng khả thi cho Digiwin tại Việt Nam.
   - **Trạng thái:** `proposal / unconfirmed`. Cần quyết định chính thức từ Bảo trước khi cấu hình cứng vào tài khoản live hoặc loại trừ khỏi audience.

2. **Đề xuất định vị tập trung vào Chuỗi cung ứng & Công nghiệp phụ trợ bán dẫn:**
   - Trọng tâm tiếp cận đề xuất:
     + Sản xuất mạch in (PCB) và đế bán dẫn (Substrate).
     + Vật liệu bán dẫn & đóng gói (Packaging materials, khuôn dập, hóa chất).
     + Linh kiện điện tử & cụm lắp ráp chuyên dụng.
     + Gia công cơ khí chính xác cho thiết bị và linh kiện bán dẫn (Precision machining / tooling).

3. **Đề xuất thông điệp cho Phân khúc Nội địa (Domestic Segment Messaging Proposal):**
   - **Thông điệp cốt lõi:** *"Đủ chuẩn tham gia vào chuỗi cung ứng bán dẫn"* — giải quyết trực tiếp rào cản lớn nhất của các nhà máy sản xuất linh kiện, phụ trợ Việt Nam khi muốn trở thành vendor/supplier cho các tập đoàn bán dẫn toàn cầu.
   - **Hai biến thể Headline chính thức (Official Headline Variants):**
     * **Biến thể 1:** *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"* — Trực diện, khẳng định năng lực đáp ứng chuẩn vendor quốc tế.
     * **Biến thể 2:** *"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"* — Nhấn mạnh vào giải pháp chuẩn hóa quy trình sản xuất, số hóa quản trị để vượt qua các kỳ audit khắt khe.
   - **Yêu cầu audit từ khách hàng tập đoàn (Corporate Customer Audit Requirements):**
     * **Truy xuất lot (Lot Traceability):** Số hóa phả hệ lot (genealogy), phân tách/gộp lot (lot split/merge), liên kết chặt chẽ nguyên vật liệu, thiết bị, thông số 4M1E xuyên suốt quy trình sản xuất.
     * **Kiểm soát yield & chất lượng (Yield & Quality Control):** Quản lý dữ liệu kiểm thử (test data) thời gian thực, giám sát SPC liên tục, cảnh báo biến động yield và chặn lỗi ngay tại nguồn.
     * **Quản lý recipe (Recipe Management):** Khóa tham số công thức sản xuất, ngăn chặn rủi ro sai sót thao tác thủ công từ công nhân, đảm bảo tính nhất quán tuyệt đối giữa các mẻ hàng.
     * **Đáp ứng audit tiêu chuẩn & khách hàng tập đoàn (Standard & Tier-1 Audit Compliance):** Minh bạch hồ sơ điện tử, trích xuất báo cáo audit nhanh chóng trong vài phút, chứng minh độ tin cậy vận hành chuẩn mực khi đón đoàn chuyên gia đánh giá từ các tập đoàn toàn cầu.

## Claims register

| ID | Draft wording / use | Source | Entity / segment | Scope / metric | Limitation | Usage-right status | Verification | Route |
|---|---|---|---|---|---|---|---|---|
| S01-C01 | **Safe mechanism draft:** “Map lot, test, quality and cost data into a traceable operating flow.” | Kickoff §4.2–4.3; source brief message house | Digiwin capability / OSAT | No outcome or number asserted | Must be narrowed to actual offer and route | Unknown; internal draft only | Partially grounded as message direction, not product proof | OSAT candidate |
| S01-C02 | “Bright Power / SCI / Spectron / Lai Jie” | Local brief only; PDF is not corroboration | Named customer/case / Fabless | No metric supplied in verified evidence | Entity, case details, date and permission unresolved | Unknown; do not publish | Unverified lead | Fabless research only |
| S01-C03 | “Baiwei / Zhonghuan / Sanan / Qunfeng” | Local brief only; PDF is not corroboration | Named customer/case / OSAT | No metric supplied in verified evidence | Exact legal entity, scope and case permission unresolved | Unknown; do not publish | Unverified lead | OSAT research only |
| S01-C04 | “200+ IC design” | Local brief | Market/customer count claim | Number has no independent source, date or denominator in workspace | Could be global, historical or differently defined | Unknown; do not publish | Unverified | None until sourced |
| S01-C05 | “100+ semiconductor MES experience” | Local brief | Experience claim | No source excerpt, denominator or period in workspace | Needs owner-approved proof and scope | Unknown; do not publish | Unverified | None until sourced |
| S01-C06 | “Vietnam has about 7,000 chip-design engineers; 2030 targets include 100 design companies, one small fab and 10 packaging/testing plants.” | Source brief links Government Decision 1018/QĐ-TTg | Vietnam market context | Public policy/context claim, not ad proof | Must be checked against the primary decision and intended wording; not a Digiwin outcome | Public source lead; rights/advertising suitability unknown | Not independently transcribed here | Context only |

## Message map

| Segment | Primary pain | Mechanism hypothesis | Safe proof level now | CTA hypothesis |
|---|---|---|---|---|
| OSAT / factories | Split/merge lot, test data, 4M1E, traceability, audit and cost close are disconnected | Join lot–test–quality–WIP–cost records so an operating question can be traced to responsible data and action | Mechanism-only; no customer result | Review an operating pain / discuss a specific traceability or cost-close problem |
| Fabless commercialization | Outsource WIP, Datecode/BIN/lot, forecast and cost are disconnected | Link outsourced WIP and product/lot data to planning and cost visibility | Mechanism-only; named cases remain leads | Discuss outsourced-WIP visibility |
| Supplier / SI / automation / materials-equipment | ERP–MES–OT, quality, traceability and partner boundaries are unclear | Define integration ownership and data handoffs across ERP/MES/OT | Architecture hypothesis only | Partner/integration discussion |
| Phân khúc Nội địa (Domestic Supporting Industries - PCB, Substrate, Vật liệu, Cơ khí chính xác) | Không đáp ứng được các tiêu chuẩn audit khắt khe của khách hàng tập đoàn toàn cầu (truy xuất lot, recipe, yield, chất lượng) để tham gia chuỗi cung ứng | Chuẩn hóa quy trình vận hành và dữ liệu sản xuất (truy xuất lot, SPC yield, quản lý recipe) giúp nhà máy nội địa đủ chuẩn tham gia chuỗi cung ứng bán dẫn | Cơ chế vận hành & chuẩn hóa dữ liệu audit (Mechanism-only; không cam kết khống kết quả) | Headline: *"Đủ chuẩn tham gia chuỗi cung ứng bán dẫn"* / *"Chuẩn hóa vận hành để tham gia chuỗi cung ứng bán dẫn"*. CTA: Khảo sát hiện trạng vận hành / Đánh giá mức độ sẵn sàng audit chuỗi cung ứng |

## Review checklist and handoff

- Every live candidate claim needs source excerpt/page, entity, segment, scope, metric/unit/baseline where applicable, limitation, usage-right decision and verification owner.
- Final creative must use only verified proof or the mechanism-only route; no placeholder, invented result or unverified customer name.
- Handoff to S02/S03: use the message map as hypothesis, not as verified capability.
- Handoff to S05/S06: do not finalize CTA or landing proof block until route, proof rights and scope are resolved.

## Stop conditions

Stop claim expansion when a source is secondary, entity scope is unclear, rights are unknown, or a number lacks baseline/unit/date. No public-source name is a live customer endorsement. No external contact or permission request is made in this batch.

## Public source log

1. Digiwin, “专注制造业数字化” PDF: https://www.digiwin.com/digiwin2023/img/top4_16.pdf — accessed 2026-09-11; public company/industry overview material, not corroboration for named cases and not evidence of usage rights.
