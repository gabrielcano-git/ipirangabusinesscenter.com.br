const fs = require('node:fs');
const path = require('node:path');
const input = process.env.PAGES_BASE_PATH || '';
if (input && (!/^\/[a-zA-Z0-9._/-]*$/.test(input) || input.includes('..') || input.includes('//'))) {
  throw new Error('PAGES_BASE_PATH deve ser um caminho absoluto seguro, por exemplo /ipirangabusinesscenter.com.br');
}
if (fs.readFileSync('dist/index.html', 'utf8').includes('<meta name="robots" content="noindex, nofollow">')) throw new Error('Execute npm run build antes de preparar Pages novamente.');
const base = input.replace(/\/+$/, '');
const prefix = value => value.startsWith('/') && !value.startsWith('//') ? base + value : value;
let count = 0;
function walk(dir) {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    const file = path.join(dir, entry.name);
    if (entry.isDirectory()) walk(file);
    else if (file.endsWith('.html')) {
      let html = fs.readFileSync(file, 'utf8');
      html = html.replace(/\b(href|src)="([^"]*)"/g, (_, name, value) => `${name}="${prefix(value)}"`);
      html = html.replace(/\b(srcset|imagesrcset)="([^"]*)"/g, (_, name, value) => `${name}="${value.split(', ').map(item => prefix(item)).join(', ')}"`);
      html = html.replace('<meta name="viewport"', '<meta name="robots" content="noindex, nofollow"><meta name="viewport"');
      fs.writeFileSync(file, html);
      count++;
    }
  }
}
walk('dist');
fs.writeFileSync('dist/.nojekyll', '');
fs.writeFileSync('dist/robots.txt', 'User-agent: *\nDisallow: /\n');
// A prévia mantém os canonicals de produção, mas não publica um sitemap de validação.
fs.rmSync('dist/sitemap.xml', { force: true });
console.log(`GitHub Pages: ${count} páginas preparadas em ${base || '/'}; prévia noindex.`);
