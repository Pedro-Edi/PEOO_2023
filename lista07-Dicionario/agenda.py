import datetime
import json


class Agenda:

  def __init__(self, id, data, confirmado, idCliente, idServico):
    self.__id = id
    self.__data = data
    self.__confirmado = False
    self.__idCliente = None
    self.__idServico = None

  def get_id(self):
    return self.__id

  def get_data(self):
    return self.__data

  def set_id(self, id):
    self.__id = id

  def set_data(self, data):
    self.__data = data

  def __str__(self):
    return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')}"


class NAgenda:
  __agendas = []

  @classmethod
  def inserir(cls, obj):
    NAgenda.abrir()
    id = 0
    for agenda in cls.__agendas:
      id = agenda.get_id()
    obj.set_id(id + 1)
    cls.__agendas.append(obj)
    NAgenda.salvar()

  @classmethod
  def listar_id(cls, id):
    NAgenda.abrir()
    for agenda in cls.__agendas:
      if agenda.get_id() == id:
        return agenda
    return None

  @classmethod
  def listar(cls):
    NAgenda.abrir()
    return cls.__agendas

  @classmethod
  def atualizar(cls, obj):
    NAgenda.abrir()
    agenda = NAgenda.listar_id(obj.get_id())
    agenda.set_data(obj.get_data())
    NAgenda.salvar()

  @classmethod
  def excluir(cls, obj):
    NAgenda.abrir()
    agenda = NAgenda.listar_id(obj.get_id())
    cls.__agendas.remove(agenda)
    NAgenda.salvar()

  @classmethod
  def abrir(cls):
    try:
      cls.__agendas = []
      with open("./lista07-Dicionario/agendas.json", mode="r") as arquivo:
        agendas_json = json.load(arquivo)
        for obj in agendas_json:
          data = datetime.datetime.strptime(obj["_data"], "%d/%m/%Y %H:%M")
          a = Agenda(obj["_id"], data, obj["_confirmado"], obj["_idCliente"],
                     obj["_idServico"])
          cls.__agendas.append(a)
    except FileNotFoundError:
      pass

  @classmethod
  def salvar(cls):
    with open("./lista07-Dicionario/agendas.json", mode="w") as arquivo:
      agendas_json = []
      for agenda in cls.__agendas:
        agenda_dict = {
          "_id": agenda.get_id(),
          "_data": agenda.get_data().strftime("%d/%m/%Y %H:%M"),
          "_confirmado": False,
          "_idCliente": 0,
          "_idServico": 0,
        }
        agendas_json.append(agenda_dict)
      json.dump(agendas_json, arquivo, indent=4)
