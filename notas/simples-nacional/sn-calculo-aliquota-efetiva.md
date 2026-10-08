---
título: Cálculo do Simples Nacional — RBT12, alíquota nominal e alíquota efetiva
dominio: simples-nacional
fontes: LC 123/2006, art. 18, caput, §§1º a 3º e 15 a 23 (redação da LC 155/2016); LC 214/2025, arts. 517 e 543; Res. CGSN 140/2018, arts. 16 a 23, 31 a 37, 77 e 78; Res. CGSN 190/2026, arts. 1º e 8º
vigencia: com-mudanca-programada
texto-base: 2026-10-07
---

# RBT12, alíquota nominal e alíquota efetiva

## A lógica em uma frase

O Simples é **progressivo por faixas, sem degrau**: a tabela do Anexo dá uma
alíquota nominal e uma "parcela a deduzir" para cada faixa de faturamento dos
últimos 12 meses, e a fórmula transforma isso numa **alíquota efetiva** que
cresce de forma suave. Funciona como a tabela do IR da pessoa física: quem
passa de faixa paga a alíquota maior só "na margem", e não sobre tudo.

## O caminho do cálculo (art. 18)

1. **Classificar a receita do mês** por tipo de atividade e Anexo (§4º). Ver
   [[sn-segregacao-receitas]].
2. **Apurar o RBT12**: receita bruta acumulada nos **12 meses anteriores ao do
   período de apuração** (§1º e §1º-A, I).
3. **Achar a faixa** do RBT12 no Anexo da atividade e ler a **alíquota
   nominal (Aliq)** e a **parcela a deduzir (PD)** (§1º-A, II e III).
4. **Calcular a alíquota efetiva** (§1º-A):

> **Alíquota efetiva = (RBT12 × Aliq − PD) ÷ RBT12**
>
> - **RBT12**: receita bruta acumulada nos doze meses anteriores ao período de apuração;
> - **Aliq**: alíquota nominal do Anexo (I a V) para a faixa do RBT12;
> - **PD**: parcela a deduzir do mesmo Anexo e faixa.

5. **Aplicar a alíquota efetiva sobre a receita bruta do mês** (§3º): o valor
   do DAS da atividade = receita do mês × alíquota efetiva.
6. **Repartir entre os tributos** (§1º-B): o percentual efetivo de cada tributo
   = alíquota efetiva × **percentual de repartição** do Anexo para a faixa.
   - O percentual efetivo do **ISS** fica limitado a **5%**; o excesso passa,
     proporcionalmente, aos **tributos federais** da mesma faixa (§1º-B, I).
   - Diferença de centavo entre a soma dos percentuais e a alíquota efetiva vai
     para o tributo de **maior** percentual de repartição na faixa (§1º-B, II).

<!-- exemplo -->
**Exemplo (números ilustrativos, não da lei):** comércio (Anexo I), RBT12 =
R$ 600.000,00. A faixa é a 3ª (de 360.000,01 a 720.000,00), com Aliq = 9,50% e
PD = R$ 13.860,00 (ver [[sn-anexo-i-comercio]]).

Alíquota efetiva = (600.000,00 × 9,50% − 13.860,00) ÷ 600.000,00
= (57.000,00 − 13.860,00) ÷ 600.000,00 = 43.140,00 ÷ 600.000,00 ≈ **7,19%**.

Com receita de R$ 50.000,00 no mês, o DAS dessa atividade ≈ 50.000,00 × 7,19%
≈ R$ 3.595,00.
<!-- /exemplo -->

## Regime de competência ou de caixa (§3º)

A regra é a receita **auferida** no mês (competência). Por opção do
contribuinte, na forma do CGSN, a alíquota pode incidir sobre a receita
**recebida** no mês (caixa). A opção é **irretratável para todo o ano** (§3º).
**Atenção:** a opção pelo regime de caixa **deixa de existir a partir de
01/01/2027** (ver bloco ⏳ abaixo).

## Início de atividade (§2º)

No início de atividade, os valores de receita bruta das tabelas dos Anexos I a
V são **proporcionalizados** ao número de meses de atividade no período (§2º).

## Excesso de receita: tributação da parcela excedente (§§16 a 17-A)

