#Crie um programa que leia seis números inteiros e mostre a soma entre
#aqueles que forem pares. Se o número for ímpar, desconsidere-o
soma = 0
cont = 0
for c in range(1, 7):
    n1 = int(input('Digite o {}° valor: '.format(c)))
    if c % 2 == 0:
        soma += n1
        cont += 1
print('Você digitou {} números pares, e a soma entre eles foi {} '.format(cont, soma))
