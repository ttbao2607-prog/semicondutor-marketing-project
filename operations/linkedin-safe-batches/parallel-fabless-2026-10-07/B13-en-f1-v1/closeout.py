"""Record actual B13 partial outcome and verify owned evidence. No generation."""
from prepare_draft import *
from collections import Counter
from PIL import Image
import re, subprocess

OUT='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v1'
PARENT=Path(BASE).parent.as_posix()
anchor='operations/Vy_Email_Content_Anchor.md'
email='operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md'
manifest=load(OUT+'/manifest.json')
cards=load(OUT+'/selected-copy.json')['cards']
attempts=load(BASE+'/attempt-ledger.json')['attempts']
evidence=sorted((ROOT/BASE/'evidence').glob('*'))
pins=[dict(path=p.relative_to(ROOT).as_posix(),sha256=hashlib.sha256(p.read_bytes()).hexdigest()) for p in evidence if p.is_file()]
review=load(BASE+'/semantic-review.json')
unit_reviews=[]
for c in cards:
    generated=bool(c['image'])
    source=c.get('source_text','')
    unit_reviews.append(dict(card_id=c['card_id'],generated=generated,fields={k:c.get(k) for k in ['caption','headline','body','artwork_labels','source_text','cta','native_headline','alt']},
        message_observation=review['per_unit_disposition'][c['card_id']],
        native='ACTUAL_SELF_REVIEW' if generated else 'NOT_GENERATED',feed='ACTUAL_333PX_SELF_REVIEW' if generated else 'NOT_GENERATED',mobile='ACTUAL_390X844_IMAGE319_56PX_SELF_REVIEW' if generated else 'NOT_GENERATED',
        brand_roles=dict(official_logo_count=1 if generated else None,extra_brand_header=0 if generated else None,source_exact=source,source_role='Publisher attribution; retain' if source else 'No publisher text needed on this unit'),
        advertiser_voice='Direct We provide in caption; customer case remains third person; source name is publisher attribution',
        disposition='CHANGES_REQUIRED_SOURCE_HIERARCHY' if c['card_id']=='RMK-BRIGHT-1' else 'SCOPED_MATCH_NO_FULL_RENDER_PASS' if generated else 'INSUFFICIENT_EVIDENCE_NOT_GENERATED'))
transitions=[dict(from_card=a['card_id'],to_card=b['card_id'],script='ACTUAL_SELF_REVIEW',postgen='SCOPED_NATIVE_FEED_MOBILE_MATCH' if a['image'] and b['image'] else 'INSUFFICIENT_EVIDENCE_MISSING_ARTWORK') for a,b in zip(cards,cards[1:])]
post=dict(revision='b13-postgen-review-v1',stage='POSTGEN_ARTIFACT',batch='B13',status='PARTIAL_HOLD_CHANGES_REQUIRED',reviewer='/root current Fabless session',independence='SELF_REVIEW',
    anchor=dict(id='VY-CONTENT-ANCHOR',revision='1.0',path=anchor,sha256=sha(anchor),original_email=dict(path=email,sha256=sha(email))),
    scope=dict(segment='FDI',locale='en',persona=PERSONA,route=ROUTE,branch='slice/linkedin-safe-fabless-parallel'),
    binding=dict(manifest=dict(path=OUT+'/manifest.json',sha256=sha(OUT+'/manifest.json')),copy=dict(path=OUT+'/selected-copy.json',sha256=sha(OUT+'/selected-copy.json')),reader_script=dict(path=BASE+'/reader-script.json',sha256=sha(BASE+'/reader-script.json')),viewer_sha256=sha(OUT+'/index.html'),reader_sha256=sha(OUT+'/case-reader.html'),artwork=manifest['artwork'],evidence=pins),
    A1_A7={k:review[k] for k in ['A1','A2','A3','A4','A5','A6','A7']},
    unit_reviews=unit_reviews,transitions=transitions,
    rendered=dict(feed='All8 actual images + captions/native headlines visually inspected in static compact page at333CSSpx',mobile='All8 actual images + captions/native headlines visually inspected, measured390x844 viewport and319.55557CSSpx artwork; no horizontal overflow',canary='Actual390x844, artwork333px in separate canary; not substituted for all8 mobile evidence',main_desktop='Cold screenshot observed, image638.222CSSpx; F1-A1 DOM loaded but screenshot timed out; remaining all8 main640 sequence INSUFFICIENT_EVIDENCE',reader='Actual English reader desktop1707x817 and mobile390x844 screenshot review; no overflow; source URL inspected and return clicked; external source link not clicked in this postcheck',navigation='Reader return -> card1 observed; Card9 -> Next -> Card10 observed with explicit NOT GENERATED state'),
    findings=[dict(id='B13-SOURCE-1',card_id='RMK-BRIGHT-1',exact='Digiwin Vietnam · Company introduction',status='OPEN_CHANGES_REQUIRED',effect='Publisher provenance visibly smaller than body at native/feed/mobile',action='Fresh layout review and corrective3 required; HOLD because cap2 already consumed',owner='Fabless session; PO cap decision needed'),dict(id='B13-PROOF-2',card_id='RMK-BRIGHT-2',status='CLOSED_SCOPED_NATIVE_FEED_MOBILE',closure='Corrective1 enlarged publisher/legal-name block and removed unapproved skyline/icon divider; actual selected image and all8 captures reviewed'),dict(id='B13-COLD-1',card_id='COLD-FABLESS-B13',status='CLOSED_SCOPED_NATIVE_FEED_MOBILE',closure='Corrective1 restored OUTSOURCED CHIP OPERATIONS and removed small paper glyphs; actual selected image and all8 captures reviewed')],
    visual_fidelity_observations=['F1-A1 omitted neutral open paths; F1-A3 omitted stage nodes/open paths; F1-A4 omitted connection but owner token remains. These omissions do not assert a production result; PO visual disposition pending.','F1-A5 uses unlabelled document/chip/team panels instead of compact open-path platform. F1-A5 and Bright2 paper bands remain unlabelled decorative observations, no technical/quantified case data. No broad visual PASS.'],
    proof_scope='Narrow qualitative China outsourcing-management case bridge only. No claim exact F1 mechanism is documented, no ERP-only causality, Vietnam deployment, or numeric ROI/results.',
    verdicts=dict(MSG_ANCHOR_01='INSUFFICIENT_EVIDENCE_WHOLE_JOURNEY',AD_ED_01='CHANGES_REQUIRED_SOURCE_HIERARCHY_AND_INCOMPLETE_RENDER',BRAND_ROLE='SCOPED_SELF_REVIEW_NO_REDUNDANT_HEADER_OBSERVED',ADVERTISER_VOICE='SCOPED_SELF_REVIEW_DIRECT_SUPPLIER_VOICE',whole_journey='NOT_READY_NOT_ACCEPTED'),
    counts=dict(original=8,corrective=2,total_actual_calls=10,reused=0,selected_artwork=8,planned_units=10),not_generated=['RMK-BRIGHT-3','RMK-BRIGHT-4'],
    stop='Plan explicitly requires HOLD at correction3. No further calls, no B14. No independent/native-market/runtime certification or retrospective acceptance.',
    cleanup=dict(viewport_reset=True,own_tab_closed=True,own_server_pid=8548,own_server_stopped=True,port8767_free=True,own_atomic_browser_lock_released=True),
    git='Working-tree files only in owned roots; no commit, merge, push or shared canonical mutation.')
