"""Bind actual v5 evidence without promoting missing full-mobile or independent review."""
from prepare_draft import *
from PIL import Image
import subprocess
def ref(p,revision=None):
 return dict(path=p,sha256=sha(p),revision=revision or (load(p).get('revision','source-v1') if Path(p).suffix=='.json' else 'actual-artifact-v5'))
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v5'
V4=OUT.replace('-v5','-v4');PARENT=Path(BASE).parent.as_posix();OLD=Path(BASE).with_name('B13-en-f1-v1').as_posix()
m=load(OUT+'/manifest.json');cards=load(OUT+'/selected-copy.json')['cards'];attempts=load(BASE+'/attempt-ledger.json')['attempts']
assert len(attempts)==6 and all(x['kind']=='original' for x in attempts)
assert len(m['artwork'])==11 and sum(x['reused'] for x in m['artwork'])==5
assert len(load(OLD+'/attempt-ledger.json')['attempts'])==14
frozen=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']
assert len(frozen)==24 and all(sha(x['path'])==x['sha256'] for x in frozen)
for a in m['artwork']:
 assert sha(a['path'])==a['sha256']==sha(a['source'])
 with Image.open(ROOT/a['path']) as im:assert im.size==(1254,1254) and im.format=='PNG'
assert sha(OUT+'/case-reader.html')==sha(V4+'/case-reader.html')
po=load(BASE+'/generation-mandate.json');assert sha(po['accepted_visual']['path'])==po['accepted_visual']['sha256']
anchor=load(OLD+'/postgen-review-t4.json')['anchor']
assert sha(anchor['path'])==anchor['sha256'] and sha(anchor['original_email']['path'])==anchor['original_email']['sha256']
receipts=[]
for a in attempts:
 files=list((ROOT/BASE).glob('**/dispatch/'+a['call_id']+'-fresh-preflight.json'));assert len(files)==1
 d=json.loads(files[0].read_text(encoding='utf-8-sig'));assert d['status']=='PREGEN_INPUTS_VERIFIED' and d['mechanical_verdict']=='PASS'
 receipts.append(ref(files[0].relative_to(ROOT).as_posix(),a['call_id']))
oldcp={x['card_id']:x for x in load(V4+'/selected-copy.json')['cards']}
for i,c in enumerate([x for x in cards if x['stage']=='explanation'],1):
 assert c['artwork_labels']==['ERP · CHIP OPERATIONS',str(i)+'/6']
 if i<6:assert all(c[k]==oldcp[c['card_id']][k] for k in ['headline','body','source_text','cta','caption','native_headline','alt'])
for c in cards:
 if c['stage']!='explanation':assert all(c[k]==oldcp[c['card_id']][k] for k in ['headline','body','source_text','cta','caption','native_headline','alt','artwork_labels'])
ev=ROOT/BASE/'evidence';evidence=[]
for p in sorted(ev.iterdir()):
 if p.is_file():
  item=ref(p.relative_to(ROOT).as_posix(),p.name)
  if p.suffix=='.jpg':
   with Image.open(p) as im:item.update(format=im.format,width=im.width,height=im.height)
  evidence.append(item)
