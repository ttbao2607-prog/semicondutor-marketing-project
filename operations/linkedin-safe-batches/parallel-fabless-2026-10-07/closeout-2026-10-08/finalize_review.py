"""Record root's actual closeout judgments; mechanical assertions do not supply judgments."""
import json, hashlib, sys
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[4]
LANE=ROOT/'operations/linkedin-safe-batches/parallel-fabless-2026-10-07'
batch=sys.argv[1]
names={'B13':('B13-en-f1-v5','B13-en-f1-v5','en'),'B14':('B14-zh-Hans-f1-v1','B14-zh-Hans-f1-v1','zh-Hans'),'B15':('B15-zh-Hant-f1-v1','B15-zh-Hant-f1-v3','zh-Hant'),'B17':('B17-zh-Hans-f2-v1','B17-zh-Hans-f2-v2','zh-Hans')}
ops,out,locale=names[batch]; base=LANE/ops; dest=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'/out
def load(p):return json.loads(p.read_text('utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def ref(p):return {'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)}
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
m=load(dest/'manifest.json'); art=m['artwork']; assert len(art)==11
for x in art:
 p=ROOT/x['path'];assert sha(p)==x['sha256'] and Image.open(p).size==(1254,1254)
 if x.get('source'):assert sha(ROOT/x['source'])==sha(p)
frozen=load(ROOT/'operations/message-anchor/freeze-2026-10-06/manifest.json')
assert len(frozen['files'])==24 and all(sha(ROOT/x['path'])==x['sha256'] for x in frozen['files'])
capture=base/'render-closeout-2026-10-08';cap=load(capture/'capture-dom.json')
latest={(x['mode'],x['card']):x for x in cap['captures']}
for mode in ['feed','main','mobile']:
 for n in range(1,12):
  x=latest[(mode,n)];assert x['counter'].replace(' ','')==f'{n}/11'
  assert x['image']['complete'] and x['image']['natural']==[1254,1254]
  assert x['scrollWidth']<=x['clientWidth']
  if mode=='mobile':assert x['viewport'][0]==390
  else:assert abs(x['image']['rect']['width']-({'feed':333,'main':640}[mode]))<=2
  assert (capture/f'{mode}-{n}.png').exists()
assert {str(x.get('action')).replace('_return_clicked','-return-click') for x in cap['reader']} >= {'desktop-return-click','mobile-return-click'}
for x in cap['reader']:
 if 'viewport' in x:assert x['scrollWidth']<=x['clientWidth']
readerfiles=['reader-desktop-top.png','reader-desktop-bottom.png','reader-mobile-top.png','reader-mobile-bottom.png']
assert all((capture/p).exists() for p in readerfiles)
shots=[dict(**ref(p),bitmap_size=Image.open(p).size) for p in sorted(capture.glob('*.png'))];assert len(shots)==37
sem=base/'semantic-review.json'
if not sem.exists():sem=base/'message-anchor-review.json'
semantic=load(sem) if sem.exists() else {}
receipt=base/'postgen-review-closeout-2026-10-08.json'
proof=[ref(base/p) for p in ['proof-source-mapping.json','vietnam-team-source.json'] if (base/p).exists()]
history=base/('postgen-review-capture-reconciled.json' if batch=='B13' else 'postgen-review.json')
units=[]
cards=load(dest/'selected-copy.json')['cards']
for n,c in enumerate(cards,1):
 units.append(dict(card_id=c['card_id'],selected_native=art[n-1],exact_copy=c,verdict='PASS_SELF_REVIEW',observed_surfaces=['native1254','feed333','main640','browser CSS390'],observation='Root actually inspected current text, glyphs, category/counter, source, CTA and illustration plus caption/native/alt context. No leaked review copy or invented report data/result. Source is visibly at least body size where required; Paper/carrier props and chip/wafer patterns are illustrative; no legible invented records or values. Generic document pictograms are not data records.'))
