class EntradaCinema:
    def __init__(self, dia, horario):
        self.dia = dia
        self.horario = horario
    
    def calcular_valor_entrada(self):
        valor_base = 0
        if self.dia in ["segunda", "terça", "quinta"]:
            valor_base = 16
        elif self.dia == "quarta":
            valor_base = 8
        else:  # sexta, sábado, domingo
            valor_base = 20

        if self.horario >= 17 and self.horario <= 24:
            valor_base *= 1.5

        return valor_base

# Exemplo de uso da classe
dia = input("Digite o dia da semana: ")
horario = int(input("Digite o horário da sessão (em horas): "))

entrada = EntradaCinema(dia, horario)
valor_entrada = entrada.calcular_valor_entrada()
print("Valor da entrada:", valor_entrada)
