class Frete:
    def __init__(self, distancia, peso):
        if distancia > 0 and peso > 0:
            self.distancia = distancia
            self.peso = peso
        else:
            raise ValueError("A distância e o peso devem ser positivos.")

    def SetDistancia(self, distancia):
        if distancia > 0:
            self.distancia = distancia
        else:
            raise ValueError("A distância deve ser positiva.")

    def SetPeso(self, peso):
        if peso > 0:
            self.peso = peso
        else:
            raise ValueError("O peso deve ser positivo.")

    def GetDistancia(self):
        return self.distancia

    def GetPeso(self):
        return self.peso

    def CalcFrete(self):
        return 0.01 * self.peso * self.distancia

    def ToString(self):
        return f"Frete - Distância: {self.distancia} km, Peso: {self.peso} kg"
class UIFrete:
    @staticmethod
    def main():
        print("Questão 2: Frete")
        try:
            distancia = float(input("Digite a distância do frete (em km): "))
            peso = float(input("Digite o peso da carga (em kg): "))

            frete = Frete(distancia, peso)

            print("Frete criado:")
            print(frete.ToString())

            print("Valor do frete:", frete.CalcFrete())
        except ValueError as error:
            print("Erro:", str(error))