#Refaça o desafio 09, mostrando a tabuada do número que o usuário escolher
#só que agora utilizando um laço 'for'

n1 = int(input('\033[7;30mDigite um número para ver sua tabuada:\033[m '))
for c in range(1, 11):
    print('{} X {} = {}'.format(n1, c, n1*c))
