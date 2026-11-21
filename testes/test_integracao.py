import json
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest
from media import calcular_media_do_arquivo


class TesteIntegracao(unittest.TestCase):
    def test_leitura_do_arquivo_e_calculo(self):
        with TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "notas.json"
            arquivo.write_text(json.dumps({"primeira": 6, "segunda": 8}), encoding="utf-8")
            self.assertEqual(calcular_media_do_arquivo(arquivo), 7)

    def test_arquivo_sem_segunda_nota(self):
        with TemporaryDirectory() as pasta:
            arquivo = Path(pasta) / "notas.json"
            arquivo.write_text('{"primeira": 6}', encoding="utf-8")
            with self.assertRaises(KeyError):
                calcular_media_do_arquivo(arquivo)
