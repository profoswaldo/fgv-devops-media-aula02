import json
import os
import shutil
from pathlib import Path
import subprocess
import sys
from tempfile import TemporaryDirectory
from zipfile import ZipFile, ZIP_DEFLATED


RAIZ = Path(__file__).resolve().parent


def executar_pipeline():
    # Uma falha nos testes encerra o fluxo antes da construção.
    print("ETAPA 1 - Executar testes", flush=True)
    ambiente = os.environ.copy()
    ambiente["PYTHONUTF8"] = "1"
    resultado = subprocess.run(
        [sys.executable, "-m", "unittest", "discover", "-s", "testes", "-v"],
        cwd=RAIZ, env=ambiente,
    )
    if resultado.returncode != 0:
        print("PIPELINE REPROVADO - Corrija os testes antes de construir.", flush=True)
        print("Um artefato de uma execução anterior pode continuar em dist.", flush=True)
        return resultado.returncode

    print("ETAPA 2 - Construir o artefato aprovado", flush=True)
    destino = RAIZ / "dist"
    destino.mkdir(exist_ok=True)
    artefato = destino / "media_aprovada.zip"
    with TemporaryDirectory(dir=destino) as pasta:
        temporario = Path(pasta) / artefato.name
        with ZipFile(temporario, "w", compression=ZIP_DEFLATED) as pacote:
            for nome in ["media.py", "notas.json", "COMO_EXECUTAR.txt"]:
                pacote.write(RAIZ / nome, arcname=nome)
            commit = "execucao-local"
            if shutil.which("git"):
                revisao = subprocess.run(
                    ["git", "rev-parse", "HEAD"], cwd=RAIZ, capture_output=True, text=True,
                )
                if revisao.returncode == 0:
                    commit = revisao.stdout.strip()
            metadados = {"testes": "aprovados", "commit": commit}
            pacote.writestr("versao.json", json.dumps(metadados, indent=2))
        temporario.replace(artefato)

    print(f"PIPELINE APROVADO - Artefato criado em {artefato}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(executar_pipeline())
