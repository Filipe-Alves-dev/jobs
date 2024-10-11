termo = int(input('Digite o termo : ' ))
razao = int(input('Digite a razao : '))
c = 1
print(f'{termo} => ', end='' )
while c < 10:
    termo += razao
    print (f'{termo} => ', end= '')
    c+=1
print('FIMMM')