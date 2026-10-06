# Simples Nacional — fase A2 (redação das notas da LC 123) — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Escrever as 28 notas `sn-*` do plano aprovado (`notas/simples-nacional/_plano-notas.md`), ligá-las ao restante do second brain e validar o domínio com perguntas-teste, deixando o Simples Nacional pronto para uso.

**Architecture:** Duas ferramentas novas em Python stdlib dão precisão à redação. `ler_lei.py` lineariza o HTML do Planalto (parágrafos e linhas de tabela na ordem do documento, com `[RISCADO]`) e recorta trechos. `conferir_numeros.py` confere se todo percentual e valor em R$ citado numa nota existe nas fontes. Cada nota é escrita a partir do texto literal recortado, do `_mapa-vigencia.md` e das cláusulas de vigência, e passa pelo `verificar.py` e pelo `conferir_numeros.py`.

**Tech Stack:** Markdown, Python 3.14 (stdlib + unittest), git, `claude -p` para as perguntas-teste.

**Spec:** `docs/superpowers/specs/2026-10-06-expansao-multi-legislacao-design.md` (seções 2.3, 2.4, 3 — etapas 5 a 7, 4.1–4.4 e 6)

## Global Constraints

- Python **só biblioteca padrão**; testes com `python -m unittest discover -s scripts/tests`.
- Frontmatter obrigatório em toda nota `sn-*`: `título`, `dominio: simples-nacional`, `fontes`, `vigencia` (`atual` | `com-mudanca-programada`, **igual à coluna do plano**), `texto-base: 2026-10-06`.
- Corpo principal = regra **vigente em 2026-10-06**. Redação futura em `## ⏳ A partir de DD/MM/AAAA — redação dada pela <lei> (art. N)`; revogação programada em `## ❌ Revogado a partir de DD/MM/AAAA — <lei> (art. N)`.
- Datas vêm **só** do `_mapa-vigencia.md` / cláusulas literais (LC 214, art. 544; LC 227, arts. 181–182; Res. CGSN 190, art. 9º; Res. CGSN 191, art. 3º).
- Conteúdo **só** do texto literal das fontes (`fontes/simples-nacional/texto/`, `fontes/reforma/texto/`). Nada de conhecimento geral. Lacuna é dita como lacuna.
- Estilo do usuário: didático, lógica antes do detalhe, analogias; **fórmulas sempre completas**; artigos citados em cada afirmação.
- Tabelas numéricas transcritas **literalmente** e conferidas por `conferir_numeros.py` (0 faltantes). Exemplos numéricos inventados ficam entre `<!-- exemplo -->` e `<!-- /exemplo -->`.
- Res. CGSN 140/190/191 = fase B: a nota pode **mencionar** que a resolução detalhará o ponto (coluna "Fase B" do plano), sem descrever conteúdo da 140 (PDF original não confiável). Res. 190/191: só datas e objeto, já registrados no mapa.
- Links entre notas: `[[nome]]`. Pontes obrigatórias: `[[simples-nacional-e-mei]]` nas notas com tema IBS/CBS; notas da reforma citadas no plano.
- Commits terminam com `Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>`. Branch `feat/simples-nacional-fase-a2`.

## Review Focus

1. **Redação superada copiada como vigente**: ao recortar o texto, linhas `[RISCADO]` nunca entram no corpo da nota. Teste na Task 1: `test_marca_paragrafo_riscado`.
2. **Regra futura apresentada como atual**: toda linha ⏳ do mapa para os artigos da nota vira bloco ⏳ na nota. Verificação na Task 9, Step 2 (script de cruzamento mapa × notas).
3. **Erro de transcrição em faixa/percentual dos Anexos**: `conferir_numeros.py` com 0 faltantes. Teste na Task 1: `test_percentual_inexistente_na_fonte_e_reportado`.
4. **Tabelas da LC 214 por período (2027–2028, depois)** confundidas entre si: o recorte linear mantém a legenda antes de cada tabela. Teste na Task 1: `test_tabela_mantem_ordem_com_legenda`.
5. **Exemplo de cálculo com número inventado** acusado como erro, ou número da lei escondido dentro de exemplo: o bloco `<!-- exemplo -->` é ignorado só ali. Teste na Task 1: `test_ignora_numeros_dentro_de_exemplo`.

