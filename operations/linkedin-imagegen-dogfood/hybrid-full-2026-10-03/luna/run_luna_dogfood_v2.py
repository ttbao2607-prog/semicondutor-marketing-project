"""Run Luna v2 candidate-specific verifier dogfood in disposable, isolated fixture roots."""
from pathlib import Path
from datetime import datetime, timezone
import copy
import hashlib
import importlib.util
import json
import shutil
import tempfile

ROOT = Path("D:/linkedin-awareness-harness-redesign").resolve()
BASE = "operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03"
OWN = (ROOT / BASE / "luna").resolve()
RELEASE = BASE + "/operator/luna-v2/release.json"
SPEC = BASE + "/operator/luna-v2/spec.json"
RELEASE_PIN = "6ea05caa8c4c82f353ccad219dfff87f54bcaad586b3647557d5846436f772ef"
CALL_ID = "F2_A1"
RECEIPT = "fixture-only/preflight.json"
DISPATCH = "fixture-only/planned-dispatch.json"
VIEWER = "fixture-only/viewer.json"
RESULT_PATH = OWN / "dogfood-results-v2.json"
HELPER_PATH = OWN / "run_luna_dogfood_v2.py"
created_roots = []
removed_roots = []

def digest_bytes(data):
    return hashlib.sha256(data).hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))

def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))

def fixture_module():
    verifier = ROOT / "scripts/verify_imagegen_preflight.py"
    spec = importlib.util.spec_from_file_location("luna_v2_preflight_gate", verifier)
    gate = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gate)
    return gate

