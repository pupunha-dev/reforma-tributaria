---
título: Tabela de CST e cClassTrib (códigos publicados no Portal dos DF-e e no IT 2025.002)
dominio: documentos-fiscais
fontes: Portal dos DF-e (SVRS), tabela de classificação tributária, captura 2026-10-08; IT 2025.002 v1.60, seções 02, 03, 06 e 07; NT 2025.002-RTC v1.52, seção 3 e Anexo III
vigencia: atual
texto-base: 2026-10-08
---

# Tabela de CST e cClassTrib

## A lógica em uma frase

A [[df-cst-cclasstrib]] explica **para que servem** o CST e o cClassTrib no XML.
Esta nota traz **os códigos em si**: quais existem, o percentual de redução de
cada um, em quais documentos fiscais valem, desde quando e se servem ao Simples
Nacional. É a "lista telefônica" que a NT 2025.002-RTC chama de Anexo III e que o
**Informe Técnico (IT) 2025.002** publica e mantém.

## De onde vêm os dados

- **IT 2025.002 v1.60 (22/06/2026):** documento oficial que divulga as tabelas
  cClassTrib, CST e cCredPres e as alíquotas padrão. Diz que as tabelas estão no
  Portal Nacional da NF-e ("Documentos" → "Diversos") e, em formato interativo, em
  https://dfe-portal.svrs.rs.gov.br/DFE/TabelaClassificacaoTributaria (seção 06).
  O mesmo IT informa um serviço em JSON em `dfe-portal.svrs.rs.gov.br/CFF/Servicos`,
  com acesso por certificado digital (não usado aqui).
- **Captura de 2026-10-08** da página interativa (o endereço do IT redireciona para
  `/DFE/ClassificacaoTributaria`; o conteúdo é idêntico ao de
  `/Cff/ClassificacaoTributaria`): **18 CST e 173 cClassTrib**. A equipe confirmou
  em 2026-10-08 que a fonte é a recomendada pelo site da Receita.
- **O portal está mais novo que o IT v1.60:** há itens publicados em 01/10/2026.
  Ex.: o `410036`, que o IT v1.60 chama de "Descontos incondicionais", aparece no
  portal como "Descontos financeiros em nota fatura". Vale a tabela do portal;
  pode existir versão do IT posterior à 1.60 que não está nas fontes.
- Arquivos em `fontes/documentos-fiscais/texto/`: `cclasstrib-svrs.json` (dados
  completos) e `cclasstrib-svrs.md` (tabelas para leitura, com o link do
  dispositivo legal). Para atualizar:
  `python scripts/tabelas_svrs.py cclasstrib --data AAAA-MM-DD` e depois
  `python scripts/tabelas_svrs.py nota notas/documentos-fiscais/df-tabela-cclasstrib.md`
  (regera só as tabelas desta nota).
- **Hierarquia:** IT e NT são documentação técnica: dizem **como classificar e
  validar** a operação no documento fiscal; não criam nem alteram tributo. Cada
  par CST + cClassTrib aponta para um dispositivo da LC 214/2025 "e normas
  complementares" (IT, seção 02), e a lei prevalece.

## Como ler a tabela (definições do IT, seções 02 e 03)

O cClassTrib tem 6 dígitos e "os três primeiros dígitos são idênticos ao
CST-IBS/CBS" (ex.: `200003` é do CST 200). Nos 173 itens capturados isso vale
sem exceção.

| Coluna desta nota | Definição no IT |
|---|---|
| Red. IBS / Red. CBS | pRedIBS e pRedCBS: percentual de redução da alíquota associado ao cClassTrib. Em alguns itens os dois diferem (ex.: IBS 60% e CBS 100%) |
| Alíquota | Tipo de Alíquota, "conforme disposto na Lei Complementar nº 214/2025". Legenda do portal: 1 Fixa, 2 Padrão, 3 Sem alíquota, 4 Uniforme nacional, 5 Uniforme setorial |
| Vigência | dIniVig e dFimVig: início e final de vigência do cClassTrib |
| Documentos | indicadores de modelo de documento: permitem ou não informar o cClassTrib no documento (NF-e, NFC-e, CT-e, NFS-e etc.) |
| Simples (tpRBSN) | "Define as formas de receita bruta aplicáveis aos contribuintes do Simples Nacional" (criado na v1.60). Legenda do portal: 0 Não é receita bruta, 1 Receita bruta interna, 2 Receita bruta interna sem cálculo IBS/CBS, 3 Exportação direta, 4 Exportação indireta, 5 Mercado interno/exportação, 9 Fornecimento incompatível com SN |

Documentos em desenvolvimento, segundo o IT: indNFeABI (NF-e de Alienação de Bens
Imóveis), indNFGas (gás canalizado) e indDERE (Declarações de Regimes
Específicos).

**Indicadores de exigência de grupos** (IT, seção 02): ind_gTribRegular,
ind_gCredPresOper, ind_gMonoPadrao, ind_gMonoReten, ind_gMonoRet,
ind_gpBioDiferenca e ind_gEstornoCred; na v1.60 o ind_gMonoDif foi excluído.
Eles dizem se o grupo correspondente do XML é exigido, permitido ou vedado. O
JSON do portal usa outros nomes (ex.: `IndTribRegular`, `IndPermiteCredPres`); o
IT não publica o JSON, então **associar os nomes é inferência** e deve ser
conferido na regra de validação da NT.

**Tabela CST** (IT, seção 03): indicadores ind_gIBSCBS, ind_gIBSCBSMono, ind_gRed,
ind_gDif, ind_gTransfCred, ind_gCredPresIBSZFM (crédito presumido de IBS sobre o
saldo devedor na ZFM, art. 450, §1º, da LC 214), ind_gAjusteCompet e
ind_RedutorBC (redução da base de cálculo, habilitado para o CST 222).

**Texto dos regulamentos por código.** O IT lista as colunas "Regulamento CBS"
(redação do dispositivo do **Decreto nº 12.955, de 29/04/2026**) e "Regulamento
IBS" (redação do dispositivo da **Resolução CGIBS nº 6, de 30/04/2026**). No JSON,
165 códigos trazem esses trechos (campos `TexRegCbs` e `TexRegIbs`), com
numeração própria: no `011005`, a LC 214 é o art. 243, e o trecho do regulamento é
o "Art. 346". **Os regulamentos inteiros não estão nas fontes** (ver
`pendencias.md`).

