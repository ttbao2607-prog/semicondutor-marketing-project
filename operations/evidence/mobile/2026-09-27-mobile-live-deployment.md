# Mobile LadiPage revision — live deployment evidence (2026-09-27)

Scope: exact existing production pages OSAT (`/semiconductor-osat`, existing editor page), Fabless (`/fabless`, existing editor page), Partner (`/supplierecosystem`, existing editor page). Bảo authorized mobile-only integration and deployment preserving Phase 5 tracking. The three `PENDING` revise_existing_page receipts and baseline files are kept as local-only evidence outside the public repository; all three offline preflights returned `EXISTING_PAGE_REVISION_PREFLIGHT_READY`.

The local canonical files were already merged in local `main` before browser work. Browser transfer used `serve_builder_step.py` one-shot loopback pages for each declared `after` span. Every step SHA-256 matched the local bridge output. Edits were confined to the declared CSS/mobile rail/mobile-toggle script spans in visible CodeMirror; after each span, the entire current Builder source matched the in-memory expected source exactly. No Basic upload, new page, form rebinding, GTM mutation, or lead submission occurred.

| Route | Canonical candidate SHA-256 | Saved/reopened Builder SHA-256 | Builder readback | Publish result |
|---|---|---|---|---|
| OSAT | `10c09475dd31053475293a96b7c76fab404981ad3bf267f7f1cba3541b1de862` | `41e22f81d9d3d6c06724994414a248b5b57443d5693c0b6cfbff844c7f0d35a3` | exact | success, same URL |
| Fabless | `865b3b21e2cc45fa8b5d7bf1c7c3fabf836ce231af85ec803a24c45f7234351c` | `95e29680f8ba128cf57263a887ec10bbed87566fa4d853a7eb0d4370b1f0239c` | exact | success, same URL |
| Partner | `41247974b1c7e5aa33ec709d678a05cec6ae24aa7ba5398c2f078708134a623e` | `97c5e9c2fea951054ed29a64a2ce9a146dfe57f9d0190a0b75edf7694ea14e16` | exact | success, same URL |

OSAT first Save removed 52 bytes of Builder-owned `store_id/time_zone` identity metadata outside the declared delta, so publication was stopped. The five mobile spans were rolled back visibly and baseline saved/reopened exactly without that pair. The second bounded attempt from this normalized baseline survived Save/reopen byte for byte and was the only OSAT mobile version published. This metadata normalization did not alter the PopupX adapter or tracking scripts. Fabless and Partner began from Builder baselines already lacking that pair, and both survived Save/reopen exactly.

Public desktop load showed the mobile markers in DOM on all three routes and the original CTA inventory: OSAT 2, Fabless 2, Partner 1. At 390px, each route showed its compact rail and collapsed map/architecture, with document scroll width 375px against 390px viewport. Fabless and Partner expand toggles were clicked; both showed `aria-expanded=true` and restored detail display. OSAT at 390px showed both mobile detail toggles and collapsed detail panels; after a clean public reload, the map toggle opened the detailed map and the nested inspector toggle opened the inspector (`aria-expanded=true` and displayed content for both). All three header CTAs opened the existing PopupX iframe (`popupx.ladi.me/6ab20306eb562e0011c1b1ed`) with visible overlay. No form was submitted.

All public routes retained one PopupX adapter and the `GTM-NGT54TM9` loader. Direct read-only CDP inspection of page runtime found `window.__dgwAwarenessSectionInitV1=true` and `section_view` events in `dataLayer`: OSAT `top` and `operations-questions`, Fabless `top` and `fabless-map`, Partner `top` and `ecosystem-architecture`. Existing Phase 5 focus/pagehide and GA4 network evidence was not rerun; this deployment changed only the declared mobile spans and did not modify the tracking code or GTM configuration. Consent behavior retains the Phase 5 scope exclusion.

At deployment closeout, the canonical mobile source was in local `main` commit `d2eb627`; that source had not reached GitHub. The LadiPage publication is live independently of GitHub. All three operator lifecycle receipts remain outside the public repository and validate as `EXISTING_PAGE_REVISION_RECONCILED` against their baseline and candidate files. This ledger records the sanitized deployment evidence; Git synchronization is tracked separately from LadiPage publication.



## Public response and protected witness hashes

The public response bodies returned HTTP 200 at the exact configured URLs. Their SHA-256 hashes were stable across two reads: OSAT `07964d21a671871447de5e2dfcccb71413c1561a7489b772684969b474b154f7`, Fabless `c6828e3f168ccf5840f45c96fe10042e07ca6130f7300587a46c720c959da113`, Partner `dcae8cded4e6640707414713389207474e2c77b49f741329dd6368b14077e4e6`. These public bytes include LadiPage runtime material and are distinct from both canonical candidate and saved Builder hashes.

Before/after SHA-256 witnesses of the actual Builder source matched for each route: tracking script, PopupX adapter script, CTA ID list, and the desktop CSS block before the inserted mobile override. The witness hashes are retained in local-only completed receipts. Browser runtime inspection found one `section_view` for the first visited section and a second for the selected destination section, with no duplicate view observed in this smoke. This was a deployment regression check, not a repeat of the full Phase 5 focus/pagehide matrix.

The canonical candidate bytes derived from each receipt match the Git blob for the three HTML paths in local `main` commit `d2eb62782fe25d3f96b8f6149d5610747d84642d` (tree `a306249330703cf748ff71948048249809f064ff`). The operator lifecycle validator returned `EXISTING_PAGE_REVISION_RECONCILED` for OSAT, Fabless and Partner using local-only baseline/candidate/receipt files. Validation checks receipt structure and hashes; the browser and public observations above are the separate live evidence.
