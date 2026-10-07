# Phase 1 — Đối soát và đầu vào Bảo chốt

Revision 1.2, 07/10/2026. Partner B25/B26 source checkpoint a09035d được refresh ở lượt kiểm cuối; budget/workflow decision vẫn revision 1.1. Quyết định dashboard/weekly của Bảo đã được áp dụng; prior snapshot1.0 giữ trong history/phase1-1.0. [git-state.json](git-state.json) ghi checkout/commit/working files; [source-register.json](source-register.json) ghi exact byte hashes và source scope. Trạng thái account là observation có ngày của source, không readback mới. Plan đã checkpoint local `7796bc6`; Phase 1 là file làm việc trên nhánh riêng, chưa checkpoint mới/main merge/push.

## Contradictions đã giải theo nguồn

| Nguồn cũ / finding | Bằng chứng đối chiếu | Disposition dùng cho v2 |
|---|---|---|
| Cleanup/audience còn OPEN chung; 780 là quy mô hiện hành | SRC-COMPANY:424research completed/submit1lần; readback Updating; repaired mapping/reach pending | Research closed; processing/readback còn lại. Không restart, reupload hoặc dùng old780 forecast. |
| Backup và tệp công ty gốc là một nhánh | SRC-COMPANY vs SRC-BACKUP/R5upload | Hai dòng độc lập; backup52 không đóng Discovery424. |
| Summary R5 Ready/>90% nhưng Details0 | SRC-BACKUP exact observations | Mapping chưa kiểm được; không coi0 là sốcompanythật hoặc>90% làcustomer-fit. Unsaved estimates giữscope. |
| S04/mail/lịch cũ35m/43,75m, coldCarousel,8weeks hoặc7→21→4weeks | SRC-BUDGET + SRC-PROGRESS superseding notices | Cap11,7m +Single image route. Historical cadence khôngtựchuyểnthànhlịchv2. |
| VN đang sai hướng/chưa rebuild | Main VNcloseout/currenttwojourneys/readers | Revisionpivotcũhistorical; currentVNcreativeclosed/offlineadopted, dùngreadinessbridge. |
| OSAT chỉ70ảnh hoặc cònbatchgent | 12B1–B12manifest +3O3pilotsmain | B1–B12=120placements; B6–B12subset70; O3pilotsriêng30. KhôngnewOSATquota. |
| Fabless ledger cũ B14–B21 NOT_RUN; main snapshot B15 chưa PNG | Working attempts/selected manifests và postgen B14/B15 mới. Ledger của owner được cập nhật ngay trong lượt Phase1, audit phát hiện hash đổi và đã đọc lại. | B14v1/B15v2 mỗi bộ 11 selected; 13/12 attempts; native corrections closed, feed333/main640 và desktop reader SELF_REVIEW. Full mobile/whole-journey acceptance pending; B14/B15 nay checkpoint local461a752, supersedes working-file text. B16–B21 chưa execution evidence. Refresh source pins, không sửa owner ledger. |
| PartnerB23/B24postgenNOT_RUN; ledger/closeoutnóiworkingfiles | Finalreviews +Git4a17968 chứaB23/B24 | B22–B24 giữ 30 selected/43 calls tại 4a17968; B25–B26 thêm 20 selected/16 calls, đã có local a09035d. Tổng 50 placements/59 calls; source SELF_REVIEW scope, chưa PO asset acceptance/creative-main. Ledger flags/historical working text không thay actual Git. |
| FDIreaderNOT_IMPLEMENTED hoặc25HTMLphảidựng | SRC-READERS-INVENTORY/currenttopnotice +10source/mainhashcomparisons |10concretefour-togglecheckpointsource-only.25rowsconditionalcoverage, khôngquota. |
| Toàn bộtrackingchưalàm hoặcpriorQAđóngmọiroutemới | SRC-TRACKING/S04priorproductionevidence | Existing3routepriorPASSWITHSCOPEEXCLUSION; readernew/campaignattribution cầnscopekhác. |
| Proofpublicphảiđềuunknown; hoặcmọicaseđượcduyệttoànphần | SRC-RIGHTS29/09 +02/10revalidation +Partneranchor | ExistingVIuse/translationapprovalexactscopegiữnguyên. Broadernumericclaims/customerlogo/newphoto/publicpaiduse đốichiếuriêng; khôngwithdrawapprovalvôcăn cứ. |
| Workbook11sheetđãbổsung vs packageworkbook6sheet | Anchor dẫn revisionhistorical11sheet; exactSRC-LEGACY-WORKBOOKfileXML có6sheet/29formulas | Hai revision/outputs khácnhau; khôngkếtluậnworkbookthiếuhoặcchọn6/11làmrequirementv2. |
| 22questions/engine/versionboundanswers phải giữ | SRC-WORKFLOW mới | Khôngcarrydefault/answers. Phase2 mớisoạn3–4nội dung đầu tư; giữ integrityrecordsngoàipackage. |

