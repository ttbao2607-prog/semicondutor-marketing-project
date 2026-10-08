"""Bounded documentation update from Bao's dashboard/weekly-review decision."""
from pathlib import Path
import shutil
P=Path(__file__).resolve().parent
R=P.parents[2]
H=P/'history'/'phase1-1.0'
H.mkdir(parents=True,exist_ok=True)
for name in ['Message_Anchor_Review.md','message-bindings.json','verification.json','source-register.json','data-register.json','Data_Register.md','Reconciliation_Notes.md','Package_V2_Skeleton_Phase1.md']:
 if not (H/name).exists():shutil.copyfile(P/name,H/name)

def replace(rel,old,new):
 p=R/rel; s=p.read_text(encoding='utf-8')
 if new in s:pass
 elif old in s:s=s.replace(old,new)
 else:raise ValueError(f'Missing expected text: {rel}: {old[:80]}')
 p.write_text(s,encoding='utf-8',newline='\n')
def prepend(rel,text):
 p=R/rel;s=p.read_text(encoding='utf-8')
 if text not in s:p.write_text(text+'\n\n'+s,encoding='utf-8',newline='\n')

base='operations/manager-package-v2/phase1/'
replace(base+'Data_Register.md','Revision 1.0, 07/10/2026.','Revision 1.1, 07/10/2026. Ngân sách/dashboard/cadence theo SRC-PO-WEEKLY; receipt/source snapshot 1.0 giữ trong history/phase1-1.0.')
replace(base+'Data_Register.md','Anchor workflow 1.0, 07/10','Anchor workflow 1.1, 07/10')
replace(base+'Data_Register.md','| D08 | DECISION | 11.700.000 VND, trần media hiện hành; thay 35.000.000 VND. Không phải all-in hoặc actual spend. | PO 06/10 | SRC-BUDGET | S1, S5 |','| D08 | DECISION | 11.700.000 VND, trần media hiện hành, ghi rõ chưa thuế; thay35.000.000VND. Bảo quản lý số tiền ads trên dashboard, không ghi như actual đã chi. | PO06/10 + clarification07/10 | SRC-BUDGET, SRC-PO-WEEKLY | S1, S5 |')
replace(base+'Data_Register.md','| D15 | PENDING | Thuế/phí, FX, khoản ngoài media và tổng all-in: chưa có giá trị xác nhận. Không dùng phần trăm đệm mặc định. | Đầu vào Finance/billing chưa pin | SRC-BUDGET, SRC-LEGACY-BUDGET | S5, S10 |','| D15 | DECISION | Package ghi ngân sách chưa thuế; kế toán/pipeline riêng của công ty tính thuế và xử lý thanh toán. Marketer quản lý/coordinate các số tiền thao tác trên dashboard, giữ đúng đơn vị/currency. Tổng all-in không là đầu vào phải chờ để chốt package; không tự thêmthuế/FX/đệm. | Chỉ đạoBảo07/10, record1.0 | SRC-PO-WEEKLY | S5, S7, S10 |')
replace(base+'Data_Register.md','mỗi bộ 11 PNG chọn ở working files.','mỗi bộ 11 PNG chọn, đã có checkpoint local461a752, chưa creative-main.')
replace(base+'Data_Register.md','| D36 | ASSUMPTION | Weekly review; quyết định dùng tiếp phần giữ lại theo mapping/relevance/delivery/attention/chi phí và RMK eligibility. Thiếu mẫu thì giữ chưa kết luận; không mở ICP/keywords chỉ để tiêu tiền. Cadence/stop values do Bảo chốt trước chạy. | Evidence principle còn phù hợp, chưa chọn schedule/threshold | SRC-S04, SRC-MAIL, SRC-LEGACY-BUDGET | S6, S7, S8 |','| D36 | DECISION | Tuần1 chạy đúng plan, review cuối tuần; tuần2 Bảo quyết định theo data matrix. Có VNweek1/week2 để ghép đúng đoạn, nhiều assetFDI để swap và audience chính/backup. Hành động linh hoạt theo nguyên nhân/tín hiệu, giữ anchor/locale/persona và cap; không tự thêm tranche hoặc threshold. | Chỉ đạoBảo07/10, matrix nội bộ1.0 | SRC-PO-WEEKLY, SRC-WEEK2-MATRIX, SRC-S04 | S1, S4, S5, S6, S7, S8 |')

