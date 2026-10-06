"""Contract-bound offline ImageGen input checks. No generation or rendering.

The coordinator supplies the trusted release SHA independently of call inputs.
PASS covers mechanics only; actual rasters still need source/editorial/creative QA.
"""
from __future__ import annotations

import argparse
from collections import Counter
import hashlib
import json
from pathlib import Path, PureWindowsPath
import re
import struct
import zlib
import sys

VERSION = 1
CARD_FIELDS = ("headline", "body", "source_text", "cta", "native_headline", "alt", "artwork_labels")
ART_FIELDS = ("headline", "body", "source_text", "cta", "artwork_labels")
TERMS = ("OSAT", "Fabless", "WIP")  # Current PO policy; ERP/MES deliberately exempt.
ROLES = {"palette", "lighting", "brand_asset", "campaign_visual", "closing_layout"}
CAMPAIGN_ATTRIBUTES = {"colors", "lighting", "shadows", "material_depth", "typography_hierarchy", "campaign_identity", "scene_diagram_integration"}
CLOSING_ATTRIBUTES = {"layout_hierarchy", "source_full_width", "source_body_hierarchy", "cta_separation"}


class Invalid(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise Invalid(message)


def shape(value, required, optional=()):
    require(isinstance(value, dict), "Expected object")
    keys = set(value)
    require(set(required) <= keys, f"Missing fields: {sorted(set(required) - keys)}")
    require(keys <= set(required) | set(optional), f"Unexpected fields: {sorted(keys - set(required) - set(optional))}")


def text(value, label):
    require(isinstance(value, str) and bool(value.strip()), f"{label}: nonempty string required")
    return value


def string_list(value, label, nonempty=True):
    require(isinstance(value, list), f"{label}: list required")
    if nonempty:
        require(bool(value), f"{label}: empty list")
    for item in value:
        text(item, label)
    require(len(value) == len(set(value)), f"{label}: duplicates")
    return value


def schema_version(value):
    require(type(value) is int and value == VERSION, "Unsupported schema version")


def digest(data):
    return hashlib.sha256(data).hexdigest()


def canonical(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":"))


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, f"Duplicate JSON key: {key}")
        result[key] = value
    return result


class Inputs:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.hashes = {}

    def path(self, name):
        text(name, "path")
        require(not PureWindowsPath(name).drive and not Path(name).is_absolute(), "Paths must be repo-relative")
        path = (self.root / name.replace("\\", "/")).resolve()
        require(path.is_relative_to(self.root) and path != self.root, "Path escapes repo")
        return path

    def read(self, name, expected=None):
        path = self.path(name)
        require(path.is_file(), f"Missing input: {name}")
        raw = path.read_bytes()
        sha = digest(raw)
        if expected is not None:
            require(isinstance(expected, str) and re.fullmatch(r"[0-9a-f]{64}", expected), "Invalid SHA-256")
            require(sha == expected, f"Changed input: {name}")
        key = path.relative_to(self.root).as_posix()
        if key in self.hashes:
            require(self.hashes[key] == sha, f"Input changed during check: {name}")
        self.hashes[key] = sha
        return raw

    def json(self, name, expected=None):
        try:
            result = json.loads(self.read(name, expected).decode("utf-8-sig"), object_pairs_hook=unique_object)
        except (UnicodeError, json.JSONDecodeError) as exc:
            raise Invalid(f"Invalid JSON: {name}") from exc
        require(isinstance(result, dict), f"JSON object required: {name}")
        return result

    def ref(self, ref, json_file=True):
        shape(ref, ("path", "sha256", "revision"))
        text(ref["revision"], "revision")
        if json_file:
            result = self.json(ref["path"], ref["sha256"])
            require(result.get("revision") == ref["revision"], f"Revision mismatch: {ref['path']}")
            return result
        self.read(ref["path"], ref["sha256"])

    def recheck(self):
        for name, sha in list(self.hashes.items()):
            self.read(name, sha)


def artwork(card):
    return {key: card[key] for key in ART_FIELDS}


