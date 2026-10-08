"""Captura e confere a tabela CST/cClassTrib do Portal da Conformidade Fácil (SVRS).

Uso:
  python scripts/cclasstrib_svrs.py baixar --data AAAA-MM-DD [--saida fontes/documentos-fiscais/texto]
  python scripts/cclasstrib_svrs.py conferir <nota.md> [--json <arquivo.json>]

A página publica os dados como JSON embutido (variável `dadosOriginais`), então
não há raspagem de tela. `baixar` grava o JSON completo (inclui as listas
NCM/NBS e o texto legal) e uma versão em Markdown para leitura. `conferir` sai
com código 1 se algum código de 6 dígitos da nota (em crase ou na 1ª coluna de
tabela) não existir no JSON.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

URL = "https://dfe-portal.svrs.rs.gov.br/Cff/ClassificacaoTributaria"
MARCADOR = "var dadosOriginais = "
NOME_ARQUIVO = "cclasstrib-svrs"

DOCUMENTOS = [
    ("IndNfe", "NFe"), ("IndNfce", "NFCe"), ("IndCte", "CTe"), ("IndCteos", "CTe OS"),
    ("IndBpe", "BPe"), ("IndNf3e", "NF3e"), ("IndNfcom", "NFCom"), ("IndNfse", "NFSE"),
    ("IndBpetm", "BPe TM"), ("IndBpeta", "BPe TA"), ("IndNfag", "NFAg"),
    ("IndNfsvia", "NFSVIA"), ("IndNfabi", "NFABI"), ("IndNfgas", "NFGas"),
    ("IndDere", "DERE"), ("IndDir", "DIR"), ("IndDuimp", "DUIMP"),
]
TIPO_ALIQUOTA = {1: "Fixa", 2: "Padrão", 3: "Sem alíquota", 4: "Uniforme nacional",
                 5: "Uniforme setorial"}
FLAGS_CST = [
    ("IndExigeTrib", "Exige tributação"), ("IndReducaoBc", "Redução de BC"),
    ("IndReducaoAliq", "Redução de alíquota"), ("IndTransferenciaCred", "Transferência de crédito"),
    ("IndDiferimento", "Diferimento"), ("IndMonofasica", "Monofásica"),
    ("IndCredPresIbsZfm", "Créd. presumido IBS ZFM"), ("IndAjusteCompet", "Ajuste de competência"),
]
CODIGO_EM_CRASE = re.compile(r"`(\d{6})`")
CODIGO_EM_TABELA = re.compile(r"^\|\s*(\d{6})\s*\|", re.M)
EXEMPLO = re.compile(r"<!--\s*exemplo\s*-->.*?<!--\s*/exemplo\s*-->", re.S)
FRONTMATTER = re.compile(r"\A---\n.*?\n---\n", re.S)


def extrair_dados(html: str) -> list[dict]:
    i = html.find(MARCADOR)
    if i < 0:
        raise ValueError("variável dadosOriginais não encontrada na página")
    dados, _ = json.JSONDecoder().raw_decode(html[i + len(MARCADOR):])
    return dados


def pct(valor: float) -> str:
    texto = f"{valor:g}".replace(".", ",")
    return f"{texto}%"


def documentos(classif: dict) -> str:
    return ", ".join(nome for campo, nome in DOCUMENTOS if classif.get(campo))


def _data(iso: str) -> str:
    return datetime.fromisoformat(iso).strftime("%d/%m/%Y")


def vigencia(classif: dict) -> str:
    ini = _data(classif["DthIniVig"])
    if classif.get("DthFimVig"):
        return f"{ini} a {_data(classif['DthFimVig'])}"
    return f"{ini} em diante"


def classificacoes(dados: list[dict]) -> list[dict]:
    return [c for cst in dados for c in cst["ClassificacoesTributarias"]]


def _celula(texto: str) -> str:
    return " ".join(str(texto).split()).replace("|", "/")


def tabela_cst(dados: list[dict]) -> str:
    cab = ["CST", "Situação"] + [nome for _, nome in FLAGS_CST] + ["Qtde cClassTrib"]
    linhas = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for cst in dados:
        marcas = ["Sim" if cst.get(campo) else "Não" for campo, _ in FLAGS_CST]
        linhas.append("| " + " | ".join(
            [cst["Cst"], _celula(cst["NomeCst"])] + marcas
            + [str(len(cst["ClassificacoesTributarias"]))]) + " |")
    return "\n".join(linhas)


def tabela_classificacoes(cst: dict) -> str:
    cab = ["cClassTrib", "Descrição", "Red. IBS", "Red. CBS", "Alíquota", "Vigência",
           "Documentos", "Trib. regular", "Créd. presumido", "Legislação"]
    linhas = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    for c in cst["ClassificacoesTributarias"]:
        linhas.append("| " + " | ".join([
            c["CodClassTrib"], _celula(c["NomeClassTrib"]), pct(c["PercRedIbs"]), pct(c["PercRedCbs"]),
            TIPO_ALIQUOTA.get(c.get("TipoAliq"), "-"), vigencia(c), documentos(c) or "-",
            "Sim" if c.get("IndTribRegular") else "Não",
            "Sim" if c.get("IndPermiteCredPres") else "Não",
            _celula(c.get("TexUrlLegislacao") or "-")]) + " |")
    return "\n".join(linhas)


def gerar_markdown(dados: list[dict], data: str, url: str) -> str:
    todas = classificacoes(dados)
    partes = [
        "# Tabela CST e cClassTrib — Portal da Conformidade Fácil (SVRS)",
        "",
        f"Origem: {url}",
        f"Capturado em: {data}",
        f"Conteúdo: {len(dados)} CST e {len(todas)} cClassTrib. Gerado por "
        "`scripts/cclasstrib_svrs.py` a partir do JSON da página; o JSON completo "
        f"(texto legal e listas NCM/NBS) está em `{NOME_ARQUIVO}.json`.",
        "",
        "## CST (situação tributária)",
        "",
        tabela_cst(dados),
    ]
    for cst in dados:
        partes += ["", f"## CST {cst['Cst']} — {_celula(cst['NomeCst'])}", "",
                   tabela_classificacoes(cst)]
    return "\n".join(partes) + "\n"


def codigos(nota: str) -> set[str]:
    nota = EXEMPLO.sub("", FRONTMATTER.sub("", nota))
    return set(CODIGO_EM_CRASE.findall(nota)) | set(CODIGO_EM_TABELA.findall(nota))


def faltantes(nota: str, dados: list[dict]) -> list[str]:
    existentes = {c["CodClassTrib"] for c in classificacoes(dados)}
    return sorted(codigos(nota) - existentes)


def _baixar(args: argparse.Namespace) -> int:
    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        html = resp.read().decode("utf-8", errors="replace")
    dados = extrair_dados(html)
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / f"{NOME_ARQUIVO}.json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / f"{NOME_ARQUIVO}.md").write_text(
        gerar_markdown(dados, args.data, URL), encoding="utf-8")
    print(f"{len(dados)} CST, {len(classificacoes(dados))} cClassTrib gravados em {saida}")
    return 0


def _conferir(args: argparse.Namespace) -> int:
    dados = json.loads(Path(args.json).read_text(encoding="utf-8"))
    falta = faltantes(args.nota.read_text(encoding="utf-8"), dados)
    for c in falta:
        print(f"FALTA NA TABELA  {c}")
    print(f"{len(falta)} código(s) sem correspondência em {args.nota.name}")
    return 1 if falta else 0


def main(argv: list[str]) -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    padrao_saida = Path(__file__).resolve().parent.parent / "fontes" / "documentos-fiscais" / "texto"
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = parser.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("baixar")
    b.add_argument("--data", required=True, help="data da captura, AAAA-MM-DD")
    b.add_argument("--saida", default=str(padrao_saida))
    b.set_defaults(func=_baixar)
    c = sub.add_parser("conferir")
    c.add_argument("nota", type=Path)
    c.add_argument("--json", default=str(padrao_saida / f"{NOME_ARQUIVO}.json"))
    c.set_defaults(func=_conferir)
    args = parser.parse_args(argv[1:])
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