sk=base+'Package_V2_Skeleton_Phase1.md'
replace(sk,'Trần media hiện hành: **11,7 triệu đồng**.','Trần media hiện hành: **11,7 triệu đồng, chưa thuế**. Revision Phase1:1.1 theo chỉ đạo Bảo về dashboard và review tuần.')
replace(sk,'giữ 6,1 triệu để quyết định đợt tiếp theo và thử Search khi có căn cứ.','giữ 6,1 triệu để quyết định đợt tiếp theo và thử Search khi có căn cứ. Tuần đầu chạy đúng plan; cuối tuần review dữ liệu để Bảo chọn hướng tuần2. Bảo theo dõi tiền ads trên dashboard; kế toán xử lý thuế/thanh toán theo pipeline của công ty.')
replace(sk,'B13 checkpoint local; B14/B15 working files.','B13 checkpoint local; B14/B15 checkpoint local461a752, còn riêng với main.')
replace(sk,'Các original/fail/corrective attempts chỉ lưu ở hồ sơ sản xuất.','Các original/fail/corrective attempts chỉ lưu ở hồ sơ sản xuất. VNweek1/week2 và thư viện FDI là nguồn thay/ghép linh hoạt sau review: đoạn nào yếu thì chọn asset phù hợp thay đoạn đó, giữ phần đang hiệu quả. Mỗi tổ hợp giữ cùng persona/locale/message và kiểm lại transition bị ảnh hưởng.')
replace(sk,'| Tổng trần media | **11.700.000 đồng** |','| Tổng trần media, chưa thuế | **11.700.000 đồng** |')
replace(sk,'Thuế/phí theo billing và khoản ngoài media cần dữ liệu Finance để nêu tổng all-in; hồ sơ hiện tại không có tỷ lệ xác nhận.','Package ghi ngân sách **chưa thuế**. Bảo quản lý/coordinate số tiền trên dashboard; kế toán và pipeline riêng của công ty tính thuế/xử lý thanh toán. Bản trình không chờ tổng all-in hoặc thêm tỷ lệ đệm. Tuần1 chạy theo plan, review cuối tuần; tuần2 điều chỉnh theo data matrix trong trần hiện hành. Mốc review này không tự chia lại5,6triệu hoặc cấp thêm ngân sách cho tuần2.')
replace(sk,'Weekly review là phương án làm việc để phản hồi sớm; thời gian không thay lượng và chất lượng evidence.','Cadence đã chốt: **tuần1 chạy đúng plan → review cuối tuần → tuần2 Bảo quyết định theo data matrix**. Matrix đọc độ tin cậy đo, đúng tệp, delivery/attention, đoạn explanation/proof/reader và số tiền dashboard. Nếu phát hiện vấn đề, sửa/swap đúng đoạn; audience có tệp chính và backup với evidence riêng. Mẫu mỏng được ghi rõ trước kết luận. [Matrix nội bộ](Week1_Review_Week2_Data_Matrix.md) cụ thể hóa cách đọc, không dựng engine tự động.')
replace(sk,'mức media và tổng chi có căn cứ; logic chi theo đợt/phần giữ lại;','mức media chưa thuế; logic chi theo đợt/phần giữ lại và review tuần1→tuần2;')
replace(sk,'Các đầu vào chưa có số hoặc chưa chọn được giữ trong [Reconciliation Notes](Reconciliation_Notes.md): all-in/thuế phí; nhóm chạy/lịch và điều kiện dùng phần giữ lại; reader revision; baseline/numeric thresholds.','Bảo đã chốt [budget/dashboard và nhịp review](PO_Dashboard_Weekly_Decision_2026-10-07.md): ngân sách chưa thuế, kế toán xử lý thuế, tuần1 chạy đúng plan, review cuối tuần và tuần2 theo data matrix. Phần ghép/swap VN/FDI và audience chính/backup nằm trong quyền Bảo. [Reconciliation Notes](Reconciliation_Notes.md) giữ reader revision, metric/ngưỡng và account readback như đầu vào execution nội bộ; không chuyển thành một vòng hỏi sếp.')
replace(sk,'Data: D08–D16, D33. Calc:','Data: D08–D16, D33, D36. Calc:')

