lista = []
cont = 0
for f in range(0,5):
    num = int(input('Digite um número para adicionar a lista: '))
    if f == 0 or num > lista[-1]:
        lista.append(num)
        print('valor inserido ultima posição da lista.')
    else :
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Valor inserido na posição {pos} da lista.')
                break
            pos += 1
print('=' * 60)
print(f'Os valores digitados foram {lista}')