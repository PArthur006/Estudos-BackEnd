#Escreva um programa que leia dois números inteiros e compare-os, mostrando
#na tela uma mensagem:
#O primeiro valor é maior!
#O segundo valor é maior!
#Nenhum valor é maior. Ambos tem o mesmo valor!
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro: '))
if n1>n2:
    print('O primeiro valor é maior!')
elif n1<n2:
    print('O segundo valor é maior!')
elif n1==n2:
    print('Nenhum valor é maior. Ambos tem o mesmo valor!')
else:
    print('Números {}INVÁLIDOS!{}'.format('\033[31;4m', '\033[m'))
