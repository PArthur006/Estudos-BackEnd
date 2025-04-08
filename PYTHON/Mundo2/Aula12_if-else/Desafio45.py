#Desenvolva um programa que faça o computador jogar jokenpô com o usuário.
import random
from time import sleep
print('\033[41;1;30mVamos brincar de Pedra, Papel ou Tesoura!\033[m')
sleep(1)
n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
s = [n1, n2, n3]
print('Digite\n1 para {}\n2 para {}\n3 para {}'.format(n1, n2, n3))
usu = str(input('Digite: '))

pc = random.choice(s)
if usu == '1' and pc == n3:
    print('Ahh, \033[42;30;1mvocê ganhou\033[m')
    print('Eu escolhi Tesoura')
elif usu == '2' and pc == n1:
    print('Ahh, \033[42;30;1mvocê ganhou\033[m')
    print('Eu escolhi Pedra')
elif usu == '3' and pc == n2:
    print('Ahh, \033[42;30;1mvocê ganhou\033[m')
    print('Eu escolhi Papel')
elif usu == '1' and pc == n2:
    print('Haha, \033[41;30;1meu ganhei\033[m')
    print('Eu escolhi Papel')
elif usu == '2' and pc == n3:
    print('Haha, \033[41;30;1meu ganhei\033[m')
    print('Eu escolhi Tesoura')
elif usu == '3' and pc == n1:
    print('Haha, \033[41;30;1meu ganhei\033[m')
    print('Eu escolhi Pedra')
else:
    print('Parece que empatamos. Vamos outra vez?')
