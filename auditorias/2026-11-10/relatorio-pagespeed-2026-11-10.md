# Relatório PageSpeed — Ipiranga Business Center

**Data:** 10/11/2026.  
**URL consultada:** https://www.ipirangabusinesscenter.com.br/  
**Escopo:** coleta de informações do PageSpeed Insights para mobile e desktop, com interpretação de Core Web Vitals conforme a skill `core-web-vitals`. Nenhuma correção, instalação de monitoramento ou alteração do site foi realizada.

## Resultado da coleta

Não foi possível obter resultados de desempenho. As duas consultas à API oficial do PageSpeed retornaram **HTTP 429**, com status **RESOURCE_EXHAUSTED** e motivo **RATE_LIMIT_EXCEEDED**. A mensagem informa cota diária excedida no serviço Google `pagespeedonline.googleapis.com`; os detalhes indicam `quota_limit_value: 0` para o projeto consumidor da requisição.

Esse erro pertence ao serviço de medição e não demonstra falha nem lentidão do site. Não é possível atribuir notas ou classificar os Core Web Vitals com essas respostas.

| Informação solicitada | Mobile | Desktop |
|---|---|---|
| Score de performance | Indisponível | Indisponível |
| Score de acessibilidade | Indisponível | Indisponível |
| Score de boas práticas | Indisponível | Indisponível |
| Score de SEO | Indisponível | Indisponível |
| LCP de laboratório | Não retornado | Não retornado |
| TBT de laboratório | Não retornado | Não retornado |
| CLS de laboratório | Não retornado | Não retornado |
| LCP de campo / CrUX | Não determinado | Não determinado |
| INP de campo / CrUX | Não determinado | Não determinado |
| CLS de campo / CrUX | Não determinado | Não determinado |
| Avaliação Core Web Vitals | Não determinada | Não determinada |
| Oportunidades e diagnósticos Lighthouse | Não retornados | Não retornados |

**Dados de campo:** a existência de amostra CrUX suficiente para esta URL ou para sua origem não pôde ser determinada. Não se deve interpretar a falha da consulta como ausência de visitantes ou ausência de dados no CrUX.

**Dados de laboratório:** nenhuma execução Lighthouse concluída foi obtida nesta coleta. TBT não substitui INP e não determina a aprovação dos Core Web Vitals.

## Tentativa pela interface pública

A página pública do PageSpeed foi obtida por HTTP, mas o HTML recebido continha apenas **“Running analysis”** e **“data loading”**, sem métricas. Isso registra o estado do HTML recebido, não uma execução concluída ou um erro definitivo da interface. A abertura pela ferramenta web também falhou. O ambiente já havia apresentado bloqueio ao iniciar o Chromium e indisponibilidade do navegador integrado na auditoria anterior; nenhuma nova captura visual foi produzida.

- [Abrir consulta mobile no PageSpeed](https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fwww.ipirangabusinesscenter.com.br%2F&form_factor=mobile)
- [Abrir consulta desktop no PageSpeed](https://pagespeed.web.dev/analysis?url=https%3A%2F%2Fwww.ipirangabusinesscenter.com.br%2F&form_factor=desktop)

Esses links abrem consultas; não são links para relatórios concluídos com notas verificadas.

## Referência de interpretação

Os limites abaixo vêm da skill solicitada e **não representam medições do site**. Para avaliação de campo, considerar o percentil 75 das visitas na janela informada pelo CrUX.

| Métrica | Bom | Precisa melhorar | Ruim |
|---|---|---|---|
| LCP — carregamento do maior elemento | ≤ 2,5 s | > 2,5 s até 4 s | > 4 s |
| INP — resposta às interações | ≤ 200 ms | > 200 ms até 500 ms | > 500 ms |
| CLS — estabilidade visual | ≤ 0,1 | > 0,1 até 0,25 | > 0,25 |

Não há base nesta coleta para apontar causas específicas de problemas, quantificar ganhos ou emitir recomendações de correção.

## Evidências preservadas

- [Resposta mobile](pagespeed-evidencias/mobile.json) e [cabeçalhos HTTP](pagespeed-evidencias/mobile-headers.txt).
- [Resposta desktop](pagespeed-evidencias/desktop.json) e [cabeçalhos HTTP](pagespeed-evidencias/desktop-headers.txt).
- [HTML da interface pública](pagespeed-evidencias/interface.html), [texto extraído](pagespeed-evidencias/interface-texto.txt) e [cabeçalhos](pagespeed-evidencias/interface-headers.txt).
- [Metadados da coleta, URL, categorias e horário UTC](pagespeed-evidencias/coleta.json).

**Conclusão:** coleta bloqueada pela cota do PageSpeed e sem resultado alternativo disponível neste ambiente. Este relatório documenta a indisponibilidade; não constitui uma avaliação medida de performance.
