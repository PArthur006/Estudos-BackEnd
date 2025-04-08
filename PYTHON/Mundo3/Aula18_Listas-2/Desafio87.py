#Aprimore o desafio anterior, mostrando no final:
#A) A soma de todos os valores pares digitados.
#B) A soma dos valores da terceira coluna.
#C) O maior valor da segunda linha
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somap = soma3 = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if c == 2:
            soma3 += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma de todos os valores pares é {somap}')
print(f'A soma de todos os valores da 3° coluna é {soma3}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c]
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha é {maior} ')
