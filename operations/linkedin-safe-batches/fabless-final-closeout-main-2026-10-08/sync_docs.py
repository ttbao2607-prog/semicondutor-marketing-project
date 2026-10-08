"""Prepend current scoped truth; preserve all dated history and non-Fabless rows."""
import hashlib,json,os,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
HERE=Path(__file__).resolve().parent
target=HERE/'README.md'
docs=['CURRENT_STATE.md','README.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','drafts/S03_LinkedIn_Audience_Research.md','operations/LinkedIn_Current_Progress_2026-10-07.md','operations/LinkedIn_Report_Artifact_Index_2026-10-05.md','operations/linkedin-safe-batches/parallel-handoff-2026-10-07/README.md']
report=[]
for name in docs:
 p=ROOT/name;before=p.read_bytes();old=before.decode('utf-8-sig')
 rel=os.path.relpath(target,p.parent).replace('\\','/')
 banner=f'> **Fabless generation COMPLETE / checkpoint main · 08/10/2026:** B13–B21 đủ **9/9batch,99vị trí PNG selected kể cả reuse;0batch chưa generation**. Nhập thêm44PNG cuối B18v4/B19v1/B20v3/B21v1 từ checkpoint **39a3abde**. Native/desktop640/feed333 scoped SELF_REVIEW PASS; B18–B21 full gate **INSUFFICIENT_EVIDENCE/PARTIAL** do thiếu ảnh mobile/reader (B21 mới1card mobile). **B15 proof2 CHANGES_REQUIRED** vì headline giản thể trong bản phồn thể; old/main bytes và lịch sử giữ nguyên, không PASS hồi tố. Hoàn tất generation/đóng nhánh nguồn để lưu trữ; chưa technical-ready/independent/live. [Danh mục, qualification và evidence]({rel}). Bảo đã cho merge và push backup; actual remote readback ghi riêng trong hồ sơ tích hợp. Mọi trạng thái NOT_RUN/chưa-main/chưa-push bên dưới là snapshot cũ theo ngày/revision, không current Fabless status. Frozen/process không đổi; adapter DEVELOPING/NOT_FROZEN.\n\n'
 assert not old.startswith('> **Fabless generation COMPLETE / checkpoint main')
 count=0
 if name=='operations/LinkedIn_Current_Progress_2026-10-07.md':
  rows=old.splitlines(keepends=True);out=[]
  for line in rows:
   if line.startswith('| Fabless FDI |'):
    ending='\r\n' if line.endswith('\r\n') else '\n'
    line='| Fabless FDI | **GENERATION_COMPLETE: B13–B21 đủ9batch/99selected PNG positions kể cả reuse;0batch chưa generation.** B18v4/B19v1/B20v3/B21v1 thêm44PNG cuối từ39a3abde. | Selected checkpoint trên main theo mandate; B18–B21 native/desktop/feed scoped PASS, full mobile INSUFFICIENT_EVIDENCE. B15 proof2 mixed-script CHANGES_REQUIRED; không blanket Hant PASS. Không independent/live certification. [Closeout](linkedin-safe-batches/fabless-final-closeout-main-2026-10-08/README.md). |'+ending
    count+=1
   out.append(line)
  assert count==2
  old=''.join(out)
 p.write_bytes(banner.encode()+old.encode('utf-8'))
 report.append({'path':name,'before_sha256':hashlib.sha256(before).hexdigest(),'after_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'changes':'Current Fabless banner only; two Fabless rows replaced' if count else 'Current Fabless banner only; existing body preserved'})
lane=ROOT/'operations/linkedin-safe-batches/parallel-fabless-2026-10-07/README.md'
assert not lane.exists()
lane.write_text('# Fabless — generation complete / checkpoint archive\n\nB13–B21 generation9/9,99selected card positions including reuse,0remaining. [Current main catalog, scope and evidence](../fabless-final-closeout-main-2026-10-08/README.md). Current B18–B21 technical gate INSUFFICIENT_EVIDENCE; B15 proof2 CHANGES_REQUIRED. Main contains selected finals/current evidence; full attempts remain on backed-up source branch. This closes the generation branch without upgrading technical/live acceptance.\n','utf-8')
(HERE/'docs-synchronization.json').write_text(json.dumps({'reviewer':'/root','changes':report,'history_preserved':True,'other_progress_rows_unchanged':True},ensure_ascii=False,indent=2)+'\n','utf-8')
print('Synchronized',len(report),'canonical/entrypoint docs and new lane index;2Fabless rows,other rows preserved')
