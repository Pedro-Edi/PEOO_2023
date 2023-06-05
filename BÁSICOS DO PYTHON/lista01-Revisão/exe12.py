expressao = input("Digite dois valores inteiros separados por um operador (+, -, * ou /): ")

valor1, operador, valor2 = expressao.split()

valor1 = int(valor1)
valor2 = int(valor2)

if operador == "+":
    resultado = valor1 + valor2
elif operador == "-":
    resultado = valor1 - valor2
elif operador == "*":
    resultado = valor1 * valor2
elif operador == "/":
    resultado = valor1 / valor2
else:
    print("Operador inválido")
    exit()

print("O resultado da operação é", resultado)
