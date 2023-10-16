class Cliente:

  def __init__(self, nome, cpf, limite):
    self.__nome = nome
    self.__cpf = cpf
    self.__limite = limite
    self.__socio =None
   
  
  def GetNome(self):
    return self.__nome

  def SetSocio(self, c):
    if c==None:
      self.__socio=None
    elif c!=None:
      self.__socio=c
      c.__socio=self
    
  def GetLimite(self):
    if self.__socio!=None:
      return f' RS {self.__limite + self.__socio.__limite}'
    else:
      return self.__limite


  def __str__(self):
    return f'{self.__nome} {self.__cpf} {self.__limite}'


class Empresa:

  def __init__(self):
    self.__clientes = []

  def inserir(self, c):
    self.__clientes.append(c)

  def listar(self):
    return self.__clientes


class UI:

  def main():
    lista=[]
    sociedade=[]
    op = int(
      input(
        '1-Inserir Cliente ,2-Listar clientes da empresa, 3- Fazer socieda '))
    
    E = Empresa()
    while True:
      if op == 1:
        Nome = input('Nome: ')
        cpf = input('Cpf: ')
        limite = int(input('Limite: '))
        c = Cliente(Nome, cpf, limite)
        E.inserir(c)
      if op == 2:
        
        for k in E.listar():
          print(f'Nome: {k.GetNome()}')
          print(f'Limite: {k.GetLimite()}')
          print('---')

      if op == 3:
        a = input('Digite o nome do cliente 1: ')
        b = input('Digite o nome do cliente 2: ')


        for k in lista:
          if a!=k.GetNome():
            sociedade.append(k)
        for s in lista:
          if b!=s.GetNome():
            sociedade.append(s)
        if len(sociedade)%2!=0:
          for w in sociedade:
            w.SetSocio(None)
          
        cliente1=None
        cliente2=None
        

        
            

        
          
        for cliente in E.listar():
          if a == cliente.GetNome():
            cliente1=cliente
            if cliente1 in lista:
              True
            else:
              lista.append(cliente1)
              
          if  b  == cliente.GetNome():
            cliente2=cliente
            if cliente2 in lista:
              True
            else:
              lista.append(cliente2)

        if cliente1.GetNome()==cliente2.GetNome():
          print('Voce digitou os mesmos cliente')
        elif cliente1!=cliente2:
          cliente1.SetSocio(cliente2)
        

          
        
  
      op = int(
        input(
          '1-Inserir Cliente ,2-Listar clientes da empresa, 3- Fazer socieda ')
      )


UI.main()
