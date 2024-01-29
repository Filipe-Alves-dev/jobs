from random import randint
from emoji import emojize
from time import sleep
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;36m                         JOKENPÔ\033[m')
print('\033[1;33m-=-\033[m' * 20)
print(emojize('Escolha entre PEDRA, PAPEL e TESOURA e tente me vencer... :pedra:  :rolo_de_papel: :tesoura:', language='pt'))
itens = ('','PEDRA', 'PAPEL' , 'TESOURA')
escolha = int(input(emojize('Digite :\n[ 1 ] - Para :pedra:\n[ 2 ] - Para :rolo_de_papel:\n[ 3 ] - Para :tesoura:\n: ', language='pt')))
npc = randint(1,3)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('\033[1;33m-=-\033[m' * 20)
if npc == escolha:
   print(f'Empate!\nComputador escolheu {itens[npc]}\nJogador escolheu {itens[escolha]}')
elif escolha == 1 and npc == 2:
   print(emojize('HAHAHA Ganhei de você escolhi :rolo_de_papel:!\nVocê escolheu :pedra:', language='pt'))
elif escolha == 2 and npc == 3:
   print(emojize('HAHAHA Ganhei de você escolhi :tesoura:!\nVocê escolheu :rolo_de_papel:', language='pt'))
elif escolha == 3 and npc == 1:
   print(emojize('HAHAH Ganhei de você escolhi :pedra:!\nVocê escolheu :tesoura:', language='pt'))
elif escolha == 1 and npc == 3:
   print(emojize('Meus parabéns você me venceu! Eu escolhi :tesoura:!\nVocê escolheu :pedra:', language='pt'))
elif escolha == 2 and npc == 1:
   print(emojize('Meus parabéns você me venceu! Eu escolhi :pedra:!\nVocê escolheu :rolo_de_papel: ', language='pt'))
elif escolha == 3 and npc == 2:
   print(emojize('Meus parabéns você me venceu! Eu escolhi :rolo_de_papel:!\nVocê escolheu :tesoura:', language='pt'))
print('\033[1;33m-=-\033[m' * 20)