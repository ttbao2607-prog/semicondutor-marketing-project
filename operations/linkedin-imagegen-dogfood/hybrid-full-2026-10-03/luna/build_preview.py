"""Build the Luna two-feed reader preview once all ten native PNGs exist.

Copies original bytes only; no image generation, resizing, browser control, or visual verdict.
"""
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse
import hashlib
import html
import json
import sys

ROOT = Path("D:/linkedin-awareness-harness-redesign").resolve()
RUN = ROOT / "operations/linkedin-imagegen-dogfood/hybrid-full-2026-10-03"
OWN = RUN / "luna"
OUTPUT = Path(r"C:\Users\ASUS\Documents\Codex\2026-10-03\chec\outputs\hybrid-luna")
COPY_PATH = RUN / "common/copy.json"
BRIEF_PATH = RUN / "common/brief.json"
MAP_PATH = RUN / "common/copy-normalization-map.json"
PUBLIC_COPY_PATH = OWN / "public-copy.json"
MANIFEST_PATH = OWN / "viewer-build-manifest.json"
EXPECTED_OUTPUTS = {"index.html", "assets"}
EXPECTED_DESTINATIONS = {
    "https://solutions.digiwin.com.vn/fabless?lang=vi",
    "https://solutions.digiwin.com.vn/supplierecosystem?lang=vi",
}

def sha_bytes(value):
    return hashlib.sha256(value).hexdigest()

def sha_file(path):
    return sha_bytes(Path(path).read_bytes())

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8-sig"))

def escape(value):
    return html.escape(value, quote=True)

