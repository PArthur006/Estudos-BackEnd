#Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre- os em uma lista
#Única que mantenha separado os valores pares e ímpares. No final, mostre os valores ímpares
#E pares em ordem crescente
numeros = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}° valor: '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)
numeros[0].sort()
numeros[1].sort()
print(f'Os números pares digitados foram {numeros[0]}')
print(f'Os números ímpares digitados foram {numeros[1]}')