---

## Mapa de arquivos

| Arquivo | Responsabilidade | Task |
|---|---|---|
| `scripts/ler_lei.py` + teste | Linearizar HTML do Planalto e recortar trechos | 1 |
| `scripts/conferir_numeros.py` + teste | Conferência de percentuais e valores em R$ | 1 |
| `fontes/reforma/texto/lc-214-2025-planalto.htm` | HTML compilado da LC 214 (Anexos XVIII–XXIII) | 1 |
| `notas/simples-nacional/sn-*.md` (28) | Conteúdo | 2–8 |
| `notas/simples-nacional/INDEX.md`, `notas/INDEX.md`, `notas/reforma/simples-nacional-e-mei.md` | Ligações | 9 |
| `notas/simples-nacional/_plano-notas.md` | `status: concluido` | 9 |
| `CLAUDE.md`, `MEMORY.md`, `fontes/reforma/FONTE.md` | Protocolo e status do domínio | 9 |
| `docs/perguntas-teste/simples-nacional.md` | Bateria do domínio | 9 |

---

### Task 1: Ferramentas de leitura e conferência

**Files:**
- Create: `scripts/ler_lei.py`, `scripts/tests/test_ler_lei.py`
- Create: `scripts/conferir_numeros.py`, `scripts/tests/test_conferir_numeros.py`
- Create (já baixado): `fontes/reforma/texto/lc-214-2025-planalto.htm`

**Interfaces:**
- Produces: `ler_lei.linearizar(html: str) -> list[str]` (uma linha por parágrafo ou por linha de tabela `| c1 | c2 |`; prefixo `[RISCADO] ` quando há `<strike` ou `line-through`); `ler_lei.recortar(linhas: list[str], inicio: str, fim: str | None, ocorrencia: int = -1) -> list[str]` (da linha que casa o regex `inicio` — escolhendo a ocorrência indicada — até antes da primeira linha seguinte que casa `fim`); CLI `python scripts/ler_lei.py <htm> --inicio REGEX [--fim REGEX] [--ocorrencia N]`.
- Produces: `conferir_numeros.numeros(texto: str) -> set[str]` (percentuais `4,00%`, `28%`; valores `180.000,00`; ignora blocos `<!-- exemplo -->…<!-- /exemplo -->`); `conferir_numeros.faltantes(nota: str, fontes: list[str]) -> list[str]`; CLI `python scripts/conferir_numeros.py <nota.md> --fontes <arq>...` (sai 1 se faltar algum).

- [ ] **Step 1: Testes que falham** — `scripts/tests/test_ler_lei.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ler_lei as ll  # noqa: E402

HTML = """
<p>Art. 18. O valor devido mensalmente.</p>
<p><strike>§ 1º Redação antiga.</strike></p>
<p>§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)</p>
<p>Art. 18-A. O MEI.</p>
<p>ANEXO I</p>
<p>Para os anos-calendário 2027 e 2028</p>
<table><tr><td>1ª Faixa</td><td>Até 180.000,00</td><td>4,00%</td></tr>
<tr><td style="text-decoration: line-through">2ª Faixa</td><td>x</td></tr></table>
<p>A partir de 2029</p>
<table><tr><td>1ª Faixa</td><td>Até 180.000,00</td><td>4,10%</td></tr></table>
<p>ANEXO II</p>
"""


class TestLerLei(unittest.TestCase):
    def setUp(self):
        self.linhas = ll.linearizar(HTML)

    def test_marca_paragrafo_riscado(self):
        self.assertIn("[RISCADO] § 1º Redação antiga.", self.linhas)
        self.assertIn("§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)", self.linhas)

    def test_tabela_vira_linhas_com_celulas(self):
        self.assertIn("| 1ª Faixa | Até 180.000,00 | 4,00% |", self.linhas)

    def test_linha_de_tabela_riscada_por_css(self):
        self.assertIn("[RISCADO] | 2ª Faixa | x |", self.linhas)

    def test_tabela_mantem_ordem_com_legenda(self):
        i = self.linhas.index("Para os anos-calendário 2027 e 2028")
        j = self.linhas.index("A partir de 2029")
        self.assertLess(i, self.linhas.index("| 1ª Faixa | Até 180.000,00 | 4,00% |"))
        self.assertLess(j, self.linhas.index("| 1ª Faixa | Até 180.000,00 | 4,10% |"))

    def test_recorta_artigo(self):
        trecho = ll.recortar(self.linhas, r"^Art\. 18\.", r"^Art\. 18-A\.")
        self.assertEqual(trecho[0], "Art. 18. O valor devido mensalmente.")
        self.assertEqual(len(trecho), 3)

    def test_recorta_anexo_ate_o_proximo(self):
        trecho = ll.recortar(self.linhas, r"^ANEXO I$", r"^ANEXO II$")
        self.assertEqual(trecho[-1], "| 1ª Faixa | Até 180.000,00 | 4,10% |")

    def test_recorta_ocorrencia_escolhida(self):
        self.assertEqual(ll.recortar(self.linhas, r"^§ 1º", None, ocorrencia=0)[0], "§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)")


if __name__ == "__main__":
    unittest.main()
```

