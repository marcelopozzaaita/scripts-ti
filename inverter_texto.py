palavra = input("Digite a palavra: ")

palavra = palavra.lower()

palavra_invertida = palavra[::-1]

print(f"A palavra invertida {palavra_invertida}")

if(palavra == palavra_invertida):
    print("É um palíndormo")