## Quyết định đã chốt và đầu vào execution nội bộ

| ID | Input / business impact | Phương án làm việc hiện tại | Owner / lúc cần |
|---|---|---|---|
| OPEN-01 — CLOSED_BY_PO | Cách ghi ngân sách và quyền theo dõi tiền. | Ghi11,7triệu media chưa thuế; Bảo quản lý/coordinate số tiền dashboard; kế toán/pipeline công ty tự tính thuế và xử lý thanh toán. Không chờ tổng all-in để chốt package. | SRC-PO-WEEKLY; kế toán giữ phần thuế. |
| OPEN-02 — CADENCE_CLOSED_BY_PO | Nhịp chạy/review và quyền quyết định tuần2. | Tuần1 chạy đúng plan, review cuối tuần, tuần2 theo data matrix. Bảo có VNweek1/week2, assetFDI và audience chính/backup để sửa/swap đúng đoạn. Daily/group cụ thể giữ trong execution; không thêm tranche mặc định hoặc nhânbudgettheobatch. | SRC-PO-WEEKLY; Bảo quyết định vận hành. |
| OPEN-03 | Reader revision ảnh hưởngdemo/locale/return/dependencies và measurement. | Mainselected làbaseline;10redesignsourceđãduyệtoffline cópins nhưngchưaadopt. Giữrõhai revision tớiBảochọn. | Bảo/destinationowner trước final library/exports. |
| OPEN-04 — EXECUTION_INPUT | Dữ liệu/metric/ngưỡng và sourceRMK cụ thể. | Logic review đã chốt theo data matrix. Baseline/coverage, numeric thresholds và exact cohort IDs/rule/eligibility do Bảo xử lý bằng dữ liệu thực; không hỏi sếp từngsetting. | Bảo/operator trước hành động tương ứng. |

Các dependencies vận hành khác — mapping/R5Details, exact cohort IDs/rule/window, Fabless render, Partner PO asset approval, final reader entry/tracking, new proof/ảnh rights — nằm ở S7 và registers. Không đẩy thành loạt câu hỏi xin sếp duyệt. Không gửi support, re-upload, genảnh hoặc bật campaign trongPhase1.

## Change register v1 → v2 ở bước data

Giữ: currentmedia cap, Singleimage→new-adRMKroute, táchVN/FDI, proofexactscope và layeredmeasurement. Refresh: haiaudienceluồng; currentcreative/source/mainadoption; readerrevisions; existingtrackingscope. Bỏlàmdefault:22questions/engine/answers, oldbudgets/schedules/cleanedreachforecast, VNtrial/SIpersonaPartner, sốsheet/formula/quotalayoutcũ. Bổsung: sourcedata/assetclaimregisters,34dispositions vàworkflowBảodata→split→polish.

## Documentation impact

Đã đọc CURRENT_STATE, DOCS_IMPACT_MAP và canonical progress/budget/kickoff/S01/S04/readiness/tracking/RMK/search/publicsources. Cập nhật scoped current-progress notice trong checkout package để chỉ rõ Fabless/Partner source advancements; thêm trạng thái package Phase1 ở CURRENT_STATE và owned README. Main worktree và sourceworktrees chỉ đọc; không sửa owner ledgers, frozen files, history/receipts hoặc assetbytes. Budget presentation/cadence mới của Bảo được sync vào current-state, S04, readiness/build và budget/RMK entrypoints trong checkout riêng; cap và actual adoption/runtime không đổi. Main chưa nhận các docs/file Phase1 này.

Trạng thái **PHASE1_PREPARED / BAO_DATA_LOCK_PENDING**: data/skeleton/registers và kiểm bounded đã thực hiện; OPEN-01 về thuế đã đóng; cadence/quyền tuần2 ở OPEN-02 đã chốt. Reader revision và metric/readback cụ thể giữ là execution inputs của Bảo, không phải câu hỏi budget cho sếp. Không tự suy Bảo đã chốt toàn bộ skeleton hoặc bắt đầuPhase2. Phase2/3 chưa chạy. Root tự đối chiếu, không độc lập/POapproval hoặc finalpackagePASS.
