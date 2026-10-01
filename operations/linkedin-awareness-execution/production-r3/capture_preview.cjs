// Explicit viewport capture for artifact QA, not an automated test.
const fs=require('fs'), path=require('path'),{spawn}=require('child_process');
const root=__dirname, profile=path.join(root,'browser-export-profile');
const chrome=spawn('C:/Program Files/Google/Chrome/Application/chrome.exe',['--headless','--disable-gpu','--no-first-run','--remote-debugging-port=9237','--user-data-dir='+profile,'about:blank'],{windowsHide:true,stdio:'ignore'});
const pause=ms=>new Promise(r=>setTimeout(r,ms));
(async()=>{
 try{
  let tabs;for(let i=0;i<40;i++){try{tabs=await(await fetch('http://127.0.0.1:9237/json')).json();break}catch(e){await pause(200)}}
  const ws=new WebSocket(tabs.find(t=>t.type==='page').webSocketDebuggerUrl);await new Promise(r=>ws.addEventListener('open',r,{once:true}));
  let id=0,pending=new Map();ws.addEventListener('message',ev=>{const v=JSON.parse(ev.data);if(pending.has(v.id)){const cb=pending.get(v.id);pending.delete(v.id);v.error?cb.reject(v.error):cb.resolve(v.result)}});
  const call=(method,params={})=>new Promise((resolve,reject)=>{const n=++id;pending.set(n,{resolve,reject});ws.send(JSON.stringify({id:n,method,params}))});
  await call('Page.enable');
  const observations=[];
  for(const [width,height,name] of [[1440,1100,'preview-desktop.png'],[390,844,'preview-mobile.png']]){
   await call('Emulation.setDeviceMetricsOverride',{width,height,deviceScaleFactor:1,mobile:width===390});
   await call('Page.navigate',{url:'http://127.0.0.1:8766/preview.html'});await pause(1000);
   const state=await call('Runtime.evaluate',{expression:'JSON.stringify({innerWidth:innerWidth,scrollWidth:document.documentElement.scrollWidth,bodyWidth:document.body.getBoundingClientRect().width})',returnByValue:true});observations.push({capture:name,...JSON.parse(state.result.value)});
   const shot=await call('Page.captureScreenshot',{format:'png',captureBeyondViewport:false});fs.writeFileSync(path.join(root,'qa',name),Buffer.from(shot.data,'base64'));
  }
  fs.writeFileSync(path.join(root,'qa','preview-viewport-evidence.json'),JSON.stringify(observations,null,2));
  await call('Browser.close');ws.close();console.log(JSON.stringify(observations));
 }finally{chrome.kill()}
})().catch(e=>{console.error(e);process.exitCode=1});
