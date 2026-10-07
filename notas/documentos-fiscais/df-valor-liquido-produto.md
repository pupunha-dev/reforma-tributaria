---
título: Valor líquido do produto e ICMS previsto no pagamento antecipado (NT 2026.008)
dominio: documentos-fiscais
fontes: NT 2026.008 v1.00 (seções 1 a 3 e cronograma)
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# Valor líquido do produto (NT 2026.008)

## A lógica em uma frase

O IBS e a CBS são calculados "por fora", mas a NT 2026.008 decide **como
mostrá-los** na nota: a partir de 2027 o valor do produto (`vProd`) passa a
**incluir** IBS, CBS e IS, e ganha um "irmão" sem tributos, o **valor líquido**
(`vProdLiq`). É como a etiqueta que mostra o preço final e, embaixo, o preço sem
impostos: o cliente vê os dois, e a soma não conta o imposto duas vezes.

## Cronograma

| Versão | Conteúdo | Homologação | Produção |
|---|---|---|---|
| 1.00 | campos de valor líquido e do ICMS previsto; regras I11c-10, I11c-20, NB01-10, NB01-20, W01a-10, W01a-20; alteração de B25-80, VB01-10 e VB01-20; **remoção da UB16-10** | 05/10/2026 | 03/11/2026 |
| 1.00 | regra NB01-30 | 01/02/2027 | 01/03/2027 |

Hoje (07/10/2026) tudo isto está **só em homologação**.

## ⏳ Em produção a partir de 03/11/2026 — NT 2026.008 v1.00 (cronograma)

**Composição do valor do produto (seção 1):**

- IBS e CBS **não** integram as próprias bases de cálculo, mas, "para fins de
  preenchimento da NF-e e da NFC-e", seus valores **devem ser acrescidos ao valor
  do produto ou serviço**, compondo o `vProd`. Isso **não** os coloca na base de
  cálculo, que segue a legislação.
- Por já estarem no `vProd`, IBS e CBS **não** são somados de novo no total da
  nota (`vNFTot`); nos grupos tributários ficam "meramente informativos".
- Observação do campo `vProd` (I11): "A partir de 2027, os valores de IBS, CBS e
  IS compõem o Valor Total Bruto, exceto nas notas de importação".

> Isso **substitui** a orientação da NT 2025.002-RTC de somar vIBS, vCBS e vIS
> no valor do item (ver [[df-calculo-e-validacoes]]). A fórmula antiga da base
> de cálculo (UB16-10) aparece **riscada** nesta NT: a regra foi removida.

**Campos novos:**

| Campo | ID | O que é |
|---|---|---|
| `vUnComLiq` | I11b | valor líquido **unitário**, sem tributos |
| `vProdLiq` | I11c | valor líquido do produto ou serviço, sem tributos |
| `vProdLiqTot` | W01a | soma dos valores líquidos dos itens |
| `ICMSPrevistoPagtoAntecip` / `vICMSPrevisto` | NB01 / NB02 | ICMS que incidirá no **fornecimento futuro**, em nota de pagamento antecipado |

A sequência de valor líquido é opcional hoje; a NT avisa que "futuramente essa
sequência será obrigatória".

**Regras:**

- **I11c-20 (rejeição 1279):** em NF-e normal, `vProdLiq` = `vUnComLiq` ×
  `qCom`, com tolerância de 0,01. A I11c-10 (`vProdLiq` obrigatório, rejeição
  1278) está como "Implementação futura".
- **W01a-10 / W01a-20 (rejeições 1282 / 1283):** se algum item tem
  `vProdLiq`, o total líquido é obrigatório e deve ser a soma dos itens.
- **ICMS previsto:** o grupo só vale em nota de débito tipo 06 (pagamento
  antecipado) ou em compra governamental com `tpOperGov` = 4 (recebimento do
  pagamento com fornecimento posterior). Fora desses casos, ou em NFC-e, é
  rejeição 1280 (NB01-10, NB01-20). Sem ICMS no fornecimento futuro, informar 0.
  A B25-80 passa a aceitar esse grupo na nota de débito tipo 06.
- **Valor do item (VB01-10, VB01-20; rejeição 1105, "Implementação Futura"):**

  > `vItem` = `vProd` (já com vIBS, vCBS e vIS) − vDesc − vICMSDeson (se
  > indDeduzDeson=1) + vICMSST + vICMSMonoReten + vFCPST + vFrete + vSeg +
  > vOutro + vII + vIPI + vIPIDevol + vServ + PIS-ST e Cofins-ST (quando somam)

  Na operação de faturamento direto de veículos novos (VB01-20), a soma é
  `vProd` − vDesc − vICMSDeson (se indDeduzDeson=1) + vFrete + vSeg + vOutro +
  vII + vIPI + vServ + PIS-ST e Cofins-ST (quando somam).

## ⏳ Em produção a partir de 01/03/2027 — NT 2026.008 v1.00 (cronograma)

**NB01-30 (rejeição 1281):** na nota de débito tipo 06 ou com `tpOperGov` = 4, o
grupo do ICMS previsto passa a ser **obrigatório** (homologação em 01/02/2027).

## Ligações

- [[df-calculo-e-validacoes]]: a fórmula anterior do valor do item e da base.
- [[df-grupo-ibs-cbs-is]]: os totais da nota.
- [[df-finalidade-debito-credito]]: a nota de débito tipo 06 (pagamento
  antecipado).
- [[df-visao-geral-reforma-nfe]]: linha do tempo das NTs.