## Histórico da tabela (IT 2025.002, seção 07)

| Versão do IT | O que mudou na tabela cClassTrib/CST |
|---|---|
| 1.10 (jun/2025) | Incluídos `010002`, `222001`, `410021`, `410999`, `820006` e `830001`; `620004` dividido em `620004` e `620005`; antigo `620005` virou `620006`; criado o CST 222; publicada a 1ª tabela cCredPres |
| 1.20 (out/2025) | Indicadores de documento passam da tabela CST para a cClassTrib; criados ind_gCredPresIBSZFM, ind_gAjusteCompet e ind_gEstornoCred |
| 1.30 (nov/2025) | ind_RedutorBC passa para a tabela CST (CST 222) |
| 1.31 (dez/2025) | `200050` habilitado para CT-e OS e `410031` para NF-e |
| 1.40 (jan/2026) | Textos e novas linhas pela LC 227/2026; `200001` sai da NF-e e entra no CT-e OS; `200044` sai da NF-e/NFC-e; `200043` e `200044` entram na NFCom; `410027` entra na NF-e; CST 820 passa a "Tributação em documento específico" |
| 1.50 (abr/2026; implantação em homologação e produção até 04/05/2026) | Criados `000005` (EAC com destinação diversa) e `200054` (cooperativa agropecuária a associado fora do regime regular); `620001` a `620005` saem da NFC-e |
| 1.60 (jun/2026; implantação em homologação e produção até 10/07/2026) | Criados `410036`, `410037`, `550024`, `550025` (Renaval) e `620007`; **fim de vigência** de `220001`, `220002` e `220003`; incluídos `221002`, `221003` e `221004`; criados tpRBSN, ind_DIR e ind_DUIMP |

## Os 18 CST

O CST é a primeira "rua" do endereço. Para cada um, o portal marca se **exige
tributação**, se tem **redução de base de cálculo ou de alíquota**, **diferimento**,
**transferência de crédito**, **tributação monofásica**, **crédito presumido do IBS
na ZFM** ou **ajuste de competência**. Esses indicadores comandam o que o XML
pode ou deve conter (ver [[df-cst-cclasstrib]], [[df-grupo-ibs-cbs-is]]).

<!-- gerado:cst -->
| CST | Situação | Indicadores marcados | cClassTrib |
|---|---|---|---|
| 000 | Tributação integral | Exige tributação | 6 |
| 010 | Tributação com alíquotas uniformes | Exige tributação | 2 |
| 011 | Tributação com alíquotas uniformes reduzidas | Exige tributação, Redução de alíquota | 5 |
| 200 | Alíquota reduzida | Exige tributação, Redução de alíquota | 56 |
| 220 | Alíquota fixa | Exige tributação | 3 |
| 221 | Alíquota fixa proporcional | Exige tributação | 4 |
| 222 | Redução de Base de Cálculo | Exige tributação, Redução de BC | 1 |
| 400 | Isenção | nenhum | 4 |
| 410 | Imunidade e não incidência | nenhum | 38 |
| 510 | Diferimento | Exige tributação, Diferimento | 1 |
| 515 | Diferimento com redução de alíquota | Exige tributação, Redução de alíquota, Diferimento | 1 |
| 550 | Suspensão | Exige tributação | 29 |
| 620 | Tributação Monofásica | Monofásica | 7 |
| 800 | Transferência de crédito | Transferência de crédito | 2 |
| 810 | Ajuste de IBS na ZFM | Créd. presumido IBS ZFM | 1 |
| 811 | Ajustes | Ajuste de competência | 3 |
| 820 | Tributação em documento específico | nenhum | 9 |
| 830 | Exclusão da Base de Cálculo | Exige tributação | 1 |
<!-- /gerado:cst -->

## Os 173 cClassTrib por CST

Códigos encerrados: `220001`, `220002` e `220003` tiveram a vigência encerrada
em **01/01/2026** (IT v1.60); use a coluna "Vigência" para conferir qualquer
outro. Para o Simples Nacional, os códigos com tpRBSN "9" são de fornecimento
incompatível com o regime; o efeito disso na emissão do optante depende da NT
futura para os CRT 1, 2 e 4 (ver [[df-visao-geral-reforma-nfe]]).

<!-- gerado:cclasstrib -->
### CST 000 — Tributação integral

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 000001 | Situações tributadas integralmente pelo IBS e CBS. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, NFCe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TA, NFAg, NFGas, DIR, DUIMP | 1 Receita bruta interna |
| 000002 | Exploração de via, observado o art. 11 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFSVIA | 1 Receita bruta interna |
| 000003 | Regime automotivo - projetos incentivados, observado o art. 311 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 000004 | Regime automotivo - projetos incentivados, observado o art. 312 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 000005 | Operação com EAC destinado à mistura com gasolina A, mas com saída do biocombustível com destinação diversa, observado o art. 179 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 01/01/2026 em diante | NFe | 1 Receita bruta interna |
| 000006 | Situações tributadas integralmente pelo IBS e CBS realizadas por autônomo | 0% | 0% | Padrão | 01/01/2026 em diante | NFSE | 1 Receita bruta interna |

### CST 010 — Tributação com alíquotas uniformes

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 010001 | Operações do FGTS não realizadas pela Caixa Econômica Federal, observado o art. 212 da Lei Complementar nº 214, de 2025. | 0% | 0% | Uniforme setorial | 05/05/2025 em diante | NFSE, DERE | 9 Incompatível com SN |
| 010002 | Operações do serviço financeiro | 0% | 0% | Uniforme setorial | 30/09/2025 em diante | NFSE, DERE | 1 Receita bruta interna |

