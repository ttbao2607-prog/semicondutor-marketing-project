"""T3 follow-up, preserve v1 review and artifact folder."""
from prepare_draft import *
from collections import Counter
from PIL import Image
import subprocess
OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v2'
PARENT=Path(BASE).parent.as_posix()
old=load(BASE+'/postgen-review.json');m=load(OUT+'/manifest.json');attempts=load(BASE+'/attempt-ledger.json')['attempts']
f=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']
assert len(f)==24 and all(sha(x['path'])==x['sha256'] for x in f)
assert Counter(x['kind'] for x in attempts)==dict(original=9,corrective=3)
receipts=[]
for a in attempts:
 p=list((ROOT/BASE).glob('**/dispatch/'+a['call_id']+'-fresh-preflight.json'));assert len(p)==1
 d=json.loads(p[0].read_text(encoding='utf-8-sig'));assert d['status']=='PREGEN_INPUTS_VERIFIED' and d['mechanical_verdict']=='PASS'
 assert sha(a['path'])==a['sha256']
 receipts.append(dict(call_id=a['call_id'],path=p[0].relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p[0].read_bytes()).hexdigest()))
for a in m['artwork']:
 assert sha(a['path'])==a['sha256']==sha(a['source'])
 with Image.open(ROOT/a['path']) as im:assert im.size==(1254,1254)
