#1151 – Fibonacci Fácil
u=int(input())
x=1
lista=[]
v=[0,0]
if u==1:
  print(0)
elif u==2:
  print(0,1)
else:
  for s in range(u-2):
    v=[v[1],x]
    x=v[0]+x
    lista.append(x)
  print(0,1," ".join(map(str,lista)))
