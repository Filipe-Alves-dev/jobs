from emoji import emojize
from random import randint
from time import sleep
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar...')
print('-=-' * 20)
ns = randint(0,5)#programa pensa um número...
n = int(input('Em que número eu pensei ? '))#jogador tenta adivinhar o número...
print('Processando...')
sleep(3)
if n > 5 or n < 0 : 
     print('Número invalido!')
elif ns == n: 
    print(emojize(f'Você acertou o número, Parabéns!!! :troféu:\nNúmero sorteado: {ns}', language='pt'))
else:
    print(emojize(f'Infelizmente você não acertou o número :rosto_chorando:\nNúmero sorteado : {ns}', language = 'pt'))
