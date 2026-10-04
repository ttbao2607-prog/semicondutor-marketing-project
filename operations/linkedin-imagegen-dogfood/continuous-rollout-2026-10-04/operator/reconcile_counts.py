import pathlib,json,hashlib
B=pathlib.Path(__file__).resolve().parent.parent
G=pathlib.Path(r'C:\Users\ASUS\.codex\generated_images\01a10436-c1be-7051-a9fe-a6f76ad94045')
orig={hashlib.sha256(p.read_bytes()).hexdigest():str(p) for p in G.glob('*.png')}
records=[]
for p in B.glob('*/operator/*/native/*.json'):
 d=json.loads(p.read_text(encoding='utf-8-sig'));h=d['native_sha256'];records.append({'native_check':str(p.relative_to(B)).replace(chr(92),'/'),'sha256':h,'tool_original_path':orig.get(h),'original_bytes_equal':h in orig,'kind':p.parents[1].name})
(B/'operator/native-provenance.json').write_text(json.dumps(records,indent=2)+'\n',encoding='utf-8')
p=B/'operator/queue-ledger.json';q=json.loads(p.read_text(encoding='utf-8-sig'));q['actual_calls']={'base':sum(x['kind']!='corrections' for x in records),'correction':sum(x['kind']=='corrections' for x in records)};p.write_text(json.dumps(q,indent=2)+'\n',encoding='utf-8');print(json.dumps({'count':len(records),'missing_original':sum(not r['original_bytes_equal'] for r in records),'actual_calls':q['actual_calls']}))
