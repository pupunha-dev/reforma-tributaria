# Expansão do second brain para múltiplas legislações — design

- **Data:** 2026-10-06
- **Status:** aprovado em 2026-10-06 (revisão 2: CGSN 140 como 2ª fonte do domínio Simples; travas de migração)
- **Primeiro caso:** domínio Simples Nacional — LC 123/2006 (fase A) + Resolução CGSN 140/2018 (fase B)

## 1. Objetivo

Hoje o second brain cobre um só domínio: a Reforma Tributária (LC 214/2025 + LC 227/2026), com 87 notas. A ideia é transformá-lo numa **biblioteca com várias leis**, para que ele:

- responda com mais precisão, porque cada lei tem escopo, índice e mapa de artigos próprios;
- cruze leis entre si (ex.: Simples Nacional × IBS/CBS);
- receba leis novas por um **procedimento repetível**, e não por improviso.

**Critérios de sucesso**

1. A estrutura migrada fica sem links quebrados e as 87 notas da reforma continuam respondendo como hoje.
2. A LC 123 fica coberta com mapa artigo → nota, aprovado antes da redação.
3. Nenhuma resposta apresenta uma redação futura como regra vigente (bateria de perguntas-teste).
4. A próxima lei entra seguindo `docs/procedimento-nova-legislacao.md`, sem precisar redesenhar nada.

**Premissas**: confirmadas ou delegadas pelo usuário em 2026-10-06.

- A LC 123 entra como **domínio completo**, para o dia a dia do fiscal, e não só como apoio à reforma.
- As notas trazem a **regra vigente hoje** e, separado, a **redação futura**, com data de início.
- A organização é **uma subpasta por domínio**, migrando também a reforma.
- O escopo continua sendo **só atos normativos federais**: leis complementares e atos infralegais federais, como resoluções do CGSN. Legislação estadual e municipal continua fora.
- **Domínio = assunto, não lei.** Um domínio pode reunir várias fontes. O Simples Nacional reúne a LC 123, que é a "constituição" do regime, e a Resolução CGSN 140, que é o "manual de operação".
- O repositório é `https://github.com/pupunha-dev/reforma-tributaria.git` (privado).

## 2. Arquitetura

### 2.1 Estrutura de pastas

```
CLAUDE.md                      ← protocolo + tabela curta de domínios
MEMORY.md, LEARNINGS.md, decisions.md   ← continuam globais (uma seção por domínio quando fizer sentido)
docs/
  procedimento-nova-legislacao.md       ← a receita (seção 3)
  perguntas-teste/<dominio>.md          ← bateria de perguntas por domínio
  superpowers/specs/                    ← specs de design
fontes/
  reforma/          lc-214-2025-texto-compilado.pdf, lc-227-2026.pdf, FONTE.md
  simples-nacional/ lc-123-2006-texto-compilado.pdf, resolucao-cgsn-140-2018-compilada.pdf, FONTE.md
notas/
  INDEX.md                    ← índice MESTRE: um bloco por domínio, com link para o índice de cada um
  reforma/                    ← as 87 notas atuais (sem mudar o nome dos arquivos)
    INDEX.md, _plano-notas.md
  simples-nacional/
    INDEX.md, _plano-notas.md, sn-*.md
scripts/
  verificar.py                ← checagens automáticas (seção 2.5)
projetos/                     ← sem mudança
```

**Por que assim:** cada domínio funciona como um "módulo" com sua própria fronteira: fontes, plano, índice e notas. O índice mestre e o CLAUDE.md fazem só o roteamento, como um API gateway que aponta para o serviço certo sem conhecer o que tem dentro dele. Com isso, entrar uma lei nova não mexe nas notas das outras.

### 2.2 Convenções de nome e de links

- **Nome de arquivo único no projeto inteiro.** Os links `[[nome]]` resolvem pelo nome, e não pelo caminho, então duas notas com o mesmo nome criariam ambiguidade. O `verificar.py` bloqueia nomes repetidos.
- **Prefixo por domínio nas notas novas**: `sn-` para o Simples Nacional. As próximas seguem o mesmo padrão, com prefixo curto e definido no `_plano-notas.md` do domínio. As notas da reforma **não** ganham prefixo, para não quebrar os 87 nomes e os links já existentes.
- **Links entre notas:** sempre `[[nome]]`. Links Markdown com caminho (`[x](notas/...)`) só aparecem em INDEX, CLAUDE.md, LEARNINGS e decisions, e o script também confere esses.

