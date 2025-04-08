#Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores à R$1250,00, calcule um aumento de 10%. Para inferiores ou iguais 15%.
salario = float(input('Digite o seu salário: R$'))
if salario <= 1250.00:
    vl1 = 15*salario/100
    print('O seu salário atual será de R${} Reais.'.format(salario+vl1))
else:
    vl2 = 10*salario/100
    print('O seu salário atual será de R${} Reais.'.format(salario+vl2))
print('Foi um bom aumento né!')