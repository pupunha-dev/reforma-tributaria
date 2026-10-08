# Fontes — domínio simples-nacional

| Arquivo | Ato | Origem (URL) | Capturado em | Última alteração vista no texto | Observação |
|---|---|---|---|---|---|
| lc-123-2006-texto-compilado.pdf | LC 123/2006 | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm | 2026-10-06 | LC 227/2026 | Impressão do navegador. A redação superada perde o risco na extração; "Produção de efeitos" não traz data (ver `notas/simples-nacional/_mapa-vigencia.md`). |
| texto/lc-123-2006-planalto.htm | LC 123/2006 (HTML oficial) | https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm | 2026-10-06 | LC 227/2026 | Convertido de windows-1252 para UTF-8. **Fonte de verdade da vigência:** o texto já superado vem em `<strike>`, e cada link "Produção de efeitos" aponta para o inciso exato do art. 544 da LC 214 (`Lcp214.htm#art544-2`, `-3`, `-5`). **Ainda não incorpora o art. 169 da LC 227** (efeitos em 2027): ver `fontes/reforma/texto/lc-227-2026-planalto.htm`. |
| resolucao-cgsn-140-2018-multivigente.pdf | Res. CGSN 140/2018 (visão multivigente) | https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/imprimir/92278/visao/multivigente | 2026-10-07 | Res. CGSN 191/2026 (alterações vigentes) e Res. CGSN 190/2026 (modificações previstas para 01/01/2027) | Portal Normas da Receita. Mostra redações antigas e vigentes (`date_range`) e marca o que muda ("Vide modificação prevista para", "Vide dispositivo a ser incluído em"), **sem** o texto futuro, que fica na Res. 190/191. Os **Anexos** são PDFs separados no portal e **não** estão aqui. A impressão às vezes corta uma marca ao meio; o `vigencia_receita.py` trata isso. |
| resolucao-cgsn-190-2026-dou.pdf | Res. CGSN 190/2026 (altera a Res. 140: IBS/CBS no Simples, Anexos I–V para 2027–2028, Anexo XIII com valores fixos do MEI 2027–2028) | https://www.in.gov.br/web/dou/-/resolucao-cgsn-n-190-de-4-de-agosto-de-2026-724454118 | 2026-10-06 | — (ato alterador; DOU de 10/08/2026, ed. 149-A extra) | Efeitos a partir de 01/01/2027 (art. 9º). A impressão do DOU **repete os arts. 1º a 6º duas vezes**: use só a primeira ocorrência. |
| resolucao-cgsn-191-2026-dou.pdf | Res. CGSN 191/2026 (altera a Res. 140: NFS-e de padrão nacional obrigatória para ME/EPP, arts. 59 e 79; revoga a Res. 189/2026) | https://www.in.gov.br/en/web/dou/-/resolucao-cgsn-n-191-de-4-de-agosto-de-2026-724399487 | 2026-10-06 | — (ato alterador; DOU de 10/08/2026, ed. 149-A extra) | Efeitos: art. 1º a partir de 01/11/2026; demais artigos, imediatamente (art. 3º). |
| resolucao-cgsn-140-2018-anexo-vi.pdf | Res. CGSN 140/2018, **Anexo VI** (CNAEs impeditivos ao Simples, art. 8º, §1º) | Portal da Receita (PDF separado da visão multivigente); fornecido pelo usuário | 2026-10-08 | Res. CGSN 143/2018 (vigência 01/01/2019) | 4 páginas, 101 subclasses CNAE. Metadado do PDF: criado em 09/01/2019. A Res. 190 não altera o Anexo VI. |
| resolucao-cgsn-140-2018-anexo-xi.pdf | Res. CGSN 140/2018, **Anexo XI** (ocupações permitidas ao MEI, Tabelas A e B, arts. 100 e 101) | idem | 2026-10-08 | Res. CGSN 182/2025 (vigência 01/10/2025) | 43 páginas, 470 ocupações (467 na Tabela A, 4 na B). Metadado: criado em 16/10/2025, depois da Res. 182, o que indica a versão atual. "REPARADOR(A) INDEPENDENTE" aparece 2 vezes (CNAEs 3314-7/01 e 3314-7/10), como no PDF. |
| solucao-consulta-cosit-71-2026.pdf | Solução de Consulta Cosit nº 71, de 24/04/2026 (Simples: administração de garantias na locação de imóveis) | Receita Federal; fornecido pelo usuário | 2026-10-08 | — (ato interpretativo) | 14 páginas. Interpreta a LC 123 e a Res. 140 para os fatos da consulente (IN RFB 2.058/2021); não cria regra. Cita a SC Cosit 66/2013, que não está nas fontes. |

## Texto extraído

- `texto/lc-123-2006.txt`: `pdftotext -enc UTF-8`, sem `-layout`.
- `texto/lc-123-2006-esqueleto.md`: `scripts/esqueleto.py --ruido "^Lcp 123$"`.
- `texto/lc-123-2006-planalto.htm`: HTML oficial, para conferir o que está riscado e o destino de cada link "Produção de efeitos".
- `texto/resolucao-cgsn-140-2018.txt`: `pdftotext -enc UTF-8` da visão multivigente; mapa em `notas/simples-nacional/_mapa-vigencia-res140.md` (`scripts/vigencia_receita.py`).
- `texto/resolucao-cgsn-140-2018-anexo-vi.md` e `texto/resolucao-cgsn-140-2018-anexo-xi.md`: tabelas extraídas com `scripts/tabela_pdf.py` (detecção de tabelas do pymupdf), conferidas contra o texto corrido (`.txt`, `-layout.txt`, `pdftotext`): mesmo número de CNAEs no Anexo VI e o mesmo multiconjunto de CNAEs no Anexo XI.
- `texto/solucao-consulta-cosit-71-2026.txt` e `-layout.txt`: `pdftotext -enc UTF-8`.
- `texto/resolucao-cgsn-190-2026.txt`, `texto/resolucao-cgsn-191-2026.txt`: `pdftotext -enc UTF-8`. São atos alteradores da Res. 140: não têm esqueleto próprio; entram no mapa de vigência e, na fase B, nos blocos ⏳ das notas.

## Relação entre as fontes

A LC 123 é a lei; a Res. CGSN 140 a regulamenta; as Res. CGSN 190 e 191
alteram a 140. A 140 multivigente (capturada em 2026-10-07) já incorpora a 191 e
marca as modificações da 190 previstas para 01/01/2027, mas não traz o
texto futuro: as 190/191 continuam sendo a fonte das redações futuras.
