print('Digite a base e a altura do retângulo')
base=float(input())
altura=float(input())
area=(base*altura)
perimetro=(base*2)+(altura*2)
diagonal= (base**2+altura**2)**0.5
print(f'Área = {area:.2f} - Périmetro = {perimetro:.2f} - Diagonal = {diagonal:.2f}')