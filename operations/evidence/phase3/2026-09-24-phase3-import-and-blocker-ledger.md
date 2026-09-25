# Phase 3 import and binding-blocker ledger

**Checkpoint:** updated 2026-09-25, Asia/Ho_Chi_Minh
**Scope:** exact-profile witness, PopupX transfer resolution, structural binding, configured-domain publication, and runtime audit.
**Lifecycle:** three imported Basic targets published under Bảo's Phase 3 action-time confirmation; no lead submission, GTM/GA4 change or campaign activation was authorized.

## Route status

| Route | Exact target | Import checkpoint | Phase 3 terminal | Verified route facts |
|---|---|---|---|---|
| OSAT | `Digiwin Semiconductor - OSAT - UXPM Draft` | `PUBLISHED_CONFIGURED_DOMAIN` | `P3_PASS_OSAT` | Public path `/semiconductor-osat`; one bridge, one SDK and one adapter; two declared CTAs remain present. Header CTA opened the existing modal. |
| Fabless | `Digiwin Semiconductor - Fabless - UXPM Draft` | `PUBLISHED_CONFIGURED_DOMAIN` | `P3_PASS_FABLESS` | Public path `/fabless`; one bridge, one SDK and one adapter; two declared CTAs remain present. Header CTA opened the existing modal. |
| Supplier/Partner | `Digiwin Semiconductor - ERP MES OT - UXPM Draft` | `PUBLISHED_CONFIGURED_DOMAIN` | `P3_PASS_SUPPLIER` | Public path `/supplierecosystem`; one bridge, one SDK and one adapter. Its sole `partner-cta-header` CTA is labeled `Tư Vấn` and opened the existing modal. |

All three public routes contain the runtime binding outside the canonical source artifact. The modal showed name, email, phone and industry; Department and Position remained hidden. No PopupX lead form was submitted. Supplier continues to use business route `partner`.

## PopupX profile and receiver witness

**Product Owner resolution (2026-09-24):** Bảo states that `Bộ phận` and `Chức danh` are hidden controls not visible to customers, and accepts the existing `Bảo` PopupX dogfood as the profile/receiver basis for this saved-preview goal. The four customer-visible fields are name, email, phone, and industry.

**Fresh profile witness:** the exact existing profile was saved and reopened through its normal route. The visible name, email, phone, and industry controls were present; Department and Position remained hidden; Data Leads was enabled; the applicable Industry labels remained intact. No profile, form, receiver, or display-rule change was made. The later snippet retrieval reopened the existing PopupX display/embed surface without clicking `Xuất bản lại`; no republish occurred in this session. No lead values were inspected or retained.

## Runtime and editor evidence

The exact profile's own publish/embed surface exposed one official SDK script and a distinct popup reference. The values were handled transiently. The installed operator helper validated the snippet. The audited `head_combined` mode placed the SDK before the adapter in one HEAD payload. That payload was saved and reopened on all three exact drafts. Cardinality was identical for each: one SDK and one adapter in HEAD, zero SDK and zero adapter in BODY.

The operator helper and its unit-test coverage are in local-only commits in the separate operator repository. Commit `dc0e74d` adds an escaped, readonly visible browser return for the validated combined payload while keeping error responses sanitized. Focused coverage passed 15/15; the full suite passed 374 tests plus 270 subtests. The operator local `main` was clean and seven commits ahead of cached `origin/main`; no push occurred. The installed skill matched the repository copy by SHA-256.

## Transfer attempts and stop condition

Earlier file/clipboard transfer approaches failed: the browser denied the temporary file URL, and the browser virtual clipboard could not receive generated output from the system clipboard. A subsequent loopback-helper attempt timed out before the local form was opened. The final authorized attempt staged the exact profile snippet before starting the helper on a free loopback port with the maximum supported timeout. In the same Chrome session, the visible textarea was cleared and verified empty, the snippet was pasted once, and the textarea value matched the source byte-for-byte with one SDK marker and one inline popup marker. The visible `Validate and prepare` control was activated once.

The local form showed a rejection on its randomized submit route, but the visible submit was not accepted as the one-shot submission and the helper remained active. This did not establish whether the browser sent a POST or whether a request reached the handler: a wrong-path POST can return before the helper marks the one-shot run finished. At that checkpoint the HTTP method and exact rejection point were unobserved, so the attempt stopped without a capture payload or receipt. The verified helper process was stopped, the listener was confirmed absent, the empty temporary directory was removed, virtual clipboards were cleared, and the local capture tab was closed. No raw snippet, provider reference, private URL, screenshot, or PII was retained. The later synthetic reproduction and resolution are recorded below.

