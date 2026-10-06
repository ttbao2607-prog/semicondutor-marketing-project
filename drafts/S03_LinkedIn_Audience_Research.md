> **Main integration · 2026-10-06 — adapter DEVELOPING / NOT_FROZEN.** Bảo chỉ cho tích hợp checkpoint `ffb4fba` (anchor/gate và adapter draft) vào main local; adapter còn developing, chưa freeze/adopt/release. Core ImageGen frozen giữ nguyên scope riêng. [Phạm vi tích hợp và dependency](../operations/linkedin-locale-adapter/Main_Integration_2026-10-06.md): không đưa ảnh/viewer/input journey VI cũ lên main; full-journey dogfood, native EN/Chinese QA và creative acceptance còn pending. Các receipt/source-only status bên dưới giữ phạm vi checkpoint cũ, không chứng minh input/asset hiện có trên main. Không push/live.

> **Message anchor · 2026-10-06 — MSG-ANCHOR-01 bắt buộc.** Email gốc đã được Bảo cung cấp trực tiếp trong phiên; [anchor nội dung VN / FDI EN–Chinese](../operations/Vy_Email_Content_Anchor.md) tách định hướng audience/persona/message khỏi đề xuất vận hành và phần đã superseded. FDI tập trung business value/ROI có căn cứ; VN là ERP hỗ trợ chuẩn bị năng lực vào chuỗi. Phải đối chiếu anchor revision/SHA256 trước generation và hậu kiểm từng artifact/surface + toàn journey. FAIL → CHANGES_REQUIRED; thiếu review/binding/evidence → INSUFFICIENT_EVIDENCE; đều chặn SCRIPT_REVIEW_PASS và ready/accepted handoff. Core harness, artwork và receipt cũ giữ nguyên; không PASS hồi tố. Những ghi nhận email gốc chưa có và budget/schedule/proposal cũ bên dưới giữ nghĩa lịch sử, không thay trạng thái hiện hành. Bảo đã yêu cầu commit checkpoint local trên nhánh hiện tại; containing commit lưu anchor/gate và adapter draft. Không merge main/push/live; các ghi nhận chưa commit bên dưới là snapshot chuẩn bị.

> **PO pivot VI → English · 2026-10-06 — VI_DOMESTIC_CHANGES_REQUIRED / EN_ADAPTATION_DEFERRED.** Bảo xác nhận bộ VI hiện tại sai hướng cho tệp nội địa và cần build lại: ERP bán dẫn là cầu nối về năng lực quản trị để doanh nghiệp chuẩn bị tham gia chuỗi cung ứng bán dẫn. Không hứa mua ERP là đạt chuẩn, vượt audit hoặc có đơn hàng. Giữ skeleton, hình/demo và receipt hiện có làm nguồn cho chuyển chuỗi asset sang English ở task sau; hiện chưa dịch/adapt/generate EN, chưa có EN acceptance.

> [Quyết định và handoff pivot](../operations/LinkedIn_VI_EN_Message_Pivot_2026-10-06.md) là trạng thái hiện hành về audience/message, bao gồm 11 carousel/55 card, 4 bộ case/16 card và demo journey 3 luồng. Các ghi nhận PASS/READY bên dưới giữ phạm vi revision cũ và kỹ thuật, không chứng minh bộ hiện tại phù hợp cho VI nội địa hoặc đã sẵn sàng EN. Format Single image cold → Carousel RMK và trần media 11,7 triệu giữ nguyên; task này chỉ đồng bộ tài liệu và commit local, không đổi asset, audience, account hoặc live.

> **PO checkpoint / main integration · 2026-10-05:** Bảo chốt Phase 1 gần như **cold Brand awareness + Carousel image**. Concept RMK theo sau: exact campaign/new-ad source → audience tương tác trong window được chọn → RMK objective Engagement hoặc click LDP; concept hợp lý đã ghi nhận, chưa phải verified native Carousel-source capability hay exact RMK objective release. Không yêu cầu warm pool có sẵn cho Phase 1; RMK mechanics/source eligibility deferred tới preparation trước Phase 2. Research đã ở worktree này; PO yêu cầu commit local và merge vào main local, không push/live. [Artifact index](../operations/LinkedIn_Report_Artifact_Index_2026-10-05.md).

> **PO scope / Carousel verification · 2026-10-05:** Giữ **new cold Brand awareness + Carousel image → RMK chính new-ad cohort sau đó**; không lấy existing Digiwin Page pool. Awareness có Carousel (PO screenshot/UI), **Engagement cũng có Carousel** (selected native UI/screenshot); official guidance thêm Website visits, Website conversions, Lead generation. Format compatibility không phải native RMK source eligibility; đổi objective chưa giải quyết Carousel-source gap. Bảo không chọn Document; không đổi objective/creative. Trước delivery chưa có warm pool là expected, không phải blocker cold launch. Source CSV 424 rows chỉ name/country/city; private full review worksheet + source registry/measurement/gate templates đã chuẩn bị, identity/cleaned reach OPEN. [Current evidence/data plan](../operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md).

