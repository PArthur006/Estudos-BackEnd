#Faça um programa que leia três números e mostre qual é o maior dentre eles.
#Programa modificado para atender à números reais.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
n3 = float(input('Digite mais um número: '))
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
maior = n2
if n1>n2 and n1>n3:
    maior = n1
if n3>n1 and n3>n2:
    maior = n3
print('O maior é {}\nE o menor é {}'.format(maior, menor))
