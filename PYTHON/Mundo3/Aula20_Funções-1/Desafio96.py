# Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno
# retangular (largura e comprimento) e mostre a área do terreno.


def area():
    print(f'A área do terreno é de {largura * comprimento}m².')


largura = float(input('Informe a largura(m): '))
comprimento = float(input('Informe o comprimento(m): '))
area()