def make_prompt(contract, call):
    """One bounded assembly contract; no copied reference composition or internal ledger."""
    campaign_guidance = ("Campaign visual references guide only reviewed material depth, typography/header identity and scene-integrated diagrams.\n"
                         "Palette/lighting references supply only their declared colors, lighting and shadows.\n"
                         "Never copy reference words, record data, exact composition or mandatory props.\n") if "campaign" in contract["style"] else ""
    closing_guidance = ("CLOSING STRUCTURAL GUIDE\n"
                        "The independently reviewed closing_layout reference is an exception only for declared structural hierarchy: source full width, source/body hierarchy and CTA separation.\n"
                        "Do not transfer its wording, data, objects, fixed counts or exact photographic composition. Use cohort-appropriate grounded scenes and integrated diagrams.\n"
                        "Print only approved words, source once, no added punctuation or diagram labels. Source must be at least body-sized and comfortable without zoom at ordinary 333px display, full width, never a footnote.\n"
                        "No skyline or icon column may narrow the source. Reduce photo/diagram area before reducing type; keep CTA separate.\n") if "closing" in contract["style"] else ""
    output_guidance = ("\nOUTPUT REQUIREMENT\n"
                       + canonical(contract["output"]) + "\n"
                       + "Create one square native PNG with minimum edge " + str(contract["output"]["min_edge"])
                       + " pixels. Preserve original native bytes; no resizing or compositing to meet this requirement.") if contract["output"].get("policy") == "native_square_min" else ""
    return ("Create the approved carousel artwork. Use only approved artwork text for printed wording.\n"
            "References supply only their declared attributes; never copy reference wording, record data or composition.\n"
            + campaign_guidance + closing_guidance + "STYLE\n" + canonical(contract["style"]) + "\n"
            "REFERENCE ROLES\n" + canonical(call["references"]) + "\n"
            "CARD CONCEPTS (not printed labels)\n" + canonical(call["concepts"]) + "\n"
            "APPROVED ARTWORK TEXT\n" + canonical(call["artwork_text"]) + output_guidance)