### Capture blocker resolution

The failure was reproduced outside LadiPage with a synthetic valid snippet in the same Chrome/CUA browser surface. Fixed diagnostic enums showed a correct randomized submit path rejected specifically because the host extension emitted `Origin: null` while Fetch Metadata identified a same-origin top-level document navigation. Operator commit `f8d4954` now admits `Origin: null` only when `Sec-Fetch-Site: same-origin`, `Sec-Fetch-Mode: navigate`, `Sec-Fetch-Dest: document`, the exact loopback Host and the exact randomized route all match. Missing metadata, cross-site requests, wrong hosts/routes and malformed requests remain rejected.

The post-fix same-Chrome/CUA synthetic smoke test returned `TRANSFER_COMPLETE`, produced a v2 combined-head payload and sanitized receipt, and completed hash-checked cleanup. Focused tests passed 35/35; the operator full suite passed 373 tests plus 270 subtests; source and installed skill validation passed. The operator local `main` and installed skill were synchronized at `f8d4954`; no push occurred. This proves the capture transport compatibility boundary, not a real LadiPage binding.

**Current terminals:** `P3_PASS_OSAT`, `P3_PASS_FABLESS`, and `P3_PASS_SUPPLIER`.

### Structural binding result and runtime boundary

The repaired visible capture flow accepted the real exact-profile snippet, returned a v2 combined payload/receipt, and passed hash-checked cleanup. The payload was applied sequentially to OSAT, Fabless, and Supplier/Partner. Each settings save was followed by a page save, reload, reopen, and marker-cardinality audit. The Supplier preview also visibly confirmed the single `Tư Vấn` button with ID `partner-cta-header`. Dashboard refresh showed all three exact drafts as `CHƯA XUẤT BẢN`.

OSAT's CTA was exercised only in LadiPage Builder Preview. No popup appeared. The preview document is hosted at `app.ladipage.com/about:srcdoc`, while the PopupX profile is scoped to root domain `digiwin.com.vn`; this host mismatch means the internal preview is insufficient provider proof. It is recorded as a runtime validation boundary, not a structural binding failure. Fabless and Supplier were not repeatedly clicked under the same known-invalid preview condition.

### Configured-domain resolution

Bảo authorized publication for Phase 3. The three exact targets were published at `https://solutions.digiwin.com.vn/semiconductor-osat`, `https://solutions.digiwin.com.vn/fabless`, and `https://solutions.digiwin.com.vn/supplierecosystem`. The first configured-domain test proved that the canonical bridge and adapter were present but the modal action did not render. Read-only SDK inspection showed the current `actionPopupX` contract requires the profile reference as its second argument and the configured popup action target as its third argument. The frozen helper passed `null` for that target.

Operator commit `95a4047` now resolves the `show_popupx` action target from the loaded configuration belonging to the exact profile, then calls the SDK with both references. It does not persist or report either physical reference. Focused tests passed 38/38 and the full suite passed 374 tests plus 271 subtests. The corrected combined HEAD and canonical bridge were saved and republished sequentially on all three targets. Public audits found one bridge, one adapter, the expected CTA marker count, and no fallback BODY runtime. Fresh configured-domain checks opened one PopupX iframe with the four visible customer fields from both OSAT CTAs, both Fabless CTAs and Supplier's sole CTA. No values were entered or submitted during this resolution.

## Boundaries and evidence limits

- Each route has one canonical bridge, one SDK and one adapter, with no fallback runtime in BODY.
- No PopupX lead form was submitted; no domain, GTM/GA4, profile, receiver or form configuration changed.
- All three configured-domain routes pass Phase 3 popup-opening behavior. This does not prove lead acceptance or Phase 4 measurement.
- Desktop pre-bind baselines are established for all routes. Mobile evidence is incomplete for Fabless and Supplier/Partner; OSAT's mobile pre-bind baseline was checked.
- The three listed public paths are the Phase 3 routes authorized and published in this checkpoint; this does not authorize later route/domain changes.
- The record contains no physical page/profile IDs, private URLs, account/session data, lead values, screenshots, credentials, cookies, or tokens.

## Resume condition

Proceed to Phase 4 only under its separate tracking-debug mandate. A synthetic lead submission still requires action-time confirmation and must not be inferred from the Phase 3 modal-opening evidence.
