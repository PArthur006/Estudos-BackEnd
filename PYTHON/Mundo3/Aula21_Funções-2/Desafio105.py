# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos
# e vai retornar um dicionário com as seguintes informações:
# -Quantidade de notas
# -A maior nota
# -A menor nota
# -A média da turma
# -A situação(opcional)


def notas(*aluno, sit=False):
    """

    :param aluno: Recebe diveras notas de um aluno
    :param sit(opcional): Mostra ou não a situação do aluno
    :return: Retorna um dicionário completo
    """
    geral = dict()
    media = sum(aluno) / len(aluno)
    geral['Quantidade de notas'] = len(aluno)
    geral['Maior nota'] = max(aluno)
    geral['Menor nota'] = min(aluno)
    geral['Média'] = f'{media:.2f}'
    if sit:
        if media >= 7:
            geral['Situação'] = 'Bom'
        elif media <= 4.99:
            geral['Situação'] = 'Ruim'
        else:
            geral['Situação'] = 'Razoável'
    return geral


resp = notas(10, 4, 10, sit=True)
print(resp)
