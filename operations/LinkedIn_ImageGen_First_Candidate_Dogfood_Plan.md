# First candidate and dogfood plan

2026-10-03 · Repo-internal plan. Current lifecycle status: `testing_dogfood`; actual candidate result: `NOT_RUN`. Bảo authorized a local checkpoint and this plan. Generation is proposed, not yet released. This plan does not act as a trusted release or review attestation.

## Outcome and bounded scope

Produce one Vietnamese F2-A2 non-closing candidate that helps the reader understand which product, planning period and related lots to compare when a forecast changes. Test whether the redesigned harness can carry reviewed input through a real native image and a clean viewer preview without losing content discipline. Proposed allowance: one base ImageGen call, zero correction calls. Stop after review; no automatic batch expansion.

The starting copy is F2-A2 at frozen commit `1f476c31de4f8a7cfbcf5b5b8842fd35a2e7390f`, path `operations/linkedin-awareness-execution/f2-forecast-imagegen-r1/copy-vi.json`. The original set remains intact. Headline: “Bắt đầu từ sản phẩm và kỳ kế hoạch”. Body: “Khi dự báo thay đổi, nhóm đối chiếu sản phẩm, kỳ kế hoạch và các lô liên quan trước khi trao đổi với đối tác.” Native headline: “Khoanh phạm vi cần đối chiếu”. The approved caption/context must accompany the preview so the audience and first mentions are understandable.

Proposed visual direction: make the relationship between product, planning period and related lots clear. Do not inherit mandatory paper/calendar/chip-tray composition. Any diagram wording is proposed copy and must be reviewed before use; no fabricated identifiers, dates, metrics or results. The old alt text describes old props: replace it with reviewed, locale-matched text that accurately describes the new concept, then reconcile it with the actual image before viewer handoff. Count actual text rather than trusting old length metadata.

## Before the single call

1. Prepare a new sibling candidate revision with freshly pinned source, copy, style/brand assets and contract. Do not copy old receipts as current authority. Review the source/copy and any new labels; pin the exact review independently of the call spec. Resolve findings before dispatch. Independently audit the real candidate inputs against the schema and retained/removed-check mapping.
2. Check the real inputs and the exact proposed call, with expected card coverage, approved words, reference roles and output destination. A fresh dispatch check must still match the reviewed versions. A mechanical pass does not grant generation authority; record Bảo's separate one-call release before invoking ImageGen.
3. Dogfood failure cases against isolated copies: changed contract/copy/review/source/reference; changed prompt; stale receipt; already occupied selected output; omitted/extra viewer wording. Each must fail the mechanical gate. Do not mutate approved originals.
4. Preserve the existing fixture expectations: homogeneous concepts can mechanically pass and receive an advisory; text-only creative review is `INSUFFICIENT_EVIDENCE`; homogeneous actual images fail human creative review. First mention is independent per A/B and per delivery surface, including CJK-adjacent OSAT/Fabless/WIP; ERP/MES remain exempt. Synthetic coverage has already passed in 35 tests; rerun only if code changes or candidate evidence reveals a new concern.

## After the call, if separately released

Save the actual tool invocation and original image provenance, hash, dimensions and output mapping in the repo. A planned-dispatch check is not evidence of an actual call. Preserve native image bytes; no post-processing to repair wording or branding. If the tool fails or the image fails review, stop with evidence; zero correction reserve means no automatic retry or edit.

Dogfood the native image for exact visible wording/labels, readable text, accurate logo, story fit and useful visual hierarchy. Inspect the actual preview on desktop and mobile, including the caption and alt text. Verify viewer-copy projection and inspect the complete delivered HTML/metadata/hidden data/attachments so internal receipts, proof classification and agent caveats do not leak. Preserve truthful case/market/source attribution; narrow unsupported claims instead of adding internal disclaimers.

An independent reviewer checks the real inputs, invocation evidence and delivered candidate; Bảo decides whether this specific card communicates the intended idea. Use the frozen repetitive imagery only as an internal negative comparison, never as an accepted creative baseline. One image can demonstrate story fit but cannot prove diversity across a new set. A later contrasting candidate needs its own bounded release. This pilot does not test Taiwan closing-source readability, full-carousel transitions, whole-set quality or live delivery.

## Status to record after actual execution

The harness lifecycle stays `testing_dogfood` throughout this bounded trial. The candidate result is separate:

| Observed outcome | Candidate result | Next action |
|---|---|---|
| Current state, no actual call | `NOT_RUN` | Prepare and audit the real inputs; obtain the separate one-call release |
| Actual image and scoped dogfood checks pass; independent review complete | `READY_FOR_PO_REVIEW` | Show Bảo the exact candidate and evidence |
| Wording, branding, readability, story fit or viewer leakage fails | `CHANGES_REQUIRED` | Record the finding; stop; prepare a bounded correction proposal |
| Tool fails or required evidence is missing | `BLOCKED` / `INSUFFICIENT_EVIDENCE` | Record the cause and missing evidence; do not claim a pass |
| Bảo accepts the specific candidate for testing | `CANDIDATE_ACCEPTED_FOR_TESTING` | Propose the next contrasting candidate; no whole-harness or live promotion |

Record observed results, reviewer and decision, actual call count and unresolved findings in a new dated repo receipt; update the status JSON and canonical entry docs. Never convert a planned result into an observed result. Reviewer acceptance does not substitute for Bảo's content decision.

## Plan review evidence

Sol independent read-only review on 2026-10-03 returned `AUDIT_PASS`, no material finding. The reviewer confirmed the F2-A2 wording against frozen source bytes, fresh independent bindings, one-call/zero-correction boundary, viewer/internal separation and evidence-dependent post-run status. Parent verified the unchanged audited code/test hashes and the current staged checkpoint scope. This plan review is not the real candidate's source-copy attestation and does not release generation.
