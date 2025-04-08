#Faça um programa que leia um número qualquer e mostre seu fatorial
#Exemplo:
#5! = 5*4*3*2*1 = 120
usu = int(input('''Digite um número para
calcular seu fatorial: '''))
f = 1
c = usu
print('Calculando {}! = '.format(usu),end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
