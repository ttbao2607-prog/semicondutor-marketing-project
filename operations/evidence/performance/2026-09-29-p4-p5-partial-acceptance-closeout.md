# PageSpeed P4/P5 partial acceptance and freeze — 2026-09-29

**Decision owner:** Bảo (Product Owner). **Decision in the active conversation:** “Ghi chấp nhận partial acceptance tại đây do Baotr quyêt định nhé codex. Tối ưu v hết mức rồi và mobile không phải ưu tiên chính. Sau đó closeout freeze P4 và P5 (Hiện tại scope đang trùng p5 luôn r).” This is authority to accept the current production outcome and close the present PageSpeed P4/P5 scope, not a claim that the original Mobile performance gate passed.

## Terminal and boundary

- **Business terminal:** `P4_P5_CLOSED_PARTIAL_ACCEPTANCE_FROZEN`. P4 audit and P5 Decision Pack/Deploy are closed together for the existing three routes at the published P4 source revision `eb88b8e`. No further optimization, repeat deployment, or new PageSpeed measurement is scheduled in this scope.
- **Technical terminal:** `LIVE_MOBILE_PERFORMANCE_BELOW_80`. The >=80 Mobile target remains the original criterion and is explicitly unmet. Desktop passed that score threshold. Partial acceptance is a Product Owner exception to the acceptance decision, not a rewritten metric or a Lighthouse/PSI PASS.
- **Scope rationale:** Source-level optimizations authorized for this slice were exhausted without degrading approved content, desktop appearance, CTA/form binding or measurement. Bảo states Mobile is not the main priority. This does not establish that every possible infrastructure or third-party optimization has been exhausted.
- **Distinction:** This P5 is the PageSpeed plan's “Decision Pack & Deploy”; the earlier tracking/operational Phase 5 retains its separate `PASS WITH SCOPE EXCLUSION` terminal and its consent exclusion.

## Evidence accepted for the decision

The [production deploy ledger](2026-09-29-p4-eb88b8e-production-deploy.md) records same-URL Publish success, source marker verification, 2/2/1 CTA IDs, PopupX opening, GTM presence, Fabless identity-metadata exception approved for this exact revision, and raw Lighthouse 13.5.0 reports. `node --test tests/landing-tracking.test.cjs` passed 12/12 before deploy. The local candidate's 88/91/94 Mobile results are not substituted for live results.

| Route | Live Mobile, two runs | Live Desktop | Decision |
|---|---:|---:|---|
| OSAT | 57 / 53 | 88 | Accept published revision; record Mobile exception |
| Fabless | 48 / 58 | 87 | Accept published revision and the separately approved 52-byte Builder identity oscillation; record Mobile exception |
| Supplier/Partner | 49 / 54 | 86 | Accept published revision; record Mobile exception |

All six Mobile scores are below 80. This remains a production Lighthouse CLI lab sample, not independent PageSpeed Insights field data or a guarantee of future user experience. The live LadiPage and third-party runtime differ from the offline source harness; the precise cause of the score gap was not isolated.

## Closeout limits and freeze

- The three LadiPage `revise_existing_page` receipts created for this deployment remain **PENDING** in local Temp. Their formal `COMPLETED` status requires the operator's canonical/Builder/published revision binding, protected witness hashes, public desktop/mobile marker refs and successful offline closeout validator. This business decision does not fabricate those witnesses or waive the receipt's technical rules.
- The full mobile visual regression matrix and tracking Phase 5 runtime matrix were not rerun in this PageSpeed retry. Live smoke established the CTA/PopupX/GTM inventory and P4 source markers. No form was submitted. Consent behavior, real campaign delivery and lead attribution are not claimed here.
- Freeze means no further edits or republish under this P4/P5 mandate. A later performance campaign, PSI validation, threshold change, LadiPage receipt completion, or platform/third-party optimization must be separately scoped and evidenced. The current published pages remain available at `/semiconductor-osat`, `/fabless`, and `/supplierecosystem`; no rollback was requested.
- Git at decision time: source commit `eb88b8e53fcd2432cb7a003d820959f1276e77c7` was on the local `slice/landing-pagespeed-optimization` branch without upstream, and this closeout documentation was a working-tree change. Production LadiPage publication is separate from Git push or merge; any later branch publication must be verified against the actual remote.

**Independent closeout audit target:** compare this decision with the user's instruction, the production ledger and nine raw reports; confirm the plan and present-state documents distinguish accepted business closure from the unmet Mobile gate; confirm Git/remote state and receipt status are reported without promotion to PASS.
