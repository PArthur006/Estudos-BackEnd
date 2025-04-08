#Desenvolva um programa que guarde 4 valores pelo teclado e guarde-os em uma tupla. No final mostre
#Quantas vezes apareceu o valor 9;
#Em que posição foi digitado o primeiro valor 3;
#Quais foram os números pares.
n = (int(input('Digite um número: ')),
     int(input('Digite outro número: ')),
     int(input('Digite mais um número: ')),
     int(input('Digite o último número: ')))
print(f'O número 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O primeiro valor três foi digitado na {n.index(3)+1}° posição')
if 3 not in n:
    print('O valor três não foi digitado')
print('Os valores pares digitados foram ', end='')
for num in n:
    if num % 2 == 0:
        print(num, end= ' ')