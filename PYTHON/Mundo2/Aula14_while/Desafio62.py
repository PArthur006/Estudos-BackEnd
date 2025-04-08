#Melhore o Desafio61, perguntando ao usuário se ele quer mostrar mais alguns termos.
#O programa encerra quando ele disser que quer mostrar 0 termos
print('\033[40;31mProgressão Aritmética\033[m')
print('\033[30m=-=\033[m'*8)
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Informe a razão: '))
cont = 1
soma = a1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} >>> '.format(soma), end='')
        soma += r
        cont += 1
    print('\033[7;31mPAUSA\033[m')
    mais = int(input('Quantos termos você quer ver a mais? '))
print('''\033[34mAcabou...\033[m
Você viu {} termos'''.format(total))
