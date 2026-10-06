"""Bounded offline adoption from an immutable owned checkpoint; no generation/live action."""
from pathlib import Path
import hashlib,json,subprocess,re
ROOT=Path(__file__).resolve().parents[4]
SRC=Path('D:/LinkedIn_VN_Journey_Rebuild_2026-10-06')
B='operations/linkedin-vn-journey-rebuild/2026-10-06'
HERE=ROOT/B/'week2-main-integration'
SOURCE='717a63a034cb149130d0e99fe14934d989a6c3ec'
BASE='89d94be6abb839f8834d1b62d9c715296fcd5d4c'
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def pin(p):return {'path':p.relative_to(ROOT).as_posix(),'sha256':sha(p)}
def save(p,v):p.write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode())
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=SRC,text=True).strip()==SOURCE
assert not subprocess.check_output(['git','status','--porcelain'],cwd=SRC)
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT,text=True).strip()==BASE
selected=read(SRC/B/'week2-r2-metric-v1/selected-manifest.json')
files=set()
demo='deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2'
files.update([demo+'/index.html',demo+'/case-aplus.html'])
for s in selected['selected']:
 for k in ('native','demo_asset'):files.add(s[k]['path'])
# Parent R2 native is needed to inspect the immutable historical review; not active selection.
files.add(B+'/week2-timegen-v2/native/vn-b-t-r2-v2.png')
for d,names in {
 'week2-r2-metric-v1':['PLAN.md','full-journey-copy.json','public-copy.json','selected-manifest.json','postgen-review.json','postgen-observed-text.json','postgen-address-scan.json','render-observations.json','verification.json','generation-ledger.json','VN-B-T-R2-V3-immediate-guard.json','spec.json','message-review.json','vn-voice-pregen.json','script-review-detail.json','contract.json','review.json','release.json','authority.md','dispatch-pins.json','case-script.json'],
 'week2-time-final':['public-copy.json','selected-manifest.json','postgen-review.json','postgen-observed-text.json','postgen-address-scan.json','render-observations.json','verification.json','generation-ledger.json','case-copy-pregen-review.json','case-script.json'],
 'week2-timeproof-v1':['SOURCE_PROOF.md','STORYBOARD.md'],
 'week2-main-integration':['PLAN.md','PO_Acceptance.json']}.items():
 files.update(B+'/'+d+'/'+n for n in names)
for d in ('week2-time-final','week2-r2-metric-v1'):
 files.update(p.relative_to(SRC).as_posix() for p in (SRC/B/d/'render').glob('*.png'))
records=[]
for name in sorted(files):
 src=SRC/name;dest=ROOT/name;blob=subprocess.check_output(['git','show',SOURCE+':'+name],cwd=SRC)
 assert src.read_bytes()==blob,name
 assert not dest.exists(),name
 dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(blob);records.append(pin(dest))
bindings=[]
for name in ('operations/Vy_Email_Content_Anchor.md','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md','operations/VN_Locale_Reader_Voice_Gate.md'):
 assert (ROOT/name).read_text(encoding='utf-8-sig')==(SRC/name).read_text(encoding='utf-8-sig'),name
 bindings.append({'main':pin(ROOT/name),'source_sha256':sha(SRC/name),'comparison':'Exact normalized text equal; raw line endings may differ. Fresh main binding, no inherited byte-pin PASS.'})
save(HERE/'selection.json',{'status':'PO_ACCEPTED_OFFLINE_WEEK2_V2 / LOCAL_MAIN_ADOPTION','source_checkpoint':SOURCE,'base_main':BASE,'PO_acceptance':pin(HERE/'PO_Acceptance.json'),'active_demo':pin(ROOT/demo/'index.html'),'case':pin(ROOT/demo/'case-aplus.html'),'active_selected':[{'card_id':s['card_id'],'asset':s['demo_asset'],'size':s['size']} for s in selected['selected']],'artifacts':records,'main_anchor_bindings':bindings,
 'history_policy':'Original reviews/inputs/PO_PENDING/local-only states are snapshots at creation. Later PO acceptance and main adoption recorded here; not retroactive PASS. Old WONIK/trials remain source branch only.',
 'generation_dependency_scope':'Original spec/guard/contracts are archival evidence. Executable guards/preflight snapshots/builders and full transitive historical dependency tree not imported or activated. Source checkpoint preserves complete evidence; main does not claim runnable regeneration/preflight.',
 'exclusions':['Old WONIK/initial alternatives','Research history beyond scoped proof','Unselected initial R1 correction','Generation scripts/guards/runtime','Account/audience/package/adapter state changes'],
 'review':'Root SELF_REVIEW from exact native and actual prior screenshots, one changed R2 actual desktop/mobile review; no independent audit claimed','live':'Offline PO acceptance only; no launch/upload/spend or freeze/remote push'})
