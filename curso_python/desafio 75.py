from math import ceil
tupla = (int(input('Digite um primeiro número: ')),
         int(input('Digite um segundo número: ')),
         int(input('Digite um terceiro número: ')),
         int(input('Digite um quarto número: ')))
print(f'Você digitou os valores {tupla}')
print(f'O valor 9 apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O valor 3 apareceu na {tupla.index(3) + 1}° posição')
else:
    print(f'O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ',end='')
for n in tupla:
    if n % 2 == 0:
        print(n, end=' | ')