def main():
    if not OWN.is_dir() or OWN.is_symlink():
        raise RuntimeError("Owned Luna directory missing or is a symlink")
    if RESULT_PATH.exists():
        raise RuntimeError("dogfood-results-v2.json already exists; refusing to overwrite")
    started = datetime.now(timezone.utc)
    gate = fixture_module()

    release_real_path = ROOT / RELEASE
    spec_real_path = ROOT / SPEC
    release_raw = release_real_path.read_bytes()
    if digest_bytes(release_raw) != RELEASE_PIN:
        raise RuntimeError("Parent-supplied release pin does not match current release bytes")
    release = load_json(release_real_path)
    spec_real = load_json(spec_real_path)
    contract = load_json(ROOT / release["contract"]["path"])
    if spec_real["release"] != {"path": RELEASE, "sha256": RELEASE_PIN, "revision": release["revision"]}:
        raise RuntimeError("Candidate spec release binding differs from the parent-supplied release identity")

    # Clone only files validated by the real offline gate. Real candidate outputs are excluded.
    input_paths = {
        RELEASE,
        SPEC,
        release["authority_ref"]["path"],
        release["contract"]["path"],
        release["copy"]["path"],
        release["review"]["path"],
    }
    input_paths.update(ref["path"] for ref in contract["sources"])
    input_paths.update(ref["path"] for ref in contract["references"])
    input_paths = sorted(input_paths)
    real_input_hashes_before = {p: digest_bytes((ROOT / p).read_bytes()) for p in input_paths}
    gate_rel = "scripts/verify_imagegen_preflight.py"
    gate_hash_before = digest_bytes((ROOT / gate_rel).read_bytes())
    call = next(c for c in spec_real["calls"] if c["call_id"] == CALL_ID)
    if len(call["references"]) != 5:
        raise RuntimeError("Selected real call is not bound to the reviewed five-reference list")
    real_native_paths = [c["output_path"] for c in spec_real["calls"]]
    if any(Path(p).is_absolute() for p in real_native_paths):
        raise RuntimeError("Candidate spec contains an unexpected absolute output path")

    cases = []
    positives = []

    def safe_cleanup(root):
        root = Path(root).resolve()
        if root.is_symlink() or root.parent != OWN or not root.name.startswith("fixture-only-luna-v2-"):
            raise RuntimeError(f"Refusing cleanup outside verified fixture child: {root}")
        if root.exists():
            shutil.rmtree(root)
        if root.exists():
            raise RuntimeError(f"Fixture root remained after cleanup: {root}")
        removed_roots.append(str(root.relative_to(ROOT)).replace("\\", "/"))

    def setup_fixture():
        fixture = Path(tempfile.mkdtemp(prefix="fixture-only-luna-v2-", dir=str(OWN))).resolve()
        if fixture.parent != OWN or fixture.is_symlink() or not fixture.is_relative_to(OWN):
            raise RuntimeError(f"New fixture root escaped owned namespace: {fixture}")
        created_roots.append(str(fixture.relative_to(ROOT)).replace("\\", "/"))
        try:
            for rel in input_paths:
                source = ROOT / rel
                target = fixture / rel
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_bytes(source.read_bytes())
            fixture_spec = load_json(fixture / SPEC)
            fixture_release = load_json(fixture / RELEASE)
            # Fresh authentic preflight receipt, with pending output paths absent in this fixture.
            preflight, _ = gate.validate(fixture, RELEASE, RELEASE_PIN, SPEC, scope_call_id=CALL_ID)
            write_json(fixture / RECEIPT, preflight)
            selected = next(c for c in fixture_spec["calls"] if c["call_id"] == CALL_ID)
            proposal = {
                "schema_version": 1,
                "record_kind": "PLANNED_DISPATCH_CHECK",
                "call_id": CALL_ID,
                "preflight_sha256": digest_bytes((fixture / RECEIPT).read_bytes()),
                "prompt": selected["prompt"],
                "prompt_sha256": selected["prompt_sha256"],
                "reference_paths": [ref["path"] for ref in selected["references"]],
                "output_path": selected["output_path"],
            }
            write_json(fixture / DISPATCH, proposal)
            (fixture / VIEWER).parent.mkdir(parents=True, exist_ok=True)
            (fixture / VIEWER).write_bytes((fixture / fixture_release["copy"]["path"]).read_bytes())
            return fixture
        except Exception:
            safe_cleanup(fixture)
            raise

    def check(fixture, mode):
        if mode == "preflight":
            return gate.validate(fixture, RELEASE, RELEASE_PIN, SPEC, scope_call_id=CALL_ID)[0]
        if mode == "dispatch":
            return gate.dispatch_check(fixture, RELEASE, RELEASE_PIN, SPEC, RECEIPT, DISPATCH)[0]
        if mode == "viewer":
            return gate.viewer_check(fixture, RELEASE, RELEASE_PIN, SPEC, VIEWER)[0]
        raise ValueError(mode)

    def run_positive_checks():
        fixture = setup_fixture()
        try:
            for mode in ("preflight", "dispatch", "viewer"):
                result = check(fixture, mode)
                observed = result.get("mechanical_verdict")
                matched = observed == "PASS"
                positives.append({
                    "check": mode,
                    "expected": "PASS",
                    "observed": observed,
                    "matched_expectation": matched,
                    "scope": "ISOLATED_FIXTURE_CLONE_OF_PARENT_BOUND_INPUTS",
                    "actual_dispatch_observed": result.get("actual_dispatch_observed", False),
                    "error": None,
                })
        finally:
            safe_cleanup(fixture)

    def json_mutation(rel, fn):
        def mutate(fixture):
            target = fixture / rel
            value = load_json(target)
            fn(value)
            write_json(target, value)
        return mutate

    def bytes_mutation(rel):
        def mutate(fixture):
            target = fixture / rel
            target.write_bytes(target.read_bytes() + b" ")
        return mutate

    def substituted_release(fixture):
        target = fixture / RELEASE
        value = load_json(target)
        value["revision"] = "fixture-substituted-release"
        write_json(target, value)

    def occupied_output(fixture):
        target = fixture / call["output_path"]
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(b"fixture-only occupied selected output")

    def record_case(name, mode, mutation):
        fixture = setup_fixture()
        try:
            mutation(fixture)
            try:
                result = check(fixture, mode)
                observed = "ACCEPTED"
                error = None
                gate_verdict = result.get("mechanical_verdict")
            except (gate.Invalid, OSError, TypeError, KeyError, AttributeError, ValueError) as exc:
                observed = "REJECTED"
                error = str(exc)
                gate_verdict = "FAIL"
            cases.append({
                "case": name,
                "mode": mode,
                "expected": "REJECTED",
                "observed": observed,
                "matched_expectation": observed == "REJECTED",
                "gate_verdict": gate_verdict,
                "error": error,
                "scope": "ISOLATED_FIXTURE_ONLY",
                "fixture_native_outputs_copied": False,
            })
        finally:
            safe_cleanup(fixture)

    run_positive_checks()

    record_case("changed contract groups", "preflight",
                json_mutation(release["contract"]["path"], lambda v: v["groups"].pop()))
    record_case("changed contract campaign style", "preflight",
                json_mutation(release["contract"]["path"],
                              lambda v: v["style"]["campaign"].update(instructions="altered fixture visual grammar")))
    record_case("changed copy bytes", "preflight", bytes_mutation(release["copy"]["path"]))
    record_case("changed review bytes", "preflight", bytes_mutation(release["review"]["path"]))
    record_case("substituted release against parent-supplied pin", "preflight", substituted_release)
    record_case("changed source bytes", "preflight", bytes_mutation(contract["sources"][0]["path"]))
    record_case("changed reference bytes", "preflight", bytes_mutation(contract["references"][0]["path"]))
    record_case("changed assembled prompt", "preflight",
                json_mutation(SPEC, lambda v: v["calls"][0].update(prompt=v["calls"][0]["prompt"] + " fixture edit")))
    record_case("stale receipt after spec change", "dispatch",
                json_mutation(SPEC, lambda v: v.update(revision=v["revision"] + "-fixture-change")))
    record_case("changed dispatch prompt", "dispatch",
                json_mutation(DISPATCH, lambda v: v.update(prompt=v["prompt"] + " fixture edit")))
    record_case("changed dispatch reference list", "dispatch",
                json_mutation(DISPATCH, lambda v: v.update(reference_paths=list(reversed(v["reference_paths"])))))
    record_case("changed dispatch receipt SHA256", "dispatch",
                json_mutation(DISPATCH, lambda v: v.update(preflight_sha256="0" * 64)))
    record_case("occupied selected output at preflight", "preflight", occupied_output)
    record_case("occupied selected output at dispatch", "dispatch", occupied_output)
    record_case("viewer added internal notes", "viewer",
                json_mutation(VIEWER, lambda v: v.update(internal_notes="fixture-only hidden note")))
    record_case("viewer added metadata", "viewer",
                json_mutation(VIEWER, lambda v: v.update(metadata={"review": "fixture-only"})))
    record_case("viewer added hidden payload", "viewer",
                json_mutation(VIEWER, lambda v: v.update(hidden_html="<div hidden>fixture-only</div>")))
    record_case("viewer added attachments", "viewer",
                json_mutation(VIEWER, lambda v: v.update(attachments=["fixture-only-review.json"])))
    record_case("viewer changed approved headline", "viewer",
                json_mutation(VIEWER,
                              lambda v: v["ads"][0]["cards"][0].update(headline="fixture altered headline")))

    real_input_hashes_after = {p: digest_bytes((ROOT / p).read_bytes()) for p in input_paths}
    gate_hash_after = digest_bytes((ROOT / gate_rel).read_bytes())
    parent_inputs_unchanged = real_input_hashes_before == real_input_hashes_after
    helper_and_gate_unchanged = gate_hash_before == gate_hash_after
    all_rejected = len(cases) == 19 and all(case["matched_expectation"] for case in cases)
    all_positive = len(positives) == 3 and all(check["matched_expectation"] for check in positives)
    cleanup_complete = len(created_roots) == len(removed_roots) and all(not (ROOT / p).exists() for p in created_roots)
    end = datetime.now(timezone.utc)
    report = {
        "schema_version": 1,
        "record_kind": "ISOLATED_CANDIDATE_DOGFOOD_V2",
        "stage_result": (
            "MECHANICAL_DOGFOOD_COMPLETE_FOR_PARENT_AUDIT"
            if all_rejected and all_positive and parent_inputs_unchanged and helper_and_gate_unchanged and cleanup_complete
            else "DOGFOOD_FINDING_REQUIRES_PARENT_REVIEW"
        ),
        "start_utc": started.isoformat().replace("+00:00", "Z"),
        "end_utc": end.isoformat().replace("+00:00", "Z"),
        "elapsed_seconds": round((end - started).total_seconds(), 3),
        "parent_supplied_release_path": RELEASE,
        "parent_supplied_release_sha256": RELEASE_PIN,
        "actual_release_sha256_before": digest_bytes(release_raw),
        "selected_fixture_call": CALL_ID,
        "positive_checks": positives,
        "negative_cases": cases,
        "negative_case_count": len(cases),
        "all_expected_rejections_observed": all_rejected,
        "all_positive_baseline_checks_passed": all_positive,
        "input_hashes_before": real_input_hashes_before,
        "input_hashes_after": real_input_hashes_after,
        "parent_bound_real_inputs_unchanged": parent_inputs_unchanged,
        "preflight_helper_sha256_before": gate_hash_before,
        "preflight_helper_sha256_after": gate_hash_after,
        "preflight_helper_unchanged": helper_and_gate_unchanged,
        "temporary_roots_created": created_roots,
        "temporary_roots_removed": removed_roots,
        "temporary_cleanup_complete": cleanup_complete,
        "real_native_output_paths_from_spec": real_native_paths,
        "real_native_outputs_read_or_copied": False,
        "actual_dispatch_observed": False,
        "image_generation_calls": 0,
        "parent_review_release_spec_or_candidate_pin_mutated": False,
        "parent_runtime_admission": {
            "requested_model": "gpt-6-luna",
            "requested_reasoning_effort": "max",
            "parent_reported_effective_model": "gpt-6-luna",
            "parent_reported_effective_reasoning_effort": "max",
            "leaf_independent_runtime_introspection": False,
            "note": "Parent said runtime acceptance was correct at max and will independently re-gate after this turn.",
        },
        "semantic_verdict": "NOT_ASSESSED_BY_THIS_MECHANICAL_DOGFOOD",
        "creative_verdict": "INSUFFICIENT_EVIDENCE",
        "scope_note": "Only isolated fixture inputs were mutated. Fixture clones included the release/spec and the minimum gate-validated authority, contract, copy, review, source, and reference bytes. No real native output was opened, copied, changed, or used as a fixture.",
        "helper_path": str(HELPER_PATH.relative_to(ROOT)).replace("\\", "/"),
        "results_path": str(RESULT_PATH.relative_to(ROOT)).replace("\\", "/"),
    }
    write_json(RESULT_PATH, report)
    print(json.dumps({
        "stage_result": report["stage_result"],
        "positive_checks": len(positives),
        "positive_passes": all_positive,
        "negative_cases": len(cases),
        "expected_rejections": all_rejected,
        "real_inputs_unchanged": parent_inputs_unchanged,
        "gate_unchanged": helper_and_gate_unchanged,
        "fixtures_removed": cleanup_complete,
        "errors": [{"case": c["case"], "observed": c["observed"], "error": c["error"]} for c in cases],
        "result_path": report["results_path"],
    }, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()

