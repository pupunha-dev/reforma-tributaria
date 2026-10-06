# Perguntas-teste — domínio reforma

Rodar depois de qualquer mudança no protocolo (CLAUDE.md) ou na estrutura.
Cada pergunta é feita numa sessão nova, na raiz do projeto:

    claude -p "<pergunta>" > saida.txt

e a saída precisa conter **todos** os termos da coluna "deve citar" e
respeitar o comportamento esperado.

| # | Pergunta | Deve citar | Comportamento esperado |
|---|---|---|---|
| R1 | Qual a alíquota de referência do IBS em 2031? | `transicao-fixacao-aliquotas` | Aponta lacuna (arts. 353–365 não detalhados na nota) e oferece consultar o PDF; não inventa percentual |
| R2 | Quais produtos tinham ST do ICMS e deixaram de ter com a reforma? | `ibs-cbs-fim-substituicao-tributaria` | Explica o porquê conceitual (split payment) e sinaliza a lista de produtos como fora de escopo |
| R3 | O que muda no IR do aluguel com a reforma? | `regime-especifico-bens-imoveis` | Sinaliza IR como fora de escopo; responde só a parte de IBS/CBS |
| R4 | Como o MEI recolhe o IBS e para quem vai o dinheiro? | `simples-nacional-e-mei` | 50% ao Município/DF e 50% ao Estado/DF (art. 22, V e VI da LC 123, red. LC 227) |
| R5 | Quem fixa a alíquota do IBS de um Município? | `ibs-cbs-aliquotas` | Lei municipal (art. 14), vinculável à alíquota de referência |
