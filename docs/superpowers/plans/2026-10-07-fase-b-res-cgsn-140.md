# Fase B — Res. CGSN 140 no domínio simples-nacional — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Incorporar a Resolução CGSN 140/2018 (visão multivigente da Receita, já com as Res. CGSN 190 e 191) às notas `sn-*`, com mapa de vigência gerado e notas novas para a matéria que não está na LC 123.

**Architecture:** Um leitor novo (`scripts/vigencia_receita.py`) transforma o texto da visão multivigente em blocos (dispositivo + marcas com data) e gera `_mapa-vigencia-res140.md`. As notas `sn-*` recebem a seção "Regulamentação (Res. CGSN 140)" e blocos ⏳ com o texto das Res. 190/191; matérias sem correspondente na LC viram notas novas.

**Tech Stack:** Python 3.14 stdlib + unittest; pdftotext; Markdown; claude -p para perguntas-teste.

**Spec:** `docs/superpowers/specs/2026-10-07-fase-b-cgsn-140-e-documentos-fiscais-design.md` (seção 2 e 4)

## Global Constraints

- Lei prevalece: cada seção de regulamentação vem **depois** da regra da LC; divergência → `> ⚠️ Conflito LC × Resolução: ...`.
- Datas de vigência da Res. 140 vêm **só** das marcas do portal (`date_range`, "Vide modificação prevista para", "Vide dispositivo a ser incluído em") e do art. 9º da Res. 190 / art. 3º da Res. 191. O texto futuro vem das Res. 190/191 (`fontes/simples-nacional/texto/resolucao-cgsn-19x-2026.txt`; na 190, só a 1ª ocorrência dos arts. 1º a 6º).
- Redações repetidas do mesmo dispositivo: vale a última com marca de data passada; versões sem marca antes dela são superadas.
- Anexos da Res. 140 não estão no PDF (são arquivos separados): Anexos VI, VII e XI são **lacuna** explícita; Anexos I–V de 2027–2028 = Res. 190 (DOU).
- Frontmatter das notas alteradas: `fontes` passa a citar a Res. CGSN 140 (e 190/191 quando usadas); `texto-base: 2026-10-07`.
- Toda nota alterada ou criada: `conferir_numeros.py` com fontes LC 123 HTML + LC 214 HTML + LC 227 HTML + `resolucao-cgsn-140-2018.txt` + Res. 190/191 txt → 0 faltantes; `verificar.py` → 0 erros.
- Commits terminam com `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`; branch `feat/fase-b-cgsn140-docfiscais`.

## Review Focus

1. **Marca associada ao dispositivo errado** quando a marca quebra em duas linhas ou cai depois de ruído de página. Teste na Task 1: `test_marca_quebrada_em_duas_linhas_e_ruido_no_meio`.
2. **Redação superada copiada como vigente** (versão antiga sem marca antes da nova). Teste na Task 1: `test_versao_anterior_fica_sem_marcas`.
3. **"Vide modificação prevista" tratada como vigente.** Teste na Task 1: `test_situacao_modificacao_prevista_futura`.
4. **Regra da resolução contrariando a lei sem aviso** — conferência manual na redação (Tasks 4–8) com o bloco ⚠️.
5. **Anexo da Res. 140 citado como se o conteúdo estivesse nas notas** — perguntas-teste da Task 9 (S17).

---

## Mapa de propriedade: artigos da Res. 140 → nota

