# Fabless interaction repair: prepared, stop before deploy

## Pinned local state

Repair commit: `2e52bf1346d1214a2823b69f10aed7c735f3daef`, integrated into local `main` by fast-forward on 2026-09-30. No GitHub push. Source: `landing/fabless-route/fabless-outsourced-popupx-basic-flat.html`.

Git-object source SHA-256: `5db304b5fad545ed81847453d1d3eb4db06b81b943e75f848d118d0fcb0f15b1`. The baseline is the same path at `0dcbb939224e495111cead99f1c8ed38c6e0c9ed`. `package-manifest.json` also distinguishes Git LF bytes from checkout CRLF bytes.

`pending-request-template.json` declares four bounded semantic operations. The official `apply_semantic_delta` helper reproduced the complete committed candidate exactly from the baseline. Request preflight was run in memory against baseline Git bytes; it correctly rejects the template only for absent named production authority. It is not a passed deploy receipt. Exact page identity is deliberately unresolved in this public-safe template; no authenticated Builder source or physical runtime references are retained.

## Current stop

Bảo explicitly requested preparation and stopping before deployment because another Codex process is deploying the previous main. That running state is PO-reported, not independently observed here. Do not claim its browser, open Builder, run a step server, save, publish, submit a form, or alter any existing receipt. This package has no live authority and does not release itself when time elapses.

## Resume sequence after a new deployment instruction

1. Read `git-state-recovery`, `CURRENT_STATE.md`, `DOCS_IMPACT_MAP.md`, `$ladipage-operator` and its `revise_existing_page` contract. Obtain the prior controller's completion/handoff evidence before acquiring the single browser controller role. Record its actual source commit, same-page identity, Save/reopen and public state. If its Git/docs closeout is still writing shared files, wait for that handoff before editing those files.
2. Require Bảo's new authority for the exact existing Fabless page and `https://solutions.digiwin.com.vn/fabless`. The only target is Fabless. Do not upload/create a page or modify OSAT/Partner. The current instruction does not authorize this step's live action.
3. Resolve and verify the exact page identity from authorized evidence. Copy the template into a new operation-owned local receipt outside Git; bind that identity and the new authority. Never overwrite the prior deployment's receipts. Keep status `PENDING` until the complete lifecycle is witnessed. Do not simply flip authority booleans because a template exists.
4. Materialize the pinned baseline and candidate from Git with a binary-safe `subprocess.check_output(['git','show', commit + ':' + path])` write. Require the manifest's hashes and exact source blob. Run `scripts/validate_existing_page_revision_request.py <new-receipt> --baseline <baseline-artifact>` from the operator skill. A future main commit must not silently change the source pin. If HTML changed, re-audit and regenerate the bounded delta before proceeding.
5. Before any edit, capture the normalized Builder anchor and reconcile it with the previous controller's completed revision. Require every patch anchor to be unique and confirm protected witnesses. The canonical baseline includes the existing four-locale source; if the previous deployment left a Vietnamese-only or other older source, this package does not authorize adding all missing locale/other changes. Stop and rebase the interaction delta onto the actually accepted Builder/canonical baseline within newly authorized scope.
6. Keep baseline/source drift, image URL normalization and identity metadata differences distinct. Map native LadiCDN images by element/alt/dimensions without changing them. Do not reuse the 2026-09-29 Fabless identity-pair exception for this new revision; unexpected metadata drift needs exact-revision evidence and authority. Stop on any unexplained difference.
7. Deliver each declared `after` span via the operator's `serve_builder_step.py <new-receipt> --baseline <baseline-artifact> --step <index> --port <owned-loopback-port>`. Start servers only during the newly authorized lifecycle. Verify the displayed SHA-256, exact visible CodeMirror selection and whole-source result after each bounded paste. Do not paste the whole HTML. The four changes are map-runtime insertion, dynamic-copy translations, inclusion of inspector options in locale translation, and the scoped locale refresh hook.
8. Save; observe completion, reopen and compare complete source. Confirm same page, then publish at the same URL. Do not retry uncertain live writes. Canonical main already contains the candidate: reconcile baseline → candidate with the helper and require exact current source identity; do not apply the same delta twice to main or copy live normalized HTML into Git.
9. Verify public desktop and 390px mobile: direct Progress/Lot/Cost tabs, corresponding diagrams and inspector, each pain card's matching view plus smooth scroll, mobile expansion, Arrow/Home/End and Enter/Space, RMA and Cost MCU controls. Check all four locales only if the preceding accepted deployment made them live. Confirm exactly two CTA IDs, existing PopupX opening without submitting a lead, GTM/bridge and existing section tracking, image rendering, no horizontal overflow and no new JS errors. Check `lang`, UTM and click-ID preservation. No new PageSpeed measurement is part of this repair.
10. Bind canonical commit/tree/blob/hash, Builder revision hash, public revision hash and the same semantic-delta hash in the new receipt. Only close as `COMPLETED` after all same-page, public and protected witnesses exist and the operator closeout validator passes. Update current docs with observed live truth; preserve historical logs. Keep publication status separate from GitHub push status.

## Protected state and acceptance

Markup, CSS, images and existing section IDs are unchanged by the committed repair. The canonical two CTA controls remain inert/provider-free; live PopupX SDK/adapter/bridge and GTM belong to the existing page and must survive unchanged. The section-awareness and mobile-toggle scripts are unchanged. No form, receiver, tag/container, campaign, lead or spend mutation is included.

Local evidence: `../../evidence/2026-09-30-fabless-local-interaction-repair.md`; browser interaction checks and tracking regression 12/12 already passed. Deployment is intentionally not attempted.

Terminal: `PREPARED_STOP_BEFORE_DEPLOY`. This is preparation success, not `EXISTING_PAGE_REVISION_PREFLIGHT_READY` or live acceptance.