mainreview={'stage':'POSTGEN_MAIN_ADOPTION','reviewer':'/root','independence':'SELF_REVIEW','anchor_id':'VY-CONTENT-ANCHOR','anchor_revision':'1.0','scope':{'segment':'VN_DOMESTIC','locale':'vi-VN','persona':'domestic supplier owner / operations director'},'bindings':bindings,'selection':pin(HERE/'selection.json'),'verdict':'MESSAGE_ANCHOR_PASS_SELF_REVIEW / PO_ACCEPTED_OFFLINE',
 'actual_artifact_scope':'Current10selected rasters byte-equal to source originals inspected;9prior actual desktop/mobile views plus changed R2 native/desktop/mobile and identical case. No new browser22-view claim on main.',
 'units':[{'card_id':s['card_id'],'asset':s['demo_asset'],'verdict':'MATCH_SELF_REVIEW','observation': 'R2 introduces Aplus China integrated iMES+TOPGP and actual whole-project3month go-live; no deadline guarantee.' if s['card_id']=='VN-B-T-R2' else 'Same exact selected bytes and reviewed audience/product/source scope from scoped original review.'} for s in selected['selected']],
 'surfaces':['Independent Cold/RMK/Evidence captions','Each raster headline/body/category/source/CTA','Native display headline/alt','Full journey transitions','VN Aplus case/destination'],
 'A1':'Semiconductor supply-chain supplier readiness, not general manufacturing or assumed fab','A2':'Actual reader/customer fit unproven; no account assertion','A3':'VN domestic owner/operations, source China does not imply FDI','A4':'FDI ROI framing N/A, no invented ROI','A5':'Operational preparation; no audit/order/deadline promise','A6':'Named integrated iMES+TOPGP mechanisms; no ERP-only SPC/serial attribution','A7':'Cold readiness -> identify data/scope -> integrated serial/SPC/parameters -> Aplus go-live timing/outputs -> discuss suitable roadmap',
 'V1_V5_AD_ED':'Advertiser/we caption, natural complete VN voice, exact Quý Doanh Nghiệp; no Bạn; case/source/metric bounded. Actual selected accents read in native/screens. No third-party voice or unsupported guarantee.',
 'limitations':['Main binding distinguishes LF/CRLF from content change','Secondary category/source small mobile','Generic illustration, not Aplus facility photo','End-to-end consultation-to-audit duration/audit success unknown','Self-review only; no independent audit'], 'generation':'No generation/release/runtime adoption','live':'No operational readiness assertion'}
save(HERE/'Main_Message_Review.json',mainreview)
prefix='''> **VN week2-v2 · Bảo accepted offline / main local adoption · 2026-10-06:** Bộ10ảnh dự phòng VN gồm Cold B +5RMK +4evidence đã duyệt; RMK2/5 thêm “Toàn dự án đi vào vận hành trong 3 tháng.” tại phần Aplus Trung Quốc/iMES + TOP GP. [Demo current](DELIVERABLE_LINK) · [Selection/provenance](RECEIPT_LINK). Source checkpoint717a63a; fresh main anchor binding và actual source SELF_REVIEW/native/render evidence, không independent audit hoặc live readiness. Claim3tháng là go-live toàn dự án tích hợp trong case, không tư vấn→audit/deadline guarantee. Source/category nhỏ mobile là limitation. Week1v3 giữ baseline; WONIK/trials không current. Budget/package/audience/live và locale artifacts hiện có giữ nguyên; adapter DEVELOPING / NOT_FROZEN, không import/activate runtime guards hoặc push. Earlier source/local-only/PO_PENDING notes remain historical snapshots.

'''
docs=['README.md','CURRENT_STATE.md','DOCS_IMPACT_MAP.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/LinkedIn_Awareness_Execution_Plan.md','operations/Pre_Ad_Readiness_Plan.md',B+'/README.md']
for name in docs:
 p=ROOT/name;depth=len(Path(name).parts)-1
 link='../'*depth+demo+'/index.html';receipt='../'*depth+B+'/week2-main-integration/README.md'
 t=prefix.replace('DELIVERABLE_LINK',link).replace('RECEIPT_LINK',receipt)
 if name=='DOCS_IMPACT_MAP.md':t='> **Docs impact reviewed · approved VN week2-v2 local integration:** Reviewed7canonical/owned entrypoints on actual current main; prepended scope/selection/acceptance links while preserving concurrent FDI/account/package body. Original raw evidence preserved. New main anchor binding accounts for newline-only difference. No frozen core/generation runtime/live/budget/adapter adoption.\n\n'+t
 p.write_bytes(t.encode()+p.read_bytes())
HERE.joinpath('README.md').write_text('''# VN week2-v2 — approved offline main selection

Bảo approved commit and merge current week2-v2 artifacts on2026-10-06. Current [10-image demo](../../../../deliverables/linkedin-vn-journey/2026-10-06-week2-time-v2/index.html); RMK2/5 includes bold-blue **Toàn dự án đi vào vận hành trong 3 tháng.** after explicit Aplus China/iMES + TOP GP scope. Whole integrated-project go-live result; no ERP-only timeline, consultation-to-audit duration, audit success or reader deadline promise.

[Selection/provenance](selection.json), [PO acceptance](PO_Acceptance.json), [fresh main anchor review](Main_Message_Review.json), [integration verification](verification.json). Source checkpoint717a63a preserves full generation/history; selected originals and relevant actual screenshots/receipts adopted byte-for-byte. Existing main FDI/account/package state preserved. Older PO_PENDING/local-only receipts describe actual earlier snapshot; current acceptance/adoption is this separate event. Root SELF_REVIEW, no independent audit claimed.

Main contains the complete offline demo plus copy/proof/review evidence. Archival spec/guard files do not establish runnable regeneration: executable scripts and full transitive source dependencies remain on source branch. No generation/release/core or adapter freeze, account/upload/publish/spend or GitHub push. Week1v3 retained; old WONIK and initial alternatives stay historical on source branch. Secondary category/source small mobile, images generic illustrations. Docs impact reviewed:7entrypoints updated current scoped truth without rewriting historical inputs.
''',encoding='utf-8')
print(len(records),'source artifacts copied exactly; main scoped docs/binding prepared.')
