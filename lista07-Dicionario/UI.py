from views import Views
from datetime import datetime
from datetime import timedelta

class UI:

  def main():
    op = UI.menu1()
    while op != 99:
      if op == 1:
        op = UI.menu2(op)
        while op != 99:
          if op == 1:
            UI.InserirCliente()
          elif op == 2:
            UI.ListarCliente()
          elif op == 3:
            UI.AtualizarCliente()
          elif op == 4:
            UI.ExcluirCliente()
          op = UI.menu2(op)
      elif op == 2:
        op = UI.menu2(op)
        while op != 99:
          if op == 1:
            UI.InserirServico()
          elif op == 2:
            UI.ListarServico()
          elif op == 3:
            UI.AtualizarServico()
          elif op == 4:
            UI.ExcluirServico()
          op = UI.menu2(op)
      elif op == 3:
        op = UI.menu2(op)
        while op != 99:
          if op == 1:
            UI.InserirAgenda()
          elif op == 2:
            UI.ListarAgenda()
          elif op == 3:
            UI.AtualizarAgenda()
          elif op == 4:
            UI.ExcluirAgenda()
          elif op == 5:
            UI.Agenda_Abrir_Agenda_do_Dia()
          op = UI.menu2(op)
          

      op = UI.menu1()

  def menu1():
      print('OPERAÇÕES')
      print('---------------------------')
      print('1 - Cliente')
      print('2 - Serviços')
      print('3 - Agenda')
      print('99 - Fechar programa')
      return int(input('Digite a opção desejada: '))

  def menu2(category):
      print('---------------------------')
      if category == 3:
          print('1 - Inserir')
          print('2 - Listar')
          print('3 - Atualizar')
          print('4 - Excluir')
          print('5 - Agenda do Dia')
      else:
          print('1 - Inserir')
          print('2 - Listar')
          print('3 - Atualizar')
          print('4 - Excluir')
      print('99 - Voltar')
      return int(input('Digite a opção desejada: '))
  def InserirCliente():
    nome = input('Digite o nome do cliente: ')
    email = input('Digite seu email: ')
    fone = int(input('Digite o número do seu telefone: '))
    Views.cliente_inserir(nome, email, fone)
    print('Cliente inserido com sucesso')

  def ListarCliente():
    for cliente in Views.cliente_listar():
      print(cliente)

  def AtualizarCliente():
    UI.ListarCliente()
    id = int(input('Digite o id que será alterado: '))
    nome = input('Digite o nome do cliente: ')
    email = input('Digite seu email: ')
    fone = int(input('Digite o número do seu telefone: '))
    Views.cliente_atualizar(id,nome, email, fone)
    print('Cliente atualizado com sucesso')

  def ExcluirCliente():
    UI.ListarCliente()
    id = int(input('Qual cliente será excluido: '))
    Views.cliente_excluir(id)
    print('Cliente excluido com sucesso')

  def InserirServico():
    descricao = input('Digite a descrição do serviço: ')
    valor = int(input('Digite o valor do serviço: '))
    duracao = int(input('Digite a duração do serviço: '))
    Views.servico_inserir(descricao, valor, duracao)
    print('Serviço inserido com sucesso')

  def ListarServico():
    for servico in Views.servico_listar():
      print(servico)

  def AtualizarServico():
    UI.ListarServico()
    id = int(input('Digite o id que será alterado: '))
    descricao = input('Digite a descrição do serviço: ')
    valor = int(input('Digite o valor do serviço: '))
    duracao = int(input('Digite a duração do serviço: '))
    Views.servico_atualizar(id,descricao,valor,duracao)
    print('Serviço atualizado com sucesso')

  def ExcluirServico():
    UI.ListarServico()
    id = int(input('Digite o id que será excluído: '))
    Views.servico_excluir(id)
    print('Serviço excluido com sucesso')

  def InserirAgenda():
    data_input = input('Digite a data disponibilizada: ')
    data = datetime.strptime(data_input, "%d/%m/%Y %H:%M")
    Views.agenda_inserir(data)
    print('Agenda inserida com sucesso')

  def ListarAgenda():
    for agenda in Views.agenda_listar():
      print(agenda)

  def AtualizarAgenda():
    UI.ListarAgenda()
    id = int(input('Digite o id que será alterado: '))
    data_input = input('Digite a data disponibilizada: ')
    data = datetime.datetime.strptime(data_input, "%d/%m/%Y %H:%M")
    Views.agenda_atualizar(id, data)
    print('Agenda atualizado com sucesso')

  def ExcluirAgenda():
    UI.ListarAgenda()
    id = int(input('Digite o id que será excluído: '))
    Views.agenda_excluir(id)
    print('Agenda excluido com sucesso')
  def Agenda_Abrir_Agenda_do_Dia():
    lista = []
    data = datetime.strptime(input('Digite a data disponibilizada:(D/M/A H:M): '),"%d/%m/%Y %H:%M")
    intervalo =  timedelta(hours=int(input('Horas: ')),minutes=int(input('Minutos: ')))
    hfim = input('Horario final: ')
    data_final = datetime.strptime(f"{data.date()} {hfim}","%Y-%m-%d %H:%M")
    while data < data_final:
      data= data + intervalo
      lista.append(data)
    
    Views.agenda_abrir_agenda_do_dia(lista)
    


UI.main()
