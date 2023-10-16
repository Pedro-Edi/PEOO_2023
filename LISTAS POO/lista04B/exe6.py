lista=[]
lista2=0
lista3=[]
while True:
    try:
        x, y = map(int, input().split())

        for s in range(x):
            num = list(map(int, input().split()))
            lista.append(num)

        for q in range(x):
            for a in range(y):
                if lista[q][a] == 1:
                    lista3.append(9)
                elif lista[q][a] == 0:
                    
                      if lista[q-1][a] == 1:
                          lista2 += 1
                  
                      if lista[q+1][a] == 1:
                          lista2 += 1
                  
                      if lista[q][a-1] == 1:
                          lista2 += 1
                  
                      if lista[q][a+1] == 1:
                          lista2 += 1
                    lista3.append(lista2)
                lista2 = 0

            print(*lista3, sep='')
            lista3 = []

        lista=[]
        lista2=0
        lista3=[]

    except EOFError:
        break
