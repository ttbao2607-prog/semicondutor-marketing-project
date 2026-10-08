"""Card3 corrected revision; all prior selected folders remain unchanged."""
from pathlib import Path
p=Path(__file__).with_name('build_review_v3.py');s=p.read_text(encoding='utf-8')
s=s.replace('B13-en-f1-v3','B13-en-f1-v4').replace('b13-review-manifest-v3-complete10','b13-review-manifest-v4-card3')
s=s.replace("s=s.replace(\"x['card_id']=='RMK-BRIGHT-1'\",\"x['card_id']=='RMK-BRIGHT-3'\")","s=s.replace(\"x['card_id']=='RMK-BRIGHT-1'\",\"False\")")
s=s.replace('10 of 10 artwork units generated · CHANGES_REQUIRED. T3 corrected case card 1. Case card 3 retains a publisher-size finding. Final card completed under separate PO instruction; full artifact acceptance remains pending.','10 of 10 artwork units generated · Card3 source corrected. Native review closed; rendered review and whole-journey acceptance remain pending.')
s=s.replace('imagegen_original=10,imagegen_corrective=3','imagegen_original=10,imagegen_corrective=4').replace('10original +3corrective','10original +4corrective')
s=s.replace('T3 fixed RMK-BRIGHT-1 source. RMK-BRIGHT-3 publisher remains smaller than body, corrective4 not authorized. Final card generated under separate PO instruction. Inventory complete; artifact acceptance pending.','T3 fixed Bright1. Authorized T4 fixed Bright3 source native; actual render review pending. Inventory complete; whole-journey acceptance pending.')
s=s.replace('CHANGES_REQUIRED case3','corrected case3 pending rendered review')
exec(compile(s,str(p),'exec'))
# Dedicated immutable-size audit surface for the changed card with real ad fields.
from prepare_draft import ROOT,BASE,load
import html
out=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v4'
c=next(x for x in load(out.relative_to(ROOT).as_posix()+'/selected-copy.json')['cards'] if x['card_id']=='RMK-BRIGHT-3')
page='<!doctype html><html lang="en"><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>B13 Card3 source review</title><style>*{box-sizing:border-box}body{margin:0;background:#f4f7fc;color:#0b132b;font:16px/1.5 Arial}main{padding:16px;max-width:960px;margin:auto}article{width:333px;max-width:100%;background:white;border:1px solid #dbe4ef;margin:16px 0}p{margin:0;padding:12px}img{width:100%;display:block;height:auto}h1{font-size:22px}a{color:#0052ba}</style><main><h1>B13 · RMK-BRIGHT-3 · corrected source</h1><article><p>'+html.escape(c['caption'])+'</p><img src="'+html.escape(c['image'])+'" alt="'+html.escape(c['alt'])+'"><p>'+html.escape(c['native_headline'])+'</p></article><a href="case-reader.html">Read the China case summary</a></main></html>'
(out/'card3-audit.html').write_text(page,encoding='utf-8')
