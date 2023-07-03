J, R = map(int, input().split())
lista_pontos = list(map(int, input().split()))
total_pontos_jogadores = []

for x in range(J):
    valor = lista_pontos[x::J]
    total_pontos_jogadores.append(valor)

total_pontos_jogadores_soma = []
for a in range(len(total_pontos_jogadores)):
    total_pontos_jogadores_soma.append(sum(total_pontos_jogadores[a]))

max_pontos = max(total_pontos_jogadores_soma)
indices_max = []

for i in range(len(total_pontos_jogadores_soma)):
    if max_pontos == total_pontos_jogadores_soma[i]:
        indices_max.append(i + 1)

if len(indices_max) > 1:
    for w in indices_max:
      p=w
    print(p)

else:
    print(*indices_max)
