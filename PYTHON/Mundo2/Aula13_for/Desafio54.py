#Crie um programa que leia a idade de 7 pessoas, e no final diga
#quais ja atingiram a maioridade, e quais não atingiram
from datetime import date
atual = date.today().year
cont = 0
cont1 = 0
for c in range(1, 8):
    nasc = int(input('Informe o ano de nascimento da {}° pessoa: '.format(c)))
    if atual - nasc >= 18:
        cont += 1
    elif atual - nasc < 18:
        cont1 += 1
print('{} pessoas \033[31;4mja atingiram\033[m a maioridade'.format(cont))
print('{} pessoas \033[34;4mainda não antingiram\033[m a maioridade'.format(cont1))