### CST 011 — Tributação com alíquotas uniformes reduzidas

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 011001 | Planos de assistência funerária, observado o art. 236 da Lei Complementar nº 214, de 2025. | 60% | 60% | Uniforme nacional | 05/05/2025 em diante | DERE | 1 Receita bruta interna |
| 011002 | Planos de assistência à saúde, observado o art. 237 da Lei Complementar nº 214, de 2025. | 60% | 60% | Uniforme nacional | 05/05/2025 em diante | DERE | 1 Receita bruta interna |
| 011003 | Intermediação de planos de assistência à saúde, observado o art. 240 da Lei Complementar nº 214, de 2025. | 60% | 60% | Uniforme nacional | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 011004 | Concursos e prognósticos, observado o art. 246 da Lei Complementar nº 214, de 2025. | 0% | 0% | Uniforme nacional | 05/05/2025 em diante | DERE | 1 Receita bruta interna |
| 011005 | Planos de assistência à saúde de animais domésticos, observado o art. 243 da Lei Complementar nº 214, de 2025. | 30% | 30% | Uniforme nacional | 05/05/2025 em diante | DERE | 1 Receita bruta interna |

### CST 200 — Alíquota reduzida

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 200001 | Serviços de transporte de bens até as zonas de processamento de exportação e bens exportados a partir das zonas de processamento de exportação, observado o art. 103 da Lei Complementar n 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | CTe, NFSE | 3 Exportação direta |
| 200002 | Fornecimento ou importação de tratores, máquinas e implementos agrícolas, destinados a produtor rural não contribuinte, e de veículos de transporte de carga destinados a transportador autônomo de carga pessoa física não contribuinte, observado o art. 110 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200003 | Vendas de produtos destinados à alimentação humana relacionados no Anexo I da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, que compõem a Cesta Básica Nacional de Alimentos, criada nos termos do art. 8º da Emenda Constitucional nº 132, de 20 de dezembro de 2023, observado o art. 125 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200004 | Fornecimento de dispositivos médicos com a especificação das respectivas classificações da NCM/SH previstas no Anexo XII da Lei Complementar nº 214, de 2025, observado o art. 144 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200005 | Fornecimento de dispositivos médicos com a especificação das respectivas classificações da NCM/SH previstas no Anexo IV da Lei Complementar nº 214, de 2025, quando adquiridos por órgãos da administração pública direta, autarquias, fundações públicas e entidades de saúde imunes, observado o art. 144 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |
| 200006 | Situação de emergência de saúde pública reconhecida pelo Poder Legislativo federal, estadual, distrital ou municipal competente, ato conjunto do Ministro da Fazenda e do Comitê Gestor do IBS poderá ser editado, a qualquer momento, para incluir dispositivos não listados no Anexo XII da Lei Complementar nº 214, de 2025, limitada a vigência do benefício ao período e à localidade da emergência de saúde pública, observado o art. 144 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200007 | Fornecimento dos dispositivos de acessibilidade próprios para pessoas com deficiência relacionados no Anexo XIII da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 145 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200008 | Fornecimento dos dispositivos de acessibilidade próprios para pessoas com deficiência relacionados no Anexo V da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, quando adquiridos por órgãos da administração pública direta, autarquias, fundações públicas e entidades imunes, observado o art. 145 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |
| 200009 | Fornecimento dos medicamentos registrados na Anvisa, observado o art. 146 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DIR, DUIMP | 1 Receita bruta interna |
| 200010 | Fornecimento dos medicamentos registrados na Anvisa, quando adquiridos por órgãos da administração pública direta, autarquias, fundações públicas e entidades imunes, observado o art. 146 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200011 | Fornecimento das composições para nutrição enteral e parenteral, composições especiais e fórmulas nutricionais destinadas às pessoas com erros inatos do metabolismo relacionadas no Anexo VI da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, quando adquiridas por órgãos da administração pública direta, autarquias e fundações públicas, observado o art. 146 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 200012 | Situação de emergência de saúde pública reconhecida pelo Poder Legislativo federal, estadual, distrital ou municipal competente, ato conjunto do Ministro da Fazenda e do Comitê Gestor do IBS poderá ser editado, a qualquer momento, limitada a vigência do benefício ao período e à localidade da emergência de saúde pública, observado o art. 146 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200013 | Fornecimento de tampões higiênicos, absorventes higiênicos internos ou externos, descartáveis ou reutilizáveis, calcinhas absorventes e coletores menstruais, observado o art. 147 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200014 | Fornecimento dos produtos hortícolas, frutas e ovos, relacionados no Anexo XV da Lei Complementar nº 214 , de 2025, com a especificação das respectivas classificações da NCM/SH e desde que não cozidos, observado o art. 148 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200015 | Venda de automóveis de passageiros de fabricação nacional de, no mínimo, 4 (quatro) portas, inclusive a de acesso ao bagageiro, quando adquiridos por motoristas profissionais que exerçam, comprovadamente, em automóvel de sua propriedade, atividade de condutor autônomo de passageiros, na condição de titular de autorização, permissão ou concessão do poder público, e que destinem o automóvel à utilização na categoria de aluguel (táxi), ou por pessoas com deficiência física, visual, auditiva, deficiência mental severa ou profunda, transtorno do espectro autista, com prejuízos na comunicação social e em padrões restritos ou repetitivos de comportamento de nível moderado ou grave, nos termos da legislação relativa à matéria, observado o disposto no art. 149 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe | 1 Receita bruta interna |
| 200016 | Prestação de serviços de pesquisa e desenvolvimento por Instituição Científica, Tecnológica e de Inovação (ICT) sem fins lucrativos para a administração pública direta, autarquias e fundações públicas ou para o contribuinte sujeito ao regime regular do IBS e da CBS, observado o disposto no art. 156 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 200017 | Operações relacionadas ao FGTS, considerando aquelas necessárias à aplicação da Lei nº 8.036, de 1990, realizadas pelo Conselho Curador ou Secretaria Executiva do FGTS, observado o art. 212 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFSE, DERE | 9 Incompatível com SN |
| 200018 | Operações de resseguro e retrocessão ficam sujeitas à incidência à alíquota zero, inclusive quando os prêmios de resseguro e retrocessão forem cedidos ao exterior, observado o art. 223 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | DERE | 9 Incompatível com SN |
| 200019 | Importador dos serviços financeiros que seja contribuinte e tenha direito de apropriação de créditos na aquisição do mesmo serviço financeiro no País, observado o art. 231 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFSE, DERE | 0 Não é receita bruta |
| 200020 | Operação praticada por sociedades cooperativas optantes por regime específico do IBS e CBS, quando o associado destinar bem ou serviço à cooperativa de que participa, e a cooperativa fornecer bem ou serviço ao associado sujeito ao regime regular do IBS e da CBS, observado o art. 271 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe, NFCe, CTe, NF3e, NFSE | 1 Receita bruta interna |
| 200021 | Serviços de transporte público coletivo de passageiros ferroviário e hidroviário urbanos, semiurbanos e metropolitanos, observado o art. 285 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFSE, BPe TM | 1 Receita bruta interna |
| 200022 | Operação originada fora da Zona Franca de Manaus que destine bem material industrializado de origem nacional a contribuinte estabelecido na Zona Franca de Manaus que seja habilitado nos termos do art. 442 da Lei Complementar nº 214, de 2025, e sujeito ao regime regular do IBS e da CBS ou optante pelo regime do Simples Nacional de que trata o art. 12 da Lei Complementar nº 123, de 2006, observado o art. 445 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 200023 | Operação realizada por indústria incentivada que destine bem material intermediário para outra indústria incentivada na Zona Franca de Manaus, desde que a entrega ou disponibilização dos bens ocorra dentro da referida área, observado o art. 448 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 200024 | Operação originada fora das Áreas de Livre Comércio que destine bem material industrializado de origem nacional a contribuinte estabelecido nas Áreas de Livre Comércio que seja habilitado nos termos do art. 456 da Lei Complementar nº 214, de 2025, e sujeito ao regime regular do IBS e da CBS ou optante pelo regime do Simples Nacional de que trata o art. 12 da Lei Complementar nº 123, de 2006, observado o art. 463 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 200025 | Fornecimento dos serviços de educação relacionados ao Programa Universidade para Todos (Prouni), instituído pela Lei nº 11.096, de 13 de janeiro de 2005, observado o art. 308 da Lei Complementar nº 214, de 2025. | 60% | 100% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200026 | Locação de imóveis localizados nas zonas reabilitadas, pelo prazo de 5 (cinco) anos, contado da data de expedição do habite-se, e relacionados a projetos de reabilitação urbana de zonas históricas e de áreas críticas de recuperação e reconversão urbanística dos Municípios ou do Distrito Federal, a serem delimitadas por lei municipal ou distrital, observado o art. 158 da Lei Complementar nº 214, de 2025. | 80% | 80% | Padrão | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 200027 | Operações de locação, cessão onerosa e arrendamento de bens imóveis, observado o art. 261 da Lei Complementar nº 214, de 2025. | 70% | 70% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200028 | Fornecimento dos serviços de educação relacionados no Anexo II da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da Nomenclatura Brasileira de Serviços, Intangíveis e Outras Operações que Produzam Variações no Patrimônio (NBS), observado o art. 129 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200029 | Fornecimento dos serviços de saúde humana relacionados no Anexo III da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NBS, observado o art. 130 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200030 | Venda dos dispositivos médicos relacionados no Anexo IV da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 131 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200031 | Fornecimento dos dispositivos de acessibilidade próprios para pessoas com deficiência relacionados no Anexo V da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 132 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200032 | Fornecimento dos medicamentos registrados na Anvisa ou produzidos por farmácias de manipulação, ressalvados os medicamentos sujeitos à alíquota zero de que trata o art. 146 da Lei Complementar nº 214, de 2025, observado o art. 133 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, DIR, DUIMP | 1 Receita bruta interna |
| 200033 | Fornecimento das composições para nutrição enteral e parenteral, composições especiais e fórmulas nutricionais destinadas às pessoas com erros inatos do metabolismo relacionadas no Anexo VI da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 133 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200034 | Fornecimento dos alimentos destinados ao consumo humano relacionados no Anexo VII da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 135 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200035 | Fornecimento dos produtos de higiene pessoal e limpeza relacionados no Anexo VIII da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH, observado o art. 136 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200036 | Fornecimento de produtos agropecuários, aquícolas, pesqueiros, florestais e extrativistas vegetais in natura, observado o art. 137 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, DUIMP | 1 Receita bruta interna |
| 200037 | Fornecimento de serviços ambientais de conservação ou recuperação da vegetação nativa, mesmo que fornecidos sob a forma de manejo sustentável de sistemas agrícolas, agroflorestais e agrossilvopastoris, em conformidade com as definições e requisitos da legislação específica, observado o art. 137 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200038 | Fornecimento dos insumos agropecuários e aquícolas relacionados no Anexo IX da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH e da NBS, observado o art. 138 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCe, NFSE, DUIMP | 1 Receita bruta interna |
| 200039 | Fornecimento dos bens e serviços listados no Anexo X da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NCM/SH e NBS, nos casos relacionados com produções nacionais artísticas, culturais, de eventos, jornalísticas e audiovisuais, observado o art. 139 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |
| 200040 | Fornec dos seguintes serv de comunic instit à admin púb direta, autarq e fund púb: serviços direcionados ao planej, criação, programação e manutenção de páginas eletrônicas da admin pública, ao monitor e gestão de suas redes sociais e à otimização de páginas e canais digitais para mecanismos de buscas e produção de mensagens, infográficos, painéis interativos e conteúdo institucional, serviços de relações com a imprensa, que reúnem estrat org para promover e reforçar a comunicação dos órgãos e das entidades contratantes com seus públicos de interesse, por meio da interação com prof da imprensa, e serviços de relações públicas, que compreendem o esforço de comunic planej, coeso e contínuo que tem por obj estab adequada percepção da atuação e dos obj instituc, a partir do estímulo à compreensão mútua e da manut de padrões de relac e fluxos de inf entre os órgãos e as entidades contrat e seus públicos de interesse, no País e no exterior, obs o art. 140 da Lei Compl nº 214, de 2025 | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200041 | Operações relacionadas às seguintes atividades desportivas: fornecimento de serviço de educação desportiva, classificado no código 1.2205.12.00 da NBS, e gestão e exploração do desporto por associações e clubes esportivos filiados ao órgão estadual ou federal responsável pela coordenação dos desportos, inclusive por meio de venda de ingressos para eventos desportivos, fornecimento oneroso ou não de bens e serviços, inclusive ingressos, por meio de programas de sócio-torcedor, cessão dos direitos desportivos dos atletas e transferência de atletas para outra entidade desportiva ou seu retorno à atividade em outra entidade desportiva, observado o art. 141 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200042 | Operações relacionadas às seguintes atividades desportivas: gestão e exploração do desporto por associações e clubes esportivos filiados ao órgão estadual ou federal responsável pela coordenação dos desportos, observado o art. 141 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200043 | Fornecimento à administração pública direta, autarquias e fundações púbicas dos serviços e dos bens relativos à soberania e à segurança nacional, à segurança da informação e à segurança cibernética relacionados no Anexo XI da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NBS e da NCM/SH, observado o art. 142 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFe, NFCom, NFSE, DUIMP | 1 Receita bruta interna |
| 200044 | Operações e prestações de serviços de segurança da informação e segurança cibernética desenvolvidos por sociedade que tenha sócio brasileiro com o mínimo de 20% (vinte por cento) do seu capital social, relacionados no Anexo XI da Lei Complementar nº 214, de 2025, com a especificação das respectivas classificações da NBS e da NCM/SH, observado o art. 142 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFCom, NFSE | 1 Receita bruta interna |
| 200045 | Operações relacionadas a projetos de reabilitação urbana de zonas históricas e de áreas críticas de recuperação e reconversão urbanística dos Municípios ou do Distrito Federal, a serem delimitadas por lei municipal ou distrital, observado o art. 158 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 05/05/2025 em diante | NFSE, NFABI | 1 Receita bruta interna |
| 200046 | Operações com bens imóveis, observado o art. 261 da Lei Complementar nº 214, de 2025. | 50% | 50% | Padrão | 05/05/2025 em diante | NFSE, NFABI | 1 Receita bruta interna |
| 200047 | Bares e Restaurantes, observado o art. 275 da Lei Complementar nº 214, de 2025. | 40% | 40% | Padrão | 05/05/2025 em diante | NFe, NFCe | 1 Receita bruta interna |
| 200048 | Hotelaria, Parques de Diversão e Parques Temáticos, observado o art. 281 da Lei Complementar nº 214, de 2025. | 40% | 40% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200049 | Transporte coletivo de passageiros rodoviário, ferroviário e hidroviário intermunicipais e interestaduais, observado o art. 286 da Lei Complementar nº 214, de 2025. | 40% | 40% | Padrão | 05/05/2025 em diante | BPe | 1 Receita bruta interna |
| 200050 | Serviços de transporte aéreo regional coletivo de passageiros ou de carga, observado o art. 287 da Lei Complementar nº 214, de 2025. | 40% | 40% | Padrão | 05/05/2025 em diante | CTe, CTe OS, BPe TA | 1 Receita bruta interna |
| 200051 | Agências de Turismo, observado o art. 289 da Lei Complementar nº 214, de 2025. | 40% | 40% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200052 | Prestação de serviços das seguintes profissões intelectuais de natureza científica, literária ou artística, submetidas à fiscalização por conselho profissional: administradores, advogados, arquitetos e urbanistas, assistentes sociais, bibliotecários, biólogos, contabilistas, economistas, economistas domésticos, profissionais de educação física, engenheiros e agrônomos, estatísticos, médicos veterinários e zootecnistas, museólogos, químicos, profissionais de relações públicas, técnicos industriais e técnicos agrícolas, observado o art. 127 da Lei Complementar nº 214, de 2025. | 30% | 30% | Padrão | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 200053 | Fornecimento de medicamentos registrados na Anvisa, quando classificados como soros ou vacinas, observado o art. 146 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 01/01/2026 em diante | NFe, NFCe, DIR, DUIMP | 1 Receita bruta interna |
| 200054 | Fornecimento de bem material pela cooperativa de produção agropecuária a associado não sujeito ao regime regular do IBS e da CBS com anulação de créditos referentes ao bem fornecido, observado o art. 271 da Lei Complementar nº 214, de 2025. | 100% | 100% | Padrão | 01/01/2026 em diante | NFe, NFCe, NFSE | 9 Incompatível com SN |
| 200055 | Fornecimento dos serviços com redução de alíquota de 60% realizado por autônomo, observado o art. 128 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 01/01/2026 em diante | NFSE | 1 Receita bruta interna |
| 200056 | Fornecimento dos serviços com redução de alíquota de 30% realizado por autônomo, observado o art. 127 da Lei Complementar nº 214, de 2025. | 30% | 30% | Padrão | 01/01/2026 em diante | NFSE | 1 Receita bruta interna |

