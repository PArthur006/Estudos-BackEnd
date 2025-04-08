#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date
ano = int(input('Que ano quer analisar? Se quiser analisar o ano atual digite 0: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é BISSEXTO!'.format(ano))
else:
    print('O ano de {} NÃO é BISSEXTO!'.format(ano))
