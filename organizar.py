from pathlib import Path
import argparse

parser = argparse.ArgumentParser(description="Organiza os arquivos de uma pasta por extensão")
parser.add_argument("pasta", help="Caminho da pasta para organizar")
parser.add_argument("--simular", action="store_true", help="mostra o que seria feito, sem mover nada")
args = parser.parse_args()

print(args.pasta)

pasta = Path(args.pasta).expanduser()
if not pasta.is_dir():
    print(f"Erro: '{pasta} não é uma pasta válida")
    raise SystemExit(1)
for item in list(pasta.iterdir()):
    if item.is_file():
        extensao = item.suffix.lower().lstrip(".")
        if  extensao == "":
            extensao = "sem_extensao"

        destino = pasta / extensao
        if (args.simular):
            print(f"[SIMULAÇÃO]: {item.name} -> {extensao}/.")
        elif(destino / item.name).exists():
            print(f"Aviso: {item.name} já existe em {extensao}, ignorado")
        else:
            destino.mkdir(exist_ok=True)
            item.rename(destino / item.name)
            print(f"Movido: {item.name} -> {destino}")