'''Ler o nome completo de uma pessoa e mostrar a mensagem: “Bem-vindo ao Python, <xxx>”, onde <xxx> é o
primeiro nome da pessoa.'''
nome=(input('Digite seu nome completo: ').split())
print(f'Bem vindo ao Pythn,{nome[0]}')