hora, minuto = map(int, input("Digite o horário no formato hh:mm: ").split(":"))

if hora < 0 or hora > 23 or minuto < 0 or minuto > 59:
    print("Hora Inválida")
    exit()

angulo_hora = (hora % 12) * 30 + minuto * 0.5
angulo_minuto = minuto * 6
diferenca = abs(angulo_hora - angulo_minuto)
menor_angulo = min(diferenca, 360 - diferenca)

print("Menor ângulo entre os ponteiros =", menor_angulo, "graus")
