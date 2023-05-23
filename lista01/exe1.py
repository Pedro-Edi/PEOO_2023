import math
class Circulo:
  def __init__(self):
    self.raio=0
  def cal_area(self):
    return self.raio**2*math.pi;
  def cal_circun(self):
    return 2*math.pi*self.raio;
Calculo=Circulo()
Calculo.raio=float(input())
print(Calculo.cal_area())
print(Calculo.cal_circun())
    