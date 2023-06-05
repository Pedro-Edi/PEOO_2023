class Disciplina:
    def __init__(self, nome):
        self.__nome = nome
        self.__notas_bimestres = [0] * 4
        self.__nota_prova_final = 0
    
    def calcular_media_parcial(self):
        pesos = [2, 2, 3, 3]
        media = sum(nota * peso for nota, peso in zip(self.__notas_bimestres, pesos)) / sum(pesos)
        return media
    
    def calcular_media_final(self):
        media_parcial = self.calcular_media_parcial()
        if media_parcial < 60:
            media_final = (media_parcial + self.__nota_prova_final) / 2
        else:
            media_final = media_parcial
        return media_final
    
    def get_nome(self):
        return self.__nome
    
    def set_nome(self, nome):
        self.__nome = nome
    
    def get_notas_bimestres(self):
        return self.__notas_bimestres
    
    def set_notas_bimestres(self, notas):
        self.__notas_bimestres = notas
    
    def get_nota_prova_final(self):
        return self.__nota_prova_final
    
    def set_nota_prova_final(self, nota):
        self.__nota_prova_final = nota

# Exemplo de uso da classe
disciplina = Disciplina("Matemática")
print("Disciplina:", disciplina.get_nome())

# Definindo notas bimestrais
notas_bimestres = []
for i in range(4):
    nota = float(input(f"Digite a nota do {i+1}º bimestre: "))
    notas_bimestres.append(nota)
disciplina.set_notas_bimestres(notas_bimestres)

# Definindo nota da prova final
nota_prova_final = float(input("Digite a nota da prova final: "))
disciplina.set_nota_prova_final(nota_prova_final)

# Calculando médias
media_parcial = disciplina.calcular_media_parcial()
media_final = disciplina.calcular_media_final()
print("Média Parcial:", media_parcial)
print("Média Final:", media_final)
