import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import vigencia_receita as vr  # noqa: E402

TEXTO = """07/10/2026, 09:29
Resol. CGSN nº 140-2018
Art. 2º Para fins desta Resolução, considera-se:
IV - empresa em início de atividade aquela que se encontra no período de 180 dias;
IV - empresa em início de atividade aquela que se encontra no período de 60
import_export
(sessenta) dias a partir da data de abertura;
[Redação dada pelo(a) Resolução CGSN nº 150, de 3 de dezembro de
https://normasinternet2.receita.fazenda.gov.br/#/consulta/externa/imprimir/92278/visao/multivigente
3/132
2019] date_range 01/01/2020
[Vide modificação prevista para 01/01/2027, nos termos do(a) Resolução CGSN nº 190, de 4 de agosto de 2026]
V - data de início de atividade a data de abertura constante do CNPJ.
[Vide dispositivo a ser incluído em 01/01/2027, nos termos do(a) Resolução CGSN nº 190, de 4 de agosto de 2026]
file_present Anexo I .pdf
Art. 3º Texto do artigo.
§ 1º Parágrafo revogado.
[Revogado(a) pelo(a) Resolução CGSN nº 183, de 26 de setembro de 2025] date_range 13/10/2025
"""


class TestVigenciaReceita(unittest.TestCase):
    def setUp(self):
        self.bs = vr.blocos(TEXTO, vr.RUIDO_PADRAO)
        self.por = {}
        for b in self.bs:
            self.por.setdefault((b.artigo, b.dispositivo), []).append(b)

    def test_remove_ruido(self):
        tudo = " ".join(b.texto for b in self.bs)
        for lixo in ("import_export", "3/132", "normasinternet2", "file_present", "09:29"):
            self.assertNotIn(lixo, tudo)

    def test_versao_anterior_fica_sem_marcas(self):
        v1, v2 = self.por[("2", "IV")]
        self.assertEqual(v1.marcas, [])
        self.assertIn("180 dias", v1.texto)

    def test_continuacao_de_linha_vai_para_o_mesmo_bloco(self):
        self.assertIn("(sessenta) dias a partir da data de abertura", self.por[("2", "IV")][1].texto)

    def test_marca_quebrada_em_duas_linhas_e_ruido_no_meio(self):
        m = self.por[("2", "IV")][1].marcas[0]
        self.assertEqual((m.tipo, m.ato, m.data), ("redacao", "Res. CGSN 150/2019", "2020-01-01"))

    def test_modificacao_prevista(self):
        m = self.por[("2", "IV")][1].marcas[1]
        self.assertEqual((m.tipo, m.ato, m.data), ("modificacao-prevista", "Res. CGSN 190/2026", "2027-01-01"))

    def test_inclusao_prevista(self):
        m = self.por[("2", "V")][0].marcas[0]
        self.assertEqual((m.tipo, m.data), ("inclusao-prevista", "2027-01-01"))

    def test_revogacao_com_date_range(self):
        m = self.por[("3", "§1º")][0].marcas[0]
        self.assertEqual((m.tipo, m.ato, m.data), ("revogacao", "Res. CGSN 183/2025", "2025-10-13"))

    def test_situacao_modificacao_prevista_futura(self):
        m = vr.Marca("modificacao-prevista", "Res. CGSN 190/2026", "2027-01-01")
        self.assertEqual(vr.situacao(m, "2026-10-07"), "⏳ modificação prevista — a redação atual vale até lá")

    def test_situacao_redacao_passada(self):
        self.assertEqual(vr.situacao(vr.Marca("redacao", "Res. CGSN 150/2019", "2020-01-01"), "2026-10-07"), "vigente")

    def test_situacao_revogacao_passada(self):
        self.assertEqual(vr.situacao(vr.Marca("revogacao", "Res. CGSN 183/2025", "2025-10-13"), "2026-10-07"), "revogado")

    def test_markdown_filtra_por_data_e_mostra_futuras(self):
        md = vr.gerar_markdown("r140.txt", self.bs, "2026-10-07", "2025-01-01")
        self.assertIn("| 2 | IV | modificacao-prevista | Res. CGSN 190/2026 | 01/01/2027 | ⏳ modificação prevista — a redação atual vale até lá |", md)
        self.assertIn("| 3 | §1º | revogacao | Res. CGSN 183/2025 | 13/10/2025 | revogado |", md)
        self.assertNotIn("Res. CGSN 150/2019", md)


