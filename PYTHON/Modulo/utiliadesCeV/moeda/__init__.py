def dobro(n=0, m=False):
    r = n * 2
    if m:
        return moeda(r)
    else:
        return r


def metade(n=0, m=False):
    r = n / 2
    if m:
        return moeda(r)
    else:
        return r


def aumentar(n=0, taxa=0, m=False):
    r = n + n * taxa / 100
    if m:
        return moeda(r)
    else:
        return r


def diminuir(n=0, taxa=0, m=False):
    r = n - n * taxa / 100
    if m:
        return moeda(r)
    else:
        return r


def moeda(preço: float=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(n=0, a=0, d=0):
    print('~'*32)
    print('>>>Resumo<<<'.center(32))
    print('~'*32)
    print(f'Dobro do preço: \t{dobro(n,True)}')
    print(f'Metade do preço: \t{metade(n,True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de desconto: \t{diminuir(n, d, True)}')
    print('~'*32)