- No ano de início de atividade, se o excesso sobre o limite proporcional não
  passar de 20% (art. 3º, §12), a parcela excedente fica sujeita às
  **alíquotas máximas** dos Anexos I a V, proporcionalmente (§16). O mesmo vale
  nas hipóteses do art. 3º, §9º (excesso do limite de EPP), do mês do excesso
  até o mês anterior aos efeitos da exclusão (§16-A).
- Para os **sublimites estaduais** (art. 3º, §13, e art. 20, §1º), a parcela
  que exceder fica sujeita, **quanto a ICMS e ISS**, às alíquotas máximas
  correspondentes (§§17 e 17-A). Ver [[sn-sublimites-icms-iss]].

## ICMS e ISS: valores fixos, isenções e reduções locais (§§18 a 21)

- Estados, DF e Municípios podem fixar **valores fixos mensais** de ICMS e ISS
  para a **microempresa** com receita, no ano anterior, até o limite da
  **2ª faixa** dos Anexos (§18). Ultrapassado esse limite no ano, ela sai do
  valor fixo no mês seguinte (§18-A). O valor fixo não pode passar de **50%**
  do maior recolhimento possível do tributo na faixa (§19).
- Isenção ou redução de ICMS/ISS, ou valor fixo, concedidos pelo ente geram
  **redução proporcional** do valor a recolher, na forma do CGSN (§20); podem
  ser dadas unilateralmente e por ramo de atividade (§20-A). Em caso de
  isenção, o valor não entra na partilha com aquele ente (§21).
- União, Estados e DF podem dar, por lei específica, isenção ou redução de
  Cofins, PIS/Pasep e ICMS para produtos da **cesta básica** vendidos por
  optantes (§20-B).

## Escritórios contábeis no Simples (§§22-A a 22-C)

Os escritórios de serviços contábeis (Anexo III, art. 18, §5º-B, XIV):

- recolhem o **ISS em valor fixo**, pela lei municipal (§22-A);
- devem, individualmente ou por suas entidades de classe (§22-B):
  - dar **atendimento gratuito** para inscrição, opção pelo MEI e primeira
    declaração anual do MEI;
  - fornecer ao CGSN resultados de pesquisas sobre as ME/EPP que atendem;
  - promover eventos de orientação fiscal, contábil e tributária;
- se descumprirem, são **excluídos** do Simples a partir do mês seguinte
  (§22-C).

## Sistema de cálculo e confissão de dívida (§§15 e 15-A)

O cálculo é feito em **sistema eletrônico** (§15). As informações prestadas
nele têm caráter **declaratório**, constituem **confissão de dívida** e são
título suficiente para cobrar o que não foi pago (§15-A, I). Devem ser
enviadas à Receita Federal até o vencimento do DAS do mês, sobre os fatos do
mês anterior (§15-A, II). Ver [[sn-obrigacoes-acessorias]].

## ⏳ A partir de 01/01/2027 — redação dada pela LC 214/2025 (art. 517)

Fundamento da data: LC 214, art. 544, III. Texto **ainda não incorporado** ao
compilado da LC 123 no Planalto; a fonte é o art. 517 da LC 214, com a
redação da LC 227:

- **RBT12 muda de janela:** passa a ser a receita bruta acumulada nos **doze
  meses antecedentes ao mês anterior** ao do período de apuração (art. 18, §1º
  e §1º-A, I). Ou seja, há um mês de defasagem a mais na janela de 12 meses.
- **Teto do ISS:** o excesso acima de 5% no percentual efetivo do ISS passa a
  ser transferido aos **tributos federais e ao IBS** da mesma faixa (§1º-B, I,
  incluído pela LC 227).
- **Excesso de sublimite e IBS:** na hipótese do art. 3º, §13, a parcela
  excedente, quanto aos percentuais do **IBS**, é tributada **junto** com a
  parcela que não excede, pelas alíquotas efetivas do §1º-A (§17-B); o mesmo se
  aplica ao excesso do limite do art. 13-A, do mês do excesso até o mês anterior
  aos efeitos do impedimento (§17-C).
- **Revogado a partir de 01/01/2027:** o §15-A (caráter declaratório e
  confissão de dívida das informações do sistema de cálculo), pela LC 214, art.
  542, XXXVI, "f". A regra passa a constar do novo art. 25 (declaração e
  declaração assistida); ver [[sn-obrigacoes-acessorias]].
