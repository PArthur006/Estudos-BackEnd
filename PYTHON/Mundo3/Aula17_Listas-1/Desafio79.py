#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
#Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os
#Valores únicos digitados, em ordem crescente.
valores = []
cont = 0
#usu = int(input('Digite um número: '))
while True:
    usu = int(input('Digite um número:[999 para encerrar] '))
    if usu == 999:
        break
    if usu not in valores:
        valores.append(usu)
        cont += 1
valores.sort()
print(f'Você digitou {cont} valores.')
print(f'Foram eles: {valores}')
