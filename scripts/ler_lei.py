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
