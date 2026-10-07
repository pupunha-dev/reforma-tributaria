import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import ler_lei as ll  # noqa: E402

HTML = """
<p>Art. 18. O valor devido mensalmente.</p>
<p><strike>§ 1º Redação antiga.</strike></p>
<p>§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)</p>
<p>Art. 18-A. O MEI.</p>
<p>ANEXO I</p>
<p>Para os anos-calendário 2027 e 2028</p>
<table><tr><td>1ª Faixa</td><td>Até 180.000,00</td><td>4,00%</td></tr>
<tr><td style="text-decoration: line-through">2ª Faixa</td><td>x</td></tr></table>
<p>A partir de 2029</p>
<table><tr><td>1ª Faixa</td><td>Até 180.000,00</td><td>4,10%</td></tr></table>
<p>ANEXO II</p>
"""


class TestLerLei(unittest.TestCase):
    def setUp(self):
        self.linhas = ll.linearizar(HTML)

    def test_marca_paragrafo_riscado(self):
        self.assertIn("[RISCADO] § 1º Redação antiga.", self.linhas)
        self.assertIn("§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)", self.linhas)

    def test_tabela_vira_linhas_com_celulas(self):
        self.assertIn("| 1ª Faixa | Até 180.000,00 | 4,00% |", self.linhas)

    def test_linha_de_tabela_riscada_por_css(self):
        self.assertIn("[RISCADO] | 2ª Faixa | x |", self.linhas)

    def test_linha_de_tabela_com_risco_so_numa_celula_curta_nao_e_riscada(self):
        html = "<table><tr><td>3ª Faixa</td><td>De 360.000,01 a 720.000,00</td><td><strike>9%</strike></td></tr></table>"
        self.assertEqual(ll.linearizar(html), ["| 3ª Faixa | De 360.000,01 a 720.000,00 | 9% |"])

    def test_tabela_mantem_ordem_com_legenda(self):
        i = self.linhas.index("Para os anos-calendário 2027 e 2028")
        j = self.linhas.index("A partir de 2029")
        self.assertLess(i, self.linhas.index("| 1ª Faixa | Até 180.000,00 | 4,00% |"))
        self.assertLess(j, self.linhas.index("| 1ª Faixa | Até 180.000,00 | 4,10% |"))

    def test_recorta_artigo(self):
        trecho = ll.recortar(self.linhas, r"^Art\. 18\.", r"^Art\. 18-A\.")
        self.assertEqual(trecho[0], "Art. 18. O valor devido mensalmente.")
        self.assertEqual(len(trecho), 3)

    def test_recorta_anexo_ate_o_proximo(self):
        trecho = ll.recortar(self.linhas, r"^ANEXO I$", r"^ANEXO II$")
        self.assertEqual(trecho[-1], "| 1ª Faixa | Até 180.000,00 | 4,10% |")

    def test_recorta_ocorrencia_escolhida(self):
        self.assertEqual(ll.recortar(self.linhas, r"^§ 1º", None, ocorrencia=0)[0], "§ 1º Redação nova. (Redação dada pela Lei Complementar nº 155, de 2016)")


if __name__ == "__main__":
    unittest.main()
