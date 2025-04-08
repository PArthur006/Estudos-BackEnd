#Crie um programa que simule o funcionamento de um caixa  eletrônico. No início, pergunte ao usuário
#Qual será o valor sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor
#Serâo entregues.
#considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input('Digite o valor a ser sacado: '))
tot = valor
ced = 50
total = 0
while True:
    if tot >= ced:
        tot -= ced
        total += 1
    else:
        if total > 0:
            print(f'Total de {total} cédulas de {ced}')
        if ced == 50:
            ced = 20
            total = 0
        elif ced == 20:
            ced = 10
            total = 0
        elif ced == 10:
            ced = 1
            total = 0
        if tot == 0:
            break