"""Synthetic repo-local fixtures. No ImageGen, renderer, source/copy or raster acceptance."""
import copy
import importlib.util
import io
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stdout, redirect_stderr

ROOT = Path(__file__).resolve().parents[1]
module_spec = importlib.util.spec_from_file_location("imagegen_gate", ROOT / "scripts/verify_imagegen_preflight.py")
gate = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(gate)


class Fixture:
    def __init__(self, root, full=False):
        self.root = root
        self.prefix = "fixture"
        self.put("source.txt", "SYNTHETIC SOURCE: no customer or capability evidence.")
        self.put("authority.txt", "SYNTHETIC FIXTURE ONLY: no generation release.")
        self.put("palette.dat", "synthetic palette bytes")
        self.copy = {"schema_version": 1, "revision": "fixture-copy-v1", "ads": []}
        definitions = {"OSAT": "dịch vụ đóng gói và kiểm thử bán dẫn thuê ngoài", "Fabless": "doanh nghiệp thiết kế chip", "WIP": "sản phẩm đang trong quá trình sản xuất"}
        count = 5 if full else 2
        for aid in ("A", "B"):
            cards = []
            for i in range(1, count + 1):
                cards.append({"card_id": aid + str(i), "headline": f"Câu hỏi {i}", "body": "ERP và MES có ý nghĩa riêng.", "source_text": "Nguồn tổng hợp tại Đài Loan", "cta": "Đọc thêm", "native_headline": f"Dữ liệu cho câu hỏi {i}", "alt": f"Mối liên hệ dữ liệu {i}", "artwork_labels": ["Lô", "Thời điểm"]})
            self.copy["ads"].append({"ad_id": aid, "caption": "OSAT (" + definitions["OSAT"] + ") và ERP/MES.", "cards": cards})
        groups = [["A1", "B1"], ["A5", "B5"], ["A2"], ["A3"], ["A4"], ["B2"], ["B3"], ["B4"]] if full else [["A1"], ["A2"], ["B1"], ["B2"]]
        refs = [{**self.ref("palette.dat", "palette-v1"), "role": "palette", "attributes": ["colors"]}]
        self.contract = {"schema_version": 1, "revision": "fixture-contract-v1", "locale": "vi", "channel": "linkedin-carousel", "copy": None,
                         "sources": [self.ref("source.txt", "source-v1")], "card_sources": {}, "ad_order": ["A", "B"], "card_order": {}, "surfaces": {}, "definitions": definitions,
                         "limits": {f: 500 for f in ("caption",) + gate.CARD_FIELDS}, "groups": groups, "reuse_fields": list(gate.CARD_FIELDS), "references": refs,
                         "style": {"brand": "Digiwin", "palette": ["white", "blue"], "lighting": "bright", "avoid": ["neon"]},
                         "output": {"directory": "fixture/planned", "extension": ".png", "width": 1254, "height": 1254}}
        for ad in self.copy["ads"]:
            aid = ad["ad_id"]
            ids = [c["card_id"] for c in ad["cards"]]
            self.contract["card_order"][aid] = ids
            self.contract["surfaces"][aid] = [{"surface_id": "feed", "reading_order": ["caption"] + [cid + "." + f for cid in ids for f in gate.CARD_FIELDS]}]
            for cid in ids:
                self.contract["card_sources"][cid] = ["fixture/source.txt"]
        self.commit_inputs()

    def put(self, name, value):
        path = self.root / self.prefix / name
        path.parent.mkdir(parents=True, exist_ok=True)
        if isinstance(value, dict):
            value = json.dumps(value, ensure_ascii=False, indent=2) + "\n"
        path.write_text(value, encoding="utf-8")
        return path

    def ref(self, name, revision):
        return {"path": self.prefix + "/" + name, "sha256": gate.digest((self.root / self.prefix / name).read_bytes()), "revision": revision}

    def commit_inputs(self):
        """Save synthetic dependency order, not a Git operation or real approval."""
        self.put("copy.json", self.copy)
        self.contract["copy"] = self.ref("copy.json", self.copy["revision"])
        self.put("contract.json", self.contract)
        subjects = {"contract": self.ref("contract.json", self.contract["revision"]), "copy": self.contract["copy"], "sources": self.contract["sources"]}
        self.review = {"schema_version": 1, "revision": "fixture-review-v1", "writer": "fixture-writer", "reviewer": "fixture-reviewer", "date": "2026-10-03", "scope": "OFFLINE_SOURCE_COPY", "independence": "INDEPENDENT", "subjects": subjects,
                       "verdicts": {"source_copy": "PASS", "editorial": "PASS", "first_mention": "PASS"}, "reviewed_ads": ["A", "B"], "reviewed_fields": [ad["ad_id"] + "/" + field for ad in self.copy["ads"] for field in ["caption"] + [c["card_id"] + "." + f for c in ad["cards"] for f in gate.CARD_FIELDS]], "unresolved_findings": []}
        self.put("review.json", self.review)
        self.release = {"schema_version": 1, "revision": "fixture-release-v1", "authorizer": "synthetic fixture authorizer", "authority_ref": self.ref("authority.txt", "authority-v1"), "purpose": "FIXTURE_ONLY", "contract": subjects["contract"], "copy": subjects["copy"], "review": self.ref("review.json", "fixture-review-v1"), "groups": self.contract["groups"]}
        self.put("release.json", self.release)
        self.anchor = self.ref("release.json", "fixture-release-v1")["sha256"]
        self.spec = {"schema_version": 1, "revision": "fixture-spec-v1", "release": self.ref("release.json", "fixture-release-v1"), "contract": self.release["contract"], "copy": self.release["copy"], "review": self.release["review"], "calls": []}
        by_id = {c["card_id"]: c for ad in self.copy["ads"] for c in ad["cards"]}
        for i, group in enumerate(self.release["groups"]):
            call = {"call_id": "call" + str(i), "targets": group, "references": self.contract["references"],
                    "concepts": [{"card_id": cid, "concept_id": "concept" + str(i), "reader_question": "Dữ liệu nào đi cùng lô?", "description": "Mối liên hệ khác nhau " + str(i), "props": ["diagram" + str(i)], "artwork_labels": by_id[cid]["artwork_labels"]} for cid in group],
                    "artwork_text": {cid: gate.artwork(by_id[cid]) for cid in group}, "prompt": "", "prompt_sha256": "", "output_id": "image" + str(i), "output_path": "fixture/planned/image" + str(i) + ".png"}
            self.spec["calls"].append(call)
        self.save_spec()

    def save_spec(self):
        for call in self.spec["calls"]:
            call["prompt"] = gate.make_prompt(self.contract, call)
            call["prompt_sha256"] = gate.digest(call["prompt"].encode("utf-8"))
        self.put("spec.json", self.spec)

    def check(self):
        return gate.validate(self.root, "fixture/release.json", self.anchor, "fixture/spec.json")[0]

    def dispatch(self):
        receipt = self.check()
        self.put("receipt.json", receipt)
        call = self.spec["calls"][0]
        self.proposal = {"schema_version": 1, "record_kind": "PLANNED_DISPATCH_CHECK", "call_id": call["call_id"], "preflight_sha256": self.ref("receipt.json", "unused")["sha256"], "prompt": call["prompt"], "prompt_sha256": call["prompt_sha256"], "reference_paths": [r["path"] for r in call["references"]], "output_path": call["output_path"]}
        self.put("dispatch.json", self.proposal)
        return self.dispatch_check()

    def dispatch_check(self):
        return gate.dispatch_check(self.root, "fixture/release.json", self.anchor, "fixture/spec.json", "fixture/receipt.json", "fixture/dispatch.json")[0]


