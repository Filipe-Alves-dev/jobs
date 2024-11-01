print('\033[1;33m=\033[m' * 50)
nome = 'PADARIA BARREIRO'
print(f'{nome: ^50}')
list_tupla = ('Refrigerante 2l', 10, 'Suco', 5, 'Café com leite', 2.5, 'Café', 2, 'Pastel', 3, 'Coxinha', 3, 'Enrolado de salsicha', 3, 'Hamburguer', 6) 
print('\033[1;33m=\033[m' * 50)
for n in list_tupla:
    if type(n) is str:
        print(f'{n:.<42}',end='' )
    else: 
        print(f'R${n:.2f}')
print('\033[1;33m=\033[m' * 50)