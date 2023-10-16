import datetime


class Amigo:

  def __init__(self, nome, nasc):
    self.__nome = nome
    self.__nasc = nasc

  def __str__(self):
    return f"{self.__nome} - {self.__nasc.strftime('%d/%m/%Y')}"

  def idade(self):
    data_hoje = datetime.datetime.today()
    ida = data_hoje - self.__nasc
    return ida


class UI:

  def main():
    colegas = []
    indivi = []
    for i in range(1, 3):
      colega = input('Digite o nome do seu amigo: ')
      dia, mes, ano = map(int, (input('Digite sua idade: ')).split("/"))
      data = datetime.datetime(ano, mes, dia)
      x = Amigo(colega, data)
      colegas.append(x.idade())
      indivi.append(x.__str__())
    menor_valor = min(colegas)  # Encontra o menor valor na lista
    posicao_menor = None  # Variável para armazenar a posição do menor valor

    for indice, valor in enumerate(colegas):
      if valor == menor_valor:
        posicao_menor = indice
        break
    print(indivi[posicao_menor])


UI.main()