def validate(root, release_path, release_sha256, spec_path, scope_call_id=None, protect_outputs=True):
    inputs = Inputs(root)
    release = inputs.json(release_path, release_sha256)
    shape(release, ("schema_version", "revision", "authorizer", "authority_ref", "purpose", "contract", "copy", "review", "groups"))
    schema_version(release["schema_version"])
    text(release["revision"], "release revision")
    text(release["authorizer"], "authorizer")
    require(release["purpose"] in ("FIXTURE_ONLY", "OFFLINE_IMAGEGEN"), "Unsupported release purpose")
    inputs.ref(release["authority_ref"], False)
    contract = inputs.ref(release["contract"])
    copy = inputs.ref(release["copy"])
    review = inputs.ref(release["review"])
    shape(contract, ("schema_version", "revision", "locale", "channel", "copy", "sources", "card_sources", "ad_order", "card_order", "surfaces", "definitions", "limits", "groups", "reuse_fields", "references", "style", "output"))
    schema_version(contract["schema_version"])
    require(contract["channel"] in ("linkedin-carousel", "linkedin-single-image"), "Unsupported campaign channel")
    if contract["channel"] == "linkedin-single-image":
        require(len(contract["ad_order"]) == 1, "Single image trial requires one ad")
        require(all(len(cards) == 1 for cards in contract["card_order"].values()), "Single image trial requires one card per ad")
        require(len(contract["groups"]) == 1 and len(contract["groups"][0]) == 1, "Single image trial requires one call target")
    text(contract["locale"], "locale")
    require(contract["copy"] == release["copy"], "Contract copy differs from trusted release")
    require(isinstance(contract["sources"], list) and contract["sources"], "Source pins required")
    source_paths = []
    for ref in contract["sources"]:
        inputs.ref(ref, False)
        source_paths.append(ref["path"])
    require(len(set(source_paths)) == len(source_paths), "Duplicate source pins")

    shape(review, ("schema_version", "revision", "writer", "reviewer", "date", "scope", "independence", "subjects", "verdicts", "reviewed_ads", "reviewed_fields", "unresolved_findings"))
    schema_version(review["schema_version"])
    for key in ("writer", "reviewer", "date"):
        text(review[key], key)
    require(review["scope"] == "OFFLINE_SOURCE_COPY", "Wrong review scope")
    require(review["independence"] in ("SELF_REVIEW", "INDEPENDENT"), "Review independence missing")
    if review["independence"] == "INDEPENDENT":
        require(review["writer"] != review["reviewer"], "Self-review cannot be labelled independent")
    shape(review["subjects"], ("contract", "copy", "sources"))
    require(review["subjects"] == {"contract": release["contract"], "copy": release["copy"], "sources": contract["sources"]}, "Review subjects differ from released inputs")
    require(review["verdicts"] == {"source_copy": "PASS", "editorial": "PASS", "first_mention": "PASS"}, "Review not passed")
    require(review["unresolved_findings"] == [], "Unresolved source/copy/editorial findings")

    shape(copy, ("schema_version", "revision", "ads"))
    schema_version(copy["schema_version"])
    require(isinstance(copy["ads"], list), "Invalid copy schema")
    ad_order = string_list(contract["ad_order"], "ad_order")
    require(review["reviewed_ads"] == ad_order, "Incomplete ad review")
    shape(contract["card_order"], ad_order)
    shape(contract["surfaces"], ad_order)
    shape(contract["definitions"], TERMS)
    for term in TERMS:
        text(contract["definitions"][term], term + " definition")
    shape(contract["limits"], ("caption",) + CARD_FIELDS)
    for limit in contract["limits"].values():
        require(type(limit) is int and limit > 0, "Positive integer field limit required")
    require([ad.get("ad_id") for ad in copy["ads"] if isinstance(ad, dict)] == ad_order, "Ad order/identity mismatch")
    cards = {}
    advisories = []
    reviewed_fields = []
    for ad in copy["ads"]:
        shape(ad, ("ad_id", "caption", "cards"))
        aid = ad["ad_id"]
        require(isinstance(ad["cards"], list), "Cards must be a list")
        ids = string_list(contract["card_order"][aid], "card_order")
        require([c.get("card_id") for c in ad["cards"] if isinstance(c, dict)] == ids, "Card order/identity mismatch")
        fields = {"caption": ad["caption"]}
        for card in ad["cards"]:
            shape(card, ("card_id",) + CARD_FIELDS)
            cid = text(card["card_id"], "card_id")
            require(cid not in cards, "Card IDs must be globally unique")
            require(re.fullmatch(r"[A-Za-z0-9_-]+", cid), "Invalid card ID")
            cards[cid] = card
            for key in CARD_FIELDS:
                fields[cid + "." + key] = card[key]
        reviewed_fields.extend(aid + "/" + key for key in fields)
        for locator, value in fields.items():
            field = locator.split(".")[-1]
            values = string_list(value, locator, False) if field == "artwork_labels" else [value]
            for wording in values:
                require(isinstance(wording, str), "Visible text must be strings")
                require(len(wording) <= contract["limits"][field], f"Field limit exceeded: {aid}/{locator}")
                require(not any(char in wording for char in "\u2013\u2014"), f"Forbidden visible dash: {aid}/{locator}")
                if re.search(r"hypothesis|pending approval|chưa xác minh|không chắc.*áp dụng|theo quy tắc repo", wording, re.I):
                    advisories.append(f"EDITORIAL_SEMANTIC_REVIEW: {aid}/{locator}")
        surfaces = contract["surfaces"][aid]
        require(isinstance(surfaces, list) and surfaces, "Declared ad delivery surfaces required")
        seen_surfaces, coverage = set(), set()
        for surface in surfaces:
            shape(surface, ("surface_id", "reading_order"))
            sid = text(surface["surface_id"], "surface_id")
            require(sid not in seen_surfaces, "Duplicate surface ID")
            seen_surfaces.add(sid)
            order = string_list(surface["reading_order"], "reading_order")
            require(set(order) <= set(fields), "Unknown reading-order field")
            coverage.update(order)
            explained = set()  # Fresh state for each ad AND each independently delivered surface.
            for locator in order:
                value = fields[locator]
                value = " ".join(value) if isinstance(value, list) else value
                for term in TERMS:
                    # CJK letters are Unicode word characters: \b would miss OSAT业务.
                    match = re.search(r"(?<![A-Za-z0-9_])" + term + r"(?![A-Za-z0-9_])", value, re.I)
                    if match and term not in explained:
                        definition = contract["definitions"][term]
                        require(re.match(r"\s*\(\s*" + re.escape(definition) + r"\s*\)", value[match.end():], re.I), f"Unexplained first mention: {aid}/{sid}/{locator}/{term}")
                        explained.add(term)
        require(coverage == set(fields), "Visible fields omitted from delivery-surface checks")

    require(review["reviewed_fields"] == reviewed_fields, "Incomplete visible-field review attestation")

    shape(contract["card_sources"], cards)
    for cid, refs in contract["card_sources"].items():
        string_list(refs, "card_sources", False)
        require(set(refs) <= set(source_paths), f"Unpinned source mapping: {cid}")
        if cards[cid]["source_text"]:
            require(bool(refs), f"Source text lacks source mapping: {cid}")
    groups = contract["groups"]
    require(isinstance(groups, list) and groups, "Declared call groups required")
    reuse_fields = string_list(contract["reuse_fields"], "reuse_fields")
    require(set(ART_FIELDS) <= set(reuse_fields) <= set(CARD_FIELDS), "Reuse must preserve artwork fields; optional native/alt reuse is contract-bound")
    all_targets = []
    for group in groups:
        string_list(group, "call group")
        all_targets.extend(group)
        first = {k: cards[group[0]][k] for k in reuse_fields} if group[0] in cards else None
        for cid in group:
            require(cid in cards, "Unknown grouped card")
            require({k: cards[cid][k] for k in reuse_fields} == first, "Shared call approved reuse fields differ")
    require(Counter(all_targets) == Counter(cards.keys()), "Campaign groups must cover every card exactly once")
    allowed_groups = release["groups"]
    require(isinstance(allowed_groups, list) and allowed_groups, "Released target subset required")
    for group in allowed_groups:
        string_list(group, "released group")
        require(group in groups, "Release group absent from reviewed contract")
    require(len({tuple(g) for g in allowed_groups}) == len(allowed_groups), "Duplicate released group")

    refs = contract["references"]
    require(isinstance(refs, list) and refs, "Reviewed references required")
    ref_keys = set()
    for ref in refs:
        shape(ref, ("path", "sha256", "revision", "role", "attributes"))
        require(ref["role"] in ROLES, "Unsupported reference role")
        string_list(ref["attributes"], "reference attributes")
        if ref["role"] == "campaign_visual":
            require(set(ref["attributes"]) <= CAMPAIGN_ATTRIBUTES, "Campaign reference cannot transfer wording/data/props/exact composition")
            require("campaign" in contract["style"], "Campaign reference requires reviewed campaign style")
        if ref["role"] == "closing_layout":
            require(set(ref["attributes"]) <= CLOSING_ATTRIBUTES, "Closing reference cannot transfer wording/data/props/exact composition")
            require("closing" in contract["style"], "Closing reference requires reviewed closing style")
        require(ref["role"] not in ("palette", "lighting") or set(ref["attributes"]) <= {"colors", "lighting", "shadows"}, "Style-only role cannot transfer composition/text/props")
        inputs.ref({k: ref[k] for k in ("path", "sha256", "revision")}, False)
        identity = (str(inputs.path(ref["path"])), ref["role"])
        require(identity not in ref_keys, "Duplicate reference role")
        ref_keys.add(identity)
    shape(contract["style"], ("brand", "palette", "lighting", "avoid"), ("campaign", "closing"))
    if "campaign" in contract["style"]:
        shape(contract["style"]["campaign"], ("revision", "instructions"))
        for key in ("revision", "instructions"):
            text(contract["style"]["campaign"][key], "campaign " + key)
    closing_refs = [r for r in refs if r["role"] == "closing_layout"]
    if "closing" in contract["style"]:
        closing = contract["style"]["closing"]
        shape(closing, ("revision", "instructions", "reference", "cards"))
        text(closing["revision"], "closing revision")
        text(closing["instructions"], "closing instructions")
        string_list(closing["cards"], "closing cards")
        require(len(closing_refs) == 1, "Closing style requires exactly one closing layout anchor")
        anchor = {k: closing_refs[0][k] for k in ("path", "sha256", "revision")}
        require(closing["reference"] == anchor, "Closing style reference differs from reviewed anchor")
        last_cards = {order[-1] for order in contract["card_order"].values()}
        require(set(closing["cards"]) <= last_cards, "Closing guide restricted to last card per ad")
        for cid in closing["cards"]:
            require(cards[cid]["source_text"].strip() and cards[cid]["cta"].strip(), "Closing card requires nonempty source and CTA")
        require(all(set(group) <= set(closing["cards"]) for group in allowed_groups), "Closing anchor release must select closing cards only")
    for key in ("brand", "lighting"):
        text(contract["style"][key], "style " + key)
    for key in ("palette", "avoid"):
        string_list(contract["style"][key], "style " + key, False)
    validate_output_policy(contract["output"])
    output_dir = inputs.path(contract["output"]["directory"])

    spec = inputs.json(spec_path)
    shape(spec, ("schema_version", "revision", "release", "contract", "copy", "review", "calls"))
    schema_version(spec["schema_version"])
    text(spec["revision"], "call revision")
    require(spec["release"] == {"path": release_path, "sha256": release_sha256, "revision": release["revision"]}, "Call spec cannot choose a different trusted release")
    for key in ("contract", "copy", "review"):
        require(spec[key] == release[key], f"Spec {key} differs from trusted release")
    calls = spec["calls"]
    require(isinstance(calls, list) and len(calls) == len(allowed_groups), "Wrong released call count")
    require([c.get("targets") for c in calls if isinstance(c, dict)] == allowed_groups, "Wrong released coverage/reuse/order")
    call_ids, output_paths, concepts = set(), set(), []
    for call in calls:
        shape(call, ("call_id", "targets", "references", "concepts", "artwork_text", "prompt", "prompt_sha256", "output_id", "output_path"))
        cid = text(call["call_id"], "call_id")
        require(cid not in call_ids, "Duplicate call ID")
        call_ids.add(cid)
        require(call["references"] == refs, "Call reference identity/role differs from reviewed references")
        require(call["artwork_text"] == {target: artwork(cards[target]) for target in call["targets"]}, "Unapproved artwork wording/label")
        require(isinstance(call["concepts"], list), "Concept list required")
        require([c.get("card_id") for c in call["concepts"] if isinstance(c, dict)] == call["targets"], "Concept targets mismatch")
        for concept in call["concepts"]:
            shape(concept, ("card_id", "concept_id", "reader_question", "description", "props", "artwork_labels"))
            for key in ("concept_id", "reader_question", "description"):
                text(concept[key], key)
            string_list(concept["props"], "props", False)
            require(concept["artwork_labels"] == cards[concept["card_id"]]["artwork_labels"], "Concept labels not approved")
            concepts.append(concept)
        require(call["prompt"] == make_prompt(contract, call), "Prompt differs from assembled approved inputs")
        require(call["prompt_sha256"] == digest(call["prompt"].encode("utf-8")), "Prompt hash mismatch")
        oid = text(call["output_id"], "output_id")
        require(re.fullmatch(r"[A-Za-z0-9_-]+", oid), "Invalid output ID")
        path = inputs.path(call["output_path"])
        require(path == output_dir / (oid + ".png"), "Output outside reviewed destination or ID mismatch")
        key = str(path).casefold()
        require(key not in output_paths, "Duplicate output path/ID")
        output_paths.add(key)
        if protect_outputs and (scope_call_id is None or scope_call_id == cid):
            require(not path.exists(), "Planned output would overwrite existing artifact")
    require(scope_call_id is None or (isinstance(scope_call_id, str) and scope_call_id in call_ids), "Unknown preflight call scope")
    # Compare call-level concepts; approved exact reuse within a shared call is intentional.
    unique_concepts = [call["concepts"][0] for call in calls]
    for key in ("concept_id", "description"):
        if len({c[key].strip().casefold() for c in unique_concepts}) < len(unique_concepts):
            advisories.append("CONCEPT_REPETITION: " + key)
    if len(unique_concepts) > 1 and len({tuple(sorted(c["props"])) for c in unique_concepts}) == 1:
        advisories.append("PROP_REPETITION: inspect actual concepts, not just text/positions")
    inputs.recheck()
    receipt = {"schema_version": VERSION, "gate_version": VERSION, "gate_sha256": digest(Path(__file__).read_bytes()), "layer": "PREGEN", "mechanical_verdict": "PASS", "purpose": release["purpose"], "spec_path": spec_path, "release_path": release_path, "release_sha256": release_sha256, "scope_call_id": scope_call_id, "input_hashes": dict(sorted(inputs.hashes.items())), "call_ids": [c["call_id"] for c in calls], "advisories": sorted(set(advisories)), "semantic_verdict": "NOT_ASSESSED", "creative_verdict": "INSUFFICIENT_EVIDENCE", "authority": "NO_GENERATION_AUTHORITY"}
    return receipt, {"inputs": inputs, "contract": contract, "copy": copy, "spec": spec}


