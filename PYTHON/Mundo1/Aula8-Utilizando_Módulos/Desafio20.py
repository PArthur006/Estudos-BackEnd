#O mesmo professor do desafio 19 quer sortear a ordem de apresentação
#de trabalho dos alunos. Faça um programa que leia o nome dos 4 alunos
#e mostre a ordem sorteada.
import random
a1 = str(input('Qual o nome do primeiro aluno? '))
a2 = str(input('Qual o nome do segundo aluno? '))
a3 = str(input('Qual o nome do terceiro aluno? '))
a4 = str(input('Qual o nome do quarto alunoo? '))
lista = [a1 ,a2 ,a3 ,a4]
random.shuffle(lista)
print('A ordem sorteada foi:\n{} '.format(lista))