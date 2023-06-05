class Viagem:
    def __init__(self, distancia, horas, minutos):
        self.distancia = distancia
        self.tempo_total = horas + minutos / 60
    
    def calcular_velocidade_media(self):
        return self.distancia / self.tempo_total

# Exemplo de uso da classe
distancia = float(input("Digite a distância da viagem (em km): "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))

viagem = Viagem(distancia, horas, minutos)
velocidade_media = viagem.calcular_velocidade_media()
print("Velocidade Média:", velocidade_media, "km/h")
