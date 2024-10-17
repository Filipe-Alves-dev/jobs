from random import randint
menor = 11
maior = 0
print('Os valores sorteados foram : ',end='')
for c in range(0,5):
    c = randint(1,10)
    tupla = (c)
    print(tupla,end=' ')
    if tupla > maior:
        maior = tupla
    if tupla < menor:
        menor = tupla
print(f'\nO maior valor gerado foi {maior}\nO menor valor gerado foi {menor}')