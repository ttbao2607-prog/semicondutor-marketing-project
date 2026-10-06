"""Bounded VN reader-address scan. Flags text; does not certify image/semantic review."""
import argparse,json,re,sys
from pathlib import Path
FIELDS=("headline","body","source_text","cta","native_headline","alt","artwork_labels")
BANNED=re.compile(r"(?<!\w)bạn(?!\w)",re.I)
CANONICAL="Quý Doanh Nghiệp"
FORMAL=re.compile(r"quý\s+doanh\s+nghiệp",re.I)
def scan_text(locator,text):
    if not isinstance(text,str):raise ValueError("Expected actual text: "+locator)
    findings=[]
    for m in BANNED.finditer(text):findings.append({"surface":locator,"kind":"READER_ADDRESS_CANDIDATE_BAN","exact":m.group(),"text":text,"disposition":"UNRESOLVED_REVIEW_REQUIRED"})
    for m in FORMAL.finditer(text):
        if m.group()!=CANONICAL:findings.append({"surface":locator,"kind":"NONCANONICAL_ADDRESS_FORM","exact":m.group(),"text":text,"disposition":"UNRESOLVED_REVIEW_REQUIRED"})
    return findings

def copy_fields(copy):
    for ad in copy["ads"]:
        yield ad["ad_id"]+"/caption",ad["caption"]
        for card in ad["cards"]:
            for field in FIELDS:
                value=card[field]
                if field=="artwork_labels":
                    for i,text in enumerate(value):yield ad["ad_id"]+"/"+card["card_id"]+"."+field+"["+str(i)+"]",text
                else:yield ad["ad_id"]+"/"+card["card_id"]+"."+field,value

def scan(fields,stage):
    if stage not in ("PREGEN_SCRIPT","POSTGEN_OBSERVED_TEXT"):raise ValueError("Unsupported review stage")
    if not fields:raise ValueError("Empty surface coverage")
    findings=[f for locator,text in fields.items() for f in scan_text(locator,text)]
    return {"gate_id":"VN-VOICE-01-V5","policy_revision":"1.1","stage":stage,"scan_status":"READER_ADDRESS_REVIEW_BLOCKED" if findings else "NO_FLAGGED_ADDRESS_TEXT","semantic_verdict":"NOT_AUTOMATICALLY_ASSESSED","observed_artwork":"REVIEWER_MUST_VERIFY" if stage=="POSTGEN_OBSERVED_TEXT" else "POSTGEN_NOT_RUN","reviewed_surfaces":list(fields),"findings":findings}

def main():
    parser=argparse.ArgumentParser();parser.add_argument("--input",required=True);parser.add_argument("--stage",required=True,choices=["PREGEN_SCRIPT","POSTGEN_OBSERVED_TEXT"]);parser.add_argument("--output");args=parser.parse_args()
    raw=json.loads(Path(args.input).read_text(encoding="utf-8-sig"));fields=dict(copy_fields(raw)) if args.stage=="PREGEN_SCRIPT" else raw["observed_fields"]
    result=scan(fields,args.stage);text=json.dumps(result,ensure_ascii=False,indent=2)+"\n"
    if args.output:Path(args.output).write_bytes(text.encode("utf-8"))
    else:print(json.dumps(result,ensure_ascii=True))
    return 1 if result["findings"] else 0
if __name__=="__main__":sys.exit(main())
