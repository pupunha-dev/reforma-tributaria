# Second brain tributário — Guia do projeto

Base de conhecimento do setor fiscal sobre **legislação tributária
federal**, organizada por **domínio** (assunto). Todo o conhecimento
factual vive em notas Markdown em `notas/<dominio>/`, com base nos textos
oficiais de `fontes/<dominio>/`.

## Domínios

| Domínio | Atos normativos | Notas | Fontes | Prefixo | Status |
|---|---|---|---|---|---|
| reforma | LC 214/2025 + LC 227/2026 + regulamentos: Decreto 12.955/2026 (CBS) e Res. CGIBS 6/2026 (IBS) | `notas/reforma/` | `fontes/reforma/` | — | ativo (92 notas; bloco "Regulamentação" em cada nota da lei) |
| simples-nacional | LC 123/2006 (fase A) + Res. CGSN 140/2018 e alteradoras, como as Res. CGSN 190 e 191/2026 (fase B) + Anexos VI e XI da Res. 140, Res. CGSN 11/2007 (arrecadação) e Solução de Consulta Cosit 71/2026 (fase C) | `notas/simples-nacional/` | `fontes/simples-nacional/` | `sn-` | ativo (35 notas) — fases A, B e C concluídas |
| documentos-fiscais | Notas Técnicas do Projeto NF-e: NT 2025.002-RTC, 2026.002, 2026.007, 2026.008 e 2026.010; Informe Técnico 2025.002 (tabelas do IBS/CBS); tabelas CST/cClassTrib e cCredPres do Portal dos DF-e (SVRS). Versões e datas de captura em `fontes/documentos-fiscais/FONTE.md` | `notas/documentos-fiscais/` | `fontes/documentos-fiscais/` | `df-` | ativo (12 notas) |

- Índice mestre: **[notas/INDEX.md](notas/INDEX.md)**. Cada domínio tem
  `INDEX.md` (notas por tema) e `_plano-notas.md` (mapa artigo → nota).
- Para incluir um domínio ou uma fonte nova, siga
  [docs/procedimento-nova-legislacao.md](docs/procedimento-nova-legislacao.md).

## Escopo

**Só atos normativos federais listados na tabela de domínios**: leis
complementares, leis e atos infralegais federais, como resoluções do
CGSN, as **Soluções de Consulta da Receita** listadas na tabela, e a
**documentação técnica nacional dos documentos fiscais eletrônicos** (Notas
Técnicas e Informes Técnicos do Projeto NF-e/NFC-e e as tabelas oficiais que
eles publicam) listada na tabela.
Ficam fora: legislação estadual e municipal (convênios, protocolos,
ITBI/IPTU municipal etc.) e tributos ou regimes que esses atos não tratam
(ex.: IRPF e IRPJ pelo lucro real/presumido; o IRPJ **dentro** do Simples
Nacional é matéria da LC 123 e está no escopo). Perguntas sobre esses temas ficam fora do escopo das
notas, mesmo quando parecem relacionadas.

**Pergunta mista (parte dentro, parte fora do escopo).** Não pare na parte
fora de escopo: sinalize-a e **responda a parte coberta abrindo as notas**
pelo `INDEX.md` do domínio, citando a nota (ex.: "IR do aluguel" → IR fora de
escopo; IBS/CBS da locação em `regime-especifico-bens-imoveis.md`; "limite da
NFC-e sem destinatário em SP" → valor estadual fora de escopo, regra nacional
da NT em `df-emissao-offline-alerta.md`). Nunca descreva a parte coberta de
memória, nem adivinhe nome de nota, nem cite de memória o ato estadual ou
municipal que estaria fora de escopo. Na parte fora de escopo, **não dê regras,
alíquotas, valores ou nomes de obrigações** (ex.: tabela do IR, carnê-leão):
diga só que o tema não está nas fontes.

**Caso especial: substituição tributária (ST), domínio reforma.** A
exclusão de escopo vale especificamente para **listas de produtos/setores
sujeitos a ST definidas por convênio ou legislação estadual** (ex.:
convênios ICMS 142/2018 e correlatos), que ficam fora de escopo. Já a
**explicação conceitual de como o desenho da reforma (split payment, não
cumulatividade) torna a lógica de ST desnecessária** é matéria federal e
está coberta em `ibs-cbs-fim-substituicao-tributaria.md`. Quando uma
pergunta misturar as duas partes, responda a parte conceitual com base nas
notas e sinalize só a parte da lista de produtos/setores como fora de
escopo, sem recusar a pergunta inteira.

**Domínio em implantação.** Responda só com as notas já escritas. O que
faltar é lacuna (regra 3): ofereça consultar o texto extraído em
`fontes/<dominio>/texto/` ou o PDF.

## Regras de resposta (protocolo)

0. **Identifique o domínio** (ou domínios) da pergunta e comece pelo
   `INDEX.md` desse domínio.
1. **Responda só com base no que está escrito nos arquivos deste projeto**
   (`notas/`, `fontes/`, `MEMORY.md`, `LEARNINGS.md`, `decisions.md`).
   Não complete lacunas com conhecimento geral: a lei tem detalhes e
   exceções específicas que não podem ser "chutados".
