#!/usr/bin/env python3
"""Consulta o código IBGE de municípios, distritos e subdistritos (DTB, data-base 22/11/2024).

Uso:
  python scripts/consulta_ibge.py lapa            # busca por parte do nome (sem acento/maiúsculas)
  python scripts/consulta_ibge.py lapa PR         # filtra pela sigla da UF
  python scripts/consulta_ibge.py --codigo 4113205
  python scripts/consulta_ibge.py --distritos pedras negras

Lê os TSV de fontes/documentos-fiscais/texto/ (gerados dos relatórios do IBGE).
"""
import argparse
import csv
import sys
import unicodedata
from pathlib import Path

TEXTO = Path(__file__).resolve().parent.parent / "fontes" / "documentos-fiscais" / "texto"


def norm(s):
    s = unicodedata.normalize("NFD", s or "")
    return "".join(c for c in s if unicodedata.category(c) != "Mn").lower()


def ler(nome):
    with open(TEXTO / nome, encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("termo", nargs="*", help="parte do nome; um token de 2 letras no final filtra a UF")
    ap.add_argument("--codigo", help="código IBGE exato (7 dígitos: município; 9: distrito; 11: subdistrito)")
    ap.add_argument("--distritos", action="store_true", help="busca nos distritos em vez dos municípios")
    a = ap.parse_args()

    if a.codigo:
        c = a.codigo.strip()
        arq, campo = {7: ("ibge-dtb-municipios.tsv", "cod_municipio"),
                      9: ("ibge-dtb-distritos.tsv", "cod_distrito"),
                      11: ("ibge-dtb-subdistritos.tsv", "cod_subdistrito")}.get(len(c), (None, None))
        if not arq:
            sys.exit("Código IBGE tem 7 (município), 9 (distrito) ou 11 (subdistrito) dígitos.")
        achou = [r for r in ler(arq) if r[campo] == c]
        for r in achou:
            print("\t".join(r.values()))
        sys.exit(0 if achou else "Código não encontrado na DTB de 22/11/2024.")

    if not a.termo:
        ap.error("informe o nome ou --codigo")
    termo = list(a.termo)
    uf = None
    if len(termo) > 1 and len(termo[-1]) == 2 and termo[-1].isalpha():
        uf = termo.pop().upper()
    busca = norm(" ".join(termo))
    if a.distritos:
        mun = {r["cod_municipio"]: r for r in ler("ibge-dtb-municipios.tsv")}
        achou = [r for r in ler("ibge-dtb-distritos.tsv") if busca in norm(r["distrito"])
                 and (not uf or mun[r["cod_municipio"]]["uf_sigla"] == uf)]
        for r in achou:
            print(f'{r["cod_distrito"]}\t{r["distrito"]}\t(município {r["cod_municipio"]} {r["municipio"]})')
    else:
        achou = [r for r in ler("ibge-dtb-municipios.tsv") if busca in norm(r["municipio"])
                 and (not uf or r["uf_sigla"] == uf)]
        for r in achou:
            print(f'{r["cod_municipio"]}\t{r["municipio"]}\t{r["uf_sigla"]}')
    if not achou:
        sys.exit("Nada encontrado.")


if __name__ == "__main__":
    main()
