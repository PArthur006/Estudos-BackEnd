import math
ang = float(input('Qual o ângulo? '))
se = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))
print('O ângulo de {} possui o Seno de {:2f}, o Cosseno de {:2f}, e a Tangente de {:2f}'.format(ang, se, cos ,tang))
