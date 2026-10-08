"""Preserve first receipt; tighten current rendered verdict to actual capture evidence."""
from prepare_draft import *
from PIL import Image
def bound(p):return dict(path=p,sha256=sha(p))
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5';PARENT=Path(BASE).parent.as_posix()
p=load(BASE+'/postgen-review.json')
assert not (ROOT/BASE/'postgen-review-capture-reconciled.json').exists()
old=bound(BASE+'/postgen-review.json');p['revision']='b13-v5-postgen-v2-capture-dimension-reconciliation';p['previous_review']=old
mobile=BASE+'/evidence/fabless-v5-team-mobile.jpg'
with Image.open(ROOT/mobile) as im:pixel=list(im.size)
assert pixel==[414,938]
measurement=dict(observation='Same new team card is visibly present in saved mobile-context screenshot. Settled DOM read reported390x844 and image347.5556CSSpx; raster capture414x938 differs. Browser zoom/DPR/capture mapping was not independently established. Do not claim pixel-accurate390px mobile verification.',dom_viewport=[390,844],dom_image_width=347.5555725097656,raster_dimensions=pixel,screenshot=bound(mobile),verdict='MOBILE_CONTEXT_OBSERVED_EXACT_DIMENSION_MAPPING_INSUFFICIENT_EVIDENCE')
p['capture_measurement_reconciliation']=measurement
p['review_discrepancies'].append(dict(issue='Mobile screenshot dimensions differ from associated DOM viewport',reconciliation=measurement['observation']))
p['technical']['mobile']='New team wording/source visibly inspected in mobile-context capture414x938; settled DOM reported390x844/image347.56. Exact CSS-to-capture dimension mapping unverified, so exact390 mobile scope insufficient. Remaining10 and reader mobile visuals absent; no raw CDP route.'
p['verdicts']['new_team_card']='PASS_SELF_REVIEW_NATIVE_FEED_DESKTOP; MOBILE_CONTEXT_OBSERVED; EXACT_390_MAPPING_INSUFFICIENT_EVIDENCE'
for u in p['per_unit']:
 if u['card_id']=='F1-A6':
  u['full_render_verdict']='INSUFFICIENT_EVIDENCE_EXACT_MOBILE_DIMENSION_MAPPING'
  u['actual_observation']+=' Capture reconciliation: mobile raster414x938 vs DOM390x844, exact mapping not verified; mobile-context readability observed only.'
put(BASE+'/postgen-review-capture-reconciled.json',p)
v=load(BASE+'/verification.json');v['revision']='b13-v5-verification-v2-capture-dimension-reconciliation';v['previous_verification']=bound(BASE+'/verification.json');v['postgen']=bound(BASE+'/postgen-review-capture-reconciled.json');v['capture_reconciliation']=measurement
put(BASE+'/verification-capture-reconciled.json',v)
ledger=load(PARENT+'/ledger.json');ledger['revision']='fabless-lane-ledger-v5-capture-reconciled';ledger['receipt']=bound(BASE+'/postgen-review-capture-reconciled.json');put(PARENT+'/ledger.json',ledger)
readme=ROOT/OUT/'README.md';s=readme.read_text(encoding='utf-8');s=s.replace('New team card additionally observed at actual mobile390×844/image347.56; caption/headline/body/source all present.','New team card additionally visible in mobile-context capture414×938; settled DOM reported390×844/image347.56. Caption/headline/body/source present, but exact CSS-to-capture dimension mapping unverified; no exact390 mobile PASS.')
s=s.replace('Receipt/verification/evidence in owned B13-en-f1-v5 operations folder.','Current receipt: postgen-review-capture-reconciled.json; verification-capture-reconciled.json. Original receipt/verification retained historical. Evidence in owned B13-en-f1-v5 operations folder.')
readme.write_text(s,encoding='utf-8')
note=ROOT/BASE/'Bao_Review_Vietnamese.md';s=note.read_text(encoding='utf-8');s=s.replace('riêng card6 đã có screenshot mobile390×844 đầy đủ chữ/nguồn.','riêng card6 có ảnh chụp mobile-context414×938 đầy đủ chữ/nguồn; DOM ghi390×844 nhưng mapping kích thước chưa được xác minh, không gọi exact390 PASS.');s+='\nReceipt hiện hành: postgen-review-capture-reconciled.json và verification-capture-reconciled.json; receipt v1 giữ nguyên lịch sử.\n';note.write_text(s,encoding='utf-8')
with (ROOT/PARENT/'docs-impact.md').open('a',encoding='utf-8') as f:f.write('\n### V5 capture-dimension reconciliation — current qualification\n\nNew team mobile-context screenshot414x938 visibly contains exact card/caption/native/source, while associated settled DOM reports390x844/image347.56CSSpx. Mapping zoom/DPR/capture not independently established, so do not certify exact390 mobile PASS. Whole-set status remains PARTIAL / REVIEW_DRAFT_RENDER_GATE_PENDING / INSUFFICIENT_EVIDENCE. Current receipt postgen-review-capture-reconciled.json and verification-capture-reconciled.json supersede technical precision only; original v5 receipts retained historical. Counts/content/artwork/frozen24 unchanged.\n')
print('Current v5 receipt qualified: mobile context observed; exact390 dimensions not certified. Prior receipt unchanged.')
