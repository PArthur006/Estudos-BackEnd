lar = float(input('Informe a largura da parede:'))
alt = float(input('Informe a altura da parede:'))
Lt = 2**2
area = lar * alt
print('A área da parede é {} metros'.format(area))
print('A quantidade de tinta necessária  para pintar a parede será de {:.2f} litro(s)'.format(area/Lt))
print('Mãos a obra!')