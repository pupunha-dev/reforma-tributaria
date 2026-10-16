#!/usr/bin/env python3
"""Gera as notas por item da LC 116 a partir da correlação expandida do Anexo VIII.

Uso: python scripts/gerar_notas_anexo_viii.py [raiz]

Lê fontes/documentos-fiscais/texto/anexo-viii-correlacao-expandida.tsv (gerado por
scripts/anexo_viii.py) e grava as notas notas/documentos-fiscais/df-nfse-correlacao-itens-*.md.
Cada nota agrupa itens da lista de serviços; para cada item mostra, por bloco de NBS com o mesmo
cIndOp e o mesmo local de incidência, os códigos cClassTrib que a planilha liga a cada NBS.
A nota principal (df-nfse-correlacao-nbs-indop) é escrita à mão.
"""
from __future__ import annotations

import csv
import sys
from collections import OrderedDict
from pathlib import Path

TEXTO_BASE = "2026-10-16"
FONTES = ("Anexo VIII — correlação entre item da NBS, cIndOp e cClassTrib v1.01.00 (planilha "
          '"tabela geral"); NT CGNFS-e 009 v1.01 (cita o anexo); Anexo VII v1.03.00')

# (arquivo, título, itens iniciais e finais por prefixo de 2 dígitos)
GRUPOS = [
    ("df-nfse-correlacao-itens-01-06", "itens 01 a 06", ("01", "06")),
    ("df-nfse-correlacao-itens-07", "item 07 (construção civil, obras, engenharia)", ("07", "07")),
    ("df-nfse-correlacao-itens-08-13", "itens 08 a 13", ("08", "13")),
    ("df-nfse-correlacao-itens-14-16", "itens 14 a 16", ("14", "16")),
    ("df-nfse-correlacao-itens-17-40", "itens 17 a 40", ("17", "40")),
    ("df-nfse-correlacao-itens-99", "item 99 (códigos nacionais de uso especial)", ("99", "99")),
]


def normaliza_local(texto: str) -> str:
    t = " ".join(texto.split())
    if not t:
        return "(vazio na planilha)"
    baixo = t.lower()
    if baixo in ("local evento", "local do evento"):
        return "Local do evento"
    if baixo.startswith("local da entrega ou"):
        return "Local da entrega ou da disponibilização"
    return t[0].upper() + t[1:]


def ler(raiz: Path) -> list[dict[str, str]]:
    caminho = raiz / "fontes/documentos-fiscais/texto/anexo-viii-correlacao-expandida.tsv"
    with caminho.open(encoding="utf-8", newline="") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def agrupar_item(linhas: list[dict[str, str]]):
    """Por (NBS, descrição), a lista de (cIndOp, local, onerosa, exterior) -> cClassTrib na ordem da planilha."""
    nbs_map: "OrderedDict[tuple[str, str], OrderedDict]" = OrderedDict()
    for r in linhas:
        chave_nbs = (r["nbs"] or "(sem NBS)", r["descricao_nbs"])
        combos = nbs_map.setdefault(chave_nbs, OrderedDict())
        combo = (r["indop"], normaliza_local(r["local_incidencia_ibs"]),
                 r["ps_onerosa"].upper(), r["adq_exterior"].upper())
        lista = combos.setdefault(combo, [])
        if r["cclasstrib"] and r["cclasstrib"] not in lista:
            lista.append(r["cclasstrib"])
    return nbs_map


def rotulo_combo(combo: tuple[str, str, str, str], com_flags: bool) -> str:
    indop, local, ps, adq = combo
    t = f"cIndOp `{indop}`" if indop else "cIndOp (vazio na planilha)"
    t += f"; local de incidência: {local}"
    if com_flags and (ps or adq):
        t += f"; P/S onerosa = {ps or '-'}, adquirente exterior = {adq or '-'}"
    return t


