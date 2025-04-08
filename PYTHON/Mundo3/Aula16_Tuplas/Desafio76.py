#Crie um programa que tenha uma tupla única com nome de produtos e seus respectivos preços,
#em sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
t = ('Arroz', 24.00, 'Feijão', 19.00, 'Peito de frango', 23.90, 'Contra filé', 34.99)
print(f'~'*10, "Tabela de preços", '~'*10)
print(' ')
for c in range(0, 8):
    if c % 2 == 0:
        print(f'{t[c]:.<30}', end=' ')
    else:
        print(f'R${t[c]:>5.2f}')
