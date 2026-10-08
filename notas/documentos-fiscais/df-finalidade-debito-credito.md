---
título: Notas de débito e de crédito na NF-e (finalidades 5 e 6)
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, seção 4, Grupo B (leiaute, campos B25 a B25.2) e regras de validação B25
vigencia: atual
texto-base: 2026-10-07
---

# Notas de débito e de crédito

## A lógica em uma frase

Débito e crédito são vistos **do lado de quem emite**: a nota de **débito**
registra que o emitente passou a dever **mais** imposto (e o destinatário,
menos); a nota de **crédito** registra que o emitente deve **menos** (e o
destinatário, mais). É o "estorno" ou o "complemento" de uma nota já emitida,
feito por documento próprio para que a apuração assistida do IBS e da CBS
enxergue o ajuste automaticamente.

## O que a NT diz (seção 4)

- A NT cria na NF-e **modelo 55** as finalidades de **nota de crédito** e de
  **nota de débito**. Nota de ajuste e nota complementar, já existentes, são
  "casos especiais de Nota de Débito". A nota de entrada que documenta a
  devolução de venda a consumidor final é "caso especial de Nota de Crédito".
- O uso dessas notas para lançamentos de ajuste será disposto na
  **regulamentação do IBS e da CBS**. Pelo Ajuste SINIEF nº 49/2025, a NF-e passa
  a admitir essas finalidades em hipóteses específicas também com reflexos no
  ICMS, "sendo vedada sua utilização fora das hipóteses expressamente previstas
  na legislação aplicável". O Ajuste SINIEF não está nas fontes.

## Campos

`finNFe` (B25): 1 normal; 2 complementar; 3 ajuste; 4 devolução de mercadoria;
**5 nota de crédito**; **6 nota de débito**.

| `tpNFDebito` (B25.1) — tipo de nota de débito | `tpNFCredito` (B25.2) — tipo de nota de crédito |
|---|---|
| 01 transferência de créditos para cooperativas | 01 multa e juros |
| 02 anulação de crédito por saídas imunes/isentas | 02 apropriação de crédito presumido de IBS sobre o saldo devedor na ZFM (art. 450, §1º, LC 214) |
| 03 débitos de notas fiscais não processadas na apuração | 03 retorno por recusa total na entrega ou por não localização do destinatário |
| 04 multa e juros | 04 redução de valores |
| 05 transferência de crédito na sucessão | 05 transferência de crédito na sucessão |
| 06 pagamento antecipado | 06 retorno por recusa parcial na entrega |
| 07 perda em estoque (perecimento, perda, furto, roubo) | |
| 08 desenquadramento do SN | |

## Regras de validação

| Regra | Situação que rejeita | Rejeição |
|---|---|---|
| B25-110 | nota de **crédito** que não seja de **entrada** (`tpNF` diferente de 0) | 1161 |
| B25-120 | nota de **débito** que não seja de **saída** (`tpNF` diferente de 1) | 1162 |
| B25.1-10 / B25.1-20 | tipo de débito informado sem finalidade 6, ou finalidade 6 sem tipo | 1139 / 1009 |
| B25.2-10 / B25.2-20 | tipo de crédito informado sem finalidade 5, ou finalidade 5 sem tipo | 1163 / 1164 |
| B25.2-30 | crédito tipo 02 (crédito presumido da ZFM) com ano de emissão anterior a 2029 | 1145 ("só pode ser usado a partir de janeiro/2029") |
| B25.2-40 | crédito tipo 03 (retorno) que não seja de entrada | 1152 |
| B25-100 | nota de crédito referenciando documento que não seja NF-e modelo 55 (no tipo 03, aceita também modelo 65) | 1003 |
| B25-80 | nota de débito ou crédito (ou `tpOperGov` = 2) com ICMS, ISSQN, IPI, II, PIS, Cofins (próprios ou ST), ICMS UF destino ou imposto devolvido | 1001 ("somente para IBS/CBS") |

Exceções da B25-80: não se aplica aos créditos tipos 03, 04 e 06 nem ao débito
tipo 07 (perda em estoque). O débito tipo 06 (pagamento antecipado) aceita PIS,
PIS-ST, Cofins e Cofins-ST em NF-e emitida em 2026, e aceita IPI.

Em palavras simples: a nota de débito/crédito é, em regra, **só de IBS/CBS**.
Ela não carrega ICMS nem os tributos antigos, salvo nas exceções acima.

## Ligações

- [[df-grupo-ibs-cbs-is]]: os campos de IBS/CBS que a nota de débito/crédito
  carrega.
- [[df-eventos-apuracao]]: o evento de aceite de débito por emissão de nota de
  crédito.
- [[ibs-cbs-cadastro-documento-fiscal]]: o documento fiscal na LC 214.