`scripts/tests/test_conferir_numeros.py`:

```python
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import conferir_numeros as cn  # noqa: E402

FONTE = "| 1ª Faixa | Até 180.000,00 | 4,00% | - | fator r igual ou superior a 28% (vinte e oito por cento)"


class TestConferirNumeros(unittest.TestCase):
    def test_extrai_percentuais_e_valores(self):
        self.assertEqual(cn.numeros("alíquota de 4,00% até R$ 180.000,00 e 28%"), {"4,00%", "180.000,00", "28%"})

    def test_tudo_encontrado(self):
        self.assertEqual(cn.faltantes("Faixa 1: até R$ 180.000,00, alíquota 4,00%; Fator R 28%.", [FONTE]), [])

    def test_percentual_inexistente_na_fonte_e_reportado(self):
        self.assertEqual(cn.faltantes("alíquota 4,10%", [FONTE]), ["4,10%"])

    def test_ignora_numeros_dentro_de_exemplo(self):
        nota = "<!-- exemplo -->\nRBT12 = R$ 1.000.000,00, alíquota efetiva 8,77%\n<!-- /exemplo -->\nalíquota 4,00%"
        self.assertEqual(cn.faltantes(nota, [FONTE]), [])

    def test_ignora_frontmatter(self):
        self.assertEqual(cn.faltantes("---\ntexto-base: 2026-10-06\n---\nalíquota 4,00%", [FONTE]), [])


if __name__ == "__main__":
    unittest.main()
```

- [ ] **Step 2: Rodar e confirmar falha**

Run: `python -m unittest discover -s scripts/tests`
Expected: `ModuleNotFoundError` para `ler_lei` e `conferir_numeros`; os 62 testes antigos continuam `ok`.

- [ ] **Step 3: Implementar** `scripts/ler_lei.py`:

