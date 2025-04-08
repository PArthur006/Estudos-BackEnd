def leiaDinheiro(texto):
    validação = False
    while not validação:
        entrada = str(input(texto)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[31mERRO! {entrada} não é um valor válido!\033[m')
        else:
            return float(entrada)
