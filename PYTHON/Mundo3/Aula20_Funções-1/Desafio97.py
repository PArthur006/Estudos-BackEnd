# Faça um programa que tenha uma função chamada escreva(),
# que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.


def escreva(frase):
    tamanho = len(frase)
    print('~' * (tamanho+4))
    print(f'  {frase}  ')
    print('~' * (tamanho+4))


escreva('Bom dia')
escreva('Sábado animado')
