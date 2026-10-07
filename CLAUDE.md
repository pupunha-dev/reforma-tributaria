# Second brain tributário — Guia do projeto

Base de conhecimento do setor fiscal sobre **legislação tributária
federal**, organizada por **domínio** (assunto). Todo o conhecimento
factual vive em notas Markdown em `notas/<dominio>/`, com base nos textos
oficiais de `fontes/<dominio>/`.

## Domínios

| Domínio | Atos normativos | Notas | Fontes | Prefixo | Status |
|---|---|---|---|---|---|
| reforma | LC 214/2025 + LC 227/2026 | `notas/reforma/` | `fontes/reforma/` | — | ativo (88 notas) |
| simples-nacional | LC 123/2006 (fase A) + Res. CGSN 140/2018 e alteradoras, como as Res. CGSN 190 e 191/2026 (fase B) | `notas/simples-nacional/` | `fontes/simples-nacional/` | `sn-` | ativo — fase A (28 notas da LC 123); fase B (Res. CGSN) pendente |

- Índice mestre: **[notas/INDEX.md](notas/INDEX.md)**. Cada domínio tem
  `INDEX.md` (notas por tema) e `_plano-notas.md` (mapa artigo → nota).
- Para incluir um domínio ou uma fonte nova, siga
  [docs/procedimento-nova-legislacao.md](docs/procedimento-nova-legislacao.md).

## Escopo

**Só atos normativos federais listados na tabela de domínios**: leis
complementares, leis e atos infralegais federais, como resoluções do
CGSN. Ficam fora: legislação estadual e municipal (convênios, protocolos,
ITBI/IPTU municipal etc.) e tributos ou regimes que esses atos não tratam
(ex.: IRPF e IRPJ pelo lucro real/presumido; o IRPJ **dentro** do Simples
Nacional é matéria da LC 123 e está no escopo). Perguntas sobre esses temas ficam fora do escopo das
notas, mesmo quando parecem relacionadas.

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
8. **Hierarquia (R-hierarquia).** Quando uma lei e um ato infralegal
   tratarem do mesmo ponto, cite os dois. Se houver conflito, a lei
   prevalece e o conflito é sinalizado.
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

## Outras fontes de contexto

- **[fontes/](fontes/)**: PDFs oficiais e texto extraído (`texto/`), uma
  pasta por domínio, com `FONTE.md` registrando origem e data de captura.
- **[MEMORY.md](MEMORY.md)**: memória persistente entre conversas.
- **[LEARNINGS.md](LEARNINGS.md)**: aprendizados (armadilhas de
  interpretação, erros já corrigidos).
- **[decisions.md](decisions.md)**: decisões adotadas pela equipe.
- **[docs/perguntas-teste/](docs/perguntas-teste/)**: bateria de regressão
  por domínio.
- **`scripts/verificar.py`**: rode `python scripts/verificar.py` depois de
  criar, mover ou renomear qualquer nota. O resultado precisa ser 0 erros.

## Diretório `projetos/`

Reservado para aplicações práticas (calculadoras, simuladores etc.)
construídas a partir do conhecimento em `notas/`. Vazio até o momento.

Consulte sempre @MEMORY.md para contexto de fundo da equipe.
