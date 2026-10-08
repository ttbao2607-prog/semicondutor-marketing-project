"""Complete10 image folder, preserve prior partial folders and findings."""
from pathlib import Path
p=Path(__file__).with_name('build_review.py');s=p.read_text(encoding='utf-8')
s=s.replace("OUT=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v1'","OUT=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v3'")
s=s.replace("x['card_id']=='RMK-BRIGHT-1'","x['card_id']=='RMK-BRIGHT-3'")
s=s.replace('HOLD / CHANGES_REQUIRED · 8 of 10 artwork units generated. Case card 1 needs a source-size correction; the batch has reached its two-correction cap. Case cards 3–4 have reviewed scripts but no generated artwork.','10 of 10 artwork units generated · CHANGES_REQUIRED. T3 corrected case card 1. Case card 3 retains a publisher-size finding. Final card completed under separate PO instruction; full artifact acceptance remains pending.')
s=s.replace('actual8','actual10').replace('Actual8','Actual10').replace('CHANGES_REQUIRED case1','CHANGES_REQUIRED case3')
s=s.replace("revision='b13-review-manifest-v1'","revision='b13-review-manifest-v3-complete10'").replace('imagegen_original=8,imagegen_corrective=2','imagegen_original=10,imagegen_corrective=3').replace('generated_selected=8','generated_selected=10').replace("not_generated=['RMK-BRIGHT-3','RMK-BRIGHT-4']","not_generated=[]")
s=s.replace('Eight of ten artwork units generated,8original +2corrective','All ten artwork units generated,10original +3corrective').replace('RMK-BRIGHT-1 source text is smaller than body and would require corrective3, beyond cap. RMK-BRIGHT-3/4 not generated.','T3 fixed RMK-BRIGHT-1 source. RMK-BRIGHT-3 publisher remains smaller than body, corrective4 not authorized. Final card generated under separate PO instruction. Inventory complete; artifact acceptance pending.')
s=s.replace('8actual PNGs','10actual PNGs')
exec(compile(s,str(p),'exec'))