### 2.3 Frontmatter padrão (notas de domínios novos)

```yaml
---
título: Fator R e enquadramento nos Anexos III/V
dominio: simples-nacional
fontes: LC 123/2006, arts. 18 §§5º-J a 5º-M; Res. CGSN 140/2018, arts. 25-26
vigencia: atual | com-mudanca-programada
texto-base: 2026-10-06        # data em que o PDF de fontes/ foi capturado
---
```

Os campos `vigencia` e `texto-base` mostram, já no cabeçalho, se a nota tem regra com data futura e de quando é o texto legal usado. Assim dá para saber quando é preciso revisar uma nota.

### 2.4 Padrão de vigência no corpo das notas

- O corpo principal descreve a **regra vigente na data do `texto-base`**.
- A redação futura entra num bloco próprio, sempre neste formato:

  ```markdown
  ## ⏳ A partir de 01/01/2027 — redação dada pela LC 214/2025 (art. 516)
  ```

  Esse bloco explica o que muda e liga para a nota da reforma que trata do assunto (normalmente `[[simples-nacional-e-mei]]`).
- Dispositivo revogado com data marcada: `## ❌ Revogado a partir de DD/MM/AAAA — LC 227/2026 (art. 181, IV)`.
- A legenda 🔵🟡🟢 continua **exclusiva do domínio reforma**. Os marcadores ⏳/❌ valem para **todos** os domínios.

### 2.5 `scripts/verificar.py`

Script em Python que usa só a biblioteca padrão e é executado com `python scripts/verificar.py`. Ele faz quatro checagens:

1. **Links**: todo `[[nome]]` precisa achar exatamente um arquivo, e todo link Markdown precisa apontar para um caminho que existe.
2. **Nomes únicos**: não pode haver dois `.md` com o mesmo nome dentro de `notas/`.
3. **Frontmatter**: as notas fora de `reforma/` precisam ter `título`, `dominio`, `fontes`, `vigencia` e `texto-base`.
4. **Cobertura**: todo arquivo citado no `_plano-notas.md` do domínio precisa existir, e toda nota do domínio precisa aparecer no plano.

O script devolve código de saída diferente de zero quando acha algum erro. Ele roda no fim de cada etapa do procedimento.

## 3. Procedimento padrão para nova legislação

Fica registrado em `docs/procedimento-nova-legislacao.md`.

| # | Etapa | Entrega | Verificação |
|---|---|---|---|
| 1 | Fonte | PDF compilado em `fontes/<dominio>/` + `FONTE.md` (URL oficial, data de captura, última lei alteradora vista no texto) | O arquivo existe e o `FONTE.md` está preenchido |
| 2 | Extração | `.txt` (PyMuPDF; OCR se não houver camada de texto) + esqueleto Livro/Título/Capítulo/Seção/Artigo, no scratchpad | O número de artigos extraídos bate com o último artigo da lei |
| 3 | Mapa de vigência | Lista de dispositivos com redação futura ou revogação programada: dispositivo, data, lei alteradora | Toda marca "(Redação dada…)"/"(Vigência…)"/"(Revogado…)" com data futura entra na lista |
| 4 | Plano de notas | `notas/<dominio>/_plano-notas.md` (arquivo → artigos → nível de profundidade) | **Aprovação do usuário** antes da etapa 5 |
| 5 | Redação | Notas no padrão das seções 2.3 e 2.4: didáticas, com artigos citados e fórmulas descritas por completo | `verificar.py` (cobertura + frontmatter) |
| 6 | Ligações | `INDEX.md` do domínio + bloco no índice mestre + `[[...]]` cruzados com outros domínios | `verificar.py` (links) |
| 7 | Protocolo | Linha nova na tabela de domínios do CLAUDE.md; bloco no MEMORY.md | Bateria `docs/perguntas-teste/<dominio>.md` |

**Atualização de uma lei já registrada** (o texto compilado muda): faça de novo as etapas 1 a 3, compare com o mapa de vigência anterior, revise só as notas afetadas e atualize o `texto-base` delas.

## 4. Aplicação à LC 123/2006

### 4.1 Níveis de profundidade

Nem toda a LC 123 pesa igual para um escritório contábil. A profundidade das notas acompanha a frequência das perguntas:

