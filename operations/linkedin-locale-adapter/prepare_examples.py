"""Reproduce three offline OSAT cold drafts. No ImageGen calls."""
import copy
import importlib.util
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = Path(__file__).resolve().parent
SOURCE = ROOT / "operations/linkedin-journey-demo/2026-10-06/osat/v1"
spec = importlib.util.spec_from_file_location("locale_adapter", ROOT / "scripts/prepare_linkedin_locale.py")
adapter = importlib.util.module_from_spec(spec)
spec.loader.exec_module(adapter)

TEXT = {
    "en": {
        "caption": "Digiwin advises on manufacturing ERP. For OSAT (outsourced semiconductor assembly and test), month-end close starts with reconciling work in progress, completed output and losses by lot between finance and the factory.",
        "headline": "Month-end is here.\nDo the factory records reconcile?",
        "body": "Work in progress, completed output, losses:\nreconcile before close.",
        "native_headline": "Month-end close starts with factory records",
        "alt": "A closing calendar and factory records waiting to be reconciled at a semiconductor plant.",
        "artwork_labels": ["SEMICONDUCTOR PLANT FINANCE", "ERP for manufacturing"],
        "question": "Have finance and the factory reconciled their records before month-end close?",
        "note": "Replace the Vietnamese chốt ambiguity with reconciliation, keep shared responsibility. Direct operational question without calendar idioms or promised automation."
    },
    "zh-Hans": {
        "caption": "Digiwin提供制造业ERP咨询。对于OSAT (半导体委外封装与测试)，月末结账前，财务与工厂需要按批次核对在制品、完工产量和损耗记录。",
        "headline": "月末结账前，\n工厂记录核对了吗？",
        "body": "在制品、完工产量、损耗：\n结账前逐项核对。",
        "native_headline": "月末结账，从核对工厂记录开始",
        "alt": "半导体工厂的结账日历与待核对的生产记录。",
        "artwork_labels": ["半导体工厂财务管理", "制造业ERP解决方案"],
        "question": "月末结账前，财务与工厂是否已核对生产记录？",
        "note": "Mainland draft uses 制造业、在制品、完工产量、核对. Ask about records explicitly; avoid literal imported syntax and slogans. Native semiconductor terminology review pending."
    },
    "zh-Hant": {
        "caption": "Digiwin提供製造業ERP諮詢。對於OSAT (半導體委外封裝與測試)，月底結帳前，財務與工廠需要依批次核對在製品、完工產量與損耗紀錄。",
        "headline": "月底結帳前，\n工廠紀錄核對了嗎？",
        "body": "在製品、完工產量、損耗：\n結帳前逐項核對。",
        "native_headline": "月底結帳，從核對工廠紀錄開始",
        "alt": "半導體工廠的結帳日曆與待核對的生產紀錄。",
        "artwork_labels": ["半導體工廠財務管理", "製造業ERP解決方案"],
        "question": "月底結帳前，財務與工廠是否已核對生產紀錄？",
        "note": "Separately authored Taiwan draft uses 諮詢、在製品、紀錄、月底結帳 and 與. This is not character conversion; native semiconductor terminology review pending."
    }
}


def main():
    for locale, wording in TEXT.items():
        public = copy.deepcopy(adapter.load(SOURCE / "public-copy.json"))
        public["revision"] = "osat-cold-" + locale + "-copy-v1"
        ad = public["ads"][0]
        ad["caption"] = wording["caption"]
        card = ad["cards"][0]
        for key in ("headline", "body", "native_headline", "alt", "artwork_labels"):
            card[key] = wording[key]
        localized = {"locale": locale, "revision": "osat-cold-" + locale + "-v1", "copy": public,
                     "protected_literals": ["Digiwin", "OSAT", "ERP"],
                     "rationale": [{"card_id": card["card_id"], "reader_intent": "Reconcile production records before financial close, without implying automatic integration.",
                                    "adaptation_note": wording["note"], "reader_question": wording["question"]}]}
        path = BASE / "examples" / (locale + ".json")
        path.parent.mkdir(parents=True, exist_ok=True)
        raw = adapter.encode(localized)
        if path.exists() and path.read_bytes() != raw:
            raise ValueError("Existing authored example changed; use a new revision")
        path.write_bytes(raw)
        subprocess.run([sys.executable, "-B", str(ROOT / "scripts/prepare_linkedin_locale.py"),
                        "--contract", str(SOURCE / "contract.json"), "--copy", str(SOURCE / "public-copy.json"),
                        "--spec", str(SOURCE / "spec.json"), "--localization", str(path),
                        "--out", "operations/linkedin-locale-adapter/drafts/" + locale], check=True)


if __name__ == "__main__":
    main()
