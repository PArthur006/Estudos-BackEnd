#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
#se elas podem ou não formar um triângulo.
reta1 = float(input('Primeiro segmento: '))
reta2 = float(input('Segundo segmento: '))
reta3 = float(input('Terceiro segmento: '))
if (reta2 - reta3)<reta1<reta2+reta3:
    print('É \033[4;32mPOSSÍVEL\033[m criar um triângulo com essas retas.')
else:
    print('É \033[4;32mNÃO É POSSÍVEL\033[m criar um triângulo com essas retas')
