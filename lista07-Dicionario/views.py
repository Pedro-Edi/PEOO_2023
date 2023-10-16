import datetime
from cliente import Cliente,NCliente
from servico import Servico,NServico
from agenda import Agenda,NAgenda



class Views:

  @classmethod
  def cliente_inserir(cls,nome,email,fone):
    cliente=Cliente(0,nome,email,fone)
    NCliente.inserir(cliente)

  @classmethod
  def cliente_listar(cls):
    return NCliente.listar()

  @classmethod
  def cliente_atualizar(cls,id,nome,email,fone):
    cliente = Cliente(id,nome,email,fone)
    NCliente.atualizar(cliente)
    
  @classmethod
  def cliente_excluir(cls,id):
    cliente = Cliente(id,"","","")
    NCliente.excluir(cliente)

  @classmethod
  def servico_inserir(cls,descricao,valor,duracao):
    servico=Servico(0,descricao,valor,duracao)
    NServico.inserir(servico)

  @classmethod
  def servico_listar(cls):
    return NServico.listar()

  @classmethod
  def servico_atualizar(cls,id,descricao,valor,duracao):
    servico = Servico(id,descricao,valor,duracao)
    NServico.atualizar(servico)
    
  @classmethod
  def servico_excluir(cls,id):
    cliente = Servico(id,"","","")
    NServico.excluir(cliente)
    
  @classmethod
  def agenda_inserir(cls,data):
    agenda= Agenda(0,data,False,0,0)
    NAgenda.inserir(agenda)

  @classmethod
  def agenda_listar(cls):
    return NAgenda.listar()

  @classmethod
  def agenda_atualizar(cls,id,data):
    agenda= Agenda(id,data,False,0,0)
    NAgenda.atualizar(agenda)
    
  @classmethod
  def agenda_excluir(cls,id):
    agenda =Agenda(id,"","","","")
    NAgenda.excluir(agenda)

  @classmethod
  def agenda_abrir_agenda_do_dia(cls,lista):
    for d in lista:
      NAgenda.inserir(Agenda(0,d,False,0,0))
    