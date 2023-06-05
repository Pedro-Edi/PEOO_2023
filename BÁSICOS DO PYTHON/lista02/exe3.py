'''Calcular a média parcial de uma disciplina semestral, dadas as notas dos 1o e 2o bimestres (pesos 2 e 3).
Considerar as notas com valores inteiros entre zero e cem.'''

nota1=int(input('Digite a nota do primeiro bimestre da disciplina:\n'))
nota2=int(input('Digite a nota do segundo bimestre da disciplina:\n'))
if nota1>100 or nota1<0 or nota2>100 or nota2<0 :
   print('Só aceitamos valores inteiros , menores ou igual a 100 e maiores ou igual a 0')
else:    
  media=((nota1*2)+(nota2*3))/5
  print(f'Média parial = {media:.2f}')
