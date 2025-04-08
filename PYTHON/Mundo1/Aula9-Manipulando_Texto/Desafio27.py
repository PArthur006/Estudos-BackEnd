#Faça um programa que leia o nome completo de uma pessoa, e em seguida mostre
#o primeiro e o ultimo nome separadamente
nome = str(input('Digite seu nome completo: ')).strip()
n = nome.split()
print('Seu primeiro nome é {}'.format(n[0]))
print('Seu último nome é {}'.format(n[len(n)-1]))
