try:
    numero = int(input("Digite o numero da tabuada: "))
    limite = int(input("Digite o limite da tabuada: "))
except ValueError:
    print("Por favor, digite apenas números inteiros.")
else:
    for i in range(1, limite+1):
        print(f"{numero} x {i} = {numero * i}")
