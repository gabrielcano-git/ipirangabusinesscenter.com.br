const fs = require('node:fs');
const path = require('node:path');
const assert = require('node:assert/strict');
const reports = require('../src/data/reports.json');
const metadata = JSON.parse(fs.readFileSync('output/pdf/manifest.json', 'utf8'));
const base = (process.env.PAGES_BASE_PATH || '').replace(/\/+$/, '');
const html = fs.readFileSync('dist/relatorios/index.html', 'utf8');
assert.equal((html.match(/<h1\b/g) || []).length, 1);
assert(html.includes('lang="pt-BR"'));
for (const report of reports) {
  const original = fs.readFileSync(path.join('output/pdf', report.pdf));
  const copy = fs.readFileSync(path.join('dist/relatorios/pdf', report.pdf));
  const info = metadata.find(item => item.pdf === report.pdf);
  assert(info && info.pages > 0);
  assert.equal(info.bytes, original.length, `Metadados desatualizados: ${report.pdf}`);
  assert(original.length > 1000);
  assert.equal(copy.subarray(0, 5).toString(), '%PDF-');
  assert(original.equals(copy), `PDF alterado ao copiar: ${report.pdf}`);
  assert(copy.subarray(-100).toString().includes('%%EOF'));
  assert(html.includes(`href="pdf/${report.pdf}"`));
  assert(html.includes(`src="pdf/${report.pdf}"`));
  assert(html.includes(`title="PDF: ${report.title.replace(/&/g, '&amp;')}"`));
}
for (const match of html.matchAll(/\b(?:href|src)="([^"]+)"/g)) {
  const href = match[1];
  if (href.startsWith('#')) { assert(html.includes(`id="${href.slice(1)}"`)); continue; }
  let file;
  if (href.startsWith('/')) {
    assert(href.startsWith(base + '/'), `Link fora do prefixo: ${href}`);
    file = path.join('dist', href.slice(base.length));
  } else file = path.join('dist/relatorios', href);
  if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
  assert(fs.existsSync(file), `Destino ausente: ${href}`);
}
const home = fs.readFileSync('dist/index.html', 'utf8');
assert(home.includes(`href="${base}/relatorios/"`), 'A home precisa tornar a área de relatórios descobrível');
console.log(`PASS: índice, ${reports.length} PDFs íntegros, links, prévias e acesso pelo rodapé; prefixo '${base}'.`);
