num = [2,5,9,1]
num [2] = 3 # substitui indice
num.append(7) # adiciona indice
num.sort(reverse=True) # sort sozinho ordena os valores , com o reverse=True ele inverte a ordem
num.insert(2,0) # nesse caso esta inserindo na posição 2 o indice 0
num.pop(2) # remove o 0 que esta na posição 2
num.insert(2, 2)
if 5 in num:
    num.remove(5)
else:
    print('Não achei o número 5')
print(num)
print(f'Essa lista tem {len(num)} elementos.') #lê quantos indices contem na variavel   
valores = []
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...', end='')
for c, r in enumerate(valores):
    print(f'\nNa posção {c} temos os valores {r}')
print('Cheguei ao final da lista.')
valores1 = []
for l in range(1,5):
    valores1.append(int(input('Digite um valor : '))) # adicionando variaveis
print(valores1)
a = [2, 3, 4, 7]
b = a # Interliga os dois 
b[2] = 8
b = a[:] # Cria uma cópia de a em b
print (f'A lista A: {a}')
print (f'A lista B: {b}')
