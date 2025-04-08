#Crie um programa que leia um número e diga se ele é PAR ou ÍMPAR.
n = int(input('Digite um número: '))
res = n % 2
if res == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))
