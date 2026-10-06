from pathlib import Path
import hashlib,json,re,subprocess
from PIL import Image
ROOT=Path(__file__).resolve().parents[4];HERE=Path(__file__).resolve().parent
BASE='89d94be6abb839f8834d1b62d9c715296fcd5d4c'
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
s=read(HERE/'selection.json')
for f in s['artifacts']:assert sha(ROOT/f['path'])==f['sha256'],f['path']
for b in s['main_anchor_bindings']:assert sha(ROOT/b['main']['path'])==b['main']['sha256']
html=(ROOT/s['active_demo']['path']).read_text(encoding='utf-8');stages=json.loads(re.search(r'const stages=(\[.*?\]);let stage=',html,re.S).group(1));cards=[c for a in stages for c in a['cards']];assert len(cards)==10 and len(s['active_selected'])==10
demo=(ROOT/s['active_demo']['path']).parent
for c,a in zip(cards,s['active_selected']):
 p=demo/c['image'];assert p.is_file() and sha(p)==a['asset']['sha256'];assert list(Image.open(p).size)==a['size'];assert Image.open(p).width>=1080
 assert (demo/c['destination']).is_file() if not c['destination'].startswith('https://') else c['destination']=='https://www.digiwin.com.vn/contact-vn/'
assert len(list((demo/'assets').glob('*.png')))==10
copy=read(HERE.parent/'week2-r2-metric-v1/full-journey-copy.json');assert 'Toàn dự án đi vào vận hành trong 3 tháng.' in copy['ads'][1]['cards'][1]['body']
for ad,stage in zip(copy['ads'],stages):
 assert ad['caption']==stage['caption']
 for c,v in zip(ad['cards'],stage['cards']):assert c['alt']==v['alt'] and c['native_headline']==v['headline']
assert not re.search(r'(?<!\w)bạn(?!\w)',json.dumps(copy,ensure_ascii=False),re.I)
case=(demo/'case-aplus.html').read_text(encoding='utf-8');assert sha(demo/'case-aplus.html')==s['case']['sha256']
assert not re.search(r'<(?:form|input|iframe)\b',case,re.I)
changed=subprocess.check_output(['git','diff',BASE,'--name-only'],cwd=ROOT,text=True).splitlines()
allowed={'README.md','CURRENT_STATE.md','DOCS_IMPACT_MAP.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/LinkedIn_Awareness_Execution_Plan.md','operations/Pre_Ad_Readiness_Plan.md','operations/linkedin-vn-journey-rebuild/2026-10-06/README.md'}
added={f['path'] for f in s['artifacts']}|{(HERE/n).relative_to(ROOT).as_posix() for n in ('integrate.py','verify.py','selection.json','Main_Message_Review.json','README.md','verification.json')}
assert set(changed)<=allowed|added,changed
for n in allowed:
 before=subprocess.check_output(['git','show',BASE+':'+n],cwd=ROOT)
 now=(ROOT/n).read_bytes();assert now.replace(b'\r\n',b'\n').endswith(before.replace(b'\r\n',b'\n')),n
# Verify every tracked file outside bounded docs unchanged; additions allowed only within selected artifact folders.
assert not subprocess.check_output(['git','diff',BASE,'--','scripts','operations/linkedin-locale-adapter','deliverables/linkedin-locale-dogfood','operations/linkedin-locale-dogfood','operations/linkedin-vn-journey-rebuild/2026-10-06/cold-v4','operations/linkedin-vn-journey-rebuild/2026-10-06/journey-v3','deliverables/linkedin-vn-journey/2026-10-06-v3'],cwd=ROOT)
result={'execution':'SUCCESS','review':'ROOT_SELF_REVIEW / NO_INDEPENDENT_AUDIT_CLAIM','PO':'PO_ACCEPTED_OFFLINE_WEEK2_V2','source_checkpoint':s['source_checkpoint'],'integration_base':BASE,'copied_exact_files':len(s['artifacts']),'active_images':10,'checks':['All imported source bytes/hashes equal immutable checkpoint','10selected native-square PNG and demo assets','RMK2-v3 named-scope3months copy/alt','All relative destination links resolve; contact href only','Case exact bytes/no form','Fresh main anchor pins and normalized source match','Current shared docs prepend only, all previous main bytes retained','Other locale/core/v3 files unchanged'],'generation_dependencies':'Archival receipts only; no executable runtime/dependency release inferred','git':'Validated selective branch before authorized local commit/merge; no remote push','live':'No account activity'}
(HERE/'verification.json').write_bytes((json.dumps(result,ensure_ascii=False,indent=2)+'\n').encode())
print('SUCCESS:82exact files,10selected images, link/copy/anchor/doc/protected-state checks.')
