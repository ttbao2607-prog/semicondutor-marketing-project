import pathlib,json,hashlib,zipfile,subprocess
R=pathlib.Path('D:/linkedin-awareness-harness-redesign');B=pathlib.Path(__file__).resolve().parent;Q=B.parent;OLD=R/'operations/linkedin-imagegen-dogfood/continuous-rollout-2026-10-04'
O=pathlib.Path('C:/Users/ASUS/Documents/Codex/2026-10-04/va/outputs');D=O/'LinkedIn_Complete_Rollout_2026-10-04'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
base=j(B/'protected-baseline.json');allowed=set(j(B/'allowed-current-doc-delta.json')['files']);changed=[p for p,s in base.items() if not (R/p).is_file() or h(R/p)!=s];assert set(changed)<=allowed
checks=j(B/'native-provenance.json');assert len(checks)==10 and sum(x['reserve'] for x in checks)==2
for n in checks:
 c=j(Q/n['native_check']);assert c['native_sha256']==n['sha256']==h(pathlib.Path(n['tool_original_path']))==h(R/c['output_path']);assert c['actual_dimensions']==[1254,1254]
 for p,s in c['input_hashes'].items():assert h(R/p)==s,p
sources={x['treatment']:OLD/x['treatment'] for x in j(OLD/'operator/queue-ledger.json')['queue'] if x['status']=='AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE'};assert len(sources)==8
sources.update({c:Q/c for c in ['P1','P2','O4-Q']});assert len(sources)==11
expected={'index.html':h(D/'index.html')};candidates={}
for case,src in sources.items():
 m=j(src/'worker/viewer-build-manifest.json');assert len(m['files'])==7
 for p,s in m['files'].items():assert h(src/'public'/p)==s==h(D/case/p);expected[case+'/'+p]=s
 for p,s in m['input_hashes'].items():assert h(R/p)==s,p
 candidates[case]=m['files']
assert {p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}==set(expected)
with zipfile.ZipFile(O/'LinkedIn_Complete_Rollout_2026-10-04.zip') as z:
 assert set(z.namelist())==set(expected)
 for p,s in expected.items():assert hashlib.sha256(z.read(p)).hexdigest()==s,p
assert len(expected)==78
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();assert head=='6d0d192dabf698ad9834c7add69aed84ce1646f8'
oldzip=O/'LinkedIn_Continuous_Rollout_2026-10-04.zip';assert h(oldzip)=='026073a310d27486bf558d098cf76c8d7c093b7513ed8fffcb6ccbcfe9094a76'
oldstatus=json.loads(subprocess.check_output(['git','show','HEAD:operations/LinkedIn_ImageGen_Harness_Status.json'],cwd=R,text=True,encoding='utf-8'));status=j(R/'operations/LinkedIn_ImageGen_Harness_Status.json');status.pop('corrective_rollout');assert status==oldstatus
out={'status':'PASS_MECHANICAL_SCOPE','baseline':head,'inventory':len(base),'equal_protected_files':len(base)-len(changed),'allowed_changed_files':changed,'fresh_native_originals':10,'primary':8,'reserve':2,'native_edge':1254,'readers':11,'selected_cards':55,'reader_files':77,'package_files':78,'package_sha256':h(O/'LinkedIn_Complete_Rollout_2026-10-04.zip'),'old_package_bytes_unchanged':True,'historical_status_objects_unchanged':True,'candidate_public_files':candidates}
(B/'final-mechanical-check.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:v for k,v in out.items() if k!='candidate_public_files'}))
