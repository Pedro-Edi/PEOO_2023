#1049 – Animal
A=input()
B=input()
C = input()
x=''
if (A=='vertebrado' and B=='ave' and C=='carnivoro'):
  x='aguia'
if (A=='vertebrado' and B=='ave' and C=='onivoro'):
  x='pomba'
if (A=='vertebrado' and B=='mamifero' and C=='onivoro'):
  x='homem'
if (A=='vertebrado' and B=='mamifero' and C=='herbivoro'):
  x='vaca'
if (A=='invertebrado' and B=='inseto' and C=='hematofago'):
  x='pulga'
if (A=='invertebrado' and B=='inseto' and C=='herbivoro'):
  x='lagarta'
if (A=='invertebrado' and B=='anelideo' and C=='hematofago'):
  x='sanguessuga'
if (A=='invertebrado' and B=='anelideo' and C=='onivoro'):
  x='minhoca'
print(x)