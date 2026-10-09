# Perguntas-teste — domínio reforma

Rodar depois de qualquer mudança no protocolo (CLAUDE.md) ou na estrutura.
Cada pergunta é feita numa sessão nova, na raiz do projeto:

    claude -p "<pergunta>" > saida.txt

e a saída precisa conter **todos** os termos da coluna "deve citar" (termos
ligados por "ou" são alternativos: basta um) e respeitar o comportamento
esperado.

| # | Pergunta | Deve citar | Comportamento esperado |
|---|---|---|---|
| R1 | Qual a alíquota de referência do IBS em 2031? | `transicao-fixacao-aliquotas` | Aponta lacuna (arts. 353–365 não detalhados na nota) e oferece consultar o PDF; não inventa percentual |
| R2 | Quais produtos tinham ST do ICMS e deixaram de ter com a reforma? | `ibs-cbs-fim-substituicao-tributaria` | Explica o porquê conceitual (split payment) e sinaliza a lista de produtos como fora de escopo |
| R3 | O que muda no IR do aluguel com a reforma? | `regime-especifico-bens-imoveis` | Sinaliza IR como fora de escopo; responde só a parte de IBS/CBS |
| R4 | Como o MEI recolhe o IBS e para quem vai o dinheiro? | `simples-nacional-e-mei` ou `sn-repasse-arrecadacao` | 50% ao Município/DF e 50% ao Estado/DF (art. 22, V e VI da LC 123, red. LC 227) |
| R5 | Quem fixa a alíquota do IBS de um Município? | `ibs-cbs-aliquotas` | Lei municipal (art. 14), vinculável à alíquota de referência |
| R6 | Quais artigos do regulamento da CBS tratam do split payment? | `ibs-cbs-split-payment` ou `_mapa-regulamentos` | Aponta os artigos do Decreto 12.955/2026 do bloco "Regulamentação" (arts. 28 a 31 e 33, mais os sem citação 32, 34 e 35 no mapa); cita a LC 214 (arts. 31 a 35) |
| R7 | A partir de quando um produtor rural pessoa física precisa ter CNPJ e emitir nota por causa do IBS/CBS? | `ibs-cbs-cadastro-regulamentacao` ou `ibs-cbs-documento-fiscal-regulamentacao` | Na CBS, a partir de 01/01/2027 (Decreto 12.955, arts. 105, §4º-A, e 115, §3º, red. Decreto 13.075); sinaliza que o regulamento do IBS das fontes não tem esse adiamento |
| R8 | Como calculo o crédito presumido na compra de produtor rural não contribuinte? | `ibs-cbs-credito-presumido-regulamentacao` | Fórmula CP = (VO × C) ÷ (1 + C), percentual anual fixado até setembro por ato do Ministro da Fazenda e do CGIBS (não está nas fontes); vale a partir de 01/01/2027; só com pagamento confirmado |
| R9 | Uma nota fiscal emitida para um cliente com CNPJ inapto gera crédito? | `ibs-cbs-documento-fiscal-regulamentacao` | Documento inidôneo quando indica adquirente com inscrição inapta, suspensa, nula ou baixada (art. 122, III, dos regulamentos); remete a crédito exigir documento idôneo |
| R10 | Qual é o percentual de crédito presumido de CBS na compra de material para reciclagem de catador? | `ibs-cbs-credito-presumido-regulamentacao` | CBS 7% (Decreto 12.955, art. 485); IBS 1,3% em 2029 até 13% a partir de 2033 (Res. CGIBS 6, art. 483); efeitos da CBS a partir de 01/01/2027 |
