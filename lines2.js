const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [w, file] of [[1920,'index.html'],[1440,'index.html'],[1100,'index.html'],[1920,'en/index.html'],[1440,'en/index.html']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto('file:///home/claude/tacoshermanos-website/' + file, { waitUntil: 'load' });
    await p.waitForTimeout(500);
    const r = await p.evaluate(() => {
      const o = {};
      for (const sel of ['.hero__kicker', '.hero__h1']) {
        const el = document.querySelector(sel);
        o[sel] = Math.round(el.getBoundingClientRect().height / parseFloat(getComputedStyle(el).lineHeight));
      }
      return o;
    });
    console.log(`${file} @${w} -> H1 ${r['.hero__kicker']} line(s), sub ${r['.hero__h1']} line(s)`);
    await p.close();
  }
  await b.close();
})();
