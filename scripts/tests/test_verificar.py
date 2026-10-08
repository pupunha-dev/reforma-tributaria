import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
import verificar as v  # noqa: E402

FM_OK = (
    "---\n"
    "título: X\n"
    "dominio: simples-nacional\n"
    "fontes: LC 123/2006, art. 1º\n"
    "vigencia: atual\n"
    "texto-base: 2026-10-06\n"
    "---\n\n# X\n"
)


class Base(unittest.TestCase):
    def setUp(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.raiz = Path(self._tmp.name)

    def tearDown(self):
        self._tmp.cleanup()

    def criar(self, caminho, texto=""):
        p = self.raiz / caminho
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(texto, encoding="utf-8")
        return p


class TestLinks(Base):
    def test_wikilink_valido_entre_dominios(self):
        self.criar("notas/reforma/a.md", "ver [[sn-b]]")
        self.criar("notas/simples-nacional/sn-b.md", "ver [[a]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_wikilink_inexistente(self):
        self.criar("notas/reforma/a.md", "ver [[nao-existe]]")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("[[nao-existe]] não encontrado", erros[0])

    def test_wikilink_com_extensao_md_e_erro(self):
        self.criar("notas/reforma/a.md", "ver [[b.md]]")
        self.criar("notas/reforma/b.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("use o nome sem .md", erros[0])

    def test_wikilink_com_alias_e_ancora(self):
        self.criar("notas/reforma/a.md", "[[b|texto]] e [[b#seção]]")
        self.criar("notas/reforma/b.md")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_link_markdown_relativo(self):
        self.criar("LEARNINGS.md", "[x](notas/reforma/a.md) e [y](notas/a.md)")
        self.criar("notas/reforma/a.md")
        erros = v.checar_links(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("notas/a.md", erros[0])

    def test_link_markdown_externo_e_ignorado(self):
        self.criar("notas/reforma/a.md", "[x](https://exemplo.gov.br/lei.md)")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_links_dentro_de_codigo(self):
        self.criar("notas/reforma/a.md", "`[[fantasma]]`\n```\n[x](nada.md)\n```\n")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_ignora_docs_superpowers(self):
        self.criar("docs/superpowers/specs/s.md", "[[fantasma]]")
        self.assertEqual(v.checar_links(self.raiz), [])

    def test_verifica_docs_fora_de_superpowers(self):
        self.criar("docs/procedimento-nova-legislacao.md", "[[fantasma]]")
        self.assertEqual(len(v.checar_links(self.raiz)), 1)


class TestNomesUnicos(Base):
    def test_nome_repetido_em_dominios_diferentes(self):
        self.criar("notas/reforma/aliquotas.md")
        self.criar("notas/simples-nacional/aliquotas.md")
        erros = v.checar_nomes_unicos(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("aliquotas", erros[0])

    def test_index_e_arquivos_de_trabalho_podem_repetir(self):
        for d in ("reforma", "simples-nacional"):
            self.criar(f"notas/{d}/INDEX.md")
            self.criar(f"notas/{d}/_plano-notas.md")
        self.assertEqual(v.checar_nomes_unicos(self.raiz), [])


class TestFrontmatter(Base):
    def nota(self, texto):
        self.criar("notas/simples-nacional/sn-a.md", texto)
        return v.checar_frontmatter(self.raiz)

    def test_nota_completa_passa(self):
        self.assertEqual(self.nota(FM_OK), [])

    def test_campo_ausente(self):
        erros = self.nota(FM_OK.replace("vigencia: atual\n", ""))
        self.assertEqual(len(erros), 1)
        self.assertIn("'vigencia'", erros[0])

    def test_vigencia_invalida(self):
        erros = self.nota(FM_OK.replace("vigencia: atual", "vigencia: futura"))
        self.assertEqual(len(erros), 1)
        self.assertIn("vigencia", erros[0])

    def test_texto_base_com_comentario_e_valido(self):
        texto = FM_OK.replace("texto-base: 2026-10-06", "texto-base: 2026-10-06   # captura")
        self.assertEqual(self.nota(texto), [])

    def test_texto_base_fora_do_formato(self):
        erros = self.nota(FM_OK.replace("2026-10-06", "06/10/2026"))
        self.assertEqual(len(erros), 1)
        self.assertIn("texto-base", erros[0])

    def test_dominio_diferente_da_pasta(self):
        erros = self.nota(FM_OK.replace("dominio: simples-nacional", "dominio: reforma"))
        self.assertEqual(len(erros), 1)
        self.assertIn("dominio", erros[0])

    def test_sem_frontmatter(self):
        erros = self.nota("# só título\n")
        self.assertEqual(len(erros), 1)
        self.assertIn("sem frontmatter", erros[0])

    def test_dominio_legado_reforma_e_isento(self):
        self.criar("notas/reforma/x.md", "---\ntítulo: X\norigem: LC 214\n---\n")
        self.assertEqual(v.checar_frontmatter(self.raiz), [])

    def test_index_e_arquivos_de_trabalho_isentos(self):
        self.criar("notas/simples-nacional/INDEX.md", "# Índice\n")
        self.criar("notas/simples-nacional/_plano-notas.md", "# Plano\n")
        self.assertEqual(v.checar_frontmatter(self.raiz), [])


PLANO = (
    "---\ntítulo: Plano\nstatus: {status}\n---\n"
    "| sn-a.md | 1–2 |\n| sn-b.md | 3 |\n"
    "Ponte: [[simples-nacional-e-mei]]\n"
)


class TestCobertura(Base):
    def dominio(self, status, notas_existentes):
        self.criar("notas/simples-nacional/_plano-notas.md", PLANO.format(status=status))
        for n in notas_existentes:
            self.criar(f"notas/simples-nacional/{n}", FM_OK)
        return v.checar_cobertura(self.raiz)

    def test_tudo_coberto(self):
        self.assertEqual(self.dominio("concluido", ["sn-a.md", "sn-b.md"]), ([], []))

    def test_nota_fora_do_plano_e_erro(self):
        erros, avisos = self.dominio("aprovado", ["sn-a.md", "sn-b.md", "sn-c.md"])
        self.assertEqual(len(erros), 1)
        self.assertIn("sn-c.md", erros[0])
        self.assertEqual(avisos, [])

    def test_planejada_ausente_e_aviso_enquanto_nao_concluido(self):
        erros, avisos = self.dominio("aguardando-aprovacao", ["sn-a.md"])
        self.assertEqual(erros, [])
        self.assertEqual(len(avisos), 1)
        self.assertIn("sn-b.md", avisos[0])

    def test_planejada_ausente_e_erro_quando_concluido(self):
        erros, avisos = self.dominio("concluido", ["sn-a.md"])
        self.assertEqual(len(erros), 1)
        self.assertIn("sn-b.md", erros[0])

    def test_dominio_com_notas_sem_plano(self):
        self.criar("notas/simples-nacional/sn-a.md", FM_OK)
        erros, _ = v.checar_cobertura(self.raiz)
        self.assertEqual(len(erros), 1)
        self.assertIn("_plano-notas.md", erros[0])


class TestMain(Base):
    def test_saida_zero_sem_erros(self):
        self.criar("notas/reforma/a.md", "[[b]]")
        self.criar("notas/reforma/b.md")
        self.criar("notas/reforma/_plano-notas.md", "| a.md |\n| b.md |\n")
        self.assertEqual(v.main(["verificar.py", str(self.raiz)]), 0)

    def test_saida_um_com_erro(self):
        self.criar("notas/reforma/a.md", "[[fantasma]]")
        self.criar("notas/reforma/_plano-notas.md", "| a.md |\n")
        self.assertEqual(v.main(["verificar.py", str(self.raiz)]), 1)


class TestVersaoNT(Base):
    def _nota(self, fontes):
        self.criar("notas/documentos-fiscais/df-x.md",
                   f"---\ntítulo: X\ndominio: documentos-fiscais\nfontes: {fontes}\n"
                   "vigencia: atual\ntexto-base: 2026-10-07\n---\n# X\n")

    def test_fontes_sem_versao_e_erro(self):
        self._nota("NT 2025.002-RTC, seção 6")
        self.assertEqual(len(v.checar_versao_nt(self.raiz)), 1)

    def test_fontes_com_versao_passa(self):
        self._nota("NT 2025.002-RTC v1.52, seção 6")
        self.assertEqual(v.checar_versao_nt(self.raiz), [])

    def test_versao_com_uma_casa_decimal_passa(self):
        self._nota("NT 2027.001 v2.1, seção 3")
        self.assertEqual(v.checar_versao_nt(self.raiz), [])


if __name__ == "__main__":
    unittest.main()
