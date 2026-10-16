---
título: NFS-e Nacional — emitir (passo 4), NFS-e gerada e emissão simplificada do MEI
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seções 4.1.4, 4.1.5 e 4.2 (p. 84-96); NT 2025.002-RTC v1.52 (referência de hierarquia, ver df-visao-geral-reforma-nfe)
vigencia: atual
texto-base: 2026-10-16
---

# Emitir a NFS-e e a emissão simplificada do MEI

## A lógica em uma frase

No fim da emissão completa o emissor mostra um **resumo para conferência** e, ao
clicar em "Emitir NFS-e", envia a DPS à Sefin Nacional, que a **valida** e devolve a
NFS-e. O **MEI** tem um atalho: depois de configurar o emissor e cadastrar seus
**serviços favoritos**, emite informando só **três dados** (cliente, serviço e valor).

## Passo 4 da emissão completa: conferir e emitir

- O sistema mostra um **resumo** dos passos e o **cálculo prévio** dos tributos.
  Nesse ponto ainda é possível voltar e alterar: **Editar Pessoas**, **Editar
  Serviço** e **Editar Tributação** (valores), cada um seguido de "Avançar".
- O comando **"Emitir NFS-e"** envia o **XML da DPS** ao serviço de geração de NFS-e
  da Sefin Nacional, que valida a DPS pelas regras do anexo de leiaute
  (`ANEXO_I-SEFIN_ADN-DPS_NFSe-SNNFSe`, fora das fontes) e devolve o **XML da
  NFS-e** gerada.
- **NFS-e gerada com sucesso:** o sistema mostra o resumo, com a **chave de acesso**.
  Ações possíveis: baixar o **XML**; baixar o **DANFSe** em PDF; **visualizar** a
  NFS-e no navegador; ir às **NFS-e emitidas**; iniciar uma **nova NFS-e**.

## Emissão simplificada (só MEI)

A versão simplificada pede um grupo menor de informações, mas ao final o emissor gera
uma NFS-e com o **mesmo leiaute** da emissão completa; a maior parte dos campos
obrigatórios já vem do cadastro do contribuinte. Não é uma "nota menor" no sentido
jurídico: muda só o preenchimento.

### Antes de emitir (itens 4.2.1 a 4.2.3)

1. **Configurações** ([[df-nfse-painel-configuracoes]]): informar e-mail e telefone e
   marcar a opção de cálculo/exibição dos valores totais dos tributos.
2. **Serviços favoritos** ([[df-nfse-painel-configuracoes]]): apelido (até 50
   caracteres), Código de Tributação Nacional, item da NBS e descrição.

Quem abre a emissão simplificada sem essas configurações recebe uma tela de aviso.

### A emissão (item 4.2.4)

O formulário pede três informações:

| Campo | Regra |
|---|---|
| CPF/CNPJ do cliente | obrigatório; pode-se recuperar dos últimos tomadores; o nome vem do cadastro CPF/CNPJ |
| Serviço prestado | obrigatório; a lista mostra os **favoritos** pelo apelido |
| Valor do serviço | obrigatório; valor total em reais |

Há um campo opcional para **complementar a descrição** do favorito; o texto vale só
para a nota em emissão e **não altera** o favorito cadastrado.

**Obra ou evento:** se o favorito for de **obra** (subitens 7.02 e 7.05) ou de
**atividade de evento** (item 12), o sistema pede dados extras:

- **Obra:** código da obra **ou** endereço no Brasil. Com o código da obra: o
  município da prestação. Com endereço: CEP, número e complemento (município, bairro e
  logradouro vêm da tabela TOM).
- **Evento:** data inicial e final; identificador do evento (opcional) com município,
  ou endereço no Brasil.

Para quase todos os serviços os três campos bastam. As ações após a emissão são as
mesmas da completa.

## Ligações

- [[df-nfse-emissao-valores-ibs-cbs]]: passo 3 da emissão completa.
- [[df-nfse-consulta-cancelamento-substituicao]]: o que fazer com a nota gerada.
- [[sn-mei-regulamentacao]]: NFS-e nacional do MEI (art. 106-A da Res. CGSN 140).
- [[sn-mei]]: o MEI no Simples Nacional.
