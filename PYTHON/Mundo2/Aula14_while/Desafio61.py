#Refaça o Desafio51, lendo o primeiro termo e a razão de uma PA mostrando os 10 primeiros termos
#da progressão usando a estrutura While
a1 = int(input('Digite o primeiro termo: '))
r = int(input('Informe a razão: '))
cont = 1
soma = a1
while cont < 10:
    soma += r
    cont += 1
    print('{} >>> '.format(soma) if cont < 10 else '{}'.format(soma), end='')





cont1 = int(input('Quer ver mais quantos termos? '))
if cont1 != 0:
    c = 1
    while c <= cont1:
        soma += r
        c += 1
        cont += 1
        print('{} >>> '.format(soma), end='')