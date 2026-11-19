with open("sistema.log", "r", encoding="utf-8") as f:
    for linha in f:
        print(linha.strip())