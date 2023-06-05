numeros = input("Digite dez valores inteiros separados por espaço: ").split()
numeros = [int(num) for num in numeros]

maior = max(numeros)
menor = min(numeros)

print("O maior valor é", maior, "e o menor é", menor)
