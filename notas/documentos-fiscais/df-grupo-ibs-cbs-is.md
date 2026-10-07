---
título: Onde e como informar IBS, CBS e IS no XML da NF-e/NFC-e (leiaute)
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, seção 6 (Grupos B, BB, BC, C, I, UB, VB, VC e W03)
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# Leiaute: os campos de IBS, CBS e IS na NF-e

## A lógica em uma frase

O IBS/CBS de cada item mora num "armário" (`IBSCBS`, UB12) com **gavetas**:
uma para o IBS da UF (`gIBSUF`), uma para o IBS do Município (`gIBSMun`) e uma
para a CBS (`gCBS`). Dentro de cada gaveta há **subdivisões opcionais**
(diferimento, devolução de tributos, redução de alíquota) que só se abrem
quando o CST/cClassTrib permite (ver [[df-cst-cclasstrib]]). No fim, a nota
soma tudo nos **totais** (W03). IBS, CBS e IS são calculados **"por fora"**: o
valor deles se soma ao total da nota.

## Item: o grupo IBSCBS (UB12)

| Campo / grupo | ID | Conteúdo |
|---|---|---|
| `CST`, `cClassTrib` | UB13, UB14 | classificação do item |
| `indDoacao` | UB14a | "1" quando doação |
| `gIBSCBS` | UB15 | grupo principal (exigido conforme o CST) |
| `vBC` | UB16 | base de cálculo do IBS e da CBS |
| `gIBSUF` → `pIBSUF`, `vIBSUF` | UB17, UB18, UB35 | alíquota e valor do IBS da UF |
| `gIBSMun` → `pIBSMun`, `vIBSMun` | UB36, UB37, UB54 | alíquota e valor do IBS do Município |
| `vIBS` | UB54a | valor do IBS = `vIBSUF` + `vIBSMun` (menos `vCredPres` se o crédito presumido tiver "IndDeduzCredPres=1") |
| `gCBS` → `pCBS`, `vCBS` | UB55, UB56, UB67 | alíquota e valor da CBS |

Subgrupos repetidos em `gIBSUF`, `gIBSMun` e `gCBS`:

- `gDif` (`pDif`, `vDif`): **diferimento**, condicionado ao indicador
  "ind_gDif" da tabela de CST.
- `gDevTrib` (`pDevTrib`, `vDevTrib`): **devolução de tributos** ("cashback")
  em energia elétrica, água, esgoto, gás natural e outras hipóteses do
  regulamento (LC 214, art. 118).
- `gRed` (`pRedAliq`, `pAliqEfet`): **redução de alíquota** do cClassTrib; a
  alíquota efetiva já inclui o redutor de compra governamental, se houver.

Outros grupos do item:

- `gALCZFMCBS` (UB66a): **CBS com alíquota zero** em áreas incentivadas
  (ALC/ZFM, arts. 451 e 466 da LC 214), quando fornecedor e destinatário estão
  nessas áreas. `tpALCZFMCBS` = 1 (sem processo industrial aprovado na Suframa)
  ou 2 (com processo aprovado, informando `nProcSuframa`). Também informa a
  alíquota e o valor que valeriam fora da área (`pAliqEfetRegCBS`,
  `vTribRegCBS`).
- `gTribRegular` (UB68): como seria a tributação **se não cumprida** a condição
  suspensiva ou resolutiva (ex.: ZFM e ALC, suspensão), com `CSTReg`,
  `cClassTribReg` e alíquotas e valores "regulares".
- `gTribCompraGov` (UB82a): composição do IBS e da CBS em **compras
  governamentais**, com o valor que seria devido sem o art. 473 da LC 214.
- `gIBSCBSMono` (UB84): **monofásicos** (combustíveis), com grupos ad rem e
  ad valorem, retenção (`gMonoReten`), retido anteriormente (`gMonoRet`) e
  diferença de mistura de biocombustível (`gpBioDiferenca`); totais do item em
  `vTotIBSMonoItem` e `vTotCBSMonoItem`.
- `gTransfCred` (UB106): transferência de créditos (`vIBS`, `vCBS`).
- `gAjusteCompet` (UB112): ajuste de competência, com o período
  `competApur` (AAAA-MM).
