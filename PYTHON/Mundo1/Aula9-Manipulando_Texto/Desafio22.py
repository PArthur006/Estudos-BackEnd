#Crie um programa que leia o nome completo de uma pessoa e mostre
#O nome com todas as letras maiúsculas e minúsculas; quantas letras ao todo
#e quantas letras tem o primeiro nome.
nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em maiúsculo fica: {}.'.format(nome.upper()))
print('Seu nome em minúsculo fica: {}.'.format(nome.lower()))
print('Seu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
nome1 = nome.split()
print('Seu primeiro nome é {}, e ele tem {} letras.'.format(nome1[0], len(nome1[0])))
