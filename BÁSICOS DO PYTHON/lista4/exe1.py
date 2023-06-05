#1012 - Area
valores = input().split()
A = float(valores[0])
B = float(valores[1])
C = float(valores[2])
Area1 = (A*C)/2
pi = 3.14159
Area2 = (C**2)*pi
Area3 = ((A+B)*C)/2
Area4 = B**2
Area5 = A*B
print(f'TRIANGULO: {Area1:.3F}')
print(f'CIRCULO: {Area2:.3F}')
print(f'TRAPEZIO: {Area3:.3F}')
print(f'QUADRADO: {Area4:.3F}')
print(f'RETANGULO: {Area5:.3F}')