import json

class Cliente:

  def __init__(self, id, nome, email, fone):
    self.__id = id
    self.__nome = nome
    self.__email = email
    self.__fone = fone

  def get_id(self):
    return self.__id

  def get_nome(self):
    return self.__nome

  def get_email(self):
    return self.__email

  def get_fone(self):
    return self.__fone

  def set_id(self, id):
    self.__id = id

  def set_nome(self, nome):
    self.__nome = nome

  def set_fone(self, fone):
    self.__fone = fone

  def set_email(self, email):
    self.__email = email

  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__email} - {self.__fone}"


'''
class NCliente:
  def __init__(self):
    self.__clientes = []

  def inserir(self,obj):
    self.__clientes.append(obj)
  def listar(self):
    return self.__clientes
'''


class NCliente:
  __clientes = []

  @classmethod
  def inserir(cls, obj):
    NCliente.abrir()
    id = 0
    for cliente in cls.__clientes:
      id = cliente.get_id()
    obj.set_id(id + 1)
    cls.__clientes.append(obj)
    NCliente.salvar()


  @classmethod
  def listar(cls):
    NCliente.abrir()
    return cls.__clientes

  @classmethod
  def listar_id(cls, id):
    NCliente.abrir()

    for cliente in NCliente.listar():
      if cliente.get_id() == id:
        return cliente
    return None

  @classmethod
  def atualizar(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cliente.set_nome(obj.get_nome())
    cliente.set_email(obj.get_email())
    cliente.set_fone(obj.get_fone())
    NCliente.salvar()

  @classmethod
  def excluir(cls, obj):
    NCliente.abrir()
    cliente = NCliente.listar_id(obj.get_id())
    cls.__clientes.remove(cliente)
    NCliente.abrir()
  @classmethod
  def abrir(cls):
    try:
      cls.__clientes=[]
      with open("clientes.json", mode="r") as arquivo:
        clientes_json=json.load(arquivo)
        for obj in clientes_json:
          c = Cliente(obj["_Cliente__id"],obj["_Cliente__nome"],
                      obj["_Cliente__email"], obj["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      #print('Nenhum arquivo encontrado')
      pass
        
  @classmethod
  def salvar(cls):
    with open("clientes.json", mode="w") as arquivo:
      json.dump(cls.__clientes, arquivo, default =vars,indent=4)
      
class UI:
  def main():
    op = UI.menu2()
    while op != 99:
      if op == 1:
        op = UI.menu()
        while op != 99:
          if op == 1:
            UI.InserirCliente()
          elif op == 2:
            UI.ListarCliente()
          elif op == 3:
            UI.AtualizarCliente()
          elif op == 4:
            UI.ExcluirCliente()
          op = UI.menu()
      op = UI.menu2()

  def menu2():
    print('OPERAÇÕES')
    print(
      '-------------------------------------------------------------------')
    print('Cliente: 1 , Serviços: 2 , Agenda: 3 , 99 - Fechar progama')
    return (int(input('Digite: ')))

  def menu():
    print(
      '-------------------------------------------------------------------')
    print('1 - INSERIR , 2 LISTAR , 3 - ATUALIZAR , 4 EXCLUIR , 99-VOLTAR')
    return (int(input('Digite: ')))

  def InserirCliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite seu email: ')
    fone = int(input('Digite o número do seu telefone: '))
    NCliente.inserir(Cliente(0, nome, email, fone))

  def ListarCliente():
    for cliente in NCliente.listar():
      print(cliente)

  def AtualizarCliente():
    UI.ListarCliente()
    id = int(input('Digite o id que será alterado: '))
    nome = input('Digite o nome do cliente: ')
    email = input('Digite seu email: ')
    fone = int(input('Digite o número do seu telefone: '))
    NCliente.atualizar(Cliente(id, nome, email, fone))
    print('Cliente atualizado com sucesso')

  def ExcluirCliente():
    UI.ListarCliente()
    id = int(input('Qual cliente será excluido: '))
    cliente = Cliente(id, "", "", "")
    NCliente.excluir(cliente)


UI.main()
