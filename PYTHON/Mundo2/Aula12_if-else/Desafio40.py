#Crie um programa que leia duas notas de um aluno e calcule sua média,
#mostrando uma mensagem no final, de acordo com a média atingida
#Média abaixo de 5.0 REPROVADO
#Média entre 5.0 e 6.5 RECUPERAÇÃO
#Média acima de 6.5 APROVADO
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
media = (nota1 + nota2)/2
if media < 5.0:
    print('Aluno {}REPROVADO{}'.format('\033[41;30;1m', '\033[m'))
    print('Sua média foi {}'.format(media))
elif media >= 5.0 and media < 6.9:
    print('Aluno de {}RECUPERAÇÃO{}'.format('\033[43;30;1m', '\033[m'))
    print('Sua média foi {}'.format(media))
elif media > 6.9:
    print('Aluno {}APROVADO{}'.format('\033[42;30;1m', '\033[m'))
    print('Sua média foi {}'.format(media))