def validate_output_policy(output):
    """Missing policy preserves the original exact-size contract."""
    policy = output.get("policy", "exact")
    if policy == "exact":
        shape(output, ("directory", "extension", "width", "height"), ("policy",))
        for key in ("width", "height"):
            require(type(output[key]) is int and output[key] > 0, "Positive output dimensions required")
    elif policy == "native_square_min":
        shape(output, ("directory", "extension", "policy", "min_edge"))
        require(type(output["min_edge"]) is int and output["min_edge"] >= 1080, "Native square minimum must be >=1080")
    else:
        raise Invalid("Unsupported output policy")
    require(output["extension"] == ".png", "Only original PNG output planned")


def png_dimensions(raw):
    """Read PNG container dimensions with chunk CRC/bounds checks; no visual/provenance certification."""
    require(raw[:8] == b"\x89PNG\r\n\x1a\n", "Native output is not PNG")
    offset, dimensions, ended = 8, None, False
    while offset < len(raw):
        require(offset + 12 <= len(raw), "Truncated PNG chunk")
        length = int.from_bytes(raw[offset:offset + 4], "big")
        kind = raw[offset + 4:offset + 8]
        end = offset + 12 + length
        require(end <= len(raw), "Truncated PNG payload")
        payload = raw[offset + 8:offset + 8 + length]
        require(zlib.crc32(kind + payload) & 0xffffffff == int.from_bytes(raw[end - 4:end], "big"), "PNG chunk CRC mismatch")
        if dimensions is None:
            require(kind == b"IHDR" and length == 13, "PNG first chunk must be IHDR")
            dimensions = struct.unpack(">II", payload[:8])
            require(all(dimensions), "PNG dimensions must be positive")
        else:
            require(kind != b"IHDR", "Duplicate PNG IHDR")
        offset = end
        if kind == b"IEND":
            require(length == 0 and offset == len(raw), "Invalid PNG end/trailing bytes")
            ended = True
            break
    require(dimensions is not None and ended, "Incomplete PNG container")
    return dimensions


