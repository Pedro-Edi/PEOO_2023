
class EquacaoSegundoGrau:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def Delta(self):
        return self.b ** 2 - 4 * self.a * self.c

    def TemRaizesReais(self):
        delta = self.Delta()
        return delta >= 0

    def Raiz1(self):
        if self.TemRaizesReais():
            delta = self.Delta()
            return (-self.b + delta ** 0.5) / (2 * self.a)
        else:
            return None

    def Raiz2(self):
        if self.TemRaizesReais():
            delta = self.Delta()
            return (-self.b - delta ** 0.5) / (2 * self.a)
        else:
            return None

    def ToString(self):
        return f"Equação do 2º Grau - Coeficientes: a = {self.a}, b = {self.b}, c = {self.c}"
class UIEquacaoSegundoGrau:
    @staticmethod
    def main():
        print("Questão 3: Equação do 2º Grau")
        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))

            equacao = EquacaoSegundoGrau(a, b, c)

            print("Equação criada:")
            print(equacao.ToString())

            delta = equacao.Delta()
            print("Delta:", delta)

            if equacao.TemRaizesReais():
                raiz1 = equacao.Raiz1()
                raiz2 = equacao.Raiz2()
                print("Raiz 1:", raiz1)
                print("Raiz 2:", raiz2)
            else:
                print("A equação não possui raízes reais.")
        except ValueError as error:
            print("Erro:", str(error))
