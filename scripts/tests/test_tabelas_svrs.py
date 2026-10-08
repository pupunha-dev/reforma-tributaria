import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import tabelas_svrs as cs  # noqa: E402


def _classif(cod, nome="Situação X", ibs=0.0, cbs=0.0, fim=None, **extra):
    base = {
        "CodClassTrib": cod, "NomeClassTrib": nome, "PercRedIbs": ibs, "PercRedCbs": cbs,
        "DthIniVig": "2025-05-05T00:00:00", "DthFimVig": fim, "DthPublicacao": "2026-06-22T00:00:00",
        "TipoAliq": 2, "IndTribRegular": False, "IndPermiteCredPres": False,
        "IndEstornoCred": False, "IndNfe": True, "IndNfce": False, "TexUrlLegislacao": "https://x/lcp214.htm#art1",
        "NroAnexo": None, "Anexos": [], "TexRegCbs": "Art. 1", "TexRegIbs": "Art. 1",
    }
    base.update(extra)
    return base


def _cst(cod, nome, classif, **flags):
    base = {"Cst": cod, "NomeCst": nome, "IndExigeTrib": True, "IndMonofasica": False,
            "IndReducaoAliq": False, "IndDiferimento": False, "IndReducaoBc": False,
            "IndTransferenciaCred": False, "IndCredPresIbsZfm": False, "IndAjusteCompet": False,
            "DthIniVig": "2025-05-01T00:00:00", "DthFimVig": None, "ClassificacoesTributarias": classif}
    base.update(flags)
    return base


DADOS = [
    _cst("000", "Tributação integral", [_classif("000001", "Tributação integral do IBS e CBS.")]),
    _cst("200", "Alíquota reduzida", [
        _classif("200003", "Vendas de bens", ibs=60.0, cbs=60.0, IndNfce=True),
        _classif("200010", "Redução parcial", ibs=60.0, cbs=100.0),
        _classif("220001", "Fixa antiga", fim="2026-01-01T00:00:00"),
    ], IndReducaoAliq=True),
]


def _html(dados):
    return ("<script>\n$(function(){\n  var dadosOriginais = "
            + json.dumps(dados, ensure_ascii=False) + ";\n  var outro = 1;\n});</script>")


class TestExtrairDados(unittest.TestCase):
    def test_le_o_json_embutido(self):
        self.assertEqual(cs.extrair_dados(_html(DADOS)), DADOS)

    def test_sem_variavel_e_erro(self):
        with self.assertRaises(ValueError):
            cs.extrair_dados("<html>sem dados</html>")


class TestFormatacao(unittest.TestCase):
    def test_percentual_inteiro(self):
        self.assertEqual(cs.pct(60.0), "60%")
        self.assertEqual(cs.pct(0.0), "0%")

    def test_percentual_com_decimal_usa_virgula(self):
        self.assertEqual(cs.pct(37.5), "37,5%")

    def test_documentos_listados_em_ordem(self):
        c = _classif("200003", IndNfe=True, IndNfce=True, IndNfse=True)
        self.assertEqual(cs.documentos(c), "NFe, NFCe, NFSE")

    def test_vigencia_sem_fim(self):
        self.assertEqual(cs.vigencia(_classif("1")), "05/05/2025 em diante")

    def test_vigencia_com_fim(self):
        self.assertEqual(cs.vigencia(_classif("1", fim="2026-01-01T00:00:00")),
                         "05/05/2025 a 01/01/2026")


