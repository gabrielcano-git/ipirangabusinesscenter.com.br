const fs = require('node:fs');
const path = require('node:path');
const reports = require('../src/data/reports.json');
const metadata = JSON.parse(fs.readFileSync('output/pdf/manifest.json', 'utf8'));
const esc = value => String(value).replace(/[&<>"']/g, c => ({'&':'&amp;', '<':'&lt;', '>':'&gt;', '"':'&quot;', "'":'&#39;'}[c]));
const output = 'dist/relatorios';
fs.mkdirSync(path.join(output, 'pdf'), { recursive: true });
for (const report of reports) {
  const file = path.join('output/pdf', report.pdf);
  const bytes = fs.readFileSync(file);
  if (bytes.subarray(0, 5).toString() !== '%PDF-') throw new Error(`PDF inválido: ${file}`);
  fs.copyFileSync(file, path.join(output, 'pdf', report.pdf));
}
const cards = reports.map(report => {
  const info = metadata.find(item => item.pdf === report.pdf);
  if (!info) throw new Error(`Metadados ausentes: ${report.pdf}`);
  const href = `pdf/${report.pdf}`;
  return `<article class="report-card" id="${esc(report.slug)}"><span class="eyebrow">${esc(report.date)} · PDF · ${info.pages} páginas · ${(info.bytes / 1024 / 1024).toFixed(2).replace('.', ',')} MB</span><h2>${esc(report.title)}</h2><p>${esc(report.description)}</p><div class="reports__actions"><a class="button" href="${href}">Abrir PDF: ${esc(report.title)}</a><a class="button button--secondary" href="${href}" download>Baixar PDF: ${esc(report.title)}</a></div><details class="report-card__preview"><summary>Pré-visualizar ${esc(report.title)}</summary><p><a href="${href}">Abra o PDF diretamente se o navegador não exibir a prévia.</a></p><iframe title="PDF: ${esc(report.title)}" src="${href}" loading="lazy" width="100%" height="700"></iframe></details></article>`;
}).join('');
const html = `<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Relatórios do projeto | Ipiranga Business Center</title><meta name="description" content="Auditoria, relatório PageSpeed e comparação do site antigo com a nova versão do Ipiranga Business Center. Consulte ou baixe os documentos em PDF."><link rel="stylesheet" href="/assets/site.css"></head><body><header class="reports__header"><div class="container"><a href="/">Ipiranga Business Center</a><a href="/">Voltar ao site</a></div></header><main class="container section reports"><span class="eyebrow">Documentação para validação</span><h1>Relatórios do projeto</h1><p class="reports__intro">Consulte a auditoria original, o registro de PageSpeed e o comparativo da nova versão. Os PDFs preservam as evidências e as limitações de cada análise.</p><p class="reports__notice"><strong>Sobre os resultados:</strong> as consultas PageSpeed retornaram erro de cota. Os documentos não apresentam notas de desempenho concluídas nem aprovação dos Core Web Vitals.</p><nav class="reports__nav" aria-label="Escolher relatório">${reports.map(r => `<a href="#${esc(r.slug)}">${esc(r.title)}</a>`).join('')}</nav>${cards}</main><footer class="reports__footer container"><p>Ipiranga Business Center · Relatórios de 10/11/2026</p><a href="/">Voltar ao site</a></footer></body></html>`;
fs.writeFileSync(path.join(output, 'index.html'), html);
console.log(`Relatórios: índice e ${reports.length} PDFs incluídos em dist/relatorios/.`);
