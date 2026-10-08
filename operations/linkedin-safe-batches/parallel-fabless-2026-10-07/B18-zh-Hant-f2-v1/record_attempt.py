from prepare_draft import *
import shutil,sys
from PIL import Image
plan=load(BASE+('/corrective-dispatch-plan.json' if '--corrective' in sys.argv else '/dispatch-plan.json'))
job=plan['calls'][int(sys.argv[1])];src=Path(sys.argv[2]);dst=ROOT/job['output_path'];assert not dst.exists();dst.parent.mkdir(parents=True,exist_ok=True);shutil.copyfile(src,dst)
assert hashlib.sha256(src.read_bytes()).hexdigest()==sha(job['output_path'])
im=Image.open(dst);assert im.format=='PNG' and im.width==im.height and im.width>=1080
entry=dict(call_id=job['call_id'],card_id=job['card_id'],kind='corrective' if '--corrective' in sys.argv else 'original',path=job['output_path'],sha256=sha(job['output_path']),width=im.width,height=im.height,copy_native_bytes=True,transformation=False,observations=sys.argv[3],reviewer='/root',independence='SELF_REVIEW',rendered='PENDING')
p=BASE+'/attempt-ledger.json';ledger=load(p) if (ROOT/p).exists() else dict(revision='b13-attempt-ledger-v1',attempts=[]);ledger['attempts'].append(entry);put(p,ledger)
put(job['folder']+'/native-checks/'+job['call_id']+'.json',entry);print(job['card_id']+': persisted '+str(im.width)+'px native PNG; '+entry['sha256'])
