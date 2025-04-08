#Crie um programa que mostre na tela todos os números pares entre 1 e 50
from time import sleep
print('Esses são os números pares de 1 à 50')
sleep(1)
for c in range(0, 51):
    if c % 2  == 0:
        print(c, end=', ')
    sleep(0.2)
else:
    print()
print('E esses os ímpares')
sleep(1)
for d in range(1, 50, 2):
    print(d, end=', '), sleep(0.3)
