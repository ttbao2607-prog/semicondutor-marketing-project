import pathlib,json,hashlib
B=pathlib.Path(__file__).resolve().parent;Q=B.parent;R=B.parents[3]
def h(p):return hashlib.sha256(p.read_bytes()).hexdigest()
G=pathlib.Path('C:/Users/ASUS/.codex/generated_images/01a10436-c1be-7051-a9fe-a6f76ad94045');orig={h(p):str(p) for p in G.glob('*.png')}
rows=[]
for case in ['P1','P2','O4-Q']:
 for p in (Q/case/'operator').rglob('native/*.json'):
  d=json.loads(p.read_text(encoding='utf-8-sig'));s=d['native_sha256'];assert h(R/d['output_path'])==s and s in orig
  for path,pin in d['input_hashes'].items():assert h(R/path)==pin,path
  assert min(d['actual_dimensions'])>=1080
  rows.append({'treatment':case,'call_id':d['call_id'],'native_check':p.relative_to(Q).as_posix(),'sha256':s,'tool_original_path':orig[s],'original_bytes_equal':True,'reserve':'/reserve/' in p.as_posix()})
(B/'native-provenance.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
q=json.loads((B/'queue-ledger.json').read_text());q['actual_calls']={'primary':sum(not x['reserve'] for x in rows),'reserve':sum(x['reserve'] for x in rows)};assert q['actual_calls']['primary']<=8 and q['actual_calls']['reserve']<=4;(B/'queue-ledger.json').write_text(json.dumps(q,indent=2)+'\n',encoding='utf-8');print(json.dumps(q['actual_calls']))
