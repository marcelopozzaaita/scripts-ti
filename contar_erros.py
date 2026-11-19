contador = 0
with open("sistema.log", "r", encoding="utf-8") as f:
    for linha in f:
        linha = linha.strip()
        if linha != "":
            if "ERROR" in linha:
                contador += 1
print(f"Total de erros: {contador}")