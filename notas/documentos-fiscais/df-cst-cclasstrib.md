---
título: CST e cClassTrib do IBS/CBS e do Imposto Seletivo na NF-e
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, seções 2 e 3, Grupo UB (leiaute) e Anexos I a IV; IT 2025.002 v1.60, seções 01 e 06
vigencia: atual
texto-base: 2026-10-07
---

# CST e cClassTrib

## A lógica em uma frase

Cada item da NF-e carrega dois códigos que dizem **como** o IBS/CBS (e o IS)
incide sobre ele: o **CST** (situação tributária: tributado, reduzido,
diferido...) e o **cClassTrib** (o dispositivo exato da LC 214 que se aplica).
É como o endereço completo de uma regra: o CST diz a "rua" e o cClassTrib o
"número da casa". A partir desses códigos, a SEFAZ sabe quais grupos o item
**pode** ou **deve** preencher.

## Onde ficam no XML (Grupo UB)

| Campo | ID | O que é | Tamanho |
|---|---|---|---|
| `CST` | UB13 | Código de Situação Tributária do IBS e CBS (tabela CST do IBS/CBS) | 3 |
| `cClassTrib` | UB14 | Código de Classificação Tributária do IBS e CBS (tabela cClassTrib) | 6 |
| `CSTIS` | UB02 | CST do Imposto Seletivo | 3 |
| `cClassTribIS` | UB03 | Classificação tributária do Imposto Seletivo (tabela cClassTribIS) | 6 |
| `CSTReg` / `cClassTribReg` | UB69 / UB70 | CST e cClassTrib da **tributação regular** (como seria sem a condição suspensiva/resolutiva), dentro de `gTribRegular` | 3 / 6 |
| `cCredPres` | UB122 | Código de classificação do **crédito presumido** (tabela cCredPres, Anexo IV) | 2 |

## Como funcionam (seções 2 e 3)

- **Tipos básicos (seção 2):** a NT cria o arquivo "DFeTiposBasicos_v1.00.xsd",
  um modelo comum de campos de IBS e CBS para **todos** os documentos fiscais
  eletrônicos, não só a NF-e.
- **cClassTrib (seção 3):** "Cada código 'cClassTrib' corresponde a um
  dispositivo específico da Lei Complementar 214/2025". A tabela também traz
  **indicadores** que ligam CST e cClassTrib às regras de validação e à
  apuração assistida do IBS e da CBS. A tabela pode mudar com o regulamento ou
  com a apuração assistida.
- **Os indicadores comandam o preenchimento.** Exemplos do leiaute: o grupo de
  diferimento depende do indicador "ind_gDif" da tabela de CST; o de redução de
  alíquota, de "ind_gRed"; o de tributação regular, de "ind_gTribRegular" da
  tabela de cClassTrib. CST inexistente dá **rejeição 1020** (regra UB13-10);
  se o CST tem indicador que não permite o IBS/CBS ("ind_gIBSCBS = 0"),
  informar o grupo `gIBSCBS` dá **rejeição 1021** ("Grupo gIBSCBS informado
  indevidamente", regra UB13-20).

## Onde estão as tabelas

| Anexo da NT 2025.002-RTC | Situação |
|---|---|
| I — NCM do Imposto Seletivo | "Tabela a ser publicada" (⚠️ lacuna) |
| II — cClassTribIS | "Tabela a ser publicada" (⚠️ lacuna) |
| III — **cClassTrib** do IBS e da CBS, e a tabela de CST | fora do PDF; publicada pelo IT 2025.002 e capturada em 2026-10-08 do Portal dos DF-e; organizada em [[df-tabela-cclasstrib]] |
| IV — **cCredPres** | fora do PDF; capturada em 2026-10-08 do Portal dos DF-e (endereço do IT 2025.002 v1.60) e organizada em [[df-credito-presumido-ccredpres]]; as colunas de alíquota da planilha do IT seguem como lacuna |

Esta nota explica o mecanismo; os códigos estão em [[df-tabela-cclasstrib]]. Ela
diz **que códigos existem**, não qual usar numa operação concreta (isso depende de
enquadrar o produto ou serviço na LC 214). Os códigos de crédito presumido estão
em [[df-credito-presumido-ccredpres]] (atenção: o exemplo "5 - Regime opcional
para cooperativa" do leiaute da NT não confere com a tabela atual).

## Ligações

- [[df-grupo-ibs-cbs-is]]: os grupos que cada código libera ou exige.
- [[df-calculo-e-validacoes]]: regras que dependem dos indicadores.
- [[ibs-cbs-cadastro-documento-fiscal]]: o documento fiscal na LC 214.
