---
título: Tabela cCredPres — códigos de crédito presumido do IBS e da CBS
dominio: documentos-fiscais
fontes: Portal dos DF-e (SVRS), tabela de crédito presumido, captura 2026-10-08; IT 2025.002 v1.60, seções 04 e 06; NT 2025.002-RTC v1.52, grupo gCredPresOper (UB120 a UB130)
vigencia: com-mudanca-programada
texto-base: 2026-10-08
---

# Tabela cCredPres (crédito presumido)

## A lógica em uma frase

Quando a LC 214 dá **crédito presumido** a quem compra (ex.: de produtor rural não
contribuinte) ou a quem opera na ZFM, o documento fiscal precisa dizer **qual**
hipótese legal está sendo usada. O código cCredPres faz isso: é o "número da
hipótese" que vai no campo `cCredPres` do grupo `gCredPresOper` (ver
[[df-grupo-ibs-cbs-is]]). A regra de mérito (quem tem direito e quanto) está na
LC 214, nas notas do domínio reforma.

## De onde vêm os dados

- **IT 2025.002 v1.60, seção 04:** define a tabela e as colunas; a seção 06 dá o
  endereço interativo https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido.
- **Captura de 2026-10-08** dessa página: **13 códigos**. Arquivos em
  `fontes/documentos-fiscais/texto/`: `ccredpres-svrs.json` e `ccredpres-svrs.md`.
  Para atualizar: `python scripts/tabelas_svrs.py ccredpres --data AAAA-MM-DD`.
- A NT 2025.002-RTC manda "Utilizar tabela cCredPres (Anexo IV)" no campo
  `cCredPres` (UB122). A tabela fica fora do PDF da NT.
- **Hierarquia:** a tabela diz **como informar** o crédito presumido no
  documento; o direito ao crédito vem da LC 214/2025, que prevalece.

## Como ler a tabela (IT, seção 04)

| Coluna desta nota | Definição no IT |
|---|---|
| Apropria no DF-e | "Apropria via NF?": a apropriação pode ser feita direto no documento fiscal (NF-e ou NFS-e) |
| Apropria por evento | "Apropria via evento?": a apropriação deve ser feita por evento específico (ver [[df-eventos-apuracao]]) |
| Deduz do tributo | indDeduzCredPres: o crédito presumido é deduzido no cálculo do valor do tributo do item (na NT, `vIBS` = `vIBSUF` + `vIBSMun` menos `vCredPres` quando o indicador é 1; ver [[df-grupo-ibs-cbs-is]]) |
| Declaração de pagamento | coluna da página do portal, sem definição no IT. A NT tem o evento 112110, "Informação de efetivo pagamento integral para liberar crédito presumido do adquirente" ([[df-eventos-apuracao]]); a página não diz que a coluna se refere a esse evento |
| Documentos | documentos em que o código pode ser informado (NF-e, NFC-e, CT-e, NFS-e) |
| IBS / CBS | dIniVig/dFimVig de cada tributo (o IT separa a vigência do IBS e a da CBS) |

**Colunas do IT que a página não mostra (⚠️ lacuna):** ind_gCBSCredPres e
ind_gIBSCredPres (se o grupo de crédito presumido da CBS ou do IBS deve ser
preenchido), "Alíquota CBS", "Alíquota IBS", pAliqCredPresCBS, pAliqCredPresIBS,
pRedTransicaoIBS (criada na v1.60) e "cClass nota referenciada". Estão na
planilha do Portal Nacional da NF-e ("Documentos" → "Diversos"), que **não está
nas fontes**. Os **percentuais e as fórmulas** de mérito estão nos regulamentos
da CBS e do IBS, para os códigos 1 a 4 (produtor rural, transportador autônomo,
reciclagem e bens usados): ver [[ibs-cbs-credito-presumido-regulamentacao]].
Para os demais códigos, ver as notas da reforma ligadas a cada um.

## Hoje (08/10/2026)

**Nenhum código tem início de vigência até hoje.** As datas informadas vão de
01/01/2027 a 01/01/2029; o IBS do código 8 aparece sem data ("Não informado"
na página). Detalhe no bloco abaixo. Por ora, a tabela serve para preparar
sistemas.

## ⏳ A partir de 01/01/2027 — tabela cCredPres (início de vigência dos códigos)

