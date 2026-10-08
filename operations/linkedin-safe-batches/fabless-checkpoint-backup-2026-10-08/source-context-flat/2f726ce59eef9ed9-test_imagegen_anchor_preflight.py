"""Synthetic no-generation tests for the developing pregen guard."""
import copy
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def module(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    value = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(value)
    return value


guard = module("anchor_guard", ROOT / "scripts/verify_imagegen_anchor_preflight.py")
fixtures = module("core_fixtures", ROOT / "tests/test_imagegen_preflight.py")


class AnchorGuardTests(unittest.TestCase):
    def setUp(self):
        work = ROOT / "work"
        work.mkdir(exist_ok=True)
        self.temp = tempfile.TemporaryDirectory(prefix="anchor-fixture-", dir=work)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for path in (guard.CORE_PATH, guard.ANCHOR_PATH, guard.SOURCE_PATH):
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes((ROOT / path).read_bytes())
        self.fx = fixtures.Fixture(self.root)
        fx = self.fx
        ads = fx.copy["ads"]
        cards = [c["card_id"] for a in ads for c in a["cards"]]
        fields = {a["ad_id"]: ["caption"] + [c["card_id"] + "." + f for c in a["cards"] for f in fixtures.gate.CARD_FIELDS] for a in ads}
        self.script = {"revision": "synthetic-script-v1", "gate_id": "AD-ED-01", "stage": "PREGEN_SCRIPT", "verdict": "SCRIPT_REVIEW_PASS",
                       "copy_sha256": fx.release["copy"]["sha256"], "BRAND_ROLE": {"verdict": "PASS"}, "ADVERTISER_VOICE": {"verdict": "PASS"},
                       "reviewed_ads": [a["ad_id"] for a in ads], "reviewed_fields": fields}
        fx.put("script.json", self.script)
        fx.put("brief.txt", "SYNTHETIC CONTEXT ONLY. No customer review or approval.")
        digest = fixtures.gate.digest
        self.review = {"schema_version": 1, "revision": "synthetic-anchor-review-v1", "gate_id": "MSG-ANCHOR-01", "stage": "PREGEN_SCRIPT", "verdict": "MESSAGE_ANCHOR_PASS",
                       "anchor": {"path": guard.ANCHOR_PATH, "sha256": digest((self.root / guard.ANCHOR_PATH).read_bytes()), "revision": "1.0"},
                       "source": {"path": guard.SOURCE_PATH, "sha256": digest((self.root / guard.SOURCE_PATH).read_bytes()), "revision": "VY-MAIL-USER-20261006"},
                       "subjects": {"contract": fx.release["contract"], "copy": fx.release["copy"], "spec": fx.ref("spec.json", fx.spec["revision"]), "script_review": fx.ref("script.json", self.script["revision"])},
                       "scope": {"segment": "VN_DOMESTIC", "locale": "vi", "persona": "synthetic operations persona", "route": "synthetic supplier"},
                       "writer": "fixture-writer", "reviewer": "fixture-reviewer", "independence": "INDEPENDENT",
                       "coverage": {"ads": [a["ad_id"] for a in ads], "cards": cards, "fields": fields, "storyboard_cards": cards},
                       "rules": {"A" + str(i): {"verdict": "MATCH", "observation": "Synthetic declaration, mechanics only."} for i in range(1, 8)},
                       "units": [{"card_id": cid, "verdict": "MATCH", "observation": "Synthetic unit."} for cid in cards],
                       "transitions": [{"cards": [a["card_id"], b["card_id"]], "verdict": "MATCH", "observation": "Synthetic transition."} for ad in ads for a, b in zip(ad["cards"], ad["cards"][1:])],
                       "context": {"scope": "STANDALONE", "verdict": "MATCH", "observation": "Synthetic standalone context.", "brief": fx.ref("brief.txt", "fixture-brief-v1"), "related_inputs": []}, "unresolved_findings": []}

    def save(self):
        self.fx.put("anchor-review.json", self.review)
        return self.fx.ref("anchor-review.json", self.review["revision"])["sha256"]

    def check(self, expected_sha=None, **overrides):
        values = {"call_id": "call0", "segment": "VN_DOMESTIC", "persona": "synthetic operations persona", "route": "synthetic supplier"}
        values.update(overrides)
        return guard.check(self.root, "fixture/release.json", self.fx.anchor, "fixture/spec.json", "fixture/anchor-review.json", expected_sha or self.save(), **values)

    def test_positive_fixture_has_no_generation_payload(self):
        result = self.check()
        self.assertEqual(result["status"], "PREGEN_INPUTS_VERIFIED")
        self.assertIsNone(result["tool_args"])
        self.assertEqual(result["purpose"], "FIXTURE_ONLY")
        self.assertIn("NOT_AUTOMATICALLY", result["semantic_verdict"])

    def reference_pack(self, count):
        refs = []
        for i in range(count):
            name = "reference" + str(i) + ".dat"
            self.fx.put(name, "SYNTHETIC REFERENCE; no image generation.")
            refs.append({**self.fx.ref(name, "synthetic-ref-v1"), "role": "palette", "attributes": ["colors"]})
        self.fx.contract["references"] = refs
        self.fx.commit_inputs()
        self.review["subjects"]["contract"] = self.fx.release["contract"]
        self.review["subjects"]["copy"] = self.fx.release["copy"]
        self.review["subjects"]["spec"] = self.fx.ref("spec.json", self.fx.spec["revision"])

    def test_five_reference_tool_boundary_allows_fixture(self):
        self.reference_pack(5)
        self.assertEqual(self.check()["status"], "PREGEN_INPUTS_VERIFIED")

    def test_six_references_block_before_dispatch(self):
        self.reference_pack(6)
        with self.assertRaisesRegex(ValueError, "at most 5 reference images"):
            self.check()

    def test_missing_receipt_blocks(self):
        with self.assertRaisesRegex(ValueError, "Missing input"):
            self.check(expected_sha="0" * 64)

    def test_pending_anchor_blocks(self):
        self.review["verdict"] = "PENDING"
        with self.assertRaisesRegex(ValueError, "not passed"):
            self.check()

    def test_changed_anchor_blocks(self):
        p = self.root / guard.ANCHOR_PATH
        p.write_bytes(p.read_bytes() + b"\nChanged anchor.")
        with self.assertRaisesRegex(ValueError, "Changed input"):
            self.check()

    def test_changed_review_hash_blocks(self):
        prior = self.save()
        self.review["revision"] = "changed"
        self.save()
        with self.assertRaisesRegex(ValueError, "Changed input"):
            self.check(expected_sha=prior)

    def test_new_copy_cannot_reuse_anchor_review(self):
        self.fx.copy["ads"][0]["cards"][0]["body"] = "Changed ERP wording."
        self.fx.commit_inputs()
        with self.assertRaisesRegex(ValueError, "subject changed"):
            self.check()

    def test_persona_change_blocks(self):
        with self.assertRaisesRegex(ValueError, "stale"):
            self.check(persona="different persona")

    def test_wrong_segment_locale_blocks(self):
        with self.assertRaisesRegex(ValueError, "locale mismatch"):
            self.check(segment="FDI")

    def test_missing_storyboard_field_review_blocks(self):
        self.review["coverage"]["storyboard_cards"].pop()
        with self.assertRaisesRegex(ValueError, "coverage"):
            self.check()

    def test_unmatched_rule_blocks(self):
        self.review["rules"]["A5"]["verdict"] = "N/A"
        with self.assertRaisesRegex(ValueError, "criterion unresolved"):
            self.check()

    def test_missing_transition_blocks(self):
        self.review["transitions"].pop()
        with self.assertRaisesRegex(ValueError, "transitions"):
            self.check()

    def test_script_not_passed_blocks(self):
        self.script["verdict"] = "PENDING"
        self.fx.put("script.json", self.script)
        self.review["subjects"]["script_review"] = self.fx.ref("script.json", self.script["revision"])
        with self.assertRaisesRegex(ValueError, "Script not reviewed"):
            self.check()

    def test_full_journey_requires_other_stage_pins(self):
        self.review["context"]["scope"] = "FULL_JOURNEY"
        with self.assertRaisesRegex(ValueError, "other stage inputs"):
            self.check()

    def test_forged_independence_blocks(self):
        self.review["reviewer"] = self.review["writer"]
        with self.assertRaisesRegex(ValueError, "independence"):
            self.check()

    def test_changed_context_blocks(self):
        self.fx.put("brief.txt", "Changed journey intent.")
        with self.assertRaisesRegex(ValueError, "Changed input"):
            self.check()

    def test_changed_scene_spec_blocks_even_with_fresh_core_prompt(self):
        self.fx.spec["calls"][0]["concepts"][0]["description"] = "Changed scene."
        self.fx.save_spec()
        with self.assertRaisesRegex(ValueError, "Changed input"):
            self.check()

    def test_fdi_locale_bindings_fixture_only(self):
        for locale in ("en", "zh-Hans", "zh-Hant"):
            with self.subTest(locale=locale):
                self.fx.contract["locale"] = locale
                self.fx.commit_inputs()
                self.review["scope"].update(segment="FDI", locale=locale)
                self.review["subjects"].update(contract=self.fx.release["contract"], copy=self.fx.release["copy"], spec=self.fx.ref("spec.json", self.fx.spec["revision"]))
                self.review["rules"]["A5"]["verdict"] = "N/A"
                self.assertIsNone(self.check(segment="FDI")["tool_args"])

    def test_payload_matches_exact_checked_call_without_tool_execution(self):
        # Synthetic OFFLINE_IMAGEGEN envelope only; no actual generation/approval.
        self.fx.release["purpose"] = "OFFLINE_IMAGEGEN"
        self.fx.put("release.json", self.fx.release)
        self.fx.anchor = self.fx.ref("release.json", self.fx.release["revision"])["sha256"]
        self.fx.spec["release"] = self.fx.ref("release.json", self.fx.release["revision"])
        self.fx.save_spec()
        self.review["subjects"]["spec"] = self.fx.ref("spec.json", self.fx.spec["revision"])
        result = self.check()
        self.assertEqual(result["tool_args"]["prompt"], self.fx.spec["calls"][0]["prompt"])
        self.assertEqual(result["authority"], "NO_ADDITIONAL_GENERATION_AUTHORITY")


if __name__ == "__main__":
    unittest.main()
