data = input("Digite uma data no formato dd/mm/aaaa: ")

dia, mes, ano = map(int, data.split("/"))

meses = [
    "janeiro", "fevereiro", "março", "abril", "maio", "junho",
    "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"
]

print("A data é", dia, "de", meses[mes-1], "de", ano)
