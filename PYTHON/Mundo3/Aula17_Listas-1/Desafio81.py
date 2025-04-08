#Crier um programa que leia vários números e coloque-os em uma lista. Depois disso mostre:
#A: Quantos números foram digitados
#B: A lista de valores digitados na ordem decrescente
#C: O valor 5 foi ou não digitado.
lista = []
cont = 0
while True:
    n = int(input('Digite qualquer número: '))
    lista.append(n)
    resp = str(input('Quer parar agora?[S/N] ')).strip().upper()[0]
    while resp not in 'SN':
        resp = str(input('Valor incorreto. Quer parar agora?[S/N] ')).strip().upper()[0]
    if resp == 'N':
        continue
    elif resp == 'S':
        lista.sort()
        print(f'Foram digitados {len(lista)} números')
        lista.reverse()
        print(f'Em ordem decrescente fica {lista}')
        if 5 in lista:
            print(f'O valor 5 apareceu na lista {lista.count(5)} vezes')
        else:
            print('O valor 5 não foi digitado nenhuma vez')
        break
print('Fim')
