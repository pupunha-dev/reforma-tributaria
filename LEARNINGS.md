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

## [2026-10-09] — Perguntas da diretoria revelaram um erro de nota e duas omissões

O que aconteceu: ao rodar as 6 perguntas da diretoria em sessão limpa, a
conferência do conteúdo (não só da citação) achou: (1) a nota
`reducao-60-alimentos-higiene-agro` dizia que, nos insumos agropecuários (art.
138), o mecanismo era o diferimento "em vez de redução"; a lei **reduz 60% e
também difere**, e a resposta sobre fertilizantes omitiu os 60%; (2) a nota de
créditos dizia que comprar de optante do Simples "vale", sem dizer que o crédito
é só o valor do regime único (a resposta B6 afirmou crédito "normalmente"); (3) a
rampa de queda do ICMS (2029 a 2032) estava em outra nota e a resposta sobre "o
ICMS acaba?" misturou 2027-2032.

Por que importa: passar na regressão (a nota esperada foi citada) não prova que
o conteúdo está certo. O erro (1) estava há semanas numa nota revisada.

Ação: conferir o conteúdo das respostas de teste contra o texto da lei, não só a
citação; corrigidas as três notas e criada, em `transicao-fixacao-aliquotas`, a
tabela "quando cada tributo atual acaba". Lacuna registrada: o regime atual de
PIS/Cofins (cumulativo no Lucro Presumido) não está nas fontes; a resposta B3
usou conhecimento geral. Fica para o domínio PIS/Cofins (Leis 9.718, 10.637 e
10.833), candidato em `MEMORY.md`.

## [2026-10-16] — Teste do bot do Telegram revelou nota que simplificava o art. 251

O que aconteceu: ao testar pelo bot a pergunta "quando a pessoa física vira contribuinte do IBS/CBS ao alugar imóveis?", a resposta repetiu a nota `regime-especifico-bens-imoveis`: "receita anual acima de R$ 240 mil" e "passar do limite dentro do próprio ano torna contribuinte imediatamente (§ 2º)". O texto da LC 214 (art. 251) e dos regulamentos (art. 382) diz outra coisa: o limiar da regra geral é medido no **ano-calendário anterior**; a antecipação no próprio ano, na locação, só ocorre quando o valor excede o limite em **20%** (e, no regulamento, observada a quantidade de imóveis); na alienação é a partir da 4ª operação (2ª, se o imóvel foi construído pelo alienante); o limite é atualizado pelo IPCA.

Por que importa: a nota resumia demais, e o erro passa despercebido na regressão que só confere a citação (a nota esperada foi citada). O bot foi fiel à nota; o conteúdo estava impreciso.

Ação: seção "Quando a pessoa física vira contribuinte (art. 251)" reescrita com tabela e os três casos de antecipação, conferida contra `fontes/reforma/texto/lc-214-2025.txt` e os dois regulamentos. Padrão a repetir: toda nota que resume limiares de enquadramento (valores, ano-base, contagem de imóveis ou de operações) deve dizer o **período de apuração** (ano anterior × próprio ano) e ser conferida literalmente contra a lei.

## [2026-10-16] — Teste com caso real: nota de exportação de serviços "espelhava" o art. 64 e índices escondiam a nota certa

O que aconteceu: dois testes do bot (quem emite NFS-e pelo Emissor Nacional; serviço prestado no Brasil a tomador no exterior, com resposta da consultoria para comparar) mostraram três problemas. (1) `ibs-cbs-exportacao` dizia que o § 1º-A do art. 80 usa "o mesmo critério espelhado do art. 64": não é igual. A importação (art. 64, § 1º, II) basta o adquirente **ou** o destinatário residir no País; a exportação (art. 80, § 1º-A, II) exige adquirente **e** destinatário no exterior, e só "nos demais casos", isto é, fora dos incisos II a IX do art. 11. A nota também não explicava a consequência para serviço executado no Brasil. (2) A linha de `df-nfse-emissao-pessoas` no `INDEX.md` não dizia que só o prestador emite, e a de `sn-obrigacoes-acessorias` não dizia que a NFS-e nacional é obrigatória só para ME/EPP optantes: o roteador não abriu as notas certas. (3) A resposta da consultoria (CST 410 / cClassTrib 410004, art. 79) batia com a tabela, mas era incondicional: omitia a condição de consumo no exterior do art. 80.

Por que importa: o roteador escolhe só pelo texto da linha do índice, então a linha precisa conter a regra que responde a pergunta mais provável, não só o tema. E "espelho" de artigo é armadilha: conferir os conectivos (e/ou) e a condição "nos demais casos".

Ação: nota de exportação reescrita com o teste completo do § 1º-A e a ligação com o art. 11; linhas dos três índices ajustadas; bloco "Comércio exterior" da NFS-e com as lacunas do guia; perguntas D24 a D26 e R11 no banco de testes. Padrão: ao resumir uma regra "espelhada", citar os dois dispositivos lado a lado e conferir cada conectivo.

