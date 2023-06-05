#2424 – Tira-teima
x,y=map(int,input().split())
if (0>x or x>432) or (0>y or y>468):
  bola='fora'
else:
  bola='dentro'
print(bola)