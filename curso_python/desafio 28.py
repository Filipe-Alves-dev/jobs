from random import randint
n = int(input('Digite um número entre 0 e 5 : '))
ns = randint(0,5)
if n > 5 or n < 0 : 
     print('Número invalido!')
elif ns == n: 
    print(f'Você acertou o número, Parabéns!!! número sorteado: {ns}')
else:
    print(f'Infelizmente você não acertou o número :( número sorteado : {ns}')
    