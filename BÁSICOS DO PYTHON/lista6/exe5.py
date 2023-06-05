#1116 – Dividindo X por Y
lista=[]
x=int(input())
for s in range(x):
  s,y=map(int,input().split())
  if y!=0:
    r=s/y
  else:
    r='divisao impossivel'
  lista.append(r)
for t in range(len(lista)):
  print(lista[t])