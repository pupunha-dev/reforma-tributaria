---
título: Cálculo do Simples Nacional — RBT12, alíquota nominal e alíquota efetiva
dominio: simples-nacional
fontes: LC 123/2006, art. 18, caput, §§1º a 3º e 15 a 23 (redação da LC 155/2016); LC 214/2025, arts. 517 e 543
vigencia: com-mudanca-programada
texto-base: 2026-10-06
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

## Início de atividade (§2º)

No início de atividade, os valores de receita bruta das tabelas dos Anexos I a
V são **proporcionalizados** ao número de meses de atividade no período (§2º).

## Excesso de receita: tributação da parcela excedente (§§16 a 17-A)

- No ano de início de atividade, se o excesso sobre o limite proporcional não
  passar de 20% (art. 3º, §12), a parcela excedente fica sujeita às
  **alíquotas máximas** dos Anexos I a V, proporcionalmente (§16). O mesmo vale
  do mês do excesso até o mês anterior aos efeitos da exclusão, no excesso de
  até 20% do art. 3º, §9º-A (§16-A).
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
- A forma de cálculo (§1º-A) e a incidência sobre a receita do mês (§3º) ficam
  mantidas; os percentuais de repartição passam a conter **CBS e IBS** nos novos
  Anexos (ver [[sn-anexo-i-comercio]] a [[sn-anexo-v-servicos]]).

## ❌ Revogado a partir de 01/01/2033 — LC 214/2025 (art. 543, V, "b")

Fundamento da data: LC 214, art. 544, V. São revogados do art. 18 o §5º-E e
os **§§14, 17, 17-A, 22-A e 23**, ou seja, as regras de excesso de sublimite
quanto a ICMS e ISS (§§17 e 17-A), o ISS em valor fixo dos escritórios
contábeis (§22-A) e o abatimento de material na base do ISS (§23).

## Ligações

- [[sn-segregacao-receitas]]: em que Anexo cada receita entra.
- [[sn-fator-r]]: quando o serviço vai para o Anexo III ou para o V.
- [[sn-anexo-i-comercio]], [[sn-anexo-ii-industria]], [[sn-anexo-iii-servicos]],
  [[sn-anexo-iv-servicos]], [[sn-anexo-v-servicos]]: as tabelas.
- [[simples-nacional-e-mei]]: o lado IBS/CBS da reforma.