> **Decision evidence round 2 · 2026-10-05:** Đã thu đủ 117 mapping: triage tên 34 consistent candidates / 8 ambiguous / 75 name-inconsistent cần review, chưa xác minh entity/ICP và không phải tỷ lệ match sai. Input Domain/Page URL đều trống ở 117 displayed rows; industry filter không thay identity cleanup. Company Page source visitors **29/30d, 101/90d, 317/365d**; CTA clicks **0/365d**. Website editor hiển thị domain thử nghiệm; chưa có production RMK pool được chứng minh. Giữ creative, ưu tiên sạch input + production tracking; chưa immediate RMK/budget/split approval. 10 ảnh mới + queue private local; không persistent UI mutation mới. Round2 docs lưu bằng containing local checkpoint theo mandate commit của Bảo; prior `764545b` local only. [Decision pack](../operations/LinkedIn_Audience_Decision_Evidence_2026-10-05.md).

> **Research live UI · 2026-10-05:** Exact Company List Ready/80%; Details và refreshed list có **753,731 members**, 117 Companies, tab Unmatched 86. VN + English profile + Engineering/Operations/IT/QA = **4,800+**; thêm Manager/Director/VP/CXO = **780** ở saved definition `RSCH-CL-VN-LEAD-20261005` (persistence verified). Cùng filters + Vietnamese profile báo too small. Size gate discovery đã xác minh; mapping quality/denominator và production decisions vẫn OPEN. Retargeting menu không có Carousel riêng; warm RMK chưa đủ evidence. Chỉ lưu Saved Audience; Exit without saving ad set, không publish/enable/spend. [Receipt](../operations/LinkedIn_Audience_Ready_Research_2026-10-05.md). Snapshot cropped-size phía dưới là lịch sử trước research.

> **Company List Ready · 2026-10-05:** Bảo xác nhận đúng `TEST-AUD-COMPANY-LIST-DISCOVERY-202610`; ảnh cung cấp hiển thị **Ready / match rate 80% / Company List / Owned**, Active ad sets `-`. Exact audience count bị cắt nên chưa xác minh reachable size hoặc gán `AUD_STATUS_READY_VIABLE`. Điều kiện chờ Building của đúng tệp này đã gỡ; engagement RMK `LI-AUD-P1-ENGAGED-30D`, targeting/filtered reach, attachment, budget và live vẫn có gate riêng. Các snapshot Building ngày 2026-09-30 bên dưới là lịch sử, được thay thế cho current Company List status bởi [evidence và bảng task](../operations/LinkedIn_Company_List_Ready_Update_2026-10-05.md).

# S03 — LinkedIn audience research

**E3 Quality VI drafts r3 (2026-10-01):** Bảo selected Quality/Process, O1 versus O4-Q, same-problem storytelling test, VI-first review, no baseline C. Two five-card copy/storyboard drafts are complete in operations/linkedin-awareness-execution/ad-records-vi.md and storyboards-vi.md. Parent STRUCTURAL/CONTRACT inspection supports READY_FOR_PO_COPY_REVIEW; r3 keeps the consultant perspective and repairs whole-chain continuity; caption counts 136/130 and all native headlines <=45. Captions/card 1/shared card 5 and matching storyboard/alt were refined at the request of Bảo; cards 2–4 remain unchanged. Card 5 synthesizes records/context/owner before separately attributed Taiwan ERP/MES context. All four transitions per narrative have been inspected at copy/storyboard level, not rendered or buyer-validated. Visual/native/buyer/product/account validation remains open; no final images or live activity. This dated update supersedes earlier selection/format-pending statements for this wave. New drafts and closeout edits are local working-tree files, not a new commit or GitHub push.

**Status:** authorized external validation completed on 2026-09-14; this public-repository record is sanitized. No audience was uploaded, no ad was added, no campaign delivered, and no spend occurred in that validation.
**Phase status:** Research Phase 1 is complete and canonicalized by commit `dbb5ff1` (`Record sanitized LinkedIn validation handoff`). Phase 2 production mapping/eligibility and live-object readiness remain separate and are not delivery evidence. A separate 2026-09-30 mandate covers one sanitized 424-row Company List discovery audience. Campaign Manager confirmed its creation; PO-provided evidence on 2026-10-05 shows `Ready` and Match rate `80%`; live research on 2026-10-05 then verified 753,731 members and filtered English leadership reach 780. Mapping identity/ICP remain unverified; round2 Company Page 30-day source has 29 visitors, not a verified RMK audience. This does not authorize production audience use, campaign attachment, or delivery.
**Owner:** Executor in this batch  
**Objective:** define a public-source account-universe methodology and role hypotheses while separating candidate identity, externally observed configuration evidence, and verified Campaign Manager delivery evidence.

