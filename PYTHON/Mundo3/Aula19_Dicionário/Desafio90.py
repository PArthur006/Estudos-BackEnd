#Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#No final, mostre o conteúdo da estrutura na tela.
dados = {}
dados['nome'] = str(input('Nome: '))
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
print(f'O nome do aluno é {dados["nome"]}')
print(f'A média de {dados["nome"]} foi {dados["média"]}')
if dados['média'] < 5:
    dados['situação'] = 'REPROVADO'
elif 5 <= dados['média'] < 7:
    dados['situação'] = 'RECUPERAÇÃO'
else:
    dados['situação'] = 'APROVADO'
print(f'E a situação final é {dados["situação"]}')