class TestMarkdown(unittest.TestCase):
    def setUp(self):
        self.md = cs.gerar_markdown(DADOS, "2026-10-08", cs.URL)

    def test_cabecalho_com_origem_e_data(self):
        self.assertIn(cs.URL, self.md)
        self.assertIn("2026-10-08", self.md)

    def test_tabela_cst(self):
        self.assertIn("| 000 | Tributação integral |", self.md)
        self.assertIn("| 200 | Alíquota reduzida |", self.md)

    def test_linhas_de_classificacao_com_percentuais(self):
        self.assertIn("| 200003 | Vendas de bens | 60% | 60% |", self.md)
        self.assertIn("| 200010 | Redução parcial | 60% | 100% |", self.md)

    def test_classificacao_encerrada_aparece_com_fim(self):
        self.assertIn("05/05/2025 a 01/01/2026", self.md)

    def test_url_com_quebra_de_linha_nao_quebra_a_tabela(self):
        dados = [_cst("000", "X", [_classif("000001", TexUrlLegislacao="https://x/lcp214.htm#art1\r\n")])]
        md = cs.gerar_markdown(dados, "2026-10-08", cs.URL)
        linha = [l for l in md.splitlines() if l.startswith("| 000001")]
        self.assertEqual(len(linha), 1)
        self.assertTrue(linha[0].endswith("#art1 |"))

    def test_conta_totais(self):
        self.assertIn("2 CST", self.md)
        self.assertIn("4 cClassTrib", self.md)


class TestConferirNota(unittest.TestCase):
    def test_codigo_existente_passa(self):
        nota = "| 200003 | texto |\nUse `000001` aqui."
        self.assertEqual(cs.faltantes(nota, DADOS), [])

    def test_codigo_inexistente_em_tabela_e_em_crase(self):
        nota = "| 299999 | texto |\nUse `288888` aqui."
        self.assertEqual(cs.faltantes(nota, DADOS), ["288888", "299999"])

    def test_numero_solto_de_seis_digitos_e_ignorado(self):
        self.assertEqual(cs.faltantes("CEP 123456 e protocolo 654321", DADOS), [])

    def test_ignora_frontmatter_e_exemplo(self):
        nota = "---\nfontes: `999999`\n---\n<!-- exemplo -->`888888`<!-- /exemplo -->\n"
        self.assertEqual(cs.faltantes(nota, DADOS), [])


class TestNota(unittest.TestCase):
    def test_tabela_cst_resumida(self):
        md = cs.tabela_cst_nota(DADOS)
        self.assertIn("| 000 | Tributação integral | Exige tributação | 1 |", md)
        self.assertIn("| 200 | Alíquota reduzida | Exige tributação, Redução de alíquota | 3 |", md)

    def test_tabelas_por_cst_com_simples(self):
        dados = [_cst("200", "Alíquota reduzida", [_classif("200003", "Vendas", ibs=60.0, cbs=60.0, TipoRbSn=9)])]
        md = cs.tabelas_classif_nota(dados)
        self.assertIn("### CST 200 — Alíquota reduzida", md)
        self.assertIn("| 200003 | Vendas | 60% | 60% | Padrão | 05/05/2025 em diante | NFe | "
                      "9 Incompatível com SN |", md)

    def test_substitui_so_o_bloco_marcado(self):
        texto = "antes\n<!-- gerado:cst -->\nvelho\n<!-- /gerado:cst -->\ndepois\n"
        novo = cs.substituir_bloco(texto, "cst", "NOVO")
        self.assertEqual(novo, "antes\n<!-- gerado:cst -->\nNOVO\n<!-- /gerado:cst -->\ndepois\n")

    def test_bloco_vazio_e_preenchido(self):
        texto = "<!-- gerado:cst -->\n<!-- /gerado:cst -->\n"
        self.assertEqual(cs.substituir_bloco(texto, "cst", "NOVO"),
                         "<!-- gerado:cst -->\nNOVO\n<!-- /gerado:cst -->\n")

    def test_bloco_ausente_e_erro(self):
        with self.assertRaises(ValueError):
            cs.substituir_bloco("sem marcadores", "cst", "x")


