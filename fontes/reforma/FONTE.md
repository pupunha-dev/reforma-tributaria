# Fontes — domínio reforma

| Arquivo | Ato | Origem (URL) | Capturado em | Observação |
|---|---|---|---|---|
| lc-214-2025-texto-compilado.pdf | LC 214/2025 (compilada, já com a LC 227) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm | 2026-08-24 | Impressão do navegador. |
| lc-227-2026.pdf | LC 227/2026 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm | 2026-08-24 | PDF **sem camada de texto** (OCR foi usado na elaboração das notas). |
| texto/lc-214-2025.txt | LC 214/2025 | (extraído do PDF acima) | 2026-10-06 | `pdftotext -enc UTF-8`. |
| texto/lc-214-2025-planalto.htm | LC 214/2025 (HTML compilado oficial) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp214compilado.htm | 2026-10-06 | Convertido de windows-1252 para UTF-8. Fonte das tabelas dos Anexos XVIII a XXIII (Simples Nacional a partir de 2027). |
| texto/lc-227-2026-planalto.htm | LC 227/2026 (HTML oficial) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp227.htm | 2026-10-06 | Convertido de windows-1252 para UTF-8. **Texto pesquisável da LC 227**, que o PDF não tem. |
| decreto-12955-2026-regulamento-cbs.pdf | Decreto nº 12.955/2026 — Regulamento da CBS | https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/d12955.htm | 2026-10-08 | Impressão do navegador (296 páginas), fornecida pelo usuário. Compilado com o **Decreto nº 13.075/2026** (arts. 105, 115 e 619). Publicação: DOU de 30/04/2026. |
| texto/decreto-12955-2026-planalto.htm | idem (HTML compilado oficial) | mesma URL | 2026-10-08 | Convertido de windows-1252 para UTF-8. **Fonte do texto da CBS**: o `<strike>` marca o texto superado (3 trechos), excluído do texto por artigo. 620 artigos + Anexo I (taxas de depreciação, art. 48, § 1º) e demais anexos. |
| res-cgibs-6-2026-regulamento-ibs.pdf | Resolução CGIBS nº 6/2026 — Regulamento do IBS | fornecido pelo usuário (Comitê Gestor do IBS) | 2026-10-08 | 252 páginas, gerado em 30/04/2026. **Texto original**: alterações posteriores do CGIBS não verificadas. A data de publicação não consta do texto. 617 artigos + Anexo I. |
| texto/res-cgibs-6-2026.txt | idem | (extraído do PDF acima) | 2026-10-08 | `pdftotext -enc UTF-8`; parágrafos longos (o Word junta as linhas). Começa com um sumário. |
| texto/decreto-12955-2026-artigos.txt e texto/res-cgibs-6-2026-artigos.txt | os dois regulamentos | gerados por `scripts/mapa_regulamento.py` | 2026-10-08 | **Uma linha por artigo**, com Livro/Título/Capítulo antes de cada mudança. Para ler um artigo, procure a linha que começa com "Art. N". |
| texto/regulamentos-mapa-cabecalho.md | — | escrito à mão | 2026-10-08 | Cabeçalho de `notas/reforma/_mapa-regulamentos.md` (cláusulas de vigência literais). |

## Regulamentos: relação com a lei

Cada artigo dos regulamentos cita, entre parênteses, o artigo da LC 214 que
regulamenta. `scripts/mapa_regulamento.py` usa essas citações para gerar
`notas/reforma/_mapa-regulamentos.md` e o bloco "Regulamentação" de cada nota.
Nenhum artigo dos dois regulamentos cita a LC 227/2026. Divergência conhecida
entre os dois: o adiamento para 2027 da inscrição e da emissão de documento por
pessoa física e produtor rural PF existe só na CBS (Decreto 13.075/2026).

