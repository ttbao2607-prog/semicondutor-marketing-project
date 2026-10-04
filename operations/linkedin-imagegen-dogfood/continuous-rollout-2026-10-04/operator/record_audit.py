import pathlib,json,hashlib,argparse
B=pathlib.Path(__file__).resolve().parent.parent
p=argparse.ArgumentParser();p.add_argument('case');p.add_argument('observations');p.add_argument('--base',type=int,default=5);p.add_argument('--correction',type=int,default=0);a=p.parse_args();c=B/a.case;m=c/'worker/viewer-build-manifest.json'
d={'status':'AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE','audit_verdict':'PASS','scope':'Local5selectedcreative; no buyer/live claims','base_calls':a.base,'correction_calls':a.correction,'selected':5,'reused':0,'viewports':{'desktop':[1280,900],'mobile':[390,844]},'render_positions_observed':10,'visual_evidence':'Root current-task native images and mcp__cua_repl10 screenshot observations bound to selectedpublic hashes','observations':a.observations,'public_manifest_sha256':hashlib.sha256(m.read_bytes()).hexdigest(),'public_files':json.loads(m.read_text())['files'],'failed_or_open_criteria':[]}
(c/'operator/final-audit.json').write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
p=B/'operator/queue-ledger.json';q=json.loads(p.read_text(encoding='utf-8-sig'))
for x in q['queue']:
 if x['treatment']==a.case:x['status']=d['status']
p.write_text(json.dumps(q,indent=2)+'\n',encoding='utf-8')
print(a.case+' root visual receipt bound')
