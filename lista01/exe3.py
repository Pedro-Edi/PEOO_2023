class Viagem:
  def __init__(self):
    self.tempo=0
    self.Distancia=0
  def velocida_media(self):
   return f'{self.Distancia/self.tempo:.2f} km/h'

Velocidade=Viagem()
Velocidade.Distancia=int(input())
x=list((map(int,input().split(':'))))
Velocidade.tempo=x[0]+(x[1]/60)
print(Velocidade.velocida_media())