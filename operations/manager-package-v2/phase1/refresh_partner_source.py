"""One-off bounded refresh for observed Partner source checkpoint a09035d."""
from pathlib import Path
import shutil
P=Path(__file__).resolve().parent
R=P.parents[2]
H=P/'history/phase1-1.1'
H.mkdir(parents=True,exist_ok=True)
for name in ['message-bindings.json','verification.json','source-register.json','data-register.json','Message_Anchor_Review_1.1.md','Data_Register.md','Package_V2_Skeleton_Phase1.md']:
 if not (H/name).exists():shutil.copyfile(P/name,H/name)

def edit(name,old,new):
 p=P/name;s=p.read_text(encoding='utf-8')
 if new in s:return
 assert old in s,(name,old)
 p.write_text(s.replace(old,new),encoding='utf-8',newline='\n')

edit('Data_Register.md','Revision 1.1, 07/10/2026.','Revision 1.2, 07/10/2026. Partner source refresh a09035d; prior record 1.1 giữ riêng trong history/phase1-1.1.')
edit('Data_Register.md','| D28 | FACT | Partner B22–B24: 30 PNG chọn, 43 calls = 30original + 13corrective; final root review trong native/feed333/desktop/actual434 scope, 390 không kiểm. Commit local 4a17968 chứa B23/B24; PO asset acceptance chưa được cấp, chưa creative-main. | Git/manifest/postgen receipts capture 07/10 | SRC-PARTNER-LEDGER, SRC-PARTNER-B22, SRC-PARTNER-B23, SRC-PARTNER-B24 | S4, S7 |','| D28 | FACT | Partner B22–B24 P1: 30 PNG chọn/43 calls (30 original + 13 corrective), checkpoint 4a17968. B25–B26 P2 factory IT/record ownership thêm 20 PNG chọn (12 mới + 8 reuse), 16 calls (12 original + 4 corrective), checkpoint local a09035d. Tổng 50 placements/59 calls; 17 corrective. Source SELF_REVIEW native/feed333/desktop/actual434, exact390 không kiểm; chưa PO asset acceptance/creative-main. Ledger working flags cũ được đối soát bằng Git. | Checkpoints và scoped source receipts 07/10 | SRC-PARTNER-LEDGER, SRC-PARTNER-B22, SRC-PARTNER-B23, SRC-PARTNER-B24, SRC-PARTNER-B25, SRC-PARTNER-B26, SRC-PARTNER-P2-CLOSEOUT | S4, S7 |')
edit('Data_Register.md','| D29 | FACT | Fabless B16–B21 và Partner B25–B30 chưa có execution evidence ở snapshot. Inventory/queue không là lệnh mới cho session này. | Owner source records 07/10 | SRC-FABLESS-LEDGER, SRC-PARTNER-LEDGER, SRC-PROGRESS | S4 |','| D29 | FACT | Fabless B16–B21 còn production/intake tại capture; Partner B25–B26 đã có selected source checkpoint, B27–B30 là phần còn lại. B27/B28 có working preparation, chưa được lấy vào asset register. Inventory/queue không là lệnh generation cho session này. | Owner source records và actual Git tại capture 07/10 | SRC-FABLESS-LEDGER, SRC-PARTNER-LEDGER, SRC-PARTNER-P2-CLOSEOUT, SRC-PROGRESS | S4 |')
edit('Data_Register.md','20 + 120 + 30 + 33 + 30 | 233 selected PNG placements','20 + 120 + 30 + 33 + 50 | 253 selected PNG placements')
edit('Package_V2_Skeleton_Phase1.md','Revision Phase 1: **1.1**','Revision Phase 1: **1.2**')
edit('Package_V2_Skeleton_Phase1.md','Operations Manager của nhà cung ứng công nghiệp như gia công linh kiện chính xác cho thiết bị bán dẫn','Operations Manager (P1) hoặc Factory IT/phụ trách hệ thống và bản ghi (P2) tại nhà cung ứng công nghiệp như gia công linh kiện chính xác cho thiết bị bán dẫn')
edit('Package_V2_Skeleton_Phase1.md','B22–B24: 30 ảnh chọn, root review trong phạm vi đã ghi; checkpoint local 4a17968.','B22–B24 P1: 30 ảnh chọn, checkpoint 4a17968; B25–B26 P2 thêm 20 ảnh chọn, checkpoint local a09035d. Root SELF_REVIEW trong native/feed333/desktop/actual434 scope, exact390 giữ riêng.')
edit('Package_V2_Skeleton_Phase1.md','Partner B25–B30 và các reader conditional','Partner B27–B30 và các reader conditional')
edit('Inventory_Disposition.md','Manifest23groups/233PNGplacements','Manifest25groups/253PNGplacements')
edit('Inventory_Disposition.md','B22–B24 postcheck source checkpoint4a17968; PO assets pending; B25–B30 còn lại.','B22–B24 P1 checkpoint4a17968; B25–B26 P2 factory IT checkpointa09035d; 50sourceplacements, PO assets pending; B27–B30 còn lại.')
edit('README.md','23 selection groups/233 PNG placements','25 selection groups/253 PNG placements')
edit('README.md','con số 233','con số 253')
edit('README.md','[message anchor review 1.1](Message_Anchor_Review_1.1.md)','[message anchor review 1.2](Message_Anchor_Review_1.2.md)')
edit('Reconciliation_Notes.md','Revision1.1, 07/10/2026.','Revision 1.2, 07/10/2026. Partner B25/B26 source checkpoint a09035d được refresh ở lượt kiểm cuối; budget/workflow decision vẫn revision 1.1.')
edit('Reconciliation_Notes.md','30selected/43calls; scopedrootreviewcomplete; committedlocal, chưaPOassetacceptance/creativemain. Ledgerflags/historicaltext khôngthayactualGit.','B22–B24 giữ 30 selected/43 calls tại 4a17968; B25–B26 thêm 20 selected/16 calls, đã có local a09035d. Tổng 50 placements/59 calls; source SELF_REVIEW scope, chưa PO asset acceptance/creative-main. Ledger flags/historical working text không thay actual Git.')
notice='> **Partner source refresh 07/10:** B25 English và B26 giản thể P2 factory IT/record ownership đã có checkpoint local `a09035d`, thêm 20 selected placements (12 mới + 8 reuse). B22–B24 P1 vẫn 30 placements tại `4a17968`; tổng Partner 50 placements/59 calls. Scoped source SELF_REVIEW không là PO asset acceptance hoặc main adoption. B27–B30 giữ production/intake riêng. Source report/ledger working-file text được đối soát với actual Git.'
p=R/'operations/LinkedIn_Current_Progress_2026-10-07.md'
s=p.read_text(encoding='utf-8')
if notice not in s:p.write_text(notice+'\n\n'+s,encoding='utf-8',newline='\n')
print('Partner source checkpoint refreshed; previous 1.1 receipt preserved.')
