from pathlib import Path
import subprocess
import os
import sys
import unittest


AMBIENTE = os.environ.copy()
AMBIENTE["PYTHONUTF8"] = "1"
PROGRAMA = Path(__file__).resolve().parents[1] / "media.py"


class TesteFuncional(unittest.TestCase):
    def test_usuario_digita_duas_notas(self):
        processo = subprocess.run(
            [sys.executable, str(PROGRAMA)],
            input="6\n8\n", text=True, capture_output=True, encoding="utf-8", env=AMBIENTE,
        )
        self.assertEqual(processo.returncode, 0, processo.stderr)
        self.assertIn("Primeira nota:", processo.stdout)
        self.assertIn("Segunda nota:", processo.stdout)
        self.assertIn("Média: 7", processo.stdout)

    def test_entrada_invalida(self):
        processo = subprocess.run(
            [sys.executable, str(PROGRAMA)],
            input="abc\n", text=True, capture_output=True, encoding="utf-8", env=AMBIENTE,
        )
        self.assertEqual(processo.returncode, 1)
        self.assertIn("Não foi possível calcular", processo.stdout)
