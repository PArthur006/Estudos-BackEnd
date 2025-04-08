#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário
#Digitar 999, que é a condição de parada. No final mostre quantos números foram digitados e qual
#Foi a soma entre eles.
cont = 1
n = int(input('Digite qualquer número: '))
soma = n
while True:
    n = int(input('Digite outro número:[999 para encerrar] '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'''Você digitou {cont} números
E a soma entre eles foi {soma}''')

