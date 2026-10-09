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

Atualização [2026-10-07]: na regressão da fase B do Simples (R3), a resposta
sinalizou o IR corretamente, mas descreveu o IBS/CBS da locação **de memória**
e chutou um nome de nota inexistente. Por isso, o CLAUDE.md ganhou a regra
"Pergunta mista": sinalizar a parte fora de escopo e responder a parte coberta
**abrindo as notas** pelo INDEX. Depois da regra, o R3 passou 2 vezes em 2.

Atualização [2026-10-08]: na regressão dos regulamentos, o R3 respondeu a parte
coberta pelas notas, mas, ao sinalizar o IR como fora de escopo, citou de memória
"carnê-leão, tabela progressiva, 27,5%". A regra "Pergunta mista" do CLAUDE.md
passou a proibir regras, alíquotas, valores e nomes de obrigações da parte fora
de escopo.

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
do art. 38-B, II, só valem a partir de 01/01/2027 (erro apontado
na revisão final). As duas notas foram corrigidas.

**Correção posterior (fase A2, 2026-10-06):** a leitura do art. 38-B estava
errada desde a origem. Ele **não** é "multa de 60% por fraude": é a
**redução** das multas fixas/mínimas de obrigação acessória (90% MEI; 50% →
**60%** para ME/EPP a partir de 2027), e as hipóteses de fraude, sonegação,
conluio etc. são as **exceções** em que a redução não se aplica. Também o
§1º-C do art. 33 já existe hoje (incisos I a VIII do art. 13); o art. 169 da
LC 227 só o estende aos incisos I a X (IBS e CBS) em 2027. A nota-ponte e o
mapa foram corrigidos. Lição: ler o **caput** do artigo alterado antes de
interpretar um inciso solto da lei alteradora.

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

## [2026-10-07] — Notas Técnicas da NF-e trazem texto riscado que o pdftotext não mostra

O que aconteceu: ao escrever o domínio documentos-fiscais, a regra UB12-10 da
NT 2025.002-RTC parecia ter produção em 03/08/2026 e, para Simples/MEI, em
04/01/2027. Renderizando a página, esses trechos estavam **riscados** (redação
superada, em vermelho com marca amarela); a redação vigente diz
"implementação futura para produção". O `pdftotext` mistura riscado e vigente
sem distinção. 4 das 5 NTs tinham texto riscado (de 5 a 52 linhas cada; a NT 2026.010 não tinha).

Por que importa: toda nova versão de NT repete o padrão (a NT acumula o
histórico riscado). Sem tratar isso, a nota apresentaria como vigente uma data
ou regra já superada.

Ação: extrair sempre com `scripts/extrair_nt.py` (pymupdf), usar só o
`*-vigente.txt` nas notas e nas conferências (`conferir_tags.py`), e consultar o
`*-riscado.md` quando algo parecer contraditório.

## [2026-10-08] — Tabelas "fora do PDF" podem estar em portal oficial como JSON embutido

O que aconteceu: a lacuna dos Anexos III/IV da NT 2025.002-RTC (cClassTrib,
cCredPres) parecia exigir cópia manual. A tela do Portal da Conformidade Fácil
(SVRS) carrega os dados como JSON na própria página (`dadosOriginais`), com
vigência, redução de IBS/CBS, documentos e texto legal por código. Um site
privado (ECONET) tinha a mesma informação, mas sem rastreabilidade oficial.

Por que importa: o mesmo padrão deve valer para outras tabelas dos portais da
NF-e. A fonte privada serve só para achar o dado, nunca como base da nota.

Ação: antes de garimpar à mão, procurar a fonte oficial e olhar se a página
entrega JSON/CSV; capturar com script, registrar a data e conferir os códigos
das notas contra a captura (`scripts/tabelas_svrs.py`).

## [2026-10-08] — Documento técnico fica defasado: vale a tabela mais nova

O que aconteceu: o leiaute da NT 2025.002-RTC v1.52 dá como exemplo o cCredPres
"5 - Regime opcional para cooperativa", mas a tabela oficial atual tem o 5 como
regime automotivo (art. 311) e nenhum código para cooperativa. E a tabela
cClassTrib do portal tem itens publicados em 01/10/2026, depois do IT 2025.002
v1.60 (22/06/2026): o `410036` mudou de nome entre um e outro.

Por que importa: NT e IT são PDFs versionados; as tabelas do Portal dos DF-e
mudam com mais frequência. Copiar um exemplo da NT para uma nota pode registrar
um código errado.

