#Elabore um programa que calcule um valor a ser pago por um produto,
#considerando seu preço normal e condição de pagamento.
#Á vista dinheiro/cheque: 10% de desconto
#Á vista no cartão: 5% de desconto
#Em até 2x no cartão: preço normal
#3x ou mais no cartão: 20% de juros
print('{:=^50}'.format('\033[41;30;1mLOJAS AMERICANAS\033[m'))
inicial = float(input('Informe o valor da compra: R$'))
print('Escolha uma forma de pagamento:')
print('Digite 1 para: \033[41;30;4mà vista no dinheiro/cheque\033[m')
print('Digite 2 para: \033[42;30;4má vista no cartão\033[m')
print('Digite 3 para \033[43;30;4mparcelar em duas vezes no cartão\033[m')
print('Digite 4 para \033[44;30;4mparcelar em mais vezes no cartão\033[m')
pagamento = int(input('Digite: '))
if pagamento == 1:
    n1 = inicial * 10 / 100
    print('Você recebeu 10% de desconto em sua compra!')
    print('Você deverá pagar R${:.2f} reais'.format(inicial-n1))
elif pagamento == 2:
    n1 = inicial * 5 / 100
    print('Você recebeu 5% de desconto em sua compra!')
    print('Você deverá pagar R${:.2f} reais'.format(inicial - n1))
elif pagamento == 3:
    n1 = inicial /2
    print('Você pagará em duas vezes no cartão sem juros')
    print('Você deverá pagar 2 parcelas de R${:.2f} reais'.format(n1))
elif pagamento == 4:
    tempo = int(input('Você irá parcelar em quantas vezes? '))
    n1 = inicial * 0.2 * tempo
    print('Você pagará 20% de juros nessa compra!')
    print('No total ficará R${:.2f} reais'.format(inicial + n1))
    print('Você pagará em {} vezes de R${:.2f} Com Juros'.format(tempo, (inicial + n1)/tempo))
else:
    print('Ocorreu um erro. Tente novamente')
