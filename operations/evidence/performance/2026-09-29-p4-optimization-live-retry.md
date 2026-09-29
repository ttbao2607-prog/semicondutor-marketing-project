# P4 optimization production retry — 2026-09-29

**Disposition:** `P4_OPTIMIZATION_PUBLISHED_LIVE_PERFORMANCE_FAIL`. Bảo reauthorized the existing-page production deployment. OSAT and Supplier/Partner were revised and published at their existing URLs. Fabless source and Builder were not changed in this retry. The live Mobile threshold of 80 remains unmet; the revision receipts remain open.

## Source and preflight

- Branch at start: `slice/landing-pagespeed-optimization`, HEAD `96d406653b156dbbfaaf6c16f3b7ce087c6458d3`, clean working tree. Optimization source commit: `0f5e30893139bc41ad8b08ef381b3258e428ed29`. These commits are local only; no Git push or merge was performed.
- The LadiPage operator package's eager imports blocked the official existing-page preflight because unrelated legacy modules were absent. Its local `__init__.py` was changed to load exports lazily. The two local, sanitized `PENDING` receipts were corrected to use unique bounded scopes. The official preflight then returned `EXISTING_PAGE_REVISION_PREFLIGHT_READY` for both.
- OSAT baseline/candidate SHA-256: `743b1bc97f3681addbb3424e5f97cc9c900eed226cf29a1294b8b007c9443070` / `5fc2f85466dc29952059255fd6899a9a2fac2f64e9a1b50e9d84c64460c82ea2`.
- Partner baseline/candidate SHA-256: `7eb55fbe67e2ec2cc7be5e2ba75315dd12ecaa729ef04f2d3b0f2c0376ea94b7` / `b0a2609bea0d06c92c240b428b1888ddf882fd6b2ec941dd1b73b237037eb5a8`.

## Builder and public checks

- Existing OSAT Builder ID ended `11d1e`; existing Partner Builder ID ended `19ebf`. No Basic import, new page, form rebind, tracking edit or lead submission occurred.
- OSAT's previously published anchor fix was already present. Three remaining bounded performance spans were applied through the visible CodeMirror editor. Each selected old span was copied and compared before paste; each replacement came from the operator's one-shot canonical step helper and was hash checked. The complete Builder source matched the exact planned replacement after every edit. After Save/reopen, the complete source matched the unsaved source byte for byte.
- Partner's one bounded `sendHeight` span followed the same selected-text, helper, whole-source and Save/reopen checks. Complete source retention was exact.
- Both existing pages reported Publish success at the same public paths. OSAT public source had zero `panel.offsetHeight` occurrences and both deferred initialization markers. Partner public source had `requestAnimationFrame(sendHeight)`. Public DOM retained OSAT's two CTA IDs, Partner's one CTA ID, the canonical PopupX bridge and `GTM-NGT54TM9` on both routes. No production form submission was attempted.
- `node --test tests/landing-tracking.test.cjs`: 12/12 pass. This is a local source regression test, not a live conversion test.

## Production Lighthouse

Lighthouse 13.5.0 was run against the public production URLs with the CLI's Mobile default and Desktop preset. Bảo requested an independent second Mobile pass to account for measurement variability. Raw JSON remains local and untracked under `%LOCALAPPDATA%\Temp\p4-live-retry-<route>-<mode>.json` and `p4-live-retry2-<route>-mobile.json`.

| Route | Mobile scores (run 1 / run 2) | Mobile LCP (ms) | Mobile TBT (ms) | Desktop score | Desktop LCP | Desktop TBT |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| OSAT | 53 / 54 | 7,849 / 8,394 | 1,056 / 778 | 87 | 2,279 ms | 95 ms |
| Fabless | 50 / 56 | 8,729 / 8,456 | 857 / 739 | 84 | 2,702 ms | 102 ms |
| Supplier/Partner | 55 / 49 | 6,571 / 9,305 | 1,005 / 1,179 | 80 | 2,903 ms | 82 ms |

All nine runs reported CLS 0. Scores are lab observations from two production Mobile runs and one Desktop run per route, not field Core Web Vitals. All six Mobile scores are below the existing 80 threshold, so the second pass does not change the FAIL disposition. The unchanged Fabless route was measured for the required three-route production matrix; its result is not evidence of a Fabless Builder revision in this retry.

## Open gates

The two retry receipts remain `PENDING` outside Git because full lifecycle closeout evidence, including mobile public render/interaction and protected witness hashes, has not been assembled. The earlier P4 performance receipts also remain open. Do not label this deployment `P4_PASS`; further optimization needs a new bounded candidate and authority. No source branch push, merge or GitHub publication occurred.

Docs impact reviewed: `CURRENT_STATE.md` and the OSAT route status were updated. Other canonical tracking and pre-ad documents did not change because no tracking, CTA, form, campaign or spend behavior was changed.