put(BASE+'/postgen-review.json',post)

canonical=['CURRENT_STATE.md','DOCS_IMPACT_MAP.md','operations/Vy_Email_Content_Anchor.md','operations/Ad_Artifact_Editorial_QA_Gate.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','operations/Public_Source_Register.md','operations/LinkedIn_Awareness_Demo_and_Human_Audit_Runbook.md','operations/LinkedIn_Safe_Batch_Execution_Plan_2026-10-06.md']
put(PARENT+'/docs-reviewed.json',dict(revision='b13-docs-impact-review-v1',files=[dict(path=p,sha256=sha(p)) for p in canonical],decision='Own lane status changes; proposed canonical update for coordinator, no shared canonical write authorized'))
(ROOT/PARENT/'docs-impact.md').write_text('''# B13 documentation impact — 2026-10-07

Reviewed CURRENT_STATE, DOCS_IMPACT_MAP, current email anchor, AD-ED-01, LinkedIn Build Pack, readiness, source register, Awareness audit runbook and safe batch plan. Exact hashes in docs-reviewed.json.

B13 changes offline lane execution status only. Content uses a narrowly attributed qualitative China case04 outsourcing-management bridge; excludes conflicting historical numeric baselines. No strategy, approved budget, public route, account, tracking, rights expansion, harness or adapter lifecycle change.

Proposed coordinator status addition for CURRENT_STATE / Build Pack / readiness: B13 English Fabless F1 has8 of10 selected native1254-square PNGs,10 actual calls=8original+2corrective, no reuse. Cold/category and Bright2 source/skyline findings closed in scoped native/feed/mobile self-review. Bright1 source still too small, requiring corrective3 beyond cap2; proof3/4 ungenerated. PARTIAL/HOLD/CHANGES_REQUIRED; whole-journey MSG-ANCHOR INSUFFICIENT_EVIDENCE and all8 main640 visual evidence incomplete. Reader desktop/mobile observed. Frozen24pins unchanged; locale adapter DEVELOPING/NOT_FROZEN. Working files in owned worktree only; no commit/main/push/live. Stop before B14.

No shared canonical files edited under exclusive lane-write mandate. This proposed update must be reconciled by coordinator before acceptance/commit/handoff promotion. Historical findings remain intact. No ready or accepted state claimed.
''',encoding='utf-8')
(ROOT/BASE/'Bao_Review_Vietnamese.md').write_text('''# B13 · Fabless F1 English — PARTIAL / HOLD

Đã chạy intake → source/persona/bridge review → script/anchor/editorial → release/guard từng call → canary → generation → native/feed/mobile/reader hậu kiểm. Kết quả chưa đủ10ảnh: có8PNG chọn,10calls gồm8original +2corrective,0reuse.

Hai corrective đã khép: cold khôi phục category và bỏ glyph nhỏ; Bright2 tăng chữ nguồn/pháp nhân và bỏ skyline ngoài storyboard. Bright1 còn dòng “Digiwin Vietnam · Company introduction” nhỏ hơn body, cần corrective3. Plan cap2 buộc dừng; Bright3/4 chưa generate. Không gọi thêm để lấp số lượng.

Persona là Operations/SCM tại commercial Fabless FDI có sản xuất thuê ngoài; quyền mua/hệ thống thực của account còn unknown. Case04 Trung Quốc chỉ nối qualitative pain quản trị thuê ngoài với integrated digital solution. Không dùng ROI/số liệu hoặc suy ERP-only causality / Việt Nam deployment.

Actual8 artwork/caption/native đã xem tại feed333 và mobile390×844 với artwork319.56px. Reader desktop/mobile và return link observed. Main desktop artwork638.22px chỉ có cold screenshot; ảnh kế timeout, không full640 PASS. Một số khác biệt scene nhẹ giữ thành visual-fidelity observations chờ PO disposition. Final MSG-ANCHOR toàn journey INSUFFICIENT_EVIDENCE; AD-ED CHANGES_REQUIRED. SELF_REVIEW, không independent/native-market certification.

Viewer/reader/copy/prompts/manifest ở deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07/B13-en-f1-v1. Full attempts/guard/evidence giữ trong folder này. Worktree D:/LinkedIn_Safe_Fabless_2026-10-07, branch slice/linkedin-safe-fabless-parallel; chỉ file working-tree local, chưa commit/main/push. Frozen24pins nguyên, adapter developing. B14 chưa chạy. Docs impact có proposal riêng cho coordinator; shared canonical không bị sửa.

Muốn hoàn tất B13 cần quyết định riêng của Bảo về corrective vượt cap, rồi fresh layout/semantic release/guard cho Bright1,2original còn lại và hậu kiểm toàn journey. Receipt hiện tại giữ nguyên trạng thái chưa đạt.
''',encoding='utf-8')

