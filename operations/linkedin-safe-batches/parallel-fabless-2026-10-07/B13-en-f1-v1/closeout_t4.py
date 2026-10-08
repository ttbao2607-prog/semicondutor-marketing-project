"""Actual card3 corrective closure, no fabricated mobile/whole-journey PASS."""
from prepare_draft import *
from PIL import Image
from collections import Counter
import subprocess,shutil
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v4';PARENT=Path(BASE).parent.as_posix()
prior=load(BASE+'/postgen-review-final10.json');m=load(OUT+'/manifest.json');attempts=load(BASE+'/attempt-ledger.json')['attempts']
assert Counter(a['kind'] for a in attempts)==dict(original=10,corrective=4)
f=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files'];assert len(f)==24 and all(sha(a['path'])==a['sha256'] for a in f)
assert len(m['artwork'])==10 and not m['not_generated']
for a in m['artwork']:
 assert sha(a['path'])==a['sha256']==sha(a['source'])
 with Image.open(ROOT/a['path']) as im:assert im.size==(1254,1254)
assert sha(OUT+'/case-reader.html')==prior['binding']['reader_sha256']
assert sha('operations/Vy_Email_Content_Anchor.md')==prior['anchor']['sha256']
receipts=[]
for a in attempts:
 p=list((ROOT/BASE).glob('**/dispatch/'+a['call_id']+'-fresh-preflight.json'));assert len(p)==1
 d=json.loads(p[0].read_text(encoding='utf-8-sig'));assert d['status']=='PREGEN_INPUTS_VERIFIED' and d['mechanical_verdict']=='PASS'
 receipts.append(dict(call_id=a['call_id'],path=p[0].relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p[0].read_bytes()).hexdigest()))
ev=ROOT/BASE/'evidence-t4'
if (ev/'fabless-t4-feed.png').exists():shutil.copyfile(ev/'fabless-t4-feed.png',ev/'card3-feed.jpg')
m.update(status='REVIEW_DRAFT_RENDER_GATE_PENDING',card3_source_finding='CLOSED_NATIVE_FEED_SELF_REVIEW',whole_journey='INSUFFICIENT_EVIDENCE',imagegen_original=10,imagegen_corrective=4)
put(OUT+'/manifest.json',m)
(ROOT/OUT/'README.md').write_text('''# B13 English Fabless F1 · corrected card3 v4

Ten selected1254square native PNGs,14calls=10original+4corrective,0reuse. Card3 source hierarchy corrected under explicit PO instruction, scoped PASS/native+actual331.22px feed self-review. Exact publisher/legal name now larger than body. Native wording/brand/voice/qualitative China source scope unchanged. V1/v2/v3 and receipts remain historical.

REVIEW_DRAFT_RENDER_GATE_PENDING. Card3 actual mobile390x844 DOM load observed but capture timed out; main638.22px desktop capture also timed out. Raw CDP mobile attempt rejected due denied permission and stopped. No full card3 desktop/mobile editorial PASS or whole-journey acceptance. Card3 source-size material finding closed in evidenced scope; missing-render evidence kept separately. Other9 PNGs unchanged from v3; reader byte-identical to previously reviewed English destination. Open index.html, case-reader.html and card3-audit.html. No ZIP/raster transforms/core/adapter changes/commit/main/push/live. Stop before B14.
''',encoding='utf-8')
counts=dict(original=10,corrective=4,total_actual_calls=14,reused=0,selected_artwork=10)
post=dict(revision='b13-card3-t4-postgen-v1',stage='POSTGEN_ARTIFACT',status='REVIEW_DRAFT_RENDER_GATE_PENDING',execution='PARTIAL_FULL_RENDER_EVIDENCE',reviewer='/root current Fabless session',independence='SELF_REVIEW',
 authorization=dict(path=BASE+'/t4-authorization.json',sha256=sha(BASE+'/t4-authorization.json')),
 previous_review=dict(path=BASE+'/postgen-review-final10.json',sha256=sha(BASE+'/postgen-review-final10.json'),scope='Prior v3 finding not retrospectively upgraded'),anchor=prior['anchor'],scope=prior['scope'],A1_A7=prior['A1_A7'],proof_scope=prior['proof_scope'],
 binding=dict(manifest=dict(path=OUT+'/manifest.json',sha256=sha(OUT+'/manifest.json')),copy=dict(path=OUT+'/selected-copy.json',sha256=sha(OUT+'/selected-copy.json')),prompts=dict(path=OUT+'/selected-prompts.json',sha256=sha(OUT+'/selected-prompts.json')),viewer_sha256=sha(OUT+'/index.html'),reader_sha256=sha(OUT+'/case-reader.html'),audit_page_sha256=sha(OUT+'/card3-audit.html'),artwork=m['artwork'],attempt_ledger=dict(path=BASE+'/attempt-ledger.json',sha256=sha(BASE+'/attempt-ledger.json')),evidence=[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in ev.glob('*') if p.is_file()]),
 card_review=dict(card_id='RMK-BRIGHT-3',exact_headline='Outsourcing management in focus',exact_body='The case identifies inefficient outsourcing management among its challenges and describes an integrated digital solution.',exact_source='Digiwin Vietnam · China case04 / 上海晶丰明源半导体股份有限公司',native='ACTUAL_SELF_REVIEW: exact words/name/category3of4 and logo once; source publisher/legal name larger than body, plain full-width white band with safe margins. Blank illustrative reports/open paths/chips retained; no metrics/UI/facility/new meaning.',feed='ACTUAL_SELF_REVIEW: static audit at331.2222CSSpx, caption/native headline/source/body inspected. Publisher/legal name readable and larger than body, no clipping.',desktop='Mainviewer DOM image638.2222CSSpx loaded, no overflow, screenshot timeout5000ms: INSUFFICIENT_EVIDENCE for visual desktop640 closure',mobile='Actual390x844 DOM image331.2222px loaded, no overflow; screenshot timeout5000ms, no visual PASS. Fresh tab reverted1707x817 and captured desktop feed; that screenshot is not mobile.',brand_role='Official logo once; publisher source once, exact case locator/legal entity necessary for provenance. No redundant DIGIWIN header.',advertiser_voice='We provide caption; case third-person customer, publisher distinct source. Body reports qualitative challenge/solution with exact named China context.',scene='Blank partner record surfaces and open coordination paths; neutral chips, not customer equipment/product/technical data.',transition='Proof2 named chip-design China entity -> proof3 outsourcing-management qualitative challenge/integrated solution -> proof4 read case -> unchanged English summary. Same Operations/SCM decision unit, no metric/F1-mechanism/ERP-only causality.',source_finding='B13-SOURCE-3 CLOSED_NATIVE_FEED',scoped_verdict='SOURCE_HIERARCHY_PASS_NATIVE_FEED_SELF_REVIEW'),
 blocked_action=dict(action='Raw CDP mobile emulation/capture on owned localhost audit tab',reason='Browser security policy reported denied permission/user declined. No CDP mutation executed; stopped route and did not bypass.',effect='Mobile evidence remains insufficient'),
 verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_WHOLE_JOURNEY',AD_ED_01_CARD3='INSUFFICIENT_EVIDENCE_FULL_DESKTOP_MOBILE',source_hierarchy='PASS_NATIVE_FEED_ONLY',whole_journey='NOT_READY_NOT_ACCEPTED'),
 stable_units='Other9 selected PNGs match v3 byte; reader unchanged. No retrospective whole-set render certification.',material_source_findings='No remaining source-size finding observed in selected native scope; card3 closure native/feed only. Render gaps remain separate.',counts=counts,
 cleanup=dict(viewport_reset=True,own_tabs_closed=True,own_server_pid=13280,own_server_stopped=True,own_browser_lock_released=True),stop='No B14, independent/native-market or PO acceptance inferred',git='Working-tree files in own2roots only, no stage/commit/main merge/push/live')
