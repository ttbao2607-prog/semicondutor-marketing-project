# LinkedIn ImageGen harness v1 — implementation record

**Local checkpoint status (2026-10-03):** `testing_dogfood`. Bảo authorized the containing local checkpoint; no push, merge or history rewrite is authorized. Bounded implementation is `SUCCESS`, 35 synthetic tests passed and Sol corrected-implementation audit is `AUDIT_PASS`. Real candidate: `NOT_RUN`; no real generation has been released. Current status is saved in `operations/LinkedIn_ImageGen_Harness_Status.json`; proposed one-call F2-A2 run and post-run result rules are in `operations/LinkedIn_ImageGen_First_Candidate_Dogfood_Plan.md`. This addendum supersedes earlier uncommitted/pending-implementation status only. Historical receipts remain intact; one non-closing candidate cannot establish set diversity, full-carousel quality or Taiwan closing-source readability.

2026-10-03 · Repo-internal evidence. Current execution status: `SUCCESS` for bounded implementation and synthetic fixture checks. Corrected implementation independently reviewed by Sol: `AUDIT_PASS`, revision hashes below. No real ImageGen call, actual tool dispatch, new native image, rendered export or creative/content/live acceptance is claimed.

## Authority and acceptance

Bảo authorized implementation after the Sol blind plan review returned `AUDIT_PASS`. The released scope is the small contract-bound gate, corresponding schema/visual instructions and meaningful fixture checks. No provider/API/framework, scheduler or image transformation is added. Git staging/commit/push and a real-asset pilot remain unreleased.

Required outcomes: validate against separately supplied contract/copy/review/mandate pins; exact campaign-declared coverage/reuse/count and approved text/reference identities; independent first mention per ad/delivery surface; advisory repetition without keyword rejection; fresh pre-dispatch binding; public-copy projection excluding internal payload; preserve frozen assets, native-image review obligations and PO release boundaries. Audit target is the code, tests, schema and canonical-doc diff compared with those outcomes and the step-1 design.

## Implementation

- `scripts/verify_imagegen_preflight.py`: standard-library-only `preflight`, `dispatch-check` and `viewer-check`. Fresh checks fail closed on malformed/unknown JSON fields, duplicate keys, mutated pins, missing or mismatched review coverage, unauthorized calls/reuse/text/references, stale receipts and changed proposed arguments. New receipts cannot overwrite inputs/artwork or hash themselves.
- `operations/LinkedIn_ImageGen_Preflight_Schema.md`: exact v1 formats, independent trust boundary, command usage and mechanical-versus-human expectations.
- `operations/LinkedIn_ImageGen_Visual_Instructions.md`: retained brand/source/content discipline with per-card concepts and explicit style-reference roles; no inherited fixed scene, proportions, folders or skyline.
- `tests/test_imagegen_preflight.py`: synthetic fixture source/copy/review/mandate objects under repo-local temporary directories, automatically removed. `FIXTURE_ONLY` is explicit and every successful result retains `NO_GENERATION_AUTHORITY`.

## Observed verification

Initial `python -B tests/test_imagegen_preflight.py` verification: **31 tests passed**. Coverage included four-call and eight-call reviewed contracts; exact grouping, shared-field reuse and target/output uniqueness; varied/diagram concepts; homogeneous concepts mechanically passing with repetition advisory and unproven creative quality; reference-label leakage; trusted-release substitution, changed contract/source/reference/review/spec and stale dispatch arguments; all OSAT/Fabless/WIP first mentions per A/B and independent surfaces; later-definition and omitted-field bypasses; ERP/MES exemption; visible text length/dashes; internal copy keys and hidden/metadata/attachment serialization; exact Taiwan/source attribution retained in viewer JSON; duplicate JSON keys, path escape, protected outputs and CLI receipt boundary. This initial pass did not cover the two audit counterexamples below.

Fixtures exercise mechanical behavior only. An intentionally flawed synthetic review of caution-contaminated copy cannot receive semantic or creative PASS from this gate; it yields an editorial advisory and `NOT_ASSESSED` semantics. Named source/editorial reviewers remain responsible for refusing such a real review and downstream handoff. Finished native images and HTML/PDF exports have not been produced or inspected in this milestone.

`git diff --check` is clean. The frozen AD-ED-01 file is unchanged at SHA-256 `a045be594186b09c1e60fa41b276ac4ccdd4a9a20873d89f2ae738d4088c61e0`. No source-copy/native/demo under `operations/linkedin-awareness-execution/`, asset, old fixture, landing, account or remote is changed. HEAD remains `5f367dd580f501f0b5504c7a6afa0726bc1b0a6e`; all implementation/design/doc work is local and uncommitted, with no staged files. GitHub live state was not refreshed by fetch.