| Arts. Res. 140 | Matéria | Nota |
|---|---|---|
| 1º–3º | definições, receita bruta, limites | sn-conceitos-definicao-me-epp |
| 4º–9º, 13–14, 145 | tributos abrangidos, opção, resultado do pedido, isenção de IR | sn-abrangencia-tributos |
| 10–12, 24 | sublimites, ultrapassagem | sn-sublimites-icms-iss |
| 15 | vedações | sn-vedacoes-ingresso |
| 16–23, 31–37, 77–78, 146–147 | base de cálculo, alíquotas, isenção/valor fixo de ICMS/ISS, regime de caixa, valores diferidos, CPP não incluída | sn-calculo-aliquota-efetiva |
| 25–30 | segregação, retenção e ST, imunidade | sn-segregacao-receitas |
| 26 (Fator R, se aí estiver) | Fator R | sn-fator-r |
| 38–45 (+ Seções IV-A e V-A da Res. 190) | aplicativos, prazos, arrecadação, repasse | sn-recolhimento-das (repasse → sn-repasse-arrecadacao) |
| 46–57 | parcelamento | **nova** sn-parcelamento |
| 58 | créditos | sn-creditos |
| 59–71, 79–80 | documentos e livros fiscais, NFS-e (Res. 191), certificação | sn-obrigacoes-acessorias |
| 72–76 | declarações (PGDAS-D, DEFIS) | **nova** sn-declaracoes-pgdas-defis |
| 81–84 | exclusão | sn-exclusao |
| 85–92 | fiscalização, autuação, omissão | sn-fiscalizacao-omissao-receita |
| 93–99 | infrações e penalidades | sn-acrescimos-penalidades |
| 100–120 | MEI (Título II) | **nova** sn-mei-regulamentacao (sn-mei recebe resumo e link) |
| 121–141 | contencioso, consulta, restituição e compensação, processos judiciais | sn-processo-administrativo-judicial (restituição/compensação → sn-recolhimento-das) |
| 141-A–141-G | transação | **nova** sn-transacao |
| 142–153 | transitórias e finais | sn-disposicoes-finais |

Anexos I–V (2027–2028, Res. 190): cada `sn-anexo-*` recebe um bloco curto apontando a Res. 190 (as tabelas da LC 214 já estão nas notas; a Res. 190 é conferida contra elas e divergências viram ⚠️). Anexo XIII (MEI 2027–2028, Res. 190) → sn-mei-regulamentacao.

---

### Task 1: `scripts/vigencia_receita.py`

**Files:** Create `scripts/vigencia_receita.py`, `scripts/tests/test_vigencia_receita.py`

**Interfaces:**
- Produces: `RUIDO_PADRAO: list[str]`; `@dataclass Marca(tipo: str, ato: str, data: str)` (tipo ∈ `redacao|inclusao|revogacao|modificacao-prevista|inclusao-prevista|vide|outro`; ato `"Res. CGSN 190/2026"` ou `""`; data ISO ou `""`); `@dataclass Bloco(artigo: str, dispositivo: str, texto: str, marcas: list[Marca])`; `blocos(texto: str, ruido: list[str]) -> list[Bloco]`; `situacao(marca: Marca, data_base: str) -> str`; `gerar_markdown(nome: str, blocos: list[Bloco], data_base: str, desde: str) -> str`; CLI `vigencia_receita.py <txt> --data-base AAAA-MM-DD [--desde AAAA-MM-DD] [--ruido R]... [--cabecalho md] [--saida md]`.

