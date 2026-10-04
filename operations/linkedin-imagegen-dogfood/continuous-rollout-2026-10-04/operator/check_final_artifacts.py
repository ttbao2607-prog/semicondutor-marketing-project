import pathlib,json,hashlib,zipfile,subprocess
R=pathlib.Path('D:/linkedin-awareness-harness-redesign');B=pathlib.Path(__file__).resolve().parent;Q=B.parent
O=pathlib.Path('C:/Users/ASUS/Documents/Codex/2026-10-04/va/outputs');D=O/'LinkedIn_Continuous_Rollout_2026-10-04'
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def j(p):return json.loads(p.read_text(encoding='utf-8-sig'))
base=j(B/'protected-baseline.json');allowed=set(j(B/'allowed-current-doc-delta.json')['files']);changed=[p for p,s in base.items() if not (R/p).is_file() or h(R/p)!=s]
assert set(changed)<=allowed,(changed,allowed)
checks=j(B/'native-provenance.json');assert len(checks)==38
for n in checks:
 c=j(Q/n['native_check']);assert c['native_sha256']==n['sha256']==h(pathlib.Path(n['tool_original_path']))==h(R/c['output_path']);assert c['actual_dimensions']==[1254,1254]
 for p,s in c['input_hashes'].items():assert h(R/p)==s,p
cases=[x['treatment'] for x in j(B/'queue-ledger.json')['queue'] if x['status']=='AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE'];assert len(cases)==8
expected={'index.html':h(D/'index.html')}
for case in cases:
 m=j(Q/case/'worker/viewer-build-manifest.json');assert len(m['files'])==7
 for p,s in m['files'].items():assert h(Q/case/'public'/p)==s==h(D/case/p);expected[case+'/'+p]=s
 for p,s in m['input_hashes'].items():assert h(R/p)==s,p
assert {p.relative_to(D).as_posix() for p in D.rglob('*') if p.is_file()}==set(expected)
with zipfile.ZipFile(O/'LinkedIn_Continuous_Rollout_2026-10-04.zip') as z:
 assert set(z.namelist())==set(expected),z.namelist()
 for p,s in expected.items():assert hashlib.sha256(z.read(p)).hexdigest()==s,p
head=subprocess.check_output(['git','rev-parse','HEAD'],cwd=R,text=True).strip();assert head=='04ac95f038b95d3e4207d1beda01c21ed1b80bad'
d={'protected_inventory':len(base),'equal_protected_files':len(base)-len(changed),'allowed_changed_files':changed,'fresh_native_originals':38,'minimum_actual_edge':1254,'passing_readers':cases,'public_files':56,'portable_package_files':57,'package_sha256':h(O/'LinkedIn_Continuous_Rollout_2026-10-04.zip'),'HEAD':head,'candidate_public_hashes':expected,'status':'PASS_MECHANICAL_SUBSCOPE_ONLY','boundary':'Does not override creative findings or prove whole-campaign PASS'}
(B/'final-mechanical-check.json').write_text(json.dumps(d,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in d.items() if k!='candidate_public_hashes'}))
