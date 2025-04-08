#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
#mostre uma mensagem dizendo que ele foi multado. a multa vai custar R$7,00
#por Km/h ultrapassado.
from time import sleep
vl = float(input('À quantos Km/h você estava? '))
if vl > 80:
    print('0o0o'*3)
    print('MULTADO!!!')
    print('0o0o'*3)
    sleep(2.0)
    print('Você terá que pagar R${} reais!'.format((vl-80)*7.00))
else:
    print('Pode continuar. Dirija com cuidado!')