| Nível | Matéria (arts. aproximados, a confirmar na etapa 2) | Tratamento |
|---|---|---|
| **1. Profundo** | Definição de ME/EPP (3º); inscrição e baixa (4º–11); Simples Nacional: abrangência, vedações, cálculo, Anexos, Fator R, sublimites, MEI, recolhimento, créditos, obrigações acessórias, exclusão, fiscalização, omissão de receita, processo (12–41); Anexos I–V | Uma nota por tema, com fórmulas completas e tabelas transcritas |
| **2. Médio** | Acesso a mercados/licitações (42–49); simplificação trabalhista (50–54); fiscalização orientadora (55) | Uma nota por capítulo |
| **3. Resumo** | Associativismo, crédito/capitalização, inovação, regras civis/empresariais, acesso à justiça, apoio e representação, disposições finais | 1 ou 2 notas de visão geral |

### 4.2 Esboço preliminar de notas (fechado na etapa 4)

`sn-conceitos-definicao-me-epp`, `sn-inscricao-baixa`, `sn-abrangencia-tributos`, `sn-vedacoes-ingresso`, `sn-calculo-aliquota-efetiva`, `sn-anexos-tabelas` (pode ser dividida por anexo), `sn-fator-r`, `sn-sublimites-icms-iss`, `sn-segregacao-receitas` (monofásico, ST, exportação), `sn-mei`, `sn-recolhimento-das`, `sn-creditos-adquirente`, `sn-obrigacoes-acessorias`, `sn-exclusao-opcao`, `sn-fiscalizacao-omissao-receita`, `sn-processo-contencioso`, `sn-acesso-mercados-licitacoes`, `sn-simplificacao-trabalhista`, `sn-fiscalizacao-orientadora`, `sn-demais-disposicoes`. São cerca de 20 a 25 notas.

### 4.3 Precisão numérica (Anexos e fórmulas)

- As tabelas dos Anexos são **transcritas literalmente** em Markdown e **conferidas duas vezes** contra o PDF: uma na extração e outra lendo a página renderizada. Um número errado numa faixa de alíquota é o tipo de erro que mais custa caro.
- As fórmulas aparecem por completo dentro da nota. Exemplo de formato: alíquota efetiva = (RBT12 × Alíq. nominal − Parcela a deduzir) ÷ RBT12, explicando cada variável. Fator R = folha de salários dos 12 meses ÷ RBT12, com o limite de 28% e o efeito de cada lado do limite.
- Anexos atuais (I–V da LC 123) e futuros (XVIII–XXII da LC 214, que substituem os atuais) ficam em **blocos separados**: o atual no corpo e o futuro num bloco ⏳ com a data de início.

### 4.4 Relação com a nota-ponte da reforma

`notas/reforma/simples-nacional-e-mei.md` continua sendo a **ponte**: explica *o que a reforma muda no Simples* e liga para as notas `sn-*` correspondentes. A regra detalhada fica nas notas `sn-*`, e a ponte não duplica esse conteúdo. As notas `sn-*` com bloco ⏳ apontam de volta para a ponte.

### 4.5 Fase B: Resolução CGSN 140/2018 no mesmo domínio

- **Ordem:** a fase B começa só depois que a fase A (LC 123) estiver concluída. Nela a resolução passa pelas etapas 1 a 4 do procedimento. O plano da fase B diz quais notas `sn-*` **ganham uma seção de detalhamento** e quais **notas novas** são necessárias, só para matéria própria da resolução. Esse plano também passa por aprovação.
- **Hierarquia:** a LC vem primeiro na nota e a resolução detalha. Se as duas disserem coisas diferentes, **a LC prevalece**, e a nota sinaliza o conflito com `> ⚠️ Conflito LC × Resolução: ...`.
- **Versão da fonte:** só serve a versão **compilada/consolidada** do Sijut2 da Receita (normas.receita.fazenda.gov.br, "visão compilado"). Em 2026-10-06 constatou-se que o PDF em `fontes/resolucao-cgsn-140-2018.pdf` é a **publicação original do DOU (24/05/2018)**, sem nenhuma marca de alteração posterior. Ele precisa ser substituído antes da fase B. O `FONTE.md` registra a resolução alteradora mais recente que aparece no texto.
- Até a fase B terminar, perguntas que dependem só da resolução são respondidas como **lacuna**.