rn=base+'Reconciliation_Notes.md'
replace(rn,'Revision 1.0, 07/10/2026.','Revision1.1, 07/10/2026. Quyết định dashboard/weekly của Bảo đã được áp dụng; prior snapshot1.0 giữ trong history/phase1-1.0.')
replace(rn,'Full mobile/whole-journey acceptance pending; B16–B21 chưa execution evidence.','Full mobile/whole-journey acceptance pending; B14/B15 nay checkpoint local461a752, supersedes working-file text. B16–B21 chưa execution evidence.')
replace(rn,'## Các đầu vào chưa chốt — nội bộ của Bảo','## Quyết định đã chốt và đầu vào execution nội bộ')
replace(rn,'| OPEN-01 | Thuế/phí/FX và tổng all-in ảnh hưởng con số trình đầu tư. | Dùng11,7mmedia; giữall-inpending, bổ sungFinance/billingthựctế, không%đệm. | Bảo/Finance trước bộ budget final. |','| OPEN-01 — CLOSED_BY_PO | Cách ghi ngân sách và quyền theo dõi tiền. | Ghi11,7triệu media chưa thuế; Bảo quản lý/coordinate số tiền dashboard; kế toán/pipeline công ty tự tính thuế và xử lý thanh toán. Không chờ tổng all-in để chốt package. | SRC-PO-WEEKLY; kế toán giữ phần thuế. |')
replace(rn,'| OPEN-02 | Nhóm đầu, lịch/daily và điều kiện dùng6,1mheld ảnh hưởngpacing/delivery. | D09–D14 làreference; chọnítmẫumộtgroup phùhợp mapping/reach; khôngchiađều4locale hoặcnhânbudgettheobatch. | Bảo trước triển khai; logic draft đượcchốt trướcPhase2. |','| OPEN-02 — CADENCE_CLOSED_BY_PO | Nhịp chạy/review và quyền quyết định tuần2. | Tuần1 chạy đúng plan, review cuối tuần, tuần2 theo data matrix. Bảo có VNweek1/week2, assetFDI và audience chính/backup để sửa/swap đúng đoạn. Daily/group cụ thể giữ trong execution; không thêm tranche mặc định hoặc nhânbudgettheobatch. | SRC-PO-WEEKLY; Bảo quyết định vận hành. |')
replace(rn,'| OPEN-04 | Baseline/numericKPI/stop và sourceRMK ảnh hưởngcáchđọcđợtđầu. | Scorecarddefinitions/cadenceproposalđãcó; dùngactualđúngscope; khôngoldthresholds/forecast. | Bảo trước chạy; measurementlogic chốt trướcPhase2. |','| OPEN-04 — EXECUTION_INPUT | Dữ liệu/metric/ngưỡng và sourceRMK cụ thể. | Logic review đã chốt theo data matrix. Baseline/coverage, numeric thresholds và exact cohort IDs/rule/eligibility do Bảo xử lý bằng dữ liệu thực; không hỏi sếp từngsetting. | Bảo/operator trước hành động tương ứng. |')
replace(rn,'OPEN-01–04 vẫn là input phải chốt hoặc được Bảo chấp nhận như assumption trước Phase2.','OPEN-01 về thuế đã đóng; cadence/quyền tuần2 ở OPEN-02 đã chốt. Reader revision và metric/readback cụ thể giữ là execution inputs của Bảo, không phải câu hỏi budget cho sếp. Không tự suy Bảo đã chốt toàn bộ skeleton hoặc bắt đầuPhase2.')
replace(rn,'Những trạng thái adoption/runtime/budget hiện hành không đổi.','Budget presentation/cadence mới của Bảo được sync vào current-state, S04, readiness/build và budget/RMK entrypoints trong checkout riêng; cap và actual adoption/runtime không đổi.')

iv=base+'Inventory_Disposition.md'
replace(iv,'Cap11,7m;5,6+5,6+0,5ref; all-in và allocation chờ Bảo.','Cap11,7m chưa thuế;5,6+5,6+0,5ref; dashboard do Bảo theo dõi, thuế do kế toán/pipeline công ty tính; không chờ all-in.')
replace(iv,'Evidence-first review/reallocation principles; chưa numericstop/cadencefinal.','Tuần1 chạy đúng plan/review cuối tuần, tuần2 theo data matrix đã chốt; ghép/swap đúng đoạn VN/FDI và audience chính/backup; numeric values giữ executioninput.')

