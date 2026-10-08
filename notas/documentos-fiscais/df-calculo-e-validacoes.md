---
título: Cálculo do IBS/CBS/IS na NF-e e regras de validação da SEFAZ
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, seções 5 e 7 (Grupos UB, VB e W03); IT 2025.002 v1.60, seção 05 (alíquotas padrão)
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# Cálculo e regras de validação

## A lógica em uma frase

A SEFAZ **refaz a conta** de cada item antes de autorizar a nota: pega a base,
aplica a alíquota (ou a alíquota efetiva, se houver redução), desconta
diferimento e devolução, e compara com o valor informado, aceitando uma
diferença de **0,01** para mais ou para menos. Se a conta não fecha, a nota é
**rejeitada** com um código de 4 dígitos. É como o caixa do supermercado que
confere o troco: errou por mais de um centavo, volta.

## Códigos de status com 4 posições (seção 5)

O código de status de resposta (`cStat`) foi ampliado para **4 posições**, e
essa nova faixa é usada para as rejeições **exclusivas dos novos tributos** (IBS,
CBS, IS). O protocolo de autorização pode ter 15 ou 17 posições; segundo a NT,
"atualmente, somente a SEFAZ-SP irá adotar o protocolo com 17 posições para a
NFC-e".

## Alíquotas que a SEFAZ aceita

| Tributo | Regra | 2025 e 2026 | 2027 e 2028 | Rejeição |
|---|---|---|---|---|
| IBS da UF (`pIBSUF`) | UB18-10 | 0,1% (art. 343 da LC 214) | 0,05% (art. 344) | 1026 |
| IBS do Município (`pIBSMun`) | UB37-10 | 0% (art. 343) | 0,05% (art. 344) | 1036 |
| CBS (`pCBS`) | UB56-10 / UB56-20 | 0,9% (art. 346) | a "alíquota vigente para o período conforme legislação" | 1037 |

- **Exceção 1 das três regras:** "Se o cClassTrib possuir indicador de
  Tributação Regular (`ind_gTribRegular` = 1)", a alíquota informada (`pIBSUF`,
  `pIBSMun`, `pCBS`) deve ser **zero**. Atenção ao sentido: é o código **com** o
  indicador ligado, que leva a tributação "como seria sem a condição" para o
  grupo `gTribRegular` (ver [[df-cst-cclasstrib]]); não se trata de código
  isento ou imune.
- As regras do IBS da UF e do Município (UB18-10 e UB37-10) não se aplicam à
  devolução (finalidade 4) nem às notas de crédito dos tipos 03, 04 e 06; a da CBS de 2025 e 2026 não se aplica à nota
  de crédito tipo 04.
- **CBS zero na ZFM e nas ALC (UB56-10, exceção 3):** é aceita quando o NCM
  **não** começa por 93 (armas), 24 (fumo), 2203 a 2208 (bebidas alcoólicas),
  8703 (automóveis) ou 33 (perfumaria, exceto 3303 a 3307) **e** emitente e
  destinatário estão na mesma área incentivada.
