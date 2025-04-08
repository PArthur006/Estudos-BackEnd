# Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show,
# que será um valor lógico (opicional) indicando se será mostrado ou não
# na tela o processo de cálculo do fatorial.


def fatorial(num, show=False):
    """
    :param num: número a ser calculado
    :param show:(opcional) Se a conta será mostrada ou não na tela
    :return: Retorna o valor final
    """
    if show:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            if c == 1:
                print(f'{c} = {f}', end='')
            else:
                print(f'{c} x ', end='')
    else:
        f = 1
        for c in range(num, 0, -1):
            f *= c
        print(f)


fatorial(10, True)
