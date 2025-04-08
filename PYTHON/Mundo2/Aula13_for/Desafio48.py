#Faça um programa que calcule a soma entre todos os números múltiplos de 3
#de 1 até 500.
cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
print('A soma de todos os {} valores é {}'.format(cont, soma))
