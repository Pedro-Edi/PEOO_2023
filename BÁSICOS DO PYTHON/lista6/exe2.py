#1080 – Maior e Posição
maior=0
for x in range(1,101):
  num=int(input())
  if num>maior:
    maior=num
    pos=x
print(maior)
print(pos)