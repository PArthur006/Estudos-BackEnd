#Escreva um programa que pergunte a quantidade de Km percorridos por
#um carro alugado e a quantidades de dias pelos quais ele foi alugado.
#Calcule o preço a pagar, sabendo que o carro custa 60$ por dia e 0,15$
#por Km rodado.
km = float(input('Quantos Km foram percorridos com o veículo?'))
dias = int(input('E por quantos dias?'))
total1 = dias * 60
total2 = km * 0.15
print('Você terá que pagar R${} reais pelo veículo!'.format(total1 + total2))