def gerar_nota(titulo: str, faixa: tuple[str, str], linhas: list[dict[str, str]]) -> str:
    por_item: "OrderedDict[str, list[dict[str, str]]]" = OrderedDict()
    for r in linhas:
        por_item.setdefault(r["item"], []).append(r)
    total_nbs = len({r["nbs"] for r in linhas if r["nbs"]})
    out = [
        "---",
        f"título: NFS-e Nacional — correlação NBS × cIndOp × cClassTrib (Anexo VIII), {titulo}",
        "dominio: documentos-fiscais",
        f"fontes: {FONTES}",
        "vigencia: com-mudanca-programada",
        f"texto-base: {TEXTO_BASE}",
        "---",
        "",
        f"# Correlação NBS × cIndOp × cClassTrib: {titulo}",
        "",
        "> **Nota gerada** por `scripts/gerar_notas_anexo_viii.py` a partir da planilha oficial "
        "(Anexo VIII v1.01.00); não edite à mão. Como ler a planilha, o que ela é e o que não é, "
        "a legenda dos cClassTrib e a regra do inciso X estão em [[df-nfse-correlacao-nbs-indop]]. "
        "Os significados dos cIndOp estão em [[df-nfse-indop-ibscbs]].",
        "",
        f"Itens da lista de serviços nesta nota: {len(por_item)}; NBS distintas: {total_nbs}. "
        "A coluna **cClassTrib** traz todos os códigos que a planilha liga à NBS naquele cIndOp "
        "(o primeiro costuma ser o geral; os demais são alternativas que dependem do fato "
        "concreto, e a planilha não diz quando cada um vale).",
        "",
    ]
    for item, rs in por_item.items():
        out.append(f"## Item {item} — {rs[0]['descricao_item'].strip().rstrip('.')}")
        out.append("")
        nbs_map = agrupar_item(rs)
        todos = list(OrderedDict.fromkeys(c for combos in nbs_map.values() for c in combos))
        if len(todos) == 1:
            out.append("**" + rotulo_combo(todos[0], True) + "**")
            out.append("")
            out.append("| NBS | Descrição | cClassTrib |")
            out.append("|---|---|---|")
            for (nbs, desc), combos in nbs_map.items():
                cc = ", ".join(next(iter(combos.values()))) or "-"
                out.append(f"| `{nbs}` | {desc.replace('|', '/')} | {cc} |")
        else:
            out.append("| NBS | Descrição | cIndOp, local de incidência e cClassTrib |")
            out.append("|---|---|---|")
            for (nbs, desc), combos in nbs_map.items():
                agrup: "OrderedDict[tuple, list[str]]" = OrderedDict()
                for combo, cc in combos.items():
                    indop, local, ps, adq = combo
                    agrup.setdefault((local, ps, adq, tuple(cc)), []).append(indop)
                partes = []
                for (local, ps, adq, cc), indops in agrup.items():
                    flag = f", onerosa={ps or '-'}/exterior={adq or '-'}" if (ps or adq) else ""
                    nomes = ", ".join(f"`{i or 'vazio'}`" for i in indops)
                    partes.append(f"{nomes} ({local}{flag}): {', '.join(cc) or '-'}")
                out.append(f"| `{nbs}` | {desc.replace('|', '/')} | {'; '.join(partes)} |")
        out.append("")
    return "\n".join(out).rstrip() + "\n"


def main(argv: list[str]) -> int:
    raiz = Path(argv[1]) if len(argv) > 1 else Path(__file__).resolve().parent.parent
    linhas = ler(raiz)
    usados = 0
    for arquivo, titulo, (ini, fim) in GRUPOS:
        sel = [r for r in linhas if ini <= r["item"].split(".")[0] <= fim]
        usados += len(sel)
        texto = gerar_nota(titulo, (ini, fim), sel)
        destino = raiz / "notas/documentos-fiscais" / f"{arquivo}.md"
        destino.write_text(texto, encoding="utf-8")
        print(f"{destino.relative_to(raiz)}: {len(sel)} linhas, {len(texto)} bytes")
    if usados != len(linhas):
        print(f"ERRO: {len(linhas) - usados} linhas fora dos grupos", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
