# RMK → mobile case adapter: shared contract v1

2026-10-04 · Product Owner: Bảo · Baseline: `d163ce7e8040c763cd649c11cd14de3ee48bc204`.

This checkpoint establishes coordination, source bindings and two local worktrees. It does not deliver the remaining RMK creatives or a working/published LDP. Bảo authorized setup + local commit, followed by one read-only Sol/low continuity audit; stop before Corrective 1, even if that audit identifies defects. Audit acceptance remains pending at this checkpoint.

## One content source, two consumers

`contract.json` controls identity, routing, ownership, locale policy and lifecycle. `case-content.json` is the sole current case payload: exact accepted R4 Vietnamese copy plus separately identified internal claim invariants. `continuity-matrix.json` covers all eleven selected Cold treatments; actual copy, selected images, readers and acceptance receipts are pinned in `input-manifest.json`. It records baseline Git blob identity separately from Windows checkout SHA256 where existing autocrlf expands line endings; this is not a content change. `release-manifest.json` binds this pack's exact bytes; its scoped `.gitattributes` disables text conversion for these new shared files. A consumer must declare the release-manifest SHA256 and its own artifact hashes in its slice-owned binding. Matching a filename or revision string alone is insufficient.

Ad and LDP may use different layouts and lengths. Every factual statement in either presentation must reference a shared claim ID; neither consumer may broaden a claim or maintain an independent translation. The LDP writer may arrange approved text, add navigation and implement layout. New factual prose, case selection or translation goes through the shared content owner first. No internal match classification, uncertainty, gate status or governance wording enters customer copy. Source, market and publisher attribution remain visible naturally.

LDP is the primary proposed expand destination; PDF is optional and NOT_SELECTED. If later selected, generate it from the same approved locale payload and bind its version/hash to the pair. Do not create an independent PDF narrative or claim a downloadable resource exists before it does.

## Continuity is an evidence chain

Cold situation → remaining reader question → new named supplier evidence in RMK → the resource promised by the closing card → matching LDP case/context/solution/result → optional original publisher source.

Current R4 is accepted content for the previously scoped O1/O4-Q lane, with PR05 adjacent operations evidence and PR10 supplier identity. It is not a claim of abnormal-test investigation results. O3 is a candidate closer to the finance result, not automatically approved reuse. Other rows remain `PROOF_SELECTION_PENDING`. Missing suitable proof is a valid hold; never force case06 onto all rows. Content matching neither proves native audience eligibility nor that a member saw a specific Cold ad.

## Parallel workflow

1. Both worktrees start at the merge baseline and receive the containing contract checkpoint by local fast-forward after commit. `worktree-registry.json` identifies paths, branches and disjoint writable output areas; neither lane is activated for production by this setup.
2. Shared owner pins a row, chosen case/claims, precise closing promise, initial locale and contract release. Content can be drafted offline while account gates remain separate. RMK and LDP writers consume the same release and produce slice-owned bindings; interface work may use R4's existing VI payload. Other cases remain absent until selected.
3. RMK writer produces ad assets in its own namespace; LDP writer produces the mobile adapter in its own namespace. Neither modifies frozen inputs, shared contract/content, the other lane, harness rules or shared canonical docs.
4. Coordinator assembles the exact pair and audits source semantics, native image wording and actual rendered click/toggle/source behavior. A mechanical PASS alone does not close the pair. Only a revision-bound pair acceptance closes that row.
5. A shared change creates a NEW release ID and content hash, with affected row IDs and cause recorded. Owners receive a delta and explicitly update their bindings; no consumer silently follows a file called latest. Until both bind and the affected checks pass, the old accepted pair stays intact and the new pair stays unaccepted.

Shared Git changes, including consumer synchronization after this setup, require the applicable mandate; no blanket push/merge authority for future production is implied. Once branches contain independent work, never reset them to the owner branch or force a fast-forward. Coordinator reviews a bounded contract-only delta; branch divergence is resolved under a separately authorized integration action.

## What invalidates acceptance

Changes to cold input, case/proof, entity/market/product, numeric meaning, public copy, artwork, caption/native fields, CTA/promise, order, locale payload, destination or routing invalidate affected pair conclusions. A shared case change invalidates ALL entries using that case, including entries in different Cold cohorts. Changes to translations invalidate that locale; shared semantics invalidate every locale. Layout changes require affected render/accessibility/navigation checks. Update dependent PDFs too. Preserve old receipts and identify their now-superseded scope.

## Future pair acceptance (not executed here)

- Exact card click resolves the bound entry, case, release, locale and stable section; the first mobile view identifies the promised case/resource. Identity, context, solution scope, result and source are accessible without forced lead submission.
- Compare original native pixels, caption/native headline/alt/CTA, actual LDP text and source; verify every new fact and translation, not just identical numbers. For case06, retain China + exact entity + integrated solution + month-close 15→5 days + publisher attribution. No ERP-only causality, Vietnam semiconductor outcome or abnormal-test outcome.
- Observe 320, 390 and 414 px mobile plus desktop; switch across every READY locale at a mid-page section; preserve case/entry/release/section and synthetic UTM. Back/reload must retain URL-selected state. Unknown entry/case/release, conflicting routing fields and duplicate control parameters are rejected explicitly; never silently show a different case. Missing/invalid language may fall back explicitly to VI with a visible language indication; a missing translation is never mislabeled.
- Open the original source link and verify its actual public target/content before deployment. The current URL/locator is locally pinned prior evidence, not a new live observation. Do not promise a direct #case06 anchor unless observed; the collection link must show its exact searchable customer/locator nearby.
- A pair acceptance receipt pins contract manifest, both consumer bindings, every final artifact/hash, tested locale/URL/viewports, observations and auditor disposition. `PAIR_ACCEPTED_OFFLINE` is separate from deploy readiness, tracking readiness and live authorization.

## Reproduction and audit target

Run `python -B operations/linkedin-rmk-continuity-contract/verify_contract.py` from the repository. Add `--probes` for in-memory negative cases; add `--worktrees` after synchronizing the contract checkpoint to verify consumer identity, exact shared bytes and clean setup state. These are contract checks, not browser tests or semantic source verification. See `execution-contract.json` for AC1–AC8. The independent auditor must compare primary files and current-session authority, reconcile historical statuses, challenge the mechanism and return findings; it must not implement corrections.
