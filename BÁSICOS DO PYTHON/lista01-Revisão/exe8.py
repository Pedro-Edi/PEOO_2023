num1 = int(input("Digite o primeiro valor: "))
num2 = int(input("Digite o segundo valor: "))
num3 = int(input("Digite o terceiro valor: "))
num4 = int(input("Digite o quarto valor: "))

if num1 == num2 or num1 == num3 or num1 == num4 or num2 == num3 or num2 == num4 or num3 == num4:
    print("Os valores não são diferentes.")
    exit()

maior = max(num1, num2, num3, num4)
menor = min(num1, num2, num3, num4)
segundo_maior = max(num1, num2, num3, num4, key=lambda x: x if x != maior else float('-inf'))
segundo_menor = min(num1, num2, num3, num4, key=lambda x: x if x != menor else float('inf'))
soma = segundo_maior + segundo_menor

print("Maior valor =", maior)
print("Menor valor =", menor)
print("A soma do segundo maior valor com o segundo menor =", soma)
