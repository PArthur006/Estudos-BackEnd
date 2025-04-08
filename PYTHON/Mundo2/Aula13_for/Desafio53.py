#Faça um programa que leia uma frase e diga se ela é ou não um palíndromo,
#desconsiderando espaços.
#PALÍNDROMO= frases que podem ser lidas de trás pra frente
frase = str(input('Escreva uma frase: ')).strip().lower()
separado = frase.split()
junto = ''.join(separado)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]
print('O inverso de {} é {}'.format(frase, inverso))
if junto == inverso:
    print('Essa frase é um palíndromo!')
else:
    print('Essa frase não é um palíndromo!')