- As alíquotas de 2026 conferem com [[transicao-fixacao-aliquotas]].
- **Confirmação do IT 2025.002 v1.60 (seção 05, "Alíquotas padrão do IBS e da
  CBS"):** o informe dá a tabela, em percentual, a informar nos documentos:

  | Ano | pIBSUF (%) | pIBSMun (%) | pCBS (%) |
  |---|---|---|---|
  | 2026 (LC 214/2025) | 0,1 | 0 | 0,9 |
  | 2027 (LC 214/2025) | 0,05 | 0,05 | Aguardar Legislação |
  | 2028 (LC 214/2025) | 0,05 | 0,05 | Aguardar Legislação |
  | 2029 em diante | Aguardar Legislação | Aguardar Legislação | Aguardar Legislação |

  Nota do IT: "Cada ente federativo deve definir suas alíquotas por lei própria
  (art. 14 da LC 214/2025). Se não o fizer, aplica-se a alíquota de referência,
  fixada por resolução do Senado Federal (art. 18)." Para a CBS de 2027 e 2028,
  a regra de cálculo está em [[transicao-fixacao-aliquotas]].

## As fórmulas conferidas (tolerância de 0,01, salvo indicação)

Alíquota efetiva, quando há redução (UB28-10 para a UF; UB47-10 para o
Município; UB66-10 para a CBS):

> sem compra governamental: `pAliqEfet` = alíquota × (1 − `pRedAliq` / 100)
>
> com compra governamental: `pAliqEfet` = alíquota × (1 − `pRedAliq` / 100) ×
> (1 − `pRedutor` / 100)

Calculada com 4 casas decimais, arredondando a última. Exemplo da própria NT:
<!-- exemplo -->alíquota 10%, redução de 40% e redutor de compra governamental de
5% → 10 × (1 − 0,4) × (1 − 0,05) = 5,7.<!-- /exemplo -->

Valores do item:

> `vDif` = `vBC` × (alíquota / 100) × (`pDif` / 100) — diferimento (UB23-10,
> UB42-10, UB61-10)
>
> `vDevTrib` = `vBC` × (`pCBS` / 100) × (`pDevTrib` / 100) — CBS devolvida
> (UB63-10; com redução, usa `pAliqEfet`)
>
> `vIBSUF` = (`vBC` × alíquota / 100) − `vDif` − `vDevTrib` (UB35-10,
> rejeição 1041)
>
> `vIBSMun` = (`vBC` × alíquota / 100) − `vDif` − `vDevTrib` (UB54-10,
> rejeição 1052)
>
> `vCBS` = (`vBC` × alíquota / 100) − `vDif` − `vDevTrib` (UB67-10, rejeição
> 1069)
>
> `vIBS` = `vIBSUF` + `vIBSMun` − `vCredPres` (este só se
> "indDeduzCredPres=1") (UB54a-10, rejeição 1150)

Em todas, "alíquota" é a alíquota vigente (`pIBSUF`, `pIBSMun`, `pCBS`) ou,
havendo o grupo de redução, a `pAliqEfet`.

Imposto Seletivo (UB11-10, rejeição 1019, "Implementação Futura"):

> `vIS` = `vBCIS` × `pIS` / 100 (+ quantidade × alíquota específica / 100,
> se houver alíquota específica)

Compras governamentais (UB82a-20, rejeição 1142): a soma `vTribIBSUF` +
`vTribIBSMun` + `vTribCBS` do grupo `gTribCompraGov` deve bater com
`vIBSUF` + `vIBSMun` + `vCBS`, com tolerância de **0,04**.

## Regras de presença de grupos

| Situação | Regra | Rejeição |
|---|---|---|
| CST inexistente | UB13-10 | 1020 |
| CST que não permite IBS/CBS, mas `gIBSCBS` informado | UB13-20 | 1021 |
| CST não permite diferimento, mas `gDif` informado (UF) | UB22-10 | 1029 |
| CST exige diferimento, e `gDif` não informado (UF) | UB22-20 | 1030 |
| CST não permite redução, mas `gRed` informado (UF) | UB26-10 | 1032 |
| CST exige redução, ou há compra governamental, e `gRed` não informado (UF) | UB26-20 | 1033 |

As mesmas checagens se repetem para o IBS do Município e para a CBS. Na
compra governamental, o grupo `gRed` vai **com `pRedAliq` igual a zero**, mesmo
que o CST vede a redução.

## Totais e itens ainda sem validação em produção

Algumas regras estão escritas, mas marcadas na própria NT como **"Implementação
Futura"** (ainda não aplicadas, sem data):

- **Base de cálculo (UB16-10):** `vBC` = vProd + vServ + vFrete + vSeg + vOutro
  + vII − vDesc − vPIS − vCOFINS − vICMS − vICMSUFDest − vFCP − vFCPUFDest −
  vICMSMono − vISSQN + vIS, com exceções para PIS-ST/Cofins-ST que compõem o
  total. Nota da NT: "Implementação Futura, aguardando orientação normativa". A
  NT 2026.008 **remove** essa regra (ver [[df-valor-liquido-produto]]).
- **Valor do item (VB01-10, rejeição 1105):** vale "se não é operação de
  Faturamento Direto para veículos novos (`tpOp` = nulo ou `tpOp` <> 2)"; nesse
  caso, `vItem` = vProd − vDesc (−
  vICMSDeson, se indDeduzDeson=1) + vICMSST + vICMSMonoReten + vFCPST + vFrete
  + vSeg + vOutro + vII + vIPI + vIPIDevol + vServ (+ PIS-ST e Cofins-ST quando
  somam) + `vIBS` + `vCBS` + `vIS` + `vTotIBSMonoItem` + `vTotCBSMonoItem`; **em
  2025 e 2026 não se somam** vIBS, vCBS, vIS e os totais monofásicos.
- **Total da nota (W60-05, rejeição 1004; W60-10, rejeição 1094):** `vNFTot`
  obrigatório quando houver `IBSCBSTot`, e igual à soma dos `vItem`.
- **Grupo IBS/CBS obrigatório (UB12-10, rejeição 1115):** em homologação para
  NF-e emitidas a partir de 01/07/2026 por CRT 3; em produção, "implementação
  futura" (ver [[df-visao-geral-reforma-nfe]]).

## ⏳ Em produção a partir de 03/11/2026 — NT 2026.008 v1.00 (cronograma)

A NT 2026.008 remove a UB16-10 (fórmula da base de cálculo) e reescreve a
VB01-10 e a VB01-20: a partir de 2027 o `vProd` **já contém** vIBS, vCBS e vIS,
que deixam de ser somados de novo no `vItem`. A VB01-10 reescrita **continua
marcada como "Implementação Futura"** (a SEFAZ ainda não a aplica), e a
composição do `vProd` com os tributos vale a partir de 2027. Também cria as
regras do valor líquido do produto. Fórmula nova completa em [[df-valor-liquido-produto]].

## Ligações

- [[df-grupo-ibs-cbs-is]]: os campos que entram nas fórmulas.
- [[df-cst-cclasstrib]]: os indicadores que comandam as regras de presença.
- [[transicao-fixacao-aliquotas]]: alíquotas de teste de 2026 a 2028 na LC 214.
- [[ibs-cbs-aliquotas]]: quem fixa a alíquota de cada ente.
