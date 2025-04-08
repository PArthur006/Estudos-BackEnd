from random import choice
n1 = input('Nome do primeiro aluno: ')
n2 = input('Nome do segundo aluno: ')
n3 = input('Nome do terceiro aluno: ')
n4 = input('Nome do quarto aluno: ')
s = (n1 ,n2 ,n3 ,n4)
choice(s)
print('O escolhido foi {}'.format(choice(s)))
