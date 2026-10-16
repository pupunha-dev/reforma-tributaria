---
título: NFS-e Nacional — painel principal, configurações do emitente, rascunhos de DPS e serviços favoritos
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seções 2, 3, 7 e 8 (p. 16-19 e 112-115); NT 2025.002-RTC v1.52 (referência de hierarquia, ver df-visao-geral-reforma-nfe)
vigencia: atual
texto-base: 2026-10-16
---

# NFS-e Nacional: painel, configurações, rascunhos e favoritos

## A lógica em uma frase

Antes da primeira nota, o emitente **configura o emissor uma vez** (contato e como
mostrar o "valor aproximado dos tributos"); depois, o painel guarda o que poupa
tempo: **rascunhos** de DPS (salvos sozinhos) e **serviços favoritos** (modelos
prontos de serviço).

## Painel principal (seção 2)

**Menu:** página inicial; tipos de emissão (completa, simplificada e por decisão
administrativa/judicial); NFS-e emitidas; NFS-e recebidas; rascunhos; MAN
(Módulo de Apuração Nacional, "por ora, apenas em ambiente de Produção Restrita");
configurações; serviços favoritos.

**Painéis gerenciais:** rascunhos; dados do usuário; últimas NFS-e emitidas; acesso
rápido (o ícone "+" do acesso rápido leva à **Emissão Completa**).

Os painéis dependem do perfil: quem **não é emitente** não tem rascunhos nem
últimas NFS-e emitidas para mostrar.

## Configurações (seção 3)

O guia diz que este módulo "deve ser o primeiro a ser acessado". Campos:

| Campo | Obrigatório? | Observação |
|---|---|---|
| E-mail | opcional | Pode ser diferente do cadastrado no município ou na RFB. |
| Telefone | opcional | Idem. |
| Opção atual no Simples Nacional | sim | Só leitura; vem dos cadastros da RFB. |
| Valor aproximado dos tributos | sim | Escolha da opção (abaixo). |

**Regra de uso do e-mail e do telefone:** vão para o grupo de informações da DPS
conforme o tipo de emitente (Prestador/Fornecedor, Tomador/Adquirente ou
Intermediário) e só são **impressos no DANFSe quando faltam nas fontes cadastrais
oficiais** (RFB e município). Se existirem lá, valem os oficiais.

### Valor aproximado dos tributos

A opção marcada define como o emissor calcula e exibe, em **cada** NFS-e, os valores
totais dos tributos federais, estaduais e municipais. O texto do guia descreve:

- **Informar a alíquota do Simples Nacional** (aparece só para optantes): a ME/EPP
  informa a **alíquota nominal** a que está sujeita no regime, conforme o art. 9º do
  Decreto 8.264/2014, que regulamenta a Lei 12.741/2012.
- **Informar percentuais:** preenchem-se os percentuais Federal, Estadual e
  Municipal.
- **Uma opção sem preenchimento adicional** ("nenhum preenchimento será
  necessário").
- Na emissão (passo "Valores") o guia também prevê informar os **valores
  monetários totais** dos tributos federal, estadual e municipal; ver
  [[df-nfse-emissao-valores-ibs-cbs]].

Os nomes exatos das opções aparecem nas telas (imagens), não no texto do guia; a
nota descreve só o que o texto diz.

⚠️ O Decreto 8.264/2014 e a Lei 12.741/2012 não estão nas fontes do projeto: a nota
repete o que o guia cita, sem conferir o texto desses atos.

Depois de configurar, a emissão está liberada (para o MEI, a emissão simplificada
exige também os serviços favoritos; ver [[df-nfse-emissao-final-mei]]).

## Rascunhos de DPS (seção 7)

- O sistema **salva o rascunho automaticamente a cada 5 segundos** enquanto a DPS é
  preenchida. O uso principal é a **perda de conexão** com o emissor.
- A lista mostra: data da última atualização, competência, "emitida para", valor,
  **passo** em que a DPS parou e as ações **Editar** e **Excluir**.
- **Editar** retoma do passo em que o rascunho está e permite alterar **todos** os
  campos, pelos mesmos passos da emissão.
- **Excluir** deleta fisicamente o rascunho.

## Serviços favoritos (seção 8)

Modelos de serviço que agilizam o **passo 2** do Emissor Web e alimentam a **DPS
simplificada** do Emissor Mobile. Campos:

| Campo | Regra |
|---|---|
| Município | recuperado dos cadastros da RFB ou do CNC, conforme o convênio do município |
| Apelido | obrigatório, no máximo **50 caracteres**; só identifica o serviço no sistema |
| Código de Tributação Nacional | obrigatório, escolhido na lista |
| Item da NBS | obrigatório; a NBS (Nomenclatura Brasileira de Serviços, Intangíveis e Outras Operações que Produzam Variações no Patrimônio) é o classificador nacional dos serviços |
| Descrição do serviço | obrigatória |

O serviço cadastrado aparece na tela inicial dos favoritos, onde pode ser editado,
excluído ou acompanhado de novos cadastros.

## Ligações

- [[df-nfse-visao-geral]]: canais de emissão e glossário.
- [[df-nfse-emissao-servico]]: onde o Código de Tributação Nacional e a NBS são usados.
- [[df-nfse-emissao-final-mei]]: o uso dos favoritos na emissão simplificada.
- [[df-nfse-acesso-perfis]]: como entrar.
