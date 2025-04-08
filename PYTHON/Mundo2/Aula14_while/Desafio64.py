#Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o
#usuário digitar o número 999, que é a condição de parada. No final, mostre quantos números foram
#digitados e qual foi a soma entre eles (desconsiderando o flag)
cont = soma = 0
n = int(input('Digite qualquer número\033[31m[Digite 999 para encerrar]\033[m: '))
while n != 999:
    cont += 1
    soma += n
    n = int(input('Digite qualquer número: '))
print('''Você informou {} números
E a soma entre eles foi {}'''.format(cont, soma))
