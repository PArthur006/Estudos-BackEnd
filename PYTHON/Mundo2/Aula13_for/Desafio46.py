#Faça um programa que mostre na tela uma contagem regressiva para o estouro
#de fogos de artíficios, indo de 10 até 0, com uma pausa de 1 segundo.

from time import sleep
print('Iniciando contagem regressiva!')
for c in range(10, 0, -1):
    print(int(c)), sleep(1)

for n in range(5):
    num = ('\033[33m🎆\033[m'*20)
    print(num)
