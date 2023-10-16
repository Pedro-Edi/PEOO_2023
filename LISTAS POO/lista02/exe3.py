class Viagem:
  def __init__(self):
    self.__distancia=0
    self.__tempo=0
  def set_distancia(self,d):
    if d>=0: self.__distancia=d
    else: raise ValueError()
  def set_tempo(self,t):
    if t>=0: self.__tempo=t
    else: raise ValueError()
      
  def get_distancia(self):
    return self.__distancia
  def get_tempo(self):
    return self.__tempo

  def velocidade_media(self):
    return self.__distancia/self.__tempo

V=Viagem()
V.set_distancia(int(input('Distancia em km: ')))
H,M=map(int,input('Tempo(HH:MM): ').split(':'))
V.set_tempo(H+(M/60))
print(f'Sua velocidade média é de : {V.velocidade_media():.1f} Km/h')