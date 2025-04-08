# Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da
# digitação de um número de tipo invállido. Aproveite e crie também uma função leiaFloat()
# com a mesma funcionalidade.


from Modulo.utiliadesCeV import leia
z = leia.leiaInt('Digite um número inteiro: ')
q = leia.leiaFloat('Digite um número real: ')
print(f'O número inteiro informado foi {z} e o real foi {q}')
