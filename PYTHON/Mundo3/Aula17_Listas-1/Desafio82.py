#Crie um programa que leia vários números e coloque em uma lista. Depois disso crie duas listas
#Extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#Ao final, mostre o conteúdo das três listas criadas.
lista = list()
par = list()
impar = list()
while True:
    lista.append(int(input('Digite qualquer número: ')))
    resp = str(input('Quer continuar?[S/N] '))
    if resp in 'Nn':
        break
for i, v in enumerate(lista):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print(f'Os números digitados foram {lista}')
print(f'Dentre esses, os pares são {par}')
print(f'E os ímpares são {impar}')
