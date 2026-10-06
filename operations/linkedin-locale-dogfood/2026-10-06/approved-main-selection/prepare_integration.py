"""Bounded, source-pinned artifact integration; no generation or Git mutation."""
import hashlib,json,re,shutil,subprocess,sys
from pathlib import Path
from PIL import Image

ROOT=Path.cwd()
SOURCE=Path(sys.argv[1]).resolve()
CHECKPOINT='bfb710accddfb7a2a183001d8cc15d7c0c3551c8'
BASE='2cf29d638a6ad212d5e1a583efbd2f3d68fafda2'
OPS=Path(__file__).resolve().parent
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=ROOT).decode().strip()==BASE
assert subprocess.check_output(['git','rev-parse','HEAD'],cwd=SOURCE).decode().strip()==CHECKPOINT
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def save(name,obj): (OPS/name).write_bytes((json.dumps(obj,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
srcops=SOURCE/'operations/linkedin-locale-dogfood/2026-10-06'
srcdel=SOURCE/'deliverables/linkedin-locale-dogfood/2026-10-06'
configs=[('candidate1','en-osat-candidate1-v4','en-osat-candidate1-corrective-v3','final-candidate-manifest.json'),('candidate3','zh-Hant-osat-candidate3-v1','zh-Hant-osat-candidate3-v1','final-viewer-manifest.json')]
files=[]
units=[]
for candidate,folder,opfolder,manifest in configs:
    source=srcdel/folder
    dest=ROOT/'deliverables/linkedin-locale-dogfood/2026-10-06'/folder
    assert not dest.exists(),dest
    dest.mkdir(parents=True)
    rows=read(srcops/opfolder/manifest)['rows']
    assert len(rows)==10
    for row in rows:
        s=source/row['image']; t=dest/row['image']
        assert sha(s)==row['sha256']
        t.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(s,t)
        im=Image.open(t);im.load();assert im.size==(1254,1254)
        assert sha(t)==row['sha256']
        units.append({'candidate':candidate,'index':row['index'],'path':str(t.relative_to(ROOT)).replace('\\','/'),'sha256':sha(t),'source_path':str(s.relative_to(SOURCE)).replace('\\','/'),'copy':row['copy'],'caption':row['caption']})
    for name in ['index.html','case-reader.html','journey.json']:
        shutil.copyfile(source/name,dest/name)
    scope=('PO-accepted offline English candidate1 v4. No open image correction; native/feed findings closed. Actual mobile viewport review still NOT_PERFORMED; historical MSG-ANCHOR rendered verdict remains INSUFFICIENT_EVIDENCE. This folder is for internal review, not technical ready/production release.' if candidate=='candidate1' else 'PO-accepted offline Traditional Chinese candidate3 final. Card9 and10 source hierarchy corrected; no open material finding. Root SELF_REVIEW covers native, desktop, narrow feed, mobile and reader. No independent native-market/buyer validation or automatic bulk acceptance.')
    (dest/'README.md').write_bytes(('# '+folder+'\n\n'+scope+'\n\nOpen index.html for the ten-card final selection and case-reader.html for the reader. All PNGs retain source bytes. Folder delivery only; no ZIP, rejected/first-attempt images or generation inputs. Source checkpoint: '+CHECKPOINT+'. See operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection for provenance. Adapter remains DEVELOPING / NOT_FROZEN; this merge grants no generation/live authority.\n').encode('utf-8'))
    evidence=OPS/'evidence'/candidate;evidence.mkdir(parents=True)
    for name in [manifest,'postgen-review.json']+(['po-checkpoint-acceptance.json'] if candidate=='candidate1' else ['browser-review.json']):
        shutil.copyfile(srcops/opfolder/name,evidence/name)
    for p in dest.rglob('*'):
        if p.is_file(): files.append({'path':str(p.relative_to(ROOT)).replace('\\','/'),'sha256':sha(p)})
    for name in ['index.html','case-reader.html']:
        text=(dest/name).read_text(encoding='utf-8-sig')
        for script in re.findall(r'<script[^>]*>(.*?)</script>',text,re.S):
            check=subprocess.run(['node','--check'],input=script.encode('utf-8'),capture_output=True)
            assert check.returncode==0,check.stderr.decode('utf-8')
        for link in re.findall(r'(?:href|src)=[\"\']([^\"\']+)',text):
            if not link.startswith(('http:','https:','#','data:')):
                assert (dest/link.split('#')[0]).is_file(),link
        for row in rows:assert (dest/row['image']).is_file()
shutil.copyfile(srcops/'checkpoint-main-selection/candidate3-po-acceptance.json',OPS/'evidence/candidate3/po-acceptance.json')
shutil.copyfile(srcops/'checkpoint-main-selection/selection-review.json',OPS/'source-selection-review.json')
for file in ['operations/Vy_Email_Content_Anchor.md','operations/source-evidence/Vy_Email_User_Provided_2026-10-06.md','scripts/prepare_linkedin_locale.py']:
    assert sha(ROOT/file)==sha(SOURCE/file),file
attrs=ROOT/'.gitattributes'
attrs.write_bytes(attrs.read_bytes()+b'\n# Preserve approved offline locale artifact/provenance bytes; no lifecycle promotion.\ndeliverables/linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-v4/** -text\ndeliverables/linkedin-locale-dogfood/2026-10-06/zh-Hant-osat-candidate3-v1/** -text\noperations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/** -text\n')
entry='> **FDI locale artifacts · 2026-10-06 — approved offline integration.** Candidate1 English-v4 và candidate3 phồn thể final đã được Bảo duyệt đưa vào main local:20 PNG gốc +2 viewer/reader, giao bằng thư mục, không ZIP. Candidate1 không còn lỗi ảnh mở nhưng vẫn thiếu actual mobile render; không nâng gate thành technical ready. Candidate3 scoped root SELF_REVIEW native/desktop/feed/mobile/reader,0 finding material mở. Candidate2 giản thể card9 còn cần sửa source hierarchy và render chưa đủ: giữ riêng trên nhánh nguồn. Adapter vẫn DEVELOPING / NOT_FROZEN. [Phạm vi và provenance]({link}). Source checkpoint `bfb710a`; không nhập lịch sử nghiên cứu, guard/freeze executable chưa có trên main hoặc cấp quyền generation/live. VN v3/Aplus hiện hành giữ nguyên; không push.\n\n'
for file,link in [('CURRENT_STATE.md','operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md'),('README.md','operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md'),('operations/Pre_Ad_Readiness_Plan.md','linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md'),('ads/linkedin/LinkedIn_Build_Pack.md','../../operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md'),('operations/linkedin-locale-adapter/README.md','../linkedin-locale-dogfood/2026-10-06/approved-main-selection/README.md')]:
    p=ROOT/file;p.write_bytes(entry.replace('{link}',link).encode('utf-8')+p.read_bytes())
save('manifest.json',{'revision':'approved-offline-main-artifacts-v1','source_checkpoint':CHECKPOINT,'base_main':BASE,'authority':'Bảo: commit local lấy checkpoint ... merge main artifact các bản đã duyệt','selected_units':units,'artifact_files':files,'excluded':['candidate2 unresolved card9','ZIP','rejected/first-attempt PNGs','generation contracts/scripts/harness/guard freeze','unrelated research history'],'review_scope':{'candidate1':'PO_ACCEPTED_OFFLINE; MOBILE_RENDER_PENDING','candidate3':'PO_ACCEPTED_OFFLINE; ROOT_SELF_REVIEW_PASS','adapter':'DEVELOPING / NOT_FROZEN'},'evidence_policy':'Evidence copies preserve original verdict/bytes. Source paths in those snapshots refer to the source checkpoint, not an assertion all generation dependencies exist on main. No retrospective gate PASS.'})
save('verification.json',{'status':'SUCCESS','audit':'ROOT_SELF_REVIEW','selected_pngs_original_sha256_match':20,'selected_pngs_decode':'1254x1254_PASS','portable_viewer_js_links':'PASS','anchor_source_adapter_match':'PASS','candidate2_artwork_imported':False,'zip_imported':False,'new_generation':0,'main_merge':'PENDING_LOCAL_GIT_MERGE','scope_audit':'Staged diff and committed tree must be checked before merge.'})
(OPS/'README.md').write_bytes(('''# Approved offline locale artifact integration · 2026-10-06

Source checkpoint **bfb710a**, integration base **2cf29d6**. Bảo requested local checkpoint and merge of reviewed artifact versions; no push/live authority. Twenty original final PNGs, two portable viewers/readers, folder delivery only.

| Candidate | Image correction | Main scope |
|---|---|---|
| 1 · English v4 | None open; original3 findings and later source reflows closed | PO-accepted offline review artifact; actual mobile viewport review still pending, historical gate remains insufficient evidence |
| 2 · Simplified Chinese | Card9 case source still too small after corrective | Excluded; source checkpoint retains images/findings |
| 3 · Traditional Chinese final | None open; card9/10 source corrections reviewed | PO-accepted offline artifact with root native/desktop/feed/mobile/reader self-review |

[English viewer](../../../../deliverables/linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-v4/index.html) · [Traditional Chinese viewer](../../../../deliverables/linkedin-locale-dogfood/2026-10-06/zh-Hant-osat-candidate3-v1/index.html).

Minimal evidence snapshots retain original verdicts and hash pins. Historical failed receipts are not upgraded. Main receives selected artifacts, not the research branch or current guarded generation dependency set; prior source freeze does not imply callable guard readiness on main. Adapter stays DEVELOPING / NOT_FROZEN. Current VN accepted v3/Aplus work, tracking, budget, campaign and core remain outside this integration.

Docs impact reviewed: current-state/root README/readiness/build pack/adapter README updated additively. Anchor/source/editorial/runbook and strategy/budget/profile/status require no change. .gitattributes receives only scoped byte-preservation rules. Inspect manifest.json, verification.json and staged/committed scope for original-byte identity and exclusions. This is root SELF_REVIEW plus quoted PO approval, not independent native-market/buyer or bulk-production acceptance.
''').encode('utf-8'))
print(json.dumps({'source_checkpoint':CHECKPOINT[:7],'selected_pngs':20,'artifact_files':len(files),'excluded':'candidate2 and ZIP','static_checks':'PASS'}))