wf='operations/manager-package-v2/Package_V2_Workflow_Anchor_2026-10-07.md'
replace(wf,'revision1.0 · 07/10/2026.','revision1.1 · 07/10/2026.')
prepend(wf,'> **Bảo clarification07/10 — revision1.1:** Package ghi11,7triệu media chưa thuế; Bảo theo dõi/coordinate tiền dashboard, kế toán/pipeline công ty xử lý thuế. Tuần1 chạy đúng plan, review cuối tuần; tuần2 theo data matrix, ghép/swap đúng đoạn bằng VNweek1/week2, assetFDI và audience chính/backup. [Decision record](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md). Workflow3phase và quyền Bảo giữ nguyên; không mở thêm câu hỏi thuế/kỹ thuật cho sếp.')
shared_notice='> **PO package v2 clarification07/10 — current in owned checkout:** Ngân sách media11,7triệu **chưa thuế**; Bảo quản lý/coordinate số tiền ads trên dashboard, kế toán/pipeline riêng của công ty tính thuế và xử lý thanh toán. **Tuần1 chạy đúng plan → review cuối tuần → tuần2 Bảo quyết định theo data matrix**, linh hoạt ghép/swap đoạn VNweek1/week2 hoặc assetFDI và chọn audience chính/backup theo evidence. Review tuần không tự cấp tranche/budget mới; cap/route/frozen gates và acceptance riêng giữ nguyên. '
for rel,link in [
 ('CURRENT_STATE.md','operations/manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('operations/LinkedIn_Current_Progress_2026-10-07.md','manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('operations/LinkedIn_PO_Direction_Budget_Checkpoint_2026-10-06.md','manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('drafts/S04_Measurement_and_Budget.md','../operations/manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('operations/Pre_Ad_Readiness_Plan.md','manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('ads/linkedin/LinkedIn_Build_Pack.md','../../operations/manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md'),
 ('operations/LinkedIn_Cold_To_RMK_Data_Plan_2026-10-05.md','manager-package-v2/phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md')]:prepend(rel,shared_notice+'[Decision record]('+link+'). Main/sourceworktrees khác không được sửa; đây là docs working files, chưa commit/mainmerge/push/live. Nội dung cũ dưới giữ phạm vi lịch sử nơi đã bị thay thế.')
prepend('operations/LinkedIn_Current_Progress_2026-10-07.md','> **Fabless source checkpoint refresh07/10:** B14/B15 hiện đã commit local `461a752`, supersedes working-file state của snapshot Phase1 trước. 22selectedPNG và rendered limitations giữ nguyên; chưa creative-main hoặc operational acceptance. Input/source pins mới ghi actualGit.')
prepend('operations/manager-package-v2/README.md','> **PO steering applied — Phase1 revision1.1:** Đã chốt ngân sách chưa thuế/dashboard owner và tuần1→review→tuần2 data matrix. Thuế không còn input phải chờ trong package; asset/audience swaps thuộc Bảo. [Decision](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md), [matrix nội bộ](phase1/Week1_Review_Week2_Data_Matrix.md). Các output mới vẫn working files local; Phase2/3 chưa bắt đầu.')
prepend('operations/manager-package-v2/Package_V2_Three_Phase_Plan_2026-10-07.md','> **Phase1 update07/10:** Budget được ghi chưa thuế; dashboard do Bảo quản lý/coordinate, kế toán xử lý thuế. Tuần1 theo plan/review cuối tuần, tuần2 quyết định theo data matrix và swap đúng đoạn từ nguồn đã chuẩn bị. [Decision record](phase1/PO_Dashboard_Weekly_Decision_2026-10-07.md) thay all-in/cadence pending; không tự bắt đầuPhase2/3.')
replace(base+'README.md','Bốn nhóm input nội bộ được ghi ở OPEN-01–04; không phải bộ câu hỏi gửi sếp.','OPEN-01 thuế đã đóng, OPEN-02 cadence/quyền tuần2 đã chốt theo [quyết định Bảo](PO_Dashboard_Weekly_Decision_2026-10-07.md). [Data matrix tuần2](Week1_Review_Week2_Data_Matrix.md) giữ action logic nội bộ; reader/metric/readback cụ thể là execution inputs, không loạt câu hỏi gửi sếp.')
replace(base+'README.md','84 source/file pins tại capture;','Source/file pins tại capture ghi trong audit cuối;')
print('PO clarification applied; earlier Phase1 receipt/bindings preserved in history/phase1-1.0.')
