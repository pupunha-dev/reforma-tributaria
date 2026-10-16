---
título: NFS-e Nacional — visão geral do Emissor Público Nacional (Web, Mobile e API)
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), histórico de versões, siglas, introdução e seção 1 (p. 2-7); NT 2025.002-RTC v1.52 (referência para CST/cClassTrib, ver df-cst-cclasstrib)
vigencia: com-mudanca-programada
texto-base: 2026-10-16
---

# NFS-e Nacional: visão geral do emissor

## A lógica em uma frase

A NFS-e Nacional é a nota de serviço **padronizada para o país inteiro**: o
contribuinte preenche uma **DPS** (a "declaração" do que prestou) num emissor
público e a **Sefin Nacional** valida a DPS e devolve a **NFS-e**. Pense na DPS
como o rascunho que você entrega no balcão e na NFS-e como o recibo carimbado que
volta; o balcão é o mesmo para todos os municípios conveniados.

> **Natureza da fonte.** O Guia é um **roteiro operacional** (como usar a tela).
> Ele fica **abaixo da Nota Técnica** e dos atos normativos: não cria tributo nem
> obrigação. Datas e obrigações vêm do ato; quando o guia cita uma data cujo ato
> não está nas fontes do projeto, a nota avisa. ISSQN e convênios dos municípios
> são matéria municipal e ficam **fora do escopo** (ver [[df-nfse-emissao-servico]]).

## Os três jeitos de emitir

| Canal | Para quê |
|---|---|
| **Emissor Web** | Gestão completa pelo contribuinte: cadastrar-se, emitir, consultar e cancelar. É o assunto destas notas. |
| **Emissor Mobile** | Emissão **simplificada**, para contribuintes de municípios que usam a Sefin Nacional; fala só com o Sistema Nacional da NFS-e. |
| **API** | Funciona como uma Secretaria de Finanças Municipal (**Sefin Nacional NFS-e**): recebe e valida as DPS enviadas direto à API ou geradas nos emissores Web e App. O município sem ambiente próprio pode se **conveniar** ao sistema nacional. |

Endereço do emissor web, segundo o guia: `https://www.nfse.gov.br/EmissorNacional`.

## O que o Emissor Web faz

Configuração do emissor; emissão; consulta das NFS-e **emitidas** e **recebidas**;
cancelamento; substituição; apuração nacional (**MAN**, "por ora, apenas em
ambiente de Produção Restrita"); serviços favoritos; e rascunhos. Ele consulta
outras bases: tabelas de convênio dos municípios (Painel Administrativo Nacional),
tabelas parametrizadas pelos municípios (Painel Municipal), cadastros de CNPJ,
CPF e Simples Nacional, tabela TOM e o **CNC NFS-e** (Cadastro Nacional de
Contribuintes).

Mapa das notas: acesso em [[df-nfse-acesso-perfis]]; painel e configurações em
[[df-nfse-painel-configuracoes]]; os quatro passos da emissão em
[[df-nfse-emissao-pessoas]], [[df-nfse-emissao-servico]],
[[df-nfse-emissao-valores-ibs-cbs]] e [[df-nfse-emissao-final-mei]]; casos
especiais em [[df-nfse-decisao-administrativa-judicial]]; consulta, cancelamento
e substituição em [[df-nfse-consulta-cancelamento-substituicao]]; notas recebidas
em [[df-nfse-notas-recebidas-manifestacao]].

## Glossário (siglas do guia)

| Sigla | Significado |
|---|---|
| **DPS** | Declaração da Prestação de Serviços |
| **NFS-e** | Nota Fiscal de Serviço Eletrônica Nacional |
| **DANFSe** | Documento Auxiliar da NFS-e (PDF resumido; ver [[df-nfse-consulta-cancelamento-substituicao]]) |
| **Sefin Nacional** | Secretaria de Finanças Nacional (valida as DPS) |
| **ADN** | Ambiente de Dados Nacional |
| **CNC** | Cadastro Nacional de Contribuintes |
| **CGNFS-e** | Comitê Gestor da NFS-e |
| **MAN** | Módulo de Apuração Nacional |
| **TOM** | tabela de municípios (endereços e CEP) |
| **RFB** | Receita Federal do Brasil |

## Versões do guia

| Versão | Data | O que mudou |
|---|---|---|
| 1.0 | (sem data no guia) | (sem descrição no guia) |
| 1.1 | 23/09/2025 | inclusão dos itens 4.3 a 4.3.4: emissão por decisão administrativa ou judicial |
| 1.2 | 27/07/2026 | "adequação do guia aos novos campos de IBS/CBS" |

O arquivo usado pelo projeto é a v1.2 (nome do arquivo: `..._versao_1-2-1.pdf`); o
guia não traz o endereço de onde foi publicado (ver `fontes/documentos-fiscais/FONTE.md`).

## IBS e CBS na NFS-e: as datas que o guia informa

A v1.2 do guia acrescentou o preenchimento de IBS e CBS na emissão (detalhe em
[[df-nfse-emissao-pessoas]] e [[df-nfse-emissao-valores-ibs-cbs]]). As datas abaixo
são **as do guia**; o ato que as fixa **não está nas fontes do projeto** (⚠️ lacuna
em `pendencias.md`).

- **Regime regular:** o guia informa que, "a partir de 03 de agosto de 2026",
  passa a ser exigido o preenchimento das informações de IBS e CBS, "observadas as
  respectivas regras de validação", e que **não é permitido emitir** documentos
  fiscais eletrônicos, pelas empresas do regime regular, sem os campos de IBS/CBS.
  Na data-base desta nota (16/10/2026) essa data já passou.

## ⏳ A partir de 01/01/2027 — Simples Nacional (guia, passo "Pessoas")

Para as empresas **optantes pelo Simples Nacional**, o guia diz que o início da
obrigatoriedade do preenchimento de IBS/CBS ocorre "para os fatos geradores
ocorridos a partir de 01 de janeiro de 2027". Até lá, o guia mantém a pergunta "Preencher as
informações IBS/CBS?" com as duas respostas (Sim/Não). Não misture com a regra do
regime regular: as duas datas valem para públicos diferentes.

## Ligações

- [[df-cst-cclasstrib]] e [[df-tabela-cclasstrib]]: o CST e o cClassTrib que o passo
  "Valores" pede (os mesmos da NF-e).
- [[sn-obrigacoes-acessorias]]: NFS-e de padrão nacional obrigatória para ME/EPP
  optantes a partir de 01/11/2026 (Res. CGSN 191/2026), na seção de regulamentação.
- [[sn-mei-regulamentacao]]: NFS-e nacional do MEI (art. 106-A).
- [[ibs-cbs-documento-fiscal-regulamentacao]]: o documento fiscal na regulamentação
  do IBS/CBS.
- [[df-visao-geral-reforma-nfe]]: o equivalente para a NF-e/NFC-e.
- [[df-nfse-cgnfse-notas-tecnicas]]: as Notas Técnicas da SE/CGNFS-e (nível de NT, acima do
  guia): cronologia, o que está em produção e o mapa dos anexos. Os campos do grupo IBSCBS
  estão em [[df-nfse-layout-ibscbs]]; a NFS-e Via, em [[df-nfse-via]].
