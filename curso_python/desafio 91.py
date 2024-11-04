from random import randint
from time import sleep
from operator import itemgetter
print(f'\033[1;33m-\033[m' * 30)
print('== VALORES SORTEADOS ==')
print(f'\033[1;33m-\033[m' * 30)
jogadores = dict()
for c in range(0,4):
    jogadores[f"jogador {c + 1}"] = randint(1,6)
ranking = list()
for k,v in jogadores.items():
        print(f'O {k} tirou {v} no dado')
        sleep(1)
print(f'\033[1;33m-\033[m' * 30)
print('== RANKING DOS JOGADORES ==')
print(f'\033[1;33m-\033[m' * 30)
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° lugar: {v[0]} com {v[1]}')
    sleep(1)