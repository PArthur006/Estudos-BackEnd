#Faça um programa que leia um número de 0 à 9999 e mostre na tela cada
#um dos digitos separados.

from time import sleep
n1 = int(input('Digite um número entre 0 e 9999: '))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
um = n1 // 1000 % 10
print('Analisando número {}...'.format(n1))
sleep(3.00)
print('A unidade é {}\nA dezena é {}\nA centena é {}\nE a unidade de milhar é {}'.format(u, d, c, um))