| cCredPres | Hipótese (art. da LC 214) | Apropria no DF-e | Apropria por evento | Deduz do tributo | Declaração de pagamento | Documentos | IBS | CBS | Mérito na reforma |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Aquisição de produtor rural e produtor rural integrado não contribuinte (art. 168) | Não | Sim | Não | Sim | NFe, NFSe | 01/01/2027 em diante | 01/01/2027 em diante | [[produtor-rural-e-integrado]] |
| 2 | Serviço de transportador autônomo de carga pessoa física não contribuinte (art. 169) | Não | Sim | Não | Sim | CTe, NFSe | 01/01/2027 em diante | 01/01/2027 em diante | [[transportador-autonomo-reciclagem-usados]] |
| 3 | Resíduos e materiais para reciclagem, reutilização ou logística reversa de pessoa física, cooperativa ou organização popular (art. 170) | Não | Sim | Não | Sim | NFe | **01/01/2029** em diante | 01/01/2027 em diante | [[transportador-autonomo-reciclagem-usados]] |
| 4 | Bens móveis usados de pessoa física não contribuinte para revenda (art. 171) | Sim | Sim | Sim | Sim | NFe, NFCe | 01/01/2027 em diante | 01/01/2027 em diante | [[transportador-autonomo-reciclagem-usados]] |
| 5 | Regime automotivo (art. 311) | Sim | Não | Não | Não | NFe | não se aplica | 01/01/2027 em diante | [[regimes-diferenciados-cbs-prouni-automotivo]] |
| 6 | Regime automotivo (art. 312) | Sim | Não | Não | Não | NFe | não se aplica | 01/01/2027 em diante | [[regimes-diferenciados-cbs-prouni-automotivo]] |
| 7 | Aquisição por contribuinte na Zona Franca de Manaus (art. 444) | Sim | Não | Sim | Não | NFe | 01/01/2027 em diante | não se aplica | [[zona-franca-manaus-e-alc]] |
| 8 | Aquisição por contribuinte na ZFM (art. 447) | Não | Sim | Não | Não | NFe | **início não informado** | não se aplica | [[zona-franca-manaus-e-alc]] |
| 9 | Aquisição por contribuinte na ZFM (art. 449) | Não | Sim | Não | Não | NFe | **01/01/2029** em diante | não se aplica | [[zona-franca-manaus-e-alc]] |
| 10 | Aquisição por contribuinte na ZFM (art. 450) | Sim | Não | Não | Não | NFe | não se aplica | 01/01/2027 em diante | [[zona-franca-manaus-e-alc]] |
| 11 | Aquisição por contribuinte na Área de Livre Comércio (art. 462) | Sim | Não | Sim | Não | NFe | 01/01/2027 em diante | não se aplica | [[zona-franca-manaus-e-alc]] |
| 12 | Aquisição por contribuinte na Área de Livre Comércio (art. 465) | Não | Sim | Não | Não | NFe | **01/01/2029** em diante | não se aplica | [[zona-franca-manaus-e-alc]] |
| 13 | Aquisição pela indústria na Área de Livre Comércio (art. 467) | Sim | Não | Não | Não | NFe | não se aplica | 01/01/2027 em diante | [[zona-franca-manaus-e-alc]] |

A descrição completa de cada código, na redação do portal, está em
`ccredpres-svrs.md`. "Não se aplica" quer dizer que o código não vale para aquele
tributo (ex.: o regime automotivo, códigos 5 e 6, é só de CBS na tabela).

## ⚠️ Divergência: exemplo da NT × tabela oficial

O leiaute da NT 2025.002-RTC v1.52 (campo `cCredPres`, UB122) traz como
exemplos: "1 - Aquisição de Produtor Rural não contribuinte"; "2 - Tomador de
serviço de transporte de TAC PF não contrib."; "3 - Aquisição de pessoa física
com destino à reciclagem"; "4 - Aquisição de bens móveis de PF não contrib. para
revenda"; e **"5 - Regime opcional para cooperativa"**. Na tabela capturada, os
códigos 1 a 4 conferem, mas o **5 é o regime automotivo (art. 311)**, e não há
código para cooperativa. **Vale a tabela**: a própria NT manda usar a tabela
cCredPres, e o exemplo do leiaute ficou desatualizado.

## Ligações

- [[df-grupo-ibs-cbs-is]]: o grupo `gCredPresOper` e os campos `vBCCredPres`,
  `cCredPres`, `gIBSCredPres` e `gCBSCredPres`.
- [[df-eventos-apuracao]]: os eventos 112110 e 211110 (apropriação por evento).
- [[df-tabela-cclasstrib]]: a tabela irmã (CST e cClassTrib) e o indicador
  ind_gCredPresOper de cada cClassTrib.
