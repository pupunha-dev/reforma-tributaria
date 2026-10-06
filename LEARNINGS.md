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
dos arts. 353-365 em `fontes/reforma/lc-214-2025-texto-compilado.pdf`, já que a
nota não tem esse detalhe ainda.

Ação: se essa pergunta voltar a ser feita com frequência, criar uma
tabela ano-a-ano (ou nota complementar) extraindo os arts. 353-365.

## [2026-08-25] — "Quais produtos tinham ST e deixaram de ter" está fora do escopo das notas

O que aconteceu: perguntado quais produtos eram sujeitos à substituição
tributária (ST) do ICMS antes da reforma e deixaram de ser, a única nota
relacionada — [icms-st-estoque-2032.md](notas/reforma/icms-st-estoque-2032.md),
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
[regime-especifico-bens-imoveis.md](notas/reforma/regime-especifico-bens-imoveis.md)
e [transicao-operacoes-bens-imoveis.md](notas/reforma/transicao-operacoes-bens-imoveis.md)
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

## [2026-10-06] — Duas leituras erradas sobre o art. 169 da LC 227 nas notas da reforma

O que aconteceu: ao montar o mapa de vigência da LC 123 com o texto
literal da LC 227 (HTML do Planalto), apareceram dois erros:
(1) [lc227-alteracoes-legislacao-correlata.md](notas/reforma/lc227-alteracoes-legislacao-correlata.md)
dizia que o art. 182 da LC 227 dá efeitos a partir de 01/01/2027 ao
"art. 169 da LC 214". O texto se refere ao **art. 169 da própria LC 227**,
que altera os arts. 18, 18-A, 21, 33 (§1º-C) e 38-B (II) da LC 123; (2)
[simples-nacional-e-mei.md](notas/reforma/simples-nacional-e-mei.md) dizia
que serviços sujeitos só a IBS/CBS são tributados pelo **Anexo II**. O
texto literal (novo inciso VIII do §4º do art. 18 da LC 123) diz
**Anexo III**. A nota também não informava que essa regra, o §1º-C do art. 33 e a multa
de 60% do art. 38-B, II, só valem a partir de 01/01/2027 (erro apontado
na revisão final). As duas notas foram corrigidas.

Por que importa: "art. N" dentro de uma cláusula de vigência se refere à
própria lei, salvo menção expressa a outra. E a segregação de receitas
do DAS é exatamente o tipo de regra que um cliente do Simples pergunta
"já vale?". Sem a data, a nota levava a aplicar em 2026 uma regra de 2027.

Ação: o trecho do art. 18-A, §7º, I ("opção até 31/12 com efeitos em
janeiro seguinte"), resumido na mesma nota, deve ser conferido contra o
texto literal na fase A2 (redação das notas `sn-*`).

## [2026-10-06] — Planalto: vigência de cada dispositivo está no HTML, não no PDF

O que aconteceu: no PDF impresso do texto compilado, a redação superada
perde o risco e "Produção de efeitos" vira texto sem data. No HTML
oficial, o texto superado vem em `<strike>`, e cada "Produção de
efeitos"/"Vigência" é um link para o inciso exato da cláusula de vigência
da lei alteradora (ex.: `Lcp214.htm#art544-3`). Com isso, o
`scripts/vigencia_planalto.py` gera o mapa de vigência sem depender de
leitura manual. O mesmo HTML mostrou que **o compilado da LC 123 ainda
não incorpora o art. 169 da LC 227** (efeitos em 2027): esse texto só
existe, por enquanto, em `fontes/reforma/texto/lc-227-2026-planalto.htm`.

Por que importa: é o padrão de todas as leis do Planalto, que provavelmente
vão entrar como próximos domínios (LC 87, LC 116, Leis 10.637/10.833). E o
compilado pode estar atrasado em relação às alterações com efeito futuro.

Ação: em todo domínio novo vindo do Planalto, capturar também o HTML
(`texto/<lei>-planalto.htm`) e gerar o mapa com `vigencia_planalto.py`.
Para alterações com efeito futuro, conferir se o compilado já as
incorporou; se não, usar o texto da lei alteradora.
