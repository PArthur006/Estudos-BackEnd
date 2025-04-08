#Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo
#Deverá analisar se a expressão passada está entre parenteses abertos e fechados na ordem correta.
cont1 = cont2 = 0
exp = (input('Digite uma expressão matemática: '))
for m in exp:
    if m == '(':
        cont1 += 1
for n in exp:
    if n == ')':
        cont2 += 1
if cont1 == cont2:
    print(f'Sua expressão é válida. Ela possui {cont1} parênteses fechados')
else:
    print(f'Sua expressão não é válida. Ela possui {cont1} parênteses abertos'
          f' e {cont2} parênteses fechados')