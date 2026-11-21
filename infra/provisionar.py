import json
from pathlib import Path


def provisionar():
    raiz = Path(__file__).resolve().parents[1]
    definicao = json.loads((raiz / "infra" / "ambiente.json").read_text(encoding="utf-8"))
    ambiente = raiz / "ambiente_local"
    ambiente.mkdir(exist_ok=True)
    print(f"Definição do ambiente: {definicao['nome']}")
    for nome in definicao["pastas"]:
        if not nome or Path(nome).name != nome or nome in [".", ".."]:
            raise ValueError("Use nomes simples para as pastas do ambiente.")
        pasta = ambiente / nome
        existia = pasta.is_dir()
        pasta.mkdir(exist_ok=True)
        print(f"{'Mantida' if existia else 'Criada'}: {pasta.name}")
    print("Ambiente local preparado conforme a definição.")


if __name__ == "__main__":
    provisionar()
