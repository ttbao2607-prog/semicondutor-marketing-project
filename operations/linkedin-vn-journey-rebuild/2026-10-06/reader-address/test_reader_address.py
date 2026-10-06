"""Counterexamples for the bounded VN gate; no image-generation calls or receipt writes."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest
from unittest.mock import patch

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]

def load(path, name):
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

scanner = load(HERE / "verify_vn_reader_address.py", "reader_address")

class ReaderAddressTests(unittest.TestCase):
    def test_direct_address_variants_block(self):
        for text in ("Bạn?", "cùng bạn.", "Doanh nghiệp bạn\ncần gì?", "BẠN đã sẵn sàng?"):
            with self.subTest(text=text):
                self.assertTrue(scanner.scan({"headline": text}, "PREGEN_SCRIPT")["findings"])

    def test_exact_form_and_descriptive_cold_are_scan_clean(self):
        for text in ("Quý Doanh Nghiệp đã sẵn sàng?", "Đồng hành cùng doanh nghiệp Việt"):
            result = scanner.scan({"headline": text}, "PREGEN_SCRIPT")
            self.assertFalse(result["findings"])
            self.assertEqual(result["semantic_verdict"], "NOT_AUTOMATICALLY_ASSESSED")

    def test_wrong_capitalization_blocks(self):
        self.assertTrue(scanner.scan({"caption": "Quý doanh nghiệp"}, "PREGEN_SCRIPT")["findings"])

    def test_actual_artwork_still_blocks_after_copy_correction(self):
        result = scanner.scan({"native-observed": "Bạn đã sẵn sàng?"}, "POSTGEN_OBSERVED_TEXT")
        self.assertTrue(result["findings"])
        self.assertEqual(result["observed_artwork"], "REVIEWER_MUST_VERIFY")

    def test_empty_coverage_rejected(self):
        with self.assertRaises(ValueError):
            scanner.scan({}, "POSTGEN_OBSERVED_TEXT")

    def test_business_relation_requires_review_not_automatic_semantic_failure(self):
        result = scanner.scan({"body": "Quan hệ bạn hàng"}, "PREGEN_SCRIPT")
        self.assertTrue(result["findings"])
        self.assertEqual(result["semantic_verdict"], "NOT_AUTOMATICALLY_ASSESSED")

    def test_real_current_copy_and_candidate(self):
        current = json.loads((HERE.parent / "journey-v1/public-copy.json").read_text(encoding="utf-8-sig"))
        candidate = json.loads((HERE / "public-copy-candidate.json").read_text(encoding="utf-8-sig"))
        self.assertEqual(len(scanner.scan(dict(scanner.copy_fields(current)), "PREGEN_SCRIPT")["findings"]), 8)
        self.assertFalse(scanner.scan(dict(scanner.copy_fields(candidate)), "PREGEN_SCRIPT")["findings"])

    def test_both_dispatch_helpers_fail_closed_without_fresh_v5(self):
        checker = "operations/linkedin-vn-journey-rebuild/2026-10-06/reader-address/verify_vn_reader_address.py"
        for version in ("journey-v1", "journey-v2"):
            helper = load(HERE.parent / version / "dispatch-verify.py", "dispatch_" + version)
            # Mock only fresh binding metadata, leaving actual current copy unchanged.
            original = helper.read
            pins = {path: helper.sha(path) for path in original("dispatch-pins.json")}
            for case, expected in (("missing_checker", "checker pin"), ("old_policy", "policy1.1 reader-address"),
                                   ("missing_review", "semantic review"), ("false_pass", "Reader address flagged")):
                with self.subTest(version=version, case=case):
                    bound = copy.deepcopy(pins)
                    voice = copy.deepcopy(original("vn-voice-pregen.json"))
                    if case != "missing_checker": bound[checker] = helper.sha(checker)
                    if case in ("missing_review", "false_pass"): voice["policy"]["revision"] = "1.1"
                    if case == "false_pass": voice["reader_address"] = {"verdict": "PASS"}
                    def read(name):
                        return bound if name == "dispatch-pins.json" else voice if name == "vn-voice-pregen.json" else original(name)
                    with patch.object(helper, "read", side_effect=read):
                        with self.assertRaisesRegex(ValueError, expected): helper.verify("NO_DISPATCH_TEST")

if __name__ == "__main__":
    unittest.main()
