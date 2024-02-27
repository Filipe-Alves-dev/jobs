from time import sleep
print('\033[01;032m-=-\033[m' * 20)
print('                    Descubrindo o fatorial')
print('\033[01;032m-=-\033[m' * 20)
n = int(input('Digite um número para saber seu fatorial : '))
resultado = 1
contador = 1 
while contador <= n:
    resultado *= contador
    contador += 1
print(f'O fatorial do número {n} é igual a {resultado}')

    