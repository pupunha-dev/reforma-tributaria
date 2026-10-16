---
título: NFS-e Nacional — emissão por decisão administrativa ou judicial
dominio: documentos-fiscais
fontes: Guia do Emissor Público Nacional Web da NFS-e v1.2 (27/07/2026), seção 4.3 (p. 96-100); NT 2025.002-RTC v1.52 (referência de hierarquia, ver df-visao-geral-reforma-nfe)
vigencia: atual
texto-base: 2026-10-16
---

# Emissão por decisão administrativa ou judicial

## A lógica em uma frase

É um **fluxo de exceção**: gera a NFS-e **sem a validação completa** das regras de
negócio do fluxo padrão, para cumprir uma decisão administrativa ou judicial
reconhecida pelo município. Como as travas e os cálculos automáticos ficam
desligados, **o emitente informa os valores** que o sistema normalmente calcularia.

## Quando se usa

- O guia diz que a funcionalidade atende "às determinações estabelecidas" por tais
  decisões e que o contribuinte deve estar **vinculado a uma decisão reconhecida pelo
  município** (cadastrada pelo município de emissão).
- Se o contribuinte não está vinculado a nenhuma decisão em nenhum município
  conveniado, o sistema mostra uma tela de aviso e não segue.
- O acesso é pela opção "Emissão por decisão administrativa/judicial" do menu
  principal (ver [[df-nfse-painel-configuracoes]]).

## Como difere da emissão normal

| Passo | Particularidade |
|---|---|
| **Pessoas** | A **data de competência** deve respeitar o **início de vigência do cadastro da decisão** feito pelo município. O mesmo CPF/CNPJ do emitente pode ser informado como tomador/adquirente, destinatário e intermediário. |
| **Serviço** | O **município de incidência** é informado pelo emitente (**não** é recuperado). O Código de Tributação Nacional lista **só** os serviços que o município cadastrou como parte da decisão favorável ao emitente. Os grupos de obra/imóvel, evento e comércio exterior são **opcionais**. |
| **Valores** | Todos os campos de valores são informados pelo emitente: alíquota, base de cálculo, valor do ISSQN e também o **valor líquido da NFS-e**, porque os cálculos automáticos não são feitos. |

Depois, "Emitir NFS-e" finaliza.

## Consultar, cancelar e substituir

- **Consulta:** em "NFS-e Emitidas", as notas desse fluxo trazem um **ícone com
  detalhe azul**.
- **Cancelar:** na nota desejada, "Cancelar NFS-e", preencher a janela e confirmar;
  o status da nota muda.
- **Substituir:** na nota, "Substituir". O sistema verifica se ela pode ser
  substituída por outra emitida **tanto pelo fluxo padrão quanto pelo de decisão** e,
  se possível, pergunta qual fluxo usar; segue para a emissão por substituição.
  Regras gerais de cancelamento e substituição:
  [[df-nfse-consulta-cancelamento-substituicao]].

## Atenção

- O guia remete à coluna "L" da planilha `RN_DPS_NFS-e` do anexo de leiaute para as
  regras que esse fluxo dispensa. Essa planilha **não está nas fontes**.
- A decisão, sua validade e o alcance dela são do município e do processo; o guia
  descreve só a operação do emissor.

## Ligações

- [[df-nfse-emissao-pessoas]], [[df-nfse-emissao-servico]] e
  [[df-nfse-emissao-valores-ibs-cbs]]: o fluxo padrão que este fluxo adapta.
- [[df-nfse-visao-geral]]: o que é a NFS-e Nacional.