put(BASE+'/postgen-review-t4.json',post)
put(BASE+'/verification-t4.json',dict(revision='b13-t4-verification-v1',frozen24='24/24_BYTE_IDENTICAL',selected10='1254x1254_NATIVE_BYTES_IDENTICAL',fresh_dispatch_receipts=receipts,counts=counts,status=post['status']))
put(PARENT+'/ledger.json',dict(revision='fabless-lane-ledger-v4-card3',owner='/root current Fabless session',active_batch='B13-en-f1-v4',status=post['status'],counts=counts,receipt=dict(path=BASE+'/postgen-review-t4.json',sha256=sha(BASE+'/postgen-review-t4.json')),remaining_queue='B14-B21 NOT_RUN',commit=False,merge=False,push=False,live=False))
(ROOT/BASE/'Bao_Review_T4_Vietnamese.md').write_text('''# B13 · sửa card3 T4

Lệnh “Xử lý card 3 để pass hậu kiểm.” cấp corrective4 riêng card3. Exact nguồn publisher và pháp nhân đã tăng lớn hơn body, an toàn trong white band. Finding B13-SOURCE-3 khép ở native và feed331.22px actual SELF_REVIEW; nội dung/claim/voice/category/logo giữ đúng. Bộ v4 đủ10PNG,14calls=10original+4corrective;9ảnh khác và reader giữ byte v3.

Full hậu kiểm card3 chưa PASS: desktop638.22px DOM load nhưng capture timeout; mobile actual390×844 load ảnh331.22px nhưng screenshot timeout. Fresh-tab screenshot là1707px desktop, không dùng làm mobile. Browser từ chối raw CDP vì quyền bị từ chối; dừng route, không bypass. Mobile/main640 và wholejourney MSG-ANCHOR vẫn INSUFFICIENT_EVIDENCE. Source hierarchy có scoped PASS native/feed, không independent/native-market certification.

V1/v2/v3 và findings lịch sử không rewrite.24frozen pins nguyên; adapter developing. Tabs/server đóng, viewport reset, lock trả. Chưa stage/commit/main/push/live; B14 chưa chạy. Docs-impact có proposal cập nhật trạng thái cho coordinator.
''',encoding='utf-8')
with (ROOT/PARENT/'docs-impact.md').open('a',encoding='utf-8') as out:
 out.write('\n## Card3 T4 — current corrective closure\n\nPO authorized Bright3 corrective4. V4 selected10PNG,14calls=10original+4corrective. Card3 publisher/legal-name enlarged; B13-SOURCE-3 CLOSED native/feed331.22px SELF_REVIEW. Full desktop640/mobile screenshots timeout; raw CDP mobile refused permission, route stopped. No full card/wholejourney PASS, REVIEW_DRAFT_RENDER_GATE_PENDING / anchor INSUFFICIENT_EVIDENCE.9otherPNG/reader byte unchanged, frozen24 same. Prior receipts remain historical. Coordinator current-state/build/readiness proposal; evidence postgen-review-t4.json / verification-t4.json. No shared docs/core/adapter/Git/live change.\n')
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT,text=True)
assert all(line[3:].replace('\\','/').startswith((PARENT+'/',Path(OUT).parent.as_posix()+'/')) for line in status.splitlines())
print(json.dumps(dict(status=post['status'],card3_source='PASS_NATIVE_FEED_SELF_REVIEW',counts=counts,frozen24='24/24 unchanged'),indent=2))
