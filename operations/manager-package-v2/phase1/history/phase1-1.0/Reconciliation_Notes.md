# Phase 1 — Đối soát và đầu vào Bảo chốt

Revision 1.0, 07/10/2026. [git-state.json](git-state.json) ghi checkout/commit/working files; [source-register.json](source-register.json) ghi exact byte hashes và source scope. Trạng thái account là observation có ngày của source, không readback mới. Plan đã checkpoint local `7796bc6`; Phase 1 là file làm việc trên nhánh riêng, chưa checkpoint mới/main merge/push.

## Contradictions đã giải theo nguồn

| Nguồn cũ / finding | Bằng chứng đối chiếu | Disposition dùng cho v2 |
|---|---|---|
| Cleanup/audience còn OPEN chung; 780 là quy mô hiện hành | SRC-COMPANY:424research completed/submit1lần; readback Updating; repaired mapping/reach pending | Research closed; processing/readback còn lại. Không restart, reupload hoặc dùng old780 forecast. |
| Backup và tệp công ty gốc là một nhánh | SRC-COMPANY vs SRC-BACKUP/R5upload | Hai dòng độc lập; backup52 không đóng Discovery424. |
| Summary R5 Ready/>90% nhưng Details0 | SRC-BACKUP exact observations | Mapping chưa kiểm được; không coi0 là sốcompanythật hoặc>90% làcustomer-fit. Unsaved estimates giữscope. |
| S04/mail/lịch cũ35m/43,75m, coldCarousel,8weeks hoặc7→21→4weeks | SRC-BUDGET + SRC-PROGRESS superseding notices | Cap11,7m +Single image route. Historical cadence khôngtựchuyểnthànhlịchv2. |
| VN đang sai hướng/chưa rebuild | Main VNcloseout/currenttwojourneys/readers | Revisionpivotcũhistorical; currentVNcreativeclosed/offlineadopted, dùngreadinessbridge. |
| OSAT chỉ70ảnh hoặc cònbatchgent | 12B1–B12manifest +3O3pilotsmain | B1–B12=120placements; B6–B12subset70; O3pilotsriêng30. KhôngnewOSATquota. |
| Fabless ledger cũ B14–B21 NOT_RUN; main snapshot B15 chưa PNG | Working attempts/selected manifests và postgen B14/B15 mới. Ledger của owner được cập nhật ngay trong lượt Phase1, audit phát hiện hash đổi và đã đọc lại. | B14v1/B15v2 mỗi bộ 11 selected; 13/12 attempts; native corrections closed, feed333/main640 và desktop reader SELF_REVIEW. Full mobile/whole-journey acceptance pending; B16–B21 chưa execution evidence. Refresh source pins, không sửa owner ledger. |
| PartnerB23/B24postgenNOT_RUN; ledger/closeoutnóiworkingfiles | Finalreviews +Git4a17968 chứaB23/B24 | 30selected/43calls; scopedrootreviewcomplete; committedlocal, chưaPOassetacceptance/creativemain. Ledgerflags/historicaltext khôngthayactualGit. |
| FDIreaderNOT_IMPLEMENTED hoặc25HTMLphảidựng | SRC-READERS-INVENTORY/currenttopnotice +10source/mainhashcomparisons |10concretefour-togglecheckpointsource-only.25rowsconditionalcoverage, khôngquota. |
| Toàn bộtrackingchưalàm hoặcpriorQAđóngmọiroutemới | SRC-TRACKING/S04priorproductionevidence | Existing3routepriorPASSWITHSCOPEEXCLUSION; readernew/campaignattribution cầnscopekhác. |
| Proofpublicphảiđềuunknown; hoặcmọicaseđượcduyệttoànphần | SRC-RIGHTS29/09 +02/10revalidation +Partneranchor | ExistingVIuse/translationapprovalexactscopegiữnguyên. Broadernumericclaims/customerlogo/newphoto/publicpaiduse đốichiếuriêng; khôngwithdrawapprovalvôcăn cứ. |
| Workbook11sheetđãbổsung vs packageworkbook6sheet | Anchor dẫn revisionhistorical11sheet; exactSRC-LEGACY-WORKBOOKfileXML có6sheet/29formulas | Hai revision/outputs khácnhau; khôngkếtluậnworkbookthiếuhoặcchọn6/11làmrequirementv2. |
| 22questions/engine/versionboundanswers phải giữ | SRC-WORKFLOW mới | Khôngcarrydefault/answers. Phase2 mớisoạn3–4nội dung đầu tư; giữ integrityrecordsngoàipackage. |

