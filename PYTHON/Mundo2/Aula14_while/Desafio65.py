#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a
#média entre eles e qual foi o maior e menor valores lidos. O programa deve perguntar ao usuário se
#ele quer ou não continuar a digitar os valores
maior = 0
menor = 99999999999999
c = 0
soma = 0
r = 'S'.upper()
while r != 'N':
    n = int(input('Digite qualquer número: '))
    c += 1
    soma += n
    print('~'*30)
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    r = str(input('Quer continuar?[S/N] ')).upper()[0]
    if r == 'S':
        print('~'*30)
        continue
    elif r == 'N':
        print('O programa foi finalizado!')
        print('\033[31mVocê informou {} números\033[m'.format(c))
        print('\033[32mA média entre os números foi {:.2f}\033[m'.format(soma/c))
        print('\033[33mO \033[30mmenor\033[33m valor apresentado foi {} e o \033[30mmaior\033[33m foi {}\033[m'.format(menor, maior))
        break
    else:
        print('Opção inválida!')
        continue