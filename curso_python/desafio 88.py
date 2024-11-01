import random
from time import sleep
print('\033[1;33m=\033[m' * 60)
cabecalho = '\033[1;33mJOGA NA MEGA SENA\033[m'
print(f'{cabecalho:^60}')
print('\033[1;33m=\033[m' * 60)
n_jogos = int(input('Quantos jogo você quer que eu sorteie? '))
lista_jogos = []
pos = []
for r in range(0, n_jogos):
    sorteio  = random.sample(range(1,61),7)
    lista_jogos.append(sorteio) 
for c,j in enumerate(lista_jogos):
    pos.append(c)
    sleep(1.5)
    print(f'Jogo {c+1}: {j}')
print('\033[1;33m=\033[m' * 60)
