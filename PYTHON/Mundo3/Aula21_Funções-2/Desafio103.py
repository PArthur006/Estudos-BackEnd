# Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
# o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar
# a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.


def ficha(nome='', gols=''):
    if nome in '   ':
        nome = '<desconhecido>'
    if gols.isalpha() == True or gols in '    ':
        gols = '0'
    print(f'O jogador {nome} fez um total de {gols} gol(s).')


nome = input('Nome do jogador: ')
gols = input('Quantidade de gols: ')
ficha(nome, gols)
