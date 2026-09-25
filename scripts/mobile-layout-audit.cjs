// Local, read-only layout capture for a self-contained landing page.
// Usage: node scripts/mobile-layout-audit.cjs <loopback-url> <output-dir> [width height]
const fs = require('node:fs');
const os = require('node:os');
const path = require('node:path');
const { spawn } = require('node:child_process');

const [url, outputDir, widthArg = '390', heightArg = '844'] = process.argv.slice(2);
const width = Number(widthArg);
const height = Number(heightArg);
if (!/^http:\/\/127\.0\.0\.1:\d+\//.test(url || '') || !outputDir || !Number.isInteger(width) || !Number.isInteger(height)) {
  throw new Error('Pass a loopback HTTP URL, output directory, width and height.');
}
const chromePath = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
const profile = fs.mkdtempSync(path.join(os.tmpdir(), 'semi-mobile-cdp-'));
fs.mkdirSync(outputDir, { recursive: true });
const browser = spawn(chromePath, [
  '--headless=new', '--no-first-run', '--no-default-browser-check', '--disable-extensions',
  '--remote-debugging-port=0', `--user-data-dir=${profile}`, 'about:blank',
], { stdio: 'ignore', windowsHide: true });
const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));

async function main() {
  let port;
  for (let i = 0; i < 100; i++) {
    const activePort = path.join(profile, 'DevToolsActivePort');
    if (fs.existsSync(activePort)) {
      port = Number(fs.readFileSync(activePort, 'utf8').split('\n')[0]);
      break;
    }
    if (browser.exitCode !== null) throw new Error(`Chrome exited: ${browser.exitCode}`);
    await sleep(100);
  }
  if (!port) throw new Error('Chrome DevTools did not become ready.');
  const pages = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
  const target = pages.find(page => page.type === 'page');
  if (!target) throw new Error('No Chrome page target.');
  const ws = new WebSocket(target.webSocketDebuggerUrl);
  await new Promise((resolve, reject) => { ws.onopen = resolve; ws.onerror = reject; });
  let sequence = 0;
  const pending = new Map();
  ws.onmessage = event => {
    const packet = JSON.parse(event.data);
    if (!packet.id || !pending.has(packet.id)) return;
    const { resolve, reject } = pending.get(packet.id);
    pending.delete(packet.id);
    packet.error ? reject(new Error(packet.error.message)) : resolve(packet.result);
  };
  const send = (method, params = {}) => new Promise((resolve, reject) => {
    const id = ++sequence;
    pending.set(id, { resolve, reject });
    ws.send(JSON.stringify({ id, method, params }));
  });
  await send('Page.enable');
  await send('Runtime.enable');
  await send('Emulation.setDeviceMetricsOverride', { width, height, deviceScaleFactor: 1, mobile: width < 800 });
  await send('Page.navigate', { url });
  for (let i = 0; i < 100; i++) {
    const state = await send('Runtime.evaluate', { expression: 'document.readyState', returnByValue: true });
    if (state.result?.value === 'complete') break;
    await sleep(100);
  }
  await sleep(1500);
  const result = await send('Runtime.evaluate', {
    returnByValue: true,
    expression: `(() => {
      const rect = el => { const r = el.getBoundingClientRect(); return { top: Math.round(r.top + scrollY), height: Math.round(r.height) }; };
      return {
        url: location.href, viewport: { width: innerWidth, height: innerHeight },
        page: { height: document.documentElement.scrollHeight, width: document.documentElement.scrollWidth, overflowX: document.documentElement.scrollWidth > innerWidth },
        sections: [...document.querySelectorAll('main > section')].map(el => ({ id: el.id, ...rect(el) })),
        blocks: [...document.querySelectorAll('main > section > .wrap > *, .cockpit-console > *')]
          .filter(el => el.getBoundingClientRect().height > 0)
          .map(el => ({ section: el.closest('main > section')?.id, tag: el.tagName.toLowerCase(), className: String(el.className).slice(0, 80), ...rect(el) })),
        ctas: [...document.querySelectorAll('[data-consultation-cta], #partner-cta-header')].map(el => ({ id: el.id, text: el.textContent.trim(), ...rect(el) })),
        details: [...document.querySelectorAll('details')].map(el => ({ id: el.id, open: el.open, ...rect(el) })),
      };
    })()`,
  });
  const data = result.result?.value;
  if (!data) throw new Error('Layout evaluation returned no data.');
  const label = `${width}x${height}`;
  fs.writeFileSync(path.join(outputDir, `${label}.json`), JSON.stringify(data, null, 2));
  const screenshot = await send('Page.captureScreenshot', {
    format: 'png', captureBeyondViewport: true,
    clip: { x: 0, y: 0, width, height: data.page.height, scale: 1 },
  });
  fs.writeFileSync(path.join(outputDir, `${label}.png`), Buffer.from(screenshot.data, 'base64'));
  let interactions = null;
  if (width <= 700) {
    const check = await send('Runtime.evaluate', {
      returnByValue: true,
      expression: `(() => {
        const button = document.querySelector('#osat-mobile-map-toggle');
        const panel = document.querySelector('#osat-mobile-map-detail');
        if (!button || !panel) return null;
        const visible = () => getComputedStyle(panel).display !== 'none';
        const before = { expanded: button.getAttribute('aria-expanded'), visible: visible() };
        button.click();
        const opened = { expanded: button.getAttribute('aria-expanded'), visible: visible() };
        button.click();
        document.querySelector('[data-open-mode]')?.click();
        const deepLink = { expanded: button.getAttribute('aria-expanded'), visible: visible() };
        return { before, opened, deepLink };
      })()`,
    });
    interactions = check.result?.value ?? null;
  }
  console.log(JSON.stringify({ file: path.join(outputDir, `${label}.png`), ...data, interactions }));
  ws.close();
}

main().catch(error => { console.error(error); process.exitCode = 1; }).finally(async () => {
  browser.kill();
  await sleep(1000);
  const resolvedProfile = path.resolve(profile);
  const tempRoot = path.resolve(os.tmpdir()) + path.sep;
  if (!resolvedProfile.startsWith(tempRoot) || !path.basename(resolvedProfile).startsWith('semi-mobile-cdp-')) {
    throw new Error('Refusing to clean an unexpected Chrome profile path.');
  }
  for (let attempt = 0; attempt < 10; attempt++) {
    try { fs.rmSync(resolvedProfile, { recursive: true, force: true }); break; }
    catch (error) {
      if (attempt === 9) { console.error(`Temporary Chrome profile remains at ${resolvedProfile}: ${error.code}`); break; }
      await sleep(500);
    }
  }
});
