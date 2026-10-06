# Aprendizados acumulados

## [2026-08-24] — transicao-fixacao-aliquotas.md não detalha a fórmula ano a ano (arts. 353-365)

O que aconteceu: ao testar a pergunta "qual a alíquota de referência do
IBS na fase de transição?", a resposta corretamente apontou uma lacuna
em vez de inventar valores — a nota cobre a lógica geral da fixação das
alíquotas de referência de 2029-2035 (arts. 349-352) e cita que "um
artigo específico para cada ano [...] detalha a fórmula daquele ano",
mas não desenvolve o conteúdo de cada um dos arts. 353 a 365
individualmente (a fórmula específica de cada ano, com seus respectivos
anos-base e variáveis).

Por que importa: para perguntas sobre o valor exato da alíquota de um
ano específico dentro de 2029-2035, é preciso consultar o texto literal
dos arts. 353-365 em `fontes/lc-214-2025-texto-compilado.pdf`, já que a
nota não tem esse detalhe ainda.

Ação: se essa pergunta voltar a ser feita com frequência, criar uma
tabela ano-a-ano (ou nota complementar) extraindo os arts. 353-365.

## [2026-08-25] — "Quais produtos tinham ST e deixaram de ter" está fora do escopo das notas

O que aconteceu: perguntado quais produtos eram sujeitos à substituição
tributária (ST) do ICMS antes da reforma e deixaram de ser, a única nota
relacionada — [icms-st-estoque-2032.md](notas/icms-st-estoque-2032.md),
arts. 142-145 da LC 227/2026 — cobre apenas a regra de transição (crédito
do ICMS-ST retido sobre estoque em 31/12/2032), não uma lista de produtos.
A resposta correta foi apontar que essa lista nunca existiu no escopo do
projeto: o regime de ST do ICMS era definido produto a produto por
convênios/protocolos estaduais, matéria que não está na LC 214/2025 nem
na LC 227/2026 (essas leis tratam da extinção do ICMS e da criação do
IBS/CBS/IS, não de listar mercadorias com ST).

Por que importa: é fácil confundir "o que a reforma extingue" (o próprio
regime de ST, substituído por split payment) com "quais produtos tinham
ST" — essa segunda pergunta é sobre legislação estadual de ICMS, fora do
material em `fontes/`. Perguntas parecidas provavelmente vão surgir de
novo (ex.: "quais produtos tinham redução de base de cálculo no ICMS-ST"),
e a resposta correta continua sendo apontar a lacuna, não a lista.

Ação: se a equipe precisar recorrentemente da lista de mercadorias/setores
com ICMS-ST hoje, isso exige levantamento externo (convênios ICMS por UF)
e não pode ser resolvido só com os PDFs de `fontes/` — registrar como
pedido de pesquisa à parte, não como nota de reforma tributária.

## [2026-09-09] — Perguntas sobre "imóveis"/"aluguel" tendem a incluir IR, que é fora de escopo

O que aconteceu: perguntado sobre o que a reforma mudou para o setor
imobiliário (venda, aluguel, incorporação), a pergunta já veio junto
com "IR para esse setor". As notas
[regime-especifico-bens-imoveis.md](notas/regime-especifico-bens-imoveis.md)
e [transicao-operacoes-bens-imoveis.md](notas/transicao-operacoes-bens-imoveis.md)
cobrem bem IBS/CBS sobre imóveis, mas Imposto de Renda é tributo
federal distinto, não tratado pela LC 214/2025 nem pela LC 227/2026 —
a resposta precisou sinalizar isso como fora de escopo, não como
lacuna de nota.

Por que importa: "imóveis" e "aluguel" são temas onde IR (ganho de
capital na venda, IR sobre aluguel recebido por pessoa física) é
associação natural para quem pensa em tributação do setor, mas essas
leis não tocam em IR. É fácil, sem atenção, tentar responder com
conhecimento geral sobre IR imobiliário — o que violaria a regra 1 do
protocolo (só responder com base nos arquivos do projeto).

Ação: em perguntas sobre imóveis/aluguel que mencionem IR (ou outros
tributos sobre renda/patrimônio não cobertos, como IPTU), responder a
parte de IBS/CBS/IS/ITCMD normalmente e sinalizar explicitamente que
IR está fora do escopo do second brain — sem tentar preencher com
conhecimento geral.
