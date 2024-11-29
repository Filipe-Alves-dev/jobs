

lista_pessoas = ['Wellington Oliveira',52, 'Filipe Alves', 23, 'Luis Felipe Furtado', 28, 'Marcelo Rabelo', 47, 'Marcela basques', 52, 'Yago Zapata', 35, 'Angelo Zanini', 19, 'Vagner Gavião', 35, 'Vicentina Maria',73 ]
lista_pessoas_add = []

def cadastro_pessoa(n):
    n = '0'
    while n.isnumeric():
        n = str(input('Nome:'))
        if n.isnumeric():
            print('\033[91mERRO: Digite um nome válido.\033[m')
    lista_pessoas.append(n)
    for i in lista_pessoas:
        if type(i) is str:
            print(f'{i:<40}', end=' ')
        else:
            print(f'{i} anos')
        lista_pessoas_add.append(lista_pessoas[:])
        
cadastro_pessoa(n = 0)