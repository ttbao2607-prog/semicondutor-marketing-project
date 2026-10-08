# Discovery424 recovery preparation — 08/10/2026

Steps1–3 requested by Bao are prepared in the dedicated Matched Audience worktree. Previous live recheck/R5 retry checkpoint **c5c38c93f1400f076a369c2b7c75920ac2d3b80a** is committed locally. This subsequent recovery preparation is **uncommitted local work**; no merge or push. Raw source/company rows, mapping tables and proposed CSV remain in the existing private evidence area outside Git.

## Result and limits

The 150 captured matched entries have unique joins to the current source using the full input projection, including city/domain/Page, rather than name alone. All93 unmatched entries have source-name candidates;64 uniquely match the current full projection,28 have an older/different projection and1 is ambiguous between duplicate rows. A ledger covers all424 source rows and separately accounts for the101 previously enriched rows.

| Current matched-entry classification | Count |
|---|---:|
| Correct entity with source evidence and fresh numeric-to-named Page redirect | 6 |
| Wrong entity confirmed by current Page readback and distinct entity evidence | 3 |
| Insufficient evidence for exact current entity mapping | 141 |

These are classification counts for150 captured platform entries, **not a source-row match rate or filtered campaign reach**. Correct identity does not establish ICP fit, decision authority, ERP need, locale or campaign eligibility. The source ledger records139 matched-only rows,55 unmatched-only,11 appearing in both,9 with only unresolved input-version candidates and210 not observed in these captures. Do not interpret the210 as unmatched, dropped or invalid. Platform aggregation/version coverage remains unresolved.

The six supported mappings retain existing accepted Page inputs; browser readback verified their numeric output URLs resolve to those named Pages. The two historical priority findings were re-evaluated: one wrong legal-services Page persists, while the earlier nonprofit output was replaced by a different apparel company, also now verified wrong. The third confirmed wrong pair is a separate manufacturing company. Evidence is row-bound in the private ledgers; historical findings were not blindly carried forward.

## Proposed correction

Prepared one **DRAFT_NOT_UPLOADED** CSV with424 rows and the original10-column LinkedIn template. Two rows change, three cells total: add two independently supported local company Pages and update one website to the official domain linked by its supported Page. The other422 rows remain identical to the current accepted source.

The check rereads the saved CSV and compares all eight protected columns to both the current source and immutable original: names, email domains, stock symbols, industries, cities, states, countries and postal codes are unchanged, preserving row order and duplicates. No parent/group Page, speculative domain, ICP deletion or arbitrary deduplication was introduced. Change log binds every changed cell to a specific source row and primary-source evidence.

| File binding | SHA256 |
|---|---|
| Current accepted424-row source | `69b9209e27baee4f4e527a686fd2497836bb7b7f1dfdcdcc6c5cc45648ae3e0c` |
| Proposed424-row CSV,27808bytes | `2d34fb975c20ec30ab769b8ebcb217a9e8806c159767106bc975d7170e304fe5` |

The original two priority companies still lack verified exact local replacement Pages. They remain unchanged and flagged. The proposal does not claim to fix all wrong/unknown mappings or guarantee LinkedIn will use the new identifiers.

## Acceptance and next checkpoint

Execution **SUCCESS for internal steps1–3 preparation**: source reconciliation, explicit classification and a source-bound proposal/change log exist. Recovery overall **PARTIAL**, audience **CHANGES_REQUIRED**, upload/readiness **HOLD**. Structural checks **PASS_SELF_CHECK**. Actual identity review is root self-review; independent audit **NOT_RUN**. [Sanitized evidence/validation](evidence.json) and [fresh anchor scope review](anchor-review.md) describe the proof and gaps.

Next recovery work: resolve exact local Pages for the two priority companies; adjudicate the remaining141 output pairs with source evidence; reconcile duplicate/version/unobserved source coverage. Any later Discovery upload is a separate operational step, followed by fresh mapping readback. No upload, campaign attachment/setting/save/enable/spend or Support message occurred in this preparation.

R5 remains at its completed retry checkpoint; proposed read-only recheck09Oct>=14:25 +07 is not scheduled. Support only if settled retry still fails, per Bao. Master203 observations unchanged.

DOCS_IMPACT_MAP reviewed. Seven affected canonical/owned entrypoints receive a current preparation notice; dated receipts and capture-time statements remain historical. Budget, creatives, frozen core and DEVELOPING/NOT_FROZEN locale adapter state unchanged.