class TestMarcaCortada(unittest.TestCase):
    TEXTO = """Art. 2º Texto.
[Incluído(a) pelo(a) Resolução
Art. 2º-A O Simples Nacional deve observar os princípios:
[Incluído(a) pelo(a) Resolução CGSN nº 183, de 26 de setembro de
2025] date_range 13/10/2025
[Incluído(a) pelo(a) Resolução CGSN nº 183, de 26
II - da transparência;
[Incluído(a) pelo(a) Resolução CGSN nº 183, de 26
de setembro de 2025] date_range 13/10/2025
"""

    def test_fragmento_de_marca_nao_engole_o_artigo(self):
        bs = vr.blocos(self.TEXTO, vr.RUIDO_PADRAO)
        chaves = [(b.artigo, b.dispositivo) for b in bs]
        self.assertIn(("2-A", "caput"), chaves)
        self.assertIn(("2-A", "II"), chaves)
        art2a = next(b for b in bs if (b.artigo, b.dispositivo) == ("2-A", "caput"))
        self.assertEqual([(m.tipo, m.data) for m in art2a.marcas], [("inclusao", "2025-10-13")])
        self.assertNotIn("[", " ".join(b.texto for b in bs))


class TestRotulos(unittest.TestCase):
    TEXTO = """Art. 6º A opção será formalizada.
I - inciso do caput;
[Redação dada pelo(a) Resolução CGSN nº 183, de 26 de setembro de 2025] date_range 13/10/2025
§ 2º Parágrafo segundo.
I - inciso do parágrafo;
[Redação dada pelo(a) Resolução CGSN nº 183, de 26 de setembro de 2025] date_range 13/10/2025
a) alínea do inciso;
[Redação dada pelo(a) Resolução CGSN nº 183, de 26 de setembro de 2025] date_range 13/10/2025
Parágrafo único. Texto.
Art. 7º Outro artigo.
II - inciso do caput do art. 7º;
ANEXO VIII MODELO DO COMPROVANTE DE PAGAMENTO
file_present Anexo VIII.pdf ANEXO IX
REGISTRO DE VALORES A RECEBER file_present Anexo IX.pdf ANEXO X
RELATÓRIO MENSAL DE RECEITAS BRUTAS file_present Anexo X .pdf ANEXO XI
OCUPAÇÕES PERMITIDAS AO MEI file_present Anexo XI.pdf file_present Anexo XI.pdf
[Redação dada pelo(a) Resolução CGSN nº 182, de 26 de setembro de 2025] date_range 01/10/2025
"""

    def setUp(self):
        self.chaves = [(b.artigo, b.dispositivo) for b in vr.blocos(self.TEXTO, vr.RUIDO_PADRAO)]

    def test_inciso_do_caput_sem_hifen(self):
        self.assertIn(("6", "I"), self.chaves)

    def test_inciso_de_paragrafo_leva_o_paragrafo(self):
        self.assertIn(("6", "§2º, I"), self.chaves)

    def test_alinea_leva_inciso_e_paragrafo(self):
        self.assertIn(("6", "§2º, I, a)"), self.chaves)

    def test_paragrafo_unico_com_espaco(self):
        self.assertIn(("6", "Parágrafo único"), self.chaves)

    def test_novo_artigo_zera_o_paragrafo(self):
        self.assertIn(("7", "II"), self.chaves)

    def test_anexos_depois_de_file_present_viram_blocos(self):
        bs = vr.blocos(self.TEXTO, vr.RUIDO_PADRAO)
        anexo = [b for b in bs if b.artigo.startswith("Anexo")]
        self.assertEqual([b.artigo for b in anexo], ["Anexo VIII", "Anexo IX", "Anexo X", "Anexo XI"])
        self.assertEqual([m.ato for m in anexo[-1].marcas], ["Res. CGSN 182/2025"])
        self.assertEqual(anexo[0].marcas, [])
        self.assertIn("OCUPAÇÕES PERMITIDAS AO MEI", anexo[-1].texto)
        self.assertNotIn("file_present", " ".join(b.texto for b in bs))


class TestRevogacaoAntiga(unittest.TestCase):
    def test_revogacao_anterior_ao_desde_aparece(self):
        texto = """Art. 97. Declaração anual.
[Revogado(a) pelo(a) Resolução CGSN nº 169, de 27 de abril de 2022] date_range 01/01/2023
Art. 98. Outro.
[Redação dada pelo(a) Resolução CGSN nº 150, de 3 de dezembro de 2019] date_range 01/01/2020
"""
        md = vr.gerar_markdown("r.txt", vr.blocos(texto, vr.RUIDO_PADRAO), "2026-10-07", "2025-01-01")
        self.assertIn("| 97 | caput | revogacao | Res. CGSN 169/2022 | 01/01/2023 | revogado |", md)
        self.assertNotIn("Res. CGSN 150/2019", md)


if __name__ == "__main__":
    unittest.main()
