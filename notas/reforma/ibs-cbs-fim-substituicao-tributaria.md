---
título: Por que a substituição tributária (ST) desaparece com a reforma
origem: LC 214/2025 + LC 227/2026
artigos: 31 a 35 (split payment); 142 a 145 (transição do ICMS-ST em estoque)
---

# Por que a ST desaparece com a reforma

## O problema que a ST resolvia no ICMS

A substituição tributária era uma **gambiarra de arrecadação**: como o ICMS é um imposto plurifásico (cobrado em cada elo da cadeia) e o Fisco tinha dificuldade de fiscalizar todo mundo, a lei concentrava a cobrança de **toda a cadeia futura** em um único elo — normalmente o fabricante ou importador. Esse elo recolhia antecipadamente o ICMS que, em tese, seria devido lá na frente pelo distribuidor, atacadista e varejista, com base numa **margem de valor agregado presumida** (a famosa MVA/IVA-ST).

Ou seja: a ST existia porque **fiscalizar a venda final era difícil**, então o Estado cobrava adiantado, apostando numa estimativa de preço. Isso gerava distorções conhecidas: se o preço presumido era maior que o preço real de venda, o contribuinte pagava a mais (e tinha que brigar por restituição); se era menor, o Estado perdia arrecadação.

## O que o IBS/CBS muda na raiz: split payment

O novo sistema não precisa desse mecanismo porque ataca o problema por outro caminho — em vez de **presumir o preço futuro**, ele garante que o tributo da **operação real** seja recolhido no exato momento em que o dinheiro circula.

Isso é o que o **split payment** faz (ver [ibs-cbs-split-payment.md](ibs-cbs-split-payment.md), arts. 31-35): quando o cliente paga (cartão, Pix, boleto), o próprio prestador do meio de pagamento já segrega e recolhe o IBS/CBS **antes** de repassar o valor ao vendedor. Não é uma estimativa sobre uma cadeia inteira — é o recolhimento do valor exato (ou de um percentual aproximado, no procedimento simplificado) daquela transação específica, verificado quase em tempo real.

Com isso, o motivo de existir da ST desaparece:

- **Não há mais necessidade de "adiantar" a cobrança em um elo concentrado**, porque cada operação já recolhe o tributo dela mesma, automaticamente, no momento do pagamento — não depende de o contribuinte declarar a venda depois.
- **Não há mais MVA/IVA-ST presumido**, porque o valor tributado é o valor real da operação, não uma estimativa da cadeia até o consumidor final.
- A **não cumulatividade ampla** do IBS/CBS (crédito financeiro, ver [ibs-cbs-nao-cumulatividade-creditos.md](ibs-cbs-nao-cumulatividade-creditos.md)) também reduz a lógica de "concentrar em um elo": cada etapa da cadeia se credita do que pagou antes e recolhe só sobre o valor agregado dela, apurado de forma corrente — não é preciso um substituto tributário calculando o imposto de todos os elos seguintes de uma vez.

Em resumo: a ST era uma solução de **fiscalização indireta** (cobrar antes porque não dá para fiscalizar depois); o split payment é uma solução de **fiscalização direta em tempo real** (cobrar exatamente quando e onde o dinheiro se move). A segunda torna a primeira desnecessária.

## O que fica da ST: só a transição do estoque

O único resquício da ST no texto da reforma é operacional, não estrutural: mercadorias que já estavam em estoque em 31/12/2032 tiveram ICMS-ST retido no regime antigo, e esse valor não pode simplesmente evaporar quando o ICMS deixa de existir em 2033. Por isso os arts. 142-145 da LC 227/2026 criam um mecanismo de **crédito/restituição** desse ICMS-ST já pago, compensável com o IBS devido (ver [icms-st-estoque-2032.md](icms-st-estoque-2032.md) para o procedimento completo). Isso não é a ST "continuando" — é só a liquidação de um passivo do sistema antigo dentro do novo.

## Nota de escopo

Este raciocínio (por que a ST deixa de existir) está fundamentado na lógica estrutural do split payment e da não cumulatividade, como descritas na LC 214/2025 e LC 227/2026. As notas do projeto não têm — e a ST antiga não é matéria dessas leis — uma lista dos produtos/setores que hoje estão sob ST estadual; ver [LEARNINGS.md](../../LEARNINGS.md), entrada de 2026-08-25.

## Regulamentação (Decreto 12.955/2026 e Res. CGIBS 6/2026)

Artigos dos regulamentos que citam os artigos da lei tratados nesta nota (lista gerada por `scripts/mapa_regulamento.py`; a regra da lei prevalece):

<!-- gerado:regulamentos -->
- **Regulamento da CBS** (Decreto nº 12.955/2026): arts. 28 a 31 e 33
- **Regulamento do IBS** (Res. CGIBS nº 6/2026): arts. 28 a 31 e 33

Texto por artigo: `fontes/reforma/texto/decreto-12955-2026-artigos.txt` e `fontes/reforma/texto/res-cgibs-6-2026-artigos.txt` (procure a linha que começa com "Art. N"). Como ler e vigência: [mapa dos regulamentos](_mapa-regulamentos.md).
<!-- /gerado:regulamentos -->
