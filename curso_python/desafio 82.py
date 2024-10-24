escolha = 'S'
list_num = list_pares = list_impar = []
print('\033[1;33m=\033[m' * 60)
while escolha == 'S':
    num = int(input('Digite um número : '))
    list_num.append(num)
    escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
print('\033[1;33m=\033[m' * 60)
print('A lista dos números digitados é : ',* list_num)
print('Os números pares da lista são : ', end=' ')
for p in list_num:
    if p % 2 == 0:
        list_pares = [p]
        print(* list_pares, end=' ')
print('\nOs números ímpares da lista são : ', end=' ')
for i in list_num:
    if i %  2 == 1:
        list_impar = [i]
        print(* list_impar, end=' ')
print('\n','\033[1;33m=\033[m' * 60)