frozen=load('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']
assert len(frozen)==24 and all(sha(x['path'])==x['sha256'] for x in frozen)
assert Counter(x['kind'] for x in attempts)==dict(original=8,corrective=2)
dispatch=[]
for a in attempts:
    receipts=list((ROOT/BASE).glob('**/dispatch/'+a['call_id']+'-fresh-preflight.json'))
    assert len(receipts)==1,(a['call_id'],receipts)
    d=json.loads(receipts[0].read_text(encoding='utf-8-sig'));assert d['status']=='PREGEN_INPUTS_VERIFIED' and d['mechanical_verdict']=='PASS'
    assert sha(a['path'])==a['sha256']
    dispatch.append(dict(call_id=a['call_id'],receipt=receipts[0].relative_to(ROOT).as_posix(),sha256=hashlib.sha256(receipts[0].read_bytes()).hexdigest()))
assert len(manifest['artwork'])==8
for a in manifest['artwork']:
    assert sha(a['path'])==a['sha256']==sha(a['source'])
    with Image.open(ROOT/a['path']) as im: assert im.size==(1254,1254)
for p in ['index.html','case-reader.html','compact-review.html']:
    for target in re.findall(r'(?:href|src)="([^"#]+)"',(ROOT/OUT/p).read_text(encoding='utf-8')):
        if not target.startswith(('http:','https:')): assert (ROOT/OUT/target).is_file(),(p,target)
status=subprocess.check_output(['git','status','--porcelain','--untracked-files=all'],cwd=ROOT,text=True)
for line in status.splitlines(): assert line[3:].replace('\\','/').startswith((PARENT+'/',str(Path(OUT).parent).replace('\\','/')+'/')),line
verification=dict(revision='b13-final-verification-v1',frozen24='24/24_BYTE_IDENTICAL',selected8='1254x1254_NATIVE_BYTES_IDENTICAL',dispatch_receipts=dispatch,counts=post['counts'],relative_asset_reader_links='EXIST',write_scope='OWN_TWO_ROOTS_ONLY',status='PARTIAL_HOLD_CHANGES_REQUIRED',git_head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip(),branch=subprocess.check_output(['git','branch','--show-current'],cwd=ROOT,text=True).strip())
put(BASE+'/verification.json',verification)
put(PARENT+'/ledger.json',dict(revision='fabless-lane-ledger-v1',owner='/root current Fabless session',active_batch='B13-en-f1-v1',status=post['status'],counts=post['counts'],receipt=dict(path=BASE+'/postgen-review.json',sha256=sha(BASE+'/postgen-review.json')),verification=dict(path=BASE+'/verification.json',sha256=sha(BASE+'/verification.json')),remaining_queue='B14-B21 NOT_RUN; stop for Bao',commit=False,merge=False,push=False,live=False))
print(json.dumps({k:verification[k] for k in ['status','frozen24','selected8','counts','write_scope','git_head','branch']},indent=2))
