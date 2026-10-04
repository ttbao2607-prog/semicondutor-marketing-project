import pathlib,json,hashlib,argparse
B=pathlib.Path(__file__).resolve().parent;Q=B.parent;R=B.parents[3]
p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('kind');p.add_argument('call');p.add_argument('verdict');p.add_argument('notes');a=p.parse_args()
c=json.loads((Q/a.case/'operator'/a.kind/'native'/(a.call+'.json')).read_text());out=R/c['output_path'];assert hashlib.sha256(out.read_bytes()).hexdigest()==c['native_sha256']
d={'call_id':a.call,'native_sha256':c['native_sha256'],'verdict':a.verdict,'evidence':'Root directly observed built-in ImageGen original returned image current task','notes':a.notes}
t=Q/a.case/'operator/visual';t.mkdir(exist_ok=True,parents=True);(t/(a.call+'.json')).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
q=json.loads((B/'queue-ledger.json').read_text());q['calls']=[x for x in q['calls'] if x['call_id']!=a.call]+[dict(d,treatment=a.case,kind=a.kind)];q['primary_used']=sum(not x['kind'].startswith('reserve') for x in q['calls']);q['reserve_used']=sum(x['kind'].startswith('reserve') for x in q['calls']);assert q['primary_used']<=8 and q['reserve_used']<=4;(B/'queue-ledger.json').write_text(json.dumps(q,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');print(a.call+' '+a.verdict)
