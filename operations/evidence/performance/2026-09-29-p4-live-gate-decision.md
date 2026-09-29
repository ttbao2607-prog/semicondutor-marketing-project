# PageSpeed P4 live gate decision — 2026-09-29

**State:** all three authorized P4 revisions are published at their existing URLs. The performance closeout gate is **FAIL**, and the three revision receipts remain open. This document does not change the `>=80` Mobile/Desktop threshold or authorize a new page, tracking change, or rollback.

## Measured facts

Lighthouse 13.5.0 on the public live URLs scored Desktop 82/82/85 for OSAT/Fabless/Partner. The first Mobile pass scored 50/62/64; an independent second pass scored 62/62/70. All six Mobile measurements were below 80, with TBT 1,230–3,690 ms versus the P2 target below 300 ms. CLS was 0 in all runs. The local HTML candidate had scored 82–100, so offline PASS did not predict the published environment. The full measurement table and public checks are in `2026-09-29-pagespeed-deploy-attempt.md`.

Live Lighthouse long-task and bootup diagnostics attribute substantial work both to the page itself and to GTM/GA4, Facebook, and other existing third-party scripts. A **diagnostic lab run only** blocked Google Tag Manager, Facebook, LinkedIn and CAPI requests on Partner; Mobile still scored 73 with TBT 1,670 ms. No production tag was changed. This indicates that removing third-party scripts alone would not guarantee the target and cannot justify a tracking mutation. The blocked run is not a valid production score.

## Decision needed for further closeout

The current bounded P1–P3 asset/CSS revision has been deployed and measured. Reaching the Mobile threshold now requires a new, separately audited optimization slice of page-owned render/JS work and perhaps later coordinated review of third-party load policy. That is materially wider than the approved P4 candidate, risks layout/interaction/tracking regressions, and would require a new semantic delta, receipts, public regression and six-route/device measurements. The existing GTM/PopupX/form contract must remain intact unless Bảo separately decides otherwise.

Recommended route: authorize a new offline page-owned performance slice first, with a repeatable Lighthouse gate and no live tracking change. Do not republish until the new local candidate passes and its page-specific preflight/authority is recorded. An alternative business decision would explicitly change the >=80 target for live Mobile; no such exception currently exists. Until then, use `P4_LIVE_PERFORMANCE_FAIL` and do not label the current publication `P4_PASS` or close the receipts.

Git state: the marketing docs and source edits are working-tree/local branch changes only; no Git commit, push, merge or GitHub publication is asserted.
