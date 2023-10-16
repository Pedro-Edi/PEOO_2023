import json
import datetime

class Aluno:
  def __init__(self,id,nome,matricula,nasc):
    self.__id = id
    self.__nome = nome
    self.__matricula = matricula
    self.__nasc = nasc

  def get_id(self): return self.__id
  def get_nome(self): return self.__nome
  def get_matricula(self): return self.__matricula
  def get_nasc(self): return self.__nasc
  def set_id(self,id): self.__id = id
  def set_nome(self,nome): self.__nome = nome
  def set_matricula(self,matricula): self.__matricula = matricula
  def set_nasc(self,nasc): self.__nasc = nasc
  def __str__(self):
    return f"{self.__id} - {self.__nome} - {self.__matricula} - {self.___nasc.strftime('%d/%m/%Y')}"

class NAluno:
  
  __alunos= []
  
  @classmethod
  def inserir(cls,obj):
    NAluno.abrir()
    id = 0
    for aluno in cls.__alunos:
      id = aluno.get_id()
    obj.set_id(id+1)
    cls.__alunos.append(obj)
    NAluno.salvar()

  @classmethod
  def listar(cls):
    NAluno.abrir()
    return cls.__alunos

  @classmethod
  def listar_id(cls,id):
    NAluno.abrir()
    for aluno in cls.__alunos:
      if id == aluno.get_id():
        return aluno
    return None

  @classmethod
  def atualizar(cls,obj):
    NAluno.abrir()
    aluno = NAluno.listar_id(obj.get_id())
    aluno.set_nome(obj.get_nome())
    aluno.set_matricula(obj.get_matricula())
    aluno.set_nasc(obj.get_nasc())
    NAluno.salvar()


  @classmethod
  def excluir(cls,obj):
    NAluno.abrir()
    aluno = NAluno.listar_id(obj.get_id())
    cls.__alunos.remove(aluno)
    NAluno.salvar()
    
  import datetime
  @classmethod
  def abrir(cls):
    cls.__alunos = []
    try:
      with open("alunos.json", mode="r") as arquivo:
        alunos_json = json.load(arquivo)
        for obj in alunos_json:
          data = datetime.datetime.strptime(obj["_nasc"], "%d/%m/%Y")
          a = Aluno(obj["_id"], obj["_nome"], obj["_matricula"], data)
          cls.__alunos.append(a)
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        pass

      
  @classmethod
  def salvar(cls):
    alu=[]
    with open("alunos.json",mode="w") as arquivo:
      for aluno in cls.__alunos:
        a= {
          "_id": aluno.get_id(),
          "_nome": aluno.get_nome(),
          "_matricula": aluno.get_matricula(),
          "_nasc": aluno.get_nasc().strftime("%d/%m/%Y")
        }
        alu.append(a)
      json.dump(alu,arquivo,indent=4,default=vars)
        
  @classmethod
  def aniversariante(cls,mes):
    NAluno.abrir()
    lista=[]
    for aluno in cls.__alunos:
      if aluno.get_nasc().moth == mes:
        lista.append(aluno)
    return lista
class UI:
  def main():
    op= UI.menu()
    while op!=99:
      if op==1: UI.InserirAluno()
      if op==2: UI.ListarAluno()
      if op==3: UI.AtualizarAluno()
      if op==4: UI.ExcluirAluno()
      if op==5: UI.AniversarianteAluno()
      op= UI.menu()

  

  def menu():
    print('1-inserir , 2- listar, 3-atualizar 4 - excluir, 5 - aniversariante, 99-fechar progama')
    return int(input('Digite: '))

  def InserirAluno():
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    nasc_txt = input("Digite o aniversario do aluno: ")
    nasc = datetime.datetime.strptime(nasc_txt,"%d/%m/%Y")
    a = Aluno(0,nome,matricula,nasc)
    NAluno.inserir(a)
  
  def ListarAluno():
    for aluno in NAluno.listar():
      print(aluno)
  def atualizar():
    id=int(input())
    nome = input("Digite o nome do aluno: ")
    matricula = input("Digite a matricula do aluno: ")
    nasc_txt = input("Digite o aniversario do aluno: ")
    nasc = datetime.datetime.strptime(nasc_txt,"%d/%m/%Y")
    NAluno.atualizar(Aluno(id, nome, matricula, nasc))
    print('Aluno atualizado com sucesso')

  def ExcluirAluno():
    UI.ListarAluno()
    id = int(input('Qual cliente será excluido: '))
    a= Aluno(id, "", "", "")
    NAluno.excluir(a)
    print('Aluno excluido com sucesso')

  def AniversarianteAluno():
    mes=int(input())
    n=NAluno()
    d=n.aniversariante(mes)
    for x in d:
      print(x)

UI.main()