class Cinema:
  def __init__(self):
    self.__dia=None
    self.__horario=0
    self.__dias=['seg','ter','quar','quin','sex','sáb','dom']
  def set_dia(self,d):
    if d in self.__dias:
      self.__dia=d
    else:
      raise ValueError()
  def set_horario(self,h):
    if 1<=h<=24:
      self.__horario=h
    else:
      raise ValueError()
      
  def get_dia(self):
    return self.__dia
  def get_horario(self):
    return self.__horario
    
  def inteira(self):
    total=0
    if self.__dia=='seg' or self.__dia=='ter' or self.__dia=='quin':
      total=16
    elif self.__dia=='quar':
      total=8
    elif self.__dia=='sex' or self.__dia=='sáb' or self.__dia=='domin':
      total=20
    if 24>=self.__horario>=17 and self.__dia!='quar':
      return (total/2)+(total)
    else:
      return total
  def meia(self):
    if self.__dia!='quar':
      
      return self.inteira()/2
    else:
      return self.inteira()
      
c=Cinema()
dia=input('Dia: ')
c.set_dia(dia)

horario=int(input('Hora: '))
c.set_horario(horario)
print(f'Inteira: {c.inteira()}\nMeia: {c.meia()}')