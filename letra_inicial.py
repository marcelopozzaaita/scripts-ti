def letra_inicial(pessoas):
    nome_a = []
    for nome in pessoas:
        if nome.lower().startswith("a"):
            nome_a.append(nome)

    return nome_a

nomes = ["Marcelo", "Anna", "Alice", "Matheus", "Sofia", "amanda"]
nomes_a = letra_inicial(nomes)
print(nomes_a)