vcom = float(input('Insira o valor da compra:'))
vdesc = float(input('Insira o valor do desconto:'))
desc = vdesc/100 * vcom
print('O desconto foi de R${}.\nE o valor final da compra é de R${}.'.format(desc ,vcom-desc))
