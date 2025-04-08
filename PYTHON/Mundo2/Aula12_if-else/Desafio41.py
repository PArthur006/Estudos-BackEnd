#A Confederação Nacional de Natação precisa de um programa que leia o ano de
#um atleta e mostre sua categoria de acordo com a idade.
idade = int(input('Informe sua idade: '))
if idade <= 9:
    print('Sua categoria é {}Mirim{}'.format('\033[1;35;40m', '\033[m'))
elif idade >9 and idade <= 14:
    print('Sua categoria é {}Infantil{}'.format('\033[1;34;40m', '\033[m'))
elif idade > 14 and idade <= 19:
    print('Sua categoria é {}Júnior{}'.format('\033[1;33;40m', '\033[m'))
elif idade > 19 and idade <=25:
    print('Sua categoria é {}Sênior{}'.format('\033[1;32;40m', '\033[m'))
else:
    print('Sua categoria é {}Master{}'.format('\033[1;31;40m', '\033[m'))