def check_dimensions(output, dimensions):
    validate_output_policy(output)
    width, height = dimensions
    if output.get("policy", "exact") == "native_square_min":
        require(width == height and width >= output["min_edge"], "Native output must be square and meet minimum edge")
    else:
        require((width, height) == (output["width"], output["height"]), "Native output differs from exact dimensions")


def native_output_check(root, release_path, release_sha256, spec_path, call_id):
    receipt, state = validate(root, release_path, release_sha256, spec_path, scope_call_id=call_id, protect_outputs=False)
    require(call_id is not None, "Native output check requires selected call")
    call = next(c for c in state["spec"]["calls"] if c["call_id"] == call_id)
    inputs = state["inputs"]
    raw = inputs.read(call["output_path"])
    dimensions = png_dimensions(raw)
    check_dimensions(state["contract"]["output"], dimensions)
    inputs.recheck()
    return {**receipt, "layer": "POSTGEN_DIMENSION_CHECK", "call_id": call_id,
            "output_path": call["output_path"], "native_sha256": digest(raw), "native_bytes": len(raw),
            "actual_dimensions": list(dimensions), "output_policy": state["contract"]["output"],
            "dimension_verdict": "PASS", "native_provenance_verdict": "NOT_ASSESSED",
            "rendered_artifact_verdict": "NOT_ASSESSED"}, state


