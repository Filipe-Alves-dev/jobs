from random import randint
from time import sleep

list_num = []

def sorteio():
    print('Sorteando 5 valores da lista : ', end=' ')
    for c in range(1,6):   
        numeros = randint(1,9)
        sleep(1)
        print(numeros, end= ' ')
        list_num.append(numeros)    


def soma_pares():
    soma_par = 0
    for p in list_num:
        if p % 2 == 0:
            soma_par += p
    print(f'\nSomando os valores de {list_num} temos {soma_par}')


sorteio()
soma_pares()
