def contador_vogais(frase):
    vogais = "aieou"
    contador = 0
    frase = frase.lower()

    for palavra in frase:
        if palavra in vogais:
            contador += 1
    return contador

frase = "Eu comi muito bem.Oi!"
print(f"Numero de vogais: {contador_vogais(frase)}")