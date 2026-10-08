"""Record root's observed scoped judgments; assertions verify bytes/coverage only."""
import json,hashlib
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
LANE=Path(__file__).resolve().parent
DEL=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
def load(p): return json.loads(p.read_text('utf-8-sig'))
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v): p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
def ref(p): return {'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)}
frozen=load(ROOT/'operations/message-anchor/freeze-2026-10-06/manifest.json')
assert len(frozen['files'])==24 and all(sha(ROOT/x['path'])==x['sha256'] for x in frozen['files'])
new=[]
for batch,ops,out in [('B18','B18-zh-Hant-f2-v1','B18-zh-Hant-f2-v4'),('B19','B19-en-f3-v1','B19-en-f3-v1')]:
 base=LANE/ops;dest=DEL/out;render=base/'render-current'
 m=load(dest/'manifest.json');cards=load(dest/'selected-copy.json')['cards'];art=m['artwork']
 assert len(art)==len(cards)==11
 for a in art:
  p=ROOT/a['path'];assert sha(p)==a['sha256']==sha(ROOT/a['source']) and Image.open(p).size==(1254,1254)
 attempts=load(base/'attempt-ledger.json')['attempts'];checks=[]
 for a in attempts:
  p=ROOT/a['path'];assert sha(p)==a['sha256']
  plan=load(base/('corrective-dispatch-plan.json' if a['kind']=='corrective' else 'dispatch-plan.json'))
  j=next(x for x in plan['calls'] if x['call_id']==a['call_id']);folder=ROOT/j['folder']
  guard=folder/'dispatch'/(a['call_id']+'-fresh-preflight.json')
  assert load(guard)['status']=='PREGEN_INPUTS_VERIFIED'
  assert sha(folder/'release.json')==j['release_sha256'] and sha(folder/'anchor-review.json')==j['review_sha256']
  checks.append({'call_id':a['call_id'],'native':ref(p),'guard':ref(guard),'release':ref(folder/'release.json'),'anchor_review':ref(folder/'anchor-review.json')})
 shots=[];dom=[]
 for mode,w in [('desktop640',640),('feed333',333)]:
  for n in range(1,12):
   stem=f'{mode}-{n:02}';p=render/(stem+'.json');d=load(p)
   assert d['counter'].replace(' ','')==f'{n}/11' and d['loaded'] and d['naturalWidth']==1254
   assert d['src']==Path(art[n-1]['path']).relative_to(dest.relative_to(ROOT)).as_posix()
   assert abs(d['artRect']['width']-w)<1 and d['documentWidth']<=d['viewport']['width']
   dom.append(ref(p))
   for suffix in (['-top.png','-bottom.png'] if mode=='desktop640' else ['-top.png']):
    im=render/(stem+suffix);assert im.exists();shots.append(dict(**ref(im),bitmap_size=Image.open(im).size))
 assert len(shots)==33
 for f in ['reader-desktop-top.png','reader-desktop-bottom.png']:
  p=render/f;shots.append(dict(**ref(p),bitmap_size=Image.open(p).size))
 ret=load(render/'reader-return.json');assert ret['counter']=='1 / 11' and ret['url'].endswith('/'+out+'/index.html')
 mobile=load(render/'mobile390-dom.json');assert len(mobile)==11
 for n,d in enumerate(mobile,1):
  assert d['viewport'][0]==390 and d['documentWidth']<=390 and d['loaded'] and d['nativeWidth']==1254 and d['counter'].replace(' ','')==f'{n}/11'
 mr=load(render/'reader-mobile390-dom.json');assert mr['viewport'][0]==390 and mr['documentWidth']<=390
 status='INSUFFICIENT_EVIDENCE'
 # Manifest status changes first so final receipt binds current bytes.
 m['status']=status;m['review_scope']='Native + all desktop640/feed333 inspected SELF_REVIEW; mobile390 DOM only, visual insufficient.'
 m['independent_audit']='NOT_RUN';put(dest/'manifest.json',m)
 findings=[]
 if batch=='B18':
  findings=[{'id':'B18-FEED-A1','card_id':'F2-A1','status':'CLOSED_NATIVE_DESKTOP_FEED','observation':'PO-authorized C1 retains exact body in two large lines; native, desktop640 and feed333 actually inspected.','evidence':[ref(render/'feed333-02-top.png')],'decision':ref(base/'feed-repair-decision.md')}, {'id':'B18-FEED-A5','card_id':'F2-A5','status':'CLOSED_NATIVE_DESKTOP_FEED','observation':'C1 enlarged body but regressed source hierarchy and remains failed history. PO-authorized C2 retains exact two-line body, enlarges complete Taiwan source above body size, reduces illustration; native, desktop640 and feed333 actually inspected.','evidence':[ref(render/'feed333-06-top.png')],'decision':ref(base/'a5-source-regression-decision.md')}]
 findings.append({'id':batch+'-MOBILE-VISUAL','status':'INSUFFICIENT_EVIDENCE','observation':'Browser CSS390/800 layout, native image loads and localized reader/return clicked. Page.captureScreenshot times out after responsive reflow, including bounded final probe; alternate fromSurface:false is explicitly refused by the browser. No valid mobile visual acceptance; DOM does not replace screenshot inspection.'})
 units=[]
 for n,(c,a) in enumerate(zip(cards,art),1):
  units.append({'card_id':c['card_id'],'native':a,'exact_copy':c,'native_content':'PASS_SELF_REVIEW','desktop640':'PASS_SELF_REVIEW','feed333':'PASS_SELF_REVIEW','mobile390_visual':'INSUFFICIENT_EVIDENCE','observation':'Root inspected actual text/glyph/category/counter/source/CTA and scene. No legible invented report values, numeric outcomes or expanded case claim. Full scoped verdict excludes missing mobile visual.'})
 r={'revision':batch.lower()+'-postgen-2026-10-08-v1','stage':'POSTGEN_ARTIFACT','gate_id':'MSG-ANCHOR-01 + AD-ED-01','reviewer':'/root','independence':'SELF_REVIEW','artifact_verdict':status,'editorial_verdict':'INSUFFICIENT_EVIDENCE','message_anchor':'INSUFFICIENT_EVIDENCE','execution':'PARTIAL','independent_audit':'NOT_RUN','locale':m['locale'],'persona':load(base/'draft-manifest.json')['persona'],'anchor':ref(ROOT/'operations/Vy_Email_Content_Anchor.md'),'anchor_revision':'1.0','original_email':ref(ROOT/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),'semantic_input':ref(base/'semantic-review.json'),'subjects':{f:ref(dest/f) for f in ['manifest.json','selected-copy.json','selected-prompts.json','index.html','case-reader.html','explanation-vi.md']},'unit_review':units,'journey_review':{'observed_scope':'Native + desktop/feed cards and desktop reader/return; mobile layout/reader-return DOM only.','observation':'Cold -> six explanation cards (including Vietnam consulting/implementation) -> four qualitative China proof cards -> source-bounded localized reader. Same Operations/SCM influence persona. F2 demand-change reconciliation vs F3 partner handoff questions. Taiwan ERP management/MES production, Vietnam services and China customer context are distinct. Eligibility, ERP-only outcomes and local Fabless deployment not inferred.','full_verdict':'INSUFFICIENT_EVIDENCE'},'counts':{'selected':11,'original':sum(a['kind']=='original' for a in attempts),'corrective':sum(a['kind']=='corrective' for a in attempts),'actual_calls':len(attempts),'same_locale_raw_reuse':m['reused_pngs']},'attempt_verification':checks,'render':{'desktop640':11,'feed333':11,'mobile390_visual':0,'mobile390_dom':ref(render/'mobile390-dom.json'),'reader_mobile_dom':ref(render/'reader-mobile390-dom.json'),'reader_desktop_return':ref(render/'reader-return.json'),'reader_mobile_return':'Actual click observed to current index, counter1/11; no screenshot PASS.','dom':dom,'screenshots':shots,'precision':'Per-capture DOM records actual browser viewport; observed art640/333; bitmap and CSS sizes differ under zoom. Mobile actualCSS390x800; no physical-device/raster mapping certification. Failed/stale probe images excluded from accepted coverage.'},'findings':findings,'source_reuse_exclusions':ref(base/'source-reuse-exclusions.json') if batch=='B18' else None,'proof_source_mapping':ref(base/'proof-source-mapping.json'),'vietnam_team_scope':ref(base/'vietnam-team-source.json'),'frozen_pins_unchanged':24,'png_transformations':0,'ready':False,'adoption':'Working files only on owned source branch; no new commit/main integration/push/live. B20/B21 not run.'}
 if batch=='B18':r['repair_closure']=[{'card_id':x,'scope':'CLOSED_NATIVE_DESKTOP_FEED','mobile':'INSUFFICIENT_EVIDENCE','observation':'Current corrective enlarged full publisher/legal-name source; selected native/desktop/feed actually inspected. Original small-source finding preserved in attempt ledger.'} for x in ['RMK-BRIGHT-2','RMK-BRIGHT-3']]
 put(base/'postgen-review.json',r)
 v={'selected_raw_png':11,'actual_card_screenshots':33,'reader_desktop_screenshots':2,'mobile_visual_screenshots_accepted':0,'mobile_dom_rows':11,'frozen_pins_unchanged':24,'png_transformations':0,'postgen':ref(base/'postgen-review.json'),'qualification':'Mechanical assertions do not grant semantic/artifact PASS. Actual root judgments above; mandatory mobile evidence missing.'}
 put(base/'verification.json',v)
 (dest/'README.md').write_text(f'# {batch} offline review\n\nCurrent: **{status} / PARTIAL**, root SELF_REVIEW. Eleven selected native PNGs, all desktop640/feed333 inspected; mobile visual INSUFFICIENT_EVIDENCE despite CSS390 DOM checks. No ready/adopted/independent/PO/live status.\n\nOpen index.html for the localized journey and case-reader.html for the source-bounded reader. Vietnamese explanation: explanation-vi.md. Evidence: operations lane/{ops}/postgen-review.json. No new commit/main/push.\n','utf-8')
 new.append({'batch':batch,'selected':out,'status':status,'postgen':ref(base/'postgen-review.json'),'counts':r['counts']})
 print(batch,status,r['counts'],'33 card +2 reader desktop screenshots; mobile DOM only; frozen24 verified')
put(LANE/'B18-B19-current-status.json',{'revision':'fabless-b18-b19-20261008-v1','owner':'/root','batches':new,'generation_remaining_queue':['B20','B21'],'new_git':'Unstaged working files on owned source branch; no new commit/main/push/live.','source_reuse_followup':'B15 proof2 native confirmed Simplified headline contradicts prior Hant PASS; proof3 legal-name suspicion not confirmed on fresh native reinspection. Old/main bytes and historical receipts preserved.'})
