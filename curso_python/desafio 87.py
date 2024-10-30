lista_1 = []
lista_2 = []
lista_3 = []
total = [] 
soma_pares = 0
matrix = matrix2 = matrix3 = []
for m1 in range(0,3):
    matrix = int(input(f'Digite um valor para [0, {m1}]: '))
    lista_1.append(matrix)
    if matrix % 2 == 0:
        soma_pares += matrix
for m2 in range(0,3):
    matrix2 = int(input(f'Digite um valor para [1, {m2}]: '))
    lista_2.append(matrix2)
    if matrix2 % 2 == 0:
        soma_pares += matrix2
for m3 in range(0,3):
    matrix3 = int(input(f'Digite um valor para [2, {m3}]: '))
    lista_3.append(matrix3)
    if matrix3 % 2 == 0:
        soma_pares += matrix3
print('\033[1;33m=\033[m' * 60)
print('[  {}  ] [  {}  ] [  {}  ]'.format( lista_1[0] ,  lista_1[1], lista_1[2]))
print('[  {}  ] [  {}  ] [  {}  ]'.format( lista_2[0] ,  lista_2[1], lista_2[2]))
print('[  {}  ] [  {}  ] [  {}  ]'.format( lista_3[0] ,  lista_3[1], lista_3[2]))

print(f'A soma dos valores pares é {soma_pares}')