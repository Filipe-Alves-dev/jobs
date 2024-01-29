from random import randint
from emoji import emojize
print('\033[1;33m-=-\033[m' * 20)
print('\033[1;36m                         JOKENPÔ\033[m')
print('\033[1;33m-=-\033[m' * 20)
print(emojize('Escolha entre PEDRA, PAPEL e TESOURA e tente me vencer... :pedra:  :rolo_de_papel: :tesoura:', language='pt'))
escolha = int(input(emojize('Digite :\n1 - Para :pedra:\n2 - Para :rolo_de_papel:\n3 - Para :tesoura:\n: ', language='pt')))
npc = randint(1,3)
if npc == escolha:
    print('Nós escolhemos o mesmo e acabamos empatando!')
elif escolha == 1 and npc == 2:
    print(emojize('HAHAHA Ganhei de você escolhi :rolo_de_papel:!"', language='pt'))
elif escolha == 2 and npc == 3:
    print(emojize('HAHAHA Ganhei de você escolhi :tesoura:!', language='pt'))
elif escolha == 3 and npc == 1:
    print(emojize('HAHAH Ganhei de você escolhi :pedra:!', language='pt'))
elif escolha == 1 and npc == 3:
    print(emojize('Meus parabéns você me venceu! Eu escolhi :tesoura:!', language='pt'))
elif escolha == 2 and npc == 1:
    print(emojize('Meus parabéns você me venceu! Eu escolhi :pedra: ', language='pt'))
elif escolha == 3 and npc == 2:
    print(emojize('Meus parabéns você me venceu! Eu escolhi :rolo_de_papel:', language='pt'))
