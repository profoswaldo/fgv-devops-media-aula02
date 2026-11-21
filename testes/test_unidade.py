import unittest
from media import calcular_media


class TesteUnidade(unittest.TestCase):
    def test_media_de_6_e_8(self):
        self.assertEqual(calcular_media(6, 8), 7)

    def test_notas_iguais(self):
        self.assertEqual(calcular_media(5, 5), 5)

    def test_notas_zero(self):
        self.assertEqual(calcular_media(0, 0), 0)
