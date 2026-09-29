# PageSpeed P4 — offline deployment decision pack (2026-09-29)

**Terminal:** `OFFLINE_HANDOFF_PREPARED`; LadiPage revision **not authorized or preflight-cleared**. P4 offline audit passed. No Builder, publish, form, tracking container, campaign, Git commit, or push action was performed for this handoff.

## Candidate and evidence

Existing published routes: `/semiconductor-osat`, `/fabless`, `/supplierecosystem` on `solutions.digiwin.com.vn`. Use `revise_existing_page` on each exact existing Basic page, preserving its URL; no new page, HTML import, or form rebind. The detailed local gate and limits are in `2026-09-29-p4-offline-audit.md`.

| Route | Earlier published canonical baseline SHA-256 (LF bytes) | P4 derived candidate SHA-256 (LF bytes) | Delta operations | Local Lighthouse Mobile / Desktop |
|---|---|---|---:|---:|
| OSAT | `10c09475dd31053475293a96b7c76fab404981ad3bf267f7f1cba3541b1de862` | `28bdd8b7a9426f2e2a9771020fec1e09f50657fe66fc889406d8da9ead1c2e6b` | 7 | 82 / 95 |
| Fabless | `865b3b21e2cc45fa8b5d7bf1c7c3fabf836ce231af85ec803a24c45f7234351c` | `efa748ad299e1512d470d9d3c764ed7fac3045851e77b2f55089e065117eba79` | 9 | 92 / 97 |
| Supplier/Partner | `41247974b1c7e5aa33ec709d678a05cec6ae24aa7ba5398c2f078708134a623e` | `e43d7c3a747bd7c58da809c1e131ffd65e7e0114cdbf24d6ad35e6a2eeba20d4` | 7 | 93 / 100 |

The baseline files match byte for byte with the earlier mobile-revision candidate artifacts and local `main`. The proposed deltas reproduce the three LF candidate files exactly under the operator's `apply_semantic_delta` validator, with no delta errors. They are local planning artifacts under `%TEMP%/semiconductor-pagespeed-revision-20260929/`; the per-page receipt drafts contain private target identities and stay out of public Git. Delta SHA-256 values (JSON drafts): OSAT `7e8da58ca89b01e3556459537920d5699976a8f8f03925dc58f36c91938d8bb9`, Fabless `d4785913a14edface27fda1e9ca39f354c829ab65e218bed2025f07569f96cc4`, Partner `6915e085339f50c910a8d4e759baa1f7caceb664e764c9c59e2e762501e6f46f`.

Windows `core.autocrlf=true` gives the current checked-out HTML different raw-byte SHA-256 values: OSAT `19fb86f7fee3cfcf8e0da46b1c38ca14ba5273592bd3f382e54c5b7f2943b20c`, Fabless `8fad9ea264655aa3d49cdd784a827286192fd4a6f14eff80a6fd1fe554eee893`, Partner `7eb55fbe67e2ec2cc7be5e2ba75315dd12ecaa729ef04f2d3b0f2c0376ea94b7`. This is line-ending normalization, not a second content candidate. Before an authorized Builder action, pin one exact LF candidate artifact and verify its bytes against the proposed delta, then verify the named Builder baseline is still current. The current branch has an uncommitted OSAT fix; no candidate commit or remote push is claimed.

## Gate results and limits

- Local Lighthouse 13.5 scores exceed 80 on all six route/device runs; OSAT Mobile repeated at 84. They do not establish post-publish PSI scores.
- Tracking source tests passed 12/12; source bridge inspection was READY on all three routes; CTA inventory remained 2/2/1. CDN availability check returned image HTTP 200 for 46 distinct URLs. Desktop anchor navigation, narrow disclosure toggles, and 390px width checks passed as detailed in the P4 ledger.
- Exact 390px touch-emulated click dispatch was unreliable in the local browser control; desktop and narrow non-touch interaction checks passed. Live Builder normalization, PopupX, GTM, and PSI remain action-time verification items.
- Preserve section IDs/observer behavior, CTA IDs/count and `Tư Vấn` label, content/proof, same public URL and page identity, and the existing PopupX/form and GTM configuration. The HTML source contains no new form or provider binding.

## Authority and execution boundary

Draft `PENDING` receipts use each prior target identity and URL, but deliberately set `approved=false` and `production_authorized=false`: the 2026-09-27 mobile-revision authority does not approve this PageSpeed revision. Direct invocation of the operator's `validate_preflight` against the exact baseline bytes rejects all three drafts **only** with `explicit_named_scope_authority_required` and `production_scope_not_authorized`; delta application itself has no errors. The packaged command-line validator currently fails during package import because `m2_proof_of_life` is absent from its import path. This tooling issue must be resolved or the same validator function invoked with a documented equivalent before production action.

Once Bảo issues a new exact-target production mandate, update the three receipts with that scope and run the operator preflight again. At action time, compare the live Builder page identity and normalized source with the receipt baseline. If either differs, stop and regenerate the delta and receipt from the observed current baseline. Then apply only the bounded semantic patch, Save/reopen, publish to each same URL, and verify desktop/mobile public markers, CTA/PopupX opening, section tracking, GTM loader, layout, and PSI. Close out each receipt with sanitized evidence and stop/rollback if a protected invariant fails. Do not submit a lead as part of PageSpeed verification without separate authority.

## Docs impact

Reviewed `DOCS_IMPACT_MAP.md`, `CURRENT_STATE.md`, the PageSpeed plan, OSAT route truth, tracking contract and existing-page operator contract. Current canonical pages and tracking configuration have not changed live; the P4 candidate state is already reflected in `CURRENT_STATE.md`, the plan and OSAT route truth. **Docs impact reviewed: no additional canonical update required for this offline handoff.**
