def max_min(lista):
    max = -99999999
    min = 9999999999
    for num in lista:
        if num < min:
            min = num
        elif num > max:
            max = num

    return max, min

lista = [10, 1, 2, 3, 11, 13, 5, 7]
max, min = max_min(lista)
print(f"Maior: {max} e menor {min}")
