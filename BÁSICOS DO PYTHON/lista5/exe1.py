#1036 – Fórmula de Bhaskara
A, B, C = map(float, input().split())
delta = ((B**2) + (-4 * A * C))
if A == 0 or delta < 0:
  print('Impossivel calcular')

else:
  raiz_delta = delta**0.5
  x1 = ((-1 * B) + (raiz_delta)) / (2 * A)

  x2 = ((-1 * B) + (raiz_delta * -1)) / (2 * A)
  print(f'R1 = {x1:.5f}\nR2 = {x2:.5f}')