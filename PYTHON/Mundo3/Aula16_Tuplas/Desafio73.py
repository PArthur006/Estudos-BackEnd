#Crie uma tupla com os 20 primerios colocados da Tabela de Campeonato de Futebol, na ordem de
#Colocação. Depois mostre:
#Os 5 primeiros times;
#Os ultimos 4 colocados;
#Times em ordem alfabética;
#Em que posição está o time da Chapecoense(Não tem esse time no momento, então escolhi o meu)
times = ('Flamengo', 'Internacional', 'Atlético-MG', 'São Paulo', 'Fluminense', 'Grêmio', 'Palmeiras',
         'Santos', 'Atlético-PR', 'Bragantino', 'Ceará SC', 'Corinthians', 'Atlético-GO', 'Bahia',
         'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Coritiba', 'Botafogo')
print(f'Os 5 primeiros times são: {times[0:5]}')
print(f'Os últimos colocados são {times[16:]}')
print(f'Em ordem alfabética os times seriam ordenados assim: {sorted(times)}')
print(f'O time para que eu torço está na {times.index("Atlético-MG")+ 1}')
