from time import sleep
from Modulo.utiliadesCeV.lib.arquivo import *
from Modulo.utiliadesCeV import lib, leia

arq = 'cursoemvídeo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = lib.menu(['Cadastrar Pessoas', 'Mostrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        lib.cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leia.leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        lib.cabeçalho('\033[1mSaindo do sistema...\033[m')
        sleep(1.5)
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(1.5)
