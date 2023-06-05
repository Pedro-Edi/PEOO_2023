hora1, minuto1 = map(int, input("Digite o primeiro horário no formato hh:mm: ").split(":"))
hora2, minuto2 = map(int, input("Digite o segundo horário no formato hh:mm: ").split(":"))

total_minutos = (hora1 * 60 + minuto1) + (hora2 * 60 + minuto2)
total_horas = total_minutos // 60
total_minutos = total_minutos % 60

print("Total de horas =", "{:02d}:{:02d}".format(total_horas, total_minutos))
