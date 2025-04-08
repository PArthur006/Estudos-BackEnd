#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final
#Mostre:
#Quantas pessoas foram cadastradas
#Uma listagem com as pessoas mais pesadas
#Uma listagem com as pessoas mais leves
temp = list()
pessoas = list()
maior = menor = 0
cont = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(pessoas) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        if temp[1] < menor:
            menor = temp[1]
    pessoas.append(temp[:])
    temp.clear()
    resp = str(input('Quer continuar?[S/N] ')).upper()[0]
    if resp in 'N':
        break
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'{[p[0]]} ', end='')
print(' ')
print(f'O menor peso foi de {menor}Kg. Peso de ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'{[p[0]]} ', end='')
print(' ')
