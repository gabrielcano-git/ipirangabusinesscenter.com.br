const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const routes = Object.keys(require('../src/data/pages.json'));
const base = (process.env.PAGES_BASE_PATH || '').replace(/\/+$/, '');
let checked = 0;
function check(value) {
  if (!value.startsWith('/') || value.startsWith('//')) return;
  assert(value.startsWith(base + '/'), `Link fora do prefixo: ${value}`);
  let file = path.join('dist', value.slice(base.length).split(/[?#]/)[0]);
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  assert(fs.existsSync(file), `Destino ausente: ${value}`);
  checked++;
}
for (const route of routes) {
  const html = fs.readFileSync(path.join('dist', route === 'home' ? '' : route, 'index.html'), 'utf8');
  assert(!/<meta\b[^>]*name="robots"[^>]*content="[^"]*(?:noindex|nofollow)/i.test(html));
  for (const match of html.matchAll(/\b(?:href|src)="([^"]*)"/g)) check(match[1]);
  for (const match of html.matchAll(/\b(?:srcset|imagesrcset)="([^"]*)"/g)) {
    for (const item of match[1].split(', ')) check(item.split(' ')[0]);
  }
}
assert(fs.existsSync('dist/.nojekyll'));
assert(!fs.existsSync('dist/CNAME'), 'A prévia não deve alterar o domínio de produção');
assert(!fs.existsSync('dist/sitemap.xml'));
assert.equal(fs.readFileSync('dist/robots.txt', 'utf8'), 'User-agent: *\nAllow: /\n');
for (const entry of fs.readdirSync('dist')) assert(!['auditorias', 'validacao', 'scripts', 'src', 'skills', '.git'].includes(entry));
console.log(`PASS: ${routes.length} rotas e ${checked} destinos com prefixo '${base}', rastreamento permitido e somente arquivos do site.`);