- **Fim do regime de caixa (§3º):** a nova redação diz só que "sobre a receita
  bruta **auferida** no mês incidirá a alíquota efetiva", **sem** a opção de
  tributar a receita recebida. Coerente com isso, é revogado o inciso IV do §4º
  do art. 23 (vedação de crédito ao comprador quando o optante usa o regime de
  caixa) (LC 214, art. 542, XXXVI, "c"). Ver [[sn-creditos]].
- **Excesso de receita (§§16 e 17):** a parcela que exceder o limite
  proporcional do início de atividade (§16) ou, quanto a ICMS e ISS, o sublimite
  (§17, observado o §17-B) passa a ser **tributada conjuntamente com a parcela
  que não o exceder, conforme as alíquotas efetivas do §1º-A**, e não mais
  pelas alíquotas máximas.
- A fórmula da alíquota efetiva (§1º-A) fica mantida; os percentuais de repartição passam a conter **CBS e IBS** nos novos
  Anexos (ver [[sn-anexo-i-comercio]] a [[sn-anexo-v-servicos]]).

## ❌ Revogado a partir de 01/01/2033 — LC 214/2025 (art. 543, V, "b")

Fundamento da data: LC 214, art. 544, V. São revogados do art. 18 o §5º-E e
os **§§14, 17, 17-A, 22-A e 23**, ou seja, as regras de excesso de sublimite
quanto a ICMS e ISS (§§17 e 17-A), o ISS em valor fixo dos escritórios
contábeis (§22-A) e o abatimento de material na base do ISS (§23).

## Regulamentação (Res. CGSN 140/2018)

- **Base de cálculo (art. 16):** receita bruta total mensal **auferida**
  (competência) ou **recebida** (caixa), irretratável no ano (§1º), somando
  todos os estabelecimentos (§2º), segregada por tipo de receita (art. 25) e
  com mercado interno e exportação em bases separadas (§3º).
- **Devolução e cancelamento (arts. 17 e 18):** a mercadoria devolvida em mês
  posterior à venda é **deduzida da receita do mês da devolução**, segregada pelas
  regras desse mês, e o saldo que sobrar vai para os meses seguintes (art. 17);
  no regime de caixa, limitada ao valor efetivamente devolvido (parágrafo
  único). Documento fiscal cancelado é deduzido no período em que foi tributado;
  o documento que o substituir é tributado no período da operação original (art.
  18).
- **Escolha do regime de caixa (art. 19):** registrada no Portal ao apurar
  **novembro** (para o ano seguinte, se já optante), **dezembro** (início de
  atividade com efeitos em dezembro) ou o mês de início dos efeitos da opção (nos
  demais casos). Ela vale **só para a base de cálculo mensal**: para todo o resto,
  inclusive a faixa de receita, vale a competência (parágrafo único). Optante pelo
  caixa: parcelas a prazo **não vencidas** entram na base até o último mês do
  ano-calendário seguinte ao da operação, e o auferido e não recebido entra na
  base no encerramento, no retorno à competência ou no mês anterior à exclusão
  (art. 20). Deve manter **registro dos valores a receber** (modelo do Anexo IX:
  documento, valor, parcelas, recebimentos, saldo e créditos incobráveis), sob
  pena de **desconsideração de ofício** do regime de caixa e recálculo pela
  competência (arts. 77 e 78).
- **Fórmula (art. 21):** alíquota efetiva = (RBT12 × Aliq − PD) ÷ RBT12, com
  RBT12 dos 12 meses anteriores ao período de apuração (II); percentual efetivo de
  cada tributo = alíquota efetiva × percentual de repartição, com ISS limitado a
  5% e o excesso transferido aos tributos federais (III, "a"). Se a RBT12 for
  **zero**, considera-se **R$ 1,00** só para achar a alíquota (parágrafo único).
  Quando a RBT12 passa do limite da 5ª faixa sem estourar o sublimite, o
  percentual de ICMS e ISS segue a fórmula do inciso III, "b", com o percentual de
  distribuição da 5ª faixa (o numerador da fração não ficou legível no texto
  extraído; ver a redação de 2027 abaixo).
