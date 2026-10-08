# Approved package v2 · snapshot-aware local main merge

Goal: adopt the PO-approved VI/zh-Hant package on local main, without replacing current project progress with the package fork snapshot.

Mandate: Bảo approved the result and requested merge main, first comparing progress against the worktree split and choosing the correct snapshot to avoid document mismatch. Necessary source checkpoint and local integration branch/worktree are included. No push or live action.

Baseline: package fork196f26b9 (2026-10-07T13:41:30+07:00); current mainc5e71913 (2026-10-08T10:18:21+07:00), six later commits. Main PartnerB22–B30 complete90PNG; FablessB13–B17 adopted55PNG, B18–B21 not run. Package remains the approved17VN/OSAT journeys/170PNG; it is not refreshed with later assets.

Plan: checkpoint approved locale changes → create integration branch from current main → merge package with normal ancestry → reconcile shared canonical docs against current main and label package's source clock → copy12ignoredprivate companion files locally → verify exact approved233file bundle, preserve existing main blobs outside bounded docs/config, links and fresh anchor binding → commit integration → advance clean main to reviewed descendant → verify actual main files and private-ignore state.

Critical criteria: all approved package files identical to PO-approved source; no existing main asset/evidence/frozen-policy blob changed; six newer commits retained in ancestry; current docs retain Partner/Fabless progress and show package source date, scope and PO approval; no account screenshot embedded HTML in Git; no unmerged entries, missing package links or unexpected staged paths; main stays local with no push. Historical receipts retain original verdicts/dates. Root SELF_REVIEW, no independent/native-market/live acceptance.

Audit target: preintegration main tree, approved233file manifest, merge parents/diff, shared-doc preservation and scoped notices, ignored companion hashes, actual main readback and navigation. Execution status is determined after verifying the final main state. Ordinary merge adds history; no reset/rebase/backdating or lost newer work. Integration/source refs preserve recovery points.