assert len(m['artwork'])==9 and m['not_generated']==['RMK-BRIGHT-4']
assert sha(OUT+'/case-reader.html')==old['binding']['reader_sha256']
cards=load(OUT+'/selected-copy.json')['cards'];assert all((ROOT/OUT/c['image']).is_file() for c in cards if c['image'])
counts=dict(original=9,corrective=3,total_actual_calls=12,reused=0,selected_artwork=9,planned_units=10)
post=dict(revision='b13-postgen-t3-followup-v1',stage='POSTGEN_ARTIFACT',status='PARTIAL_HOLD_CHANGES_REQUIRED',reviewer='/root current Fabless session',independence='SELF_REVIEW',
 prior_review=dict(path=BASE+'/postgen-review.json',sha256=sha(BASE+'/postgen-review.json'),scope='Original8 self-review history; not retrospectively upgraded'),
 authorization=dict(path=BASE+'/t3-authorization.json',sha256=sha(BASE+'/t3-authorization.json')),
 anchor=old['anchor'],scope=old['scope'],A1_A7=old['A1_A7'],proof_scope=old['proof_scope'],
 binding=dict(manifest=dict(path=OUT+'/manifest.json',sha256=sha(OUT+'/manifest.json')),copy=dict(path=OUT+'/selected-copy.json',sha256=sha(OUT+'/selected-copy.json')),viewer_sha256=sha(OUT+'/index.html'),reader_sha256=sha(OUT+'/case-reader.html'),artwork=m['artwork'],attempt_ledger=dict(path=BASE+'/attempt-ledger.json',sha256=sha(BASE+'/attempt-ledger.json')),evidence=[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in (ROOT/BASE/'evidence-t3').glob('*') if p.is_file()]),
 changed_units=[dict(card_id='RMK-BRIGHT-1',exact_source='Digiwin Vietnam · Company introduction',native='SOURCE_HIERARCHY_CLOSED',feed333='ACTUAL_SOURCE_HIERARCHY_CLOSED: publisher larger than body; white safe band; exact copy retained',mobile='INSUFFICIENT_EVIDENCE_CAPTURE_TIMEOUT',brand_role='Official logo once; publisher source once, necessary provenance. No redundant brand header.',voice='We develop and provide retained; direct We provide caption',meaning='Same supplier role and qualitative bridge; no new result, metric, UI or documentary premise',closure='Native/feed only; full desktop/mobile closure pending'),
 dict(card_id='RMK-BRIGHT-3',exact_source='Digiwin Vietnam · China case04 / 上海晶丰明源半导体股份有限公司',native='CHANGES_REQUIRED_PUBLISHER_SMALLER_THAN_BODY',feed333='ACTUAL_CHANGES_REQUIRED: publisher smaller than body; legal name present',mobile='INSUFFICIENT_EVIDENCE_CAPTURE_TIMEOUT',brand_role='Official logo once; publisher/locator once; full Chinese entity. No redundant brand header.',voice='Case third-person customer; direct supplier caption; publisher attribution distinct',meaning='Exact outsourcing-management challenge/integrated digital solution; no ERP-only causality. Blank illustrative records/open paths/neutral chips, no technical or quantified data/customer premise.',action='Needs first corrective for this card, batch T4 beyond authorized T3. HOLD')],
 stable_units='Other7 PNGs and copy match v1 byte. Actual full9 feed333 rechecked; prior native/mobile evidence remains revision-bound history, no fresh all9 mobile visual review.',
 transitions=[dict(from_card=a['card_id'],to_card=b['card_id'],script='Same reviewed content/order',postgen='SCOPED_NATIVE_FEED_MATCH_NO_FULL_RENDER_PASS' if a['image'] and b['image'] else 'INSUFFICIENT_EVIDENCE_MISSING_ARTWORK') for a,b in zip(cards,cards[1:])],
 rendered=dict(feed='Actual all9 artwork + caption/native headline viewed at333CSSpx in compact fullpage screenshot, viewport1707x817, no overflow',mobile='Actual390x844 DOM:9 loaded images at319.55557CSSpx, no overflow. Fullpage/focused viewport screenshot each timed out5000ms. DOM is not visual evidence or PASS.',main_desktop='Updated card7/card9/card10 navigation observed DOM; T3 selected asset loaded. No new all9 main640 screenshot review.',reader='Byte-identical to prior desktop/mobile-reviewed reader; no fresh browser reader PASS claimed'),
 findings=[dict(id='B13-SOURCE-1',status='CLOSED_NATIVE_FEED_ONLY_MOBILE_PENDING',card_id='RMK-BRIGHT-1'),dict(id='B13-SOURCE-3',status='OPEN_CHANGES_REQUIRED',card_id='RMK-BRIGHT-3',exact='Digiwin Vietnam · China case04',effect='Publisher smaller than body at native/feed333',needed='Batch T4, not authorized by T3 exception')],
 verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_WHOLE_JOURNEY',AD_ED_01='CHANGES_REQUIRED_SOURCE_HIERARCHY_AND_INCOMPLETE_RENDER',whole_journey='NOT_READY_NOT_ACCEPTED'),counts=counts,not_generated=['RMK-BRIGHT-4'],stop='T3 exception consumed; no T4/B14. Further source finding requires HOLD under plan.',cleanup=dict(viewport_reset=True,own_tab_closed=True,own_server_pid=16732,own_server_stopped=True,own_atomic_browser_lock_released=True),git='Local working-tree files only; no stage/commit/main merge/push/live.')
put(BASE+'/postgen-review-t3.json',post)
put(BASE+'/verification-t3.json',dict(revision='b13-verification-t3-v1',frozen24='24/24_BYTE_IDENTICAL',selected9='1254x1254_NATIVE_BYTES_IDENTICAL',fresh_dispatch_receipts=receipts,reader='BYTE_IDENTICAL_TO_PRIOR_REVIEW',counts=counts,status=post['status']))
put(PARENT+'/ledger.json',dict(revision='fabless-lane-ledger-v2-t3',owner='/root current Fabless session',active_batch='B13-en-f1-v2',status=post['status'],counts=counts,receipt=dict(path=BASE+'/postgen-review-t3.json',sha256=sha(BASE+'/postgen-review-t3.json')),prior_receipt=post['prior_review'],remaining_queue='B14-B21 NOT_RUN; stop for Bao',commit=False,merge=False,push=False,live=False))
(ROOT/BASE/'Bao_Review_T3_Vietnamese.md').write_text('''# B13 sau T3 · PARTIAL / HOLD

Bảo cho phép “Cho phép lượt sửa T3.” T3 sửa riêng RMK-BRIGHT-1; nguồn tăng lớn hơn body, khép ở native/feed333. Mobile capture mới timeout nên chưa khép đủ mobile. V1 receipt/ảnh/manifest giữ nguyên; bộ mới ở B13-en-f1-v2.

Đã generate tiếp RMK-BRIGHT-3: đúng nội dung, pháp nhân China và qualitative integrated-solution scope. Dòng “Digiwin Vietnam · China case04” nhỏ hơn body ở native/feed333. Cần corrective4; ngoại lệ T3 không cấp T4. Dừng ngay, RMK-BRIGHT-4 chưa generate.

Tổng12calls =9original +3corrective;9/10ảnh chọn,0reuse. All9 feed333 thực tế đã xem. DOM mobile390×844 cho thấy9ảnh load ở319.56px, nhưng screenshot fullpage/focused đều timeout; không gọi DOM là visual PASS. Reader giữ byte bản đã review desktop/mobile. Whole journey MSG-ANCHOR INSUFFICIENT_EVIDENCE, AD-ED CHANGES_REQUIRED.

24frozen pins nguyên; adapter DEVELOPING/NOT_FROZEN. Server/tab riêng đã đóng, viewport reset, trả browser lock. Chỉ file working-tree ở2root sở hữu, chưa stage/commit/main/push/live. B14 chưa chạy.
''',encoding='utf-8')
with (ROOT/PARENT/'docs-impact.md').open('a',encoding='utf-8') as out:
 out.write('\n## T3 follow-up — current proposal supersedes execution counts only\n\nPO authorized extra T3 for Bright1. Current B13-en-f1-v2:9/10PNG;12calls=9original+3corrective. Bright1 source closed native/feed333, mobile capture pending. New Bright3 publisher smaller than body requires T4 outside exception, HOLD; Bright4 not generated. Full9 feed333 reviewed; mobile DOM load is not visual PASS. Reader byte unchanged. Final anchor insufficient/editorial changes required.24frozen pins unchanged; no shared canon/core/adapter/Git/live change. Evidence: B13-en-f1-v1/postgen-review-t3.json and verification-t3.json. Coordinator to reconcile CURRENT_STATE/build/readiness before acceptance/commit promotion. Prior receipts remain historical.\n')
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT,text=True)
assert all(line[3:].replace('\\','/').startswith((PARENT+'/',Path(OUT).parent.as_posix()+'/')) for line in status.splitlines())
print(json.dumps(dict(status=post['status'],counts=counts,frozen24='24/24 unchanged',writes='Owned roots only'),indent=2))
