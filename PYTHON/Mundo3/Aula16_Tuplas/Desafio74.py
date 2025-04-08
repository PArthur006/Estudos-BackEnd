#Crie um programa que vai gerar 5 números aleatórios e colocar em uma tupla. Depois disso, mostre
#Mostre a listagem de números gerados e também indique o maior e o menor número gerado na tupla
maior = menor = 0
from random import randint
print('Os números gerados foram:', end=' ')
for c in range(0, 6):
    n = randint(0, 10)
    print(n, ','if c < 5 else ' ', end='')
print(' ')
print(f'O maior valor foi {max(maior)}')
print(f'E o menor foi {max(menor)}')
