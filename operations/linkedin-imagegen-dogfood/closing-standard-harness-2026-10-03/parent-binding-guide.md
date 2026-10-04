# Parent binding guide — drafts only

Checkpoint3587fe740988a8ef50fe5df96b7231daea574add exists locally before dogfood. Writer does not author review/release/spec. Read dogfood-preparation-manifest.json for four contract hashes, exact copy refs, draft paths and reviewed release subsets. Independently review full5 source/public fields and reference roles; release campaign A1–A4, closing A5 ONLY. Spec calls must be byte-equivalent to calls-draft calls. Spec reference keys release/contract/copy/review must be the independent release bindings; supplied release SHA comes from coordinator trust, never spec self-discovery.

Suggested parent-only records: operator/f2/{campaign,closing}/ and operator/o1/{campaign,closing}/, each review.json/release.json/spec.json. Draft revision can become spec revision; retain calls and prompt UTF8 sha exactly. Per selected pending call, run from repo:

```powershell
python -B scripts/verify_imagegen_preflight.py preflight --root . --release <parent-release-path> --release-sha256 <independently-supplied-pin> --spec <parent-spec-path> --call-id F2_A5 --output <parent-preflight-path>
python -B scripts/verify_imagegen_preflight.py dispatch-check --root . --release <parent-release-path> --release-sha256 <independently-supplied-pin> --spec <parent-spec-path> --receipt <parent-preflight-path> --dispatch <parent-planned-dispatch-path> --output <parent-dispatch-check-path>
```

F2_A5/O1_A5 are closing call IDs; F2_A1…A4/O1_A1…A4 campaign calls. Planned dispatch exactly selected prompt, prompt_sha256, reference_paths in reviewed order, output_path and receipt SHA; singleton native targets in sol/{f2,o1}/native. Root is sole image operator. After actual native, parent native-output-check uses fresh bindings plus --call-id and records container/dimensions/hash only, then independently decodes/visually audits.

Only after five selected originals exist and root releases viewer build:

```powershell
python -B operations/linkedin-imagegen-dogfood/closing-standard-harness-2026-10-03/sol/f2/build_preview.py
python -B operations/linkedin-imagegen-dogfood/closing-standard-harness-2026-10-03/sol/o1/build_preview.py
```

Clean seven-file bundles are outputs/closing-standard-f2 and outputs/closing-standard-o1. Exact raw copy projection + manifest remain sol/{case}/ outside bundle. Builder refuses existing populated output, keeps native/official logo bytes, renders caption/native headline/alt/CTA from exact public copy and destination from immutable source metadata. Parent viewer-check and actual desktop/mobile allpositions/nav/story checks remain required. No generation or viewer build was executed by preparation writer.
