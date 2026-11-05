"""Synthetic checks for the weekly LinkedIn record validator and account preflight. No browser/account access."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("weekly_check", ROOT / "scripts/check_linkedin_weekly_record.py")
chk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(chk)
BASE = ROOT / "operations/weekly-records/linkedin"
RECORD = chk.load(BASE / "linkedin_2026-10-26_2026-11-01.json")
PRE = chk.load(BASE / "preflight/preflight_2026-10-26_2026-11-01.json")
EXP = chk.load(BASE / "preflight_expectations.json")


class WeeklyRecordTests(unittest.TestCase):
    def test_committed_record_and_preflight_pass(self):
        self.assertEqual(chk.check_preflight(PRE, EXP), [])
        self.assertEqual(chk.check_record(RECORD), [])

    def test_personal_on_hold_account_fails_preflight(self):
        pre = copy.deepcopy(PRE)
        pre["observed"].update(ad_account_label="Digiwin ASEAN", ad_account_status="On hold", business_context="personal")
        errors = chk.check_preflight(pre, EXP)
        self.assertTrue(any("hard-stop" in e for e in errors))
        self.assertTrue(errors)

    def test_wrong_business_manager_fails(self):
        pre = copy.deepcopy(PRE)
        pre["observed"]["business_manager_label"] = "Other BM"
        self.assertTrue(chk.check_preflight(pre, EXP))

    def test_preflight_must_not_hold_ids_or_urls(self):
        pre = copy.deepcopy(PRE)
        pre["observed"]["note"] = "https://www.linkedin.com/campaignmanager/accounts/123"
        self.assertTrue(chk.check_preflight(pre, EXP))

    def test_money_key_and_account_id_forbidden_in_record(self):
        rec = copy.deepcopy(RECORD)
        rec["totals"]["spend"] = 1
        rec["limits"].append("account 519775676")
        errors = chk.check_record(rec)
        self.assertTrue(any("key bi cam" in e for e in errors))
        self.assertTrue(any("chuoi bi cam" in e for e in errors))

    def test_null_is_not_zero_and_totals_must_match(self):
        rec = copy.deepcopy(RECORD)
        rec["totals"]["impressions"] = 36
        self.assertTrue(any("totals.impressions" in e for e in chk.check_record(rec)))

    def test_range_mismatch_requires_applied_range(self):
        rec = copy.deepcopy(RECORD)
        rec["collection"]["date_range_applied"] = ""
        self.assertTrue(chk.check_record(rec))

    def test_ratio_flag_must_match_data(self):
        rec = copy.deepcopy(RECORD)
        rec["internal_flags"]["impression_ratio_over_3_to_1"] = False
        self.assertTrue(chk.check_record(rec))


if __name__ == "__main__":
    unittest.main()
