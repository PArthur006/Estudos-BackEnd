#Escreva um programa em Python que leia um número inteiro qualquer e peça para
#o usuário escolher qual será a base de conversão:
#1 para binário, 2 para octal e 3 para hexadecimal
print('Escolha uma base de conversão')
print('1 para binário\n2 para octal\n3 para hexadecimal\n4 para todas as bases')

base = int(input('Digite: '))
num = int(input('Digite um número: '))

if base == 1:
    print('A forma Binária do número {} é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('A forma Octal do número {} é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('A forma Hexadecimal do número {} é {}'.format(num, hex(num)[2:]))
elif base == 4:
    print('A forma Binária do número {} é {}\nNa forma Octal é {}\nE na forma Hexadecimal é {}'.format(num, bin(num)[2:], oct(num)[2:], hex(num)[2:]))
else:
    print('Opção inválida!')