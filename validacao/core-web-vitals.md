# Otimização com a skill core-web-vitals

Data: 10/11/2026. Aplicada à nova versão estática local, sem publicação.
Prévia desta execução: http://127.0.0.1:4183/.

## LCP — carregamento

- Identificadas no código fotos JPEG sem alternativas responsivas. Geradas 66 variantes WebP para 18 fotos, em até 320/640/960/1440 px, limitadas à resolução real do original.
- `srcset` e `sizes` permitem selecionar arquivos conforme largura de exibição e densidade da tela. Galeria continua oferecendo links aos originais.
- A foto da abertura é candidata a LCP, mas o elemento real não foi medido. Mantida em HTML inicial, com `loading="eager"` e `fetchpriority="high"`; preload responsivo somente no desktop, com os mesmos `srcset` e `sizes` da imagem. No celular, onde aparece depois do texto, não foi acrescentado preload.
- CSS compilado completo (9.854 bytes) incorporado ao HTML. Eliminada a requisição de stylesheet antes da renderização, sem depender de JavaScript para aplicar estilos. Há limite no build de 14 KiB para reavaliar a estratégia caso o CSS cresça. Isso aumenta cada HTML e reduz o aproveitamento de cache CSS entre páginas; a escolha foi proporcional ao tamanho atual.

Tamanhos reais da foto de abertura:

| Arquivo | Bytes | Redução frente ao JPEG original |
|---|---:|---:|
| JPEG original, 1440 px | 188.674 | — |
| WebP, 320 px | 8.796 | 95,3% |
| WebP, 640 px | 23.262 | 87,7% |
| WebP, 960 px | 41.048 | 78,2% |
| WebP, 1440 px | 80.166 | 57,5% |

Esses valores são tamanhos dos arquivos em disco. Não medem tempo de carregamento, não indicam qual variante cada navegador solicitará e não comprovam melhora visual/perceptual da compressão. Originais foram mantidos.

## INP — interações

JavaScript existente revisado: 1.467 bytes, carregamento com `defer`, sem framework de runtime, scripts de terceiros ou cálculos volumosos nos handlers. Menu e preparação de mensagem operam sobre poucos elementos. Não houve evidência estática de trabalho que justificasse workers, debounce ou divisão artificial das tarefas. Não foram medidos tempos dos handlers nem long tasks; INP permanece sem medição. Não foi instalado analytics ou transmissão de dados de visitantes.

## CLS — estabilidade

- Dimensões de fotos passam a corresponder aos metadados reais, substituindo dimensões genéricas.
- Hero fica posicionado dentro do container com altura mínima reservada, para a altura intrínseca da foto não alterar o tamanho da linha do grid durante o carregamento.
- Alturas de cards e galeria continuam reservadas no CSS incorporado; logo mantém dimensões explícitas.
- Reservado espaço para o retorno do formulário, reduzindo o risco de empurrar conteúdo quando a mensagem aparece.
- Mantidas fontes locais, ausência de embeds dinâmicos e respeito a movimento reduzido.

Essas correções tratam riscos observados no código; não representam CLS medido.

## Validação realizada

- `npm run build`: PASS, 16 rotas e pipeline de imagens/SCSS/Tailwind/CSS incorporado.
- `npm run validate`: PASS nas 16 rotas.
- `npm run validate:images`: PASS: arquivos e decodificação WebP, dimensões, proporções, ausência de ampliação, originais preservados, destinos dos srcsets, loading, prioridade, preload compatível e ausência de stylesheet externo no HTML.
- Sintaxe de `build.cjs` e `serve.cjs`: PASS.
- Servidor atualizado em 4183: verificados HTTP 200 das 16 rotas e Content-Type image/webp para uma variante, com resultado registrado em `core-web-vitals-http.json`.
- `node scripts/browser-check.cjs`: BLOCKED, Chromium falhou antes da navegação com MachPort/Permission denied. Registro em `core-web-vitals-browser.txt`. Nenhuma captura ou medição concluída.

## Limites

LCP, INP e CLS continuam **não medidos**. Não houve auditoria Lighthouse concluída nem PageSpeed da nova versão; ela está disponível apenas localmente. Não há dados de visitantes/CrUX desta versão. Não é possível afirmar que passou nos Core Web Vitals, atribuir notas ou quantificar ganho de tempo. Compressão, recortes e responsividade ainda precisam de conferência visual em navegador permitido. Hospedagem, compressão HTTP, cache/CDN e TTFB de produção não foram alterados.

## Fontes e artefatos

- `scripts/optimize-images.cjs`: preparação das variantes.
- `scripts/build.cjs`: HTML responsivo e preload.
- `scripts/inline-css.cjs`: incorporação do CSS compilado.
- `src/styles/site.scss`: reserva de espaço do hero e formulário.
- `scripts/serve.cjs`: MIME WebP e porta configurável via `PORT`.
- `scripts/validate-images.cjs`: verificações de imagens e HTML.
- `src/data/images.json`, `public/assets/optimized/` e `dist/`: artefatos gerados.
- `core-web-vitals-assets.json`: medições de tamanho.
