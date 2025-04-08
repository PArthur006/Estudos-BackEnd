#Crie um programa que leia o nome e o preço de vários produtos. O programa sempre deve perguntar se
#O usuário vai continuar ou não. No final mostre:
#Qual o gasto total da compra
#Quantos produtos custam mais de R$1000 reais
#Qual o nome do produto mais barato
total = mais1000 = maisbarato = totalx = 0
nomebarato = ' '
while True:
    produto = str(input('Informe o nome do produto: '))
    print('\033[34m═\033[m '*20)
    preco = float(input('Informe o preço: R$'))
    print('\033[31m═\033[m '*20)
    total += preco
    totalx += 1
    if totalx == 1 or preco < maisbarato:
        maisbarato = preco
        nomebarato = produto
    if preco >= 1000:
        mais1000 += 1
    resposta = ' '
    if totalx == 1:
        print(f'Você tem {totalx} produto no total.')
        print(' ')
    else:
        print(f'Você tem {totalx} produtos no total.')
        print(' ')
    while resposta not in 'SN':
        resposta = str(input('Deseja adicionar mais produtos?[S/N]')).upper().strip()[0]
        print(' ')
    if resposta == 'N':
        break
print('\033[35m─\033[m'*45)
print(f'''\033[31mNo total, a compra custou R${total}\033[m
\033[33mDentre os produtos, {mais1000} custam mais de R$1000;\033[m
\033[34mE o produto mais barato foi o(a) {nomebarato}, que custou R${maisbarato}''')
