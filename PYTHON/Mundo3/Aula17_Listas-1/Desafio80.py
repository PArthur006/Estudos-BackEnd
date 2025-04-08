#Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
#Já na posição correta de inserção(sem usar o sort()).  No final, mostre a lista ordenada na tela
lista = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n >= lista[-1]:
        lista.append(n)
    else:
        pos = 0
        while pos < len(lista):
            if n <= lista[pos]:
                lista.insert(pos, n)
                break
            pos += 1
print(f'Os números em ordem correta ficam {lista}')
