#Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre o(com idade)
#Em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano
#De contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a
#Pessoa vai se aposentar.

from datetime import date
data = date.today()
dados = {}
dados['Nome'] = str(input('Insira o seu nome: '))
nasc = int(input('Ano de nascimento: '))
dados['Idade'] = data.year - dados["Ano de Nascimento"]
dados['CTPS'] = int(input('N° Carteira de trabalho [0 caso não possua]: '))
if dados['CTPS'] != 0:
    dados['Ano de contratação'] = int(input('Insira o ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = 65 - dados['Idade']
for k, v in dados.items():
    print(f'{k} tem o valor {v}')
