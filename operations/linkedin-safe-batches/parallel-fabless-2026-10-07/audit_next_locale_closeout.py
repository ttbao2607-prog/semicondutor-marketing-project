"""Read-only closeout audit, except its own result JSON. No semantic approval."""
import ast
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
LANE='operations/linkedin-safe-batches/parallel-fabless-2026-10-07'
DEL='deliverables/linkedin-safe-batches/parallel-fabless-2026-10-07'
def read(p): return json.loads((ROOT/p).read_text(encoding='utf-8'))
def digest(p): return hashlib.sha256((ROOT/p).read_bytes()).hexdigest()
def git(*args): return subprocess.check_output(['git',*args],cwd=ROOT).decode('utf-8').rstrip('\r\n')
pins=0
def audit_refs(obj):
    global pins
    if isinstance(obj,dict):
        if 'path' in obj and 'sha256' in obj:
            assert digest(obj['path'])==obj['sha256'],obj['path']
            pins+=1
        for v in obj.values(): audit_refs(v)
    elif isinstance(obj,list):
        for v in obj: audit_refs(v)

ledger=read(LANE+'/ledger.json')
assert ledger['counts']['two_batches_actual_calls']==25
assert ledger['remaining_queue']=='B16-B21 NOT_RUN'
audit_refs(ledger)
for batch,locale,version in [('B14','zh-Hans','v1'),('B15','zh-Hant','v2')]:
    base=LANE+'/'+batch+'-'+locale+'-f1-v1'
    out=DEL+'/'+batch+'-'+locale+'-f1-'+version
    receipt=read(base+'/postgen-review.json')
    audit_refs(receipt)
    audit_refs(read(base+'/verification.json'))
    assert receipt['audit_verdict']=='INSUFFICIENT_EVIDENCE'
    assert receipt['unresolved_creative_findings']==[]
    assert len(receipt['unit_reviews'])==11 and len(receipt['transition_reviews'])==10
    assert len(receipt['anchor_rules'])==7
    for unit in receipt['unit_reviews']:
        assert unit['full_render_verdict']=='INSUFFICIENT_EVIDENCE'
    reader=(ROOT/out/'case-reader.html').read_text(encoding='utf-8')
    assert 'https://www.digiwin.com.vn/resources/digiwin-semiconductor-8-case-studies-cn/' in reader
    assert '上海晶丰明源半导体股份有限公司' in reader
    assert 'href="index.html"' in reader
    # Every localized public-copy field is source-authored; no English copy inheritance.
    copies=read(out+'/selected-copy.json')['cards']
    assert copies[6]['card_id']=='F1-A6' and ('越南' in copies[6]['headline'])
    assert copies[8]['artwork_labels'][0]==('芯片设计案例' if batch=='B14' else '晶片設計案例')
    assert copies[9]['source_text'].endswith('上海晶丰明源半导体股份有限公司')

for f in read('operations/message-anchor/freeze-2026-10-06/manifest.json')['files']:
    assert digest(f['path'])==f['sha256']
    pins+=1
for f in (ROOT/LANE).glob('*.py'):
    ast.parse(f.read_text(encoding='utf-8'),filename=str(f))
changes=git('status','--porcelain=v1','-uall').splitlines()
for row in changes:
    assert row[:2] in [' M','??'],row
    assert row[3:].startswith((LANE+'/',DEL+'/')),row
assert git('diff','--cached','--name-only')==''
assert git('rev-parse','HEAD')=='e3b65780356cdf5f489ea3a45ac4927af616cd81'
assert git('branch','--show-current')=='slice/linkedin-safe-fabless-parallel'
assert subprocess.run(['git','diff','--check'],cwd=ROOT).returncode==0
assert not Path('C:/Users/ASUS/AppData/Local/Temp/fabless-b14-b15-full-preview-state.json').exists()
lock=Path('C:/Users/ASUS/AppData/Local/Temp/codex-linkedin-safe-batch-browser-owner.lock')
assert not lock.exists() or json.loads(lock.read_text(encoding='utf-8-sig'))['owner_id']!='Fabless-B14-B15-e3b6578-session-v1'
result=dict(revision='fabless-b14-b15-final-root-mechanical-audit-v1', reviewer='/root', independence='SELF_REVIEW', verdict='MECHANICAL_CLOSEOUT_PASS', pins_verified=pins, source_call_and_raw_byte_validation='Both bound batch verification receipts', frozen_files=24, selected_pngs=22, original_calls=22, corrective_calls=3, status='REVIEW_DRAFT_RENDER_GATE_PENDING', full_audit='INSUFFICIENT_EVIDENCE', creative_findings_open=0, semantic_authority='Actual root observations only; no independent/native-market/PO acceptance', git=dict(branch=git('branch','--show-current'),head=git('rev-parse','HEAD'),changed_paths_before_this_audit=len(changes),all_changes_inside_owned_roots=True,staged=False,new_commit=False,main_integration=False,push=False,remote_note='Initial fetch provided remote-tracking evidence; refs are not live GitHub verification. B14/B15 remain uncommitted files on this computer.'),cleanup=dict(own_preview_state_removed=True,own_browser_lock_released=True,tab_and_viewport='CUA actual close/reset observed'),stop='B16-B21 NOT_RUN',docs='Latest-main current-progress Fabless snapshot stale; concrete coordinator refresh in docs-impact.md, no shared canonical mutation.')
(ROOT/LANE/'B14-B15-final-audit.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False))
