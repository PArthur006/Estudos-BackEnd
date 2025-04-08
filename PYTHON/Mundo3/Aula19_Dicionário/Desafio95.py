# Aprimore o desafio 93 para que ele funcione com vários jogadores,
# incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.

gols = list()
jogador = dict()
time = list()
total = 0
resp = ''
while True:
    jogador.clear()
    jogador['Nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas ele jogou: '))
    for c in range(1, partidas + 1):
        gols.append(int(input(f'Quantos gols na {c}° partida? ')))
    total = sum(gols)
    jogador['Gols'] = gols[:]
    jogador['Total de gols'] = total
    time.append(jogador.copy())
    gols.clear()
    total = 0
    while True:
        resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
        if resp not in 'SN':
            continue
        else:
            break
    if resp == 'S':
        continue
    elif resp == 'N':
        break
print(':=:'*15)
print('Cód ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print('')
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print('')
while True:
    jog = int(input('Escolha um jogador para ver seus gols:[999 para interromper]  '))
    if jog == 999:
        break
    if jog >= len(time):
        print(f'Não exite jogador com código {jog}!!!')
    else:
        for i, v in enumerate(time[jog]['Gols']):
            print(f'   =>Na partida {i+1} o jogador {time[jog]["Nome"]} fez {v} gols')
    print(':=:' * 15)
