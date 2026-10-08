"""Offline locale drafts around the frozen gate. No review, release or generation."""
from __future__ import annotations

import argparse
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
CORE_SHA = "9817e828f35e832e99e15f36f4b2cbd227b625b626dc84c72f781e680c2b4dca"
PROFILES = ROOT / "operations/linkedin-locale-adapter/profiles.json"
FIELDS = ("headline", "body", "source_text", "cta", "native_headline", "alt", "artwork_labels")
ART_FIELDS = ("headline", "body", "source_text", "cta", "artwork_labels")


def require(ok, message):
    if not ok:
        raise ValueError(message)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encode(value):
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def load(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, "Duplicate JSON key: " + key)
            result[key] = value
        return result
    return json.loads(Path(path).read_text(encoding="utf-8-sig"), object_pairs_hook=unique)


def flatten_copy(value):
    words = []
    for ad in value["ads"]:
        words.append(ad["caption"])
        for card in ad["cards"]:
            for field in FIELDS:
                words.extend(card[field] if field == "artwork_labels" else [card[field]])
    return "\n".join(words)


def build(contract, source, spec, localized, profiles, out_relative):
    """Keep scenes/order/reference roles; explicit author-supplied localized copy."""
    locale = localized["locale"]
    require(locale in profiles["locales"], "Unsupported locale")
    profile = profiles["locales"][locale]
    revision = localized["revision"]
    require(isinstance(revision, str) and re.fullmatch(r"[A-Za-z0-9_-]+", revision), "Invalid revision")
    target = copy.deepcopy(localized["copy"])
    require(target["schema_version"] == source["schema_version"] == 1, "Wrong copy schema")
    require(target["revision"] != source["revision"], "New copy revision required")
    require([a["ad_id"] for a in target["ads"]] == contract["ad_order"] == [a["ad_id"] for a in source["ads"]], "Ad order changed")
    cards, replacements = {}, {}
    for old, new in zip(source["ads"], target["ads"]):
        require(set(new) == {"ad_id", "caption", "cards"}, "Unexpected ad fields")
        require([c["card_id"] for c in new["cards"]] == contract["card_order"][new["ad_id"]] == [c["card_id"] for c in old["cards"]], "Storyboard card order changed")
        require(isinstance(new["caption"], str) and len(new["caption"]) <= contract["limits"]["caption"], "Caption limit/type")
        for before, after in zip(old["cards"], new["cards"]):
            require(set(after) == {"card_id", *FIELDS}, "Unexpected card fields")
            cards[after["card_id"]] = after
            for field in FIELDS:
                vals = after[field] if field == "artwork_labels" else [after[field]]
                require(isinstance(after[field], list) if field == "artwork_labels" else isinstance(after[field], str), "Wrong field type")
                require(all(isinstance(v, str) and len(v) <= contract["limits"][field] for v in vals), "Field limit/type: " + field)
            require(len(before["artwork_labels"]) == len(after["artwork_labels"]), "Label role count changed")
            for field in ART_FIELDS:
                old_vals = before[field] if field == "artwork_labels" else [before[field]]
                new_vals = after[field] if field == "artwork_labels" else [after[field]]
                for a, b in zip(old_vals, new_vals):
                    if a:
                        require(a not in replacements or replacements[a] == b, "Conflicting repeated artwork wording")
                        replacements[a] = b
    original_text, target_text = flatten_copy(source), flatten_copy(target)
    require(not any(c in target_text for c in "\u2013\u2014"), "PO dash policy")
    # Does not prove claim equivalence; protects exact tokens while human review is pending.
    token = r"https?://[^\s]+|\d+(?:[.,]\d+)*"
    require(sorted(re.findall(token, original_text)) == sorted(re.findall(token, target_text)), "Numeric/URL tokens changed")
    for literal in localized["protected_literals"]:
        require(isinstance(literal, str) and literal and original_text.count(literal) > 0, "Invalid protected literal")
        require(original_text.count(literal) == target_text.count(literal), "Protected entity changed: " + literal)
    rationales = localized["rationale"]
    require([r["card_id"] for r in rationales] == list(cards), "One ordered rationale per card required")
    for r in rationales:
        for key in ("reader_intent", "adaptation_note", "reader_question"):
            require(isinstance(r[key], str) and bool(r[key].strip()), "Missing locale rationale")
    candidate = copy.deepcopy(contract)
    candidate["revision"] = revision + "-contract"
    candidate["locale"] = locale
    candidate["definitions"] = copy.deepcopy(profile["definitions"])
    candidate["copy"] = {"path": out_relative + "/public-copy.draft.json", "sha256": sha(encode(target)), "revision": target["revision"]}
    candidate["output"]["directory"] = out_relative + "/native-pending-review"
    # Edit language instructions only; frozen visual grammar remains around them.
    def adapt_style(text):
        for a, b in sorted(replacements.items(), key=lambda item: -len(item[0])):
            text = text.replace(a, b)
        text = text.replace("Preserve Vietnamese accents exactly.", profile["typography"])
        text = text.replace("two-line", "readable")
        require("Vietnamese" not in text, "Unresolved Vietnamese style instruction")
        return text
    candidate["style"]["brand"] = adapt_style(candidate["style"]["brand"])
    campaign = candidate["style"].setdefault("campaign", {"revision": revision, "instructions": "Preserve the source visual grammar."})
    campaign["revision"] = revision + "-locale-style"
    campaign["instructions"] = adapt_style(campaign["instructions"]) + "\nLOCALE: " + locale + ". " + profile["prompt_guidance"] + " " + profile["typography"]
    calls = copy.deepcopy(spec["calls"])
    require([c["targets"] for c in calls] == contract["groups"], "Source call/storyboard coverage changed")
    by_card = {r["card_id"]: r for r in rationales}
    for call in calls:
        require(call["references"] == contract["references"], "Source reference roles changed")
        require([c["card_id"] for c in call["concepts"]] == call["targets"], "Source concept order changed")
        for concept in call["concepts"]:
            concept["reader_question"] = by_card[concept["card_id"]]["reader_question"]
            concept["artwork_labels"] = cards[concept["card_id"]]["artwork_labels"]
        call["artwork_text"] = {cid: {f: cards[cid][f] for f in ART_FIELDS} for cid in call["targets"]}
        call["call_id"] += "_" + revision
        call["output_id"] += "_" + revision
        call["output_path"] = candidate["output"]["directory"] + "/" + call["output_id"] + ".png"
        call.pop("prompt", None)
        call.pop("prompt_sha256", None)
    return candidate, target, calls


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ("contract", "copy", "spec", "localization", "out"):
        parser.add_argument("--" + name, required=True)
    args = parser.parse_args()
    out = (ROOT / args.out).resolve()
    require(out.is_relative_to(ROOT) and out != ROOT and not out.exists(), "Use a new repo-local output directory")
    core = ROOT / "scripts/verify_imagegen_preflight.py"
    require(sha(core.read_bytes()) == CORE_SHA, "Frozen core changed; reconcile before using adapter")
    paths = [Path(getattr(args, key)).resolve() for key in ("contract", "copy", "spec", "localization")]
    require(all(p.is_relative_to(ROOT) for p in paths), "Inputs must be repo-local")
    inputs = [load(p) for p in paths]
    require(inputs[0]["copy"]["sha256"] == sha(paths[1].read_bytes()) and inputs[0]["copy"]["revision"] == inputs[1]["revision"], "Source copy pin mismatch")
    require(inputs[2]["contract"]["sha256"] == sha(paths[0].read_bytes()) and inputs[2]["contract"]["revision"] == inputs[0]["revision"], "Source contract pin mismatch")
    require(inputs[2]["copy"] == inputs[0]["copy"], "Source spec copy mismatch")
    profile = load(PROFILES)
    contract, target, calls = build(*inputs, profile, out.relative_to(ROOT).as_posix())
    module_spec = importlib.util.spec_from_file_location("frozen_gate", core)
    gate = importlib.util.module_from_spec(module_spec)
    module_spec.loader.exec_module(gate)
    for call in calls:
        call["prompt"] = gate.make_prompt(contract, call)
        call["prompt_sha256"] = sha(call["prompt"].encode("utf-8"))
    manifest = {"status": "LOCALIZATION_DRAFT_REVIEW_REQUIRED", "locale": inputs[3]["locale"], "core_sha256": CORE_SHA,
                "source_inputs": [{"path": p.relative_to(ROOT).as_posix(), "sha256": sha(p.read_bytes())} for p in paths],
                "profile_sha256": sha(PROFILES.read_bytes()), "adapter_sha256": sha(Path(__file__).read_bytes()), "rationale": inputs[3]["rationale"],
                "pending": ["native market/domain copy review", "claim and protected-entity scope", "first mention per surface with ASCII parentheses", "fresh editorial review/release/pins", "native PNG glyph and 333px layout review", "destination locale and journey continuity"]}
    out.mkdir(parents=True)
    for name, obj in (("contract.draft.json", contract), ("public-copy.draft.json", target), ("calls.draft.json", {"status": manifest["status"], "calls": calls}), ("manifest.json", manifest)):
        (out / name).write_bytes(encode(obj))
    print(manifest["status"] + ": " + out.relative_to(ROOT).as_posix())


if __name__ == "__main__":
    main()
