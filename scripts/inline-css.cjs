const fs = require('node:fs');
const path = require('node:path');
const css = fs.readFileSync('dist/assets/site.css', 'utf8');
if (Buffer.byteLength(css) > 14 * 1024) throw new Error('CSS acima do limite de 14 KiB: revisar estratégia antes de incorporar.');
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (file.endsWith('.html')) {
      const html = fs.readFileSync(file, 'utf8').replace('<link rel="stylesheet" href="/assets/site.css">', `<style>${css}</style>`);
      fs.writeFileSync(file, html);
    }
  }
}
walk('dist');
console.log(`CSS incorporado: ${Buffer.byteLength(css)} bytes por página; nenhuma requisição de CSS para renderizar.`);
