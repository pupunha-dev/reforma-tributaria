# Fontes — domínio documentos-fiscais

Notas Técnicas (NT) do Projeto NF-e (Receita Federal + Secretarias de Fazenda/ENCAT),
fornecidas pelo usuário em 2026-10-06 (antes em `fontes/simples-nacional/`) e
capturadas neste domínio em 2026-10-07. Origem pública: Portal Nacional da
NF-e (www.nfe.fazenda.gov.br), aba "Documentos".

| Arquivo | NT | Assunto | Versão | Publicação | Capturado em | Observação |
|---|---|---|---|---|---|---|
| nt-2025-002-rtc-v1.52.pdf | NT 2025.002-RTC | Reforma Tributária do Consumo — adequações da NF-e/NFC-e (grupos IBS/CBS/IS, regras de validação, eventos) | 1.52 | setembro/2026 | 2026-10-07 | 94 páginas. Anexos I (NCM do IS) e II (cClassTribIS): "tabela a ser publicada". Anexos III (**cClassTrib**) e IV (**cCredPres**): tabelas publicadas **só no Portal NF-e**, fora do PDF → **lacuna**. A seção 9 (DANFE) diz "em estudo", superada pela NT 2026.010. |
| nt-2026-002-v1.11.pdf | NT 2026.002 | Vendas presenciais e não presenciais, autorização com alerta, DANFE Simplificado Tipo 2 | 1.11 | setembro/2026 | 2026-10-07 | Cronograma por versão (1.00 a 1.11). |
| nt-2026-007-v1.10.pdf | NT 2026.007 | Emissão por contribuinte exclusivo do IBS/CBS | 1.10 | setembro/2026 | 2026-10-07 | Produção em 03/11/2026. |
| nt-2026-008-v1.00.pdf | NT 2026.008 | Valor líquido do produto; ICMS previsto no pagamento antecipado | 1.00 | setembro/2026 | 2026-10-07 | Campos: produção em 03/11/2026; parte das regras de validação: produção em 01/03/2027. |
| nt-2026-010-v1.00.pdf | NT 2026.010 | DANFE da reforma tributária (leiaute de impressão) | 1.00 | outubro/2026 | 2026-10-07 | Produção em 01/12/2026. |

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
