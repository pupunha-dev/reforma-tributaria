# Roteiro da apresentação à diretoria

Base de conhecimento tributário federal do setor fiscal. Posição em 09/10/2026.

## O que mostrar em 1 minuto

- **139 notas** em 3 domínios: Reforma Tributária (92), Simples Nacional e MEI
  (35) e documentos fiscais da NF-e (12).
- **Fontes oficiais**: LC 214/2025, LC 227/2026, Regulamentos da CBS (Decreto
  12.955/2026) e do IBS (Res. CGIBS 6/2026), LC 123/2006, Res. CGSN 140/2018 com
  anexos, Res. CGSN 11/2007, Solução de Consulta Cosit 71/2026, 5 Notas Técnicas,
  o Informe Técnico 2025.002 e as tabelas oficiais de cClassTrib e cCredPres.
- **Cada resposta** cita a nota e o artigo, separa o que vale hoje do que vale a
  partir de 2027 ou 2029 e diz quando a informação **não está** nas fontes.

## Demonstração (perguntas já validadas)

Faça as perguntas nesta ordem. Cada uma mostra uma capacidade.

| # | Pergunta | O que ela mostra |
|---|---|---|
| 1 | Um eletricista que atende residências pode ser MEI? Qual CNAE e ele recolhe ISS ou ICMS no DAS? | Consulta direta a tabela oficial (ocupações do MEI) |
| 2 | Como o MEI recolhe o IBS e para quem vai o dinheiro? | Separação hoje × 2027 e cruzamento Simples × reforma |
| 3 | Como calculo o crédito presumido na compra de produtor rural não contribuinte? | Fórmula completa do regulamento e vigência |
| 4 | A partir de quando um produtor rural pessoa física precisa ter CNPJ e emitir nota por causa do IBS/CBS? | Divergência entre o regulamento da CBS e o do IBS, sinalizada |
| 5 | Uma empresa com o CNAE 6810-2/02 pode optar pelo Simples? | Lista oficial de CNAEs impeditivos e a leitura da Receita |
| 6 | Uma empresa que administra caução de aluguel pode ser do Simples? Em qual Anexo? | Uso de Solução de Consulta como interpretação da Receita |
| 7 | Na NF-e, o cCredPres 5 é o do regime opcional de cooperativa? | Detecta exemplo desatualizado da NT e segue a tabela oficial |
| 8 | O que muda no IR do aluguel com a reforma? | Limite do escopo: diz que IR não está nas fontes e responde só o IBS/CBS |

## Como fazer uma boa pergunta

- Diga o **tipo de empresa** (Simples, MEI, regime regular) e a **operação**
  (venda, serviço, compra de produtor rural...).
- Diga o **período** que interessa (hoje, 2027, 2033).
- Uma pergunta por vez rende respostas melhores.

## O que esperar e o que não esperar

- **Espera-se**: nota e artigo citados; fórmula descrita por completo; aviso
  quando a regra muda numa data; aviso quando falta fonte.
- **Não é** parecer: a base organiza e cita a lei; a decisão final é do
  profissional responsável.
- **Fora do escopo**: ICMS e ISS estaduais e municipais em detalhe, IR de pessoa
  física e IRPJ fora do Simples, convênios e listas estaduais.
- **Pendências conhecidas** (em `pendencias.md`): decisões D1 a D3 da equipe,
  versão atual da Res. CGIBS 6, ato com as datas de obrigatoriedade dos
  documentos fiscais, percentuais anuais de crédito presumido, Anexos VII, X e XII
  da Res. 140 e a NT da NF-e para Simples/MEI.

## Depois da apresentação

As perguntas da diretoria entram no [registro de testes](registro-testes.md).
Cada erro ou lacuna vira correção de nota ou pergunta nova na bateria de
regressão (`docs/perguntas-teste/`).
