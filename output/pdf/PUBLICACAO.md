# Publicação dos relatórios

Os três PDFs estão gerados, conferidos visualmente e integrados à área `dist/relatorios/`. A home e as páginas de negócio oferecem o acesso pelo rodapé.

Validações concluídas: build; verificação das páginas de negócio; PDFs originais e cópias idênticas; índice; links e pré-visualizações; preparação e validação no prefixo `/ipirangabusinesscenter.com.br`; requisições HTTP locais ao índice e aos três PDFs com status 200 e MIME correto.

A publicação remota não foi executada: o Git local não pôde criar `.git/index.lock` (Operation not permitted), e a integração GitHub rejeitou a gravação por exigir aprovação com a política da sessão definida como `never`.

Execute no checkout para enviar somente os arquivos desta entrega, sem incluir a pasta `skills/` ou as renderizações temporárias:

```sh
git add .gitignore README.md package.json scripts/build-site.cjs scripts/build.cjs scripts/serve.cjs scripts/validate-pages.cjs scripts/build-reports.cjs scripts/generate-report-pdfs.py scripts/requirements-pdf.txt scripts/validate-reports.cjs src/data/reports.json src/styles/site.scss output/pdf dist
git commit -m "Add PDF reports and GitHub Pages reports area"
git push origin main
```

O workflow Pages já executa `npm run build`, `npm run validate` e `npm run validate:pages`, agora incluindo os relatórios. Aguarde o deploy concluído e verifique:

- Índice: https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/relatorios/
- Auditoria: https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/relatorios/pdf/auditoria-site-antigo-2026-11-10.pdf
- PageSpeed: https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/relatorios/pdf/relatorio-pagespeed-2026-11-10.pdf
- Comparativo: https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/relatorios/pdf/comparativo-antigo-novo-2026-11-10.pdf

Essas URLs são os destinos configurados, não confirmação de publicação. Os arquivos Markdown e as evidências não são copiados ao site; os PDFs preservam links para as fontes no GitHub.
