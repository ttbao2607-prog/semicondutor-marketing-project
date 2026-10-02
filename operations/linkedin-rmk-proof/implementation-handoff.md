# LinkedIn platform confirmation and implementation handoff

2026-10-02 · Owner: Codex · Internal documentation only. Bảo requested durable source/gate manifest, local checkpoint and a continuity-map plan. Account observation, creative production and live execution are not released.

## Confirmed versus unresolved

- **CONFIRMED_DOCUMENTED:** Carousel Image Ads still support **Brand awareness**. Keep the cold carousel awareness decision; no requirement to change to Website Visits, conversions or Document Ads. Brand awareness optimizes reach/impressions according to format and bidding. See LI01–LI02 in [implementation manifest](implementation-manifest.json).
- **DOCUMENTED_SOURCE_GAP:** Supported creative/objective does not prove that viewers/swipers/engagers of that carousel can form a native RMK source. Official overview lists single image, document and video among sources, but not carousel images. This is a documentation gap, not proof of platform-wide impossibility. Do not silently treat image carousel as single image or PDF/document.
- **CONFIRMED_DOCUMENTED:** Single-image source supports any interaction or chargeable clicks, not mere impressions. Video source uses 25/50/75/97% views; document uses interaction/download/chargeable clicks. Signals do not establish buying intent or full content reading.
- **ARCHITECTURE_PROPOSAL:** Use separate cold and RMK ad sets when they need different targeting. Targeting is at ad-set level; adding a proof creative to the cold ad set does not create a separate warm audience. Campaign grouping/objective compatibility must be reconciled in the actual account, not assumed from mixed old/new terminology.
- **SOURCE_GRANULARITY:** Single-image guide selects source ad sets. One cold creative in one source ad set can isolate that creative's pool; multiple creatives can pool signals. Do not claim cold-ID-specific exposure or deterministic sequential delivery without evidence.
- **ACCOUNT_UNKNOWN:** Minimum 300 matched member accounts; engagement totals are not unique audience members. Ready status, reachable size after constraints and eligibility require witnessed account evidence. Historical Building label is not readiness. A 30D window is a planning option, not a verified purchase cycle.

## Mandatory future handoff gates

Before P2 strategy, read the manifest and [continuity-map plan](../LinkedIn_Cold_to_RMK_Continuity_Map_Plan.md). Keep content continuity separate from technical audience lineage; no purchase intent is inferred.

Before P3 production, pin the chosen cold IDs/revisions, proof IDs/rights, advertiser/role attribution, format/objective and intended next step. An offline draft may proceed within its mandate while account gate stays open; do not label it live-ready.

Before P5 account implementation, obtain the route-specific mandate, re-open LI01–LI05, then capture sanitized evidence for G1–G5 in the manifest. Evidence must include exact source format/ad-set identity, selectable source category and signal/window, actual audience status/count/reachable size, receiving ad-set targeting and objective/format, exclusions/expansion behavior and measurement/budget decisions. Use no raw audience/member data or private URLs in Git. If carousel cannot be shown as an eligible source, hold that route and present a separately labeled single-image/document/video/website alternative to Bảo; do not migrate cold format or substitute a broader pool silently. Website route requires its own tag/consent/measurement verification.

Source observations are public-doc content, accessed 2026-10-02; no account witness or independent audit. URLs are revalidation targets, not immutable page snapshots. Manifest records concise observations and their limits; existing research source-map remains historical.
