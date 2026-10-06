from pathlib import Path
import json, hashlib, importlib.util, sys
ROOT=Path(__file__).resolve().parents[4]
B="operations/linkedin-vn-journey-rebuild/2026-10-06/journey-v2"
P=ROOT/B
def sha(path): return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()
def read(name): return json.loads((P/name).read_text(encoding="utf-8-sig"))
def verify(call_id):
    pins=read("dispatch-pins.json")
    for path,expected in pins.items():
        if sha(path)!=expected: raise ValueError("Changed input: "+path)
    v=read("vn-voice-pregen.json"); m=read("message-review.json")
    assert v["gate_id"]=="VN-VOICE-01" and v["stage"]=="PREGEN_SCRIPT" and v["verdict"]=="VN_VOICE_PASS" and v["unresolved_findings"]==[]
    assert v["scope"]==m["scope"] and v["reviewed_fields"]==m["coverage"]["fields"]
    assert [u["card_id"] for u in v["units"]]==m["coverage"]["cards"]
    for unit in v["units"]:
        assert unit["verdict"]=="VN_VOICE_PASS" and unit["V1_V4_observation"].strip()
    for key in ("policy","freeze","copy","spec"):
        assert sha(v[key]["path"])==v[key]["sha256"]
    snapshot="operations/linkedin-vn-journey-rebuild/2026-10-06/cold-v4/inputs/verify_imagegen_anchor_preflight.snapshot.py"
    spec=importlib.util.spec_from_file_location("anchor",ROOT/snapshot); guard=importlib.util.module_from_spec(spec);spec.loader.exec_module(guard)
    scope=m["scope"]
    result=guard.check(ROOT,B+"/release.json",pins[B+"/release.json"],B+"/spec.json",B+"/message-review.json",pins[B+"/message-review.json"],call_id,scope["segment"],scope["persona"],scope["route"])
    result["VN_VOICE_receipt"]={"path":B+"/vn-voice-pregen.json","sha256":pins[B+"/vn-voice-pregen.json"],"binding":"PASS","semantic":"REVIEWER_ATTESTED_NOT_AUTOMATIC"}
    (P/(call_id+"-immediate-guard.json")).write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+"\n").encode())
    return result
if __name__=="__main__":
    print(json.dumps(verify(sys.argv[1])["tool_args"],ensure_ascii=True))