### 4.6 Fora do escopo deste domínio (registrar como lacuna, não "chutar")

- Legislação estadual e municipal (ex.: regras próprias de sublimite e ICMS-ST por UF), seguindo o escopo atual.
- IRPJ/CSLL fora do Simples, folha e INSS patronal fora do que a LC 123 trata.

## 5. Mudanças no protocolo (CLAUDE.md e MEMORY.md)

- A seção **Escopo** vira uma **tabela de domínios**: domínio, leis, pasta, prefixo e status. O caso especial da ST continua, agora dentro do domínio reforma.
- O **mapa de navegação** detalhado sai do CLAUDE.md e vai para os INDEX de cada domínio. O CLAUDE.md fica só com o roteamento, e não cresce a cada lei nova.
- Regras novas do protocolo:
  - **R-domínio:** identificar primeiro a qual domínio (ou domínios) a pergunta pertence e procurar no índice desse domínio.
  - **R-vigência:** ao citar uma regra de nota com `vigencia: com-mudanca-programada`, dizer se ela vale **hoje** ou **a partir de quando**, e nunca misturar as duas.
  - **R-hierarquia:** quando uma lei e um ato infralegal tratam do mesmo ponto, citar os dois. Se houver conflito, a lei prevalece.
  - **R-cruzamento:** pergunta que envolve dois domínios (ex.: Simples × IBS/CBS) usa as notas dos dois e cita ambas.
- O MEMORY.md registra que o second brain passou a ter vários domínios e lista os domínios ativos.
- As regras atuais 1 a 6 continuam iguais.

## 6. Testes

- **Estruturais:** `scripts/verificar.py` sem erros depois da migração e no fim de cada etapa.
- **Regressão da reforma:** de 5 a 8 perguntas já respondidas antes (ex.: a lacuna dos arts. 353–365, a ST fora de escopo, o IR em imóveis) precisam continuar dando a mesma resposta depois da migração.
- **Bateria do Simples** (`docs/perguntas-teste/simples-nacional.md`): de 10 a 15 perguntas, cada uma com a nota e o artigo esperados, cobrindo:
  - cálculo da alíquota efetiva com números;
  - Fator R no limite de 28%;
  - vedação de ingresso;
  - **armadilha de vigência**: pergunta sobre o DAS "hoje" que não pode trazer a regra de 2027;
  - **cruzamento**: crédito de IBS/CBS para quem compra de optante do Simples;
  - **lacuna**: detalhe que só existe na Resolução CGSN;
  - **fora de escopo**: sublimite estadual específico.

## 7. Riscos e mitigação

| Risco | Mitigação |
|---|---|
| A migração quebra links ou perde conteúdo | (a) commit + push do estado atual antes de migrar, como rollback; (b) script de comparação: o conteúdo de cada nota antes e depois só pode diferir em linhas de link com caminho; (c) contagem de 87 notas com os mesmos nomes; (d) `verificar.py` sem erros; (e) perguntas de regressão |
| O texto compilado do Planalto envelhece | `texto-base` em cada nota + `FONTE.md` com data + procedimento de atualização (seção 3) |
| Erro de transcrição nos Anexos | Dupla conferência (4.3) + perguntas-teste com valores numéricos |
| O PDF da LC 123 não tem camada de texto | Usar o mesmo pipeline de OCR já usado na LC 227 (RapidOCR + páginas renderizadas para conferência) |

## 8. Ordem de execução (base para o plano)

1. `git init` + commit do estado atual + push para o GitHub (feito em 2026-10-06).
2. Criar `scripts/verificar.py` e rodar no estado atual, como linha de base.
3. Migrar a reforma para `notas/reforma/` e `fontes/reforma/`, criar o índice mestre e ajustar os links. `verificar.py` precisa passar sem erros, e a regressão também.
4. Reescrever o CLAUDE.md (tabela de domínios + regras novas) e atualizar o MEMORY.md.
5. Escrever `docs/procedimento-nova-legislacao.md`.
6. LC 123, etapas 1 a 4 do procedimento, **parando para aprovação do plano de notas**.
7. LC 123, etapas 5 a 7, e bateria de perguntas-teste (fim da fase A).
8. Fase B (CGSN 140): substituir o PDF pela versão compilada, rodar as etapas 1 a 4 com aprovação do plano e depois as etapas 5 a 7.