2. **Sempre cite o arquivo-fonte** da informação usada na resposta
   (ex.: `ibs-cbs-aliquotas.md`) e o artigo do ato normativo quando a nota
   indicar.
3. **Se a informação não estiver nas notas**, diga isso explicitamente, sem
   inventar. Nesse caso, ofereça consultar o texto em
   `fontes/<dominio>/texto/` ou o PDF em `fontes/<dominio>/` e, se fizer
   sentido, proponha criar ou atualizar uma nota depois.
4. Ao explicar uma regra ou fórmula de cálculo, descreva-a por completo
   (não apenas "veja a nota X"), que é o estilo de trabalho do usuário.
5. **Critério para registrar em LEARNINGS.md**: só vale a pena registrar
   algo como aprendizado se pelo menos uma destas condições for
   verdadeira: (1) revelou uma lacuna real numa nota existente,
   (2) expôs uma interpretação que precisou ser corrigida ou (3) é um
   padrão que provavelmente vai se repetir. Não registre detalhes
   triviais de uma única sessão.
6. **Critério para registrar em decisions.md**: só registre quando a
   equipe efetivamente adotou uma posição, especialmente em pontos onde a
   lei é ambígua, ainda não regulamentada ou permite mais de uma
   interpretação válida. Não registre hipóteses discutidas, opções
   cogitadas e descartadas ou dúvidas ainda em aberto.
7. **Vigência (R-vigência).** Ao usar uma nota com
   `vigencia: com-mudanca-programada`, diga se a regra citada vale **hoje**
   ou **a partir de quando** (blocos `⏳`/`❌`). Nunca misture a redação
   vigente com a futura na mesma frase.
8. **Hierarquia (R-hierarquia).** Lei > resolução/ato infralegal > nota
   técnica. Quando dois níveis tratarem do mesmo ponto, cite os dois. Se
   houver conflito, prevalece o nível mais alto e o conflito é sinalizado.
   A nota técnica diz **como preencher e validar** o documento fiscal; ela
   não cria nem altera tributo. O **Informe Técnico** e as tabelas oficiais
   que ele publica (cClassTrib, cCredPres) têm o nível da NT; quando o
   exemplo de uma NT diverge da tabela que ela manda usar, vale a tabela.
   Os **regulamentos da reforma** (Decreto 12.955/2026 para a CBS; Res. CGIBS
   6/2026 para o IBS) são atos infralegais: detalham a LC 214 e citam, em cada
   artigo, o dispositivo da lei; ao usar uma nota da reforma, consulte o bloco
   "Regulamentação" dela e diga se a regra é da CBS, do IBS ou dos dois.
   A **Solução de Consulta** da Receita interpreta a lei e a resolução para
   os fatos descritos pelo consulente: cite-a como "interpretação da Receita",
   nunca como regra nova, e sinalize se ela divergir da lei ou da resolução.
9. **Cruzamento (R-cruzamento).** Pergunta que envolve dois domínios (ex.:
   Simples Nacional × IBS/CBS) usa as notas dos dois e cita ambas.

## Legendas

- **Domínio reforma:** 🔵 só LC 214/2025 · 🟡 tema presente nas duas (LC 227
  alterou dispositivo da LC 214) · 🟢 só LC 227/2026.
- **Todos os domínios:** `## ⏳ A partir de DD/MM/AAAA — redação dada pela
  <lei> (art. N)` marca redação futura; `## ❌ Revogado a partir de
  DD/MM/AAAA — <lei> (art. N)` marca revogação programada. O frontmatter
  `vigencia` e `texto-base` diz se a nota tem regra futura e de quando é o
  texto legal usado.
- **Domínio documentos-fiscais:** a NT entra em vigor por cronograma
  (homologação e produção). `## ⏳ Em produção a partir de DD/MM/AAAA — NT N
  vX (cronograma)` marca o que ainda não está em produção; a versão da NT
  usada fica no `fontes` do frontmatter. As NTs têm **texto riscado**
  (redação superada): use só os arquivos `*-vigente.txt`.

## Outras fontes de contexto

- **[fontes/](fontes/)**: PDFs oficiais e texto extraído (`texto/`), uma
  pasta por domínio, com `FONTE.md` registrando origem e data de captura.
- **[MEMORY.md](MEMORY.md)**: memória persistente entre conversas.
- **[LEARNINGS.md](LEARNINGS.md)**: aprendizados (armadilhas de
  interpretação, erros já corrigidos).
- **[decisions.md](decisions.md)**: decisões adotadas pela equipe.
- **[pendencias.md](pendencias.md)**: o que está em aberto (decisões da
  equipe a tomar, fontes que faltam, itens adiados).
- **[docs/perguntas-teste/](docs/perguntas-teste/)**: bateria de regressão
  por domínio.
- **`scripts/verificar.py`**: rode `python scripts/verificar.py` depois de
  criar, mover ou renomear qualquer nota. O resultado precisa ser 0 erros.

## Diretório `projetos/`

Reservado para aplicações práticas (calculadoras, simuladores etc.)
construídas a partir do conhecimento em `notas/`. Vazio até o momento.

Consulte sempre @MEMORY.md para contexto de fundo da equipe.