- **Início de atividade (art. 22):** no **1º mês**, RBT12 = receita do mês × 12
  (§2º); nos **11 meses seguintes**, RBT12 = média aritmética da receita dos meses
  anteriores × 12 (§3º). Quem começou no ano anterior ao da opção usa a média até
  completar 12 meses e a regra geral a partir do 13º (§4º). Usam-se as
  **últimas faixas** dos Anexos quando a RBT12 passa do limite anual mas a receita
  do ano em curso não (§5º). Mercado interno e exportação, em separado (art. 23).
- **Isenções, reduções e valores fixos de ICMS/ISS (arts. 31 a 36):** Estados,
  DF e Municípios podem dar isenção ou redução, inclusive só para um ramo de
  atividade, ou fixar **valores fixos** (arts. 31 e 32). Para o **ISS**, o
  benefício não pode resultar em percentual **menor que 2%**, salvo os
  subitens 7.02, 7.05 e 16.01 da lista da LC 116/2003 (art. 31, parágrafo único). Valores fixos mensais
  máximos, para ME com receita no ano anterior de **até R$ 180.000,00**: ICMS
  R$ 108,00 e ISS R$ 162,75; **entre R$ 180.000,00 e R$ 360.000,00**: ICMS
  R$ 295,50 e ISS R$ 427,50 (art. 33, §2º). Valem só a partir do ano seguinte e
  por faixa (§1º). Ficam fora a ME com mais de um estabelecimento, no ano de
  início de atividade ou com ramos de atividade de regimes diferentes (§3º).
  Excedido o limite, sai do valor fixo no mês seguinte (§9º). Isenção ou redução
  específica gera **redução proporcional** dos percentuais de ICMS ou ISS (art.
  35); isenção ou redução de Cofins, PIS/Pasep ou ICMS da **cesta básica**, por lei
  específica, segue a mesma lógica (art. 36). Escritórios contábeis: ISS em valor
  fixo (art. 34). Nenhum incentivo fiscal fora do previsto (art. 37).

## ⏳ A partir de 01/01/2027 — Res. CGSN 190/2026 (arts. 1º e 8º; Res. 140, arts. 16 a 22, 36, 77 e 78)

Fundamento da data: Res. 190, art. 9º.

- **Só competência (art. 16):** base de cálculo = receita bruta total mensal
  **auferida**; receita auferida = a reconhecida na forma do art. 2º, §§8º e 9º-A
  (momento do **faturamento**) (§1º-A). Revogam-se o §1º do art. 16, o parágrafo
  único do art. 17, o §1º do art. 18, os arts. 19 e 20 e os arts. 77 e 78 (Res.
  190, art. 8º, IX a XII e XXIII): **acaba o regime de caixa**.
- **RBT12 (art. 21, II, "a"):** receita dos **doze meses antecedentes ao mês
  anterior** ao período de apuração. O ISS segue limitado a 5%, com o excesso
  transferido aos **tributos federais e ao IBS** (III). Acima da 5ª faixa, o
  percentual de **ICMS, ISS e IBS** = **{[(RBT12 × alíquota nominal da 5ª faixa)
  − parcela a deduzir da 5ª faixa] ÷ RBT12} × percentual de distribuição do ICMS,
  ISS e IBS da 5ª faixa** (IV).
- **Início de atividade (art. 22):** no **1º e 2º meses**, alíquotas da
  **primeira faixa** (§2º, I); do **3º ao 13º mês**, RBT12 = média aritmética da
  receita dos meses antecedentes ao mês anterior × 12 (§2º, II); quem começou no
  ano anterior à opção segue essas regras até 13 meses e a regra geral a partir
  do 14º (§4º).
- **Cesta básica (art. 36):** a redução proporcional passa a valer só para
  isenção ou redução de **ICMS** (PIS/Cofins deixam de existir).

## Ligações

- [[sn-segregacao-receitas]]: em que Anexo cada receita entra.
- [[sn-fator-r]]: quando o serviço vai para o Anexo III ou para o V.
- [[sn-anexo-i-comercio]], [[sn-anexo-ii-industria]], [[sn-anexo-iii-servicos]],
  [[sn-anexo-iv-servicos]], [[sn-anexo-v-servicos]]: as tabelas.
- [[simples-nacional-e-mei]]: o lado IBS/CBS da reforma.
