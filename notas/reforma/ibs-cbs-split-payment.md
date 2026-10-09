---
título: Split payment — recolhimento na liquidação financeira
origem: LC 214/2025 + LC 227/2026
artigos: 31 a 35
---

# Split payment (recolhimento na liquidação financeira)

## A ideia central

É a principal novidade de arrecadação do novo sistema: em vez de o contribuinte recolher o tributo depois de receber o pagamento, **o próprio meio de pagamento (cartão, Pix, boleto etc.) já separa e recolhe** o IBS/CBS automaticamente no momento em que o dinheiro é liquidado, antes de chegar às mãos do fornecedor. Isso reduz drasticamente a sonegação por "não declarar a venda".

Quem executa essa segregação são os **prestadores de serviço de pagamento** e **instituições operadoras de arranjos de pagamento** (art. 31) — bandeiras de cartão, PSPs, instituições de pagamento do Pix etc.

## Dois procedimentos (art. 31, §1º — redação da 227)

1. **Procedimento padrão** (art. 32): o valor exato do IBS/CBS da operação é identificado e segregado. O originador da transação (quem inicia o pagamento) transmite ao prestador de pagamento os dados que permitem vincular a transação à operação e calcular o tributo devido. O sistema consulta os valores exatos junto ao Comitê Gestor/RFB antes de liberar os recursos ao fornecedor.

2. **Procedimento simplificado** (art. 33): quando não há informação suficiente para calcular o valor exato, aplica-se um **percentual pré-estabelecido** sobre o valor da operação (definido pelo CGIBS para o IBS e pela RFB para a CBS, podendo variar por setor). É uma aproximação — o valor retido pode ser maior ou menor que o devido de fato; o ajuste fino ocorre na apuração mensal do contribuinte.

## Regras comuns (art. 34)

- a segregação ocorre no momento da **liquidação financeira**, não na data da venda;
- em pagamento parcelado, a segregação é proporcional a cada parcela;
- antecipação de recebíveis (ex.: "antecipar" vendas no cartão) não muda a obrigação de segregar/recolher;
- o prestador de pagamento **não é responsável tributário** pelo IBS/CBS da operação em si — só pelo cumprimento do dever de segregar e recolher.

## Alterações pela LC 227/2026

- **Art. 31, §1º**: agora nomeia explicitamente os dois procedimentos (padrão e simplificado) como opções dentro do split payment — antes a distinção entre eles era menos clara na redação original.
- **Art. 31, §1º-A** (novo): define "originador da transação" e diferencia transações **iniciadas pelo recebedor** (quem define o valor é quem vai receber, ex.: cobrança via Pix) de transações **iniciadas pelo pagador** (quem paga define o valor, sem instrução prévia do recebedor) — distinção relevante para saber de quem é a obrigação de informar os dados da operação ao sistema.
- **Art. 32, §2º-A** (novo): se o recebedor optar por não informar os dados de vinculação da operação (art. 32, §1º, I), cabe ao fornecedor ou à plataforma digital incluir essa informação no próprio documento fiscal eletrônico — como salvaguarda para o sistema não perder rastreabilidade.
- **Art. 33 inteiro reescrito**: o procedimento simplificado deixou de ser regra excepcional/transitória para virar uma opção estrutural, com regras próprias de uso dos valores retidos (§3º, incisos I e II, novos) e devolução de sobras em até 3 dias úteis (§4º). O §2º-A (novo) esclarece que, se a transação não identificar os valores de IBS/CBS conforme o art. 32, isso **já implica automaticamente** a opção pelo procedimento simplificado.
- **Art. 34, V, "a"**: ajuste de redação sem mudança de fundo.

## Regulamentação (Decreto 12.955/2026 e Res. CGIBS 6/2026)

Artigos dos regulamentos que citam os artigos da lei tratados nesta nota (lista gerada por `scripts/mapa_regulamento.py`; a regra da lei prevalece):

<!-- gerado:regulamentos -->
- **Regulamento da CBS** (Decreto nº 12.955/2026): arts. 28 a 31 e 33
- **Regulamento do IBS** (Res. CGIBS nº 6/2026): arts. 28 a 31 e 33

Texto por artigo: `fontes/reforma/texto/decreto-12955-2026-artigos.txt` e `fontes/reforma/texto/res-cgibs-6-2026-artigos.txt` (procure a linha que começa com "Art. N"). Como ler e vigência: [mapa dos regulamentos](_mapa-regulamentos.md).
<!-- /gerado:regulamentos -->
