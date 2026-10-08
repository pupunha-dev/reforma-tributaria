"""Mapa entre a LC 214/2025 (e LC 227/2026) e os regulamentos da CBS e do IBS.

Uso:
  python scripts/mapa_regulamento.py \\
    --cbs fontes/reforma/texto/decreto-12955-2026-planalto.htm \\
    --ibs fontes/reforma/texto/res-cgibs-6-2026.txt \\
    --plano notas/reforma/_plano-notas.md \\
    --cabecalho fontes/reforma/texto/regulamentos-mapa-cabecalho.md \\
    --mapa notas/reforma/_mapa-regulamentos.md \\
    --textos fontes/reforma/texto [--notas notas/reforma]

Cada artigo dos regulamentos cita entre parênteses o artigo da lei que
regulamenta, como "(Art. 12, § 2º, da Lei Complementar nº 214, de 16 de janeiro
de 2025)" no Decreto 12.955/2026 e "(Art. 12, § 2º, da LC 214/2025)" na Res.
CGIBS 6/2026. O script:
- divide cada regulamento em artigos (texto por artigo em `--textos`);
- lê as citações e monta o mapa lei → regulamento (`--mapa`);
- com `--notas`, grava em cada nota do plano o bloco gerado
  `<!-- gerado:regulamentos -->` com os artigos dos dois regulamentos.
O texto da CBS vem do HTML compilado do Planalto, sem os parágrafos riscados.
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from tabelas_svrs import substituir_bloco  # noqa: E402

PARENTESES = re.compile(r"\(([^()]*)\)")
LEI = re.compile(
    r"Lei Complementar n[º°o]\s*(\d+),\s*de\s*(?:\d+\s*de\s*\w+\s*de\s*)?\d{4}"
    r"|\bLC\s*(\d+)/\d{4}")
PARAGRAFOS = re.compile(r"§+\s*\d+[º°o]?(?:\s*(?:,|e)\s*\d+[º°o]?)*")
NUMERO = re.compile(r"(\d+)[º°o]?(?:\s*-\s*([A-Z])\b)?")
CADEIA = re.compile(r"[Aa]rts?\.\s*\d+[º°o]?(?:\s*-\s*[A-Z]\b)?"
                    r"(?:\s*(?:,|e|a)\s*(?:[Aa]rts?\.\s*)?\d+[º°o]?(?:\s*-\s*[A-Z]\b)?)*")
OUTRO_ATO = re.compile(r"^\s*,?\s*(?:§[^a-z]*)?(?:d[ao]s?)\s+(?:Lei\b|Decreto|Constitui|Medida|Resolu|Emenda|Instru)")
CABECA_ARTIGO = re.compile(r"(?<![\w(])Art\.\s*(\d+)\s*[º°o]?(?:\s*-\s*([A-Z])\b)?\s*\.?(?=\s)")
TITULO = re.compile(r"\b(LIVRO|TÍTULO|CAPÍTULO|Seção|Subseção)\s+([IVXLC]+(?:-[A-Z])?)\b\s*-?\s*"
                    r"(?=D[aoAOEIS]|DISPOSI|NORMAS|Normas)")
NIVEIS = ["LIVRO", "TÍTULO", "CAPÍTULO", "Seção", "Subseção"]

# Cláusulas de vigência: Decreto 12.955/2026, art. 619, II (red. Decreto 13.075/2026),
# e Res. CGIBS 6/2026, art. 617, II e III. Artigos não listados: desde a publicação
# (salvo o Cap. I do Tít. II do Livro I e o art. 112, inciso I das duas cláusulas).
EFEITOS = {
    "CBS": {**{str(n): "01/01/2027" for n in [*range(245, 251), *range(252, 259), *range(518, 529), 531, 539]},
            "105": "01/01/2027 (só § 3º, VI, “b” e “d”)",
            "115": "01/01/2027 (só caput, VI, “b” e “c”)"},
    "IBS": {**{str(n): "01/01/2027" for n in [*range(245, 251), *range(252, 259), 515, 525, 526]},
            **{str(n): "01/01/2029" for n in [517, 518, 520, 521, 522, 528, 529, *range(532, 565), 615]}},
}
NOME_REG = {"CBS": "**Regulamento da CBS** (Decreto nº 12.955/2026)",
            "IBS": "**Regulamento do IBS** (Res. CGIBS nº 6/2026)"}
TITULO_SECAO = "## Regulamentação (Decreto 12.955/2026 e Res. CGIBS 6/2026)"


@dataclass
class Artigo:
    numero: str
    texto: str
    contexto: str
    leis: dict[str, list[str]] = field(default_factory=dict)


def chave(numero: str) -> tuple[int, int]:
    n, _, suf = numero.partition("-")
    return int(n), (ord(suf) - 64 if suf else 0)


def _numero(m: re.Match) -> str:
    return m.group(1) + (f"-{m.group(2)}" if m.group(2) else "")


def _artigos_da_cadeia(cadeia: str) -> list[str]:
    saida: list[str] = []
    anterior = None
    for m in NUMERO.finditer(cadeia):
        atual = _numero(m)
        antes = cadeia[:m.start()].rstrip()
        if anterior and re.search(r"\ba(?:\s+[Aa]rts?\.)?$", antes):
            ini, fim = chave(anterior)[0], chave(atual)[0]
            saida += [str(n) for n in range(ini + 1, fim)]
        saida.append(atual)
        anterior = atual
    return saida


def citacoes(texto: str) -> dict[str, list[str]]:
    """Artigos citados por lei ("214", "227"...), na ordem e sem repetição."""
    saida: dict[str, list[str]] = {}
    for p in PARENTESES.finditer(texto):
        conteudo, inicio = p.group(1), 0
        for lei in LEI.finditer(conteudo):
            trecho = PARAGRAFOS.sub(" ", conteudo[inicio:lei.start()])
            inicio = lei.end()
            numero_lei = lei.group(1) or lei.group(2)
            for cadeia in CADEIA.finditer(trecho):
                if OUTRO_ATO.match(trecho[cadeia.end():]):
                    continue  # artigo de outro ato citado no mesmo parêntese
                for art in _artigos_da_cadeia(cadeia.group(0)):
                    lista = saida.setdefault(numero_lei, [])
                    if art not in lista:
                        lista.append(art)
    return saida


def dividir_artigos(texto: str) -> list[Artigo]:
    candidatos, ultimo = [], (0, 0)
    for m in CABECA_ARTIGO.finditer(texto):
        k = chave(_numero(m))
        if k > ultimo and k[0] <= ultimo[0] + 10:
            candidatos.append(m)
            ultimo = k
    contexto: dict[str, str] = {}

    def atualizar(trecho: str) -> str:
        """Lê os títulos do trecho, atualiza o contexto e devolve o trecho sem eles."""
        for t in TITULO.finditer(trecho):
            nivel = t.group(1)
            fim = re.search(r"\s(?:Art\.|LIVRO|TÍTULO|CAPÍTULO|Seção|Subseção)\s|\n|$", trecho[t.end():])
            nome = " ".join((t.group(0) + trecho[t.end():t.end() + fim.start()]).split())
            for n in NIVEIS[NIVEIS.index(nivel):]:
                contexto.pop(n, None)
            contexto[nivel] = nome[:100]
        return trecho

    atualizar(texto[:candidatos[0].start()] if candidatos else texto)
    artigos = []
    for i, m in enumerate(candidatos):
        fim = candidatos[i + 1].start() if i + 1 < len(candidatos) else len(texto)
        corpo = texto[m.start():fim]
        ctx = " > ".join(contexto[n] for n in NIVEIS if n in contexto)
        corte = TITULO.search(corpo)
        proprio = corpo[:corte.start()] if corte else corpo
        artigos.append(Artigo(_numero(m), " ".join(proprio.split()), ctx, citacoes(proprio)))
        atualizar(corpo)
    return artigos


def inverter(artigos: list[Artigo], lei: str) -> dict[str, list[str]]:
    inv: dict[str, list[str]] = {}
    for a in artigos:
        for citado in a.leis.get(lei, []):
            lista = inv.setdefault(citado, [])
            if a.numero not in lista:
                lista.append(a.numero)
    return {k: sorted(v, key=chave) for k, v in inv.items()}


def _juntar(itens: list[str]) -> str:
    return itens[0] if len(itens) == 1 else ", ".join(itens[:-1]) + " e " + itens[-1]


def faixas(numeros: list[str]) -> str:
    if not numeros:
        return "—"
    nums = sorted(set(numeros), key=chave)
    partes, i = [], 0
    while i < len(nums):
        j = i
        while (j + 1 < len(nums) and "-" not in nums[j + 1] and "-" not in nums[j]
               and chave(nums[j + 1])[0] == chave(nums[j])[0] + 1):
            j += 1
        if j - i >= 2:
            partes.append(f"{nums[i]} a {nums[j]}")
        else:
            partes += nums[i:j + 1]
        i = j + 1
    return _juntar(partes)


@dataclass
class NotaPlano:
    nota: str
    lei: str
    intervalos: list[tuple[str, tuple[int, int], tuple[int, int]]]

    def contem(self, artigo: str, lei: str | None = None) -> bool:
        k = chave(artigo)
        return any(l == (lei or self.lei) and ini <= k <= fim for l, ini, fim in self.intervalos)

    def leis(self) -> list[str]:
        return sorted({l for l, _, _ in self.intervalos})


ROTULO = r"(\d+)(?:-([A-Z]{1,2}|[IVX]+))?"


def _chave_rotulo(m: re.Match, fim: bool) -> tuple[int, int]:
    n, suf = int(m.group(1)), m.group(2) or ""
    if suf and re.fullmatch(r"[A-Z]", suf):
        return n, ord(suf) - 64
    return (n, 99) if fim else (n, 0)  # inciso (181-IV) ou sem sufixo: o artigo inteiro


def notas_do_plano(md: str) -> list[NotaPlano]:
    saida, lei_secao = [], "214"
    for linha in md.splitlines():
        if linha.startswith("## "):
            lei_secao = "227" if "LC 227" in linha else "214"
            continue
        m = re.match(r"^\|\s*([a-z0-9-]+)\.md\s*\|\s*([^|]+)\|", linha)
        if not m:
            continue
        intervalos = []
        for parte in m.group(2).split("·"):
            lei = lei_secao
            rotulo_lei = re.match(r"\s*LC (\d+):", parte)
            if rotulo_lei:
                lei, parte = rotulo_lei.group(1), parte[rotulo_lei.end():]
            parte = re.sub(r"\+.*", "", parte).replace("(", " (").split(" (")[0]
            for pedaco in parte.split(","):
                f = re.match(rf"\s*{ROTULO}\s*(?:–|-(?=\d)| a )\s*{ROTULO}\s*$", pedaco)
                s = re.match(rf"\s*{ROTULO}\s*$", pedaco)
                if f:
                    a = re.match(ROTULO, pedaco.strip())
                    b = re.search(rf"{ROTULO}\s*$", pedaco)
                    intervalos.append((lei, _chave_rotulo(a, False), _chave_rotulo(b, True)))
                elif s:
                    intervalos.append((lei, _chave_rotulo(s, False), _chave_rotulo(s, True)))
        if intervalos:
            saida.append(NotaPlano(m.group(1), intervalos[0][0], intervalos))
    return saida


def _art(lista: list[str]) -> str:
    return ("art. " if len(lista) == 1 and " a " not in faixas(lista) else "arts. ") + faixas(lista)


def bloco_nota(arts: dict[str, list[str]], efeitos: dict[str, dict[str, str]]) -> str:
    if not any(arts.values()):
        return ("Nos dois regulamentos, nenhum artigo cita os artigos da lei desta nota. "
                "Ver o [mapa dos regulamentos](_mapa-regulamentos.md).")
    linhas = []
    for reg in ("CBS", "IBS"):
        lista = arts.get(reg, [])
        if not lista:
            linhas.append(f"- {NOME_REG[reg]}: nenhum artigo cita os artigos desta nota.")
            continue
        linhas.append(f"- {NOME_REG[reg]}: {_art(lista)}")
        por_data: dict[str, list[str]] = {}
        for a in lista:
            if a in efeitos.get(reg, {}):
                por_data.setdefault(efeitos[reg][a], []).append(a)
        for data, futuros in sorted(por_data.items()):
            verbo = "produz" if len(futuros) == 1 else "produzem"
            linhas.append(f"  - ⏳ {verbo} efeitos a partir de {data}: {_art(futuros)}")
    linhas.append("")
    linhas.append("Texto por artigo: `fontes/reforma/texto/decreto-12955-2026-artigos.txt` e "
                  "`fontes/reforma/texto/res-cgibs-6-2026-artigos.txt` (procure a linha que começa "
                  "com \"Art. N\"). Como ler e vigência: [mapa dos regulamentos](_mapa-regulamentos.md).")
    return "\n".join(linhas)


def aplicar_bloco(texto: str, conteudo: str) -> str:
    if "<!-- gerado:regulamentos -->" in texto:
        return substituir_bloco(texto, "regulamentos", conteudo)
    secao = (f"{TITULO_SECAO}\n\nArtigos dos regulamentos que citam os artigos da lei "
             f"tratados nesta nota (lista gerada por `scripts/mapa_regulamento.py`; "
             f"a regra da lei prevalece):\n\n<!-- gerado:regulamentos -->\n{conteudo}\n"
             f"<!-- /gerado:regulamentos -->\n")
    m = re.search(r"^## Ligações\b", texto, re.M)
    if m:
        return texto[:m.start()] + secao + "\n" + texto[m.start():]
    return texto.rstrip("\n") + "\n\n" + secao


# --- leitura das fontes -------------------------------------------------------

RUIDO_IBS = [re.compile(p) for p in (
    r"^\d{1,3}$", r"^Comitê Gestor do Imposto sobre Bens e Serviços – CGIBS$")]


def texto_cbs(html: str) -> str:
    from vigencia_planalto import paragrafos_html
    corpo = [t for t, risc, _ in paragrafos_html(html) if t and not risc]
    texto = "\n".join(corpo)
    inicio = texto.find("DECRETA:")
    fim = texto.find("Este texto não substitui")
    return texto[inicio + len("DECRETA:"): fim if fim > 0 else None]


def texto_ibs(txt: str) -> str:
    linhas = [l for l in txt.splitlines() if not any(r.match(l.strip()) for r in RUIDO_IBS)]
    texto = "\n".join(linhas)
    inicio = texto.find("RESOLVE:", texto.find("Regulamenta o Imposto"))
    fim = texto.find("ANEXO I - TAXAS ANUAIS", inicio)  # o sumário também cita o Anexo I
    corpo = texto[inicio + len("RESOLVE:"): fim if fim > 0 else None]
    return re.sub(r"\n\d{3}\s+ITEM REFERÊNCIA NCM.*", "", corpo, flags=re.S)


def texto_por_artigo(artigos: list[Artigo], titulo: str) -> str:
    partes, ctx = [f"# {titulo}", "", "Uma linha por artigo; contexto (Livro > Título > ...) "
                   "antes de cada mudança. Gerado por scripts/mapa_regulamento.py.", ""], None
    for a in artigos:
        if a.contexto != ctx:
            partes += ["", f"## {a.contexto}", ""]
            ctx = a.contexto
        partes.append(a.texto)
    return "\n".join(partes) + "\n"


def gerar_mapa(cabecalho: str, regs: dict[str, list[Artigo]], plano: list[NotaPlano]) -> str:
    inv = {(reg, lei): inverter(arts, lei) for reg, arts in regs.items() for lei in ("214", "227")}
    linhas = [cabecalho.rstrip("\n"), "",
              "<!-- Tabelas geradas por scripts/mapa_regulamento.py. Não editar à mão. -->", "",
              "## Por nota", "",
              "| Nota | Artigos da lei | Regulamento da CBS | Regulamento do IBS |", "|---|---|---|---|"]
    for n in plano:
        arts = {reg: sorted({a for (r, lei), m in inv.items() if r == reg for citado, lista in m.items()
                             if n.contem(citado, lei) for a in lista}, key=chave) for reg in regs}
        rot = "; ".join(f"LC {l}" for l in n.leis())
        linhas.append(f"| [[{n.nota}]] | {rot} | {faixas(arts['CBS'])} | {faixas(arts['IBS'])} |")
    for lei in ("214", "227"):
        citados = sorted({c for reg in regs for c in inv[(reg, lei)]}, key=chave)
        linhas += ["", f"## Por artigo da LC {lei} ({len(citados)} artigos citados)", "",
                   f"| Art. da LC {lei} | Regulamento da CBS | Regulamento do IBS |", "|---|---|---|"]
        for c in citados:
            linhas.append(f"| {c} | {faixas(inv[('CBS', lei)].get(c, []))} | {faixas(inv[('IBS', lei)].get(c, []))} |")
    for reg, arts in regs.items():
        sem = [a for a in arts if not a.leis.get("214") and not a.leis.get("227")]
        linhas += ["", f"## {NOME_REG[reg].replace('**', '')}: artigos sem citação da LC 214 ou 227 ({len(sem)})",
                   "", "Matéria própria do regulamento, citação de outra lei ou disposição final.", "",
                   "| Art. | Onde está | Início do texto |", "|---|---|---|"]
        for a in sem:
            linhas.append(f"| {a.numero} | {a.contexto} | {a.texto[:110].replace('|', '/')}… |")
    return "\n".join(linhas) + "\n"


def blocos_por_nota(regs: dict[str, list[Artigo]], plano: list[NotaPlano]) -> dict[str, str]:
    saida = {}
    for n in plano:
        arts = {}
        for reg, artigos in regs.items():
            arts[reg] = sorted({a.numero for a in artigos for lei, citados in a.leis.items()
                                for c in citados if n.contem(c, lei)}, key=chave)
        saida[n.nota] = bloco_nota(arts, EFEITOS)
    return saida


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    for nome in ("--cbs", "--ibs", "--plano", "--cabecalho", "--mapa", "--textos"):
        p.add_argument(nome, type=Path, required=True)
    p.add_argument("--notas", type=Path)
    a = p.parse_args(argv[1:])
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    regs = {"CBS": dividir_artigos(texto_cbs(a.cbs.read_text(encoding="utf-8"))),
            "IBS": dividir_artigos(texto_ibs(a.ibs.read_text(encoding="utf-8")))}
    (a.textos / "decreto-12955-2026-artigos.txt").write_text(
        texto_por_artigo(regs["CBS"], "Decreto nº 12.955/2026 — Regulamento da CBS"), encoding="utf-8", newline="\n")
    (a.textos / "res-cgibs-6-2026-artigos.txt").write_text(
        texto_por_artigo(regs["IBS"], "Resolução CGIBS nº 6/2026 — Regulamento do IBS"), encoding="utf-8", newline="\n")
    plano = notas_do_plano(a.plano.read_text(encoding="utf-8"))
    a.mapa.write_text(gerar_mapa(a.cabecalho.read_text(encoding="utf-8"), regs, plano),
                      encoding="utf-8", newline="\n")
    for reg, arts in regs.items():
        com = sum(1 for x in arts if x.leis)
        print(f"{reg}: {len(arts)} artigos (de {arts[0].numero} a {arts[-1].numero}), {com} com citação de LC")
    if a.notas:
        for nota, bloco in blocos_por_nota(regs, plano).items():
            arq = a.notas / f"{nota}.md"
            if arq.exists():
                arq.write_text(aplicar_bloco(arq.read_text(encoding="utf-8"), bloco), encoding="utf-8", newline="\n")
        print(f"blocos gravados em {len(plano)} notas do plano")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
