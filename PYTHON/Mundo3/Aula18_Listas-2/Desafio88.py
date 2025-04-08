#Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
#O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60
#para cada jogo, cadastrando tudo em uma lista composta.

print(' ' * 10, '\033[1;30mMega Sena\033[m')
numeros = []
jogos = []
import random
from time import sleep
quantidade = int(input('Quantos jogos você quer realizar? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        num = random.randint(0, 60)
        if num not in numeros:
            numeros.append(num)
            cont += 1
        if cont >= 6:
            break
    numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()
    total += 1
for n, j in enumerate(jogos):
    print(f'\033[37;40mJogo {n+1}: {j}\033[m')
    sleep(1)
