#2670 – Máquina de Café
A1=int(input())
A2=int(input())
A3=int(input())
tempo1=A2*2+A3*4
tempo2=A1*2+A3*2
tempo3=A1*4+A2*2
lista=[tempo1,tempo2,tempo3]
print(min(lista))