### CST 220 — Alíquota fixa

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 220001 | Incorporação imobiliária submetida ao regime especial de tributação, observado o art. 485 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 05/05/2025 a 01/01/2026 | NFABI | 0 Não é receita bruta |
| 220002 | Incorporação imobiliária submetida ao regime especial de tributação, observado o art. 485 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 05/05/2025 a 01/01/2026 | NFABI | 0 Não é receita bruta |
| 220003 | Alienação de imóvel decorrente de parcelamento do solo, observado o art. 486 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 05/05/2025 a 01/01/2026 | NFABI | 0 Não é receita bruta |

### CST 221 — Alíquota fixa proporcional

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 221001 | Locação, cessão onerosa ou arrendamento de bem imóvel com alíquota sobre a receita bruta, observado o art. 487 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 05/05/2025 em diante | NFSE | 1 Receita bruta interna |
| 221002 | Incorporação imobiliária submetida ao regime especial de tributação, observado o art. 485 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 01/01/2026 em diante | NFABI | 9 Incompatível com SN |
| 221003 | Incorporação imobiliária submetida ao regime especial de tributação, observado o art. 485 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 01/01/2026 em diante | NFABI | 9 Incompatível com SN |
| 221004 | Alienação de imóvel decorrente de parcelamento do solo, observado o art. 486 da Lei Complementar nº 214, de 2025. | 0% | 0% | Fixa | 01/01/2026 em diante | NFABI | 1 Receita bruta interna |

