import datetime

class Esporte:
    def __init__(self, nome, prova):
        self.__nome = ''
        self.__prova = ''
        self.__recordes = []
        self.setnome(nome)
        self.setprova(prova)

    def setnome(self, nome, comprimento_min=2, comprimento_max=50):
        if comprimento_min <= len(nome) <= comprimento_max:
            self.__nome = nome
        else:
            raise ValueError()

    def setprova(self, prova, comprimento_min=2, comprimento_max=50):
        if comprimento_min <= len(prova) <= comprimento_max:
            self.__prova = prova
        else:
            raise ValueError()

    def getnome(self):
        return self.__nome

    def getprova(self):
        return self.__prova

    def inserir(self, recorde):
        self.__recordes.append(recorde)

    def listar(self):
        return self.__recordes

class Recorde:
    def __init__(self, atleta, nacionalidade, data, tempo):
        self.__atleta = atleta
        self.__nacionalidade = nacionalidade
        self.__data = data
        self.__tempo = tempo

    def getatleta(self):
        return self.__atleta

    def getnacionalidade(self):
        return self.__nacionalidade

    def getdata(self):
        return self.__data

    def gettempo(self):
        return self.__tempo

    def __str__(self):
        return f"Atleta: {self.__atleta}, Nacionalidade: {self.__nacionalidade}, Data: {self.__data.strftime('%d/%m/%Y')}, Tempo: {self.__tempo}"

class UI:
    @staticmethod
    def main():
        op = int(input('1-Nome do esporte- 2-Novo recorde'))
        while op != 0:
            if op == 1:
                nome = input('Esporte: ')
                prova = input('Prova: ')
                x = Esporte(nome, prova)
            elif op == 2:
                atleta = input('Atleta: ')
                nacionalidade = input('Nacionalidade: ')
                data_txt = input('Data (dd/mm/aaaa): ')
                tempo_txt = input('Tempo (mm:ss): ')
                m, s = map(int, tempo_txt.split(":"))
                data = datetime.datetime.strptime(data_txt, "%d/%m/%Y")
                tempo = datetime.timedelta(minutes=m, seconds=s)
                f= Recorde(atleta, nacionalidade, data, tempo)
                x.inserir(f)
            elif op==3:
              for w in x.listar():
                print(w)

            op = int(input('1-Novo esporte - 2-Novo recorde'))


UI.main()
