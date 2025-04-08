# Faça um mini-sistema que utilize o interactive Help do Python. O usuário vai digitar o comando
# e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará.
# Importante: use cores.


def ajuda(a):
    help(a)


n = ''
while True:
    from time import sleep
    print('\033[1;43;30m~' * 40)
    print('        SISTEMA DE AJUDA PYHELP')
    print('~'*40)
    n = str(input('\033[m <<< Função ou biblioteca >>> '))
    if n.lower() == 'fim':
        print('\033[30;1;41m')
        print('Até logo')
        print('')
        break
    print('\033[1;30;44m~'*42)
    print(f'   Acessando o manual do comando "{n}"')
    print('~'*42)
    print('\033[m')
    sleep(1)
    print('\033[7;30m')
    ajuda(n)
