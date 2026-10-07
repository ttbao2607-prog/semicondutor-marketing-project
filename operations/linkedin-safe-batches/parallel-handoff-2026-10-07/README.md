> **Partner scope correction — local candidate 2026-10-07.** Partner = nhà cung ứng công nghiệp theo [LDP đã được duyệt](../parallel-partner-2026-10-07/partner-ldp-content-anchor-v1.md). P1/P2 SI và P3 nội địa chỉ là nguồn lịch sử cần adapt cho FDI. Lượt hiện hành chỉ sửa ambiguity trong worktree Partner theo Bảo; chưa generation/commit/merge/push. Quyền sửa docs local của lượt này supersede riêng batch-write-only clause bên dưới; không cấp quyền cho worktree khác, frozen files hay live. Trạng thái PREPARED bên dưới là snapshot handoff ban đầu; Partner đã có worktree và đang chuẩn bị bản sửa để Bảo xét merge.

# Ba session FDI song song · 2026-10-07

PO yêu cầu chia các biến còn lại thành OSAT / Fabless / Partner để Bảo tự mở session. Đây là phân công thực thi offline theo plan batch hiện hành, không tự spawn. Kết quả handoff mong muốn: ba queue không trùng ID/path/writer, mỗi session có input, dependency, output, acceptance và stop rõ.

| Session | ID dành riêng | Queue dự kiến | Batch bắt đầu |
|---|---|---|---|
| OSAT | B6–B12 | O2 zh-Hant; O4-O en/zh-Hans/zh-Hant; O4-Q en/zh-Hans/zh-Hant | B6 O2 zh-Hant |
| Fabless | B13–B21 | F1, F2, F3; mỗi treatment en → zh-Hans → zh-Hant | B13 F1 en |
| Partner | B22–B30 | P1, P2, P3; mỗi treatment en → zh-Hans → zh-Hant | B22 P1 en |

25 là số batch dự kiến nếu tất cả intake fit. Không phải quota bắt buộc: Fabless/Partner cần recheck buyer/ERP trigger; P3 có thể HOLD nếu nguồn chỉ phục vụ VN hoặc khác persona. Không tự chuyển lane VN. Không chạy lại O1/B1–B3, O2 English/B4 hoặc giản thể/B5; O3 dùng pilot phù hợp, không gent lại mặc định.

## Dependency và quyền sở hữu

Nguồn executable đầy đủ: `D:/optimize-awareness-LinkedIn-adcopy`, commit `f2883d1c9db7c4abb72afa8998d2bde0cc192b74`, branch `slice/linkedin-audience-ready-research`. Main local `b2694b4` là selected artifact canonical, không phải source runtime đầy đủ. Cả hai chưa push; không dùng origin/main làm baseline runtime. File handoff mới hiện là working files; session đọc bản này từ đường dẫn tuyệt đối trước khi vào worktree riêng.

Bảo mở ba session và dán nội dung file tương ứng. Mỗi session tự recovery trước khi tạo nhánh/worktree riêng theo prompt được Bảo giao; không cùng sửa checkout nguồn. Source, B1–B5, frozen24pins, anchor/email và proof snapshots chỉ READ. Write chỉ batch paths/ledger/docs-impact của nhóm mình. Session này giữ shared canonical docs, freeze/core/adapter lifecycle và main integration. Session thực thi không spawn child, merge/push, sửa budget/live hoặc mở lane VN.

Mỗi nhóm một journey đang gent; tổng tối đa ba journey, thay giới hạn một journey toàn workflow trong plan cũ theo mandate song song mới của Bảo. Calls vẫn tuần tự trong từng session,10original +2corrective tối đa/batch, một corrective/card. Canary2card trước phần còn lại. Mọi batch chạy tới gent ảnh + reader + hậu kiểm trong mandate; browser thiếu evidence không tự nâng PASS, không gent lại để chữa preview. Dừng trước batch kế tiếp cho Bảo duyệt; danh sách queue không phải blanket acceptance.

## Browser dùng lần lượt

Mỗi session có tab/session name và own loopback preview server/state record riêng; không giả định port8765. Browser/viewport cùng backend có thể là tài nguyên chung dù khác tab. Chỉ một session điều khiển browser cùng lúc, kể cả tạo tab, viewport, navigation/capture và cleanup. Giữ quyền trong từng đoạn kiểm liên tục; trả quyền sau reset viewport và đóng own tab. Không đóng tab/process của nhóm khác.

Dùng một file quyền sở hữu tạm ngoài Git: `$env:TEMP/codex-linkedin-safe-batch-browser-owner.lock`. Session tạo bằng `FileMode.CreateNew` (atomic); ghi group/batch/branch/time, không chứa secret. File đã tồn tại: không browser action, không xóa/chiếm; báo nhóm đang giữ và tiếp tục công việc không cần browser. Không polling framework hoặc retry loop. Khi chính mình giữ quyền, cleanup own browser/server rồi xóa đúng file mình tạo. Nếu session chết, owner/Bảo phải xác nhận release trước khi session khác bỏ khóa; timeout không phải quyền takeover. Đây là ownership record tối giản, không scheduler/API mới.

Nếu không chứng minh browser riêng hoặc quyền độc quyền, giữ render pending và không điều khiển browser. Pregen anchor/script/fresh guard vẫn bắt buộc; scope cho gent khi render evidence thiếu kế thừa chỉ đạo Bảo “mỗi batch chạy tới gen ảnh”, không bypass semantic gate. Canary native lỗi phải sửa hoặc dừng; canary render thiếu thì ghi thiếu thực tế, không tuyên bố qua rendered gate.

## Acceptance và handoff từng batch

Đúng persona/locale, source/proof scope, advertiser voice, tất cả fields/scene/reader và từng transition được actual review trước gent; fresh wrapper trả đúng payload trước từng call. Native PNG giữ byte; chọn chỉ final10unit nếu intake thực là10. Đủ desktop/feed333/mobile actual390, reader/return khi tool cung cấp được; thiếu ghi INSUFFICIENT_EVIDENCE. Lỗi material ghi CHANGES_REQUIRED. Root tự review ghi SELF_REVIEW, không tự nhận native-market/independent/runtime model-effort certification.

Output thư mục thường: selected assets, index/reader, selected-copy/prompts/manifest, raw attempts, guard/release/anchor bindings, ledger/findings/closure/render coverage; bản diễn giải tiếng Việt cho Chinese. Báo paths, counts, unresolved findings, docs-impact; dừng cho Bảo. Commit chỉ theo lệnh riêng của Bảo trong session; main merge chỉ coordinator theo mandate riêng, selected cuối/evidence, không attempts/corrective dirs. Không ZIP.

Shared docs gate được xử lý bằng `docs-impact.md` của từng nhóm: liệt kê canonical đã đọc, statement đề nghị cập nhật và evidence path/hash. Session không sửa shared canonical. Coordinator đồng bộ trước handoff cuối/commit/merge. Historical pinned receipts không rewrite. Harness/anchor/process frozen, adapter DEVELOPING/NOT_FROZEN.

Trạng thái gói: PREPARED / chưa khởi động session,0ImageGen, chưa tạo worktree/commit/main merge/push trong lượt chia việc. Kiểm gói bằng25ID duy nhất,7/9/9, ba writer roots không overlap và stop sau first batch từng nhóm.
