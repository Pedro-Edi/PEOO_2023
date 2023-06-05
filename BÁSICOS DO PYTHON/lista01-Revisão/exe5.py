mes = int(input("Informe o número do mês: "))

if mes == 1:
    trimestre = 1
    nome_mes = "janeiro"
elif mes == 2:
    trimestre = 1
    nome_mes = "fevereiro"
elif mes == 3:
    trimestre = 1
    nome_mes = "março"
elif mes == 4:
    trimestre = 2
    nome_mes = "abril"
elif mes == 5:
    trimestre = 2
    nome_mes = "maio"
elif mes == 6:
    trimestre = 2
    nome_mes = "junho"
elif mes == 7:
    trimestre = 3
    nome_mes = "julho"
elif mes == 8:
    trimestre = 3
    nome_mes = "agosto"
elif mes == 9:
    trimestre = 3
    nome_mes = "setembro"
elif mes == 10:
    trimestre = 4
    nome_mes = "outubro"
elif mes == 11:
    trimestre = 4
    nome_mes = "novembro"
elif mes == 12:
    trimestre = 4
    nome_mes = "dezembro"
else:
    print("Mês inválido")
    exit()

print("O mês de", nome_mes, "é do", trimestre, "º trimestre do ano.")
