class Disciplina:

  def __init__(self):
    self.nome = 0
    self.nota1 = 0
    self.nota2 = 0
    self.nota3 = 0
    self.nota4 = 0
    self.notafinal = 0

  def cal_nota(self):
    return ((self.nota1 * 2) + (self.nota2 * 2) + (self.nota3 * 3) +(self.nota4 * 3)) / 10
  def cal_recu(self):
    return self.cal_nota() + self.notafinal / 2


Materia = Disciplina()
Materia.nome = input()
Materia.nota1 = int(input())
Materia.nota2 = int(input())
Materia.nota3 = int(input())
Materia.nota4 = int(input())
print(Materia.cal_nota())
if Materia.cal_nota() < 60:
  Materia.notafinal = int(input())
  print(Materia.cal_recu())