assert len(evidence)==30
assert (ev/'fabless-v5-team-mobile.jpg').is_file()
counts=dict(v5_base_calls=6,new_card=1,sequence_revision_edits=5,v5_corrective_calls=0,v5_reused_pngs=5,selected_artwork=11,prior_calls=14,cumulative_calls=20)
obs={
 'COLD-FABLESS-B13':'Exact outsourced-production headline and lot/stage/report-time handoff body, advertiser We provide caption; neutral chip trays, blank central folios and open paths, no owned fab/customer data.',
 'F1-A1':'Exact partner-report/stage question,1/6; blank reports and wafer protective carrier retained from PO accepted visual. Same next-decision problem.',
 'F1-A2':'Exact product/lot references and partner periods/test classifications,2/6; blank reference folios/chip and open paths. Questions and conventions, no claimed automatic product feature.',
 'F1-A3':'Exact process stage/status-recording time/supporting partner report,3/6; approved carrier scene retained, no fabricated process result.',
 'F1-A4':'Exact report format/exchange schedule/update owner,4/6; generic responsibility token and neutral report props, not a named member of Digiwin team.',
 'F1-A5':'Exact shared basis of lot/stage/report time/update ownership,5/6. Taiwan ERP/MES source and Explore outsourced-production questions CTA intact; source complete/readable on white. Existing unlabelled rule-lines in approved report prop retained under PO visual-preservation instruction, not real records or data.',
 'F1-A6':'Exact Consulting and implementation in Vietnam headline; Work with our team in Vietnam on ERP consulting and implementation. Start with your reporting workflows, update ownership and project priorities. Exact Digiwin Vietnam · ERP consulting and implementation source and6/6. Neutral consultation folios, chip, team/gear tokens; no staff portrait, Vietnam customer facility, metrics or Fabless implementation proof. Large high-contrast full-width white source visually readable native/feed333/desktop638.22/mobile347.56 at actual390x844 viewport. Caption/native headline outside raster, official mark once.',
 'RMK-BRIGHT-1':'Exact first-person digital-provider text and Company introduction source;1/4, generic chip/report props. Separate provider introduction from customer case, no customer outcomes.',
 'RMK-BRIGHT-2':'Exact China chip-design entity/context,2/4 and 上海晶丰明源半导体股份有限公司 source preserved. Existing unlabelled report rule-lines retained in byte-identical PO accepted visual, not numeric records. Large named source readable native/feed/desktop.',
 'RMK-BRIGHT-3':'Exact outsourcing-management challenge/integrated digital-solution body,3/4; Digiwin Vietnam · China case04 and full legal name clearly larger than body on full white band. Current native/feed331.22/desktop638.22 observation closes source hierarchy in these scopes; mobile remains absent, historical v4 technical receipt untouched.',
 'RMK-BRIGHT-4':'Exact business challenges/integrated digital-solution China case context,4/4; full named source and Read the China case CTA. Neutral chip sample, no customer product/facility implication; actual reader link clicked to unchanged English summary.'}
unit_reviews=[]
for i,c in enumerate(cards,1):
 feed='fabless-v5-feed-'+str(i).zfill(2)+('-confirmed' if i in [9,10] else '')+'.jpg'
 unit_reviews.append(dict(card_id=c['card_id'],exact_fields={k:c[k] for k in ['headline','body','source_text','cta','caption','native_headline','alt','artwork_labels']},actual_observation=obs[c['card_id']],native=ref(m['artwork'][i-1]['path']),feed=ref(BASE+'/evidence/'+feed),desktop=ref(BASE+'/evidence/fabless-v5-desktop-'+str(i).zfill(2)+'.jpg'),mobile=ref(BASE+'/evidence/fabless-v5-team-mobile.jpg') if c['card_id']=='F1-A6' else 'INSUFFICIENT_EVIDENCE_NO_ACCEPTED_V5_MOBILE_CAPTURE',semantic_disposition='MATCH_IN_OBSERVED_SCOPE',full_render_verdict='PASS_SELF_REVIEW_NATIVE_FEED_DESKTOP_MOBILE' if c['card_id']=='F1-A6' else 'INSUFFICIENT_EVIDENCE_FULL_MOBILE'))
