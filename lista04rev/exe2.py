class Esporte:
  def __init__(self,nome,horario,mensalidade):
    self.__nome=nome
    self.__horario=horario
    self.__mensalidade=mensalidade
  def men(self):
    return self.__mensalidade
  def GetNome(self):
    return self.__nome
  def __str__(self):
    return f'ESPORTE: {self.__nome} -HORÁRIO: {self.__horario} - MENSALIDADE {self.__mensalidade}'

class Academia:
  def __init__(self,nome,endereço):
    self.__nome=nome
    self.__endereço=endereço
    self.__esportes=[]
  def inserir(self,e):
    self.__esportes.append(e)
  def listar(self):
    return self.__esportes
  def mediamen(self):
    if len(self.__esportes)==0: return 'NÃO HÁ NENHUM ESPORTE REGISTRADO'
    men,num=0,0
    for x in self.__esportes:
      men+=x.men()
      num+=1
    for esporte in self.__esportes:
      return f'{esporte.GetNome()}: R${esporte.men():.2f}'
    return f'A média das mensalidades dos esportes é R$ {men/num:.}'

class UI:
  def main():
    A=Academia(input('NOME DA ACADEMIA: '), input('ENDEREÇO: '))
    op=int(input('1-Novo esporte: ,2-Listar Esportes,3-Média das mensalidades:,0-Fim: '))
    while True:
      if op==1:
        esporte=input('Nome do esporte: ')
        horario=input('Horario(xx:mm: ')
        valor=float(input('Valor Mensalidade: '))
        e=Esporte(esporte,horario,valor)
        A.inserir(e)
      if op==2:
        for k in A.listar():
          print(k.GetNome())
          print(k.men())
          print('-----')
      if op==3:
        print(A.mediamen())
      if op==0:
        break
      op=int(input('1-Novo esporte: ,2-Listar Esportes,3-Média das mensalidades:,0-Fim: '))

UI.main()
        
    
      