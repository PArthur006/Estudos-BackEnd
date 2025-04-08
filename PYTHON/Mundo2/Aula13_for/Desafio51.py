#Desenvolva um programa que leia o primeiro termo de uma razão de uma PA
#No final, mostre os 10 primeiros termos dessa progressão
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Informe a razão: '))
cont = 0
soma = 0
for c in range(1, 11):
    soma += (a1 + r)
    cont += 1
    print('a{} é = {}'.format(cont, soma))



#a1 + r = a2
#a2 + r = a3
#a3 + r = a4
