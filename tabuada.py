numero = int(input("Digite o numero da tabuada: "))
limite = int(input("Digite o limite da tabuada: "))

for i in range(1, limite+1):
    print(f"{numero}x{i} = {numero * i}")