transitions=[dict(from_card=a['card_id'],to_card=b['card_id'],observation=a['headline']+' -> '+b['headline'],disposition='MATCH_IN_NATIVE_FEED_DESKTOP_OBSERVED_SCOPE') for a,b in zip(cards,cards[1:])]
transitions[5]['observation']+='; shared report basis -> discussion with Vietnam team of reporting workflow/ownership/project priorities, no delivery outcome promise.'
transitions[6]['observation']+='; local service invitation -> provider introduction leading to separately attributed China customer case. No suggestion Bright was deployed by Vietnam team.'
sem=load(BASE+'/semantic-review.json')
m.update(status='REVIEW_DRAFT_RENDER_GATE_PENDING',native_feed_desktop='ACTUAL_SELF_REVIEW_ALL_11',new_team_card='ACTUAL_SELF_REVIEW_NATIVE_FEED_DESKTOP_MOBILE',whole_journey='INSUFFICIENT_EVIDENCE_FULL_MOBILE_AND_CANONICAL_RECONCILIATION',po_v4_visual='ACCEPTED_SEPARATE_FROM_V5_TECHNICAL_GATE')
put(OUT+'/manifest.json',m)
post=dict(revision='b13-v5-postgen-v1',stage='POSTGEN_ARTIFACT',status=m['status'],execution='PARTIAL',audit_verdict='INSUFFICIENT_EVIDENCE',reviewer='/root current Fabless session',independence='SELF_REVIEW',authorization=ref(BASE+'/generation-mandate.json'),anchor=anchor,scope=dict(segment='FDI',locale='en',persona=load(BASE+'/dispatch-plan.json')['persona'],route=load(BASE+'/dispatch-plan.json')['route'],branch='slice/linkedin-safe-fabless-parallel'),
 binding=dict(manifest=ref(OUT+'/manifest.json'),copy=ref(OUT+'/selected-copy.json'),prompts=ref(OUT+'/selected-prompts.json'),reader=ref(OUT+'/case-reader.html'),viewer=ref(OUT+'/index.html'),artwork=m['artwork'],attempts=ref(BASE+'/attempt-ledger.json'),evidence=evidence),
 A1_A7={k:sem[k] for k in ['A1','A2','A3','A4','A5','A6','A7']},source=ref(BASE+'/vietnam-team-source.json'),per_unit=unit_reviews,transitions=transitions,reader=dict(observation='Actual desktop reader screenshot inspected, source English-summary disclosure/name/China geography/qualitative context correct; reader and return route observed. Current mobile390x844 DOM text/no overflow observed; capture timed out, no mobile visual PASS.',desktop=ref(BASE+'/evidence/fabless-v5-reader-desktop.jpg'),sha_matches_v4=True),
 proof_scope='Qualitative China outsourced-management integrated-solution case. Local Vietnam ERP consulting/implementation service is a separate source-backed prospective discussion. No Vietnam Fabless deployment, exact F1 mechanism proof, ERP-only causality, metrics, headcounts or all-team language promise.',
 review_discrepancies=[dict(issue='Existing report prop rule-lines are not literally blank paper surfaces',reconciliation='PO latest Visual ổn r/content-only addition interpreted as preserving selected v4 visuals. A5 and reused Bright2 generic unlabelled lines retained, with no record values/text or invented metrics. Do not certify literal all-paper-blank compliance from the prompt. Frozen core/procedure unchanged; this scoped interpretation and visual evidence remain reviewable.'),dict(issue='Immediate screenshots after switching proof2/proof3 showed preceding artwork',reconciliation='Original feed09/feed10 excluded. Rebound after fresh DOM/currentSrc observations; confirmed09/10 screenshots reviewed and selected instead. No asset replacement was required.'),dict(issue='Mobile DOM reads during rapid navigation showed loaded=false/naturalWidth0 for some cards',reconciliation='Transient reads retained as observations, not load or visual PASS. Team final settled mobile capture and nativeWidth1254 verified; all-other mobile captures remain missing.')],
 verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_WHOLE_JOURNEY_FULL_MOBILE',AD_ED_01='INSUFFICIENT_EVIDENCE_WHOLE_SET_FULL_MOBILE',new_team_card='PASS_SELF_REVIEW_IN_NATIVE_FEED_DESKTOP_MOBILE_SCOPE',whole_journey='NOT_READY_NOT_ACCEPTED',independent_native_market='NOT_RUN'),
 technical=dict(feed='All11 current artwork visually inspected at331.22CSSpx plus separate team333CSSpx; caption/native wording compared with selected copy. Some viewer feed native-headline tails below initial viewport; desktop screenshot covers full native headline.',desktop='All11 artwork fully visible at638.22CSSpx in current main viewer, source/body/sequence/logo inspected; actual viewport1707x879. No full-page capture claim.',mobile='Team card actual390x844 DOM image347.56CSSpx and accepted viewport screenshot inspected; body/source/headline all present. Full remaining10 and reader mobile visual captures missing; multiple5000ms timeouts. No raw CDP route used.',capture_failures=['Initial team desktop fullPage timeout5000ms, subsequent viewport capture succeeded','Reader mobile capture timeout5000ms','Cold mobile viewport capture twice timeout5000ms despite settled loaded1254/image inside390x844viewport'],browser_contention='First lock attempt found Partner B22 owner; no tab action; own preliminary server stopped. Later atomic acquisition succeeded, v5 controlled only its created tab.'),
 counts=counts,freeze='24/24 byte identical; locale adapter DEVELOPING/NOT_FROZEN',docs='Owned docs-impact proposal updated for coordinator, shared canonical writes not authorized. Reconcile current-state/build/readiness/source-register before PASS/commit/accepted handoff.',cleanup=dict(own_tab_closed=True,viewport_reset_api_returned=True,immediate_post_reset_DOM=[390,844],viewport_note='Immediate DOM read was not used as proof of restored default dimensions; reset API completed before tab close.',own_servers_stopped=[3840,25028],own_lock_released=True),git='Working-tree files only in owned2roots. No stage/commit/merge/main/push/live.',stop='B14-B21 NOT_RUN; v1-v4 receipts/findings retained historical.')