## Source boundary

- Local: kickoff §§4, 7, 8; source brief “Thực tế VN”, “Thông điệp theo nhóm đối tượng” and “Digital Ads — Bảo”.
- Public official: LinkedIn Matched Audiences overview, https://www.linkedin.com/help/linkedin/answer/a420552/matched-audiences (accessed 2026-09-11); LinkedIn match-rate guidance, https://www.linkedin.com/help/linkedin/answer/a420595/matched-audiences-match-rates (accessed 2026-09-11); company/contact targeting overview, https://www.linkedin.com/help/linkedin/answer/a424397/linkedin-account-and-contact-targeting-overview (accessed 2026-09-11).
- Public official guidance indicates company/contact targeting and member-provided profile layers exist, and audience size/match rate are account/UI outputs. An authorized external read-only validation was completed on 2026-09-14. Raw account, audience, list and screenshot evidence is intentionally retained outside this public repository.

## Fact / proposal / unknown

**Facts:** LinkedIn awareness is planned; OSAT/factory is priority; role/account targeting must be evidenced rather than inferred from aggregate reach. The external validation observed that Company Names, geography and role facets can be configured; it did not establish delivery or commercial outcomes.

**Proposal:** retain a quality-first company universe and use the observed configuration as a production hypothesis only after human review of unresolved entity mappings. Keep Company Names and Job Functions in separate AND groups; do not treat aggregate estimates as account-role delivery proof.

**Unknown:** approval of unresolved parent-level entity mappings, final production audience definition, consent/eligibility, account-reporting granularity, and actual delivery.

**Current UI note:** external validation was limited to non-delivering draft/off configuration. The public record does not retain raw account or audience data. No upload, creative attachment, launch or spend is claimed.

Production handoff: `../ads/linkedin/LinkedIn_Build_Pack.md`.

## Candidate account-universe methodology

| Tier | Provenance | Candidate examples | Status / rule |
|---|---|---|---|
| A — named local lead | Source brief names OSAT/factory, fabless and supplier/SI categories | No account list asserted | Category only; needs Vietnam company universe |
| B — local-brief lead | The local brief names semiconductor cases/companies; no verified account list is present | Not populated in this draft | Names are research leads only, not confirmed target accounts, customers or current legal identities |
| C — public Vietnamese ecosystem | Government/industry sources may identify companies and associations | Not populated in this draft | Add only with URL, date, entity identity and relevance rationale |

No personal names, emails, scraped contacts or PII are included.

## Role / function / seniority hypotheses

| Segment | Function hypotheses | Seniority hypotheses | Exclusions / caution |
|---|---|---|---|
| OSAT / factory | Operations, manufacturing, quality, process engineering, supply chain, finance/controlling, IT/MES | Manager, head/director, VP/executive where available | Do not equate job title with decision authority; validate language and local taxonomy |
| Fabless commercialization | Operations, planning, supply chain, R&D/program, finance, product/operations leadership | Manager/director/VP | Avoid broad chip-design audiences unrelated to commercial operations |
| Supplier/SI/automation | Solution engineering, industrial automation, ERP/MES/OT, partner/channel, quality | Manager/director/partner leadership | Separate partner objective from end-user awareness |

## Objective / format hypotheses

- Primary hypothesis: LinkedIn awareness using pain → mechanism → safe proof direction, subject to account and format availability.
- Candidate formats: single-image or document/carousel-style professional explanation if the authorized account supports it; format is not a required deliverable.
- Retargeting is conditional on an eligible, consent-compatible audience source; do not assume website visitors or engagement audiences exist.

## UI validation plan

1. Obtain human sign-off for the remaining parent-level or otherwise unresolved entity mappings before any production audience decision.
2. Keep Company Names and Job Functions in separate AND groups. Do not use an OR grouping to infer account-role targeting.
3. Keep production audiences uncreated. The only current exception is the separate 2026-09-30 sanitized Company List discovery audience described above; keep it unattached pending separate production-use authorization; retain observed Ready/80% without inferring exact size, filtered reach or delivery eligibility.
4. Re-check audience estimate, delivery eligibility and expansion settings at the moment a production draft is explicitly authorized; external validation is not delivery evidence.
5. Record objective, format, placement, consent/eligibility and reporting constraints as observed or unknown. Do not infer account × role intersection from marginal reports.

## Acceptance, dependencies and stop

**Acceptance:** provenance-bearing public candidate methodology; no PII; role hypotheses and exclusions; sanitized external-validation boundary; explicit production gate.
**Dependencies:** S01 message map; human sign-off on unresolved entity mappings; S04 measurement and a separate operational mandate.
**Stop:** no additional upload, no production audience use, no campaign build, no message/invitation, no public commit of raw account/audience data, and no claim of match rate/size/reach/delivery beyond retained evidence. The discovery audience shows Ready/80% in PO-provided evidence; Active ad sets displays `-`, and production use remains unauthorized.
