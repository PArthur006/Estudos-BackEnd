#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre a média de idade do grupo, qual o nome do
#homem mais velho e quantas mulheres tem menos de 20 anos
nomevelho = ''
cont = 0
idadevelho = 0
totidade = 0
for p in range(1, 5):
    print('-'*10, p,'Pessoa', '-'*10, )
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo(M/F): '))

    if p == 1 and sexo == 'Mm':
        nomevelho = nome
        idadevelho = idade
    else:
        if idadevelho < idade:
            idadevelho = idade
            nomevelho = nome
    if idade < 20 and sexo == 'Ff':
        cont += 1
    totidade += idade
media = (totidade / 4)
print('-'*60)
print('A média de idades é {:.1f}'.format(media))
print('E o homem mais velho é o {}'.format(nomevelho))
print('Dentre as pessoas informadas, {} mulheres tem menos de 20 anos'.format(cont))