## [2026-10-16] — Reteste do caso real: o roteador deixou de abrir a nota do NIF e a nota trazia um exemplo que a lei não dá

O que aconteceu: no reteste da pergunta do colaborador (serviço prestado no Brasil a tomador no exterior), a resposta ficou correta e condicional, mas disse que "o NIF não consta nas notas", embora `df-nfse-emissao-pessoas` o trate. Pergunta com várias partes (CST/cClassTrib, sete campos de comércio exterior, NIF) esgota as 4 notas do roteador; a linha do índice dessa nota não citava o tomador no exterior nem o NIF, e ela perdeu para as outras quatro. Além disso, `ibs-cbs-exportacao` dava como exemplo de serviço do inciso X "serviço intelectual ou técnico a distância": exemplo nosso, não da lei, e perigoso (serviço de engenharia executado em obra no Brasil pode ser do art. 11, II ou V).

Por que importa: "não consta nas notas" dito sobre algo que está na base é o erro que mais abala a confiança da diretoria; e exemplo inventado numa nota vira regra na resposta do bot.

Ação: linha do índice passa a citar tomador no exterior e NIF; exemplo removido e substituído por aviso de enquadramento no art. 11; pergunta D27 no banco de testes. Padrão: pergunta com várias partes pode precisar de mais de 4 notas (`maxNotas` no nó "Preparar"); avaliar subir para 5 se o padrão se repetir. Nota nunca deve trazer exemplo de enquadramento que o texto legal não traz.

## [2026-10-16] — NFS-e: documentos técnicos do mesmo assunto não se alinham por data nem por número

O que aconteceu: ao ler as NTs da SE/CGNFS-e (003 a 010) e os anexos, apareceram quatro armadilhas. (1) A NT 005 (19/11/2025) é **anterior** à NT 004 v2.00 (10/12/2025), mas a 004 v2.00 diz que as evoluções da 005 só entram em produção depois: "a mais nova vale" não resolve, é preciso separar **publicada** de **em produção**. (2) O Anexo I recebido (modificado em 09/09/2025) é anterior ao RTC e não tem o grupo IBSCBS, enquanto as NTs citam versões de 10/12/2025 e o guia cita a v1.01 de 09/02/2026: um anexo em mãos pode estar defasado em relação à NT que o cita. (3) Nas regras de recepção do Anexo I, a mesma regra roda em colunas diferentes (emissores nacionais, decisão judicial, compartilhamento com o ADN): afirmar que uma regra "sempre vale" sem ver a coluna levou a um erro corrigido antes da publicação (as regras do valor 0 e de nDI/nRE rodam só nos emissores nacionais). (4) Planilhas têm anomalias (cenários 68, 111 e 112 do comércio exterior) que não se resolvem nas fontes.

Por que importa: o bot responderia "vale desde X" ou "a Sefin rejeita" sem base. A diretoria perde confiança se aparecer data ou rejeição errada.

Ação: nota de cronologia (`df-nfse-cgnfse-notas-tecnicas`) com seção "O que está em produção hoje?", versão do anexo registrada no `FONTE.md`, anomalias sinalizadas com ⚠️ nas notas, e `scripts/verificar.py` passou a aceitar versões do tipo "NT CGNFS-e 004 v2.00". Padrão: ao ingerir anexo ou planilha, registrar a data interna do arquivo, comparar com a versão citada pela NT e ler as colunas de aplicabilidade antes de afirmar onde uma regra roda.

## [2026-10-16] — Arquivo recebido não é o que o nome diz: conferir conteúdo, data e origem antes de usar

O que aconteceu: a segunda leva de arquivos mostrou quatro casos. (1) O PDF "Lista de Serviços Anexa à LC 116" é, na verdade, a lista **nacional** da NFS-e, com 335 códigos de 6 dígitos (cTribNac), e não a lista de 4 dígitos da lei; a página do portal é de 20/08/2024, e o guia cita um arquivo de 22/01/2026. (2) Um CSV de terceiros ("contabilin") cruzava item × NBS × cIndOp × cClassTrib e parecia o Anexo VIII que faltava, mas a conferência mostrou 3 cIndOp que não existem no Anexo VII, textos de local de incidência que contradizem o código e nomes de cClassTrib diferentes da tabela oficial. (3) A NT 2025.002 v1.33 já estava superada pela v1.52. (4) No PDF impresso do site, o `pdftotext` embaralha o primeiro item de cada página (cabeçalho fixo): a extração com `pymupdf` por blocos resolveu e foi conferida contra o `pdftotext -layout`.

Por que importa: a tabela de terceiros daria ao bot uma resposta de aparência oficial e errada. A diretoria perde a confiança se perceber um código inexistente.

