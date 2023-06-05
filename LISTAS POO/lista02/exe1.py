import math

class Circulo:
    def __init__(self, raio):
        self.__raio = raio
    
    def calcular_area(self):
        return math.pi * (self.__raio ** 2)
    
    def calcular_circunferencia(self):
        return 2 * math.pi * self.__raio
    
    def get_raio(self):
        return self.__raio
    
    def set_raio(self, raio):
        self.__raio = raio

# Exemplo de uso da classe
raio = float(input("Digite o raio do círculo: "))
circulo = Circulo(raio)
print("Área:", circulo.calcular_area())
print("Circunferência:", circulo.calcular_circunferencia())

# Acessando e modificando o raio usando os métodos de acesso
novo_raio = float(input("Digite o novo raio: "))
circulo.set_raio(novo_raio)
print("Novo
