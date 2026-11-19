contagem ={}
try:
    arq = input("Digite o nome do arquivo: ")
    with open(arq, "r", encoding="utf-8") as f:
        for linha in f:
            linha = linha.strip()
            if linha != "":
                partes = linha.split()
                if len(partes) >= 3:
                    nivel = partes[2]
                    contagem[nivel] = contagem.get(nivel, 0) + 1
except FileNotFoundError:
    print(f"Erro: o arquivo {arq} não foi encontrado.")
for nivel, quantidade in contagem.items():
    print(f"{nivel}: {quantidade}")        
with open("relatorios.txt", "w", encoding="utf-8") as f:
    f.write("Relatorio de log\n")
    for nivel, quantidade in contagem.items():
        f.write(f"{nivel}: {quantidade}\n")