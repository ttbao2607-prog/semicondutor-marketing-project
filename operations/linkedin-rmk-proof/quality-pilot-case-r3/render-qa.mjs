import {spawn} from 'node:child_process';
import {mkdtempSync,writeFileSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {join} from 'node:path';
const profile=mkdtempSync(join(tmpdir(),'codex-rmk-render-'));
const browser=spawn('C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',['--headless=new','--disable-gpu','--no-first-run','--remote-debugging-port=0',`--user-data-dir=${profile}`],{windowsHide:true});
let stderr='';browser.stderr.on('data',b=>stderr+=b);
const delay=n=>new Promise(r=>setTimeout(r,n));
let ws;
try{
 for(let i=0;i<100&&!stderr.includes('DevTools listening on');i++)await delay(100);
 const endpoint=stderr.match(/DevTools listening on (ws:\/\/[^\s]+)/)?.[1];if(!endpoint)throw Error('No owned debugger endpoint');
 ws=new WebSocket(endpoint);await new Promise((r,j)=>{ws.onopen=r;ws.onerror=j});let seq=0;const pending=new Map();
 ws.onmessage=e=>{const m=JSON.parse(e.data);if(m.id){const p=pending.get(m.id);pending.delete(m.id);m.error?p.reject(Error(JSON.stringify(m.error))):p.resolve(m.result)}};
 const send=(method,params={},sessionId)=>new Promise((resolve,reject)=>{const id=++seq;pending.set(id,{resolve,reject});ws.send(JSON.stringify({id,method,params,...(sessionId?{sessionId}:{})}))});
 const {targetId}=await send('Target.createTarget',{url:'about:blank'});const {sessionId}=await send('Target.attachToTarget',{targetId,flatten:true});
 const call=(m,p={})=>send(m,p,sessionId);await call('Page.enable');
 const evidence=[];
 for(const mode of ['desktop','mobile']){
  await call('Emulation.setDeviceMetricsOverride',{width:mode==='mobile'?390:1440,height:mode==='mobile'?1100:1100,deviceScaleFactor:1,mobile:false});
  for(let card=1;card<=4;card++){
   await call('Page.navigate',{url:`http://127.0.0.1:8765/index.html?mode=${mode}&card=${card}`});await delay(350);
   const state=await call('Runtime.evaluate',{expression:`JSON.stringify({qa:JSON.parse(document.documentElement.dataset.qa||'[]'),images:[...document.images].map(i=>({loaded:i.complete&&i.naturalWidth>0})),ordinal:document.querySelector('.ordinal')?.textContent,bodyOverflow:document.body.scrollWidth>innerWidth})`,returnByValue:true});
   evidence.push({mode,card,...JSON.parse(state.result.value)});
   const shot=await call('Page.captureScreenshot',{format:'png'});writeFileSync(new URL(`./${mode}-${card}.png`,import.meta.url),Buffer.from(shot.data,'base64'));
  }
 }
 writeFileSync(new URL('./render-evidence.json',import.meta.url),JSON.stringify({renderer:'owned isolated headless Edge, loopback only; no signed-in browser',views:evidence},null,2));
 const bad=evidence.filter(e=>e.images.some(i=>!i.loaded)||e.qa.length!==4||e.ordinal!==`${e.card}/4`||e.bodyOverflow);
 if(bad.length)throw Error('Render checks failed '+JSON.stringify(bad));
 console.log('Rendered 8 desktop/mobile views, 4 original PNG loaded; images/order/navigation boundary checks passed. Human/visual inspection separate.');
 await send('Browser.close');
}finally{ws?.close();browser.kill()}
