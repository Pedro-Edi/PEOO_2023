class Viagem:
  def __init__(self,distancia,tempogasto):
    self.distancia=distancia
    self.tempogasto=tempo_gasto
  def velocidademedia(self):
    velocidademedia=self.distancia/self.tempogasto
    return f'{velocidademedia:.1f}'
distancia=int(input('Distância em km: '))
horas,minutos=map(int,input('Digite o tempo (hh:mm): ').split(':'))
tempo_gasto=horas+(minutos/60)
v=Viagem(distancia,tempo_gasto)
print(f'A viagem teve um velocidade média de {v.velocidademedia()} km/h')