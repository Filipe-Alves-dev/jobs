from random import randint
from emoji import emojize
sorteio = randint(0,10)
print('\033[033;032m-=-\033[m' * 20)
print('                  \033[033;034m-Jogo de advinhação-\033[m')
print('\033[033;032m-=-\033[m' * 20)
n_jogador = int(input(emojize('Escolhi um número entre 0 e 10 , tente acertar... :rosto_zangado_com_chifres: :', language='pt')))
while sorteio != n_jogador:
   n_jogador= (int(input('Número errado! Tente novamente... :')))
print(emojize(f'Parabéns, você acertou! O número que escolhi foi {sorteio} :troféu:!', language='pt'))