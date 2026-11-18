def calcular_soma_e_media(lista):
    if not lista:
        return 0, 0
    
    total = sum(lista)
    quantidade = len(lista)
    media = total / quantidade

    return total, media
meus_numeros = [10, 20, 30, 40, 50]

soma_total, media_valor = calcular_soma_e_media(meus_numeros)

print(f"A soma é: {soma_total}")
print(f"A média é: {media_valor:.2f}")