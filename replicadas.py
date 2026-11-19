def tira_duplicadas(lista):
    sem_repeticao = []
    for val in lista:
        if (val not in sem_repeticao):
            sem_repeticao.append(val)
    print(f"Lista sem repetição: {sem_repeticao}")

lista = [1, 2, 3, 3, 4, 3, 2, 5, 6, 5]
tira_duplicadas(lista)