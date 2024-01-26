from random import randint
from emoji import emojize
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;36m                         JOKENPÔ\033[m')
print('\033[1;33m-=-\033[m' * 20)
print(emojize('Escolha entre PEDRA, PAPEL e TESOURA e tente me vencer... :pedra:  :rolo_de_papel: :tesoura:', language='pt'))
escolha = int(input('Digite :\n1 - Para PEDRA\n2 - Para PAPEL\n3 - Para PEDRA\n: '))
npc = randint(1,3)
if npc == escolha:
    print('Nós escolhemos o mesmo e acabamos empatando!')
elif escolha == 1 and npc == 2:
    print(emojize('HAHAHA Ganhei de você escolhi papel! :rolo_de_papel:', language='pt'))
    print(npc)