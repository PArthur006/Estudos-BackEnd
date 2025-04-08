#Refaça o desafio 35 dos triângulos, acrescentando o recurso de mostrar que
#tipo de triângulo será formado.
#Equilátero - todos os lados iguais
#Isósceles - dois lados iguais, um diferente
#Escaleno - todos os lados diferentes
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if (reta2 - reta3)<reta1<reta2+reta3:
    print('\033[4;32mÉ POSSÍVEL\033[m criar um triângulo com essas retas')
    if reta1 == reta2 or reta2 == reta3 or reta1 == reta3:
        print('Forma-se um triângulo Equilátero')
    elif reta1 != reta2 != reta3:
        print('Forma-se um triângulo Escaleno')
    else:
        print('Forma-se um triângulo Isósceles')
else:
    print('\033[4;32mNÃO É POSSÍVEL\033[m criar um triângulo com essas retas')
