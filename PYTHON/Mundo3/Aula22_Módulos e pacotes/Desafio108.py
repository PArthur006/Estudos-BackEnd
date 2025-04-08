# Adapte o código do desafio107, criando uma função adicional chamada moeda()
# que consiga mostrar os números como um valor monetário formatado

from Modulo.utiliadesCeV import moeda
num = float(input('Digite o preço:R$'))
print(f'R${num} com aumento de 20% é {moeda.moeda(moeda.aumentar(num, 20))}')
print(f'R${num} com desconto de 60% é {moeda.moeda(moeda.diminuir(num, 60))}')
print(f'O dobro de R${num} é {moeda.moeda(moeda.dobro(num))}')
print(f'A metade de R${num} é {moeda.moeda(moeda.metade(num))}')
