import random


class Bingo:

  def __init__(self):
    self.__numBolas = 10
    self.__sorteadas = []

  def Iniciar(self, numBolas):
    if numBolas > 0:
      self.__numBolas = numBolas
      self.__sorteadas = []
    else:
      raise ValueError()

  def proximo(self):
    if len(self.__sorteadas) == self.__numBolas:
      return -1
    x = random.randrange(1, self.__numBolas + 1)
    while x in self.__sorteadas:
      x = random.randrange(1, self.__numBolas + 1)

    self.__sorteadas.append(x)
    return x

  def sorteadas(self):
    return self.__sorteadas


class UI:

  def main():
    op = int(input('1- Novo Jogo , 2 -sortear , 3 -sortedas, 0 - encerrar'))
    B = Bingo()
    while True:
      if op == 1:
        valor = int(input('Me diga o número de Bolas:'))
        B.Iniciar(valor)

      elif op == 2:
        print(B.proximo())

      elif op == 3:
        print(B.sorteadas())
      elif op == 0:
        break
      op = int(input('1- Novo Jogo , 2 -sortear , 3 -sortedas, 0 - encerrar'))


UI.main()