## Limits and next gate

This script checks proposed inputs and a structured public-copy payload. It does not call ImageGen or prove a tool invocation, inspect arbitrary final HTML/PDF or native-image pixels, certify source support, enforce filesystem permissions against a malicious coordinator, or accept creative quality/brand fidelity. POSTGEN still requires original-byte provenance/hash/dimension/manifest reconciliation and actual native/contact-sheet/desktop/mobile/export review after a separately authorized asset exists.

The proposed F2/P3 pilot remains at most four non-closing images with no correction reserve unless separately released. It cannot close Taiwan closing-source readability, full-carousel transitions or whole-set quality. Implementing/passing this harness does not turn prior failed frozen images into accepted content.

Docs impact reviewed: current entry/readiness/build/execution/review/inventory docs are updated for implementation scope. The pinned editorial gate and historical records stay intact. Strategy, S02/S03, proof/source inventory, rights, targeting and governance approvals are unchanged; no new canonical claim or content acceptance is introduced.

## Independent first-pass audit and reconciled corrections

Sol returned `AUDIT_FAIL` against gate SHA-256 `4cebfa0cd6963e086233dc75f803206083c9df46ce10be0268c4a1350c8cee4b` / test SHA-256 `54900ee98c9bd544b9b851276f9a84ffd8141de723425810e1bbe07add729707`, with two reproduced findings. Parent separately reproduced both in cleaned synthetic directories before accepting them. No other supported material finding was reported.

- **P1, sequential lifecycle:** initial code rejected any existing output across the whole batch during subsequent dispatch/viewer checks. Saving dummy bytes at only the first target caused both an exact second-call check and exact public-copy check to fail. Correction separates input integrity from output protection; fresh selected-call preflight/dispatch protect that call and allow completed siblings; viewer-copy checks retain input integrity without requiring absent outputs. Initial whole-batch preflight still refuses existing outputs. Selected-call scope is recorded and cannot be reused for a different call.
- **P2, CJK first-mention detection:** Unicode word boundaries missed `OSAT业务`, `Fabless业务` and `WIP业务`. Correction recognizes Latin identifier boundaries independently of surrounding CJK characters. Regression subcases cover zh-Hans/zh-Hant, captions/cards, Chinese prefix/suffix, case-insensitive explained forms and unexplained-first/later-definition forms. Longer Latin identifiers are not mistaken for the standalone terms. A/B independence and ERP/MES exception remain intact.

Corrected verification: **35 tests passed**, including all prior checks plus sequential second-call/post-output viewer checks, existing-selected-output rejection, fresh selected-call scope binding, CJK first occurrences and Latin-substring handling. Synthetic files are dummy bytes/fixtures, not generated images or human creative evidence. Independent corrected-revision audit remains pending.

## Corrected-revision independent audit closeout

Sol returned **`AUDIT_PASS` for the corrected bounded implementation** after running the 35-test suite and additional independent counterexamples. Reviewed gate SHA-256: `2b4c7666887fe2d8c3973fb79ac6a3379b0cbba375c9c82fd92fac0553c690f7`. Reviewed tests SHA-256: `86c0110b04ce84746c84d0e03fb1344ed0937e2c72a3e87cf5b1a32062e02b15`. This closes the pending re-audit statement above for this exact code revision; the first-pass failure remains historical evidence.

Observed independent closure:

- All four synthetic calls were checked sequentially, with dummy completed bytes created after each check. Subsequent pending calls passed; repeating each completed call failed with selected-output overwrite protection. Exact public copy passed after all outputs existed; changing the pinned source then failed that viewer check, confirming freshness remained active.
- Original unexplained OSAT/Fabless/WIP counterexamples failed under both zh-Hans and zh-Hant. Lowercase explained terms with adjacent Chinese prefix/suffix passed. Caption/card, later-definition and Latin-identifier regressions passed in the test suite.
- Selected-call scope, trusted approval/review/source/reference/prompt binding, campaign-specific coverage/reuse, viewer/internal projection and mechanical-versus-human boundaries remained active. No remaining supported material finding was reported.

Parent reconciliation: both first-pass findings were independently reproduced before correction; changed implementation follows their bounded fixes; final code/test hashes match the reviewed revision; targeted selected-call CLI check passed with a completed sibling. No finding was accepted as automatic mutation authority or simulated human creative approval. Documentation/status-only closeout after this audit does not change the audited code/test hashes.

Final scope result: implemented input gate, corresponding schema/visual instructions and synthetic mechanical checks complete. No native image, actual dispatch, arbitrary rendered export or buyer/creative/brand/readability evidence is established. A real-asset pilot remains separately unreleased. All changes remain local and uncommitted; no staging, GitHub push or merge occurred.
