# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
# em um dicionário e todos os dicionários em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) A média de idade.
# C) Uma lista com as mulheres.
# D) Uma lista de pessoas com idade acima da média.

pessoas = list()
pessoa = dict()
mulheres = list()
idadetemp = 0
idade = 0
cont = 0

while True:
    pessoa['Nome'] = str(input('\033[7;30mNome: '))
    while True:
        pessoa['Sexo'] = str(input('\033[7;30mSexo[M/F]: ')).strip().upper()[0]
        if pessoa['Sexo'] not in 'MF':
            print('\033[41;1;30m     ERRO! USE SOMENTE "M" OU "F"!     \033[m')
            continue
        else:
            break
    idadetemp = int(input('\033[7;30mIdade: '))
    idade += idadetemp
    cont += 1
    pessoa['Idade'] = idadetemp
    if pessoa['Sexo'] == 'F':
        mulheres.append(pessoa['Nome'][:])
    pessoas.append(pessoa.copy())
    pessoa.clear()

    while True:
        print('\033[34;40m░\033[m' * 40)
        resp = str(input('\033[7;30mQuer catalogar mais alguem?[S/N] ')).upper().strip()[0]
        print('\033[34;40m░\033[m' * 40)
        if resp not in 'SN':
            print('\033[41;1;30m    !ERRO! USE SOMENTE "S" OU "N"!     \033[m')
            continue
        else:
            break
    if resp == 'S':
        continue
    else:
        break
media = idade / cont
print('\033[32;40m░\033[m'*40)
print(f'\033[7;30mForam cadastradas {len(pessoas)} pessoas.')
print(f'\033[7;30mA média das idades foi {media}')
print('\033[7;30mAs mulheres cadastradas foram: ', end='')
for c, v in enumerate(mulheres):
    print(f'{v}', end=', ')
print('')
print(f'\033[7;30mAs pessoas que ficaram acima da média foram: ', end='')
for c, v in enumerate(pessoas):
    if pessoas[c]['Idade'] > media:
        print(f'{pessoas[c]["Nome"]}', end=', ')
print('')
