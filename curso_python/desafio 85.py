lista_num = [[],[]]
for v in range(1,7):
    while True:
        num = int(input(f'Digite o {v}º valor : '))
        if num in lista_num[0] or num in lista_num[1]:
            print('Esse programa nao aceita números repetidos')
        else:
            if num % 2 == 0:
                lista_num[0].append(num)
            else: 
                lista_num[1].append(num)
            break
print(f'Os valores pares digitados foram: {sorted(lista_num[0])}')
print(f'Os valores ímpares digitados foram: {sorted(lista_num[1])}')