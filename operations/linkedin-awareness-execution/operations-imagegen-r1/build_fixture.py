"""Build one self-contained offline Operations review fixture from pinned native bytes."""
import base64
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
COPY = OUT / "copy-vi.json"
LOGO = ROOT / "operations/linkedin-awareness-execution/production-r3/dependencies/digiwin-logo.webp"
MAP = {
    "A1": "A1-shared-native.png", "A2": "A2-native.png", "A3": "A3-native.png",
    "A4": "A4-native.png", "A5": "A5-shared-native.png",
    "B1": "A1-shared-native.png", "B2": "B2-native.png", "B3": "B3-native.png",
    "B4": "B4-native.png", "B5": "A5-shared-native.png",
}

def digest(path):
    data = path.read_bytes()
    return {"path": path.resolve().relative_to(ROOT).as_posix(), "sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data)}

copy = json.loads(COPY.read_text(encoding="utf-8"))
assert [r["id"] for r in copy["records"]] == [f"A{i}" for i in range(1, 6)] + [f"B{i}" for i in range(1, 6)]
sources = {"production_copy": digest(COPY), "builder": digest(Path(__file__)), "template": digest(OUT / "template.html"), "logo": digest(LOGO), "images": {}}
for rec in copy["records"]:
    rec["sequence"] = rec["id"][1] + "/5"
    path = OUT / MAP[rec["id"]]
    sources["images"][rec["id"]] = digest(path)
    rec["image"] = "data:image/png;base64," + base64.b64encode(path.read_bytes()).decode("ascii")
logo_uri = "data:image/webp;base64," + base64.b64encode(LOGO.read_bytes()).decode("ascii")
template = (OUT / "template.html").read_text(encoding="utf-8")
html = template.replace("__COPY_JSON__", json.dumps(copy, ensure_ascii=False).replace("</", "<\\/"))
html = html.replace("__LOGO_URI__", logo_uri)
(OUT / "index.html").write_text(html, encoding="utf-8")
source_map = {"revision": "operations-imagegen-r1", "status": "CURRENT_SELF_CONTAINED_DEMO_RENDER_QA_BLOCKED", "sources": sources,
              "copy_delta": "P1 main/caption/native/destination/proof unchanged; alt weak meta labels removed in separate production snapshot",
              "reuse": {"B1": "A1", "B5": "A5"},
              "limits": "Offline simulated feed; original PNG bytes embedded, no image transform. Parent browser permission failure blocked desktop/mobile/navigation observation; human content decision pending."}
(OUT / "source-map.json").write_text(json.dumps(source_map, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print("built", len(html.encode("utf-8")), "bytes,", len(sources["images"]), "record images")
