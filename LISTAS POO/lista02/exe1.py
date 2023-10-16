import math
class Circulo:
  def __init__(self):
    self.__raio=0
  def set_raio(self,v):
    if v>0: self.__raio=v
    else: raise ValueError('Não existe raio menor ou igual a 0!')
  def get_raio(self):
    return self.__raio
  def calc_area(self):
    return self.__raio**2*math.pi
  def calc_circunferencia(self):
    return 2*math.pi*self.__raio

C=Circulo()
C.set_raio(int(input('Raio: ')))
print(f'O raio mede: {C.get_raio():.1f} m ')
print(f'Área: {C.calc_area():.1f} m')
print(f'Circunferência: {C.calc_circunferencia():.1f} m')