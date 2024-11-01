# lista_1 = []
# lista_2 = []
# lista_3 = []
# for m1 in range(0,3):
#     matrix = [int(input(f'Digite um valor para [0, {m1}]: '))]
#     lista_1.append(matrix)
# for m2 in range(0,3):
#     matrix2 = [int(input(f'Digite um valor para [1, {m2}]: '))]
#     lista_2.append(matrix2)
# for m3 in range(0,3):
#     matrix3 = [int(input(f'Digite um valor para [2, {m3}]: '))]
#     lista_3.append(matrix3)

# print('\033[1;33m=\033[m' * 60)
# print('[  {}  ] [  {}  ] [  {}  ]'.format(* lista_1[0] ,*  lista_1[1],* lista_1[2]))
# print('[  {}  ] [  {}  ] [  {}  ]'.format(* lista_2[0] ,*  lista_2[1],* lista_2[2]))
# print('[  {}  ] [  {}  ] [  {}  ]'.format(* lista_3[0] ,*  lista_3[1],* lista_3[2]))

# Inicializando a matriz 3x3
matriz = []

# Coletando dados do usuário
for i in range(3):
    linha = []  # Criando uma nova linha para a matriz
    for j in range(3):
        valor = int(input(f'Digite um valor para [{i}, {j}]: '))
        linha.append(valor)  # Adicionando o valor à linha
    matriz.append(linha)  # Adicionando a linha à matriz

# Exibindo a matriz formatada
print('\033[1;33m=\033[m' * 60)
for linha in matriz:
    print('[ {} ] [ {} ] [ {} ]'.format(*linha))
