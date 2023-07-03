import datetime
class Jogador:
  def __init__(self,nome,camisa,gols,data):
    self.__nome=nome
    self.__camisa=camisa
    self.__gols=gols
    self.__data=data.strftime("%d/%m/%Y")
  def Nome(self):
    return self.__nome
  def gols(self):
    return self.__gols
  def idade(self):
    return self.__data

  def __str__(self):
    return f'Nome:{self.__nome} - Camisa:{self.__camisa} - Gols: {self.__gols}'

class Time:
  def __init__(self,nome,estado):
    self.__nome=nome
    self.__estado=estado
    self.__jogadores=[]
  def inserir(self,j):
    self.__jogadores.append(j)
  def listar(self):
    return self.__jogadores
  def artilheiro(self):
    if len(self.__jogadores) == 0: return None
    art=self.__jogadores[0]
    maior=self.__jogadores[0].gols()
    for x in self.__jogadores:
      if maior<x.gols():
        maior=x.gols()
        art=x
    return f'{art.Nome()}: {art.gols()} gols'

  def maisnovo(self):
    if len(self.__jogadores) == 0: return None
    num=self.__jogadores[0]
    for x in self.__jogadores:
      if x.idade()>num.idade():
        num=x
    return f'O mais novo é {num.Nome()} com idade de {num.idade()}'
      
        
  def __str__(self):
    return f'TIME:{self.__nome} ESTADO: {self.__estado}'


time=Time(input('TIME: '),input('ESTADO: '))
text=input()
data1=datetime.datetime.strptime(text,"%d/%m/%Y").date()
J=Jogador('pepe',10,20,data1)
time.inserir(J)
text=input()
data2=datetime.datetime.strptime(text,"%d/%m/%Y").date()
J=Jogador('kaka',10,20,data2)
time.inserir(J)
for k in time.listar():
  print(f'{k.Nome()}: {k.gols()} gols')

print(time.artilheiro())
print(time.maisnovo())

      
      
        
    
    
        
        
    
      
     