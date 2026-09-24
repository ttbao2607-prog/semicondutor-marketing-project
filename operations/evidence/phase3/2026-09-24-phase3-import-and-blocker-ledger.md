# Phase 3 import and binding-blocker ledger

**Checkpoint:** 2026-09-24, Asia/Ho_Chi_Minh
**Scope:** Phase 3 import identity and read-only PopupX readiness gate only.
**Lifecycle:** imported, unpublished drafts; no binding save/reopen occurred; publication was not authorized.

## Route status

| Route | Exact target | Import checkpoint | Phase 3 binding terminal | Verified baseline / route fact |
|---|---|---|---|---|
| OSAT | `Digiwin Semiconductor - OSAT - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_OSAT_RUNTIME_RESOLVER_UNPROVEN` | Basic HTML-to-LadiPage import and builder identity verified; desktop baseline verified. Mobile evidence is incomplete. Two declared OSAT CTAs remain provider-free in the imported source. |
| Fabless | `Digiwin Semiconductor - Fabless - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_FABLESS_RUNTIME_RESOLVER_UNPROVEN` | Basic HTML-to-LadiPage import and builder identity verified; desktop baseline verified. Mobile evidence is incomplete. Two declared Fabless CTAs remain provider-free in the imported source. |
| Supplier/Partner | `Digiwin Semiconductor - ERP MES OT - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_SUPPLIER_RUNTIME_RESOLVER_UNPROVEN` | Basic HTML-to-LadiPage import and builder identity verified; desktop baseline verified. The sole CTA is `partner-cta-header`, labeled `Tư Vấn`. |

All three drafts are unpublished. The desktop baseline was checked before any mutation. The checkpoint does not claim a saved/reopened page or a working modal; the Supplier mobile state is not upgraded to a separate PASS by this record. Supplier continues to use business route `partner`.

## PopupX profile and receiver gate

**Product Owner resolution (2026-09-24):** Bảo states that `Bộ phận` and `Chức danh` are hidden controls not visible to customers, and accepts the existing `Bảo` PopupX dogfood as the profile/receiver basis for this saved-preview binding goal. The four customer-visible fields are name, email, phone, and industry. This resolves the prior field and receiver-basis ambiguity for this goal; no profile, form configuration, or display rule was changed. No lead values were inspected or retained.

**Runtime resolver check (2026-09-24):** the authenticated LadiPage domain inventory showed `solutions.digiwin.com.vn` verified with SSL enabled. Bảo clarified that the absence of PopupX on the current root homepage is context only, not a blocker for unpublished drafts that will receive the SDK. Read-only inspection of the authenticated PopupX manager/editor and the existing published profile found no visible official embed snippet or unambiguous runtime trigger for this exact profile. The profile action menu exposed no embed-code action; the editor exposed page-level JavaScript/CSS and display-configuration entries, but no usable integration snippet through the accessible UI. The published view's observed external `<script src>` entries were standard LadiPage CDN bundles; no PopupX-named SDK was found among them. The inspected DOM had no native trigger attribute or bridge-event literal, and its accessible render was blank. The existing dogfood evidence remains accepted by Bảo as the profile/receiver basis, but does not itself provide the exact runtime SDK/trigger. Therefore the environment-owned provider reference still cannot be derived unambiguously without guessing. No profile, form, or display configuration was changed. No physical provider/page references or private URLs are retained.

**Stop condition:** the profile/receiver basis is accepted by the Product Owner for this saved-preview goal, but do not add the PopupX SDK or adapter, save/reopen, or test a CTA until the authenticated profile/editor surface yields an official integration snippet or runtime trigger unambiguously bound to the exact published profile. That resolver was not exposed on this attempt; all three routes remain blocked at that shared gate. Revalidate each exact target and its final Phase 2 package immediately before resuming.

## Boundaries and evidence limits

- No page binding or builder edit; no SDK/adapter; no save/reopen; no CTA/modal test; no form submission; no profile/configuration edit; no publication; no GTM/GA4 change.
- All three drafts remain unpublished. This is not `P3_PREVIEW_ONLY` and does not satisfy any `P3_PASS_<ROUTE>` terminal.
- Desktop baseline verification is established for all routes. Mobile evidence is incomplete for OSAT and Fabless; this ledger makes no mobile PASS claim for those routes.
- Future public paths reserved by the Product Owner are `solutions.digiwin.com.vn/semiconductor-osat`, `solutions.digiwin.com.vn/semiconductor-fabless`, and `solutions.digiwin.com.vn/semiconductor-supplierecosystem`. They are future targets only, not published routes or publication authorization.
- This sanitized record contains no physical page/profile IDs, private URLs, account/session data, lead values, screenshots, credentials, cookies, or tokens.

## Resume condition

Resume Phase 3 only after an official integration snippet or runtime trigger for the exact published profile is unambiguously available from the authenticated PopupX environment; the Product Owner's existing dogfood profile/receiver basis remains accepted for this saved-preview goal, and root-homepage PopupX absence alone is not a blocker. Then revalidate the route-specific final bridge receipt/artifact and exact imported target. Preserve the saved-preview-only lifecycle. Publication remains outside this checkpoint.