### CST 222 — Redução de Base de Cálculo

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 222001 | Transporte internacional de passageiros, caso os trechos de ida e volta sejam vendidos em conjunto, a base de cálculo será a metade do valor cobrado, observado o Art. 12 § 8º da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | CTe OS, BPe, BPe TA | 5 Mercado interno/exportação |

### CST 400 — Isenção

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 400001 | Fornecimento de serviços de transporte público coletivo de passageiros rodoviário e metroviário de caráter urbano, semiurbano e metropolitano, sob regime de autorização, permissão ou concessão pública, observado o art. 157 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | BPe, NFSE, BPe TM | 1 Receita bruta interna |
| 400002 | Fornecimento de serviços de transporte público coletivo de passageiros rodoviário e metroviário de caráter urbano, semiurbano e metropolitano, sob regime de autorização, permissão ou concessão pública, com medição por quilômetro rodado, observado o art. 157 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | CTe OS | 1 Receita bruta interna |
| 400003 | Bagagens de viajantes e de tripulantes, acompanhadas ou desacompanhadas, observado o art. 94 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | DIR, DUIMP | 0 Não é receita bruta |
| 400004 | Remessas internacionais, observado o art. 94 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | DIR, DUIMP | 0 Não é receita bruta |

### CST 410 — Imunidade e não incidência

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 410001 | Fornecimento de bonificações quando constem do respectivo documento fiscal e que não dependam de evento posterior, observado o art. 5º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TA, NFAg, NFABI, NFGas, DUIMP | 0 Não é receita bruta |
| 410002 | Transferências entre estabelecimentos pertencentes ao mesmo contribuinte, observado o art. 6º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 0 Não é receita bruta |
| 410003 | Doações que não tenham por objeto bens ou serviços que tenham permitido a apropriação de créditos pelo doador, observado o art. 6º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TA, NFAg, NFABI, NFGas, DERE, DUIMP | 0 Não é receita bruta |
| 410004 | Exportações de bens e serviços, observado o art. 8º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TA | 3 Exportação direta |
| 410005 | Fornecimentos realizados pela União, pelos Estados, pelo Distrito Federal e pelos Municípios, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFSE, NFAg | 9 Incompatível com SN |
| 410006 | Fornecimentos realizados por entidades religiosas e templos de qualquer culto, inclusive suas organizações assistenciais e beneficentes, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFSE | 9 Incompatível com SN |
| 410007 | Fornecimentos realizados por partidos políticos, inclusive suas fundações, entidades sindicais dos trabalhadores e instituições de educação e de assistência social, sem fins lucrativos, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFSE | 9 Incompatível com SN |
| 410008 | Fornecimentos de livros, jornais, periódicos e do papel destinado a sua impressão, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFCom, NFSE, DIR, DUIMP | 2 Receita bruta interna sem cálculo IBS/CBS |
| 410009 | Fornecimentos de fonogramas e videofonogramas musicais produzidos no Brasil contendo obras musicais ou literomusicais de autores brasileiros e/ou obras em geral interpretadas por artistas brasileiros, bem como os suportes materiais ou arquivos digitais que os contenham, salvo na etapa de replicação industrial de mídias ópticas de leitura a laser, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFCom, NFSE, DIR, DUIMP | 2 Receita bruta interna sem cálculo IBS/CBS |
| 410010 | Fornecimentos de serviço de comunicação nas modalidades de radiodifusão sonora e de sons e imagens de recepção livre e gratuita, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFCom, NFSE, DERE | 2 Receita bruta interna sem cálculo IBS/CBS |
| 410011 | Fornecimentos de ouro, quando definido em lei como ativo financeiro ou instrumento cambial, observado o art. 9º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | - | 2 Receita bruta interna sem cálculo IBS/CBS |
| 410012 | Fornecimento de condomínio edilício não optante pelo regime regular, observado o art. 26 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFSE | 9 Incompatível com SN |
| 410013 | Exportações de combustíveis, observado o art. 98 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 3 Exportação direta |
| 410014 | Fornecimento de produtor rural não contribuinte, observado o art. 164 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, NFSE | 1 Receita bruta interna |
| 410015 | Fornecimento por transportador autônomo não contribuinte, observado o art. 169 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | CTe, NFSE | 9 Incompatível com SN |
| 410016 | Fornecimento ou aquisição de resíduos sólidos, observado o art. 170 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 410017 | Aquisição de bem móvel com crédito presumido sob condição de revenda realizada, observado o art. 171 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 0 Não é receita bruta |
| 410018 | Operações relacionadas aos fundos garantidores e executores de políticas públicas, inclusive de habitação, previstos em lei, assim entendidas os serviços prestados ao fundo pelo seu agente operador e por entidade encarregada da sua administração, observado o art. 213 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFABI, DERE | 9 Incompatível com SN |
| 410019 | Exclusão da gorjeta na base de cálculo no fornecimento de alimentação, observado o art. 274 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe | 1 Receita bruta interna |
| 410020 | Exclusão do valor de intermediação na base de cálculo no fornecimento de alimentação, observado o art. 274 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe | 1 Receita bruta interna |
| 410021 | Contribuição de que trata o art. 149-A da Constituição Federal, observado o art. 12 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NF3e | 9 Incompatível com SN |
| 410022 | Consolidação da propriedade pelo credor de bens móveis ou imóveis que tenham sido objeto de garantia, observado o art. 200 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFABI | 0 Não é receita bruta |
| 410023 | Alienação de bens móveis ou imóveis que tenham sido objeto de garantia constituída em favor de credor em que o prestador da garantia não seja contribuinte, observado o art. 200 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFABI | 9 Incompatível com SN |
| 410024 | Consolidação da propriedade pelo grupo de consórcio de bem que tenha sido objeto de garantia, observado o art. 204 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFABI | 1 Receita bruta interna |
| 410025 | Alienação de bem que tenha sido objeto de garantia constituída em favor do grupo de consórcio em que o prestador da garantia não seja contribuinte, observado o art. 204 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFABI | 9 Incompatível com SN |
| 410026 | Doações sem contraprestação em benefício do doador, com anulação de crédito apropriados pelo doador referente ao fornecimento doado, observado o art. 6º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFCe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TA, NFAg, NFABI, NFGas, DERE | 0 Não é receita bruta |
| 410027 | Fornecimento de bens e serviços, desde que vinculados direta e exclusivamente à exportação de bens materiais ou associados à entrega no exterior de bens materiais, observado o art. 6º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NFe, CTe, CTe OS, NFSE | 3 Exportação direta |
| 410028 | Operações com bens imóveis realizadas por pessoas físicas não consideradas contribuintes do regime regular do IBS e da CBS, observado o art. 251 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | - | 9 Incompatível com SN |
| 410029 | Operações não sujeitas à incidência de IBS e de CBS, alcançadas apenas por obrigação acessória do ICMS, observado o art. 4º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NFe, NFCe | 0 Não é receita bruta |
| 410030 | Estorno de crédito apropriado de bens adquiridos e venham a perecer, deteriorar-se ou ser objeto de roubo, furto ou extravio, observado o art. 47 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NFe | 0 Não é receita bruta |
| 410031 | Fornecimento em período anterior ao início de vigência de incidências de CBS e IBS, observado o art. 544 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NFe, NF3e, NFCom, NFAg, NFGas | 1 Receita bruta interna |
| 410032 | Tributos incidentes na operação que não integram a base de cálculo do IBS e da CBS, observado o art. 12 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NF3e, NFCom, NFAg, NFGas | 0 Não é receita bruta |
| 410033 | Operações com bens imóveis, inclusive operações com direitos reais sobre bens imóveis, realizadas por Fundos de Investimento Imobiliário (FII) e Fundos de Investimento nas Cadeias Produtivas do Agronegócio (Fiagro), observado o art. 26 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFSE, NFABI | 9 Incompatível com SN |
| 410034 | Fundos de investimento cujo patrimônio seja constituído exclusivamente por aplicações em participações societárias, certificados, direitos, títulos, valores mobiliários e demais ativos financeiros permitidos pela Comissão de Valores Mobiliários, observado o art. 26 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | - | 9 Incompatível com SN |
| 410035 | Fornecimento realizado por nanoempreendedor, observado o art. 26 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, NFCe, CTe, CTe OS, NFSE | 9 Incompatível com SN |
| 410036 | Descontos financeiros em nota fatura, observado o art. 12 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NF3e, NFCom, NFAg, NFGas | 0 Não é receita bruta |
| 410037 | Importação de bens materiais sem incidência de IBS e CBS, observado o art. 66 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | DIR, DUIMP | 0 Não é receita bruta |
| 410999 | Operações não onerosas sem previsão de tributação, não especificadas anteriormente, observado o art. 4º da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFCe, CTe, CTe OS, BPe, NF3e, NFCom, NFSE, BPe TM, BPe TA, NFAg, NFABI, NFGas, DUIMP | 0 Não é receita bruta |