- `gEstornoCred` (UB116): estorno de crédito (`vIBSEstCred`).
- `gCredPresOper` (UB120): **crédito presumido da operação**, com `vBCCredPres`,
  `cCredPres` e os grupos `gIBSCredPres` e `gCBSCredPres` (`pCredPres`,
  `vCredPres`, `vCredPresCondSus`). Exemplos de cCredPres na própria NT:
  1 aquisição de produtor rural não contribuinte; 2 transporte de TAC pessoa
  física não contribuinte; 3 aquisição de pessoa física para reciclagem;
  4 bens móveis de pessoa física não contribuinte para revenda (veículos,
  brechó); 5 regime opcional para cooperativa.
- `gCredPresIBSZFM` (UB131): crédito presumido de IBS sobre o saldo devedor na
  **ZFM** (art. 450, §1º, da LC 214), com `tpCredPresIBSZFM`.

Imposto Seletivo: grupo `IS` (UB01) com `CSTIS`, `cClassTribIS`, `vBCIS`,
`pIS`, quantidade (`uTrib`, `qTrib`) e `vIS`.

## Campos novos fora do grupo UB

| Campo | ID | Para quê |
|---|---|---|
| `dPrevEntrega` | B10a | data da previsão de entrega ou disponibilização do bem (não usar na NFC-e) |
| `cMunFGIBS` | B12a | município de consumo, fato gerador do IBS/CBS |
| `finNFe` | B25 | finalidade, agora com 5 = nota de crédito e 6 = nota de débito (ver [[df-finalidade-debito-credito]]) |
| `cIndOp` | B25d | código indicador do local da operação de fornecimento (obrigatório, por exemplo, em leilão judicial ou licitação) |
| `gCompraGov` | BB01 | compra governamental: `tpEnteGov` (União, Estado, DF, Município, consórcio público, Comitê Gestor do IBS), `pRedutor`, `tpOperGov`, `refDFeAnt` |
| `gPagAntecipado` | BC01 | NF-e de antecipação de pagamento referenciada (`refNFe`) |
| `ISUFEmit` | C22 | inscrição Suframa do emitente (CBS alíquota zero, arts. 451 e 466) |
| `tpCredPresIBSZFM` | I05k | classificação do crédito presumido na ZFM: 1 bens de consumo final (55%); 2 bens de capital (75%); 3 bens intermediários (90,25%); 4 informática e outros (100%) |
| `indBemMovelUsado` | I17c | bem móvel usado comprado de pessoa física não contribuinte ou MEI |
| `vItem` | VB01 | valor total do item |
| `DFeReferenciado` | VC01 | referência a item de outro documento (`chaveAcesso`, `nItem`) |

## Totais da nota (W03)

- `ISTot` (`vIS`) e `IBSCBSTot`, com `vBCIBSCBS`, `gIBS` (por UF e por
  Município: `vDif`, `vDevTrib`, `vIBSUF`, `vIBSMun`; e `vIBS`, `vCredPres`,
  `vCredPresCondSus`), `gCBS` (`vCBS` etc.), `gMono` e `gEstornoCred`. Cada
  total é a **soma** do campo correspondente dos itens.
- `vNFTot` (W60): valor total da NF-e com IBS, CBS e IS. A NT diz que o IS, o
  IBS e a CBS são "por fora", e seus valores devem ser adicionados ao total.

## ⏳ Em produção a partir de 03/11/2026 — NT 2025.002-RTC v1.52 (cronograma)

- Na **devolução**, o item devolvido passa a ser referenciado **exclusivamente**
  no grupo `DFeReferenciado` (regra VC02-14).
- Leiaute **reformulado da monofasia de combustíveis** (v1.50), já descrito
  acima, com produção em 03/11/2026.

## Ligações

- [[df-cst-cclasstrib]]: os códigos que liberam cada grupo.
- [[df-calculo-e-validacoes]]: as fórmulas de `vIBSUF`, `vCBS` e afins.
- [[df-valor-liquido-produto]]: campos de valor líquido (NT 2026.008).
- [[ibs-cbs-split-payment]]: o recolhimento que usa esses valores.
