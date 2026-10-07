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

    def test_risco_so_no_link_nao_marca_o_paragrafo(self):
        html = ('<p>Art. 517. A Lei Complementar nº 123 passa a vigorar com as seguintes alterações: '
                '<a href="Lcp214.htm#art544"><strike>Produção de efeitos</strike></a></p>')
        self.assertFalse(vp.paragrafos_html(html)[0][1])

    def test_risco_na_maior_parte_marca_o_paragrafo(self):
        html = '<p><strike>§ 1º Redação antiga e longa do dispositivo.</strike> (Vide LC)</p>'
        self.assertTrue(vp.paragrafos_html(html)[0][1])

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


HTML_REVISAO = """
<p>Art. 18-A. O MEI poderá optar.</p>
<p>V – texto do inciso. (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art544-3">Produção de efeitos</a></p>
<p>d) alínea d. (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art517">x</a> <a href="Lcp214.htm#art544-3">Produção de efeitos</a> <a href="Lcp214.htm#art543">y</a> <a href="Lcp214.htm#art544-5">Produção de efeitos</a></p>
<p>e) alínea e. (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art517">x</a> <a href="Lcp214.htm#art544-3">Produção de efeitos</a> <a href="Lcp214.htm#art543">y</a> <a href="Lcp214.htm#art544-5">Produção de efeitos</a></p>
<table><tr><td><p>0,50%</td><td><p>ANEXO II DA LEI COMPLEMENTAR (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art519">Produção de efeitos</a></p></td></tr></table>
<p>Anexo VII (Vide Lei Complementar nº 214, de 2025) <a href="Lcp214.htm#art520">Produção de efeitos</a></p>
"""

TSV_REVISAO = """Lcp214.htm#art544-3\t2027-01-01\tLC 214, art. 544, III
Lcp214.htm#art544-5\t2033-01-01\tLC 214, art. 544, V
Lcp214.htm#art517\t2027-01-01\tLC 214, art. 544, III (art. 517)
Lcp214.htm#art519\t2027-01-01\tLC 214, art. 544, III (art. 519)
Lcp214.htm#art520\t2027-01-01\tLC 214, art. 544, III (art. 520)\tinclusao
Lcp214.htm#art543\t2033-01-01\tLC 214, art. 544, V (art. 543)\trevogacao
Lcp214.htm#art543@18-A|d)\t-\tart. 543 revoga só a alínea e\tignorar
Lcp214.htm#art544-5@18-A|d)\t-\tart. 543 revoga só a alínea e\tignorar
"""


class TestAchadosDaRevisao(unittest.TestCase):
    def setUp(self):
        self.pars = vp.paragrafos_html(HTML_REVISAO)
        self.linhas, _ = vp.mapear(self.pars, vp.ler_ancoras(TSV_REVISAO), "2026-10-06")

    def linhas_de(self, artigo, dispositivo):
        return [l for l in self.linhas if (l.artigo, l.dispositivo) == (artigo, dispositivo)]

    def test_paragrafo_sem_fechamento_nao_engole_o_titulo_seguinte(self):
        self.assertTrue(any(t.startswith("ANEXO II") for t, _, _ in self.pars))
        self.assertEqual(len(self.linhas_de("Anexo II", "cabecalho")), 1)

    def test_anexo_em_caixa_mista(self):
        self.assertEqual(len(self.linhas_de("Anexo VII", "cabecalho")), 1)

    def test_natureza_inclusao_da_ancora(self):
        self.assertEqual(self.linhas_de("Anexo VII", "cabecalho")[0].situacao,
                         "⏳ futura — dispositivo ainda não vale")

    def test_inciso_com_travessao(self):
        self.assertEqual(len(self.linhas_de("18-A", "V-")), 1)

    def test_vide_sem_redacao_nova_e_o_texto_vigente(self):
        self.assertEqual(
            self.linhas_de("18-A", "V-")[0].situacao,
            "vigente — alteração prevista para 01/01/2027 (texto novo ainda não compilado; ver lei alteradora)",
        )

    def test_paragrafo_com_duas_datas_gera_uma_linha_por_data(self):
        datas = sorted((l.data, l.situacao) for l in self.linhas_de("18-A", "e)"))
        self.assertEqual([d for d, _ in datas], ["2027-01-01", "2033-01-01"])
        self.assertEqual(datas[1][1], "⏳ revogação futura — dispositivo ainda vale")

    def test_natureza_ignorar_descarta_link_divergente(self):
        self.assertEqual([l.data for l in self.linhas_de("18-A", "d)")], ["2027-01-01"])


if __name__ == "__main__":
    unittest.main()
