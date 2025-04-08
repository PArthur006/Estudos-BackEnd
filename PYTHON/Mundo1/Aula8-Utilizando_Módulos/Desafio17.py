from math import sqrt
co = float(input('Digite o tamanho do cateto oposto: '))
ca = float(input('Digite o tamanho do cateto adjacente: '))
h2 = co**2 + ca**2
h = sqrt(h2)
print('O valor da hipotenusa é igual à {:.2f}'.format(h))

print('No Teorema de Pitágoras ele afirma que \nA fórmula para descobrir o valor da hipotenusa é\n co(2) + ca(2) == h(2)')
