
'''
x ={}
x= {'PB' : 'Natal', 'TO': 'Piai'}
x['QUERETARO'] = 'MY EGGS'
for f in x:
  print(f)
for ite in x.items(): print(ite)

for key, value in x.items(): print(key, value)
'''
import json

dados = {"nome": "Alice", "idade": 28}

print(json.dumps(dados))
