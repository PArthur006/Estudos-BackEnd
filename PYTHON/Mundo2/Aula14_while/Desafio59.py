#Crie um programa que leia dois valores e mostre um menu na tela
#1 somar
#2 Multiplicar
#3 Maior
#4 Novos números
#5 Sair do programa
#Seu programa deverá realizar as operações solicitadas em cada caso
from time import sleep
v1 = float(input('\033[30;7mDigite um valor:\033[m '))
v2 = float(input('\033[30;7mDigite outro valor:\033[m '))
print('\033[31mEscolha uma das opções abaixo:\033[m')
cond = False
while not cond:
    print('\033[32m[1] Somar\033[m')
    sleep(0.5)
    print('\033[33m[2] Multiplicar\033[m')
    sleep(0.5)
    print('\033[34m[3] Maior\033[m')
    sleep(0.5)
    print('\033[35m[4] Novos números\033[m')
    sleep(0.5)
    print('\033[36m[5] Sair do programa\033[m')
    sleep(0.5)
    usu = int(input('\033[30;7m>>>Qual sua escolha?\033[m '))
    if usu == 1:
        print('-'*40)
        print('\033[32m{} + {} é igual a {}\033[m'.format(v1, v2, v1 + v2))
        print('-'*40)
        sleep(1.5)
    elif usu == 2:
        print('-'*40)
        print('\033[33m{} X {} é igual a {}\033[m'.format(v1, v2, v1*v2))
        print('-'*40)
        sleep(1.5)
    elif usu == 3:
        print('-'*40)
        if v1 > v2:
            print('\033[34mO {} é maior que o {}\033[m'.format(v1, v2))
        elif v1 == v2:
            print('\033[34mNão existe maior, ambos tem o mesmo valor\033[34m')
        else:
            print('\033[34mO {} é maior que o {}\033[m'.format(v2, v1))
        print('-'*40)
        sleep(1.5)
    elif usu == 4:
        print('Escolha seus outros números: ')
        v1 = float(input('\033[30;7mDigite um valor:\033[m '))
        v2 = float(input('\033[30;7mDigite outro valor:\033[m '))
        continue
    elif usu == 5:
        print('')
        print('Encerrando...')
        sleep(1.9)
        print('\033[36;4mPrograma encerrado com sucesso!\033[m')
        break
    else:
        print('Valor inválido! Tente novamente:')
        sleep(2)
        continue
