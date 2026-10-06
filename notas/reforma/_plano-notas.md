---
título: Plano de notas — reforma tributária (LC 214/2025 + LC 227/2026)
status: rascunho de trabalho — não é conteúdo final
---

# Plano final aprovado (87 notas)

Legenda: 🔵 só LC 214/2025 · 🟢 só LC 227/2026 · 🟡 ambas (227 alterou dispositivo da 214)

Fontes de trabalho (scratchpad da sessão):
- `lc214.txt` — texto extraído via PyMuPDF do PDF compilado da LC 214 (544 artigos + 23 anexos, já COM as marcações "(Incluído/Redação dada pela Lei Complementar nº 227, de 2026)")
- `lc227_ocr.txt` — texto via OCR (RapidOCR) do PDF da LC 227 (104 páginas, 182 artigos; PDF sem camada de texto, texto virou vetor no "Print to PDF")
- `outline214.txt`, `outline214_top.txt` — estrutura LIVRO/TÍTULO/CAPÍTULO/Seção/Subseção da 214
- `pg227/p*.png` — páginas renderizadas da 227 para conferência visual quando o OCR for ambíguo

## Ajustes desta rodada em relação à proposta de 82→96 notas

1. Simples Nacional unificado: `simples-nacional-e-mei.md` (🟡) absorve LC 214 arts. 516–520 + Anexos XVIII–XXIII E LC 227 arts. 168, 169, 181-IV.
2. Grupo "legislação correlata" da 227 fundido em `lc227-alteracoes-legislacao-correlata.md` (🟢), com uma seção por lei alterada.
3. Grupo 4 (reduções 30/60/zero) mantido como 10 notas separadas, sem fusão.
4. Arts. 179 e 180 da 227 NÃO viram seção própria em `lc227-alteracoes-legislacao-correlata.md` — seguem a mesma regra do art. 174 (alteração direta de dispositivo da 214) e são distribuídos:
   - art. 179 (altera art. 172 da LC 214 — combustíveis) → dentro de `regime-especifico-combustiveis.md`, bloco "## Alterações pela LC 227/2026"
   - art. 180 (altera art. 481 §5º-A da LC 214 — CGIBS) → dentro de `cgibs-na-lc214.md`, bloco "## Alterações pela LC 227/2026"

## Padrão de cada nota

- Frontmatter simples: título, origem (214/227/ambas), artigos cobertos.
- Conteúdo curado (não é despejo do texto legal): explicação didática da lógica/regra, com os artigos citados como referência.
- Notas 🟡 fecham com `## Alterações pela LC 227/2026` explicando o que mudou e por quê, quando identificável.

---

## 1. Núcleo IBS/CBS — arts. 1–62 (16 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| ibs-cbs-conceitos-principios.md | 1–3 | 🔵 |
| ibs-cbs-hipoteses-incidencia.md | 4–7 | 🟡 (6, 40, 50) |
| ibs-cbs-imunidades.md | 8–9 | 🔵 |
| ibs-cbs-fato-gerador-momento.md | 10 | 🟡 (§3º novo) |
| ibs-cbs-local-operacao.md | 11 | 🟡 (inciso X; §8º revogado) |
| ibs-cbs-base-calculo.md | 12–13 | 🟡 |
| ibs-cbs-aliquotas.md | 14–20 | 🟡 |
| ibs-cbs-sujeicao-passiva.md | 21–26 | 🟡 |
| ibs-cbs-extincao-debitos.md | 27–30 | 🟡 |
| ibs-cbs-split-payment.md | 31–35 | 🟡 |
| ibs-cbs-fim-substituicao-tributaria.md | 31–35 (conceitual; nota criada após o plano) | 🟡 |
| ibs-cbs-recolhimento-adquirente-responsavel.md | 36–37 | 🔵 |
| ibs-cbs-pagamento-indevido-ressarcimento.md | 38–40 | 🟡 |
| ibs-cbs-regime-regular-e-simples.md | 41–46 | 🔵 |
| ibs-cbs-nao-cumulatividade-creditos.md | 47–56 | 🟡 |
| ibs-cbs-uso-consumo-pessoal.md | 57 | 🟡 |
| ibs-cbs-cadastro-documento-fiscal.md | 58–62 | 🟡 |