def dispatch_check(root, release_path, release_sha256, spec_path, receipt_path, dispatch_path):
    check_files = Inputs(root)
    saved = check_files.json(receipt_path)
    proposal = check_files.json(dispatch_path)
    fresh, state = validate(root, release_path, release_sha256, spec_path, scope_call_id=saved.get("scope_call_id"), protect_outputs=False)
    inputs = state["inputs"]
    require(saved == fresh, "Stale or altered preflight receipt")
    shape(proposal, ("schema_version", "record_kind", "call_id", "preflight_sha256", "prompt", "prompt_sha256", "reference_paths", "output_path"))
    schema_version(proposal["schema_version"])
    require(proposal["record_kind"] == "PLANNED_DISPATCH_CHECK", "Not a planned dispatch check")
    receipt_key = check_files.path(receipt_path).relative_to(check_files.root).as_posix()
    require(proposal["preflight_sha256"] == check_files.hashes[receipt_key], "Dispatch receipt hash mismatch")
    calls = {c["call_id"]: c for c in state["spec"]["calls"]}
    require(proposal["call_id"] in calls, "Unreleased dispatch call")
    require(saved["scope_call_id"] is None or saved["scope_call_id"] == proposal["call_id"], "Dispatch differs from selected preflight call")
    call = calls[proposal["call_id"]]
    for field in ("prompt", "prompt_sha256", "output_path"):
        require(proposal[field] == call[field], f"Dispatch {field} differs from verified call")
    require(proposal["reference_paths"] == [r["path"] for r in call["references"]], "Dispatch reference paths differ")
    require(not inputs.path(call["output_path"]).exists(), "Selected output would overwrite existing artifact")
    inputs.recheck()
    check_files.recheck()
    return {**fresh, "layer": "DISPATCH_CHECK", "call_id": call["call_id"], "record_kind": "PLANNED_DISPATCH_CHECK", "actual_dispatch_observed": False}, state


