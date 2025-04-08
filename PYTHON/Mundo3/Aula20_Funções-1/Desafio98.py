# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros:
# Início, fim e passo. Seu programa tem que realizar três contagens através da função criada:
# a) De 1 até 10, de 1 em 1;
# b) De 10 até 0, de 2 em 2;
# c) Uma contagem personalizada.


from time import sleep


def contador(início, fim, passo):
    if início < fim:
        for c in range(início, fim+1, passo):
            print(c, end=' ')
            sleep(0.5)
        print()
    else:
        for c in range(início, fim-1, passo):
            if passo > 0:
                passo *= (-1)
            print(c, end=' ')
            sleep(0.5)
        print()


print('Contagem de 1 até 10, de 1 em 1:')
contador(1, 10, 1)
print('Contagem de 10 até 0, de 2 em 2:')
contador(10, 0, -2)
print('Contagem personalizada!')
início = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(início, fim, passo)
