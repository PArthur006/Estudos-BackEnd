#Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
#Guarde esses resultados em um dicionário em Python.
#No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

cont = 1
from random import randint
from time import sleep
dados = {}
dados['Jogador1'] = randint(1, 6)
dados['Jogador2'] = randint(1, 6)
dados['Jogador3'] = randint(1, 6)
dados['Jogador4'] = randint(1, 6)
print('Rolando dados...')
sleep(1)
for k, v in dados.items():
    print(f'{k} = {v}')
    sleep(1)
print('-:-' * 15)
print(' '*13, 'RANKING')
for i in sorted(dados, key=dados.get, reverse=True):
    print(f'{" "*10}{cont}°  {i} = {dados[i]}')
    cont += 1
