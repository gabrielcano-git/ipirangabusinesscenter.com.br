const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const sharp = require('sharp');
const manifest = require('../src/data/images.json');
const pages = require('../src/data/pages.json');
(async () => {
  let variants = 0;
  for (const [file, image] of Object.entries(manifest)) {
    assert(fs.existsSync(path.join('dist/assets', file)), 'Original deve continuar disponível');
    for (const variant of image.variants) {
      const actual = await sharp(path.join('dist', variant.src)).metadata();
      assert.equal(actual.format, 'webp');
      assert.equal(actual.width, variant.width);
      assert.equal(actual.height, variant.height);
      assert(actual.width <= image.width);
      assert(Math.abs(actual.height - actual.width * image.height / image.width) <= 1);
      variants++;
    }
  }
  for (const route of Object.keys(pages)) {
    const html = fs.readFileSync(path.join('dist', route === 'home' ? '' : route, 'index.html'), 'utf8');
    assert(html.includes('<style>'));
    assert(!html.includes('rel="stylesheet"'));
    assert(html.includes('src="/assets/site.js" defer'));
    for (const match of html.matchAll(/<img\b[^>]*srcset="([^"]+)"[^>]*>/g)) {
      const tag = match[0];
      for (const item of match[1].split(', ')) assert(fs.existsSync(path.join('dist', item.split(' ')[0])));
      assert(tag.includes('sizes="'));
      if (tag.includes('hero__image')) { assert(tag.includes('loading="eager"')); assert(tag.includes('fetchpriority="high"')); }
      else assert(tag.includes('loading="lazy"'));
    }
    if (route === 'home') {
      const preload = html.match(/<link rel="preload"[^>]+>/)[0];
      const hero = html.match(/<img class="hero__image"[^>]+>/)[0];
      assert.equal(preload.match(/imagesrcset="([^"]+)"/)[1], hero.match(/srcset="([^"]+)"/)[1]);
      assert.equal(preload.match(/imagesizes="([^"]+)"/)[1], hero.match(/sizes="([^"]+)"/)[1]);
      assert(preload.includes('media="(min-width: 48rem)"'));
    }
  }
  const hero = manifest['f02a459b12c27987.jpg'];
  const savings = hero.variants.map(variant => ({ width: variant.width, bytes: variant.bytes, reductionPercent: +(100 * (1 - variant.bytes / hero.originalBytes)).toFixed(1) }));
  const report = { measuredAt: new Date().toISOString(), scope: 'Tamanhos de arquivos; não são métricas de navegação ou Core Web Vitals', originalHeroBytes: hero.originalBytes, heroVariants: savings, photos: Object.keys(manifest).length, variants, cssBytes: fs.statSync('dist/assets/site.css').size, javascriptBytes: fs.statSync('dist/assets/site.js').size };
  fs.writeFileSync('validacao/core-web-vitals-assets.json', JSON.stringify(report, null, 2) + '\n');
  console.log(JSON.stringify(report, null, 2));
})().catch(error => { console.error(error); process.exitCode = 1; });
