import argparse
from pathlib import Path
import subprocess
import sys
from tempfile import mkdtemp
from zipfile import ZipFile


def main():
    parser = argparse.ArgumentParser(description="Simulação local de entrega e implantação.")
    parser.add_argument("modo", choices=["manual", "automatico"])
    argumentos = parser.parse_args()
    raiz = Path(__file__).resolve().parent

    # O mesmo fluxo de testes e construção aprova a versão antes da publicação.
    resultado = subprocess.run([sys.executable, str(raiz / "pipeline.py")], cwd=raiz)
    if resultado.returncode != 0:
        print("PUBLICAÇÃO INTERROMPIDA - A versão atual não passou nos testes.")
        return resultado.returncode

    if argumentos.modo == "manual":
        aprovacao = input("Artefato pronto. Digite PUBLICAR para aprovar: ")
        if aprovacao.strip() != "PUBLICAR":
            print("Entrega preparada. Publicação aguardando uma decisão.")
            return 0

    # Cada publicação entra em uma pasta nova para preservar as demonstrações anteriores.
    publicacoes = raiz / "publicacoes" / argumentos.modo
    publicacoes.mkdir(parents=True, exist_ok=True)
    pasta = Path(mkdtemp(prefix="versao_", dir=publicacoes))
    with ZipFile(raiz / "dist" / "media_aprovada.zip") as pacote:
        pacote.extractall(pasta)
    print(f"SIMULAÇÃO LOCAL - Aplicação publicada em {pasta}")
    print("Conferência da versão publicada", flush=True)
    return subprocess.run(
        [sys.executable, str(pasta / "media.py"), "--arquivo", str(pasta / "notas.json")], cwd=pasta,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
