class Cinema:
  def __init__(self):
    self.dia=''
    self.horari=0
  def valor(self):
  
    if self.dia=='Segunda' or self.dia=='Terça' or self.dia=='Quinta':
      valor=16
    if self.dia=='Sexta' or self.dia=='Sábado' or self.dia=='Domingo':
      valor=20
    if self.dia=='Quarta':
      valor=8
    if self.horario >17:
      valor*=1.5
    return valor
  def meia(self):
    if self.dia!='Quarta':
      return valor/2
    else:
      return valor
Valor=Cinema()
Valor.dia=input()
Valor.horario=int(input())
print(Valor.valor())
print(Valor.meia())

        