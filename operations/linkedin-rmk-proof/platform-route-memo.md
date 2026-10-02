# LinkedIn RMK source và format memo

Research 2026-10-02; sources official, no Campaign Manager observation. Tài liệu xác nhận platform feature; không xác nhận account availability, tạo audience, reach hoặc delivery.

## Audience source

[Retargeting overview](https://www.linkedin.com/help/lms/answer/a427551/retargeting-overview?lang=en-us) documents single-image and document sources, each with 30–365-day windows, and a minimum 300 matched member accounts for targeting. Website source requires Insight Tag. Engagement totals do not equal matched unique members. Account status/targeting size still requires UI evidence. Canonical 30D is a planned window, not verified buying cycle.

[Single-image audience guide](https://www.linkedin.com/help/lms/answer/a713230) specifies any interaction versus chargeable clicks, 30/60/90/180/365 days, and ad sets with performance metrics. These signals are not buying-intent labels. Note: Public_Source_Register's older “Audience guidance” URL a713230 now resolves to this source-specific guide; don't treat it as general ICP validation.

| Route | Source vs receiving format | Research conclusion / gate |
|---|---|---|
| Native single-image engagement | Eligible single-image ad set engagement → chosen supported RMK format | Documented source; account objects/data unknown. May seed a pool only after production/live mandate; no inference that historical carousel qualifies. |
| Native document engagement | Document interactions/download/chargeable clicks → chosen RMK format | Documented source; verify separate audience config and combination/overlap in UI later. `single-image/document` planning shorthand doesn't prove one combined audience exists. |
| Carousel images | Image carousel receiver/creative is supported; direct source category not in overview or single-image guide | `DOCUMENTED_SOURCE_GAP`: no verified direct pool of carousel swipers. Do not claim absolute impossibility; hold dependency until official/account evidence identifies a route. Carousel creative can still be served to an eligible audience from another source. |
| Company Page | Page visit/header CTA signal, not “everyone who engaged with our carousel” | Different, broader source with possible organic traffic; eligibility/ICP/permission review needed. Not silently substituted. |
| Website | Tagged page visitors, potentially routed from ad click | Separate Insight Tag/consent/measurement mandate; prior firing isn't evidence of audience or conversion readiness. No tag change now. |
| Company List | Account prospecting/source list | Does not establish person-level engagement or warm intent. Discovery Building isn't RMK readiness. |

Changing the lookback window to grow size is a future proposal; it does not identify actual consideration period and is not done here. No new source collection/CAPI/CRM integration or audience upload proposed as default.

## Receiving creative and objective

[Carousel help](https://www.linkedin.com/help/linkedin/answer/a423087) documents image carousel objectives including awareness, visits, engagement and conversion/lead options. Working creative requirement: 2–10 cards, recommended 1080-square, images scaled to 312-square. Account placement/export review remains necessary. Format compatibility is not source-audience compatibility.

[Document overview](https://www.linkedin.com/help/lms/answer/a737898) supports native case reading/download; [specs](https://www.linkedin.com/help/lms/answer/a493903/document-ads-advertising-specifications?lang=en) set 100 MB/300-page limits, consistent page size and flattened PDF, plus reader hyperlinks only after download. [Best practices](https://www.linkedin.com/help/lms/answer/a726534) advises short, readable content and avoiding apparently clickable in-player CTAs.

Research proposal: a short ungated case document for native learning, or a case carousel if PO keeps image format. Engagement objective is an option for document attention, not approved objective replacement for canonical Brand Awareness. Website Visits with a single image/case landing is another option for evaluation; requires PO destination/measurement choice. No Lead Gen Form release, no gated case offer assumed. Feed-native content shouldn't promise an in-reader clickable consultation button.

## Pre-live account evidence target (not executed)

One authorized controller must identify exact account/Page permissions, source ad sets/formats and performance window, actual audience status/unique count, reachable size after targeting restrictions, overlap/exclusion/locale/placements and destination. Reconcile the two-campaign vs three-segment-ad-set proposals, allocation and source ownership before object build. Existing Building documentation remains historical recorded status, account state unknown. No native delivery data gathered or exported in this research.

## Reconfirmation and implementation gates (2026-10-02)

Bảo correctly recalled image carousel with Brand awareness. Official objective page explicitly includes Carousel image; this does not require conversion/click-through objective. Source eligibility remains a separate unresolved question. Future implementation must read [handoff](implementation-handoff.md) and execute applicable [manifest gates G1–G5](implementation-manifest.json) within a separately authorized route.
