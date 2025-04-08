#Faça um programa que leia um número inteiro e diga se ele é primo ou não.
tot = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        tot += 1
if tot == 2:
    print('O número {} foi divisível {} vezes\nPor isso ele é primo'.format(num, tot))
else:
    print('O número {} foi divisível {} vezes\nE por isso não é um número primo'.format(num, tot))
