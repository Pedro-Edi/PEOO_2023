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
      cls.__clientes = []
      with open("./lista07-Dicionario/clientes.json", mode="r") as arquivo:
        clientes_json = json.load(arquivo)
        for obj in clientes_json:
          c = Cliente(obj["_Cliente__id"], obj["_Cliente__nome"],
                      obj["_Cliente__email"], obj["_Cliente__fone"])
          cls.__clientes.append(c)
    except FileNotFoundError:
      #print('Nenhum arquivo encontrado')
      pass

  @classmethod
  def salvar(cls):
    with open("./lista07-Dicionario/clientes.json", mode="w") as arquivo:
      json.dump(cls.__clientes, arquivo, default=vars, indent=4)