def write_internal_json(path, value):
    Path(path).write_bytes((json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8"))

def main():
    copy_doc = load_json(COPY_PATH)
    brief = load_json(BRIEF_PATH)
    destination_map = load_json(MAP_PATH)
    contract = load_json(OWN / "contract.json")
    cards = {card["card_id"]: card for ad in copy_doc["ads"] for card in ad["cards"]}
    source_images = {
        card["card_id"]: OWN / "native" / (card["card_id"].lower() + ".png")
        for ad in copy_doc["ads"] for card in ad["cards"]
    }
    expected_ids = [f"F2-A{i}" for i in range(1, 6)] + [f"P2-A{i}" for i in range(1, 6)]
    if list(cards) != expected_ids or len(copy_doc["ads"]) != 2:
        raise RuntimeError("Shared copy must contain the exact two five-card scenarios.")
    missing = [cid for cid, path in source_images.items() if not path.is_file()]
    if missing:
        print(json.dumps({
            "build_result": "WAITING_FOR_NATIVE_FILES",
            "available_count": len(source_images) - len(missing),
            "expected_count": 10,
            "missing": missing,
        }, ensure_ascii=False, indent=2))
        return 2
    if any(len(ad["cards"]) != 5 for ad in copy_doc["ads"]):
        raise RuntimeError("Each scenario must have exactly five cards.")
    if OUTPUT.exists() and (not OUTPUT.is_dir() or any(OUTPUT.iterdir())):
        raise RuntimeError("Output bundle already exists and is populated; refusing to replace it.")
    if PUBLIC_COPY_PATH.exists() or MANIFEST_PATH.exists():
        raise RuntimeError("Internal viewer outputs already exist; refusing to overwrite.")

    # Require the shared copy bytes to match the brief's frozen common copy pin.
    copy_pin = brief["copy_ref"]
    if copy_pin["path"] != COPY_PATH.relative_to(ROOT).as_posix():
        raise RuntimeError("Brief points to a different shared copy path.")
    copy_bytes = COPY_PATH.read_bytes()
    if sha_bytes(copy_bytes) != copy_pin["sha256"]:
        raise RuntimeError("Shared copy no longer matches the brief pin.")

    # Use reviewed candidate destinations, and require one consistent route per scenario.
    mapping = {entry["card_id"]: entry["destination"] for entry in destination_map["cards"]}
    if set(mapping) != set(expected_ids):
        raise RuntimeError("Destination map does not cover the exact two scenarios.")
    for destination in mapping.values():
        parsed = urlparse(destination)
        if parsed.scheme != "https" or destination not in EXPECTED_DESTINATIONS:
            raise RuntimeError("Destination differs from the reviewed approved route set.")
    for ad in copy_doc["ads"]:
        ad_destinations = {mapping[card["card_id"]] for card in ad["cards"]}
        if len(ad_destinations) != 1:
            raise RuntimeError(f"Scenario has inconsistent destinations: {ad['ad_id']}")

    refs = brief["references"]
    logo_ref = next(ref for ref in refs if ref["role"] == "brand_asset")
    logo_src = ROOT / logo_ref["path"]
    if sha_file(logo_src) != logo_ref["sha256"]:
        raise RuntimeError("Official supplied logo changed from the brief pin.")

    # Verify native PNG structure and square minimum dimensions, without decoding or changing pixels.
    sys.path.insert(0, str(ROOT / "scripts"))
    import verify_imagegen_preflight as gate
    source_hashes = {}
    dimensions = {}
    for card_id, path in source_images.items():
        raw = path.read_bytes()
        dims = gate.png_dimensions(raw)
        gate.check_dimensions(contract["output"], dims)
        source_hashes[path.relative_to(ROOT).as_posix()] = sha_bytes(raw)
        dimensions[card_id] = list(dims)

    # Give exported files neutral public asset names; card IDs remain in the internal build manifest only.
    output_names = {}
    for index, card_id in enumerate(expected_ids, 1):
        output_names[card_id] = f"image-{index:02d}.png"

    feed_markup = []
    for ad in copy_doc["ads"]:
        first = ad["cards"][0]
        cards_markup = []
        for card_index, card in enumerate(ad["cards"], 1):
            card_id = card["card_id"]
            asset = "assets/" + output_names[card_id]
            width, height = dimensions[card_id]
            link = (
                '<a class="native-link" href="' + escape(asset) +
                '" target="_blank" rel="noopener noreferrer" aria-label="' +
                escape(card["native_headline"]) + '">'
            )
            image = (
                '<img class="artwork" src="' + escape(asset) +
                '" alt="' + escape(card["alt"]) +
                '" width="' + str(width) + '" height="' + str(height) + '">'
            )
            cta = ""
            if card["cta"]:
                cta = (
                    '<a class="reading-link" href="' + escape(mapping[card_id]) +
                    '" target="_blank" rel="noopener noreferrer">' +
                    escape(card["cta"]) + '</a>'
                )
            cards_markup.append(
                '<article class="card"' + (' hidden' if card_index != 1 else '') + '>' +
                link + image + '</a>' +
                '<p class="native-headline">' + escape(card["native_headline"]) + '</p>' +
                cta + '</article>'
            )
        dots = "".join(
            '<button type="button" class="dot" aria-label="Thẻ ' + str(i) +
            ' trong 5" aria-pressed="' + ("true" if i == 1 else "false") +
            '"></button>'
            for i in range(1, 6)
        )
        feed_markup.append(
            '<section class="feed" aria-label="' + escape(first["native_headline"]) + '">' +
            '<img class="brand" src="assets/digiwin-logo.webp" alt="Digiwin">' +
            '<p class="caption">' + escape(ad["caption"]) + '</p>' +
            '<div class="cards">' + "".join(cards_markup) + '</div>' +
            '<nav class="navigation" aria-label="' + escape(first["native_headline"]) + '">' +
            '<button class="previous" type="button" aria-label="Ảnh trước" disabled>‹</button>' +
            '<div class="dots">' + dots + '</div>' +
            '<span class="position" aria-live="polite" aria-atomic="true">1/5</span>' +
            '<button class="next" type="button" aria-label="Ảnh tiếp">›</button>' +
            '</nav></section>'
        )

    title = escape(copy_doc["ads"][0]["cards"][0]["headline"])
    document = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>""" + title + """</title>
<style>
*{box-sizing:border-box}
body{margin:0;padding:16px;background:#fff;color:#0B132B;font-family:system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif}
main{max-width:1248px;margin:auto;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:24px}
.feed{min-width:0;padding:16px;border:1px solid #e3e8f0;border-radius:12px;background:#fff}
.brand{display:block;width:126px;max-width:50%;height:auto;margin-bottom:16px}
.caption{font-size:16px;line-height:1.5;margin:0 0 16px;overflow-wrap:anywhere}
.card[hidden]{display:none}
.native-link{display:block}
.artwork{display:block;width:100%;height:auto;aspect-ratio:1/1;object-fit:contain}
.native-headline{font-size:18px;line-height:1.4;font-weight:600;margin:14px 0;overflow-wrap:anywhere}
.reading-link{display:inline-block;color:#0052ff;font-size:16px;line-height:1.5;max-width:100%;overflow-wrap:anywhere}
.navigation{display:flex;align-items:center;justify-content:center;gap:10px;margin-top:16px}
.navigation>button{width:40px;height:40px;border:1px solid #c8d5e8;background:#fff;color:#0052ff;border-radius:50%;font-size:26px;cursor:pointer}
.navigation>button:disabled{opacity:.4;cursor:default}
.dots{display:flex;align-items:center;gap:4px}
.dot{padding:0;width:28px;height:32px;border:0;background:transparent;cursor:pointer}
.dot:after{content:"";display:block;width:8px;height:8px;margin:auto;border-radius:50%;background:#b9c7da}
.dot[aria-pressed="true"]:after{background:#0052ff}
.position{font-size:14px;min-width:28px}
a:focus-visible,button:focus-visible{outline:3px solid #0052ff;outline-offset:3px}
@media(max-width:760px){main{grid-template-columns:minmax(0,1fr);gap:24px}.feed{padding:12px}.navigation{gap:6px}.dot{width:26px}.caption{font-size:16px}}
</style>
</head>
<body><main>""" + "".join(feed_markup) + """</main>
<script>
for(const feed of document.querySelectorAll('.feed')){
 const cards=[...feed.querySelectorAll('.card')],dots=[...feed.querySelectorAll('.dot')],previous=feed.querySelector('.previous'),next=feed.querySelector('.next'),position=feed.querySelector('.position');let selected=0;
 function show(value){selected=Math.max(0,Math.min(cards.length-1,value));cards.forEach((card,i)=>{card.hidden=i!==selected});dots.forEach((dot,i)=>{dot.setAttribute('aria-pressed',String(i===selected))});previous.disabled=selected===0;next.disabled=selected===cards.length-1;position.textContent=String(selected+1)+'/5'}
 previous.addEventListener('click',()=>show(selected-1));next.addEventListener('click',()=>show(selected+1));dots.forEach((dot,i)=>dot.addEventListener('click',()=>show(i)));
 feed.addEventListener('keydown',event=>{if(event.key==='ArrowLeft'){event.preventDefault();show(selected-1)}if(event.key==='ArrowRight'){event.preventDefault();show(selected+1)}});
}
</script>
</body>
</html>
"""

    output_was_created = False
    try:
        OUTPUT.mkdir(parents=True, exist_ok=False)
        output_was_created = True
        assets_dir = OUTPUT / "assets"
        assets_dir.mkdir()
        for card_id, source in source_images.items():
            target = assets_dir / output_names[card_id]
            target.write_bytes(source.read_bytes())
            if sha_file(target) != source_hashes[source.relative_to(ROOT).as_posix()]:
                raise RuntimeError(f"Exported image bytes differ from native input: {card_id}")
        logo_target = assets_dir / "digiwin-logo.webp"
        logo_target.write_bytes(logo_src.read_bytes())
        if sha_file(logo_target) != logo_ref["sha256"]:
            raise RuntimeError("Exported logo bytes differ from official source.")
        html_path = OUTPUT / "index.html"
        html_path.write_bytes(document.encode("utf-8"))
        exported = sorted(p.relative_to(OUTPUT).as_posix() for p in OUTPUT.rglob("*") if p.is_file())
        expected_export = sorted(["index.html", "assets/digiwin-logo.webp"] +
                                 ["assets/" + output_names[cid] for cid in expected_ids])
        if exported != expected_export:
            raise RuntimeError("Export includes an unexpected file or is missing an asset.")
        html_text = html_path.read_text(encoding="utf-8")
        forbidden = ("benchmark", "receipt", "sha256", "review status", "model name", "internal note")
        if any(term.casefold() in html_text.casefold() for term in forbidden):
            raise RuntimeError("Reader HTML contains prohibited internal metadata text.")
        if "<script src=" in html_text.lower() or "http://" in html_text.lower():
            raise RuntimeError("Reader HTML contains an external script or insecure link.")
        # Confirm that internal copy and build evidence remain outside the export.
        PUBLIC_COPY_PATH.write_bytes(copy_bytes)
        output_hashes = {rel: sha_file(OUTPUT / rel) for rel in expected_export}
        end = datetime.now(timezone.utc)
        manifest = {
            "schema_version": 1,
            "built_utc": end.isoformat().replace("+00:00", "Z"),
            "output_directory": str(OUTPUT),
            "export_files": output_hashes,
            "input_hashes": {
                "common_copy": sha_bytes(copy_bytes),
                "common_copy_revision": copy_doc["revision"],
                "common_brief": sha_file(BRIEF_PATH),
                "common_reference_map": sha_file(MAP_PATH),
                "contract": sha_file(OWN / "contract.json"),
                "official_logo": logo_ref["sha256"],
                "native_pngs": source_hashes,
            },
            "native_dimensions": dimensions,
            "native_bytes_unchanged": True,
            "official_logo_bytes_unchanged": True,
            "destination_routes_from_common_review_map": mapping,
            "feeds": [
                {"ad_id": ad["ad_id"], "card_count": len(ad["cards"])}
                for ad in copy_doc["ads"]
            ],
            "public_copy_path": str(PUBLIC_COPY_PATH),
            "manifest_exported": False,
            "rendered_verdict": "NOT_ASSESSED",
            "responsive_and_interaction_verdict": "PARENT_BROWSER_CHECK_REQUIRED",
            "visual_alt_truthfulness_verdict": "PARENT_IMAGE_REVIEW_REQUIRED",
        }
        write_internal_json(MANIFEST_PATH, manifest)
        print(json.dumps({
            "build_result": "BUILT_FOR_PARENT_RENDER_AUDIT",
            "export_file_count": len(output_hashes),
            "native_card_count": 10,
            "full_square_pngs": all(d[0] == d[1] and d[0] >= contract["output"]["min_edge"] for d in dimensions.values()),
            "native_bytes_unchanged": True,
            "official_logo_bytes_unchanged": True,
            "html_sha256": output_hashes["index.html"],
            "rendered_verdict": "NOT_ASSESSED",
            "output_directory": str(OUTPUT),
        }, ensure_ascii=False, indent=2))
        return 0
    except Exception:
        # Remove only this script's just-created bundle, after proving the target is the exact authorized directory.
        if output_was_created and OUTPUT.resolve() == Path(r"C:\Users\ASUS\Documents\Codex\2026-10-03\chec\outputs\hybrid-luna").resolve():
            import shutil
            shutil.rmtree(OUTPUT)
        raise

if __name__ == "__main__":
    raise SystemExit(main())

