"""Verify committed integration scope and staged/original native bytes."""
import hashlib,json,subprocess
from pathlib import Path
from PIL import Image
ROOT=Path.cwd()
OPS=Path(__file__).resolve().parent
def read(p):return json.loads(p.read_text(encoding='utf-8-sig'))
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT)
manifest=read(OPS/'manifest.json')
base=manifest['base_main']
allowed={'.gitattributes','CURRENT_STATE.md','README.md','ads/linkedin/LinkedIn_Build_Pack.md','operations/Pre_Ad_Readiness_Plan.md','operations/linkedin-locale-adapter/README.md'}
prefixes=('deliverables/linkedin-locale-dogfood/2026-10-06/en-osat-candidate1-v4/','deliverables/linkedin-locale-dogfood/2026-10-06/zh-Hant-osat-candidate3-v1/','operations/linkedin-locale-dogfood/2026-10-06/approved-main-selection/')
changes=git('diff','--name-status',base,'HEAD').decode('utf-8').splitlines()
for line in changes:
    status,path=line.split('\t')
    assert path in allowed or (status=='A' and path.startswith(prefixes)),line
    assert not path.endswith('.zip'),path
    assert 'linkedin-vn-' not in path,path
for row in manifest['artifact_files']:
    blob=git('show','HEAD:'+row['path'])
    assert hashlib.sha256(blob).hexdigest()==row['sha256'],row['path']
    assert blob==(ROOT/row['path']).read_bytes(),row['path']
for row in manifest['selected_units']:
    p=ROOT/row['path'];im=Image.open(p);im.load();assert im.size==(1254,1254)
assert len(manifest['selected_units'])==20
for folder in ['en-osat-candidate1-v4','zh-Hant-osat-candidate3-v1']:
    assert len(list((ROOT/'deliverables/linkedin-locale-dogfood/2026-10-06'/folder/'assets').glob('*.png')))==10
v=read(OPS/'verification.json')
v.update({'scope_audit':'PASS_COMMITTED_ARTIFACTS_ONLY','committed_artifact_byte_matches':28,'original_png_decode_matches':20,'base_existing_files_changed':sorted(allowed),'protected_main_vn_core_tracking_budget':'UNCHANGED_IN_COMMITTED_DIFF','candidate1_mobile_gate':'NOT_PERFORMED_PRESERVED','candidate2':'EXCLUDED','committed_file_count_before_audit_receipt':len(changes),'audited_artifact_commit':git('rev-parse','HEAD').decode().strip(),'audit_recovery':'Initial precommit audit stopped on Windows default encoding; artifact commit existed before audit completed. UTF-8 audit rerun on committed tree now PASS; merge not yet performed.','main_merge':'READY_FOR_AUTHORIZED_LOCAL_MERGE'})
(OPS/'verification.json').write_bytes((json.dumps(v,ensure_ascii=False,indent=2)+'\n').encode('utf-8'))
print(json.dumps({'scope':'PASS','committed_artifact_original_bytes':28,'pngs_decoded':20,'VN_other_protected':'UNCHANGED','candidate2':'EXCLUDED','zip':'EXCLUDED'}))
