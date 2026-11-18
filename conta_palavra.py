def contar_palavras(frase):
    contagem = {}

    frase = frase.lower()
    frase = frase.split()

    for palavra in frase:
        if(palavra in contagem):
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

resultado = contar_palavras("o gato viu o rato")
print(resultado)