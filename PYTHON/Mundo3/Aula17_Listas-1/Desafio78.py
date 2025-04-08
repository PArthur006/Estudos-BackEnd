#Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi
#O maior e o menor valor digitado e suas respectivas posições.
maior = menor= 0
valores = list()
for c in range(0, 5):
    v = int(input('Digite um número: '))
    valores.append(v)
print(valores)
print(f'O maior valor digitado foi {max(valores)}, na posição {valores.index(max(valores)) + 1}')
print(f'E o menor foi {min(valores)}, na posição {valores.index(min(valores)) + 1}')
