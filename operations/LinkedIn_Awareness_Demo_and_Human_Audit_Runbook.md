# LinkedIn Awareness demo and human content audit runbook

2026-10-01 · CANONICAL PROCESS for the current LinkedIn Awareness carousel workflow. Bảo adopted the existing mockup for this review process. That adoption does not approve current ad content, story, authority, storyboard or account/live use. Other formats require a separate mandate; this is not a generic automation framework.

## Required loop and ownership

Executor assembles artifacts/demo and identity evidence. Coordinator/auditor independently reconciles mechanics and render findings. Bảo or a named authorized human reviewer owns content accept/edit/hold for an exact revision. No review status is inferred from file creation or an audit PASS.

| Step | Required action and evidence | Stop/revision rule |
|---|---|---|
| 1. Artifact exists | Immediately pin variant/locale, ordered card IDs, caption/native headlines/alt/destination, displayed copy, proof/source scope and rights, input revisions/SHA256. Include current PNG and copy differences explicitly. | Missing components may be shown as a labelled rough/partial demo, blocked for full acceptance. Never silently mix revisions. |
| 2. Assemble current demo | Use retained fixture route below after E4 rough output and immediately after each E5 artifact/revision. Demo shows full caption and initial cover together, ordered navigation, native headlines, inert destination. Source-map/manifest pin exact bytes. | No content handoff as ready without current demo. Old demo may stay history but cannot authorize changed content. |
| 3. Mechanical identity | Reconcile every card order/locale/text/alt/destination/source hash, embedded image/logo bytes and explicit mismatch list. | Any unresolved revision/identity mismatch prevents full acceptance. |
| 4. Rendered QA | Observe desktop and mobile initial feed/fold, caption/cover, all cards, headlines, context/source qualification, clipping/readability and navigation. Record exact views/actions, evidence and unobserved interactions. | Source code is not rendered evidence. Missing viewport/action evidence remains unknown or partial. |
| 5. Human context review | Apply criteria below to current demo; record findings by AC/card/transition/revision with required action/owner. | Human reads current feed sequence, not only isolated source copy. No simulated target-buyer validation. |
| 6. Decision | Explicit accept/edit/hold mapped to revision/hash and review criteria using receipt template. | Acceptance only within stated scope. Missing reviewer/date/decision is unknown, never prefilled approved. |
| 7. Changed content | Any copy/image/locale/order/proof/destination change rebuilds demo/source-map/manifest; reobserve affected views/transitions and dependent claims. Link superseded receipt. | Old approval invalid for changed revision. Preserve original observations/history; no checkbox closure without evidence. |

## Retained route: adapt inputs, not a generic pipeline claim

Existing approved review fixture: `operations/linkedin-awareness-execution/linkedin-feed-mockup/index.html`; builder is **build_fixture.py**. `template.html` supplies local static HTML/CSS/JS. Builder inspected: hardcodes repo-root depth, V2 directory, revised-copy JSON, A1/A2v3/A3/A4/A5 and B1-B4/B5reuseA5 mapping, official-logo path, baseline and historical-difference notes. It embeds original image bytes as data URIs and JSON without image transforms. It is not manifest-driven or generally reusable without adapting those hardcoded inputs.

For a new content revision, create a versioned sibling demo within the authorized content task. This adopted workflow includes routine demo assembly/rebuild; no separate approval is needed. Seek a decision only for material scope change, new format or live authority. Adapt builder/template copy and mapping from that revision's selected manifest, update baseline/source notes and pin builder revision/hash. Inspect inputs, assemble current demo immediately, then audit source-map and rendered views. Do not execute the old hardcoded builder as if it consumed new assets automatically, overwrite the audited frozen mockup, or add framework/scheduler/account integration. Prefer offline file viewing; any loopback preview follows local-web-preview under authorized browser ownership.

Fixture geometry is simulation, not exact live LinkedIn UI. Existing route has desktop640/post580, mobile390, first-card85% with next peek, inert chrome and destination, no invented metrics/profiles. [Official Help](https://www.linkedin.com/help/linkedin/answer/a423087) supports introductory150recommended/255max and headline2lines; firstcardfull/secondpeek follows [official tips](https://business.linkedin.com/advertise/ads/sponsored-content/carousel-ads/tips?product=sales). Exact85%width is fixture geometry, not a verified live specification. No account/upload/spend permission follows from demo review.

## Human review criteria

| AC | Reviewer observes | Required evidence/decision granularity |
|---|---|---|
| H1 Initial feed trigger | Cover plus full caption: recognizable consultant observation, credible Quality/OSAT situation, professional interest without consumer suspense. | Initial desktop/mobile view; accept/edit/hold per opening revision. |
| H2 Role/pain | Intended role recognizes one pain and review situation. In future revisions, the first customer-visible OSAT/Fabless or acronym mention in each ad has a brief locale-matched, source-checked parenthetical explanation; association/cue remain source-bounded hypotheses. | Exact card/caption finding and character-limit check, not invented buyer research. See first-touch-anchor.md dated 2026-10-02; existing revisions stay historical. |
| H3 Story continuity | Every 1→2→3→4→5 transition understandable, progression or question framework coherent, conclusion earns management/brand connection. | One observation/decision for each transition; source storyboard alone insufficient. |
| H4 Authority/proof | Consultant viewpoint supported without unsupported cases/years/outcomes; verified claims retain exact authorized scope/source/rights; ERP versus MES separated; Taiwan/local regional scope and source qualifiers readable and exact. | Claim string/card + source revision/scope/rights; preserve essential Taiwan attribution. |
| H5 Brand/copy discipline | Logo/wordmark/headline/body/proof frequency and prominence justified; no customer-visible em/en dashes, weak illustration/meta labels, success ticks or invented record data. | Count and role per affected card; no mechanical brand-count PASS. Internal AI fictional provenance retained. |
| H6 Readability/context | Vietnamese glyphs, nativeheadline lines, full source qualification, no clipping, feed/fold/card order/navigation coherent on observed views. | Viewport/action/evidence and unknowns; approximate font/logo or simulated UI disclosed. |

## Separate status models and release gate

- Execution: `SUCCESS`, `PARTIAL`, `FAILURE`, `BLOCKED` describe achieved work/evidence, not human approval.
- Audit: `AUDIT_PASS`, `AUDIT_FAIL`, `INSUFFICIENT_EVIDENCE` describe independent comparison against contract. Audit findings are reconciled claims, not automatic mutation authority.
- PO/human review: `READY` (awaits decision), `CHANGES_REQUESTED`, `ON_HOLD`, `ACCEPTED_FOR_OFFLINE_CONTENT` (explicit scoped revision). Accept/edit/hold correspond to accepted/changes/hold; never default to accepted.

Offline content release after E5 and before E7 requires **current demo + source-map + artifact manifest + desktop/mobile observations + completed revision-bound human receipt**, plus source/rights/native/spec gaps reconciled for that release. E4 rough context previews and every revision use the same loop with partial status where needed. Missing/mismatched rough artifacts may help discussion but block full `ACCEPTED_FOR_OFFLINE_CONTENT`. Acceptance of this process or visual direction is not content acceptance, buyer learning, final account approval or live/spend mandate.

Template: `operations/linkedin-awareness-execution/human-review-receipt-template.md`. Actual workflow-only adoption receipt: `demo-process-po-acceptance.md` in the same directory. Keep receipts outside audited mockup's hashed set. Handoff links contract, demo/source-map/manifest, rendered observations, human receipt and exact selected revision; changed inputs invalidate dependent acceptance.
