import datetime
class Paciente:
  def __init__(self,nome,cpf,telefone,nascimneto):
    self.__nome=nome
    self.__cpf=cpf
    self.__telefone=telefone
    self.__nascimento=nascimneto
  def idade(self):
    y=datetime.datetime.today()
    data=y-self.__nascimento
    anos=data.days//365
    meses= (data.days%365)//30
    dias=(data.days%365)-(meses*30)
    return f'VOCE TEM {anos} anos , {meses} meses, {dias} dias'
  def __str__(self):
    return f'\nNome : {self.__nome}\nCpf: {self.__cpf}\nTelefone : {self.__telefone}\nNascimento :{self.__nascimento}'
class UI:
  def main():
    nome=input('Digite seu nome: ')
    cpf=input('Seu cpf (xxx.xxx.xxx-xx): ')
    telefone=input('Seu telefone ((xx) xxxxx-xxxx): ')
    num1,num2,num3=map(int,input('ME DIGA SUA IDADE (DIA/MES/ANO) : ').split('/'))
    nascimento=datetime.datetime(  num3, num2 , num1 )
    print(nascimento)
    p=Paciente(nome,cpf,telefone,nascimento)
    print(p)
    print(f'IDADE = {p.idade()}')
UI.main()