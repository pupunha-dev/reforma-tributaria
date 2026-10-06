import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import vigencia_planalto as vp  # noqa: E402

HTML = """
<p>Vigência (Vide <a href="Lcp214.htm#art544-3">Produção de efeitos</a>)</p>
<p>Art. 3º Para os efeitos desta Lei Complementar:</p>
<p><strike>§ 1º Considera-se receita bruta o produto da venda.</strike></p>
<p>§ 1º Considera-se receita bruta e demais receitas. (Redação dada pela Lei Complementar nº 214, de 2025)
<a href="../LCP/Lcp214.htm#art544-2">Produção de efeitos</a></p>
<p>V - cujo sócio seja administrador;</p>
<p>V - cujo sócio de fato seja administrador; (Redação dada pela Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art544-3">Produção de efeitos</a></p>
<p>XII - que tenha filial no exterior. (Incluído pela Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art544-3">Produção de efeitos</a></p>
<p>Art. 31. As alterações de que trata o art. 30:</p>
<p>§ 4o No caso de exclusão do Simples Nacional. (Vide Lei Complementar nº 227, de 2026) <a href="Lcp227.htm#art181">Vigência</a></p>
<p>Art. 41. Texto.</p>
<p>VI - atividade antiga. (Incluído pela Lei Complementar nº 147, de 2014) (Vide Lei Complementar nº 227, de 2026) <a href="Lcp227.htm#art181">x</a></p>
<p>Art. 33. A competência para fiscalizar. (Redação dada pela Lei Complementar nº 227, de 2026) <a href="Lcp227.htm#art168">x</a></p>
<p><strike>II - na declaração a que se refere o art. 25. (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art544-3">Produção de efeitos</a></strike></p>
<p>Art. 40. Texto com <a href="Lcp155.htm#art11">Produção de efeito</a></p>
"""

TSV = """# chave\tdata\tfundamento
Lcp214.htm#art544-2\t2025-01-01\tLC 214, art. 544, II
Lcp214.htm#art544-3\t2027-01-01\tLC 214, art. 544, III
Lcp227.htm#art168\t2026-01-13\tLC 227, art. 182, III
Lcp227.htm#art181\t2033-01-01\tLC 227, art. 181, IV, d\trevogacao
Lcp227.htm#art181@31|§4º\t2026-11-30\tLC 227, art. 181, IV, c\trevogacao
"""


class TestVigenciaPlanalto(unittest.TestCase):
    def setUp(self):
        self.ancoras = vp.ler_ancoras(TSV)
        self.linhas, self.nao_mapeadas = vp.mapear(vp.paragrafos_html(HTML), self.ancoras, "2026-10-06")
        self.por_chave = {(l.artigo, l.dispositivo): l for l in self.linhas}

    def test_le_ancoras_ignorando_comentarios(self):
        self.assertEqual(len(self.ancoras), 5)
        self.assertEqual(self.ancoras["Lcp214.htm#art544-2"], ("2025-01-01", "LC 214, art. 544, II", "alteracao"))
        self.assertEqual(self.ancoras["Lcp227.htm#art181"][2], "revogacao")

    def test_paragrafo_html_normaliza_link_e_detecta_risco(self):
        pars = vp.paragrafos_html(HTML)
        self.assertIn("Lcp214.htm#art544-2", pars[3][2])
        self.assertTrue(pars[2][1])
        self.assertFalse(pars[3][1])

    def test_ignora_paragrafo_antes_do_primeiro_artigo(self):
        self.assertNotIn("", {l.artigo for l in self.linhas})

    def test_redacao_ja_vigente(self):
        l = self.por_chave[("3", "§1º")]
        self.assertEqual((l.data, l.fundamento, l.situacao), ("2025-01-01", "LC 214, art. 544, II", "vigente"))
        self.assertEqual(l.lei, "LC 214/2025")

    def test_redacao_futura_mantem_a_anterior(self):
        self.assertEqual(self.por_chave[("3", "V-")].situacao, "⏳ futura — redação anterior ainda vale")

    def test_inclusao_futura(self):
        self.assertEqual(self.por_chave[("3", "XII-")].situacao, "⏳ futura — dispositivo ainda não vale")

    def test_ancora_especifica_por_dispositivo_tem_prioridade(self):
        l = self.por_chave[("31", "§4º")]
        self.assertEqual(l.data, "2026-11-30")
        self.assertEqual(l.situacao, "⏳ revogação futura — dispositivo ainda vale")

    def test_natureza_revogacao_da_ancora_prevalece_sobre_marca_antiga(self):
        l = self.por_chave[("41", "VI-")]
        self.assertEqual(l.data, "2033-01-01")
        self.assertEqual(l.situacao, "⏳ revogação futura — dispositivo ainda vale")
        self.assertIn("revogacao", l.tipos)

    def test_caput_alterado_pela_lc227(self):
        l = self.por_chave[("33", "caput")]
        self.assertEqual((l.data, l.situacao, l.lei), ("2026-01-13", "vigente", "LC 227/2026"))

    def test_paragrafo_riscado_e_superado(self):
        self.assertEqual(self.por_chave[("33", "II-")].situacao, "superado (riscado no Planalto)")

    def test_ancora_nao_mapeada_e_contada(self):
        self.assertEqual(dict(self.nao_mapeadas), {"Lcp155.htm#art11": 1})
        self.assertNotIn(("40", "caput"), self.por_chave)

    def test_gera_tabela_markdown(self):
        md = vp.gerar_markdown("lcp123.htm", self.linhas, self.nao_mapeadas, "2026-10-06")
        self.assertIn("| Artigo | Dispositivo | Tipo | Lei | Efeitos a partir de | Fundamento | Situação em 06/10/2026 |", md)
        self.assertIn("| 3 | §1º | redacao, efeitos-sem-data | LC 214/2025 | 01/01/2025 | LC 214, art. 544, II | vigente |", md)
        self.assertIn("Lcp155.htm#art11 (1)", md)


if __name__ == "__main__":
    unittest.main()
