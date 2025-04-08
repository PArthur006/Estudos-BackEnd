#Crie um programa que tenha uma tupla com várias palavras(não usar acentos). Depois disso, você
#Deve mostrar, para cada palavra, quais são suas vogais.
t = ('ganancioso', 'armado', 'ferradura', 'miojo', 'lagartixa', 'mundo', 'felicidade')
for p in t:
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end=' ')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')