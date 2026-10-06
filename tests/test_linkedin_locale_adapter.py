"""Locale draft invariants; the frozen gate remains the release authority."""
import copy
import importlib.util
from pathlib import Path
import unittest
import tempfile

ROOT = Path(__file__).resolve().parents[1]
module = importlib.util.spec_from_file_location("locale_adapter", ROOT / "scripts/prepare_linkedin_locale.py")
adapter = importlib.util.module_from_spec(module)
module.loader.exec_module(adapter)
demo_module = importlib.util.spec_from_file_location("locale_examples", ROOT / "operations/linkedin-locale-adapter/prepare_examples.py")
demo = importlib.util.module_from_spec(demo_module)
demo_module.loader.exec_module(demo)


class LocaleDraftTests(unittest.TestCase):
    def setUp(self):
        source = ROOT / "operations/linkedin-journey-demo/2026-10-06/osat/v1"
        self.profiles = adapter.load(adapter.PROFILES)
        self.localized = adapter.load(ROOT / "operations/linkedin-locale-adapter/examples/en.json")
        if (source / "contract.json").is_file():
            self.contract = adapter.load(source / "contract.json")
            self.public = adapter.load(source / "public-copy.json")
            self.spec = adapter.load(source / "spec.json")
        else:
            # Main intentionally excludes the old VI journey. This authored
            # in-memory fixture tests mechanics, not original-source acceptance.
            drafts = ROOT / "operations/linkedin-locale-adapter/drafts/en"
            self.contract = adapter.load(drafts / "contract.draft.json")
            self.public = copy.deepcopy(self.localized["copy"])
            self.public["revision"] = "synthetic-locale-source-v1"
            self.public["ads"][0]["cards"][0]["artwork_labels"] = ["TÀI CHÍNH NHÀ MÁY BÁN DẪN", "Giải pháp ERP cho sản xuất"]
            self.contract["style"]["brand"] = "Official supplied Digiwin mark once; category line gives role: Giải pháp ERP cho sản xuất."
            self.contract["style"]["campaign"] = {"revision": "synthetic-vi-style-v1", "instructions": "Single square cold advertisement. Use two-line headline. Preserve Vietnamese accents exactly."}
            self.spec = {"calls": adapter.load(drafts / "calls.draft.json")["calls"]}

    def build(self, localized=None):
        return adapter.build(self.contract, self.public, self.spec, localized or self.localized, self.profiles, "draft-fixture")

    def test_all_locales_keep_storyboard_and_change_prompt_language(self):
        for locale in demo.TEXT:
            with self.subTest(locale=locale):
                local = adapter.load(ROOT / "operations/linkedin-locale-adapter/examples" / (locale + ".json"))
                contract, public, calls = self.build(local)
                self.assertEqual(contract["locale"], locale)
                self.assertIn("LOCALE: " + locale, contract["style"]["campaign"]["instructions"])
                self.assertNotIn("Preserve Vietnamese accents exactly", contract["style"]["campaign"]["instructions"])
                self.assertNotIn("Giải pháp", contract["style"]["brand"])
                for key in ("groups", "card_order", "ad_order", "references", "sources", "card_sources", "limits", "surfaces"):
                    self.assertEqual(contract[key], self.contract[key])
                for before, after in zip(self.spec["calls"], calls):
                    for a, b in zip(before["concepts"], after["concepts"]):
                        for key in ("description", "props", "concept_id", "card_id"):
                            self.assertEqual(a[key], b[key])
                    self.assertNotEqual(before["output_path"], after["output_path"])
                self.assertEqual(contract["copy"]["sha256"], adapter.sha(adapter.encode(public)))

    def test_reject_unknown_locale(self):
        self.localized["locale"] = "zh"
        with self.assertRaisesRegex(ValueError, "Unsupported locale"):
            self.build()

    def test_reject_storyboard_card_change(self):
        self.localized["copy"]["ads"][0]["cards"][0]["card_id"] = "different"
        with self.assertRaisesRegex(ValueError, "Storyboard"):
            self.build()

    def test_reject_new_number_claim(self):
        self.localized["copy"]["ads"][0]["cards"][0]["body"] += " Save 30%."
        with self.assertRaisesRegex(ValueError, "Numeric"):
            self.build()

    def test_reject_entity_change(self):
        self.localized["copy"]["ads"][0]["caption"] = self.localized["copy"]["ads"][0]["caption"].replace("Digiwin", "Someone")
        with self.assertRaisesRegex(ValueError, "entity"):
            self.build()

    def test_reject_field_overflow(self):
        self.localized["copy"]["ads"][0]["cards"][0]["headline"] = "long " * 70
        with self.assertRaisesRegex(ValueError, "limit"):
            self.build()

    def test_source_inputs_not_mutated(self):
        snapshot = copy.deepcopy((self.contract, self.public, self.spec, self.localized))
        self.build()
        self.assertEqual(snapshot, (self.contract, self.public, self.spec, self.localized))

    def test_draft_has_no_release_or_approval(self):
        contract, public, calls = self.build()
        for value in (contract, public, {"calls": calls}):
            self.assertNotIn("review", value)
            self.assertNotIn("release", value)

    def test_pinned_draft_bytes_survive_checkout(self):
        for locale in demo.TEXT:
            directory = ROOT / "operations/linkedin-locale-adapter/drafts" / locale
            manifest = adapter.load(directory / "manifest.json")
            self.assertEqual(manifest["adapter_sha256"], adapter.sha((ROOT / "scripts/prepare_linkedin_locale.py").read_bytes()))
            self.assertEqual(manifest["profile_sha256"], adapter.sha(adapter.PROFILES.read_bytes()))
            contract = adapter.load(directory / "contract.draft.json")
            self.assertEqual(contract["copy"]["sha256"], adapter.sha((directory / "public-copy.draft.json").read_bytes()))

    def test_multicard_locale_drafts_fit_unchanged_carousel_gate(self):
        fixture_spec = importlib.util.spec_from_file_location("frozen_fixtures", ROOT / "tests/test_imagegen_preflight.py")
        fixtures = importlib.util.module_from_spec(fixture_spec)
        fixture_spec.loader.exec_module(fixtures)
        work = ROOT / "work"
        work.mkdir(exist_ok=True)
        for locale in demo.TEXT:
            with self.subTest(locale=locale), tempfile.TemporaryDirectory(dir=work) as directory:
                fx = fixtures.Fixture(Path(directory))
                target = copy.deepcopy(fx.copy)
                target["revision"] = "fixture-" + locale + "-v1"
                rationale = []
                definition = self.profiles["locales"][locale]["definitions"]["OSAT"]
                for ad in target["ads"]:
                    ad["caption"] = "OSAT (" + definition + ") ERP/MES."
                    for card in ad["cards"]:
                        index = card["card_id"][-1]
                        card.update(headline="Question " + index, body="ERP and MES are separate.", source_text="Synthetic source in Taiwan", cta="Read more",
                                    native_headline="Data " + index, alt="Relationship " + index, artwork_labels=["Lot", "Time"])
                        rationale.append({"card_id": card["card_id"], "reader_intent": "Synthetic fixture", "adaptation_note": "Mechanics only", "reader_question": "Which records?"})
                local = {"locale": locale, "revision": "fixture-" + locale, "copy": target, "protected_literals": ["OSAT"], "rationale": rationale}
                candidate, target, calls = adapter.build(fx.contract, fx.copy, fx.spec, local, self.profiles, "fixture/locale")
                self.assertEqual([c["targets"] for c in calls], fx.contract["groups"])
                fx.contract, fx.copy = candidate, target
                fx.commit_inputs()  # Synthetic FIXTURE_ONLY review, never a real approval.
                fx.spec["calls"] = calls
                fx.save_spec()
                self.assertEqual(fx.check()["mechanical_verdict"], "PASS")
                local["copy"]["revision"] += "-next"
                local["copy"]["ads"][0]["cards"].reverse()
                with self.assertRaisesRegex(ValueError, "Storyboard"):
                    adapter.build(candidate, target, fx.spec, local, self.profiles, "fixture/next")


if __name__ == "__main__":
    unittest.main()