Ação: compilação de terceiros arquivada em `referencias-nao-oficiais/`, fora das notas, com os resultados da conferência no `FONTE.md`; pendência F15 segue aberta até o Anexo VIII oficial. Padrão: fonte não oficial só entra depois de bater, linha a linha, com as tabelas oficiais; se não bater, fica arquivada e registrada. Para PDFs de página web, extrair por blocos e comparar contagens com outra extração.


## [2026-10-16] — Teste do bot: "não consta nas notas" sobre código que está na fonte, e tela do guia que contradiz o Anexo I

O que aconteceu: no reteste do caso do tomador estrangeiro, 4 das 5 respostas conferiram linha a linha com as fontes (cTribNac, E0372, IBGE, Anexo VIII). A quinta tinha duas lacunas de nota: (1) o bot disse que o CST 06 do PIS/COFINS "não consta nas notas", mas a NT 007 define o 06 como "Operação Tributável a Alíquota Zero"; a nota só listava as faixas de códigos, sem o significado. (2) Disse que o mecanismo de apoio do tomador "só aparece na nota do tomador" (texto do Anexo I), enquanto o guia mostra os dois mecanismos como obrigatórios na tela de quem emite e o valor 0 é rejeitado; o usuário via o campo e a resposta o contradizia. O guia também lista o vínculo "desconhecido" (sem "filial"), o que o Anexo I não tem.

Por que importa: afirmar que algo "não consta" quando consta, ou contradizer a tela que o usuário está vendo, abala a confiança na ferramenta. O Anexo I em mãos é de 09/09/2025 e o guia é de 27/07/2026, então a divergência pode ser só desatualização do anexo.

Ação: quadro com o significado dos CST do PIS/COFINS em `df-nfse-layout-ibscbs` (e o erro de digitação do 07 no Anexo I sinalizado); avisos ⚠️ sobre os dois mecanismos e o vínculo em `df-nfse-comercio-exterior` e `df-nfse-emissao-servico`; linha do índice atualizada; perguntas D46 a D48. Padrão: quando guia (tela) e anexo divergem, a nota deve dizer as duas versões, qual prevalece pela hierarquia e que a fonte não concilia, em vez de repetir só uma.

## [2026-10-16] — Anexos novos da NFS-e: cópia antiga da fonte, dois "Anexo IV", regras que só existem no Anexo VI e planilhas de células mescladas

O que aconteceu: (1) as respostas "confusas e duvidosas" vieram de um Anexo I de 09/09/2025 que ficou na pasta mesmo havendo a v1.01-20260209; a nota afirmava que o Anexo VIII e o Anexo VI "não estavam nas fontes" e usava 11 códigos de obra (hoje 13) e três códigos de imóvel (o Anexo VI usa cinco). (2) Dois documentos se chamam "Anexo IV": o do ADN (distribuição de DF-e, nas fontes) e o da NFS-e Via (citado pela NT 010, fora das fontes). (3) Regras de rejeição existem só no Anexo VI (por exemplo E0855, E0239, E0243, E0919, E0309) e as fórmulas de `vBC` e `vTotNF` mudam entre o Anexo I v1.01 e o VI; sem data de produção para o VI nas fontes. (4) No TSV, a matriz de NSU do Anexo IV perdeu o mapeamento coluna → destino (células mescladas): só a planilha original (`openpyxl`, intervalos mesclados) mostrou que a coluna "Município emissor, recepção" é V apenas para DF-e do sistema próprio do município. (5) A lista de serviços do portal está defasada: o Anexo I v1.01 tem 110501, 141403 e 141404.

Por que importa: a diretoria perde a confiança com qualquer data ou rejeição errada; a mesma frase vale ou não conforme o anexo.

Ação: sempre abrir `FONTE.md` e conferir versão e data antes de responder; as notas dizem de qual anexo vem cada regra ("I e VI" ou "só VI"); o nome "Anexo IV" é sempre qualificado; planilhas com células mescladas são lidas pela planilha original, não só pelo TSV. Padrão para novos anexos: comparar com o anterior por código de erro e registrar o que mudou.

## [2026-10-16] — Telegram: "can't parse entities" por _ * ` [ soltos na resposta

O que aconteceu: o nó "Telegram: enviar resposta" falhou com "Bad Request: can't parse entities" numa resposta que citava a tela `IndOp_IBSCBS`. O nó do n8n envia com `parse_mode` Markdown por padrão (não aparece nos Additional Fields), e um `_`, `*`, crase ou `[` sem par faz o Telegram recusar a mensagem inteira. Funcionava antes só porque as respostas anteriores não tinham esses caracteres.

Por que importa: respostas sobre NFS-e e NT trazem muitos nomes com underscore (campos, tags, telas); a falha some a resposta da vista de quem perguntou. Correção: `Formatar resposta` põe barra invertida antes desses 4 caracteres depois de dividir a mensagem (teste [5b]). Se um dia o nó passar a usar HTML ou MarkdownV2, o escape muda.
