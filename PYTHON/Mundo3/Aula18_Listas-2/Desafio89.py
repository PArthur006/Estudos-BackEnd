#Crie um programa que leia o nome e duas notas de varios alunos e guarde tudo em uma lista composta.
#No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as
#Notas de cada aluno individualmente.

ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    resp = str(input('Quer continuar?[S/N]: ')).upper().strip()[0]
    if resp == 'N':
        break
print(f'{"N°":<4}{"Nome":<10}{"Média":>8}')
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.2f}')
while True:
    aluno = int(input('Escolha um aluno para ver suas notas[999 para interromper]: '))
    if aluno == 999:
        break
    if aluno <= len(ficha) - 1:
        print(f'As notas de {ficha[aluno][0]} são {ficha[aluno][1]}')
