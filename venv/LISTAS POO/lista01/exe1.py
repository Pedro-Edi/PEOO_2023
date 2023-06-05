import math

class Circulo:
    def __init__(self, raio):
        self.raio = raio
    
    def calcular_area(self):
        return math.pi * (self.raio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.raio

# Exemplo de uso da classe
raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print("Área:", circulo.calcular_area())
print("Circunferência:", circulo.calcular_circunferencia())
