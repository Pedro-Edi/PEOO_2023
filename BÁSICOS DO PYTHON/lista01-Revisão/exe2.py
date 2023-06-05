num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))

media = (num1 + num2 + num3 + num4) / 4

print("Média =", media)

print("Números menores que a média:")
if num1 < media:
    print(num1)
if num2 < media:
    print(num2)
if num3 < media:
    print(num3)
if num4 < media:
    print(num4)

print("Números maiores ou iguais à média:")
if num1 >= media:
    print(num1)
if num2 >= media:
    print(num2)
if num3 >= media:
    print(num3)
if num4 >= media:
    print(num4)
