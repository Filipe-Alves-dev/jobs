termo = int(input('Digite o termo : ' ))
razao = int(input('Digite a razao : '))
c = 1
mais = 10
total = 0 
print(f'{termo} => ', end='' )
while mais != 0:
    total += mais
    while c < total:
        termo += razao
        print (f'{termo} => ', end='')
        c+=1   
    print('Pausa', end='')
    mais = int(input('\nVoce deseja mostrar mais quantos termos: '))
print('FIMMM')
