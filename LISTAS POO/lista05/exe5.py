class Banda:
  def __init__(self,nome,pais,estilo):
    self.__nome=nome
    self.__pais=pais
    self.__estilo=estilo
    self.__albuns=[]

  def inserir(self,album):
    self.__albuns.append(album)
  def listar(self):
    return self.__albuns
  def ultimo(self):
    w=self.__albuns[0]
    for x in self.__albuns:
      if x.getlancamento().date()>datetime.datetime.today():
        w=x
    return f'O mais novo tem a seguinte data{w.getlancamento().strftime("%d/%m/%Y")}'
        
class Album:
  def __init__(self,titulo,formato,gravadora,lancamento):
    self.__titulo=titulo
    self.__formato=formato
    self.__gravadora=gravadora
    self.__lancamento=lancamento
  def getlancamento(self):
    return self.__lancamento
  def __str__(self):
    return f'{self.__titulo} - {self.__formato.name} - {self.__gravadora} {self.__lancamento.strftime("%d/%m/%Y")}'
import enum
class Midia(enum.Enum):
  LP=1
  CD=2
  DVD=3
  BD=4
  Stream=5
import datetime
B=Banda(input('Nome da banda: '),input('Pais: '),input('Estilo: '))
for x in range(2):
  titulo=input()
  formato=Midia(int(input('LP:1 , CD:2, DVD:3, BD: 4, Stream: 5')))
  gravadora=input('Nome gravadora')
  lancamento_txt=input('DIA/MES/ANO')
  lancamento=datetime.datetime.strptime(lancamento_txt,"%d/%m/%Y")
  A=Album(titulo,formato,gravadora,lancamento)
  B.inserir(A)
for w in B.listar():
  print(w)
print(B.ultimo())