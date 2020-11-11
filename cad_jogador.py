jogador = {'nome': str((input('Nome:')))}
partidas = int(input(f'Quantas partidas jogou?'))
gols = []
total = 0
for c in range(0, partidas):
    gols.append(int(input(f'Quantos gols {jogador["nome"]} fez na partida {c+1}? ')))
    jogador['gols'] = gols[: ]
total = sum(gols)
jogador['total'] = total
print(jogador)
for k, v in jogador.items():
    print(f'{k} tem valor {v}')
print('\n')
print(f'{jogador["nome"]} jogou {partidas} partidas')
for k, v in enumerate(jogador['gols']):
    print(f'Na partida {k + 1} fez {v} gols')
