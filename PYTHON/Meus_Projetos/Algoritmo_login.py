#TESTE PARA CRIAR UMA PLATAFORMA DE REGISTRO E LOGIN

from Modulo.utiliadesCeV.leia import *
from Modulo.utiliadesCeV.lib.arquivo import *

arq = 'Lista de cadastros'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    print(f'''    1 - CADASTRAR
    2 - LOGIN
    3 - ENCERRAR PROGRAMA''')
    resp = leiaInt('Opção: ')
    if resp == 1:
        cabeçalho('Tela de cadastro')
        nome = str(input('Insira seu nome: '))
        senha = int(input('Insira sua senha: '))
        cadastrar(arq, nome, senha)
    elif resp == 2:
        #Login
        print('')
    elif resp == 3:
        break
    else:
        print('ERRO! Digite um número válido!')
        continue
