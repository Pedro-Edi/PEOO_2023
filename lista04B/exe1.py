lista=[]
for x in range(10):
  matriz=int(input())
  if matriz<=0:  
    matriz=1 
  lista.append(matriz)
for s in range(len(lista)):
  print(f'X[{s}] = {lista[s]}')