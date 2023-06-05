class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.__distancia = distancia
        self.__horas = horas
        self.__minutos = minutos
    
    def calcular_velocidade_media(self):
        tempo_total = self.__horas + self.__minutos / 60
        velocidade_media = self.__distancia / tempo_total
        return velocidade_media
    
    def get_distancia(self):
        return self.__distancia
    
    def set_distancia(self, distancia):
        self.__distancia = distancia
    
    def get_horas(self):
        return self.__horas
    
    def set_horas(self, horas):
        self.__horas = horas
    
    def get_minutos(self):
        return self.__minutos
    
    def set_minutos(self, minutos):
        self.__minutos = minutos

# Exemplo de uso da classe
distancia = float(input("Digite a distância percorrida (em km): "))
horas = int(input("Digite o tempo em horas: "))
minutos = int(input("Digite o tempo em minutos: "))
viagem = Viagem(distancia, horas, minutos)
print("Velocidade Média:", viagem.calcular_velocidade_media())

# Acessando e modificando os atributos da viagem usando os métodos de acesso
novo_distancia = float(input("Digite a nova distância percorrida (em km): "))
viagem.set_distancia(novo_distancia)
print("Nova distância:", viagem.get_distancia())