### CST 510 — Diferimento

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 510001 | Operações, sujeitas a diferimento, com energia elétrica ou com direitos a ela relacionados, relativas à importação, geração, comercialização, distribuição e transmissão, observado o art. 28 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NF3e, DUIMP | 2 Receita bruta interna sem cálculo IBS/CBS |

### CST 515 — Diferimento com redução de alíquota

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 515001 | Operações, sujeitas a diferimento, com insumos agropecuários e aquícolas, observado o art. 138 da Lei Complementar nº 214, de 2025. | 60% | 60% | Padrão | 30/09/2025 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |

### CST 550 — Suspensão

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 550001 | Exportações de bens materiais, observado o art. 82 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 4 Exportação indireta |
| 550002 | Regime de Trânsito, observado o art. 84 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | DUIMP | 0 Não é receita bruta |
| 550003 | Regimes de Depósito, observado o art. 85 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550004 | Regimes de Depósito, observado o art. 87 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 4 Exportação indireta |
| 550005 | Regimes de Depósito, observado o art. 87 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 4 Exportação indireta |
| 550006 | Regimes de Permanência Temporária com suspensão total, observado o art. 88 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550007 | Regimes de Aperfeiçoamento (Recof), observado o art. 90 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550008 | Importação de bens para o Regime de Repetro-Temporário, de que tratam o inciso I do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550009 | GNL-Temporário, de que trata o inciso II do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550010 | Repetro-Permanente, de que trata o inciso III do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550011 | Repetro-Industrialização, de que trata o inciso IV do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550012 | Repetro-Nacional, de que trata o inciso V do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 1 Receita bruta interna |
| 550013 | Repetro-Entreposto, de que trata o inciso VI do art. 93 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550014 | Zona de Processamento de Exportação, observado os arts. 99 e 100 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 4 Exportação indireta |
| 550015 | Regime Tributário para Incentivo à Modernização e à Ampliação da Estrutura Portuária - Reporto, observado o art. 105 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550016 | Regime Especial de Incentivos para o Desenvolvimento da Infraestrutura - Reidi, observado o art. 106 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |
| 550017 | Regime Tributário para Incentivo à Atividade Econômica Naval – Renaval, observado o art. 107 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550018 | Desoneração da aquisição de bens de capital, observado o art. 109 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550019 | Importação de bem material por indústria incentivada para utilização na Zona Franca de Manaus, observado o art. 443 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550020 | Áreas de livre comércio, observado o art. 461 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550021 | Fornecimento de produtos agropecuários in natura para contribuinte do regime regular que promova industrialização destinada a exportação, observado o art. 82 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe | 4 Exportação indireta |
| 550022 | Regime Especial de Incentivos para a Produção de Hidrogênio de Baixa Emissão de Carbono (Rehidro), observado o art. 106 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, NFSE, DUIMP | 1 Receita bruta interna |
| 550023 | Operações com hidrocarbonetos líquidos derivados de petróleo não combustíveis ou de gás natural, inclusive nafta, observado o art. 172 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, DUIMP | 1 Receita bruta interna |
| 550024 | Importações e nas aquisições no mercado interno de máquinas, equipamentos e veículos destinados a utilização nas atividades de que trata o inciso IIIdo art. 107 efetuadas para incorporação a seu ativo imobilizado, observado o art. 107 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | DUIMP | 1 Receita bruta interna |
| 550025 | Importações e nas aquisições no mercado interno de matérias-primas, produtos intermediários, partes, peças e componentes para utilização na construção, conservação, modernização e reparo de embarcações pré-registradas ou registradas no REB, observado o art. 107 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | DUIMP | 1 Receita bruta interna |
| 550026 | Regimes de admissão temporária com suspensão total do pagamento dos tributos durante o período de sua permanência na Zona Franca de Manaus, observado o art. 89 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550027 | Regimes de Aperfeiçoamento (Drawback), observado o art. 90 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550028 | Regimes de Aperfeiçoamento (Admissão temporária), observado o art. 90 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe, DUIMP | 0 Não é receita bruta |
| 550029 | Zona de Processamento de Exportação, observado os art. 102 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe | 4 Exportação indireta |

