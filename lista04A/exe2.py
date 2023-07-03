import datetime
class Musica:
  def __init__(self, titulo, artista, album, duracao):
    self.__titulo = titulo
    self.__artista = artista
    self.__album = album
    self.__data_inclusao = datetime.datetime.today()
    self.__duracao = duracao
  def __str__(self):
    data = self.__data_inclusao.strftime("%d/%m/%Y")
    return f"{self.__titulo} - {self.__artista} - {self.__album} - {data} - {self.__duracao}"
  def get_duracao(self):
    return self.__duracao
    
class PlayList:
  def __init__(self, nome, descricao):
    self.__nome = nome
    self.__descricao = descricao
    self.__musicas = []
  def inserir(self, m):
    if m in self.__musicas:
      raise ValueError("música já inserida na playlist")
    else:  
      self.__musicas.append(m)
  def listar(self):
    return self.__musicas
  def tempo_total(self): 
    total = datetime.timedelta()
    for k in self.__musicas:
      total += k.get_duracao()
    return total

class UI:
  @staticmethod
  def main():
    p = PlayList("Infoweb 2", "Playlist de Infoweb 2")    
    print("1 - Inserir música, 2 - Listar, 3 - Tempo total, 0 - Fim")
    op = int(input())
    while op != 0:
      if op == 1:
        titulo = input("Título da música: ")
        artista = input("Banda: ")
        album = input("Álbum: ")
        duracao_txt = input("Duração (mm:ss): ")
        #duracao = datetime.timedelta.strptime(duracao_txt, "%M:%S")
        min, sec = map(int, duracao_txt.split(":"))
        duracao = datetime.timedelta(minutes=min, seconds=sec)
        m = Musica(titulo, artista, album, duracao)
        p.inserir(m)
      if op == 2:
        for k in p.listar(): print(k)
      if op == 3:  
        print(p.tempo_total())
      print("1 - Inserir música, 2 - Listar, 3 - Tempo total, 0 - Fim")
      op = int(input())

UI.main()
