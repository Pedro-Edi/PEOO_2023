#1094 – Experiências
x =int(input())
coelho,sapo,rato,n3=0,0,0,0
for i in range(x):
  n=input().split()
  n1=int(n[0])
  n2=n[1]
  if(n2=='C'):
    coelho+=n1
  if(n2=='R'):
    rato+=n1
  if(n2=='S'):
     sapo+=n1
  n3+=n1
  coelhoP=(coelho*100)/n3
  sapoP=(sapo*100)/n3
  ratoP=(rato*100)/n3
print(f'Total: {n3} cobaias\nTotal de coelhos: {coelho}\nTotal de ratos: {rato}\nTotal de sapos: {sapo}\nPercentual de coelhos: {coelhoP:.2f} %\nPercentual de ratos: {ratoP:.2f} %\nPercentual de sapos: {sapoP:.2f} %')