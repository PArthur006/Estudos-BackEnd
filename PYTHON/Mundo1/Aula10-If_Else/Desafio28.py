#Escreva um programa que faça o computador 'pensar' em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido.
#O programa deverá escrever na tela se o usuário perdeu ou venceu.
print('!Bem vindo ao meu primeiro jogo!')
print('Vou pensar em um número entre 0 e 5 você terá que adivinhar')
#from time import sleep
#sleep(2.5)
#print('PENSANDO....')
#sleep(2.5)
import random
pc = random.randint(0, 5)
print('PENSEI')
usu = int(input('Em qual número pensei? '))
if pc == usu:
    print('Ahh, você ganhou!\nParabéns!!!')
else:
    print('Você perdeu!\nEu pensei no número {}'.format(pc))
