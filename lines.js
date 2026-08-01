const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
  for (const [w, file] of [[1920,'index.html'],[1440,'index.html'],[1200,'index.html'],[1024,'index.html'],[1920,'en/index.html'],[1440,'en/index.html'],[1200,'en/index.html']]) {
    const p = await b.newPage({ viewport: { width: w, height: 900 } });
    await p.goto('file:///home/claude/tacoshermanos-website/' + file, { waitUntil: 'load' });
    await p.waitForTimeout(600);
    const r = await p.evaluate(() => {
      const el = document.querySelector('.hero__h1');
      const cs = getComputedStyle(el);
      const lh = parseFloat(cs.lineHeight);
      return { lines: Math.round(el.getBoundingClientRect().height / lh), text: el.textContent.trim().length };
    });
    console.log(`${file} @${w}px -> ${r.lines} line(s), ${r.text} chars`);
    await p.close();
  }
  await b.close();
})();
