#Desenvolva um programa que pergunte a distância de uma viagem em Km.
#Calcule o preço da passagem cobrando R$0,50 por Km para viagens de até 200Km
#e R$0,45 para viagens mais longas.
km = float(input('À quantos Km de distância fica o local? '))
if km <= 200:
    print('Sua viagem ficará R${} Reais.'.format(km*0.50))
else:
    print('Sua viagem ficará R${} Reais.'.format(km*0.45))