- [ ] **Step 1: Testes que falham** — `scripts/tests/test_vigencia_receita.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import vigencia_receita as vr  # noqa: E402

TEXTO = """07/10/2026, 09:29
Resol. CGSN nº 140-2018
Art. 2º Para fins desta Resolução, considera-se:
IV - empresa em início de atividade aquela que se encontra no período de 180 dias;
IV - empresa em início de atividade aquela que se encontra no período de 60
import_export
(sessenta) dias a partir da data de abertura;
[Redação dada pelo(a) Resolução CGSN nº 150, de 3 de dezembro de
https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/imprimir/92278/visao/multivigente
3/132
2019] date_range 01/01/2020
[Vide modificação prevista para 01/01/2027, nos termos do(a) Resolução CGSN nº 190, de 4 de agosto de 2026]
V - data de início de atividade a data de abertura constante do CNPJ.
[Vide dispositivo a ser incluído em 01/01/2027, nos termos do(a) Resolução CGSN nº 190, de 4 de agosto de 2026]
file_present Anexo I .pdf
Art. 3º Texto do artigo.
§ 1º Parágrafo revogado.
[Revogado(a) pelo(a) Resolução CGSN nº 183, de 26 de setembro de 2025] date_range 13/10/2025
"""


class TestVigenciaReceita(unittest.TestCase):
    def setUp(self):
        self.bs = vr.blocos(TEXTO, vr.RUIDO_PADRAO)
        self.por = {}
        for b in self.bs:
            self.por.setdefault((b.artigo, b.dispositivo), []).append(b)

    def test_remove_ruido(self):
        tudo = " ".join(b.texto for b in self.bs)
        for lixo in ("import_export", "3/132", "normasinternet2", "file_present", "09:29"):
            self.assertNotIn(lixo, tudo)

    def test_versao_anterior_fica_sem_marcas(self):
        v1, v2 = self.por[("2", "IV-")]
        self.assertEqual(v1.marcas, [])
        self.assertIn("180 dias", v1.texto)

    def test_continuacao_de_linha_vai_para_o_mesmo_bloco(self):
        self.assertIn("(sessenta) dias a partir da data de abertura", self.por[("2", "IV-")][1].texto)

    def test_marca_quebrada_em_duas_linhas_e_ruido_no_meio(self):
        m = self.por[("2", "IV-")][1].marcas[0]
        self.assertEqual((m.tipo, m.ato, m.data), ("redacao", "Res. CGSN 150/2019", "2020-01-01"))

    def test_modificacao_prevista(self):
        m = self.por[("2", "IV-")][1].marcas[1]
        self.assertEqual((m.tipo, m.ato, m.data), ("modificacao-prevista", "Res. CGSN 190/2026", "2027-01-01"))

    def test_inclusao_prevista(self):
        m = self.por[("2", "V-")][0].marcas[0]
        self.assertEqual((m.tipo, m.data), ("inclusao-prevista", "2027-01-01"))

    def test_revogacao_com_date_range(self):
        m = self.por[("3", "§1º")][0].marcas[0]
        self.assertEqual((m.tipo, m.ato, m.data), ("revogacao", "Res. CGSN 183/2025", "2025-10-13"))

    def test_situacao_modificacao_prevista_futura(self):
        m = vr.Marca("modificacao-prevista", "Res. CGSN 190/2026", "2027-01-01")
        self.assertEqual(vr.situacao(m, "2026-10-07"), "⏳ modificação prevista — a redação atual vale até lá")

    def test_situacao_redacao_passada(self):
        self.assertEqual(vr.situacao(vr.Marca("redacao", "Res. CGSN 150/2019", "2020-01-01"), "2026-10-07"), "vigente")

    def test_situacao_revogacao_passada(self):
        self.assertEqual(vr.situacao(vr.Marca("revogacao", "Res. CGSN 183/2025", "2025-10-13"), "2026-10-07"), "revogado")

    def test_markdown_filtra_por_data_e_mostra_futuras(self):
        md = vr.gerar_markdown("r140.txt", self.bs, "2026-10-07", "2025-01-01")
        self.assertIn("| 2 | IV- | modificacao-prevista | Res. CGSN 190/2026 | 01/01/2027 | ⏳ modificação prevista — a redação atual vale até lá |", md)
        self.assertIn("| 3 | §1º | revogacao | Res. CGSN 183/2025 | 13/10/2025 | revogado |", md)
        self.assertNotIn("Res. CGSN 150/2019", md)


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2:** `python -m unittest discover -s scripts/tests` → `ModuleNotFoundError: vigencia_receita`; os 77 anteriores OK.

- [ ] **Step 3: Implementar** — `scripts/vigencia_receita.py`:

```python
"""Mapa de vigência a partir da visão multivigente do portal Normas da Receita.

Uso:
  python scripts/vigencia_receita.py <texto.txt> --data-base AAAA-MM-DD [--desde AAAA-MM-DD]
      [--ruido REGEX ...] [--cabecalho cabecalho.md] [--saida mapa.md]

O texto vem de `pdftotext -enc UTF-8` da impressão "Visão Multivigente". Cada
dispositivo é seguido das suas marcas entre colchetes, como
"[Redação dada pelo(a) Resolução CGSN nº N, de ...] date_range DD/MM/AAAA" ou
"[Vide modificação prevista para DD/MM/AAAA, nos termos do(a) ...]".
O texto futuro NÃO aparece: ele está no ato alterador.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from esqueleto import ANEXO, ARTIGO, DISPOSITIVO, TITULO, normalizar_rotulo  # noqa: E402

RUIDO_PADRAO = [
    r"^\d{2}/\d{2}/\d{4}, \d{2}:\d{2}$",
    r"^\d+/\d+$",
    r"^https?://\S+$",
    r"^(import_export\s*)+$",
    r"^file_present\b.*$",
    r"^Resol\. CGSN nº \d+-\d{4}$",
    r"^NORMAS$",
    r"^Visão Multivigente$",
]
MARCA = re.compile(r"\[([^\]]*)\](?:\s*date_range\s*(\d{2}/\d{2}/\d{4}))?")
TIPOS = [
    ("modificacao-prevista", re.compile(r"^Vide modificação prevista para (\d{2}/\d{2}/\d{4})")),
    ("inclusao-prevista", re.compile(r"^Vide dispositivo a ser incluído em (\d{2}/\d{2}/\d{4})")),
    ("redacao", re.compile(r"^Redação dada")),
    ("inclusao", re.compile(r"^Incluíd")),
    ("revogacao", re.compile(r"^Revogad")),
    ("vide", re.compile(r"^Vide ")),
]
ATO = re.compile(r"Resolução CGSN nº (\d+), de \d+ de \w+ de (\d{4})")


@dataclass
class Marca:
    tipo: str
    ato: str
    data: str


@dataclass
class Bloco:
    artigo: str
    dispositivo: str
    texto: str
    marcas: list[Marca] = field(default_factory=list)


def _iso(br: str) -> str:
    dia, mes, ano = br.split("/")
    return f"{ano}-{mes}-{dia}"


def _br(iso: str) -> str:
    ano, mes, dia = iso.split("-")
    return f"{dia}/{mes}/{ano}"


def _marca(conteudo: str, date_range: str | None) -> Marca:
    conteudo = re.sub(r"\s+", " ", conteudo).strip()
    tipo, data = "outro", ""
    for nome, padrao in TIPOS:
        m = padrao.search(conteudo)
        if m:
            tipo = nome
            if m.groups():
                data = _iso(m.group(1))
            break
    if not data and date_range:
        data = _iso(date_range)
    a = ATO.search(conteudo)
    return Marca(tipo, f"Res. CGSN {a.group(1)}/{a.group(2)}" if a else "", data)


def blocos(texto: str, ruido: list[str]) -> list[Bloco]:
    padroes = [re.compile(p) for p in ruido]
    limpo = "\n".join(
        l.strip() for l in texto.splitlines()
        if l.strip() and not any(p.match(l.strip()) for p in padroes)
    )
    saida: list[Bloco] = []
    artigo, rotulo = "", ""
    pos = 0
    for m in list(MARCA.finditer(limpo)) + [None]:
        trecho = limpo[pos:m.start()] if m else limpo[pos:]
        for linha in trecho.splitlines():
            linha = linha.strip()
            if not linha:
                continue
            m_anexo, m_art = ANEXO.match(linha), ARTIGO.match(linha)
            m_disp = None if (m_anexo or m_art) else DISPOSITIVO.match(linha)
            if m_anexo:
                artigo, rotulo = f"Anexo {m_anexo.group(1).upper()}", "cabecalho"
            elif m_art:
                artigo = m_art.group(1) + (f"-{m_art.group(2)}" if m_art.group(2) else "")
                rotulo = "caput"
            elif m_disp:
                rotulo = normalizar_rotulo(m_disp.group(1))
            elif TITULO.match(linha) or not saida:
                saida.append(Bloco(artigo, "titulo", linha))
                continue
            else:
                saida[-1].texto += " " + linha
                continue
            saida.append(Bloco(artigo, rotulo, linha))
        if m is None:
            break
        if saida:
            saida[-1].marcas.append(_marca(m.group(1), m.group(2)))
        pos = m.end()
    return saida


def situacao(marca: Marca, data_base: str) -> str:
    futuro = marca.data > data_base
    if marca.tipo == "modificacao-prevista":
        return "⏳ modificação prevista — a redação atual vale até lá" if futuro else "modificação já em vigor"
    if marca.tipo == "inclusao-prevista":
        return "⏳ dispositivo novo a ser incluído" if futuro else "dispositivo já incluído"
    if marca.tipo == "revogacao":
        return "⏳ revogação futura" if futuro else "revogado"
    return "⏳ futura" if futuro else "vigente"


def gerar_markdown(nome: str, blocos_: list[Bloco], data_base: str, desde: str) -> str:
    linhas = [
        f"<!-- Tabela gerada por scripts/vigencia_receita.py a partir de {nome}. Não editar à mão. -->",
        "",
        f"## Marcas de vigência desde {_br(desde)} (e todas as futuras)",
        "",
        f"| Artigo | Dispositivo | Marca | Ato | Data | Situação em {_br(data_base)} |",
        "|---|---|---|---|---|---|",
    ]
    for b in blocos_:
        if not b.artigo or b.dispositivo == "titulo":
            continue
        for m in b.marcas:
            if m.tipo in ("vide", "outro") or not m.data:
                continue
            if m.data < desde and m.data <= data_base:
                continue
            linhas.append(f"| {b.artigo} | {b.dispositivo} | {m.tipo} | {m.ato} | {_br(m.data)} | {situacao(m, data_base)} |")
    return "\n".join(linhas) + "\n"


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("texto", type=Path)
    p.add_argument("--data-base", required=True)
    p.add_argument("--desde", default="2025-01-01")
    p.add_argument("--ruido", action="append", default=[])
    p.add_argument("--cabecalho", type=Path)
    p.add_argument("--saida", type=Path)
    a = p.parse_args(argv[1:])
    bs = blocos(a.texto.read_text(encoding="utf-8"), RUIDO_PADRAO + a.ruido)
    md = gerar_markdown(a.texto.name, bs, a.data_base, a.desde)
    if a.cabecalho:
        md = a.cabecalho.read_text(encoding="utf-8").rstrip("\n") + "\n\n" + md
    if a.saida:
        a.saida.write_text(md, encoding="utf-8", newline="\n")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(md, end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4:** `python -m unittest discover -s scripts/tests` → 88 testes OK.
- [ ] **Step 5:** Commit `feat: vigencia_receita.py lê a visão multivigente da Receita`.

### Task 2: Fonte, extração e mapa de vigência da Res. 140

**Files:** Move `fontes/simples-nacional/resolucao-cgsn-140-2018.pdf` → `resolucao-cgsn-140-2018-multivigente.pdf`; remove do git o PDF do DOU já apagado; Create `fontes/simples-nacional/texto/resolucao-cgsn-140-2018.txt`, `fontes/simples-nacional/texto/resolucao-cgsn-140-2018-mapa-cabecalho.md`, `notas/simples-nacional/_mapa-vigencia-res140.md`; Modify `fontes/simples-nacional/FONTE.md`.

- [ ] **Step 1:** `git mv`/`git rm` dos PDFs; `pdftotext -enc UTF-8` para o `.txt`.
- [ ] **Step 2:** Cabeçalho do mapa (frontmatter `título`, `dominio`, `texto-base: 2026-10-07`; como ler; cláusulas de vigência literais: Res. 190, art. 9º, e Res. 191, art. 3º; lacuna dos Anexos VI, VII, XI e demais em PDF separado).
- [ ] **Step 3:** Gerar: `python scripts/vigencia_receita.py fontes/simples-nacional/texto/resolucao-cgsn-140-2018.txt --data-base 2026-10-07 --cabecalho ... --saida notas/simples-nacional/_mapa-vigencia-res140.md`.
- [ ] **Step 4: Conferir completude:** nº de marcas "Vide modificação prevista" + "Vide dispositivo a ser incluído" no `.txt` (`tr '\n' ' ' | grep -o`) = nº de linhas `modificacao-prevista` + `inclusao-prevista` no mapa (as do cabeçalho de histórico, se houver, justificadas). Conferir 5 linhas por amostragem contra o texto.
- [ ] **Step 5:** FONTE.md: linha da Res. 140 multivigente (URL `https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/imprimir/92278/visao/multivigente`, capturada em 2026-10-07, última alteração vista: Res. CGSN 191/2026 e modificações previstas da 190) e remoção da linha do DOU. `verificar.py` → 0 erros. Commit.

### Task 3: Plano de notas da fase B

**Files:** Modify `notas/simples-nacional/_plano-notas.md` (status volta para `aprovado` enquanto houver notas novas por escrever; nova seção "Fase B — Res. CGSN 140" com o mapa de propriedade deste plano e as 4 notas novas: sn-parcelamento, sn-declaracoes-pgdas-defis, sn-mei-regulamentacao, sn-transacao).

- [ ] **Step 1:** Escrever a seção. **Step 2:** `verificar.py` → 0 erros e 4 avisos (notas novas ainda inexistentes). **Step 3:** Commit. (Aprovação delegada pelo usuário em 2026-10-07 — registrar como Ruling.)

### Tasks 4 a 8: Integração nas notas existentes (procedimento comum)

Para cada nota do grupo:

1. Recortar os artigos da Res. 140 do `.txt` (`awk '/^Art\. N[º.]/,/^Art\. M[º.]/'`), descartando versões superadas (regra das Global Constraints).
2. Ler no mapa `_mapa-vigencia-res140.md` as linhas desses artigos; para cada `⏳`, buscar o texto novo na Res. 190 (1ª ocorrência dos arts. 1º–6º) ou 191.
3. Acrescentar antes de `## Ligações`:

```markdown
## Regulamentação (Res. CGSN 140/2018)

<regras operacionais, cada uma com (Res. 140, art. N, §, inciso)>

## ⏳ A partir de 01/01/2027 — Res. CGSN 190/2026 (art. N; Res. 140, art. M)

<o que muda, literal>
```

4. `conferir_numeros.py` (fontes das Global Constraints) → 0 faltantes; `verificar.py` → 0 erros.

- **Task 4:** sn-conceitos-definicao-me-epp, sn-abrangencia-tributos, sn-sublimites-icms-iss, sn-vedacoes-ingresso.
- **Task 5:** sn-calculo-aliquota-efetiva, sn-segregacao-receitas, sn-fator-r, sn-anexo-i a v (bloco curto + conferência Res. 190 × LC 214).
- **Task 6:** sn-recolhimento-das, sn-repasse-arrecadacao, sn-creditos, sn-obrigacoes-acessorias.
- **Task 7:** sn-exclusao, sn-fiscalizacao-omissao-receita, sn-acrescimos-penalidades, sn-processo-administrativo-judicial, sn-disposicoes-finais, sn-mei (resumo + link).
- **Task 8:** notas novas sn-parcelamento, sn-declaracoes-pgdas-defis, sn-mei-regulamentacao (inclui Anexo XIII da Res. 190 — valores fixos do MEI 2027–2028, conferidos contra o Anexo VII da LC 214), sn-transacao; plano → `status: concluido`.

Cada task termina com commit `feat(simples-nacional): Res. CGSN 140 em <grupo>`.

### Task 9: Ligações, protocolo e perguntas-teste

**Files:** Modify `notas/simples-nacional/INDEX.md` (notas novas e link do mapa da Res. 140), `notas/INDEX.md`, `CLAUDE.md` (status: "fase B concluída"), `MEMORY.md`, `docs/procedimento-nova-legislacao.md` (seção "Fontes da Receita — visão multivigente" com o comando do `vigencia_receita.py`), `docs/perguntas-teste/simples-nacional.md` (S15–S19).

- [ ] **Step 1:** Atualizações acima; `verificar.py` → 0 erros, 0 avisos.
- [ ] **Step 2:** Perguntas novas: S15 um detalhe operacional da Res. 140 (ex.: prazo de pagamento do DAS, art. 40); S16 uma mudança de 2027 da Res. 190; S17 lacuna de Anexo (ex.: "quais CNAEs são impeditivos?") — deve dizer que o Anexo VI não está nas fontes; S18 parcelamento; S19 conflito/hierarquia (se houver ⚠️ registrado; senão, transação).
- [ ] **Step 3:** Rodar S1–S19 e R1–R5 com `claude -p` (3 em paralelo); todos citam a nota esperada e o comportamento confere.
- [ ] **Step 4:** Commit.
