class Disciplina:
  def __init__(self,nome,nota1,nota2,nota3,nota4):
    self.nome=nome
    self.nota1=nota1
    self.nota2=nota2
    self.nota3=nota3
    self.nota4=nota4
    self.notarec=0
  def mediaparcial(self):
    return (((self.nota1*2)+(self.nota2*2)+(self.nota3*3)+(self.nota4*3))/10)
  
  def mediafinal(self,notafinal):
    Rec=self.mediaparcial()+notafinal/2.0
    if Rec>=60:
      return f'A sua média com a prova final é de {Rec}\nAprovado'
    else:
      return f'A sua média com a prova final é de {Rec}\nReprovado:('
      
nome=input('Nome da disciplina: ')
nota1=int(input('Nota1: '))
nota2=int(input('Nota2: '))
nota3=int(input('Nota3: '))
nota4=int(input('Nota4: '))
D=Disciplina(nome,nota1,nota2,nota3,nota4)
print(D.mediaparcial())
if D.mediaparcial()>=60:
  print('Situação: Aprovado')
else:
  print('Situação: Prova Final')
  notafinal=int(input('Nota final: '))
  print(D.mediafinal(notafinal))

      