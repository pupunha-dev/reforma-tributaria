# Reforma Tributária (LC 214/2025 + LC 227/2026) — Guia do projeto

Este projeto documenta a Reforma Tributária do consumo (IBS, CBS, IS, ITCMD,
CGIBS) a partir do texto compilado da **LC 214/2025** e das alterações
trazidas pela **LC 227/2026**. Todo o conhecimento factual vive em arquivos
Markdown em `notas/`, com base nos PDFs de `fontes/`.

**Escopo: só legislação federal.** O second brain cobre exclusivamente a
LC 214/2025 e a LC 227/2026 (nível federal). Não cobre convênios,
protocolos ou legislação estadual/municipal — ex.: legislação municipal
de ITBI/IPTU. Perguntas sobre esses temas ficam fora do escopo das
notas, mesmo quando parecem relacionadas à reforma.

**Caso especial — substituição tributária (ST):** a exclusão de escopo
vale especificamente para **listas de produtos/setores sujeitos a ST
definidas por convênio ou legislação estadual** (ex.: convênios ICMS
142/2018 e correlatos) — isso é fora de escopo. Já a **explicação
conceitual de como o desenho da reforma (split payment, não
cumulatividade) torna a lógica de ST desnecessária** é matéria federal
(LC 214/227) e está coberta em `ibs-cbs-fim-substituicao-tributaria.md`
— isso está dentro do escopo normal. Quando uma pergunta misturar as
duas partes, responda a parte conceitual com base nas notas e sinalize
apenas a parte da lista de produtos/setores como fora de escopo — não
recuse a pergunta inteira.

## Regras de resposta (protocolo)

1. **Responda só com base no que está escrito nos arquivos deste projeto**
   (`notas/`, `fontes/`, `MEMORY.md`, `LEARNINGS.md`, `decisions.md`).
   Não complete lacunas com conhecimento geral sobre reforma tributária —
   a lei tem detalhes e exceções específicas que não podem ser "chutados".
2. **Sempre cite o arquivo-fonte** da informação usada na resposta
   (ex.: `ibs-cbs-aliquotas.md`), e o artigo da LC quando a nota indicar.
3. **Se a informação não estiver nas notas**, diga isso explicitamente —
   não invente. Nesse caso, ofereça consultar diretamente o PDF em
   `fontes/` (LC 214 ou LC 227) e, se fizer sentido, propor criar/atualizar
   uma nota depois.
4. Ao explicar uma regra ou fórmula de cálculo, descreva-a por completo
   (não apenas "veja a nota X") — está no estilo de trabalho do usuário.
5. **Critério para registrar em LEARNINGS.md**: só vale a pena registrar
   algo como aprendizado se pelo menos uma destas condições for
   verdadeira — (1) revelou uma lacuna real numa nota existente,
   (2) expôs uma interpretação que precisou ser corrigida, ou (3) é um
   padrão que provavelmente vai se repetir. Não registrar detalhes
   triviais de uma única sessão.
6. **Critério para registrar em decisions.md**: só registrar quando a
   equipe efetivamente adotou uma posição — especialmente em pontos
   onde a lei é ambígua, ainda não regulamentada, ou permite mais de
   uma interpretação válida. Não registrar hipóteses discutidas, opções
   cogitadas e descartadas, ou dúvidas ainda em aberto — essas ficam de
   fora até haver decisão real.

## Legenda usada nas notas

🔵 só LC 214/2025 · 🟡 tema presente nas duas (LC 227 alterou dispositivo
da LC 214) · 🟢 só LC 227/2026 (matéria nova, ex.: CGIBS, PAT-IBS, ITCMD)

## Mapa de navegação por tema

O índice completo e atualizado das 87 notas vive em
**[notas/INDEX.md](notas/INDEX.md)** — use-o como fonte de verdade para
achar o arquivo certo. Áreas cobertas:

1. **Núcleo IBS/CBS** — incidência, imunidades, fato gerador, local da
   operação, base de cálculo, alíquotas, sujeição passiva, split payment,
   não cumulatividade/créditos, cadastro e documento fiscal.
2. **Comércio exterior** — importação, exportação, regimes aduaneiros
   especiais, zonas de processamento de exportação, bens de capital
   (Reporto, Reidi, Renaval).
3. **Cashback e cesta básica** — devolução a pessoas físicas, cesta
   básica nacional.
4. **Regimes diferenciados** — reduções de alíquota (30%/60%) por setor,
   alíquota zero, transporte público, reabilitação urbana, produtor rural.
5. **Regimes específicos** — combustíveis, serviços financeiros, planos
   de saúde, bens imóveis, cooperativas, bares/hotelaria/turismo, SAF,
   disposições comuns aos regimes.
6. **Administração, contencioso e penalidades** — competência normativa,
   harmonização e consulta tributária, contencioso integrado (recurso
   especial), fiscalização/lançamento de ofício, infrações e penalidades.
7. **Transição para IBS/CBS** — cronograma de alíquotas 2026-2035,
   compras governamentais, saldo credor de PIS/COFINS, Fundo de
   Compensação de benefícios fiscais de ICMS, bens de capital.
8. **Imposto Seletivo (IS)** — incidência, base de cálculo/alíquotas,
   sujeição passiva/apuração, importação.
9. **Demais disposições da LC 214** — ZFM/ALC, devolução a turista
   estrangeiro, PNCT, penalidades não tributárias, compras
   governamentais, avaliação quinquenal, CGIBS na LC 214, Simples
   Nacional/MEI, alterações em outras leis, revogações/vigência.
10. **CGIBS, processo administrativo e ITCMD (matéria nova da LC 227)** —
    natureza/estrutura/controle/orçamento do CGIBS; PAT-IBS (normas,
    contencioso, recursos, órgãos de julgamento); distribuição de
    receita do IBS; ITCMD (fato gerador, base, competência).
11. **Legislação correlata (LC 227)** — alterações em ITBI, COSIP,
    cota-parte do ICMS, Fundeb, crimes de responsabilidade, PAF federal,
    AFRMM etc.

Para o mapeamento artigo-por-artigo de qual nota cobre qual dispositivo,
veja [notas/_plano-notas.md](notas/reforma/_plano-notas.md).

## Outras fontes de contexto

- **[fontes/](fontes/)** — PDFs originais: `lc-214-2025-texto-compilado.pdf`
  e `lc-227-2026.pdf`. Consulte diretamente quando uma nota não cobrir o
  dispositivo perguntado, ou para conferir a redação literal de um artigo.
- **[MEMORY.md](MEMORY.md)** — memória persistente entre conversas sobre
  este projeto (decisões de escopo, preferências de trabalho, etc.).
- **[LEARNINGS.md](LEARNINGS.md)** — aprendizados acumulados durante a
  elaboração das notas (armadilhas de interpretação, erros já corrigidos).
- **[decisions.md](decisions.md)** — decisões tomadas sobre como
  estruturar/nomear as notas e como tratar conflitos entre LC 214 e LC 227.

## Diretório `projetos/`

Reservado para aplicações práticas da reforma (calculadoras, simuladores,
etc.) construídas a partir do conhecimento em `notas/`. Vazio até o momento.

Consulte sempre @MEMORY.md para contexto de fundo da equipe.