## 2. Comércio exterior — arts. 63–111 (5 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| ibs-cbs-importacao.md | 63–78 | 🟡 |
| ibs-cbs-exportacao.md | 79–83 | 🟡 (81-A novo) |
| regimes-aduaneiros-especiais.md | 84–98-B | 🟡 (Seção VIII nova) |
| zonas-processamento-exportacao.md | 99–104 | 🔵 |
| regimes-bens-de-capital.md | 105–111 | 🟡 |

## 3. Cashback e cesta básica — arts. 112–125 (2 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| cashback-devolucao-pessoas-fisicas.md | 112–124 | 🔵 |
| cesta-basica-nacional.md | 125 + Anexo I | 🔵 |

## 4. Regimes diferenciados — arts. 126–171 (10 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| regimes-diferenciados-visao-geral.md | 126 | 🟡 |
| reducao-30-profissoes-regulamentadas.md | 127 | 🔵 |
| reducao-60-educacao-saude-dispositivos.md | 128–134 + Anexos II–V | 🔵 |
| reducao-60-alimentos-higiene-agro.md | 135–138 + Anexos VII, IX | 🔵 |
| reducao-60-cultura-esporte-seguranca.md | 139–142 + Anexos X, XI | 🟡 |
| aliquota-zero.md | 143–156 + Anexos XII, XIII, XV | 🟡 |
| transporte-publico-coletivo.md | 157 | 🔵 |
| reabilitacao-urbana.md | 158–163 | 🔵 |
| produtor-rural-e-integrado.md | 164–168 | 🟡 |
| transportador-autonomo-reciclagem-usados.md | 169–171 | 🔵 |

## 5. Regimes específicos — arts. 172–316 (11 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| regime-especifico-combustiveis.md | 172–180 | 🟡 (172, 174; + art. 179 da 227) |
| regime-especifico-servicos-financeiros.md | 181–233 | 🟡 |
| regime-especifico-planos-saude.md | 234–243 | 🟡 |
| regime-especifico-concursos-prognosticos.md | 244–250 | 🔵 |
| regime-especifico-bens-imoveis.md | 251–270 | 🟡 |
| regime-especifico-cooperativas.md | 271–272 | 🔵 |
| regime-especifico-bares-hotelaria-turismo.md | 273–291 | 🔵 |
| regime-especifico-saf.md | 292–296 | 🟡 |
| regime-especifico-missoes-diplomaticas.md | 297–299 | 🔵 |
| regimes-especificos-disposicoes-comuns.md | 300–307 | 🔵 |
| regimes-diferenciados-cbs-prouni-automotivo.md | 308–316 | 🔵 |

## 6. Administração, contencioso e penalidades — arts. 317–341-H (5 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| regulamento-competencia-normativa.md | 317 | 🔵 |
| harmonizacao-e-consulta-tributaria.md | 318–323-F | 🟡 (323-A a 323-F novos) |
| contencioso-integrado-ibs-cbs.md | 323-G a 323-M | 🟢 |
| fiscalizacao-lancamento-oficio.md | 324–341 | 🟡 |
| infracoes-penalidades-ibs-cbs.md | 341-A a 341-H | 🟢 |

## 7. Transição para IBS/CBS — arts. 342–408 (5 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| transicao-fixacao-aliquotas.md | 342–370 | 🟡 |
| transicao-compras-gov-e-contratos.md | 371–377 | 🔵 |
| transicao-saldo-credor-pis-cofins.md | 378–383 | 🔵 |
| compensacao-beneficios-fiscais-icms.md | 384–405 | 🟡 |
| transicao-bens-de-capital.md | 406–408 | 🔵 |

## 8. Imposto Seletivo — arts. 409–438 (4 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| is-conceitos-incidencia.md | 409–413 | 🔵 |
| is-base-calculo-aliquotas.md | 414–423 + Anexo XVII | 🟡 |
| is-sujeicao-passiva-apuracao.md | 424–433 | 🟡 |
| is-importacao-e-finais.md | 434–438 | 🟡 |