r=dict(revision=batch.lower()+'-actual-closeout-2026-10-08',stage='POSTGEN_ARTIFACT',gate_id='MSG-ANCHOR-01 + AD-ED-01',reviewer='/root',independence='SELF_REVIEW',artifact_verdict='PASS_SELF_REVIEW',editorial_verdict='EDITORIAL_QA_PASS',message_anchor='MESSAGE_ANCHOR_PASS',execution='SUCCESS',independent_audit='NOT_PERFORMED',locale=locale,segment='FDI',persona='Operations / SCM Manager influencing business-system decisions at an eligible commercial Fabless FDI entity with outsourced production',anchor=ref(ROOT/'operations/Vy_Email_Content_Anchor.md'),anchor_revision='1.0',original_email=ref(ROOT/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),subjects={p:ref(dest/p) for p in ['manifest.json','selected-copy.json','selected-prompts.json','index.html','case-reader.html']},semantic_input=ref(sem) if sem.exists() else None,source_evidence=proof,historical_receipt=ref(history),unit_review=units,anchor_review={k:semantic[k] for k in ['A1','A2','A3','A4','A5','A6','A7'] if k in semantic},journey_review=dict(verdict='PASS_SELF_REVIEW',observation='Actual cold -> six explanation cards including Vietnam consulting/implementation -> four qualitative China case cards -> localized source reader and return inspected. Same Operations/SCM decision and reporting responsibility context. Taiwan ERP/MES management/production context, Vietnam service scope and China customer implementation separately attributed. Exact China legal entity retained. No numeric ROI, autonomous planning/synchronization, Vietnam Fabless deployment, or local buyer eligibility inferred. First-person advertiser voice and useful source attribution retained.'),render=dict(coverage=ref(capture/'capture-dom.json'),screenshots=shots,feed333=11,main640=11,mobile390CSS=11,reader='Actual desktop/mobile top/bottom and return clicks',precision='CSS viewport and screenshot bitmap differ under browser zoom. No physical-device/native-market certification. Capture failures retained; latest successful captures supersede earlier samples.'),findings=[],frozen_pins_unchanged=24,png_transformations=0,authorization='Bao 2026-10-08: Xử lý B17 trước để closeout, B13-15 closeout để merge nó vào main. Tiến hành sửa/hậu kiểm, action cần thiết.',adoption='Source local files; canonical sync and selective local-main integration pending; no push/live.')
if batch=='B17':
 attempts=load(base/'attempt-ledger.json')['attempts']; assert len(attempts)==8 and sum(x['kind']=='original' for x in attempts)==6
 checks=[]
 for x in attempts:
  assert sha(ROOT/x['path'])==x['sha256']
  plan=load(base/('corrective-dispatch-plan.json' if x['kind']=='corrective' else 'dispatch-plan.json'))
  j=next(y for y in plan['calls'] if y['call_id']==x['call_id']);folder=ROOT/j['folder'];g=folder/'dispatch'/(x['call_id']+'-fresh-preflight.json')
  assert load(g)['status']=='PREGEN_INPUTS_VERIFIED'; assert sha(folder/'release.json')==j['release_sha256'] and sha(folder/'anchor-review.json')==j['review_sha256']
  checks.append({'call_id':x['call_id'],'native':ref(ROOT/x['path']),'guard':ref(g),'release':ref(folder/'release.json'),'anchor_review':ref(folder/'anchor-review.json')})
 r['counts']=dict(selected=11,original=6,corrective=2,reused=5,actual_calls=8)
 r['closure']=dict(card_id='F2-A5',current_call='B17_F2_A5_C2',verdict='CLOSED',observation='Actual native/feed/main/mobile show plain pale-blue upright tile, removed ruled document glyph; all approved words and large complete ERP/MES source retained, no CTA arrow/source panel. C1 historical finding retained.',authorization=ref(base/'actual-corrective-f2-a5-c2-review.json'))
 r['attempt_verification']=checks

if batch=='B13':
 r['preserved_visual_exception']='B13v5 approved visual preserved per PO: A5 and case2 retain unlabelled rule-lines in illustrative paper/report props and generic document icon. Actual current inspection confirms no legible records/data. Historical exception explicitly recorded in postgen-review-capture-reconciled.json; B17 blank-tile corrective does not apply to B13.'
 r['render']['vertical_scroll']='B13 mobile navigation below fold is normal vertical scroll; artwork is fully visible and no horizontal overflow.'
if batch=='B14':
 r['closure']='Current A5 and case2 papers blank as required by their historical repair scope; generic document icon/CTA chevron/source panel remain the approved scene. B17 stricter object edit is not applied across batches. All11 current native reviewed, including five exact images later reused in B17.'
if batch=='B15':
 attempts=load(base/'attempt-ledger.json')['attempts']; assert len(attempts)==15
 r['counts']=dict(selected=11,original=11,corrective=4,actual_calls=15,new_calls_this_closeout=3)
 r['closure']=dict(card_id='F1-A5',current_call='B15_F1_A5_C3',verdict='CLOSED',observation='Original, C1 and C2 inherited Simplified CTA lettering. Actual C3 native/feed333/main640/mobile390 show exact Hant 探討委外生產管理問題; source complete and at least body-size. Reconstructed within B13v5 visual family; all paper blank, generic document pictogram illustrative. Legal Chinese entity remains intentional source literal, all other copy Hant. Source colon glyph is rendered ASCII in artwork; semantic attribution unchanged; no substantive text omission.',authority='Current explicit repair/actions mandate permits extra targeted corrective; history preserved.')
 r['attempt_verification']=[]
 for x in attempts[-3:]:
  j=next(y for y in load(base/'corrective-dispatch-plan.json')['calls'] if y['call_id']==x['call_id']);folder=ROOT/j['folder'];g=folder/'dispatch'/(x['call_id']+'-fresh-preflight.json')
  assert sha(ROOT/x['path'])==x['sha256'] and load(g)['status']=='PREGEN_INPUTS_VERIFIED' and sha(folder/'release.json')==j['release_sha256'] and sha(folder/'anchor-review.json')==j['review_sha256']
  r['attempt_verification'].append(dict(call_id=x['call_id'],native=ref(ROOT/x['path']),guard=ref(g),release=ref(folder/'release.json'),anchor_review=ref(folder/'anchor-review.json')))

put(receipt,r)
put(base/'verification-closeout-2026-10-08.json',dict(selected_raw_png=11,actual_card_captures=33,reader_captures=4,frozen_pins_unchanged=24,png_transformations=0,postgen=ref(receipt),qualification='Mechanical hashes/dimensions/coverage only; judgments recorded by root actual review.'))
print(batch+' closeout recorded: PASS_SELF_REVIEW, 11 native, 33 card +4 reader captures,24 frozen pins unchanged.')
