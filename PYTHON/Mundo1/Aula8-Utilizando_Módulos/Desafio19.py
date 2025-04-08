import random
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
s = (n2, n1, n3, n4)
print('O escolhido foi {}'.format(random.choice(s)))