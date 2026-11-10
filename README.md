# Ipiranga Business Center — nova versão

Site estático gerado a partir do conteúdo público coletado em 10/11/2026 e do `DESIGN.md`.

```sh
npm ci --cache /private/tmp/ibc-npm-cache
npm run build
npm start
```

Abra **http://127.0.0.1:4173/**. Use esse endereço exato: há outro servidor local respondendo em IPv6 na porta 4173.

- `scripts/build.cjs`: componentes reutilizáveis (botões e ícones, cards e formulário, cabeçalho e rodapé, templates).
- `src/styles/site.scss`: tokens e componentes BEM; Tailwind fornece utilitários de layout.
- `src/data/pages.json`: blocos de conteúdo e referências das imagens originais.
- `public/assets/`: imagens locais e melhoria progressiva em JavaScript.
- `dist/`: **somente o site publicável**, com 16 rotas, CSS compilado, JS, imagens, robots e sitemap. Nenhum relatório acompanha a pasta publicada.
- `validacao/`: verificações e limitações da entrega.

`npm run validate` verifica os arquivos de todas as rotas e seus destinos internos. Com o servidor ativo, `node scripts/browser-check.cjs` verifica páginas em 320, 390, 768 e 1440 px, menu móvel e capturas. O ambiente atual bloqueia a inicialização dos navegadores.

A hospedagem precisa servir `/<rota>/index.html` para `/<rota>` e `/<rota>/`. Canonicals conservam as URLs públicas originais. Não foi feita publicação nem alteração no Wix.

Os formulários preparam a mensagem no WhatsApp e mostram um link para revisão e envio. Não há envio automático, persistência, servidor de formulário nem confirmação fictícia. Contatos por telefone, WhatsApp e e-mail continuam disponíveis. Galerias usam links para ampliar os arquivos originais sem depender de JavaScript.

A divergência de capacidade do auditório (36/40) está explícita na página, aguardando confirmação do responsável. O histórico “mais de 6 anos” foi preservado; 2016 permanece como início do copyright, sem inferir data de fundação.

## Core Web Vitals

O build também gera fotos WebP responsivas, corrige suas dimensões e incorpora o CSS compilado ao HTML. Os JPEGs originais permanecem disponíveis na galeria. As variantes e o manifesto de imagens são derivados automaticamente; altere os originais ou os scripts, sem editar `dist/` manualmente.

```sh
npm run validate:images
PORT=4183 npm start
```

Prévia da execução de otimização: **http://127.0.0.1:4183/**. A porta alternativa evita o processo antigo na 4173. Evidências e limitações em `validacao/core-web-vitals.md`; LCP, INP e CLS ainda não foram medidos em navegador.

## Publicação de validação no GitHub Pages

O workflow `.github/workflows/pages.yml` executa o build e as verificações antes de publicar **somente `dist/`**. Publicações ocorrem em pushes para `main` ou manualmente em Actions → “Publicar prévia no GitHub Pages” → “Run workflow”.

No repositório de destino, selecione **Settings → Pages → Build and deployment → Source → GitHub Actions**. A URL definitiva aparece no ambiente `github-pages` e no resumo da execução concluída. Não é necessário configurar domínio personalizado, DNS, `CNAME` ou secrets de deploy.

A ação `configure-pages` informa automaticamente o subdiretório da prévia. O script `prepare-pages.cjs` ajusta navegação, fotos, srcsets, preload e JavaScript para esse prefixo, adiciona `.nojekyll` e permite o rastreamento, sem diretivas `noindex` ou `nofollow`. A prévia mantém os canonicals de produção e não publica sitemap; isso não constitui controle de acesso ao site público.

Para reproduzir a preparação de um site de projeto:

```sh
npm run build
npm run validate
npm run validate:images
PAGES_BASE_PATH=/ipirangabusinesscenter.com.br npm run prepare:pages
PAGES_BASE_PATH=/ipirangabusinesscenter.com.br npm run validate:pages
```

Execute `npm run build` novamente para restaurar a versão local sem prefixo. O build usa a pasta temporária do sistema e funciona em macOS e Linux. Antes de enviar todo o histórico a um novo repositório público, confira o conteúdo versionado: auditorias e evidências não entram no site, mas podem estar no histórico Git enviado.

## Relatórios em PDF no Pages

A rota **`/relatorios/`**, acessível pelo link “Relatórios do projeto” no rodapé, oferece os três documentos em PDF, com abertura direta, download e pré-visualização opcional no navegador:

- Auditoria do site antigo;
- Relatório PageSpeed;
- Comparativo do site antigo com a nova versão, com capturas reais.

Na publicação de projeto, a área fica em `https://gabrielcano-git.github.io/ipirangabusinesscenter.com.br/relatorios/`. Esse endereço só passa a oferecer os arquivos após o deploy desta alteração.

Os documentos são registrados em `src/data/reports.json`. As versões finais ficam em `output/pdf/`, com metadados em `output/pdf/manifest.json`. O build copia somente os PDFs registrados para `dist/relatorios/pdf/` e gera o índice; não publica a árvore completa de auditorias, evidências ou arquivos de trabalho. As referências de evidência dentro dos PDFs apontam para os arquivos no repositório GitHub.

`npm run validate` e `npm run validate:pages` conferem os PDFs, sua assinatura, a integridade das cópias, os links e a entrada pelo rodapé. O workflow existente já executa esses comandos. A publicação não exige Python ou instalação de bibliotecas PDF, porque usa os documentos finais versionados.

Para atualizar o conteúdo dos PDFs, use Python com as dependências de `scripts/requirements-pdf.txt` e execute `python scripts/generate-report-pdfs.py`. O script de autoria usa Arial instalada no macOS; em outro sistema, configure `REPORT_FONT_DIR` com as fontes indicadas no script. Depois confira as páginas renderizadas e execute `npm run build`, `npm run validate` e as verificações de Pages antes de publicar.