## 9. Demais disposições LC 214 — arts. 439–544 (11 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| zona-franca-manaus-e-alc.md | 439–468 | 🟡 |
| devolucao-turista-estrangeiro.md | 469–471 | 🔵 |
| pnct-conformidade-tributaria.md | 471-A a 471-C | 🟢 |
| penalidades-nao-tributarias-split.md | 471-D a 471-F | 🟢 |
| compras-governamentais.md | 472–473 | 🟡 |
| avaliacao-quinquenal-e-compensacoes.md | 474–479 | 🟡 |
| cgibs-na-lc214.md | 480–484 | 🟡 (+ art. 180 da 227: §5º-A do art. 481) |
| transicao-operacoes-bens-imoveis.md | 485–490 | 🟡 |
| lc214-alteracoes-outras-leis.md | 491–515, 521–541 | 🔵 |
| simples-nacional-e-mei.md | LC 214: 516–520 + Anexos XVIII–XXIII · LC 227: 168, 169, 181-IV | 🟡 |
| lc214-revogacoes-vigencia.md | 542–544 | 🟡 |

## 10. CGIBS, processo e ITCMD — LC 227 arts. 1–164 (17 notas)

| Arquivo | Arts. | Origem |
|---|---|---|
| cgibs-natureza-competencias.md | 1–20 | 🟢 |
| cgibs-estrutura-organizacional.md | 21–39 | 🟢 |
| cgibs-controle-transparencia.md | 40–44 | 🟢 |
| cgibs-orcamento-financiamento.md | 45–53 | 🟢 |
| pat-ibs-normas-processuais.md | 54–66 | 🟢 |
| pat-ibs-contencioso.md | 67–74 | 🟢 |
| pat-ibs-recursos.md | 75–87 | 🟢 |
| pat-ibs-orgaos-julgamento.md | 88–102 | 🟢 |
| ibs-distribuicao-receita-base.md | 103–113 | 🟢 |
| ibs-distribuicao-transicao.md | 114–116 | 🟢 |
| ibs-distribuicao-complementar.md | 117 | 🟢 |
| ibs-destinacao-vinculacoes.md | 118–131 | 🟢 |
| icms-saldo-credor-transicao.md | 132–141 | 🟢 |
| icms-st-estoque-2032.md | 142–145 | 🟢 |
| itcmd-conceitos-fato-gerador.md | 146–150 | 🟢 |
| itcmd-base-aliquota-contribuintes.md | 151–158 | 🟢 |
| itcmd-competencia-fiscalizacao.md | 159–164 | 🟢 |

## 11. Legislação correlata — LC 227 arts. 165–182 (1 nota)

lc227-alteracoes-legislacao-correlata.md 🟢 — seções internas:

| Seção | Art. 227 | Lei alterada |
|---|---|---|
| ITBI — fato gerador e valor venal | 165 | CTN arts. 35, 35-A (vetado), 38, 41 |
| COSIP/CIP — iluminação e monitoramento | 165 | CTN, Título V-A, art. 82-A |
| Cota-parte do ICMS | 166 | LC 63/1990, arts. 3º e 5º |
| Imposto Seletivo na base do ICMS | 167 | LC 87/1996 (Kandir), art. 13 §1º III |
| Vinculação de saúde | 170 | LC 141/2012 |
| Fundeb | 171 | Lei 14.113/2020, art. 3º, X |
| Crimes de responsabilidade | 172 | Lei 1.079/1950, Parte Quinta |
| Processo administrativo fiscal federal | 173 | Decreto 70.235/1972 |
| Compensação de ofício | 175 | Lei 9.430/1996, art. 81, VIII |
| Legislação aduaneira | 176 | DL 37/1966 |
| AFRMM | 177 | Lei 10.893/2004 |
| Combustíveis monofásicos | 178 | LC 192/2022, art. 2º |
| Revogações e vigência | 181, 182 | — |

NÃO entram aqui (regra do ajuste 4): art. 174 (distribuído nas 39 notas 🟡), arts. 168/169/181-IV (foram para simples-nacional-e-mei.md), art. 179 (foi para regime-especifico-combustiveis.md), art. 180 (foi para cgibs-na-lc214.md).

---

## Contagem final

26 🔵 + 39 🟡 + 22 🟢 = 87 notas

## Ordem de criação sugerida

1. notas/INDEX.md
2. Grupos 1–2 (núcleo + comércio exterior) — 21 notas
3. Grupos 3–5 (cashback, regimes diferenciados, regimes específicos) — 23 notas
4. Grupos 6–9 (administração, transição, IS, demais disposições LC 214) — 25 notas
5. Grupos 10–11 (CGIBS/processo/ITCMD + legislação correlata) — 18 notas
