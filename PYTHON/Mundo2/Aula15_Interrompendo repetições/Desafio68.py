#Faça um programa que jogue par ou ímpar com o usuário. O jogo só será interrompido quando o
#Jogador perder, mostrando no final o número de vitórias consecutivas.
from random import randint
cont = 0
while True:
    pc = randint(0, 10)
    jog = int(input('\033[31;4mDigite um número:\033[m '))
    escolhajog = str(input('\033[34;4mEscolha ímpar ou par[I/P]: \033[m')).upper().strip()[0]
    print('▬ '*30)
    result = pc + jog
    if result % 2 == 0:
        print('O resultado foi PAR')
        print(f'Você jogou {jog} e o Computador {pc}, o resultado foi {result}')
        print('▬ '*35)
        if escolhajog == 'P':
            print('\033[40;34;1mVocê venceu!\033[m')
            print('▬ '*10)
            cont += 1
        elif escolhajog == 'I':
            print('\033[31;40;1mE o Computador venceu!\033[m')
            print('▬ '*11)
            break
    if result % 2 != 0:
        print('O resultado foi ÍMPAR')
        print(f'Você jogou {jog} e Computador {pc}, o resultado foi {result}')
        print('▬ '*35)
        if escolhajog == 'I':
            print('\033[34;40;1mVocê venceu!\033[m')
            print('▬ '*10)
            cont += 1
        elif escolhajog == 'P':
            print('\033[31;40;1mE o Computador venceu!\033[m')
            print('▬ '*11)
            break
print('\033[30;7mGame encerrado\033[m')
print(f'Você ganhou \033[36m{cont}\033[m vezes seguidas!')