### CST 620 — Tributação Monofásica

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 620001 | Tributação monofásica sobre combustíveis, observados os art. 172 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, DUIMP | 9 Incompatível com SN |
| 620002 | Tributação monofásica com responsabilidade pela retenção sobre combustíveis, observado o art. 178 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, DUIMP | 9 Incompatível com SN |
| 620003 | Tributação monofásica com responsabilidade de retenção de tributos por terceiros, observado o art. 178 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, DUIMP | 9 Incompatível com SN |
| 620004 | Tributação monofásica sobre mistura de EAC com gasolina A em percentual superior ou inferior ao obrigatório, observado o art. 179 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe | 9 Incompatível com SN |
| 620005 | Tributação monofásica sobre mistura de EAC com gasolina A em percentual superior ou inferior ao obrigatório, observado o art. 179 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe | 9 Incompatível com SN |
| 620006 | Tributação monofásica sobre combustíveis cobrada anteriormente, observador o art. 180 da Lei Complementar nº 214, de 2025. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, NFCe | 2 Receita bruta interna sem cálculo IBS/CBS |
| 620007 | Perecimento, deteriorização, roubo, furto ou extravio no regime monofásico sem estorno de crédito, observado o art. 47 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | NFe | 0 Não é receita bruta |

### CST 800 — Transferência de crédito

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 800001 | Fusão, cisão ou incorporação, observado o art. 55 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFSE | 0 Não é receita bruta |
| 800002 | Transferência de crédito do associado, inclusive as cooperativas singulares, para cooperativa de que participa das operações antecedentes às operações em que fornece bens e serviços e os créditos presumidos, observado o art. 272 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe, NFSE | 0 Não é receita bruta |

