#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule
#seu Índice de Massa Corporal(IMC) e mostre seu status, de acordo com a tabela
#Abaixo de 18,5: abaixo do peso
#Entre 18,5 e 25: Peso ideal
#25 até 30: Sobre peso
#30 até 40: Obesidade
#Acima de 40: Obesidade mórbida
peso = float(input('Informe seu peso: '))
altura = float(input('Informe sua altura: '))
imc = peso/altura**2
if imc < 18.5:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Classificado como: \033[34;1;40mabaixo do peso\033[m')
elif imc >= 18.5 and imc < 25:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Classificado como: \033[32;1;40mpeso ideal\033[m')
elif imc >=25 and imc < 30:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Classificado como: \033[33;1;40mSobre peso\033[m')
elif imc >= 30 and imc < 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Classificado como: \033[31;1;40mObesidade\033[m')
elif imc >= 40:
    print('Seu IMC é {:.1f}'.format(imc))
    print('Classificado como: \033[7;30mObesidade Mórbida\033[m')
