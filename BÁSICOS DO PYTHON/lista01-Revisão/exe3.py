num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))

soma_pares = 0
soma_impares = 0

if num1 % 2 == 0:
    soma_pares += num1
else:
    soma_impares += num1

if num2 % 2 == 0:
    soma_pares += num2
else:
    soma_impares += num2

if num3 % 2 == 0:
    soma_pares += num3
else:
    soma_impares += num3

if num4 % 2 == 0:
    soma_pares += num4
else:
    soma_impares += num4

print("Soma dos pares =", soma_pares)
print("Soma dos ímpares =", soma_impares)
