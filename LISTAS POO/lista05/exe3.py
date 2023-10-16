import datetime


class lote:

  def __init__(self, numero, vencimento, qtd):
    self.__numero = None
    self.__vencimento = 0
    self.__qtd = 0
    self.set_numero(numero)
    self.set_vencimento(vencimento)
    self.set_qtd(qtd)

  def set_numero(self, numero):
    if int(numero) >= 0:
      self.__numero = numero
    else:
      raise ValueError('Não ha numero de lote')

  def set_vencimento(self, vencimento):
    if vencimento.year >= 2020:
      self.__vencimento = vencimento
    else:
      raise ValueError('Não há lotes com esse ano')

  def set_qtd(self, qtd):
    if qtd >= 0:
      self.__qtd = qtd
    else:
      raise ValueError('Digite uma quantidade Válida')

  def get_numero(self):
    return self.__numero

  def get_vencimento(self):
    return self.__vencimento

  def get_qtd(self):
    return self.__qtd

  def __str__(self):
    return f'{self.__numero} - {self.__vencimento} - {self.__qtd}'


class Medicamento:

  def __init__(self):
    self.__lista = []

  def inserir(self, l):
    self.__lista.append(l)

  def listar(self):
    return self.__lista

  def qtd(self):
    total = 0
    for x in self.__lista:
      total += x.get_qtd()
    return f'O total é {total}'

  def vencidos(self):
    hoje = datetime.datetime.today()
    lista = []
    for x in self.__lista:
      if x.get_vencimento() < hoje:
        lista.append(x.get_numero())

    if len(lista) == 0:
      return f'Não há vencidos'
    else:
      return f'Os vencidos são: {" ".join(str(item) for item in lista)}'


Remedio = Medicamento()
for x in range(3):
  numero = input('Qual o numero: ')
  vencimento = datetime.datetime.strptime(input('DIA/MÊS/ANO: '), "%d/%m/%Y")
  qtd = int(input('Qual a quantidade: '))
  L = lote(numero, vencimento, qtd)

  Remedio.inserir(L)
for x in Remedio.listar():
  print(x)
print(Remedio.vencidos())
print(Remedio.qtd())
