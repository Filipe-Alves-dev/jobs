# from time import sleep
# print('\033[01;032m-=-\033[m' * 20)
# print('                    Descubrindo o fatorial')
# print('\033[01;032m-=-\033[m' * 20)
# n = int(input('Digite um número para saber seu fatorial : '))
# resultado = 1
# contador = 1 
# while contador <= n:
#     resultado *= contador
#     contador += 1
# print(f'O fatorial do número {n} é igual a {resultado}')

# from math import factorial
# n = int(input('Digite um número para saber seu fatorial : '))
# fat = factorial(n)
# print (f'o fatorial do número {n} é igual a {fat}')
from math import factorial
n = int(input('Digite um número para saber o seu fatorial : '))
c = n
print(f'calculando fatorial!')
while c > 0:
    print(f' {c}', end= '')
    print(' x ' if c > 1 else ' = ', end= '' )
    c-=1
print (factorial(n) , end= '')