Ação: para códigos (cClassTrib, cCredPres), a fonte é a tabela capturada, com
data (`scripts/tabelas_svrs.py`); o exemplo da NT só ilustra. Quando divergirem,
a nota avisa (⚠️) e segue a tabela, que a própria NT manda usar.

## [2026-10-08] — Mapa da visão multivigente: anexos na mesma linha e versão do anexo

O que aconteceu: o mapa da Res. 140 dizia que as Res. CGSN 178/2024 e 182/2025
alteraram o **Anexo VIII**; eram do **Anexo XI**. Na impressão do portal, os
títulos "ANEXO IX", "ANEXO X" e "ANEXO XI" ficam na mesma linha do link
`file_present ... .pdf`, e o filtro de ruído apagava a linha inteira. Também: a
marca de redação de um anexo vem **depois** do link do arquivo (não antes do
título), e os PDFs de anexo não dizem a versão.

Por que importa: toda resolução da Receita com anexos em PDF separado repete o
padrão (próximos: Anexos VII, X e XII). Um rótulo errado no mapa leva a
atribuir uma alteração ao anexo errado.

Ação: `vigencia_receita.py` agora tira só o trecho `file_present ... .pdf` e
separa cada título de anexo. Para saber a versão de um PDF de anexo, cruzar a
última marca do anexo no mapa com a data de criação do PDF (metadado) e
registrar as duas no `FONTE.md`.

## [2026-10-08] — Solução de Consulta: interpretação para os fatos do consulente

O que aconteceu: entrou a primeira Solução de Consulta (SC Cosit 71/2026). Ela
admite no Simples a administração de garantias de locação (Anexo III) e diz que
rendimento de aplicação fica fora do DAS, mas só para os fatos descritos e sem
convalidá-los (art. 45 da IN RFB 2.058/2021, citado na própria SC).

Por que importa: SCs vão chegar com frequência e são úteis para casos concretos
de clientes, mas não são regra geral nem estão acima da lei.

Ação: SC entra no domínio do ato que interpreta, numa nota de soluções de
consulta, como "interpretação da Receita", com os fatos resumidos e o limite
("vale para os fatos descritos"). Regra 8 do CLAUDE.md atualizada.

## [2026-10-08] — Regulamento que cita a lei artigo por artigo: mapear por script, não à mão

O que aconteceu: os regulamentos da CBS (620 artigos) e do IBS (617) chegaram
juntos. Escrever notas para 1.200+ artigos antes dos testes era inviável. Mas
cada artigo cita entre parênteses o dispositivo da LC 214 que regulamenta, em
dois formatos estáveis ("Lei Complementar nº 214, de 16 de janeiro de 2025" e
"LC 214/2025"). `scripts/mapa_regulamento.py` lê essas citações, gera o mapa
lei → regulamentos e grava em cada nota um bloco "Regulamentação" com os artigos
e a vigência (⏳ 2027/2029). Os artigos sem citação revelaram onde o regulamento
cria matéria própria (documento fiscal, cadastro, cashback, ZFM), que virou nota.

Por que importa: o padrão vale para qualquer regulamento futuro (ex.: atos do
CGIBS, novas versões). No PDF gerado pelo Word (Res. CGIBS 6), o `pdftotext`
junta parágrafos e o "Art. N" aparece no meio da linha; a divisão em artigos
precisa aceitar só números crescentes e ignorar "(Art. N da LC ...)".

Ação: para regulamento novo, rodar o script, conferir que não há artigo faltando
e que as citações não reconhecidas são zero ou explicadas, e só então escrever
notas para a matéria sem citação.

## [2026-10-08] — CBS e IBS regulamentados por atos diferentes podem divergir

O que aconteceu: o Decreto 13.075/2026 alterou o Regulamento da CBS para adiar a
2027 a inscrição no CNPJ e a emissão de documento por pessoa física e produtor
rural PF (arts. 105, § 4º-A, e 115, § 3º). A Res. CGIBS 6 das fontes, de mesma
numeração, não tem esse adiamento.

Por que importa: a reforma tem dois regulamentos para tributos "gêmeos"; o
cliente vê uma só operação, mas as regras podem andar em ritmos diferentes.

Ação: ao responder com regulamento, dizer se a regra é da CBS, do IBS ou dos
dois; quando só um foi alterado, sinalizar (⚠️) e registrar a pendência de
conferir o outro.