```python
"""Lineariza o HTML compilado do Planalto e recorta trechos.

Uso:
  python scripts/ler_lei.py <lei.htm> --inicio REGEX [--fim REGEX] [--ocorrencia N]

Cada parágrafo vira uma linha; cada linha de tabela vira "| c1 | c2 |".
Texto já superado (<strike> ou line-through) recebe o prefixo "[RISCADO] ".
"""
from __future__ import annotations

import argparse
import html as html_lib
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from vigencia_planalto import paragrafos_html  # noqa: E402

TABELA = re.compile(r"<table\b.*?</table>", re.S | re.I)
LINHA = re.compile(r"<tr\b.*?</tr>", re.S | re.I)
CELULA = re.compile(r"<t[dh]\b.*?</t[dh]>", re.S | re.I)
TAG = re.compile(r"<[^>]+>")


def _texto(fragmento: str) -> str:
    return re.sub(r"\s+", " ", html_lib.unescape(TAG.sub("", fragmento))).strip()


def _riscado(fragmento: str) -> bool:
    baixo = fragmento.lower()
    return "<strike" in baixo or "line-through" in baixo


def linearizar(html: str) -> list[str]:
    linhas: list[str] = []
    pos = 0
    for tabela in TABELA.finditer(html):
        linhas += [("[RISCADO] " if r else "") + t for t, r, _ in paragrafos_html(html[pos:tabela.start()]) if t]
        for tr in LINHA.findall(tabela.group(0)):
            celulas = [_texto(c) for c in CELULA.findall(tr)]
            if any(celulas):
                linhas.append(("[RISCADO] " if _riscado(tr) else "") + "| " + " | ".join(celulas) + " |")
        pos = tabela.end()
    linhas += [("[RISCADO] " if r else "") + t for t, r, _ in paragrafos_html(html[pos:]) if t]
    return linhas


def recortar(linhas: list[str], inicio: str, fim: str | None, ocorrencia: int = -1) -> list[str]:
    ini = re.compile(inicio)
    posicoes = [i for i, l in enumerate(linhas) if ini.search(l)]
    if not posicoes:
        return []
    a = posicoes[ocorrencia]
    if fim is None:
        return linhas[a:]
    fim_re = re.compile(fim)
    b = next((i for i in range(a + 1, len(linhas)) if fim_re.search(linhas[i])), len(linhas))
    return linhas[a:b]


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("html", type=Path)
    parser.add_argument("--inicio", required=True)
    parser.add_argument("--fim")
    parser.add_argument("--ocorrencia", type=int, default=-1)
    args = parser.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    linhas = linearizar(args.html.read_text(encoding="utf-8"))
    print("\n".join(recortar(linhas, args.inicio, args.fim, args.ocorrencia)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

`scripts/conferir_numeros.py`:

```python
"""Confere se todo percentual e valor em R$ de uma nota existe nas fontes.

Uso: python scripts/conferir_numeros.py <nota.md> --fontes <arquivo> [<arquivo> ...]
Ignora o frontmatter e blocos <!-- exemplo --> ... <!-- /exemplo -->.
Sai com código 1 se algum número da nota não aparecer nas fontes.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

PERCENTUAL = re.compile(r"(?<![\d.,])\d+(?:,\d+)?%")
VALOR = re.compile(r"(?<![\d.,])\d{1,3}(?:\.\d{3})+,\d{2}(?![\d%])")
EXEMPLO = re.compile(r"<!--\s*exemplo\s*-->.*?<!--\s*/exemplo\s*-->", re.S)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def numeros(texto: str) -> set[str]:
    texto = EXEMPLO.sub("", FRONTMATTER.sub("", texto))
    return set(PERCENTUAL.findall(texto)) | set(VALOR.findall(texto))


def faltantes(nota: str, fontes: list[str]) -> list[str]:
    disponiveis: set[str] = set()
    for f in fontes:
        disponiveis |= numeros(f)
    return sorted(numeros(nota) - disponiveis)


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("nota", type=Path)
    parser.add_argument("--fontes", type=Path, nargs="+", required=True)
    args = parser.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    falta = faltantes(args.nota.read_text(encoding="utf-8"),
                      [f.read_text(encoding="utf-8") for f in args.fontes])
    for n in falta:
        print(f"FALTA NAS FONTES  {n}")
    print(f"{len(falta)} número(s) sem correspondência em {args.nota.name}")
    return 1 if falta else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
```

- [ ] **Step 4: Rodar e confirmar que passa**

Run: `python -m unittest discover -s scripts/tests`
Expected: 74 testes (62 + 7 + 5), todos `OK`.

- [ ] **Step 5: Gerar os textos lineares de trabalho** (rascunho, fora do repositório)

```bash
S="$SCRATCHPAD/linear"; mkdir -p "$S"
python -I -c "import sys; sys.path.insert(0,'scripts'); import ler_lei as l; sys.stdout.reconfigure(encoding='utf-8'); print('\n'.join(l.linearizar(open(sys.argv[1],encoding='utf-8').read())))" fontes/simples-nacional/texto/lc-123-2006-planalto.htm > "$S/lc123.txt"
python -I -c "...mesmo comando..." fontes/reforma/texto/lc-214-2025-planalto.htm > "$S/lc214.txt"
python -I -c "...mesmo comando..." fontes/reforma/texto/lc-227-2026-planalto.htm > "$S/lc227.txt"
grep -c "^\[RISCADO\]" "$S/lc123.txt"
```
Expected: os três arquivos existem; `lc123.txt` tem linhas `[RISCADO]` (> 0).

- [ ] **Step 6: Commit**

```bash
git add scripts fontes/reforma/texto/lc-214-2025-planalto.htm notas/simples-nacional/_plano-notas.md docs/superpowers/plans
git commit -m "feat: ler_lei.py e conferir_numeros.py para a redação das notas

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>"
```

---

### Procedimento comum de redação (Tasks 2 a 8)

Para **cada** nota da task:

1. Recortar o texto literal: `python scripts/ler_lei.py fontes/simples-nacional/texto/lc-123-2006-planalto.htm --inicio "^Art\. N" --fim "^Art\. M"` (ou o linear do Step 5). Ler **tudo**, ignorando `[RISCADO]` para o corpo.
2. Consultar as linhas do `_mapa-vigencia.md` dos artigos da nota (`grep "^| N |"`) e as lacunas do cabeçalho (LC 227, art. 169; revogações com data própria).
3. Escrever a nota no formato:

```markdown
---
título: <título>
dominio: simples-nacional
fontes: LC 123/2006, arts. <faixa>[; LC 214/2025, art. <n>; LC 227/2026, art. <n>]
vigencia: <igual à coluna do plano>
texto-base: 2026-10-06
---

# <título>

## A lógica em uma frase
<o porquê da regra, com analogia quando ajudar>

## <seções temáticas com a regra vigente, cada afirmação com (art. X, §Y, inciso Z)>

## ⏳ A partir de DD/MM/AAAA — redação dada pela <lei> (art. N)
<o que muda, citando o texto literal da lei alteradora>

## Ligações
- [[nota-relacionada]] — por quê
```

4. Verificar: `python scripts/verificar.py` (0 erros) e `python scripts/conferir_numeros.py <nota> --fontes fontes/simples-nacional/texto/lc-123-2006-planalto.htm fontes/reforma/texto/lc-214-2025-planalto.htm fontes/reforma/texto/lc-227-2026-planalto.htm` → `0 número(s) sem correspondência`.

### Task 2: Capítulos I a III e abrangência (5 notas)

**Files:** Create `notas/simples-nacional/sn-conceitos-definicao-me-epp.md` (arts. 1–3-B), `sn-inscricao-baixa.md` (4–11), `sn-abrangencia-tributos.md` (12–16), `sn-vedacoes-ingresso.md` (17), `sn-calculo-aliquota-efetiva.md` (18: caput, §§1º–3º, §§15–16 e regras de cálculo).

- [ ] **Step 1:** Redigir as 5 notas pelo procedimento comum. Em `sn-calculo-aliquota-efetiva.md`, a fórmula do §1º-A do art. 18 é escrita por completo, com cada variável explicada e um exemplo numérico entre `<!-- exemplo -->`.
- [ ] **Step 2:** `python scripts/verificar.py` → `0 erro(s)`; `conferir_numeros.py` em cada nota → 0 faltantes.
- [ ] **Step 3:** Commit `feat(simples-nacional): notas dos caps. I a III, abrangência, vedações e cálculo`.

### Task 3: Art. 18 — segregação e Fator R (2 notas)

**Files:** Create `sn-segregacao-receitas.md` (art. 18, §4º, §4º-A, §§5º-B a 5º-I, monofásico/ST/exportação), `sn-fator-r.md` (§§5º-J a 5º-M, §24).

- [ ] **Step 1:** Redigir pelo procedimento comum. `sn-segregacao-receitas.md` traz bloco ⏳ 01/01/2027 com os incisos VIII e IX do §4º (texto literal da LC 227, art. 169, em `fontes/reforma/texto/lc-227-2026-planalto.htm`) e bloco ❌ 01/01/2033 para o inciso VI do §4º (LC 227, art. 181, IV, "d"). `sn-fator-r.md` traz a fórmula completa do Fator R e o efeito de cada lado dos 28%.
- [ ] **Step 2:** Verificação do procedimento comum.
- [ ] **Step 3:** Commit `feat(simples-nacional): segregação de receitas e Fator R`.

### Task 4: Anexos I a V (5 notas)

**Files:** Create `sn-anexo-i-comercio.md`, `sn-anexo-ii-industria.md`, `sn-anexo-iii-servicos.md`, `sn-anexo-iv-servicos.md`, `sn-anexo-v-servicos.md`.

- [ ] **Step 1:** Para cada Anexo N, recortar a **última** versão vigente da LC 123 (`--inicio "^ANEXO N\b" --ocorrencia -1`, ignorando linhas `[RISCADO]`) e o Anexo correspondente da LC 214 (XVIII a XXII) com todas as tabelas por período e suas legendas.
- [ ] **Step 2:** Escrever cada nota: tabela de alíquotas e tabela de repartição vigentes, literalmente; bloco `## ⏳ A partir de 01/01/2027 — redação dada pela LC 214/2025 (art. 519, Anexo X)` com **cada tabela por período** e sua legenda literal; nota sobre os Anexos de 2027–2028 da Res. CGSN 190 (fase B).
- [ ] **Step 3:** `conferir_numeros.py` em cada nota → 0 faltantes (é aqui que um erro de transcrição apareceria). `verificar.py` → 0 erros.
- [ ] **Step 4:** Commit `feat(simples-nacional): Anexos I a V (vigentes e LC 214)`.

### Task 5: MEI, sublimites, recolhimento e repasse (4 notas)

**Files:** Create `sn-mei.md` (18-A–18-F, Anexo VII da LC 214 via art. 520 / Anexo XXIII), `sn-sublimites-icms-iss.md` (19–20), `sn-recolhimento-das.md` (21–21-B), `sn-repasse-arrecadacao.md` (22).

- [ ] **Step 1:** Redigir pelo procedimento comum. `sn-mei.md`: as linhas do mapa para 18-A (IV e V "vigente — alteração prevista"; "e" revogada em 2033; b) e c) revogadas em 2027) viram ⏳/❌ com as datas do mapa; o §7º, I, do art. 18-A da LC 227 entra no bloco ⏳ 01/01/2027 com o texto literal. `sn-repasse-arrecadacao.md`: incisos IV a VI do art. 22 (LC 227, art. 168, vigente) e bloco ❌ para os incisos I e II (LC 214, art. 543, 2033).
- [ ] **Step 2:** Verificação do procedimento comum.
- [ ] **Step 3:** Commit `feat(simples-nacional): MEI, sublimites, recolhimento e repasse`.

### Task 6: Créditos, obrigações e exclusão (3 notas)

**Files:** Create `sn-creditos.md` (23–24), `sn-obrigacoes-acessorias.md` (25–27), `sn-exclusao.md` (28–32).

- [ ] **Step 1:** Redigir. `sn-exclusao.md` traz `## ❌ Revogado a partir de 30/11/2026 — LC 227/2026 (art. 181, IV, "c")` para o §4º do art. 31. `sn-obrigacoes-acessorias.md` menciona a NFS-e de padrão nacional obrigatória a partir de 01/11/2026 (Res. CGSN 191, art. 3º, I) como ponto da fase B, ligando a `[[ibs-cbs-cadastro-documento-fiscal]]`.
- [ ] **Step 2:** Verificação do procedimento comum.
- [ ] **Step 3:** Commit `feat(simples-nacional): créditos, obrigações acessórias e exclusão`.

### Task 7: Fiscalização, penalidades e processo (3 notas)

**Files:** Create `sn-fiscalizacao-omissao-receita.md` (33–34), `sn-acrescimos-penalidades.md` (35–38-B), `sn-processo-administrativo-judicial.md` (39–41).

- [ ] **Step 1:** Redigir. Blocos ⏳ 01/01/2027 para o §1º-C do art. 33 e o inciso II do art. 38-B (LC 227, art. 169, texto literal). Contencioso do art. 39 (LC 227, art. 168, vigente).
- [ ] **Step 2:** Verificação do procedimento comum.
- [ ] **Step 3:** Commit `feat(simples-nacional): fiscalização, penalidades e processo`.

### Task 8: Níveis 2 e 3 (6 notas)

**Files:** Create `sn-acesso-mercados.md` (42–49-B), `sn-simplificacao-trabalhista.md` (50–54), `sn-fiscalizacao-orientadora.md` (55), `sn-associativismo-credito-inovacao.md` (56–67-A), `sn-regras-civis-justica-apoio.md` (68–76-A), `sn-disposicoes-finais.md` (77–89).

- [ ] **Step 1:** Redigir no nível de profundidade do plano (médio: uma seção por seção da lei; resumo: visão geral com os artigos de cada instituto).
- [ ] **Step 2:** Verificação do procedimento comum.
- [ ] **Step 3:** Commit `feat(simples-nacional): notas de nível 2 e 3`.

### Task 9: Ligações, protocolo e perguntas-teste

**Files:**
- Create: `notas/simples-nacional/INDEX.md`, `docs/perguntas-teste/simples-nacional.md`
- Modify: `notas/simples-nacional/_plano-notas.md` (`status: concluido`), `notas/INDEX.md`, `notas/reforma/simples-nacional-e-mei.md` (seção "Ligações com o domínio simples-nacional"), `CLAUDE.md` (status "ativo (28 notas)"), `MEMORY.md`, `fontes/reforma/FONTE.md` (linha do HTML da LC 214)

- [ ] **Step 1:** Escrever o `INDEX.md` do domínio (notas por tema, com uma linha de descrição cada), atualizar o índice mestre, a ponte, o CLAUDE.md, o MEMORY.md e o FONTE.md; mudar o plano para `status: concluido`.
- [ ] **Step 2:** Cruzamento mapa × notas (Review Focus 2):

```bash
python -I - <<'EOF'
import re, sys, pathlib
sys.stdout.reconfigure(encoding="utf-8")
mapa = pathlib.Path("notas/simples-nacional/_mapa-vigencia.md").read_text(encoding="utf-8")
futuros = sorted({l.split("|")[1].strip() for l in mapa.splitlines()
                  if l.startswith("| ") and ("⏳" in l or "alteração prevista" in l)})
plano = pathlib.Path("notas/simples-nacional/_plano-notas.md").read_text(encoding="utf-8")
for art in futuros:
    notas = [l.split("|")[1].strip() for l in plano.splitlines() if l.startswith("| sn-")]
    textos = {n: pathlib.Path("notas/simples-nacional", n).read_text(encoding="utf-8") for n in notas}
    achou = [n for n, t in textos.items() if "⏳" in t and re.search(rf"\bart\. {re.escape(art)}\b|{re.escape(art)}\b", t)]
    print(f"{art}: {'OK' if achou else 'SEM BLOCO ⏳'} {achou[:2]}")
EOF
```
Expected: nenhum `SEM BLOCO ⏳`.

- [ ] **Step 3:** `python scripts/verificar.py` → `0 erro(s), 0 aviso(s)` (plano concluído exige todas as notas).
- [ ] **Step 4:** Escrever `docs/perguntas-teste/simples-nacional.md` com 12 perguntas (mesmo formato da bateria da reforma: pergunta, deve citar, comportamento esperado), cobrindo: cálculo da alíquota efetiva com números; Fator R no limite de 28%; vedação de ingresso; armadilha de vigência (DAS hoje × 2027); Anexo III em 2027; MEI e IBS (cruzamento); crédito de IBS/CBS de quem compra de optante (cruzamento); exclusão e o §4º do art. 31 (revogação em 30/11/2026); multa de 60% (só 2027); NFS-e nacional (fase B/lacuna de conteúdo da Res. 140); sublimite de um Estado específico (fora de escopo); IRPJ dentro do Simples (no escopo).
- [ ] **Step 5:** Rodar as 12 com `claude -p` e as 5 da reforma; conferir "deve citar" e comportamento. Ajustar notas/protocolo se alguma falhar, e rodar de novo.
- [ ] **Step 6:** Commit `feat(simples-nacional): índice, ligações, protocolo e perguntas-teste`.
