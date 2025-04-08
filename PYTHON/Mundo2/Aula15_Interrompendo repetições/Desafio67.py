#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
#Pelo usuário.
print('           \033[30;7mTabuda V3\033[m')
print(' '*9, '~'*11)
print('Para encerrar o programa digite 0!')
print('▬'*34)
while True:
    n = int(input('Insira um valor para ver sua tabudada: '))
    if n <= 0:
        print('\033[31;7mPrograma encerrado com sucesso!\033[m')
        break
    for c in range(0, 11):
        print(f'{n} × {c} = {n*c}')
    print('▬'*15)
