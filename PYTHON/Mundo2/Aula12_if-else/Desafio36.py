#Escreva um programa para aprovar um empréstimo bancário para a compra de
#uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos
#ele vai pagar. A prestação mensal não pode exceder 30% do salário ou
#então o empréstimo será negado.
print('Bem vindo ao \033[1;32mBanco\033[m!')
#Variáveis
casa = float(input('Qual o valor da casa? R$'))
salario = float(input('Qual o valor do seu salário? R$'))
tempo = int(input('Em quantos anos planeja pagar? '))
#Prestação da casa e porcentagem do salário
prestação = casa/(tempo*12)
minimo = salario*30/100
#Resultados
if prestação<=minimo:
    print('Empréstimo {}APROVADO!{}'.format('\033[32;4m','\033[m'))
    print('O valor mensal será de {}R${:.2f}{}'.format('\033[32;4m', prestação, '\033[m'))
else:
    print('Empréstimo {}NEGADO!{}'.format('\033[31;4m', '\033[m'))
    print('O valor da prestação será de R${:.2f}. Está fora de suas condições!'.format(prestação))
