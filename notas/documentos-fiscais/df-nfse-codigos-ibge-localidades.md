---
título: NFS-e Nacional — códigos IBGE de município, distrito e subdistrito (DTB) e onde a DPS os usa
dominio: documentos-fiscais
fontes: Anexo I do leiaute da DPS/NFS-e (arquivo de 09/09/2025, anterior à versão de 10/12/2025 citada pela NT CGNFS-e 004 v2.00: campos cLocEmi, cLocPrestacao, cLocIncid, cMun e xLocEmi); Relatórios da Divisão Territorial Brasileira do IBGE (BET, data-base 22/11/2024; municípios, distritos e subdistritos) e planilhas de distritos e subdistritos novos de 2023
vigencia: atual
texto-base: 2026-10-16
---

# Códigos IBGE de localidades na NFS-e Nacional

## A lógica em uma frase

Todo "lugar" da DPS e da NFS-e (município do emitente, do prestador, do tomador, local da
prestação, local de incidência) é informado pelo **código IBGE de 7 dígitos do município**, sem
nome: o nome é só descrição (`xLoc...`). A tabela completa (5.570 municípios) **não cabe numa
nota**; ela está nas fontes e o time de TI consulta pelo script `scripts/consulta_ibge.py`.
Esta nota explica **onde o código é usado** e **o que a tabela do IBGE contém**.

## Onde a DPS usa o código (Anexo I)

| Campo | O que é | Observação do leiaute |
|---|---|---|
| `cLocEmi` | município emissor da NFS-e (7 dígitos) | "sempre corresponderá a um município brasileiro" da tabela do IBGE, **ou** a um trecho de concessão de exploração de rodovia; o município emissor tem de ser conveniado e ativo no sistema nacional |
| `cLocPrestacao` | local da prestação do serviço (7 dígitos, grupo `locPrest`, alternativa de `cPaisPrestacao`) | pode ser qualquer município da tabela do IBGE, **um trecho de concessão de rodovia** do cadastro do Sistema Nacional, ou `0000000`, que representa **"Águas Marítimas"** |
| `cLocIncid` | localidade de incidência do ISSQN (7 dígitos) | o sistema nacional a identifica; não existe em imunidade, exportação de serviço e serviço sem incidência (`cTribNac` 990101) |
| `cMun` (`enderNac`) | município do endereço do emitente, prestador, tomador, intermediário e fornecedor de documento de dedução | "Tabela do IBGE", 7 dígitos |
| `xLocEmi`, `xLocPrestacao`, `xLocIncid` | descrição (nome) do código | preenchidas pelo sistema |

(Código de **país** é outra tabela, a ISO2 do Anexo A, que **não está nas fontes**.)
O ISSQN em si (quem cobra, onde incide) é matéria municipal e fora do escopo; ver
[[df-nfse-emissao-servico]] para a tela e [[df-nfse-lista-servicos-ctribnac]] para o código do serviço.

## O que a tabela do IBGE traz

- **Fonte:** relatórios da Divisão Territorial Brasileira (DTB), "BET – Banco de Estruturas
  Territoriais", com **data-base 22/11/2024**. Se um município for criado, extinto ou renomeado depois
  dessa data, a tabela não mostra.
- **Municípios:** **5.570**, em 27 UFs, cada um com o **código de 7 dígitos** (os 2 primeiros
  são o código da UF; por exemplo, 41 = Paraná). Exemplo conferido: **Lapa (PR) = 4113205**.
  Nomes repetem entre UFs (há "Belém" no PA, na PB e em AL): **sempre conferir a UF**.
- **Distritos:** 10.724, com código de **9 dígitos** (o do município seguido do número do distrito).
- **Subdistritos:** 645, com código de **11 dígitos**.
- **"Distritos novos 2023" e "Subdistritos novos 2023":** 54 distritos e 2 subdistritos criados em 2023;
  **todos já constam** nos relatórios de 22/11/2024.
- A NFS-e usa o código do **município** (7 dígitos). O leiaute lido (Anexo I) não menciona distrito
  nem subdistrito.

## Como consultar

No repositório: `python scripts/consulta_ibge.py lapa PR` (por nome e UF) ou
`python scripts/consulta_ibge.py --codigo 4113205`. Os arquivos de apoio são
`fontes/documentos-fiscais/texto/ibge-dtb-municipios.tsv`, `ibge-dtb-distritos.tsv` e
`ibge-dtb-subdistritos.tsv`; as planilhas originais ficam em `fontes/documentos-fiscais/ibge-dtb/`.

## O que a nota não responde

- O **código IBGE de um município específico**: o bot não tem a tabela; use o script ou o
  emissor, que preenche o código a partir do nome.
- Se o município **aderiu ao convênio da NFS-e Nacional** (matéria municipal, fora do escopo).
- Códigos de trechos de concessão de rodovia (cadastro próprio do Sistema Nacional, não nas fontes).
