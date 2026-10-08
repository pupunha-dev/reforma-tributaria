"""Captura e confere as tabelas da reforma no Portal dos DF-e (SVRS): CST/cClassTrib e cCredPres.

Uso:
  python scripts/tabelas_svrs.py cclasstrib --data AAAA-MM-DD [--saida fontes/documentos-fiscais/texto]
  python scripts/tabelas_svrs.py ccredpres --data AAAA-MM-DD [--saida fontes/documentos-fiscais/texto]
  python scripts/tabelas_svrs.py conferir <nota.md> [--json <arquivo.json>]
  python scripts/tabelas_svrs.py nota <nota.md> [--json <arquivo.json>]

Endereços: os indicados no IT 2025.002 v1.60, seção 06 ("Tabelas Online").
- cClassTrib: a página traz os dados como JSON embutido (variável
  `dadosOriginais`); grava o JSON completo (texto legal, listas NCM/NBS) e um
  Markdown para leitura.
- cCredPres: a página é uma tabela HTML; cada código tem uma linha de detalhe
  ("Detalhes do Crédito Presumido N") com configurações e vigência por tributo,
  lida como texto.
`conferir` sai com código 1 se algum código de 6 dígitos da nota (em crase ou na
1ª coluna de tabela) não existir no JSON do cClassTrib. `nota` regera, a partir
do JSON, só os trechos da nota entre `<!-- gerado:cst -->` e
`<!-- gerado:cclasstrib -->` e seus fechamentos `<!-- /gerado:... -->`.
"""
from __future__ import annotations

import argparse
import html as html_lib
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

URL = "https://dfe-portal.svrs.rs.gov.br/DFE/TabelaClassificacaoTributaria"
URL_CCREDPRES = "https://dfe-portal.svrs.rs.gov.br/DFE/TabelaCreditoPresumido"
MARCADOR = "var dadosOriginais = "
NOME_ARQUIVO = "cclasstrib-svrs"
NOME_CCREDPRES = "ccredpres-svrs"

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
        "`scripts/tabelas_svrs.py` a partir do JSON da página; o JSON completo "
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


TIPO_RBSN = {0: "0 Não é receita bruta", 1: "1 Receita bruta interna",
             2: "2 Receita bruta interna sem cálculo IBS/CBS", 3: "3 Exportação direta",
             4: "4 Exportação indireta", 5: "5 Mercado interno/exportação",
             9: "9 Incompatível com SN"}


def tabela_cst_nota(dados: list[dict]) -> str:
    linhas = ["| CST | Situação | Indicadores marcados | cClassTrib |", "|---|---|---|---|"]
    for c in dados:
        marcados = ", ".join(n for campo, n in FLAGS_CST if c.get(campo)) or "nenhum"
        linhas.append(f"| {c['Cst']} | {_celula(c['NomeCst'])} | {marcados} | "
                      f"{len(c['ClassificacoesTributarias'])} |")
    return "\n".join(linhas)


