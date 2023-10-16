lista=[]
for x in range(100):
  matriz=float(input())
  if matriz<=10:
    lista.append(f'A[{x}] = {matriz:.1f}')
for w in range(len(lista)):
  print(lista[w])