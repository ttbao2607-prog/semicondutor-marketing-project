"""Persist actual root judgments; assertions establish provenance/coverage, not semantics."""
import hashlib,json,subprocess
from pathlib import Path
from PIL import Image
ROOT=Path(__file__).resolve().parents[3]
LANE=Path(__file__).resolve().parent
DEL=ROOT/'deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
def load(p):return json.loads(p.read_text('utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def put(p,v):p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n','utf-8')
def ref(p):return {'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)}
frozen=load(ROOT/'operations/message-anchor/freeze-2026-10-06/manifest.json')
assert len(frozen['files'])==24 and all(sha(ROOT/x['path'])==x['sha256'] for x in frozen['files'])
notes=[
 'Cold: Khi chuyển lô cho đối tác, cần giao kèm thông tin gì? Mở bài bằng lô, hồ sơ và người xác nhận, đúng vai trò Operations/SCM có ảnh hưởng tới quyết định hệ thống.',
 'A1: Đặt vấn đề chuyển giao lô gia công giữa các đối tác; chốt thông tin đi cùng lô và trách nhiệm xác nhận.',
 'A2: Chọn một điểm bàn giao và sản phẩm cụ thể theo quy trình đã thống nhất với đối tác. Không mặc định hệ thống tự đồng bộ.',
 'A3: Đối chiếu lô, sản phẩm và nguồn hồ sơ. Nếu mã chưa khớp, xác định người kiểm chứng trước khi cập nhật.',
 'A4: Liệt kê thông tin còn thiếu và người xác nhận ở hai bên; bước tiếp theo phải theo quy trình thực tế của đối tác.',
 'A5: Đưa phạm vi lô, nguồn hồ sơ và trách nhiệm xác nhận vào cùng cuộc trao đổi. Nguồn Đài Loan phân biệt ERP quản trị kinh doanh và MES sản xuất; không suy thành kết quả chỉ nhờ ERP.',
 'A6 — nuance Việt Nam: Trao đổi với đội Digiwin tại Việt Nam về tư vấn và triển khai ERP, bắt đầu từ luồng báo cáo, trách nhiệm cập nhật và ưu tiên dự án. Đây là phạm vi dịch vụ; không khẳng định đã triển khai Fabless tại Việt Nam, số chuyên gia, năng lực ngôn ngữ, SLA hay kết quả khách hàng.',
 'Proof1: Giới thiệu Digiwin cung cấp giải pháp số cho sản xuất, từ ERP đến sản xuất thông minh. Vai trò nhà cung cấp tách khỏi bằng chứng khách hàng.',
 'Proof2: Giới thiệu doanh nghiệp thiết kế chip Trung Quốc 晶丰明源 và bối cảnh triển khai. Pháp nhân nguồn: 上海晶丰明源半导体股份有限公司. Trường hợp Trung Quốc không phải kết quả Việt Nam.',
 'Proof3: Nguồn nêu thách thức hiệu quả quản lý gia công và giải pháp số tích hợp. Không có số cải thiện được dùng; không quy toàn bộ kết quả cho ERP.',
 'Proof4: Mời đọc bối cảnh thách thức và giải pháp tích hợp của case Trung Quốc, dẫn tới reader cùng ngôn ngữ rồi trở về đúng chủ đề bàn giao.'
]
current=[]
for batch,ops,out in [('B20','B20-zh-Hans-f3-v1','B20-zh-Hans-f3-v3'),('B21','B21-zh-Hant-f3-v1','B21-zh-Hant-f3-v1')]:
 base=LANE/ops;dest=DEL/out;render=base/'render-current'
 m=load(dest/'manifest.json');cards=load(dest/'selected-copy.json')['cards'];art=m['artwork']
 assert len(cards)==len(art)==11
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
 counts={'selected':11,'original':sum(a['kind']=='original' for a in attempts),'corrective':sum(a['kind']=='corrective' for a in attempts),'actual_calls':len(attempts),'same_locale_raw_reuse':m['reused_pngs']}
 assert counts==({'selected':11,'original':6,'corrective':2,'actual_calls':8,'same_locale_raw_reuse':5} if batch=='B20' else {'selected':11,'original':6,'corrective':0,'actual_calls':6,'same_locale_raw_reuse':5})
 shots=[];dom=[]
 for mode,w in [('desktop640',640),('feed333',333)]:
  for n in range(1,12):
   stem=f'{mode}-{n:02}';p=render/(stem+'.json');d=load(p)
   assert d['counter'].replace(' ','')==f'{n}/11' and d['loaded'] and d['naturalWidth']==1254
   assert d['src']==Path(art[n-1]['path']).relative_to(dest.relative_to(ROOT)).as_posix()
   assert abs(d['artRect']['width']-w)<1 and d['documentWidth']<=d['viewport']['width']
   dom.append(ref(p))
   for suffix in (['-top.png','-bottom.png'] if mode=='desktop640' else ['-top.png']):
    im=render/(stem+suffix);shots.append(dict(**ref(im),bitmap_size=Image.open(im).size))
 assert len(shots)==33
 for f in ['reader-desktop-top.png','reader-desktop-bottom.png']:
  p=render/f;shots.append(dict(**ref(p),bitmap_size=Image.open(p).size))
 for f in ['reader-return.json','reader-mobile-return.json']:
  ret=load(render/f);assert ret['counter']=='1 / 11' and ret['url'].endswith('/'+out+'/index.html')
 mobile=load(render/'mobile390-dom.json');assert len(mobile)==11
 for n,d in enumerate(mobile,1):
  assert d['viewport']==[390,800] and d['documentWidth']<=390 and d['loaded'] and d['nativeWidth']==1254 and d['counter'].replace(' ','')==f'{n}/11'
  assert d['src']==Path(art[n-1]['path']).relative_to(dest.relative_to(ROOT)).as_posix()
 mr=load(render/'reader-mobile390-dom.json');assert mr['viewport']==[390,800] and mr['documentWidth']<=390
 mobile_shots=[ref(render/'mobile390-01-probe.png')] if batch=='B21' else []
 explanation=f'# {batch} — Diễn giải tiếng Việt cho Bảo\n\n11 card, F3: bàn giao lô giữa các đối tác. Giữ anchor/persona/visual của B13 v5.\n\n'
 for n,(c,note) in enumerate(zip(cards,notes),1):
  explanation+=f'## {n}. {c["card_id"]}\n\n**Chữ trên ảnh:** {c["headline"]}\n\n{note}\n\n'
 explanation+='Reader nối lại điểm bàn giao, sản phẩm, hồ sơ và người xác nhận; nguyên văn tên pháp nhân giản thể được giữ ngay cả ở bản phồn thể và có giải thích. Ngôn ngữ không chứng minh quyền quyết định ERP tại Việt Nam hay tình trạng pháp nhân đủ điều kiện. Nguồn China/Taiwan/Vietnam có vai trò riêng.\n\nHậu kiểm: root SELF_REVIEW đủ native1254, desktop640 và feed333; chưa đủ bằng chứng hình ảnh mobile390/reader. B20 A5 C2 khép finding trong ba phạm vi đã xem; C1 lỗi nguồn vẫn là lịch sử. Không có independent/native-market/live PASS.\n'
 (dest/'explanation-vi.md').write_text(explanation,'utf-8')
 status='INSUFFICIENT_EVIDENCE'
 m.update(status=status,review_scope='Native + all desktop640/feed333 inspected SELF_REVIEW; mobile390 incomplete visual evidence.',independent_audit='NOT_RUN',ready=False)
 put(dest/'manifest.json',m)
 findings=[]
 if batch=='B20':
  findings.append({'id':'B20-A5-BODY-AND-SOURCE','status':'CLOSED_NATIVE_DESKTOP_FEED','card_id':'F3-A5','observation':'Original body too small at feed; C1 enlarged body to two lines but source became smaller than body. Explicit PO-authorized C2 preserves exact words, full source in three lines at least body size, reduces scene. Actual native/desktop640/feed333 inspected; earlier failed attempts unchanged.','evidence':[ref(render/'feed333-06-top.png')],'authorization_review':ref(base/'actual-corrective-f3-a5-source-po-review.json')})
 findings.append({'id':batch+'-MOBILE-VISUAL','status':status,'observation':'Fresh viewport set before tab navigation; CSS390x800 all11 loaded and reader/return actually clicked, no horizontal DOM overflow. Screenshot tool timed out. B21 obtained and inspected one cold screenshot, then next capture timed out. B20 zero valid mobile images; B21 only cold card. Missing10/11 mobile cards and both mobile reader visuals prevents full gate PASS.','probe_failure':ref(render/'mobile-probe-failure.json')})
 units=[]
 for n,(c,a) in enumerate(zip(cards,art),1):
  units.append({'card_id':c['card_id'],'native':a,'exact_copy':c,'native_content':'PASS_SELF_REVIEW','desktop640':'PASS_SELF_REVIEW','feed333':'PASS_SELF_REVIEW','mobile390_visual':'PASS_SELF_REVIEW_COLD_ONLY' if batch=='B21' and n==1 else status,'observation':'Root actually inspected text/glyph/category/counter/source/CTA and scene. A1/A2 compact body remains legible in actual feed. Full Taiwan/proof attribution legible; legal name follows original Simplified source. No invented report values or broader results.','explanation_vi':notes[n-1]})
 r={'revision':batch.lower()+'-postgen-2026-10-08-v1','stage':'POSTGEN_ARTIFACT','gate_id':'MSG-ANCHOR-01 + AD-ED-01','reviewer':'/root','independence':'SELF_REVIEW','artifact_verdict':status,'editorial_verdict':status,'message_anchor':status,'execution':'PARTIAL','independent_audit':'NOT_RUN','locale':m['locale'],'persona':load(base/'draft-manifest.json')['persona'],'anchor':ref(ROOT/'operations/Vy_Email_Content_Anchor.md'),'anchor_revision':'1.0','original_email':ref(ROOT/'operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'),'semantic_input':ref(base/'semantic-review.json'),'subjects':{f:ref(dest/f) for f in ['manifest.json','selected-copy.json','selected-prompts.json','index.html','case-reader.html','explanation-vi.md']},'unit_review':units,'journey_review':{'observed_scope':'Native + desktop/feed cards and desktop reader/return; mobile layout/reader-return DOM, B21 cold screenshot only.','observation':'Cold -> six explanation cards including Vietnam consulting/implementation -> four qualitative China proof cards -> same-locale reader with F3 handoff questions. Operations/SCM influence persona retained. Taiwan ERP management/MES production, Vietnam services and China case distinct. No ERP-only outcome or Vietnam Fabless implementation inference.','full_verdict':status},'counts':counts,'attempt_verification':checks,'render':{'desktop640':11,'feed333':11,'mobile390_visual_cards':len(mobile_shots),'mobile390_visual_screenshots':mobile_shots,'mobile390_dom':ref(render/'mobile390-dom.json'),'reader_mobile_dom':ref(render/'reader-mobile390-dom.json'),'reader_desktop_return':ref(render/'reader-return.json'),'reader_mobile_return':ref(render/'reader-mobile-return.json'),'dom':dom,'screenshots':shots,'precision':'Per-capture DOM records CSS viewport and art640/333. Bitmap differs under zoom. Mobile actualCSS390x800; DOM is not visual acceptance. Only genuine B21 cold probe included; no stale/failed image substituted.'},'findings':findings,'proof_source_mapping':ref(base/'proof-source-mapping.json'),'vietnam_team_scope':ref(base/'vietnam-team-source.json'),'frozen_pins_unchanged':24,'png_transformations':0,'ready':False,'adoption':'B20/B21 working files only on owned source branch. No new commit/main integration/push/live. B18/B19 checkpoint b83d061b local only.'}
 put(base/'postgen-review.json',r)
 put(base/'verification.json',{'selected_raw_png':11,'actual_card_screenshots_desktop_feed':33,'reader_desktop_screenshots':2,'mobile_visual_cards_accepted':len(mobile_shots),'mobile_reader_visual':0,'mobile_dom_rows':11,'frozen_pins_unchanged':24,'png_transformations':0,'postgen':ref(base/'postgen-review.json'),'qualification':'Mechanical assertions do not grant semantic/artifact PASS; mandatory mobile evidence incomplete.'})
 (dest/'README.md').write_text(f'# {batch} offline review\n\n**INSUFFICIENT_EVIDENCE / PARTIAL**, root SELF_REVIEW. 11 selected native PNGs; all native1254/desktop640/feed333 inspected and scoped PASS. Mobile390 visual incomplete ({len(mobile_shots)}/11 cards, reader0); layout DOM alone is insufficient. No independent/live certification or release.\n\n[Viewer](index.html) · [Reader](case-reader.html) · [Diễn giải Việt](explanation-vi.md)\n\nFull provenance and actual judgments: operations/linkedin-safe-batches/parallel-fabless-2026-10-07/{ops}/postgen-review.json. B20 A5 C2 closes native/desktop/feed findings; failed history retained. Working files only, not committed/main/pushed.\n','utf-8')
 current.append({'batch':batch,'selected':out,'status':status,'postgen':ref(base/'postgen-review.json'),'counts':counts})
 print(batch,status,counts,'frozen24 verified; 33card+2reader desktop/feed screenshots')
put(LANE/'B20-B21-current-status.json',{'revision':'fabless-b20-b21-20261008-v1','owner':'/root','batches':current,'generation_remaining_queue':[],'lane_generated_batches':9,'lane_selected_png_positions':99,'full_lane_acceptance':'NOT_COMPLETE; B18-B21 mobile visual insufficient; B15 proof2 current acceptance qualification retained separately.','new_git':'B18/B19 local checkpoint b83d061b; B20/B21 uncommitted owned working files; no new main/push/live.'})
