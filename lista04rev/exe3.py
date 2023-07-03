 import datetime
class amigos:

  def __init__(self,nome,idade):
    self.__nome=nome
    self.__idade=idade
  def idade(self):
    data=datetime.datetime.today()
    nas=data.date()-self.__idade
    return nas
  def __str__(self):
    return f'{self.__nome} - {self.__idade}'
class UI:
  def main():
    amigos1=[]
    idades=[]
    for x in range(2):
      idade_txt=input('IDADE: ')
      idade=datetime.datetime.strptime(idade_txt,"%d/%m/%Y").date()
      nome=input('NOme')
      a=amigos(nome,idade)
      amigos1.append(a)
      
      
            
    amigos.sort()
    print(amigos1[len])
    


UI.main()
    