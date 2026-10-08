---
título: Eventos da NF-e para a apuração do IBS e da CBS
dominio: documentos-fiscais
fontes: NT 2025.002-RTC v1.52, seção 8 (eventos 8.1 a 8.18)
vigencia: atual
texto-base: 2026-10-07
---

# Eventos para a apuração do IBS e da CBS

## A lógica em uma frase

A nota fiscal registra a operação; o **evento** registra o que acontece
**depois** dela e muda o crédito ou o débito: pagamento confirmado, mercadoria
roubada no caminho, bem incorporado ao imobilizado, nota de crédito aceita. É
como um "post-it" oficial colado na nota já autorizada, que a apuração assistida
do IBS e da CBS lê automaticamente.

## Por que importam em 2026

A NT diz que os eventos "integram as obrigações acessórias" do IBS e da CBS e
que, em 2026, quem cumpre integralmente as obrigações acessórias fica
**dispensado do recolhimento** do IBS e da CBS; por isso, os eventos devem ser
registrados "a partir de janeiro/2026, sempre que a situação concreta exigir".

> ⚠️ **Citação da NT × lei:** a NT atribui essa dispensa ao "artigo 348, §1º, da
> Emenda Constitucional". A regra está no **art. 348, §1º, da LC 214/2025** (ver
> [[transicao-fixacao-aliquotas]]). Vale a lei; a NT só lembra a consequência.

## Lista de eventos (8.1)

Autorizados na **SVRS** (SEFAZ Virtual do Rio Grande do Sul).

| Código | Evento | Autor |
|---|---|---|
| 112110 | Informação de efetivo pagamento integral para liberar crédito presumido do adquirente | emitente |
| 112120 | Importação em ALC/ZFM não convertida em isenção | emitente |
| 112130 | Perecimento, perda, roubo ou furto durante o transporte contratado pelo **fornecedor** | emitente |
| 112140 | Fornecimento não realizado com pagamento antecipado | emitente (da nota de débito tipo 06) |
| 112150 | Atualização da data de previsão de entrega | emitente |
| 211110 | Solicitação de apropriação de crédito presumido | emitente ou destinatário |
| 211124 | Perecimento, perda, roubo ou furto durante o transporte contratado pelo **adquirente** (frete FOB) | destinatário |
| 211128 | Aceite de débito na apuração por emissão de nota de crédito | destinatário |
| 211130 | Imobilização de item | destinatário |
| 211140 | Solicitação de apropriação de crédito de combustível | destinatário |
| 211150 | Solicitação de apropriação de crédito para bens e serviços que dependem de atividade do adquirente | destinatário |
| 212110 / 212120 | Manifestação sobre pedido de transferência de crédito de IBS / CBS em operações de sucessão | sucessora |
| 412120 / 412130 | Manifestação do fisco sobre pedido de transferência de crédito de IBS / CBS em operações de sucessão | fisco |
| 110001 | Cancelamento de evento (genérico, informando o código do evento cancelado) | o mesmo autor do evento cancelado |

## Para que serve cada um (funções descritas na NT)

- **112110:** o fornecedor informa que recebeu o pagamento integral, o que
  **libera o crédito presumido** do adquirente (campo `indQuitacao` igual a 1).
- **211110:** o destinatário pede a apropriação de crédito presumido em notas de
  terceiros; o emitente também pode usar quando a informação faltou na NF-e ou
  precisa de correção.
- **211128:** o destinatário **concorda** com os valores da nota de crédito, que
  serão lançados **a débito** na apuração assistida dele (ver
  [[df-finalidade-debito-credito]]).
- **211130:** o adquirente informa que integrou o bem ao **ativo imobilizado**,
  para o fisco controlar o prazo-limite de análise de ressarcimento (art. 40, I,
  da LC 214).
- **211140:** crédito de **combustível** (art. 172 da LC 214) consumido na
  atividade de quem pertence à cadeia desses combustíveis, observada a exceção do
  art. 180.
- **211124 / 112130:** perda, roubo, furto ou perecimento **em trânsito**,
  conforme quem contratou o frete (adquirente ou fornecedor).
- **112120:** o adquirente de região incentivada (ALC/ZFM) informa que a
  importação **não** se converteu em isenção por não cumprir as condições.
- **112140:** o fornecedor informa que o **pagamento antecipado** não teve
  fornecimento.
- **112150:** o fornecedor atualiza a previsão de entrega, para **tirar o débito
  do mês** previsto inicialmente.
- **Sucessão (212110, 212120, 412120, 412130):** aceite da transferência de
  crédito entre sucessoras da mesma empresa sucedida e manifestação do fisco.

## Como enviar (8.2)

- Hoje um lote pode ter até **20 eventos**, mas a NT diz que o uso de lote
  "deverá ser eliminada" no futuro e **orienta enviar cada evento da reforma
  individualmente**.
- A v1.40 ajustou o leiaute do evento 211110 e **eliminou o evento 211120**.

## Ligações

- [[df-finalidade-debito-credito]]: as notas de débito e crédito.
- [[df-grupo-ibs-cbs-is]]: o crédito presumido no item (`gCredPresOper`).
- [[transicao-fixacao-aliquotas]]: a dispensa de recolhimento de 2026.
- [[ibs-cbs-split-payment]]: o recolhimento que depende da quitação.
