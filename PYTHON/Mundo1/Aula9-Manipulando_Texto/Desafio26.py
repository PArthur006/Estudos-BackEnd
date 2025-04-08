
frase = str(input('Digite uma frase qualquer: '))
frase1 = frase.lower()
frase1.strip(' ')
print('A letra "A" aparece {} vezes'.format(frase1.count('a')))
print('A letra "A" aparece primeiro na {}° posição!'.format(frase1.find('a')+1))
print('A letra "A" aparece por ultimo na {}° posição!'.format(frase1.rfind('a') +1))
