x=int(input())
a=list(map(int,input().split()))
menor=a[0]
pos=0
for i in range(len(a)):
  if a[i]<menor:
    menor=a[i]
    pos=i
print(f'Menor valor: {menor}')
print(f'Posicao: {pos}')