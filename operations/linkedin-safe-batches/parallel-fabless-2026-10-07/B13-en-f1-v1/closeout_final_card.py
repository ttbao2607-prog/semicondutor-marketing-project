"""Complete inventory; retain prior scoped reviews and unresolved findings."""
from prepare_draft import *
from PIL import Image
from collections import Counter
import subprocess
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v3';PARENT=Path(BASE).parent.as_posix()
prior=load(BASE+'/postgen-review-t3.json');m=load(OUT+'/manifest.json');attempts=load(BASE+'/attempt-ledger.json')['attempts']
assert Counter(a['kind'] for a in attempts)==dict(original=10,corrective=3)
frozen=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files'];assert len(frozen)==24 and all(sha(a['path'])==a['sha256'] for a in frozen)
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
counts=dict(original=10,corrective=3,total_actual_calls=13,reused=0,selected_artwork=10,planned_units=10)
post=dict(revision='b13-final10-postgen-v1',stage='POSTGEN_ARTIFACT',status='IMAGE_INVENTORY_COMPLETE_ARTIFACT_CHANGES_REQUIRED',execution='PARTIAL_RENDER_AND_EDITORIAL_GATES',reviewer='/root current Fabless session',independence='SELF_REVIEW',
 authorization=dict(path=BASE+'/final-card-authorization.json',sha256=sha(BASE+'/final-card-authorization.json')),
 previous_review=dict(path=BASE+'/postgen-review-t3.json',sha256=sha(BASE+'/postgen-review-t3.json'),scope='Retain card3 CHANGES_REQUIRED and changed-card mobile/main640 gaps; no retrospective PASS'),
 anchor=prior['anchor'],scope=prior['scope'],A1_A7=prior['A1_A7'],proof_scope=prior['proof_scope'],
 binding=dict(manifest=dict(path=OUT+'/manifest.json',sha256=sha(OUT+'/manifest.json')),copy=dict(path=OUT+'/selected-copy.json',sha256=sha(OUT+'/selected-copy.json')),prompts=dict(path=OUT+'/selected-prompts.json',sha256=sha(OUT+'/selected-prompts.json')),viewer_sha256=sha(OUT+'/index.html'),reader_sha256=sha(OUT+'/case-reader.html'),artwork=m['artwork'],attempt_ledger=dict(path=BASE+'/attempt-ledger.json',sha256=sha(BASE+'/attempt-ledger.json')),evidence=[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (ROOT/BASE/'evidence-final').glob('*') if p.is_file()]),
 final_card=dict(card_id='RMK-BRIGHT-4',exact_headline='Read the chip-design case',exact_source='Digiwin Vietnam · digiwin.com.vn / Semiconductor case04 / 上海晶丰明源半导体股份有限公司',exact_cta='Read the China case',native='ACTUAL_SELF_REVIEW: exact approved text/source/name/category4of4; source at least body-size; CTA separate; no metric/UI/facility/skyline',desktop='ACTUAL_SELF_REVIEW: main viewer artwork638.2222CSSpx; source/CTA readable, exact, no clipping; caption/native headline match',feed='DOM loaded331.2222CSSpx only; screenshot timeout5000ms, INSUFFICIENT_EVIDENCE',mobile='Screenshot timeout5000ms; requested351x760 but readback1707x817, no actual390 or visual PASS',brand_role='Official Digiwin logo once; publisher/domain locator necessary attribution, no redundant brand header',voice='Direct supplier We provide caption; artwork invites reading, customer/source properly attributed',scene='Unlabelled chip display folio rather than blank booklet: visual-fidelity observation, no claim of customer product/result',transition='Qualitative outsourcing-management pain/integrated solution -> source invitation -> English summary; actual native/desktop consistent with same Operations/SCM reader',reader_navigation='Actual Card10 reader link -> English reader -> return index Card1; reader byte identical to prior reviewed destination'),
 verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_WHOLE_JOURNEY',AD_ED_01='CHANGES_REQUIRED_CARD3_SOURCE_AND_INCOMPLETE_RENDER',whole_journey='NOT_READY_NOT_ACCEPTED'),open_findings=prior['findings'],counts=counts,not_generated=[],cleanup=dict(viewport_reset=True,own_tab_closed=True,own_server_pid=12924,own_server_stopped=True,own_atomic_browser_lock_released=True),stop='B13 complete image inventory; no T4/B14; await PO disposition',git='Working files only; no stage/commit/main merge/push/live')
put(BASE+'/postgen-review-final10.json',post)
put(BASE+'/verification-final10.json',dict(revision='b13-final10-verification-v1',frozen24='24/24_BYTE_IDENTICAL',selected10='1254x1254_NATIVE_BYTES_IDENTICAL',counts=counts,fresh_dispatch_receipts=receipts,reader='BYTE_IDENTICAL_TO_PRIOR_REVIEW',status=post['status']))
put(PARENT+'/ledger.json',dict(revision='fabless-lane-ledger-v3-complete10',owner='/root current Fabless session',active_batch='B13-en-f1-v3',status=post['status'],counts=counts,receipt=dict(path=BASE+'/postgen-review-final10.json',sha256=sha(BASE+'/postgen-review-final10.json')),remaining_queue='B14-B21 NOT_RUN',commit=False,merge=False,push=False,live=False))
(ROOT/BASE/'Bao_Review_Final10_Vietnamese.md').write_text('''# B13 · đủ10ảnh, chưa nghiệm thu toàn bộ

Theo lệnh “Gent card cuối cho hoàn chỉnh luôn đi codex.” đã generate RMK-BRIGHT-4; nguồn/body/CTA đúng, rõ ở native/desktop638.22px. Reader link và return đã click kiểm tra. Folio trưng chip thay booklet giữ như visual-fidelity observation; không có dữ liệu/kết quả/facility giả.

B13-en-f1-v3 có10/10PNG1254square native bytes,13calls=10original+3corrective,0reuse. Viewer/reader/copy/prompts/manifest đầy đủ. V1/v2 và receipt lịch sử giữ nguyên.

Card3 publisher nhỏ hơn body, CHANGES_REQUIRED giữ nguyên. Lệnh gent card cuối không cấp corrective4. Feed/mobile capture card cuối timeout; viewport readback không xác nhận390, không visual PASS. Final MSG-ANCHOR wholejourney INSUFFICIENT_EVIDENCE, chưa ready/accepted. B14 chưa chạy.

24frozen pins nguyên; adapter developing. Server/tab đóng, viewport reset, lock trả. Chỉ working files local ở nhánh sở hữu, chưa stage/commit/main/push/live. Shared docs impact proposal riêng cho coordinator.
''',encoding='utf-8')
with (ROOT/PARENT/'docs-impact.md').open('a',encoding='utf-8') as out:
 out.write('\n## Final original card — current inventory update\n\nPO authorized Bright4 despite Bright3 finding. B13-en-f1-v3 now10/10selected native1254PNG,13calls=10original+3corrective,0reuse. Finalcard native/desktop source+CTA observed; reader/return clicked, reader byte unchanged. Bright3 source CHANGES_REQUIRED retained; feed/mobile and wholejourney anchor INSUFFICIENT_EVIDENCE retained. No acceptance/T4/B14/lifecycle/Git/live authority. Frozen24 identical. Coordinator current-state/build/readiness proposal; evidence postgen-review-final10.json / verification-final10.json. Historical receipts untouched.\n')
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT,text=True)
assert all(line[3:].replace('\\','/').startswith((PARENT+'/',Path(OUT).parent.as_posix()+'/')) for line in status.splitlines())
print(json.dumps(dict(status=post['status'],counts=counts,frozen24='24/24 unchanged',writes='Owned roots only'),indent=2))