def _detalhe(cod, ibs, cbs, nfe="Sim", dfe="Não", evento="Sim"):
    def trib(nome, rotulo, partes):
        if partes is None:
            return (f'<h6>{nome} ({rotulo})</h6><p><small class="text-muted">Aplicável:</small>'
                    '<span>N&#227;o</span></p>')
        ini, fim = partes
        return (f'<h6>{nome} ({rotulo})</h6><p><small class="text-muted">Aplicável:</small>'
                f'<span>Sim</span></p><p><small class="text-muted">Início Vigência:</small>\n{ini}  </p>'
                f'<p><small class="text-muted">Fim Vigência:</small><span>{fim}</span></p>')
    return (
        f'<tr class="credito-row" data-codigo="{cod}"><td>{cod}</td><td>resumo</td></tr>\n'
        f'<tr id="detail-{cod}" style="display: none;"><td colspan="11">'
        f'<h4>Detalhes do Crédito Presumido {cod}</h4>'
        f'<p><small class="text-muted">Código:</small> {cod}</p>'
        f'<p><small class="text-muted">Descrição:</small> Cr&#233;dito presumido do art. {cod}.</p>'
        '<h6><strong>Configurações:</strong></h6>'
        f'<p><small class="text-muted">Apropria DFE:</small><span>{dfe}</span></p>'
        f'<p><small class="text-muted">Apropria Evento:</small><span>{evento}</span></p>'
        '<p><small class="text-muted">Deduz Crédito Presumido:</small><span>Não</span></p>'
        '<p><small class="text-muted">Declaração de Pagamento:</small><span>Sim</span></p>'
        f'<p><small class="text-muted">NFe:</small><span>{nfe}</span></p>'
        '<p><small class="text-muted">NFCe:</small><span>N&#227;o</span></p>'
        '<p><small class="text-muted">CTe:</small><span>N&#227;o</span></p>'
        '<p><small class="text-muted">NFSe:</small><span>Sim</span></p>'
        '<h6><strong>Vigência dos Tributos:</strong></h6>'
        + trib("IBS", "Imposto sobre Bens e Serviços", ibs)
        + trib("CBS", "Contribuição sobre Bens e Serviços", cbs)
        + "</td></tr>\n"
    )


HTML_CREDPRES = ('<tbody id="tableBody">'
                 + _detalhe(1, ("01/01/2027", "Indeterminado"), ("01/01/2027", "Indeterminado"))
                 + _detalhe(5, None, ("01/01/2027", "Indeterminado"), dfe="Sim", evento="Não")
                 + _detalhe(8, ("Não informado", "Indeterminado"), None)
                 + "</tbody>")


class TestCredPres(unittest.TestCase):
    def setUp(self):
        self.itens = cs.extrair_ccredpres(HTML_CREDPRES)

    def test_le_um_item_por_linha_de_detalhe(self):
        self.assertEqual([i["codigo"] for i in self.itens], [1, 5, 8])

    def test_descricao_sem_entidades_html(self):
        self.assertEqual(self.itens[0]["descricao"], "Crédito presumido do art. 1.")

    def test_configuracoes(self):
        i = self.itens[1]
        self.assertEqual((i["apropria_dfe"], i["apropria_evento"], i["deduz"], i["declaracao_pagamento"]),
                         (True, False, False, True))
        self.assertEqual(i["documentos"], ["NFe", "NFSe"])

    def test_vigencia_por_tributo(self):
        self.assertEqual(self.itens[0]["ibs"], {"aplicavel": True, "inicio": "01/01/2027", "fim": "Indeterminado"})
        self.assertEqual(self.itens[1]["ibs"], {"aplicavel": False, "inicio": None, "fim": None})
        self.assertEqual(self.itens[2]["ibs"]["inicio"], "Não informado")

    def test_sem_linhas_de_detalhe_e_erro(self):
        with self.assertRaises(ValueError):
            cs.extrair_ccredpres("<html>nada</html>")

    def test_markdown(self):
        md = cs.markdown_ccredpres(self.itens, "2026-10-08", cs.URL_CCREDPRES)
        self.assertIn(cs.URL_CCREDPRES, md)
        self.assertIn("3 códigos", md)
        self.assertIn("| 1 | Crédito presumido do art. 1. | Não | Sim | Não | Sim | NFe, NFSe | "
                      "01/01/2027 em diante | 01/01/2027 em diante |", md)
        self.assertIn("| não se aplica |", md)
        self.assertIn("início não informado", md)


if __name__ == "__main__":
    unittest.main()
