lista = []
escolha = 'S'
print('\033[1;33m=\033[m' * 60)
while escolha == 'S':
    valor = int(input('Digite um valor: '))
    lista.append(valor)
    escolha = str(input('Quer continuar? [S/N]')).upper().strip()
print('\033[1;33m=\033[m' * 60)
print(f'Foram digitados {len(lista)} números.\n')
lista.sort()
print(f'Os valores em ordem ficam assim {lista}\n')
lista.sort(reverse=True)
print(f'Os valores em ordem inversa ficam assim {lista}\n')
if 5 in lista:
    print('Existe o número 5 nessa lista!')
else:
    print('Nao existe o número 5 nessa lista!')
print('\033[1;33m=\033[m' * 60)