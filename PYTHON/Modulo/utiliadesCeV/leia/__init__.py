def leiaInt(texto):
    try:
        valor = int(input(texto))
    except ValueError:
        while True:
            valor = input('\033[1;31mInsira um número inteiro válido:\033[m ')
            if valor.isnumeric():
                break
    return valor


def leiaFloat(texto):
    try:
        valor = float(input(texto))
    except ValueError:
        while True:
            valor = input('\033[1;31mInsira um número real válido:\033[m')
            if valor.isdecimal():
                break
    return valor


def leiaDinheiro(texto):
    validação = False
    while not validação:
        entrada = str(input(texto)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! {entrada} não é um valor válido!\033[m')
        else:
            return float(entrada)
