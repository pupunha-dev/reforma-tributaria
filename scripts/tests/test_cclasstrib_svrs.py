import json
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import cclasstrib_svrs as cs  # noqa: E402


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


if __name__ == "__main__":
    unittest.main()
