
import math
class Circulo:
  def __init__(self,raio):
    self.raio=raio
  def circunferencia(self):
    C=2*math.pi*self.raio
    return f'A circunferencia é de {C:.1f} cm'
  def area(self):
    A=(math.pi)*(self.raio**2)
    return f'A area do círculo é de {A:.1f} cm'
    
C=Circulo(float(input('Raio é de : ')))
print(C.circunferencia())
print(C.area())