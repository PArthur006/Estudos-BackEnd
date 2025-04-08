#Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de 0 a 20.
#Seu programa deverá ler um número pelo teclado e mostrá-lo por extenso.
extenso = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis',
           'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze',
           'Catorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito',
           'Dezenove', 'Vinte')
while True:
    while True:
        usu = int((input('\033[36mDigite um número (Entre 0 e 20) para vê-lo por extenso:\033[m ')))
        if 0 <= usu <= 20:
           break
        print('\033[31;1mENTRE 0 E 20. \033[m', end='')
    print(f'\033[34mO número {usu} por extenso é {extenso[usu]}\033[m')
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input('Deseja ver mais algum número?[S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
print('\033[33;4mTenha um bom dia, volte sempre.\033[m')
