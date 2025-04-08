#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos
#de uma Sequência de Fibonacci
print('='*23)
print('Sequência de Fibonacci')
print('='*23)
c = 0
n = int(input('Quantos termos quer mostrar? '))
while c != n+1:
    sf = (1.618034**c - (1-1.618034)**c)/2.23606798
    print('{} >>> '.format(round(sf)) if c != n else '{}'.format(round(sf)), end='')
    c += 1
print('')
print('')
print('''Sequência de Fibonacci se escreve na forma:
x = (Øª - (1 - Ø)ª) ÷ √5''')
