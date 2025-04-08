# Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
# A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função
# vai mostrar a soma entre todos os valores pares sorteados pela função anterior.


from time import sleep
from random import randint
números = list()


def sorteia():
    print('   Gerando números...')
    sleep(1.5)
    print('Os números gerados foram: ', end='')
    sleep(1)
    for c in range(1, 6):
        números.append(randint(0, 10))
        print(f'{números[-1]} ', end='')
        sleep(0.5)
    print('')


def somaPar():
    pares = 0
    for i, v in enumerate(números):
        if v % 2 == 0:
            pares += v
    sleep(1)
    print(f'Dentre os números {números}, a soma de todos os pares é {pares}.')


sorteia()
somaPar()
