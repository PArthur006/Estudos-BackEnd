from math import floor
rl = float(input('Quanto possúi na carteira?'))
dl = 3.27
vl = rl/dl
print('Você poderá comprar {} em dólares'.format(floor(vl)))
