# Phase 3 import and binding-blocker ledger

**Checkpoint:** 2026-09-24, Asia/Ho_Chi_Minh
**Scope:** exact-profile witness, PopupX runtime resolution, and saved-preview transfer attempt.
**Lifecycle:** three imported drafts; binding remains blocked; drafts remain unpublished; no lead submission or publication was authorized.

## Route status

| Route | Exact target | Import checkpoint | Phase 3 terminal | Verified route facts |
|---|---|---|---|---|
| OSAT | `Digiwin Semiconductor - OSAT - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_OSAT_CAPTURE_REQUEST_HANDLING` | Basic import and builder identity were previously verified. Desktop and mobile pre-bind baselines were checked. Two declared CTAs remain provider-free. The earlier settings attempt was undone and the page reloaded unchanged; the final transfer attempt did not touch this draft. |
| Fabless | `Digiwin Semiconductor - Fabless - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_FABLESS_SHARED_CAPTURE_GATE` | Basic import and builder identity were previously verified; desktop baseline is verified and mobile evidence remains incomplete. Two declared CTAs remain provider-free. Route binding did not start after the shared capture gate failed. |
| Supplier/Partner | `Digiwin Semiconductor - ERP MES OT - UXPM Draft` | `IMPORT_VERIFIED_UNPUBLISHED` | `P3_BLOCKED_SUPPLIER_SHARED_CAPTURE_GATE` | Basic import and builder identity were previously verified; desktop baseline is verified and mobile evidence remains incomplete. Its only CTA is `partner-cta-header`, labeled `Tư Vấn`. Route binding did not start after the shared capture gate failed. |

All three drafts remain unchanged, unpublished, and unbound. No route completed a binding save/reopen, CTA modal check, or post-bind desktop/mobile check. No PopupX lead form was submitted. Supplier continues to use business route `partner`.

## PopupX profile and receiver witness

**Product Owner resolution (2026-09-24):** Bảo states that `Bộ phận` and `Chức danh` are hidden controls not visible to customers, and accepts the existing `Bảo` PopupX dogfood as the profile/receiver basis for this saved-preview goal. The four customer-visible fields are name, email, phone, and industry.

**Fresh profile witness:** the exact existing profile was saved and reopened through its normal route. The visible name, email, phone, and industry controls were present; Department and Position remained hidden; Data Leads was enabled; the applicable Industry labels remained intact. No profile, form, receiver, or display-rule change was made. The later snippet retrieval reopened the existing PopupX display/embed surface without clicking `Xuất bản lại`; no republish occurred in this session. No lead values were inspected or retained.

## Runtime and editor evidence

The exact profile's own publish/embed surface exposed one official SDK script and a distinct popup reference. The values were handled transiently. The installed operator helper validated the snippet. One target-specific save/reopen observation found that page HEAD content persisted while BODY content was discarded. This observation is recorded in the local operator repository at `docs/g7-head-combined-fallback-evaluation-20260924.md`; it does not establish general LadiPage behavior or prove that a combined payload persists, executes, or opens PopupX. The audited `head_combined` mode is opt-in and places the SDK before the adapter in one HEAD payload. No combined payload was saved to a LadiPage draft.

The operator helper and its unit-test coverage are in local-only commits in the separate operator repository: runtime binding `0035e84`, opt-in head-combined fallback `a70bf9c`, one-shot capture `63c8962`, and sanitized error handling `e6b1f4f`. The operator repository's `main` was clean at `e6b1f4f`, four commits ahead of its cached `origin/main`; the fallback branch was local-only. Relevant coverage is in `tests/test_popupx_runtime_binding.py` and `tests/test_popupx_snippet_transfer.py`, including combined-head placement/cleanup and one-shot request validation. These are code-level tests, not live-capture evidence; this capture produced no success receipt or output payload.

## Transfer attempts and stop condition

Earlier file/clipboard transfer approaches failed: the browser denied the temporary file URL, and the browser virtual clipboard could not receive generated output from the system clipboard. A subsequent loopback-helper attempt timed out before the local form was opened. The final authorized attempt staged the exact profile snippet before starting the helper on a free loopback port with the maximum supported timeout. In the same Chrome session, the visible textarea was cleared and verified empty, the snippet was pasted once, and the textarea value matched the source byte-for-byte with one SDK marker and one inline popup marker. The visible `Validate and prepare` control was activated once.

The local form showed a rejection on its randomized submit route, but the visible submit was not accepted as the one-shot submission and the helper remained active. This does not establish whether the browser sent a POST or whether a request reached the handler: a wrong-path POST can return before the helper marks the one-shot run finished. The HTTP method and exact method/path rejection point were not observed; record the blocker as **unresolved capture request method/path handling**. No capture payload or receipt was generated. The verified helper process was stopped, the listener was confirmed absent, the empty temporary directory was removed, virtual clipboards were cleared, and the local capture tab was closed. No raw snippet, provider reference, private URL, screenshot, or PII was retained.

**Current terminal:** `BLOCKED` — Phase 3 live binding is blocked on unresolved capture request method/path handling. Do not label any route `P3_PREVIEW_ONLY` or PASS. Do not repeat the current capture route without a diagnosed, tested, and approved transfer flow.

## Boundaries and evidence limits

- No route SDK/adapter was saved; no binding save/reopen or CTA/modal test occurred.
- No PopupX lead form was submitted; no landing draft was published; no domain, GTM/GA4, profile, receiver, or form configuration changed.
- All three drafts remain `IMPORT_VERIFIED_UNPUBLISHED`; no route passes Phase 3.
- Desktop pre-bind baselines are established for all routes. Mobile evidence is incomplete for Fabless and Supplier/Partner; OSAT's mobile pre-bind baseline was checked.
- Future public paths reserved by the Product Owner are not published routes or publication authorization.
- The record contains no physical page/profile IDs, private URLs, account/session data, lead values, screenshots, credentials, cookies, or tokens.

## Resume condition

Resume only after capture request method/path handling is resolved and a supported visible-UI transfer flow is tested to complete the helper's one-shot POST without using another browser surface, DOM injection, direct file access, or other workaround. Then revalidate each exact target and its final Phase 2 receipt/artifact. Continue sequentially OSAT, Fabless, Supplier/Partner under the existing saved-preview authority; stop on the first failure. Publication, domain changes, GTM changes, and lead submission remain outside this checkpoint.