put(BASE+'/postgen-review.json',post)
put(BASE+'/verification.json',dict(revision='b13-v5-verification-v1',status=post['status'],execution='PARTIAL',frozen_files=frozen,selected11='1254x1254_NATIVE_PNG_BYTES_MATCH_ALL_SOURCES',counts=counts,fresh_dispatch_receipts=receipts,sequence_copy_checks='1/6..6/6; prior five fields unchanged; cold/proof/reader byte/content preserved',postgen=ref(BASE+'/postgen-review.json')))
put(PARENT+'/ledger.json',dict(revision='fabless-lane-ledger-v5',owner='/root current Fabless session',active_batch='B13-en-f1-v5',status=post['status'],execution='PARTIAL',counts=counts,receipt=ref(BASE+'/postgen-review.json'),remaining_queue='B14-B21 NOT_RUN',commit=False,merge=False,push=False,live=False))
(ROOT/OUT/'README.md').write_text('''# B13 Fabless F1 English · v5

11 selected native1254-square PNGs: cold1 + explanation6 + China proof4. Card6 adds Vietnam ERP consulting/implementation team nuance with a concrete first-discussion basis: reporting workflows, update ownership and project priorities. Source: official Digiwin Vietnam electronics ERP implementation publication, scoped to local service presence. No Vietnam Fabless deployment/results or team-size/language promise. Existing explanation1–5 edited sequence5→6; cold+four proof PNGs reused byte-identical from v4. V5=6basecalls (5sequence edits+1newcard),0corrective,5reuse; prior14calls historical, cumulative20. Built-in image_gen; selected-prompts.json records prompts. Reader byte-identical to v4.

Native, feed331.22 and desktop638.22 actual SELF_REVIEW completed for all11. New team card additionally observed at actual mobile390×844/image347.56; caption/headline/body/source all present. Full other10/reader mobile capture remains insufficient due browser timeout; no whole-journey PASS, independent/native-market or v5 PO acceptance inferred. REVIEW_DRAFT_RENDER_GATE_PENDING, execution PARTIAL for full render scope. Existing generic unlabelled rule-lines in approved visual props retained under PO visual-preservation direction; literal all-paper-blank invariant not certified. Prior technical/historical findings remain separate.

Open index.html, compact-review.html, vietnam-team-audit.html and case-reader.html. Receipt/verification/evidence in owned B13-en-f1-v5 operations folder.24frozen pins unchanged; adapter developing. Docs-impact proposal awaits coordinator reconciliation. No ZIP/raster transformation/shared-canonical/Git/live change; browser tab/server closed, override reset API performed, lock returned. Stop before B14.
''',encoding='utf-8')
(ROOT/BASE/'Bao_Review_Vietnamese.md').write_text('''# B13 v5 · thêm nuance đội ngũ tại Việt Nam

Đã thêm explanation card6: “Consulting and implementation in Vietnam”. Body mời trao đổi với đội ngũ tại Việt Nam về tư vấn/triển khai ERP, bắt đầu từ reporting workflows, update ownership và project priorities. Nguồn chính thức Digiwin Vietnam được giữ riêng; không biến case Bright ở Trung Quốc thành case triển khai Fabless tại Việt Nam.

Bộ11PNG native1254:1cold+6explanation+4proof. V5 có6ImageGen calls=5sửa số thứ tự+1card mới,0corrective;5cold/proof reuse đúng byte v4. Tổng lịch sử20calls; v1-v4 không rewrite. Bộ prompt selected-prompts.json, viewer index.html, reader giữ byte v4.

Đã xem actual native/feed/desktop đủ11; riêng card6 đã có screenshot mobile390×844 đầy đủ chữ/nguồn. Full mobile10card còn lại và reader chưa đủ pixel evidence vì capture timeout. Giữ REVIEW_DRAFT_RENDER_GATE_PENDING / execution PARTIAL / MSG-ANCHOR INSUFFICIENT_EVIDENCE cho cả bộ; scoped card6 SELF_REVIEW không là independent/native-market certification. V4 Visual ổn r là PO acceptance riêng visual cũ, không nâng technical PASS hồi tố. Generic unlabelled report lines trong visual cũ giữ theo lệnh giữ visual; không chứng nhận literal mọi giấy trắng.

24frozen pins nguyên; adapter DEVELOPING/NOT_FROZEN. Docs-impact có proposal cho coordinator về counts/status/source mới; không sửa shared canon. Browser/server đóng, gọi reset viewport và trả lock. Chỉ working files tại máy này, chưa stage/commit/main/push/live; B14 chưa chạy.
''',encoding='utf-8')
with (ROOT/PARENT/'docs-impact.md').open('a',encoding='utf-8') as f:
 f.write('\n## B13 v5 — Vietnam team nuance and six-card explanation\n\nCurrent proposal supersedes B13 counts/inventory only: v5 selected11PNG=1cold+6explanation+4proof;6base ImageGen calls=5sequence edits+1new local-service card,0corrective,5PNG reused byte-identical. Historical14calls preserved, cumulative20. PO accepted v4 visual; v5 technical acceptance not inferred. All11 actual native/feed331.22/desktop638.22 reviewed SELF_REVIEW. New Vietnam card also observed mobile390x844/image347.56; full other10/reader mobile pixels insufficient after capture timeouts. REVIEW_DRAFT_RENDER_GATE_PENDING / PARTIAL / wholejourney anchor INSUFFICIENT_EVIDENCE. Existing generic unlabelled report rule-lines retained under PO visual-preservation interpretation; literal all-paper-blank not certified.\n\nCoordinator proposal: reconcile CURRENT_STATE/LinkedIn Build Pack/Pre_Ad_Readiness_Plan with this scoped status before PASS/commit/handoff. Public_Source_Register/creative source governance should add the official Digiwin Vietnam Huakun electronics ERP implementation publication as support for local consulting/implementation service only: https://www.digiwin.com.vn/casestudies/huakun-electronic-viet-nam-san-xuat-thong-minh-digiwin-erp/ . No outcome metrics/testimonial/logo/headcounts/teamwide languages/Fabless Vietnam deployment reused. China Bright qualitative proof remains separately attributed. Audience/anchor/strategy/budget/live rights unchanged. Owned vietnam-team-source.json holds URL/locator/scope; postgen-review.json and verification.json bind actual11.24frozen pins unchanged; adapter developing. No shared canonical update authorized; proposal pending coordinator. Prior receipts/history untouched. Stop before B14; no stage/commit/main/push/live.\n')
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT,text=True)
assert all(line[3:].replace('\\','/').startswith((PARENT+'/',Path(OUT).parent.as_posix()+'/')) for line in status.splitlines())
assert not subprocess.check_output(['git','diff','--cached','--name-only'],cwd=ROOT,text=True).strip()
print(json.dumps(dict(status=post['status'],execution='PARTIAL',counts=counts,frozen24='UNCHANGED',own_roots_only=True),indent=2))
