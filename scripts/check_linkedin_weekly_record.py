"""Offline validator for LinkedIn weekly record (contract v1) and its account preflight.

No browser, no network, no account access. Usage:
  python scripts/check_linkedin_weekly_record.py RECORD.json PREFLIGHT.json
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
EXPECTATIONS = ROOT / "operations/weekly-records/linkedin/preflight_expectations.json"
SCHEMA = "semi-awareness-weekly-record-v1"
FORBIDDEN_KEYS = {
    "spend", "spent", "budget", "cpc", "cpm", "cpl", "cost", "audience", "creative",
    "account_id", "campaign_id", "ad_id", "url", "email", "phone",
}
FORBIDDEN_TEXT = (
    re.compile(r"https?://", re.I),
    re.compile(r"linkedin\.com", re.I),
    re.compile(r"\b[A-Za-z]:[\\/]"),
    re.compile(r"\b\d{8,}\b"),  # numeric account/campaign/ad identifiers
    re.compile(r"R5-52|TEST-AUD|RMK-SRC", re.I),
)
NUMERIC = ("impressions", "clicks", "ctr", "reach", "frequency")


def load(path):
    def unique(pairs):
        out = {}
        for key, value in pairs:
            if key in out:
                raise ValueError("Duplicate JSON key: " + key)
            out[key] = value
        return out
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique)


def walk(value, path=""):
    if isinstance(value, dict):
        for key, child in value.items():
            yield path + "/" + key, key, child
            yield from walk(child, path + "/" + key)
    elif isinstance(value, list):
        for i, child in enumerate(value):
            item = "{}[{}]".format(path, i)
            yield item, str(i), child
            yield from walk(child, item)


def check_preflight(pre, expectations):
    errors = []
    exp = expectations["expected"]
    if pre.get("schema") != "semi-linkedin-account-preflight-v1":
        errors.append("preflight.schema sai")
    obs = pre.get("observed", {})
    for key in ("business_manager_label", "ad_account_label", "ad_account_status", "ad_set_label"):
        if obs.get(key) != exp[key]:
            errors.append("preflight {}: {!r} != expected {!r}".format(key, obs.get(key), exp[key]))
    for unit, label in exp["ad_labels"].items():
        if obs.get("ad_labels", {}).get(unit) != label:
            errors.append("preflight ad label {} khong khop".format(unit))
    blob = json.dumps(obs, ensure_ascii=False)
    for bad in expectations["hard_stop_labels"]:
        # hard-stop is exact label of the wrong account/state, not substring of the right BM name
        if bad in (obs.get("ad_account_label"), obs.get("ad_account_status")):
            errors.append("preflight hard-stop: " + bad)
    if "businessId=personal" in blob or obs.get("business_context") == "personal":
        errors.append("preflight hard-stop: tai khoan ca nhan")
    if pre.get("result") != "PASS":
        errors.append("preflight.result khong phai PASS")
    for text in (p[2] for p in walk(pre) if isinstance(p[2], str)):
        for pattern in FORBIDDEN_TEXT:
            if pattern.search(text):
                errors.append("preflight chua ID/URL/duong dan: " + text[:60])
    return errors


def check_record(rec):
    errors = []
    if rec.get("schema") != SCHEMA:
        errors.append("schema sai")
    if rec.get("channel") != "linkedin":
        errors.append("channel phai la linkedin")
    period = rec.get("period", {})
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", str(period.get("start"))) or period.get("timezone") != "Asia/Ho_Chi_Minh":
        errors.append("period sai dinh dang/timezone")
    for path, key, value in walk(rec):
        if key.lower() in FORBIDDEN_KEYS:
            errors.append("key bi cam: " + path)
        if isinstance(value, str):
            for pattern in FORBIDDEN_TEXT:
                if pattern.search(value):
                    errors.append("chuoi bi cam tai {}: {}".format(path, pattern.pattern))
    coll = rec.get("collection", {})
    for unit in rec.get("units", []):
        for k in NUMERIC:
            v = unit.get(k)
            if v is None:
                if k not in unit.get("unavailable", {}) and not rec.get("limits"):
                    errors.append("{}.{} null thieu ly do".format(unit.get("key"), k))
            elif isinstance(v, bool) or not isinstance(v, (int, float)) or v < 0:
                errors.append("{}.{} khong hop le".format(unit.get("key"), k))
        if isinstance(unit.get("ctr"), (int, float)) and unit["ctr"] > 1:
            errors.append("ctr phai la ty le 0-1")
        if unit.get("frequency") is not None and not unit.get("reach"):
            errors.append("frequency phai null khi reach null/0")
    totals = rec.get("totals", {})
    units = rec.get("units", [])
    if coll.get("range_matches_period") is False:
        has_numbers = any(totals.get(k) is not None for k in NUMERIC)
        if has_numbers and not coll.get("date_range_applied"):
            errors.append("range_matches_period=false co so lieu nhung thieu date_range_applied")
    imp = [u.get("impressions") for u in units]
    if all(isinstance(x, int) for x in imp) and totals.get("impressions") is not None and sum(imp) != totals["impressions"]:
        errors.append("totals.impressions != tong units")
    clicks = [u.get("clicks") for u in units]
    if all(isinstance(x, int) for x in clicks) and totals.get("clicks") is not None and sum(clicks) != totals["clicks"]:
        errors.append("totals.clicks != tong units")
    if isinstance(totals.get("impressions"), int) and totals["impressions"] > 0 and isinstance(totals.get("clicks"), int):
        if totals.get("ctr") is not None and abs(totals["ctr"] - totals["clicks"] / totals["impressions"]) > 1e-9:
            errors.append("totals.ctr phai tinh lai tu clicks/impressions")
    flags = rec.get("internal_flags", {})
    if all(isinstance(x, int) and x > 0 for x in imp) and len(imp) == 2:
        ratio_flag = max(imp) / min(imp) > 3
        if flags.get("impression_ratio_over_3_to_1") is not None and flags["impression_ratio_over_3_to_1"] != ratio_flag:
            errors.append("cho impression_ratio_over_3_to_1 khong khop so lieu")
    return errors


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("record")
    parser.add_argument("preflight")
    args = parser.parse_args(argv)
    errors = check_preflight(load(args.preflight), load(EXPECTATIONS)) + check_record(load(args.record))
    for e in errors:
        print("FAIL:", e)
    print("PASS" if not errors else "CHANGES_REQUIRED")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
