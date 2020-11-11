from random import randint
from time import sleep
from operator import itemgetter
dict = {'jogador1' : randint(1, 6),
        'jogador2' : randint(1, 6),
        'jogador3' : randint(1, 6),
        'jogador4' : randint(1, 6)}

ranking = []

for k, v in dict.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
print('\n')
ranking = sorted(dict.items(), key=itemgetter(1), reverse=True)
for i, j in enumerate(ranking):
    print(f'{i + 1} lugar: {j[0]} com {j[1