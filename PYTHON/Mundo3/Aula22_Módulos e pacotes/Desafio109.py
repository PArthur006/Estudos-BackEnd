# Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
# informando se o valor retornado por elas vai ser ou não formatado pela função moeda(),
# desenvolvida no desafio 108.

from Modulo.utiliadesCeV import moeda
num = float(input('Digite o preço:R$'))
print(f'{moeda.moeda(num)} com aumento de 20% é {moeda.aumentar(num, 20, True)}')
print(f'{moeda.moeda(num)} com desconto de 60% é {moeda.diminuir(num, 60, True)}')
print(f'O dobro de R${moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'A metade de R${moeda.moeda(num)} é {moeda.metade(num, True)}')
