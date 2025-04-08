#print('!Bem vindo ao meu primeiro jogo!')
#print('Vou pensar em um número entre 0 e 5 você terá que adivinhar')
#from time import sleep
#sleep(2.5)
#print('PENSANDO....')
#sleep(2.5)
#import random
#pc = random.randint(0, 5)
#print('PENSEI')
#usu = int(input('Em qual número pensei? '))
#if pc == usu:
#    print('Ahh, você ganhou!\nParabéns!!!')
#else:
#    print('Você perdeu!\nEu pensei no número {}'.format(pc))
import random
from time import sleep
#Melhore o Desafio 28 onde o computador 'pensa' em um número de 0 a 5
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando
#no final quantos palpites foram necessários para vencer
cont = 0

print('\033[31m-\033[m'*30)
print('\033[35;40;1mBem vindo ao jogo\033[m')
print('\033[31m-\033[m'*30)
print('Eu irei pensar em um número de \033[31;1m0 a 10\033[m e você terá que adivinhar')
sleep(2.5)
print('\033[32;1mPENSANDO...\033[m')
sleep(2.5)
print('\033[31;40;1mPENSEI\033[m')
sleep(1)
pc = random.randint(0, 10)
usu = int(input('\033[30;7mEm qual número pensei?\033[m '))
while pc != usu:
    usu = int(input('Você errou! Me diga, \033[30;7mem qual número pensei:\033[m '))
    cont += 1
print('Você acertou! Eu pensei no número \033[30;7m{}\033[m também'.format(pc))
print('Você errou {} vezes!'.format(cont))
if cont <= 5:
    print('\033[34mVocê acertou bem rápido!\033[m')
else:
    print('\033[35mVocê demorou bastante hein\033[m')
