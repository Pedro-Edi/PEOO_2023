class Disciplina:
  def __init__(self):
    self.__nome=None
    self.__nota1=0
    self.__nota2=0
    self.__nota3=0
    self.__nota4=0
    self.__notafinal=0
    self.__disciplinas=['Portugês','Matemática','Química','Física','Biologia','História','Geografia','Sociologia','Filosofia','Educação Física','Inglês']
  def set_nome(self,s):
    if s in self.__disciplinas:
      self.__nome=s
    else : raise ValueError()
  def set_nota1(self,n):
    if 0<=n<=100 : self.__nota1=n
    else: raise ValueError()
  def set_nota2(self,n):
    if 0<=n<=100 : self.__nota2=n
    else: raise ValueError()
  def set_nota3(self,n):
    if 0<=n<=100 : self.__nota3=n
    else: raise ValueError()
  def set_nota4(self,n):
    if 0<=n<=100 : self.__nota4=n
    else: raise ValueError()
  def set_notafinal(self,n):
    if 0<=n<=100 : self.__notafinal=n
    else: raise ValueError()
  

  def get_nome(self):
    return self.__nome
  def get_nota1(self):
    return self.__nota1
  def get_nota2(self):
    return self.__nota2
  def get_nota3(self):
    return self.__nota3
  def get_nota4(self):
    return self.__nota4
  def get_notafinal(self):
    return self.__notafinal

  def calc_media_parcial(self):
    M=(self.__nota1*2+self.__nota2*2+self.__nota3*3+self.__nota4*3)/10
    return M
  def calc_media_final(self):
    return (self.calc_media_parcial()+self.__notafinal)/2
D=Disciplina()
D.set_nome(input('NOME DA MATÉRIA: '))
D.set_nota1(int(input('Nota1: ')))
D.set_nota2(int(input('Nota2: ')))
D.set_nota3(int(input('Nota3: ')))
D.set_nota4(int(input('Nota4: ')))
if D.calc_media_parcial()>60:
  print(f'Média: {D.calc_media_parcial()}\nSituação: Aprovado')
else:
  print(f'Média: {D.calc_media_parcial()}\nSituação: Prova Final')
  D.set_notafinal(int(input('Nota Final: ')))
  if D.calc_media_final()<60:
    print(f'Média final foi de {D.calc_media_final()}\nSituação: Reprovado')
  else:
    print(f'Média final foi de {D.calc_media_final()}\nSituação: Aprovado')
    