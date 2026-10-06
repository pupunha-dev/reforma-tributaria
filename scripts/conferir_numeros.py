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
