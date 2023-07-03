N = int(input())

lista = []
for _ in range(N):
  posicoes = list(map(int, input().split()))
  lista.append(posicoes)
print(lista)
for s in range(N):
  lista1 = []
  for w in range(N):
    if w != s:
      resultado = ((lista[w][0] - lista[s][0]) ** 2 + (lista[w][1] - lista[s][1]) ** 2 + (lista[w][2] - lista[s][2]) ** 2) ** 0.5
      lista1.append(resultado)
  num = min(lista1)

  if num < 20:
    print('A')
  elif num >= 20 and num < 50:
    print('M')
  elif num >= 50:
    print('B')