## Các đầu vào chưa chốt — nội bộ của Bảo

| ID | Input / business impact | Phương án làm việc hiện tại | Owner / lúc cần |
|---|---|---|---|
| OPEN-01 | Thuế/phí/FX và tổng all-in ảnh hưởng con số trình đầu tư. | Dùng11,7mmedia; giữall-inpending, bổ sungFinance/billingthựctế, không%đệm. | Bảo/Finance trước bộ budget final. |
| OPEN-02 | Nhóm đầu, lịch/daily và điều kiện dùng6,1mheld ảnh hưởngpacing/delivery. | D09–D14 làreference; chọnítmẫumộtgroup phùhợp mapping/reach; khôngchiađều4locale hoặcnhânbudgettheobatch. | Bảo trước triển khai; logic draft đượcchốt trướcPhase2. |
| OPEN-03 | Reader revision ảnh hưởngdemo/locale/return/dependencies và measurement. | Mainselected làbaseline;10redesignsourceđãduyệtoffline cópins nhưngchưaadopt. Giữrõhai revision tớiBảochọn. | Bảo/destinationowner trước final library/exports. |
| OPEN-04 | Baseline/numericKPI/stop và sourceRMK ảnh hưởngcáchđọcđợtđầu. | Scorecarddefinitions/cadenceproposalđãcó; dùngactualđúngscope; khôngoldthresholds/forecast. | Bảo trước chạy; measurementlogic chốt trướcPhase2. |

Các dependencies vận hành khác — mapping/R5Details, exact cohort IDs/rule/window, Fabless render, Partner PO asset approval, final reader entry/tracking, new proof/ảnh rights — nằm ở S7 và registers. Không đẩy thành loạt câu hỏi xin sếp duyệt. Không gửi support, re-upload, genảnh hoặc bật campaign trongPhase1.

## Change register v1 → v2 ở bước data

Giữ: currentmedia cap, Singleimage→new-adRMKroute, táchVN/FDI, proofexactscope và layeredmeasurement. Refresh: haiaudienceluồng; currentcreative/source/mainadoption; readerrevisions; existingtrackingscope. Bỏlàmdefault:22questions/engine/answers, oldbudgets/schedules/cleanedreachforecast, VNtrial/SIpersonaPartner, sốsheet/formula/quotalayoutcũ. Bổsung: sourcedata/assetclaimregisters,34dispositions vàworkflowBảodata→split→polish.

## Documentation impact

Đã đọc CURRENT_STATE, DOCS_IMPACT_MAP và canonical progress/budget/kickoff/S01/S04/readiness/tracking/RMK/search/publicsources. Cập nhật scoped current-progress notice trong checkout package để chỉ rõ Fabless/Partner source advancements; thêm trạng thái package Phase1 ở CURRENT_STATE và owned README. Main worktree và sourceworktrees chỉ đọc; không sửa owner ledgers, frozen files, history/receipts hoặc assetbytes. Những trạng thái adoption/runtime/budget hiện hành không đổi. Main chưa nhận các docs/file Phase1 này.

Trạng thái **PHASE1_PREPARED / BAO_DATA_LOCK_PENDING**: data/skeleton/registers và kiểm bounded đã thực hiện; OPEN-01–04 vẫn là input phải chốt hoặc được Bảo chấp nhận như assumption trước Phase2. Phase2/3 chưa chạy. Root tự đối chiếu, không độc lập/POapproval hoặc finalpackagePASS.
