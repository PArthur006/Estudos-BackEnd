def expressão(*num):
    total = num[0]
    for i, v in enumerate(num):
        if i != 0:
            total -= v
    print(f'O resultado foi {total}')


def raiz(num):
    r = num**(1/2)
    return r


def bhaskara(a, b=0, c=0):
    delta = (b ** 2 - 4 * a * c)
    x1 = ((-b + raiz(delta)) / (2*a))
    x2 = ((-b - raiz(delta)) / (2*a))
    print(f'\033[7;40mx1 = {x1:.2f}\033[m')
    print(f'\033[7;40mx2 = {x2:.2f}\033[m')


