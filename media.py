import argparse
import json
from pathlib import Path


def calcular_media(primeira, segunda):
    return (primeira + segunda) / 2


def calcular_media_do_arquivo(caminho):
    notas = json.loads(Path(caminho).read_text(encoding="utf-8"))
    return calcular_media(notas["primeira"], notas["segunda"])


def main():
    parser = argparse.ArgumentParser(description="Calcula a média de duas notas.")
    parser.add_argument("--arquivo", help="Arquivo JSON com as duas notas.")
    argumentos = parser.parse_args()

    try:
        if argumentos.arquivo:
            resultado = calcular_media_do_arquivo(argumentos.arquivo)
        else:
            primeira = float(input("Primeira nota: ").replace(",", "."))
            segunda = float(input("Segunda nota: ").replace(",", "."))
            resultado = calcular_media(primeira, segunda)
    except (ValueError, TypeError, KeyError, OSError) as erro:
        print(f"Não foi possível calcular a média: {erro}")
        return 1

    print(f"Média: {resultado:g}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
