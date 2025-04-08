# Vamos criar um menu em Python, usando modularização.

from time import sleep
from Modulo.utiliadesCeV import lib


while True:
    resposta = lib.menu(['Cadastrar Pessoas', 'Listar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lib.cabeçalho('Opção 1')
    elif resposta == 2:
        lib.cabeçalho('Opção 2')
    elif resposta == 3:
        lib.cabeçalho('\033[1mSaindo do sistema...\033[m')
        sleep(1.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
