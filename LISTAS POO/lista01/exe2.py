class Disciplina:
    def __init__(self, nome, notas_bimestrais, nota_prova_final=0):
        self.nome = nome
        self.notas_bimestrais = notas_bimestrais
        self.nota_prova_final = nota_prova_final
    
    def calcular_media_parcial(self):
        pesos = [2, 2, 3, 3]
        soma = sum(nota * peso for nota, peso in zip(self.notas_bimestrais, pesos))
        return soma / sum(pesos)
    
    def calcular_media_final(self):
        media_parcial = self.calcular_media_parcial()
        if media_parcial >= 60:
            return media_parcial
        else:
            return (media_parcial + self.nota_prova_final) / 2

# Exemplo de uso da classe
notas = [70, 80, 75, 85]
disciplina = Disciplina("Matemática", notas, 60)
print("Média Parcial:", disciplina.calcular_media_parcial())
