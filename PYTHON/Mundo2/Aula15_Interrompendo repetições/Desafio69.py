#Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa
#Deverá perguntar se o usuário quer ou não continuar. No final, mostre:
#Quantas pessoas tem mais de 18 anos.
#Quantos homens foram cadastrados.
#Quantas mulheres tem menos de 20 anos
mais18 = homens = mulheres = cont = 0
while True:
    print('Cadastro de Dados')
    print('='*17)
    sexo = str(input('Informe o sexo:[M/F] ')).upper().strip()[0]
    while sexo not in 'MF':
        sexo = str(input('Informe o sexo:[M/F] ')).upper().strip()[0]
    if sexo == 'M':
        homens += 1
    idade = int(input('Informe a idade: '))
    cont += 1
    if idade >= 18:
        mais18 +=1
    if sexo == 'F' and idade < 20:
        mulheres += 1
    resposta = str(input('Deseja cadastrar mais alguém?[S/N]: ')).upper().strip()[0]
    while resposta not in 'NS':
        resposta = str(input('Deseja cadastrar mais alguém?[S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
print(f'''No total {cont} pessoas foram cadastradas!
Dentre essas, {homens} eram homens;
{mais18} pessoas tinham mais de 18 anos;
E {mulheres} eram mulheres abaixo dos 20 anos!''')
print('='*38)
print('Fim do programa!')
