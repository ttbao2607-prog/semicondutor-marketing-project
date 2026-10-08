"""Developing anchor/script guard before ImageGen. Frozen gate stays unchanged."""
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path
import re
import sys

CORE_PATH = "scripts/verify_imagegen_preflight.py"
CORE_SHA = "9817e828f35e832e99e15f36f4b2cbd227b625b626dc84c72f781e680c2b4dca"
SINGLE_PATH = "operations/linkedin-journey-demo/2026-10-06/inputs/verify_single_image_trial.py"
SINGLE_SHA = "aa71327c78dd2db4cf436bd9454003960492657b627a3bf36901a467bb75b72c"
ANCHOR_PATH = "operations/Vy_Email_Content_Anchor.md"
SOURCE_PATH = "operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md"
# Built-in ImageGen rejected six local reference paths in the 2026-10-06 pilot.
# Keep this tool boundary outside the frozen mechanical core and locale adapter.
TOOL_MAX_REFERENCE_IMAGES = 5


def module(path):
    spec = importlib.util.spec_from_file_location("bounded_imagegen_gate", path)
    result = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(result)
    return result


def check(root, release_path, release_sha, spec_path, review_path, review_sha,
          call_id, segment, persona, route):
    root = Path(root).resolve()
    if hashlib.sha256((root / CORE_PATH).read_bytes()).hexdigest() != CORE_SHA:
        raise ValueError("Frozen core changed")
    core = module(root / CORE_PATH)
    files = core.Inputs(root)
    files.read(CORE_PATH, CORE_SHA)
    # The caller supplies both trusted SHAs; this script never creates approval.
    review = files.json(review_path, review_sha)
    release = files.json(release_path, release_sha)
    contract = files.ref(release["contract"])
    gate = core
    if contract["channel"] == "linkedin-single-image":
        files.read(SINGLE_PATH, SINGLE_SHA)
        gate = module(root / SINGLE_PATH)
    mechanical, state = gate.validate(root, release_path, release_sha, spec_path, scope_call_id=call_id)
    core.require(call_id in mechanical["call_ids"], "Unknown selected call")
    core.shape(review, ("schema_version", "revision", "gate_id", "stage", "verdict", "anchor", "source", "subjects", "scope", "writer", "reviewer", "independence", "coverage", "rules", "units", "transitions", "context", "unresolved_findings"))
    core.schema_version(review["schema_version"])
    core.require(review["gate_id"] == "MSG-ANCHOR-01" and review["stage"] == "PREGEN_SCRIPT", "Wrong anchor review stage")
    core.require(review["verdict"] == "MESSAGE_ANCHOR_PASS", "Anchor review has not passed")
    core.require(review["unresolved_findings"] == [], "Unresolved anchor findings")
    for key in ("revision", "writer", "reviewer"):
        core.text(review[key], key)
        core.require(review[key].strip().upper() not in ("UNKNOWN", "PENDING", "TEMPLATE"), "Unfilled review metadata: " + key)
    expected_independence = "SELF_REVIEW" if review["writer"] == review["reviewer"] else "INDEPENDENT"
    core.require(review["independence"] == expected_independence, "False reviewer independence")
    core.require(segment in ("VN_DOMESTIC", "FDI"), "Unsupported segment")
    core.text(persona, "specific persona")
    core.text(route, "route")
    locale = contract["locale"]
    core.require(locale in (("vi", "vi-VN") if segment == "VN_DOMESTIC" else ("en", "zh-Hans", "zh-Hant")), "Segment/locale mismatch")
    core.require(review["scope"] == {"segment": segment, "locale": locale, "persona": persona, "route": route}, "Persona/locale/route review is stale")
    core.require(review["anchor"]["path"] == ANCHOR_PATH, "Noncanonical anchor")
    core.require(review["source"]["path"] == SOURCE_PATH, "Noncanonical email source")
    anchor = files.read(ANCHOR_PATH, review["anchor"]["sha256"]).decode("utf-8-sig")
    version = re.search(r"Revision:\s*\*\*([^*]+)\*\*", anchor)
    core.require(version is not None and review["anchor"]["revision"] == version.group(1), "Anchor revision mismatch")
    core.require("VY-CONTENT-ANCHOR" in anchor, "Wrong anchor identity")
    core.require(review["source"]["revision"] == "VY-MAIL-USER-20261006", "Wrong source record")
    files.read(SOURCE_PATH, review["source"]["sha256"])
    subjects = review["subjects"]
    core.shape(subjects, ("contract", "copy", "spec", "script_review"))
    for key in ("contract", "copy"):
        core.require(subjects[key] == release[key], "Anchor review subject changed: " + key)
        files.ref(subjects[key])
    core.require(subjects["spec"]["path"] == spec_path, "Different reviewed storyboard/spec")
    files.ref(subjects["spec"])
    script = files.ref(subjects["script_review"])
    core.require(script.get("gate_id") == "AD-ED-01" and script.get("stage") == "PREGEN_SCRIPT" and script.get("verdict") == "SCRIPT_REVIEW_PASS", "Script not reviewed before generation")
    core.require(script.get("copy_sha256") == release["copy"]["sha256"], "Script copy changed")
    for criterion in ("BRAND_ROLE", "ADVERTISER_VOICE"):
        core.require(script.get(criterion, {}).get("verdict") == "PASS", "Script criterion not passed: " + criterion)
    ads = state["copy"]["ads"]
    cards = [card["card_id"] for ad in ads for card in ad["cards"]]
    fields = {ad["ad_id"]: ["caption"] + [card["card_id"] + "." + field for card in ad["cards"] for field in core.CARD_FIELDS] for ad in ads}
    expected_coverage = {"ads": [ad["ad_id"] for ad in ads], "cards": cards, "fields": fields, "storyboard_cards": cards}
    core.require(review["coverage"] == expected_coverage, "Incomplete script/field/storyboard coverage")
    core.require(script.get("reviewed_ads") == expected_coverage["ads"] and script.get("reviewed_fields") == fields, "Incomplete editorial script coverage")
    core.require(set(review["rules"]) == {"A" + str(i) for i in range(1, 8)}, "Missing anchor rules")
    for rule, observation in review["rules"].items():
        core.text(observation.get("observation"), rule + " concrete observation")
        allowed = ("MATCH", "N/A") if rule == ("A4" if segment == "VN_DOMESTIC" else "A5") else ("MATCH",)
        core.require(observation.get("verdict") in allowed, "Anchor criterion unresolved: " + rule)
    core.require([u.get("card_id") for u in review["units"]] == cards, "Missing per-card script review")
    for unit in review["units"]:
        core.require(unit.get("verdict") == "MATCH", "Card message not matched")
        core.text(unit.get("observation"), "card observation")
    transitions = [[a["card_id"], b["card_id"]] for ad in ads for a, b in zip(ad["cards"], ad["cards"][1:])]
    core.require([t.get("cards") for t in review["transitions"]] == transitions, "Missing story transitions")
    for transition in review["transitions"]:
        core.require(transition.get("verdict") == "MATCH", "Story transition unresolved")
        core.text(transition.get("observation"), "transition observation")
    context = review["context"]
    core.require(context.get("scope") in ("STANDALONE", "FULL_JOURNEY"), "Declare journey review scope")
    core.require(context.get("verdict") == "MATCH", "Journey/standalone intent not matched")
    core.text(context.get("observation"), "journey observation")
    files.ref(context["brief"], False)
    core.require(isinstance(context.get("related_inputs"), list), "Journey source pins required")
    if context["scope"] == "FULL_JOURNEY":
        core.require(bool(context["related_inputs"]), "Full journey must bind other stage inputs")
    for ref in context["related_inputs"]:
        files.ref(ref, False)
    files.recheck()
    state["inputs"].recheck()
    call = next(c for c in state["spec"]["calls"] if c["call_id"] == call_id)
    core.require(len(call["references"]) <= TOOL_MAX_REFERENCE_IMAGES,
                 "ImageGen tool supports at most 5 reference images; revise and review the reference pack before dispatch")
    payload = None if release["purpose"] == "FIXTURE_ONLY" else {"prompt": call["prompt"], "referenced_image_paths": [str(files.path(r["path"])) for r in call["references"]], "transparent_background": False}
    return {"layer": "PREGEN_ANCHOR_SCRIPT_CHECK", "status": "PREGEN_INPUTS_VERIFIED", "call_id": call_id,
            "scope": review["scope"], "anchor": review["anchor"], "message_review_sha256": review_sha,
            "script_review": subjects["script_review"], "input_hashes": {**mechanical["input_hashes"], **files.hashes},
            "mechanical_verdict": "PASS", "message_review_binding": "PASS", "semantic_verdict": "REVIEWER_ATTESTED_NOT_AUTOMATICALLY_ASSESSED",
            "purpose": release["purpose"], "authority": "NO_ADDITIONAL_GENERATION_AUTHORITY", "tool_args": payload}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", default=".")
    for key in ("release", "release-sha256", "spec", "message-review", "message-review-sha256", "call-id", "segment", "persona", "route"):
        parser.add_argument("--" + key, required=True)
    args = parser.parse_args()
    try:
        result = check(args.root, args.release, args.release_sha256, args.spec, args.message_review,
                       args.message_review_sha256, args.call_id, args.segment, args.persona, args.route)
    except (ValueError, OSError, KeyError, TypeError, AttributeError, StopIteration) as exc:
        print(json.dumps({"status": "PREGEN_BLOCKED", "reason": str(exc), "tool_args": None}, ensure_ascii=True))
        return 1
    print(json.dumps(result, ensure_ascii=True, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
