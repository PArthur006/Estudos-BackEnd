# Faça um programa que tenha uma função chamada maior() que receba vários parâmetros
# com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles é maior.


numeros = list()
from random import randint
from time import sleep


def maior(num):
    maiornum = 0
    for i, v in enumerate(numeros):
        if i == 0:
            maiornum = v
        else:
            if v > maiornum:
                maiornum = v
    print('~'*30)
    print('Analisando os números...')
    sleep(1.5)
    for i, v in enumerate(numeros):
        print(v, end=' ')
        sleep(0.5)
    print(f'. Foram sorteados {len(numeros)} números. Dentre eles, o maior é {maiornum}')
    sleep(0.5)
    numeros.clear()


for c in range(0, 6):
    numeros.append(randint(0, 10))
maior(numeros)
for c in range(0,3):
    numeros.append(randint(0, 10))
maior(numeros)
for c in range(0, 2):
    numeros.append(randint(0, 10))
maior(numeros)
for c in range(0, 1):
    numeros.append(randint(0, 10))
maior(numeros)
