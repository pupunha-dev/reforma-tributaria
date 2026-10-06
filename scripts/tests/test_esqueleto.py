import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import esqueleto as e  # noqa: E402

AMOSTRA = """06/10/2026, 14:50

Lcp 123

Art. 1º Esta Lei Complementar estabelece normas gerais.

Art. 3º Para os efeitos desta Lei Complementar, consideram-se microempresas:

§ 1º Considera-se receita bruta o produto da venda.

§ 1º Considera-se receita bruta o produto da venda e as demais receitas. (Redação dada pela Lei Complementar nº 214, de 2025) Produção de efeitos

2/44

https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm

V - cujo sócio seja administrador;

V - cujo sócio de fato seja administrador; (Redação dada pela Lei Complementar nº 214, de
2025) Produção de efeitos

CAPÍTULO IV

Art. 18-A. O Microempreendedor Individual poderá optar. (Incluído pela Lei Complementar nº 128, de 2008)

ANEXO I DA LEI COMPLEMENTAR No 123

ANEXO I DA LEI COMPLEMENTAR No 123 (Redação dada pela Lei Complementar nº 155, de 2016) Produção de efeito
"""


class TestEsqueleto(unittest.TestCase):
    def setUp(self):
        self.blocos = e.paragrafos(AMOSTRA, e.RUIDO_PADRAO + [r"^Lcp 123$"])
        self.artigos, self.registros = e.analisar(self.blocos)
        self.por_chave = {(r.artigo, r.dispositivo): r for r in self.registros}

    def test_remove_ruido_de_impressao(self):
        texto = "\n".join(self.blocos)
        self.assertNotIn("06/10/2026, 14:50", texto)
        self.assertNotIn("2/44", texto)
        self.assertNotIn("planalto.gov.br", texto)
        self.assertNotIn("Lcp 123", texto)

    def test_junta_linhas_quebradas_do_mesmo_paragrafo(self):
        self.assertIn(
            "V - cujo sócio de fato seja administrador; (Redação dada pela "
            "Lei Complementar nº 214, de 2025) Produção de efeitos",
            self.blocos,
        )

    def test_lista_artigos_unicos_em_ordem(self):
        self.assertEqual(self.artigos, ["1", "3", "18-A"])

    def test_detecta_redacao_anterior_e_nova_do_mesmo_dispositivo(self):
        self.assertEqual(self.por_chave[("3", "§1º")].versoes, 2)
        self.assertEqual(self.por_chave[("3", "V-")].versoes, 2)

    def test_marca_producao_de_efeitos_sem_data(self):
        r = self.por_chave[("3", "§1º")]
        self.assertEqual(r.tipos, ["redacao", "efeitos-sem-data"])
        self.assertEqual(r.lei, "LC 214/2025")

    def test_inclusao_sem_redacao_anterior_tem_uma_versao(self):
        r = self.por_chave[("18-A", "caput")]
        self.assertEqual(r.tipos, ["inclusao"])
        self.assertEqual(r.versoes, 1)
        self.assertEqual(r.lei, "LC 128/2008")

    def test_anexo_repetido_conta_como_segunda_versao(self):
        r = self.por_chave[("Anexo I", "cabecalho")]
        self.assertEqual(r.versoes, 2)
        self.assertEqual(r.lei, "LC 155/2016")

    def test_so_registra_blocos_com_marca(self):
        self.assertEqual(len(self.registros), 4)

    def test_gera_markdown_com_resumo_e_tabela(self):
        md = e.gerar_markdown("amostra.txt", self.artigos, self.registros)
        self.assertIn("Artigos únicos encontrados: 3", md)
        self.assertIn("Último artigo: 18-A", md)
        self.assertIn("Dispositivos com mais de uma redação no texto: 3", md)
        self.assertIn("| 3 | §1º | 2 | redacao, efeitos-sem-data | LC 214/2025 |", md)


if __name__ == "__main__":
    unittest.main()