def viewer_check(root, release_path, release_sha256, spec_path, viewer_path):
    receipt, state = validate(root, release_path, release_sha256, spec_path, protect_outputs=False)
    viewer = state["inputs"].json(viewer_path)
    # Exact public-copy projection: no internal keys, hidden payload or extra attachments.
    require(viewer == state["copy"], "Viewer payload differs from approved public-field projection")
    state["inputs"].recheck()
    return {**receipt, "layer": "VIEWER_PAYLOAD_CHECK", "rendered_artifact_verdict": "NOT_ASSESSED"}, state


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("preflight", "dispatch-check", "viewer-check", "native-output-check"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--release", required=True, help="Repo-relative trusted release file")
    parser.add_argument("--release-sha256", required=True, help="Coordinator-supplied pin, not read from call spec")
    parser.add_argument("--spec", required=True)
    parser.add_argument("--call-id", help="Preflight selected pending call; completed siblings may exist")
    parser.add_argument("--receipt")
    parser.add_argument("--dispatch")
    parser.add_argument("--viewer")
    parser.add_argument("--output", help="Optional repo-internal check receipt; never viewer copy")
    args = parser.parse_args(argv)
    try:
        common = (args.root, args.release, args.release_sha256, args.spec)
        if args.mode == "native-output-check":
            result, state = native_output_check(*common, args.call_id)
        elif args.mode == "dispatch-check":
            require(args.receipt and args.dispatch, "Dispatch check requires --receipt and --dispatch")
            result, state = dispatch_check(*common, args.receipt, args.dispatch)
        elif args.mode == "viewer-check":
            require(args.viewer, "Viewer check requires --viewer")
            result, state = viewer_check(*common, args.viewer)
        else:
            result, state = validate(*common, scope_call_id=args.call_id)
        if args.output:
            inputs = state["inputs"]
            path = inputs.path(args.output)
            require(path.suffix.lower() == ".json", "Check receipt output must be JSON")
            require(path.relative_to(inputs.root).as_posix() not in inputs.hashes, "Receipt must be outside its own input set")
            require(not path.is_relative_to(inputs.path(state["contract"]["output"]["directory"])), "Internal receipt cannot enter artwork output directory")
            require(not path.exists(), "Receipt output already exists; choose a new revision")
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(json.dumps(result, ensure_ascii=True, indent=2))
        return 0
    except (Invalid, OSError, TypeError, KeyError, AttributeError) as exc:
        print(json.dumps({"mechanical_verdict": "FAIL", "error": str(exc), "authority": "NO_GENERATION_AUTHORITY"}, ensure_ascii=True), file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
