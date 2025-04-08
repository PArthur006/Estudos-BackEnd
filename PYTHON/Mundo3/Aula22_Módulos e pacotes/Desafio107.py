# Crie um módulo chamado moeda.py que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade(). Faça também um programa que
# importe esse módulo e use algumas dessas funções.


from Modulo.utiliadesCeV import moeda
num = float(input('Digite o preço:R$'))
print(f'R${num} com aumento de 20% é R${moeda.aumentar(num, 20)}')
print(f'R${num} com desconto de 60% é R${moeda.diminuir(num, 60)}')
print(f'O dobro de R${num} é R${moeda.dobro(num)}')
print(f'A metade de R${num} é R${moeda.metade(num)}')