### CST 810 — Ajuste de IBS na ZFM

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 810001 | Crédito presumido sobre o valor apurado nos fornecimentos a partir da Zona Franca de Manaus, observado o art. 450 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFe | 0 Não é receita bruta |

### CST 811 — Ajustes

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 811001 | Anulação de crédito proporcional ao valor das operações imunes e isentas, observado o art. 51 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFSE | 0 Não é receita bruta |
| 811002 | Débitos de notas fiscais não processadas na apuração, observado o art. 45 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFSE | 0 Não é receita bruta |
| 811003 | Débitos apurados após o desenquadramento do regime Simples Nacional, observado o art. 41 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFe, NFSE | 0 Não é receita bruta |

### CST 820 — Tributação em documento específico

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 820001 | Documento com informações de fornecimento de serviços de planos de assistência à saúde elencados no art. 234 da Lei Complementar nº 214, de 2025, mas com tributação realizada por outro meio | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 820002 | Documento com informações de fornecimento de serviços de planos de assinstência funerária, mas com tributação realizada por outro meio, observado o art. 236 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 820003 | Documento com informações de fornecimento de serviços de planos de assinstência à saúde de animais domésticos, mas com tributação realizada por outro meio, observado o art. 243 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 820004 | Documento com informações de prestação de serviços de consursos de prognósticos, mas com tributação realizada por outro meio, observado o art. 248 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFSE | 9 Incompatível com SN |
| 820005 | Documento com informações de alienação de bens imóveis, mas com tributação realizada por outro meio,, observado o art. 254 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 05/05/2025 em diante | NFABI | 0 Não é receita bruta |
| 820006 | Documento com informações de fornecimento de serviços de exploração de via, mas com tributação realizada por outro meio, observado o art. 11 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 30/09/2025 em diante | NFSE | 0 Não é receita bruta |
| 820007 | Documento com informações de fornecimento de serviços financeiros, mas com tributação realizada por outro meio, observado o art. 181 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NFSE | 9 Incompatível com SN |
| 820008 | Documento com informações de fornecimento de serviço continuado, mas com tributação realizada em fatura anterior, observado o art. 10 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 19/11/2025 em diante | NF3e, NFCom, NFAg, NFGas | 0 Não é receita bruta |
| 820009 | Fornecimentos declarados e tributados em outro documento, observado o art. 60 da Lei Complementar nº 214, de 2025. | 0% | 0% | Sem alíquota | 01/01/2026 em diante | CTe OS, NF3e, NFCom, NFSE, NFAg, NFGas | 0 Não é receita bruta |

### CST 830 — Exclusão da Base de Cálculo

| cClassTrib | Descrição | Red. IBS | Red. CBS | Alíquota | Vigência | Documentos | Simples (tpRBSN) |
|---|---|---|---|---|---|---|---|
| 830001 | Documento com exclusão da base de cálculo da CBS e do IBS refrente à energia elétrica fornecida pela distribuidora à unidade consumidora, conforme Art 28, parágrafos 3° e 4°. | 0% | 0% | Padrão | 05/05/2025 em diante | NFe, NF3e | 0 Não é receita bruta |
<!-- /gerado:cclasstrib -->

## O que esta nota não responde

- A tabela diz **que códigos existem**. Qual deles usar numa operação concreta
  depende de enquadrar o produto ou serviço no dispositivo da LC 214, o que está
  nas notas do domínio reforma (ex.: [[reducao-60-alimentos-higiene-agro]],
  [[cesta-basica-nacional]]) e não nesta tabela.
- Os códigos de crédito presumido (cCredPres) estão em
  [[df-credito-presumido-ccredpres]].
- As tabelas de NCM do Imposto Seletivo (Anexo I) e de **cClassTribIS** (Anexo II)
  seguem "a ser publicadas" na NT 2025.002-RTC.
- As listas de NCM/NBS ligadas a 35 cClassTrib (4.728 itens; "anexo técnico"
  9XXXY, em que XXX é o artigo da LC 214 que define a lista, segundo o IT) estão
  só no JSON e ainda não viraram nota.

## Ligações

- [[df-cst-cclasstrib]]: o mecanismo (campos UB13, UB14, regras de validação).
- [[df-credito-presumido-ccredpres]]: a tabela irmã, de crédito presumido.
- [[df-grupo-ibs-cbs-is]]: os grupos que cada código libera ou exige.
- [[df-calculo-e-validacoes]]: regras que dependem dos indicadores e as alíquotas
  padrão a informar.
