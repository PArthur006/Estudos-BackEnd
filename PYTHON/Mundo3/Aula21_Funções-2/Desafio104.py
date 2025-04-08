# Crie um programa que tenha a função leiaInt(),
# que vai funcionar de forma semelhante à função input() do Python,
# só que fazendo a validação para aceitar apenas um valor numérico.


def leiaInt(texto):

    valor = input(texto)

    if valor.isdecimal():
        return int(valor)

    else:

        print(f'\033[1;31mValor inválido. Digite um número inteiro!\033[m')

        return leiaInt(texto)


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}.')
