# Fontes — domínio documentos-fiscais

Notas Técnicas (NT) do Projeto NF-e (Receita Federal + Secretarias de Fazenda/ENCAT),
fornecidas pelo usuário em 2026-10-06 (antes em `fontes/simples-nacional/`) e
capturadas neste domínio em 2026-10-07. Origem pública: Portal Nacional da
NF-e (www.nfe.fazenda.gov.br), aba "Documentos".

| Arquivo | NT | Assunto | Versão | Publicação | Capturado em | Observação |
|---|---|---|---|---|---|---|
| nt-2025-002-rtc-v1.52.pdf | NT 2025.002-RTC | Reforma Tributária do Consumo — adequações da NF-e/NFC-e (grupos IBS/CBS/IS, regras de validação, eventos) | 1.52 | setembro/2026 | 2026-10-07 | 94 páginas. Anexos I (NCM do IS) e II (cClassTribIS): "tabela a ser publicada". Anexos III (**cClassTrib**) e IV (**cCredPres**): fora do PDF; publicadas pelo IT 2025.002 e capturadas do Portal dos DF-e (seções abaixo). A seção 9 (DANFE) diz "em estudo", superada pela NT 2026.010. |
| nt-2026-002-v1.11.pdf | NT 2026.002 | Vendas presenciais e não presenciais, autorização com alerta, DANFE Simplificado Tipo 2 | 1.11 | setembro/2026 | 2026-10-07 | Cronograma por versão (1.00 a 1.11). |
| nt-2026-007-v1.10.pdf | NT 2026.007 | Emissão por contribuinte exclusivo do IBS/CBS | 1.10 | setembro/2026 | 2026-10-07 | Produção em 03/11/2026. |
| nt-2026-008-v1.00.pdf | NT 2026.008 | Valor líquido do produto; ICMS previsto no pagamento antecipado | 1.00 | setembro/2026 | 2026-10-07 | Campos: produção em 03/11/2026; parte das regras de validação: produção em 01/03/2027. |
| nt-2026-010-v1.00.pdf | NT 2026.010 | DANFE da reforma tributária (leiaute de impressão) | 1.00 | outubro/2026 | 2026-10-07 | Produção em 01/12/2026. |

## Informe Técnico 2025.002 (tabelas de classificação do IBS e da CBS)

Fornecidos pelo usuário em 2026-10-08 (pasta `fontes/novos-analise/`). O IT
divulga e mantém as tabelas cClassTrib, CST e cCredPres e as alíquotas padrão, e
dá os endereços oficiais das tabelas online (seção 06).

| Arquivo | Documento | Versão | Publicação | Capturado em | Observação |
|---|---|---|---|---|---|
| it-2025-002-v1.60.pdf | IT 2025.002 — Tabelas de Classificação do IBS e da CBS | 1.60 | 22/06/2026 | 2026-10-08 | **Versão usada nas notas.** 12 páginas. Seções: objetivo, cClassTrib, CST, cCredPres, alíquotas padrão 2026–2029, tabelas online, histórico de alterações (v1.10 a v1.60). Cita o Decreto 12.955/2026 (Regulamento da CBS) e a Res. CGIBS 6/2026 (Regulamento do IBS), que **não estão nas fontes**. 1 trecho riscado ("ind_gMonoDif", excluído). |
| it-2025-002-v1.31.pdf | idem | 1.31 | 15/12/2025 | 2026-10-08 | **Superada** pela v1.60; guardada para histórico. 8 linhas riscadas. |

Texto em `texto/`: `<it>-vigente.txt` e `<it>-riscado.md` (`scripts/extrair_nt.py`),
mais `.txt` e `-layout.txt` (`pdftotext`). Use só o `-vigente.txt`.

## Tabelas online do Portal dos DF-e (SVRS)

Capturadas em **2026-10-08** pelos endereços do IT 2025.002 v1.60 (seção 06), com
`scripts/tabelas_svrs.py`. Acesso público, sem login. A equipe confirmou em
2026-10-08 que a fonte é a recomendada pelo site da Receita.

| Arquivo (em `texto/`) | Origem | Conteúdo |
|---|---|---|
| cclasstrib-svrs.json | https://dfe-portal.svrs.rs.gov.br/DFE/TabelaClassificacaoTributaria (redireciona para `/DFE/ClassificacaoTributaria`; mesmo JSON de `/Cff/ClassificacaoTributaria`) | 18 CST e 173 cClassTrib, completos: indicadores, tpRBSN, texto dos regulamentos da CBS e do IBS (165 códigos), listas NCM/NBS de 35 códigos. Os dados vêm como JSON embutido na página |
| cclasstrib-svrs.md | idem | as mesmas tabelas em Markdown (`tabelas_svrs.py cclasstrib`) |
| ccredpres-svrs.json / .md | https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido | 13 códigos cCredPres: apropriação (DF-e ou evento), dedução, declaração de pagamento, documentos e vigência por tributo (`tabelas_svrs.py ccredpres`). A página é HTML; as colunas de alíquota e percentual do IT **não** aparecem nela |

A tabela cClassTrib do portal tem itens publicados em 01/10/2026, **depois** do IT
v1.60. A tabela **muda**: repetir a captura quando a NT, o IT ou o regulamento
mudar, comparar com o arquivo anterior e regerar a nota com
`python scripts/tabelas_svrs.py nota notas/documentos-fiscais/df-tabela-cclasstrib.md`.
Códigos de 6 dígitos citados nas notas são conferidos com
`python scripts/tabelas_svrs.py conferir <nota.md>`.

## Texto extraído

**Atenção: as NTs têm texto riscado.** A redação superada aparece com um traço
sobre o texto (em vermelho, com marca amarela), como o `<strike>` do Planalto. O
`pdftotext` **não** distingue isso: nos arquivos `.txt` e `-layout.txt` o texto
riscado aparece misturado ao vigente (ex.: na NT 2025.002, a data "03/08/2026"
de produção da regra UB12-10 está riscada; a redação vigente diz "implementação
futura para produção").

Para cada NT, em `texto/`:

- `<nt>-vigente.txt` — **fonte principal das notas.** Gerado por
  `scripts/extrair_nt.py` (requer `pip install pymupdf`): só o texto não riscado,
  uma linha visual por linha, colunas separadas por " | ".
- `<nt>-riscado.md` — lista, por página, do que está riscado (auditoria; **não**
  usar nas notas).
- `<nt>.txt` (`pdftotext -enc UTF-8`) e `<nt>-layout.txt` (`pdftotext -layout`):
  apoio de leitura; contêm o texto riscado misturado. Na `.txt` alguns códigos
  perdem o hífen na quebra de linha (ex.: "N1250").

Linhas riscadas por NT (2026-10-07): 2025.002-RTC 32; 2026.002 52; 2026.007 5;
2026.008 34; 2026.010 0.

Identificadores técnicos (tags, códigos de regra, códigos de rejeição) são
conferidos com `scripts/conferir_tags.py` contra os `-vigente.txt`.

## Hierarquia

A NT diz **como preencher e validar** o documento fiscal; não cria nem altera
tributo. Lei (LC 214/2025, LC 123/2006) > resolução/ato infralegal > NT.
