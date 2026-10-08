"""Build separate T3 review folder; original partial v1 and evidence untouched."""
from pathlib import Path
p=Path(__file__).with_name('build_review.py')
s=p.read_text(encoding='utf-8')
s=s.replace("OUT=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v1'","OUT=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v2'")
s=s.replace("x['card_id']=='RMK-BRIGHT-1'","x['card_id']=='RMK-BRIGHT-3'")
s=s.replace('HOLD / CHANGES_REQUIRED · 8 of 10 artwork units generated. Case card 1 needs a source-size correction; the batch has reached its two-correction cap. Case cards 3–4 have reviewed scripts but no generated artwork.','HOLD / CHANGES_REQUIRED · 9 of 10 artwork units generated. T3 corrected case card 1. Case card 3 has a publisher-size finding requiring another correction beyond the T3 exception. Case card 4 is not generated.')
s=s.replace('actual8','actual9').replace('Actual8','Actual9').replace('CHANGES_REQUIRED case1','CHANGES_REQUIRED case3')
s=s.replace("revision='b13-review-manifest-v1'","revision='b13-review-manifest-v2-t3'").replace('imagegen_original=8,imagegen_corrective=2','imagegen_original=9,imagegen_corrective=3').replace('generated_selected=8','generated_selected=9').replace("not_generated=['RMK-BRIGHT-3','RMK-BRIGHT-4']","not_generated=['RMK-BRIGHT-4']")
s=s.replace('Eight of ten artwork units generated,8original +2corrective','Nine of ten artwork units generated,9original +3corrective').replace('RMK-BRIGHT-1 source text is smaller than body and would require corrective3, beyond cap. RMK-BRIGHT-3/4 not generated.','T3 fixed RMK-BRIGHT-1 publisher size. RMK-BRIGHT-3 publisher is smaller than body and needs corrective4, outside the T3 exception. RMK-BRIGHT-4 not generated.')
s=s.replace('8actual PNGs','9actual PNGs')
exec(compile(s,str(p),'exec'))