class GateTests(unittest.TestCase):
    def setUp(self):
        # Keep test artifacts in this repository, not unmanaged Windows Temp.
        work = ROOT / "work"
        work.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="imagegen-fixture-", dir=work)
        self.addCleanup(self.temp.cleanup)
        self.fx = Fixture(Path(self.temp.name))

    def fails(self, pattern, check=None):
        with self.assertRaisesRegex(gate.Invalid, pattern):
            (check or self.fx.check)()

    def test_varied_positive_has_no_creative_acceptance(self):
        receipt = self.fx.check()
        self.assertEqual(receipt["mechanical_verdict"], "PASS")
        self.assertEqual(receipt["advisories"], [])
        self.assertEqual(receipt["creative_verdict"], "INSUFFICIENT_EVIDENCE")
        self.assertEqual(receipt["authority"], "NO_GENERATION_AUTHORITY")

    def test_homogeneous_is_advisory_not_keyword_veto(self):
        for call in self.fx.spec["calls"]:
            for concept in call["concepts"]:
                concept.update(concept_id="same", description="Paper pen chip tray", props=["paper", "pen", "chip tray"])
        self.fx.save_spec()
        receipt = self.fx.check()
        self.assertEqual(receipt["mechanical_verdict"], "PASS")
        self.assertTrue(any("CONCEPT_REPETITION" in a for a in receipt["advisories"]))
        self.assertTrue(any("PROP_REPETITION" in a for a in receipt["advisories"]))
        self.assertEqual(receipt["creative_verdict"], "INSUFFICIENT_EVIDENCE")

    def test_diagram_with_approved_labels_passes(self):
        self.fx.spec["calls"][0]["concepts"][0]["description"] = "A source-safe lot/time diagram"
        self.fx.save_spec()
        self.assertEqual(self.fx.check()["mechanical_verdict"], "PASS")

    def test_four_call_and_eight_call_contracts(self):
        self.assertEqual(len(self.fx.check()["call_ids"]), 4)
        full = Fixture(self.fx.root / "full", full=True)
        self.assertEqual(len(full.check()["call_ids"]), 8)

    def test_wrong_count_and_reuse_and_missing_coverage(self):
        original = copy.deepcopy(self.fx.spec)
        for mutation in (lambda s: s["calls"].pop(), lambda s: s["calls"][0]["targets"].append("B1"), lambda s: s["calls"].append(copy.deepcopy(s["calls"][0]))):
            with self.subTest(mutation=mutation):
                self.fx.spec = copy.deepcopy(original)
                mutation(self.fx.spec)
                self.fx.save_spec()
                self.fails("count|coverage")

    def test_unapproved_reference_label_fails(self):
        self.fx.spec["calls"][0]["artwork_text"]["A1"]["artwork_labels"].append("Reference customer record 999")
        self.fx.save_spec()
        self.fails("Unapproved artwork")

    def test_contract_and_spec_cannot_replace_trusted_release(self):
        anchor = self.fx.anchor
        self.fx.contract["style"]["lighting"] = "changed"
        self.fx.commit_inputs()
        self.fx.anchor = anchor
        self.fails("Changed input: fixture/release")

    def test_old_release_rejects_changed_contract_and_updated_spec(self):
        self.fx.contract["groups"].pop()
        self.fx.put("contract.json", self.fx.contract)
        self.fx.spec["contract"] = self.fx.ref("contract.json", self.fx.contract["revision"])
        self.fx.save_spec()
        self.fails("Changed input: fixture/contract")

    def test_missing_review_and_wrong_subject_and_unresolved(self):
        original = copy.deepcopy(self.fx.review)
        for key in ("verdicts", "subjects", "unresolved_findings", "reviewed_ads"):
            with self.subTest(field=key):
                review = copy.deepcopy(original)
                if key == "verdicts":
                    review[key]["editorial"] = "FAIL"
                elif key == "subjects":
                    review[key]["copy"]["sha256"] = "0" * 64
                elif key == "unresolved_findings":
                    review[key] = ["leaked internal caution"]
                else:
                    review[key] = ["A"]
                self.fx.put("review.json", review)
                self.fx.release["review"] = self.fx.ref("review.json", "fixture-review-v1")
                self.fx.put("release.json", self.fx.release)
                self.fx.anchor = self.fx.ref("release.json", "fixture-release-v1")["sha256"]
                self.fx.spec.update(review=self.fx.release["review"], release=self.fx.ref("release.json", "fixture-release-v1"))
                self.fx.save_spec()
                self.fails("Review|review|Unresolved|Incomplete")

    def test_A_explanation_cannot_exempt_B(self):
        for ad in self.fx.copy["ads"]:
            ad["caption"] = "ERP/MES"
        definition = self.fx.contract["definitions"]["OSAT"]
        self.fx.copy["ads"][0]["cards"][0]["headline"] = "OSAT (" + definition + ")"
        self.fx.copy["ads"][1]["cards"][0]["headline"] = "OSAT"
        self.fx.commit_inputs()
        self.fails("Unexplained first mention: B")

    def test_later_definition_does_not_repair_first_occurrence(self):
        self.fx.copy["ads"][0]["caption"] = "OSAT. OSAT (" + self.fx.contract["definitions"]["OSAT"] + ")"
        self.fx.commit_inputs()
        self.fails("Unexplained first mention: A")

    def test_all_required_terms_and_case_insensitive_matching(self):
        for term in gate.TERMS:
            with self.subTest(term=term):
                definition = self.fx.contract["definitions"][term]
                for ad in self.fx.copy["ads"]:
                    ad["caption"] = term.lower() + " (" + definition + ") ERP/MES"
                self.fx.commit_inputs()
                self.assertEqual(self.fx.check()["mechanical_verdict"], "PASS")
                self.fx.copy["ads"][1]["caption"] = term.lower()
                self.fx.commit_inputs()
                self.fails("Unexplained first mention: B")

    def test_missing_caption_on_independent_surface_cannot_supply_definition(self):
        self.fx.copy["ads"][0]["cards"][0]["headline"] = "OSAT"
        self.fx.contract["surfaces"]["A"].append({"surface_id": "standalone", "reading_order": ["A1.headline", "A1.body"]})
        self.fx.commit_inputs()
        self.fails("A/standalone")

    def test_cjk_adjacent_first_mentions_in_captions_and_cards(self):
        for locale in ("zh-Hans", "zh-Hant"):
            for term in gate.TERMS:
                for location in ("caption", "headline"):
                    for prefix in ("", "检查"):
                        with self.subTest(locale=locale, term=term, location=location, prefix=prefix):
                            fx = Fixture(self.fx.root / (locale + term + location + str(len(prefix))))
                            fx.contract["locale"] = locale
                            for ad in fx.copy["ads"]:
                                ad["caption"] = "ERP/MES"
                            ad = fx.copy["ads"][1]
                            wording = prefix + term + "业务"
                            if location == "caption":
                                ad["caption"] = wording
                            else:
                                ad["cards"][0]["headline"] = wording
                            fx.commit_inputs()
                            with self.assertRaisesRegex(gate.Invalid, "Unexplained first mention: B"):
                                fx.check()
                            later = term + " (" + fx.contract["definitions"][term] + ")"
                            if location == "caption":
                                ad["caption"] = wording + "。" + later
                            else:
                                ad["cards"][0]["headline"] = wording + "。" + later
                            fx.commit_inputs()
                            with self.assertRaisesRegex(gate.Invalid, "Unexplained first mention: B"):
                                fx.check()
                            explained = prefix + term.lower() + " (" + fx.contract["definitions"][term] + ")业务"
                            if location == "caption":
                                ad["caption"] = explained
                            else:
                                ad["cards"][0]["headline"] = explained
                            fx.commit_inputs()
                            self.assertEqual(fx.check()["mechanical_verdict"], "PASS")

    def test_latin_identifier_substrings_not_treated_as_terms(self):
        self.fx.copy["ads"][0]["caption"] = "xOSAT OSAT2 _WIP Fablessness"
        self.fx.commit_inputs()
        self.assertEqual(self.fx.check()["mechanical_verdict"], "PASS")

    def test_omitted_field_cannot_bypass_first_mention(self):
        self.fx.contract["surfaces"]["B"][0]["reading_order"].remove("B1.alt")
        self.fx.commit_inputs()
        self.fails("Visible fields omitted")

    def test_visible_limits_and_dash(self):
        for wording in ("x" * 501, "ERP\u2014MES"):
            with self.subTest(wording=wording):
                self.fx.copy["ads"][0]["cards"][0]["body"] = wording
                self.fx.commit_inputs()
                self.fails("Field limit|Forbidden visible dash")

    def test_source_and_reference_bytes_rechecked(self):
        for filename in ("source.txt", "palette.dat", "authority.txt"):
            with self.subTest(filename=filename):
                self.fx = Fixture(self.fx.root / filename.replace(".", "_"))
                self.fx.dispatch()
                self.fx.put(filename, "changed bytes")
                self.fails("Changed input", self.fx.dispatch_check)

    def test_reference_role_cannot_inherit_layout(self):
        self.fx.contract["references"][0]["attributes"].append("composition")
        self.fx.commit_inputs()
        self.fails("cannot transfer composition")

    def test_prompt_and_reference_paths_bound_at_dispatch(self):
        self.fx.dispatch()
        for key in ("prompt", "reference_paths", "output_path", "preflight_sha256"):
            with self.subTest(field=key):
                proposal = copy.deepcopy(self.fx.proposal)
                proposal[key] = ["fixture/source.txt"] if key == "reference_paths" else "tampered"
                self.fx.put("dispatch.json", proposal)
                self.fails("Dispatch", self.fx.dispatch_check)

    def test_dispatch_rejects_changed_spec_and_review(self):
        self.fx.dispatch()
        self.fx.spec["calls"][0]["concepts"][0]["description"] = "changed source-safe diagram"
        self.fx.save_spec()
        self.fails("Stale or altered", self.fx.dispatch_check)
        self.fx.dispatch()
        self.fx.review["date"] = "changed"
        self.fx.put("review.json", self.fx.review)
        self.fails("Changed input", self.fx.dispatch_check)

    def test_dispatch_pass_is_not_an_actual_call(self):
        result = self.fx.dispatch()
        self.assertFalse(result["actual_dispatch_observed"])
        self.assertEqual(result["authority"], "NO_GENERATION_AUTHORITY")

    def test_completed_sibling_allows_second_dispatch_and_viewer_check(self):
        self.fx.dispatch()
        first_path = self.fx.root / self.fx.spec["calls"][0]["output_path"]
        first_path.parent.mkdir(parents=True, exist_ok=True)
        first_path.write_bytes(b"synthetic completed output, not an ImageGen image")
        call = self.fx.spec["calls"][1]
        self.fx.proposal.update(call_id=call["call_id"], prompt=call["prompt"], prompt_sha256=call["prompt_sha256"], reference_paths=[r["path"] for r in call["references"]], output_path=call["output_path"])
        self.fx.put("dispatch.json", self.fx.proposal)
        self.assertEqual(self.fx.dispatch_check()["mechanical_verdict"], "PASS")
        self.fx.put("viewer.json", self.fx.copy)
        self.assertEqual(gate.viewer_check(self.fx.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", "fixture/viewer.json")[0]["mechanical_verdict"], "PASS")
        second_path = self.fx.root / call["output_path"]
        second_path.write_bytes(b"second completed fixture output")
        self.fails("Selected output would overwrite", self.fx.dispatch_check)

    def test_fresh_selected_call_preflight_and_scope_binding(self):
        first_path = self.fx.root / self.fx.spec["calls"][0]["output_path"]
        first_path.parent.mkdir(parents=True, exist_ok=True)
        first_path.write_bytes(b"completed fixture output")
        self.fails("overwrite existing")  # Batch preflight still protects every output.
        call = self.fx.spec["calls"][1]
        receipt = gate.validate(self.fx.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", scope_call_id=call["call_id"])[0]
        self.fx.put("receipt.json", receipt)
        self.fx.proposal = {"schema_version": 1, "record_kind": "PLANNED_DISPATCH_CHECK", "call_id": call["call_id"], "preflight_sha256": self.fx.ref("receipt.json", "unused")["sha256"], "prompt": call["prompt"], "prompt_sha256": call["prompt_sha256"], "reference_paths": [r["path"] for r in call["references"]], "output_path": call["output_path"]}
        self.fx.put("dispatch.json", self.fx.proposal)
        self.assertEqual(self.fx.dispatch_check()["scope_call_id"], call["call_id"])
        another = self.fx.spec["calls"][2]
        self.fx.proposal.update(call_id=another["call_id"], prompt=another["prompt"], prompt_sha256=another["prompt_sha256"], reference_paths=[r["path"] for r in another["references"]], output_path=another["output_path"])
        self.fx.put("dispatch.json", self.fx.proposal)
        self.fails("selected preflight call", self.fx.dispatch_check)
        with self.assertRaisesRegex(gate.Invalid, "Unknown preflight call scope"):
            gate.validate(self.fx.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", scope_call_id="unknown")

    def test_viewer_projection_rejects_hidden_notes_metadata_attachments(self):
        for key in ("internal_notes", "hidden_html", "metadata", "attachments", "source_map"):
            with self.subTest(field=key):
                viewer = copy.deepcopy(self.fx.copy)
                viewer[key] = "Case chỉ ở Đài Loan, không chắc sẽ áp dụng cho khu vực..."
                self.fx.put("viewer.json", viewer)
                self.fails("Viewer payload", lambda: gate.viewer_check(self.fx.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", "fixture/viewer.json"))

    def test_public_copy_cannot_serialize_internal_keys(self):
        self.fx.copy["ads"][0]["cards"][0]["internal_notes"] = "hypothesis"
        self.fx.commit_inputs()
        self.fails("Unexpected fields")

    def test_internal_caution_not_approved_for_artwork(self):
        self.fx.spec["calls"][0]["artwork_text"]["A1"]["source_text"] = "Case chỉ ở Đài Loan, không chắc sẽ áp dụng cho khu vực..."
        self.fx.save_spec()
        self.fails("Unapproved artwork")

    def test_matching_bad_copy_does_not_get_semantic_pass(self):
        self.fx.copy["ads"][0]["cards"][0]["source_text"] = "Case chỉ ở Đài Loan, không chắc sẽ áp dụng cho khu vực..."
        self.fx.commit_inputs()  # Deliberately flawed synthetic human review.
        result = self.fx.check()
        self.assertTrue(any("EDITORIAL_SEMANTIC_REVIEW" in a for a in result["advisories"]))
        self.assertEqual(result["semantic_verdict"], "NOT_ASSESSED")
        self.assertEqual(result["authority"], "NO_GENERATION_AUTHORITY")

    def test_accurate_taiwan_source_kept_in_viewer_projection(self):
        self.fx.put("viewer.json", self.fx.copy)
        result = gate.viewer_check(self.fx.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", "fixture/viewer.json")[0]
        self.assertEqual(result["mechanical_verdict"], "PASS")
        self.assertEqual(result["rendered_artifact_verdict"], "NOT_ASSESSED")

    def test_duplicate_output_and_overwrite_blocked(self):
        self.fx.spec["calls"][1]["output_id"] = self.fx.spec["calls"][0]["output_id"]
        self.fx.spec["calls"][1]["output_path"] = self.fx.spec["calls"][0]["output_path"]
        self.fx.save_spec()
        self.fails("Duplicate output")
        self.fx.commit_inputs()
        path = self.fx.root / self.fx.spec["calls"][0]["output_path"]
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(b"frozen artifact")
        self.fails("overwrite existing")

    def test_path_escape_and_duplicate_json_keys(self):
        inputs = gate.Inputs(self.fx.root)
        for path in ("../outside.json", "C:/outside.json", "/outside.json"):
            with self.subTest(path=path), self.assertRaises(gate.Invalid):
                inputs.path(path)
        self.fx.put("bad.json", '{"a":1,"a":2}')
        self.fails("Duplicate JSON key", lambda: inputs.json("fixture/bad.json"))

    def test_missing_inputs_fail_closed(self):
        (self.fx.root / "fixture/review.json").unlink()
        self.fails("Missing input")

    def test_boolean_schema_version_is_rejected(self):
        self.fx.spec["schema_version"] = True
        self.fx.save_spec()
        self.fails("Unsupported schema version")

    def test_missing_visible_field_attestation_is_rejected(self):
        self.fx.review["reviewed_fields"].remove("A/A1.source_text")
        self.fx.put("review.json", self.fx.review)
        self.fx.release["review"] = self.fx.ref("review.json", "fixture-review-v1")
        self.fx.put("release.json", self.fx.release)
        self.fx.anchor = self.fx.ref("release.json", "fixture-release-v1")["sha256"]
        self.fx.spec.update(review=self.fx.release["review"], release=self.fx.ref("release.json", "fixture-release-v1"))
        self.fx.save_spec()
        self.fails("Incomplete visible-field")

    def test_cli_and_receipt_self_hash_boundary(self):
        command = [sys.executable, "-B", str(ROOT / "scripts/verify_imagegen_preflight.py"), "preflight", "--root", str(self.fx.root), "--release", "fixture/release.json", "--release-sha256", self.fx.anchor, "--spec", "fixture/spec.json", "--output", "fixture/receipt.json"]
        result = subprocess.run(command, capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["mechanical_verdict"], "PASS")
        self.fx.dispatch()
        args = command[3:]
        for output in ("fixture/spec.json", "fixture/planned/receipt.json"):
            args[-1] = output
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                self.assertEqual(gate.main(args), 1)


if __name__ == "__main__":
    unittest.main(verbosity=2)
