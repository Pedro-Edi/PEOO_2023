class EntradaCinema:
    def __init__(self, dia, horario):
        self.__dia = dia
        self.__horario = horario
    
    def calcular_valor_entrada(self):
        if self.__dia in ["segunda", "terça", "quinta"]:
            valor_base = 16.00
        elif self.__dia == "quarta":
            valor_base = 8.00
        else:  # sexta, sábado e domingo
            valor_base = 20.00
        
        if self.__horario >= 17 and self.__horario <= 23:
            valor_base *= 1.5
        
        return valor_base
    
    def get_dia(self):
        return self.__dia
    
    def set_dia(self, dia):
        self.__dia = dia
    
    def get_horario(self):
        return self.__horario
    
    def set_horario(self, horario):
        self.__horario = horario

# Exemplo de uso da classe
dia = input("Digite o dia da sessão (segunda, terça, quarta, quinta, sexta, sábado ou domingo): ")
horario = int(input("Digite o horário da sessão (entre 0 e 23): "))
entrada = EntradaCinema(dia, horario)
print("Valor da Entrada:", entrada.calcular_valor_entrada())

# Acessando e modificando os atributos da entrada usando os métodos de acesso
novo_dia = input("Digite o novo dia da sessão: ")
entrada.set_dia(novo_dia)
print("Novo dia:", entrada.get_dia())