def tabelas_classif_nota(dados: list[dict]) -> str:
    cab = ["cClassTrib", "Descrição", "Red. IBS", "Red. CBS", "Alíquota", "Vigência",
           "Documentos", "Simples (tpRBSN)"]
    blocos = []
    for c in dados:
        linhas = [f"### CST {c['Cst']} — {_celula(c['NomeCst'])}", "",
                  "| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
        for x in c["ClassificacoesTributarias"]:
            linhas.append("| " + " | ".join([
                x["CodClassTrib"], _celula(x["NomeClassTrib"]), pct(x["PercRedIbs"]),
                pct(x["PercRedCbs"]), TIPO_ALIQUOTA.get(x.get("TipoAliq"), "-"), vigencia(x),
                documentos(x) or "-", TIPO_RBSN.get(x.get("TipoRbSn"), "-")]) + " |")
        blocos.append("\n".join(linhas))
    return "\n\n".join(blocos)


def substituir_bloco(texto: str, nome: str, conteudo: str) -> str:
    padrao = re.compile(rf"(<!-- gerado:{nome} -->).*?(<!-- /gerado:{nome} -->)", re.S)
    if not padrao.search(texto):
        raise ValueError(f"marcadores <!-- gerado:{nome} --> não encontrados")
    return padrao.sub(lambda m: f"{m.group(1)}\n{conteudo}\n{m.group(2)}", texto, count=1)


def codigos(nota: str) -> set[str]:
    nota = EXEMPLO.sub("", FRONTMATTER.sub("", nota))
    return set(CODIGO_EM_CRASE.findall(nota)) | set(CODIGO_EM_TABELA.findall(nota))


def faltantes(nota: str, dados: list[dict]) -> list[str]:
    existentes = {c["CodClassTrib"] for c in classificacoes(dados)}
    return sorted(codigos(nota) - existentes)


DETALHE = re.compile(r'<tr id="detail-[^"]*".*?(?=<tr |</tbody>)', re.S)
CONFIG_CREDPRES = [("apropria_dfe", "Apropria DFE"), ("apropria_evento", "Apropria Evento"),
                   ("deduz", "Deduz Crédito Presumido"),
                   ("declaracao_pagamento", "Declaração de Pagamento")]
DOCS_CREDPRES = ["NFe", "NFCe", "CTe", "NFSe"]
TRIBUTO = re.compile(
    r"(IBS|CBS) \([^)]*\) Aplicável: (Sim|Não)"
    r"(?: Início Vigência: (Não informado|\d{2}/\d{2}/\d{4}))?"
    r"(?: Fim Vigência: (Indeterminado|\d{2}/\d{2}/\d{4}))?")


def _texto_html(trecho: str) -> str:
    sem_tags = re.sub(r"<[^>]+>", " ", trecho)
    return " ".join(html_lib.unescape(sem_tags).split())


def _sim(texto: str, rotulo: str) -> bool:
    m = re.search(rf"(?<![\w]){re.escape(rotulo)}: (Sim|Não)", texto)
    if not m:
        raise ValueError(f"campo '{rotulo}' não encontrado")
    return m.group(1) == "Sim"


def extrair_ccredpres(html: str) -> list[dict]:
    itens = []
    for bloco in DETALHE.finditer(html):
        texto = _texto_html(bloco.group(0))
        cab = re.search(r"Código: (\d+) Descrição: (.*?) Configurações:", texto)
        if not cab:
            raise ValueError("linha de detalhe sem código e descrição")
        item = {"codigo": int(cab.group(1)), "descricao": cab.group(2)}
        for chave, rotulo in CONFIG_CREDPRES:
            item[chave] = _sim(texto, rotulo)
        item["documentos"] = [d for d in DOCS_CREDPRES if _sim(texto, d)]
        vigencia = texto.split("Vigência dos Tributos:", 1)[-1]
        for trib, aplicavel, ini, fim in TRIBUTO.findall(vigencia):
            item[trib.lower()] = {"aplicavel": aplicavel == "Sim",
                                  "inicio": ini or None, "fim": fim or None}
        itens.append(item)
    if not itens:
        raise ValueError("nenhuma linha de detalhe de crédito presumido encontrada")
    return itens


def _vig_credpres(trib: dict) -> str:
    if not trib.get("aplicavel"):
        return "não se aplica"
    if trib.get("inicio") in (None, "Não informado"):
        return "início não informado"
    fim = trib.get("fim")
    return f"{trib['inicio']} em diante" if fim in (None, "Indeterminado") else f"{trib['inicio']} a {fim}"


def markdown_ccredpres(itens: list[dict], data: str, url: str) -> str:
    sn = lambda v: "Sim" if v else "Não"  # noqa: E731
    cab = ["cCredPres", "Descrição", "Apropria no DF-e", "Apropria por evento", "Deduz do tributo",
           "Declaração de pagamento", "Documentos", "IBS", "CBS"]
    linhas = [
        "# Tabela cCredPres — Portal dos DF-e (SVRS)", "",
        f"Origem: {url}", f"Capturado em: {data}",
        f"Conteúdo: {len(itens)} códigos. Gerado por `scripts/tabelas_svrs.py`; dados "
        f"estruturados em `{NOME_CCREDPRES}.json`.", "",
        "| " + " | ".join(cab) + " |", "|" + "---|" * len(cab),
    ]
    for i in itens:
        linhas.append("| " + " | ".join([
            str(i["codigo"]), _celula(i["descricao"]), sn(i["apropria_dfe"]), sn(i["apropria_evento"]),
            sn(i["deduz"]), sn(i["declaracao_pagamento"]), ", ".join(i["documentos"]) or "-",
            _vig_credpres(i.get("ibs", {})), _vig_credpres(i.get("cbs", {}))]) + " |")
    return "\n".join(linhas) + "\n"


def _get(url: str) -> str:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.read().decode("utf-8", errors="replace")


def _ccredpres(args: argparse.Namespace) -> int:
    itens = extrair_ccredpres(_get(URL_CCREDPRES))
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / f"{NOME_CCREDPRES}.json").write_text(
        json.dumps(itens, ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / f"{NOME_CCREDPRES}.md").write_text(
        markdown_ccredpres(itens, args.data, URL_CCREDPRES), encoding="utf-8")
    print(f"{len(itens)} cCredPres gravados em {saida}")
    return 0


def _baixar(args: argparse.Namespace) -> int:
    dados = extrair_dados(_get(URL))
    saida = Path(args.saida)
    saida.mkdir(parents=True, exist_ok=True)
    (saida / f"{NOME_ARQUIVO}.json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=1), encoding="utf-8")
    (saida / f"{NOME_ARQUIVO}.md").write_text(
        gerar_markdown(dados, args.data, URL), encoding="utf-8")
    print(f"{len(dados)} CST, {len(classificacoes(dados))} cClassTrib gravados em {saida}")
    return 0


def _nota(args: argparse.Namespace) -> int:
    dados = json.loads(Path(args.json).read_text(encoding="utf-8"))
    texto = args.nota.read_text(encoding="utf-8")
    texto = substituir_bloco(texto, "cst", tabela_cst_nota(dados))
    texto = substituir_bloco(texto, "cclasstrib", tabelas_classif_nota(dados))
    args.nota.write_text(texto, encoding="utf-8", newline="\n")
    print(f"tabelas de {args.nota.name} atualizadas ({len(classificacoes(dados))} cClassTrib)")
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
    for nome, func in (("cclasstrib", _baixar), ("ccredpres", _ccredpres)):
        b = sub.add_parser(nome)
        b.add_argument("--data", required=True, help="data da captura, AAAA-MM-DD")
        b.add_argument("--saida", default=str(padrao_saida))
        b.set_defaults(func=func)
    for nome, func in (("conferir", _conferir), ("nota", _nota)):
        c = sub.add_parser(nome)
        c.add_argument("nota", type=Path)
        c.add_argument("--json", default=str(padrao_saida / f"{NOME_ARQUIVO}.json"))
        c.set_defaults(func=func)
    args = parser.parse_args(argv[1:])
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
