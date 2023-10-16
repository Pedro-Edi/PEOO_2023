class Cinema:
  def __init__(self):
    self.dia=dia
    self.horario=horario
  def inteira(self):
    total=0
    if self.dia=='segunda' or self.dia=='terça' or self.dia=='quinta':
      total=16
    elif self.dia=='quarta':
      total=8
    elif self.dia=='sexta' or self.dia=='sábado' or self.dia=='domingo':
      total=20
    if 24>=self.horario>=17 and self.dia!='quarta':
      return (total/2)+(total)
    else:
      return total
  def meia(self):
    if self.dia!='quarta':
      
      return self.inteira()/2
    else:
      return self.inteira()
dia=input('Dia: ')
horario=int(input('Hora: '))
c=Cinema(dia,horario)
print(f'Inteira: {c.inteira()}\nMeia: {c.meia()}')