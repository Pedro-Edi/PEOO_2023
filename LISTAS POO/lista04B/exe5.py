O=input()
lista=[]
lista1=[]

for x in range(12):
  lista=[]
  for s in range(12):
    num=float(input())
    lista.append(num)
  lista1.append(lista)
lista2=[]
for w in range(12):
  q=12
  while q>0:
    q-=1
    if q>w:
      lista2.append(lista1[w][q])

re=sum(lista2)
su=len(lista2)
l=re/su
if O=='S':
  print(f'{re:.1f}')
if O=='M':
  print(f'{l:.1f}')

