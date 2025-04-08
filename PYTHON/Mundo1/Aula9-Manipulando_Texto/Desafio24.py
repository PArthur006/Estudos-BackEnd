#Faça um programa que leia o nome de uma cidade e diga se ela começa ou
#não com "Santo".

city = str(input('Qual a sua cidade? ')).strip()
print(city[:5].upper() == 'SANTO')