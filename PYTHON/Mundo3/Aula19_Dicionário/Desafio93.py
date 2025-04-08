# Crie um programa que gerencie o aproveitamento de um jogador de futebol.
# O programa vai ler o nome do jogador e quantas partudas ele jogou.
# Depois vai ler a quantidade de gols feitos em cada partida.
# No final, tudo isso será guardado em um dicionário,
# incluindo o total de gols feitos durante o campeonato.

gols = []
jogador = {}
total = 0
jogador['Nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas ele jogou: '))
for c in range(1, partidas + 1):
    gols.append(int(input(f'Quantos gols na {c}° partida? ')))
total = sum(gols)
jogador['Gols'] = gols[:]
jogador['Total de gols'] = total
print(':=:'*15)
print(jogador)
print(':=:'*15)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print(':=:'*15)
print(f'O jogador {jogador["Nome"]} jogou {partidas} partidas.')
for c, v in enumerate(gols):
    print(f'   =>Na partida {c+1}, fez {v} gols.')
print(f'Ele fez um total de {total} gols.')
