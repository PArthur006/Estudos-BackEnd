#Faça um programa que leia o ano de nascimento de uma pessoa e informe,
#de acordo com a sua idade se ele ainda vai se alistar ao serviço militar,
#se é a hora exata dele se alistar ou se ja passou do tempo do alistamento.
#Seu programa tambem deverá mostrar o tempo que falta, ou que passou do prazo.
from datetime import date
atual = date.today().year
sexo = str(input('Informe seu sexo: ')).strip()
if sexo == 'Feminino':
    print('Você não é obrigada a se alistar.')
else:
    nasc = int(input('Informe seu ano de nascimento: '))
    idade = atual - nasc
    if idade < 18:
        print('Você ainda não tem idade suficiente.')
        print('Você deverá se alistar em {}'.format(atual + (18-idade)))
    elif idade == 18:
        print('Você deve se alistar esse ano. Não perca tempo!')
    elif idade > 18:
        print('Já passou da hora de se alistar')
        print('Você deveria ter se alistado em {}'.format(atual - (idade-18)))
