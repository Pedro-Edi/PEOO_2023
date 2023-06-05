class Retangulo:
    def __init__(self, base, altura):
        if base > 0 and altura > 0:
            self.base = base
            self.altura = altura
        else:
            raise ValueError("A base e a altura devem ser positivas.")

    def SetBase(self, base):
        if base > 0:
            self.base = base
        else:
            raise ValueError("A base deve ser positiva.")

    def SetAltura(self, altura):
        if altura > 0:
            self.altura = altura
        else:
            raise ValueError("A altura deve ser positiva.")

    def GetBase(self):
        return self.base

    def GetAltura(self):
        return self.altura

    def CalcArea(self):
        return self.base * self.altura

    def CalcDiagonal(self):
        return (self.base ** 2 + self.altura ** 2) ** 0.5

    def ToString(self):
        return f"Retângulo - Base: {self.base}, Altura: {self.altura}"

class UIRetangulo:
    @staticmethod
    def main():
        print("Questão 1: Retângulo")
        try:
            base = float(input("Digite a base do retângulo: "))
            altura = float(input("Digite a altura do retângulo: "))

            retangulo = Retangulo(base, altura)

            print("Retângulo criado:")
            print(retangulo.ToString())

            print("Área:", retangulo.CalcArea())
            print("Diagonal:", retangulo.CalcDiagonal())
        except ValueError as error:
            print("Erro:", str(error))
          