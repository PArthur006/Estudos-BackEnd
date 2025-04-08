# Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o
# ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto
# NEGADO, OPCIONAL E OBRIGATÓRIO nas eleções.


def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    return idade


nasc = int(input('Informe o ano de nascimento: '))
idade = voto(nasc)
print(f'Você tem {idade} anos. O seu voto é ', end='')
if idade < 16:
    print('NEGADO!')
elif 18 <= idade < 65:
    print('OBRIGATÓRIO!')
else:
    print('OPCIONAL!')
