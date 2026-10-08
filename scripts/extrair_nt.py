"""Extrai o texto VIGENTE de uma Nota Técnica (PDF), sem os trechos riscados.

Uso: python scripts/extrair_nt.py <nt.pdf> [<nt.pdf> ...] --saida-dir <pasta>
Gera, para cada PDF, <nome>-vigente.txt (texto sem o que está riscado, uma
linha visual por linha, colunas separadas por " | ") e <nome>-riscado.md
(lista do texto riscado, por página, para auditoria).

As NTs marcam a redação superada com um traço horizontal sobre o texto (como
o <strike> do Planalto); o pdftotext não distingue isso. Requer pymupdf
(pip install pymupdf).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

TOLERANCIA_LINHA = 2.0   # pontos: spans com centros verticais próximos = mesma linha
LACUNA_COLUNA = 15.0     # pontos: espaço horizontal que separa colunas


def _tracos(pagina) -> list:
    import pymupdf
    tracos = []
    for desenho in pagina.get_drawings():
        for item in desenho["items"]:
            if item[0] == "l":
                p1, p2 = item[1], item[2]
                if abs(p1.y - p2.y) < 1 and abs(p2.x - p1.x) > 3:
                    tracos.append(pymupdf.Rect(min(p1.x, p2.x), p1.y - 0.5, max(p1.x, p2.x), p1.y + 0.5))
            elif item[0] == "re":
                r = item[1]
                if r.height < 1.5 and r.width > 3:
                    tracos.append(r)
    return tracos


def _riscado(caixa, tracos) -> bool:
    altura = caixa.y1 - caixa.y0
    for t in tracos:
        meio = (t.y0 + t.y1) / 2
        if not (caixa.y0 + altura * 0.3 < meio < caixa.y1 - altura * 0.2):
            continue
        sobreposicao = min(caixa.x1, t.x1) - max(caixa.x0, t.x0)
        if sobreposicao >= 0.5 * (caixa.x1 - caixa.x0):
            return True
    return False


def _linhas(spans: list[tuple]) -> list[str]:
    """spans: (x0, y0, x1, y1, texto[, id do span]). Agrupa por linha visual e ordena por x.

    Pedaços do mesmo span (separados por um riscado parcial) nunca viram
    colunas diferentes: dentro de um span não há quebra de coluna.
    """
    grupos: list[list[tuple]] = []
    for sp in sorted(spans, key=lambda s: ((s[1] + s[3]) / 2, s[0])):
        centro = (sp[1] + sp[3]) / 2
        if grupos and abs(centro - grupos[-1][0]) <= TOLERANCIA_LINHA:
            grupos[-1][1].append(sp)
        else:
            grupos.append([centro, [sp]])
    saida = []
    for _, membros in grupos:
        membros.sort(key=lambda s: s[0])
        texto, fim, origem_ant = "", None, None
        for x0, _, x1, _, t, *origem in membros:
            mesmo_span = bool(origem) and origem == origem_ant
            if fim is None:
                texto = t
            elif x0 - fim > LACUNA_COLUNA and not mesmo_span:
                texto = texto.rstrip() + " | " + t.lstrip()
            elif texto.endswith(" ") or t.startswith(" "):
                texto += t
            else:
                texto += " " + t
            fim, origem_ant = x1, origem
        saida.append(" ".join(texto.split()))
    return saida


def _pedacos(span: dict, tracos, origem: int) -> list[tuple[bool, tuple]]:
    """Divide o span em trechos contínuos riscados ou não, letra por letra.

    O risco pode cobrir só parte de um span (ex.: só a data antiga de uma
    frase); classificar o span inteiro perderia o resto do texto.
    """
    import pymupdf
    y0, y1 = span["bbox"][1], span["bbox"][3]
    pedacos: list[list] = []  # [riscado, x0, x1, texto]
    for ch in span["chars"]:
        caixa = pymupdf.Rect(ch["bbox"])
        caixa.y0, caixa.y1 = y0, y1
        # espaço e pontuação herdam do vizinho: o traço às vezes não cobre a vírgula
        risc = _riscado(caixa, tracos) if ch["c"].isalnum() else None
        if pedacos and (risc is None or risc == pedacos[-1][0] or pedacos[-1][0] is None):
            if pedacos[-1][0] is None:
                pedacos[-1][0] = risc
            pedacos[-1][2] = caixa.x1
            pedacos[-1][3] += ch["c"]
        else:
            pedacos.append([risc, caixa.x0, caixa.x1, ch["c"]])
    return [(bool(r), (x0, y0, x1, y1, t, origem)) for r, x0, x1, t in pedacos if t.strip()]


def extrair(pdf: Path) -> tuple[str, list[tuple[int, str]]]:
    import pymupdf
    doc = pymupdf.open(pdf)
    paginas, riscados = [], []
    for n, pagina in enumerate(doc, 1):
        tracos = _tracos(pagina)
        vivos, mortos = [], []
        spans = (sp for bloco in pagina.get_text("rawdict")["blocks"]
                 for linha in bloco.get("lines", []) for sp in linha["spans"])
        for origem, sp in enumerate(spans):
            for risc, item in _pedacos(sp, tracos, origem):
                (mortos if risc else vivos).append(item)
        paginas.append(f"=== página {n} ===\n" + "\n".join(_linhas(vivos)))
        riscados += [(n, t) for t in _linhas(mortos)]
    return "\n\n".join(paginas) + "\n", riscados


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("pdfs", type=Path, nargs="+")
    parser.add_argument("--saida-dir", type=Path, required=True)
    args = parser.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    args.saida_dir.mkdir(parents=True, exist_ok=True)
    for pdf in args.pdfs:
        vigente, riscados = extrair(pdf)
        (args.saida_dir / f"{pdf.stem}-vigente.txt").write_text(vigente, encoding="utf-8", newline="\n")
        linhas = [f"# Texto riscado — {pdf.name}", "",
                  "Trechos marcados como superados (traço sobre o texto). **Não** usar nas notas.", ""]
        linhas += [f"- p. {n}: {t}" for n, t in riscados]
        (args.saida_dir / f"{pdf.stem}-riscado.md").write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")
        print(f"{pdf.name}: {len(riscados)} linha(s) riscada(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
