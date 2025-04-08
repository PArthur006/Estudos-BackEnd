salario = float(input('Digite o salário do funcionário:'))
aumentpcen = int(input('Digite a porcentagem a ser implementada:'))
pcent = aumentpcen/100 * salario
valor = pcent + salario
print('O valor salarial a ser somado será de R${}\nE o valor final será de R${}'.format(pcent ,valor))
