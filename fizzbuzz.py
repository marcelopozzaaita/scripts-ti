
num = int(input("Digite um numero entre 1 e 50: "))
if(num > 50):
    print("Numero tem que ser entre 50")
else:
    if( (num % 5 ==0) & (num % 3 ==0)):
        print("FizzBuzz")
    elif (num % 5 ==0):
        print("Buzz")
    elif (num % 3 == 0):
        print("Fizz")
    else:
        print(f"{num}")