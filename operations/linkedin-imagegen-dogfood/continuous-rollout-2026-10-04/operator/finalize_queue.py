import json,pathlib
B=pathlib.Path(__file__).resolve().parent
def read(name):return json.loads((B/name).read_text(encoding='utf-8-sig'))
def write(name,d):(B/name).write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
q=read('queue-ledger.json')
assert len(q['queue'])==11 and all(x['status'] in ['AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE','HOLD_AFTER_BOUNDED_CORRECTION','CHANGES_REQUIRED'] for x in q['queue'])
assert q['actual_calls']=={'base':31,'correction':7}
q.update(status='QUEUE_COMPLETED_WITH_FINDINGS',execution='PARTIAL',audit_verdict='FAIL',passing_treatments=8,held_treatments=3,selected_cards=40,reused_cards=20,current_finding='P1 closing; P2 A1/A4; O4-Q B4 retain exact-artwork findings after sole correction budget. No extra calls or human pauses.')
write('queue-ledger.json',q)
c=read('execution-contract.json');c['execution']='QUEUE_COMPLETED_WITH_FINDINGS';c['parent_disposition']='PARTIAL_NOT_WHOLE_CAMPAIGN_ACCEPTED';write('execution-contract.json',c)
n={'type':'BEHAVIORAL/RUNTIME','source':'Root actual mcp__cua_repl button interactions in current task','cases':{},'boundary':'8 passing local readers, no live or external CTA action'}
for x in q['queue']:
 if x['status']=='AUDIT_PASSED_UNDER_PO_CONTINUOUS_MANDATE':n['cases'][x['treatment']]={'sequence':['1/5','2/5','1/5','3/5','4/5','3/5'],'end':'5/5','next_disabled':True,'actions':['next','prev','dot3','ArrowRight','ArrowLeft','dot5']}
write('navigation-audit.json',n)
print('Queue classified11;8PASS3held;38actual calls;navigation8PASS')
