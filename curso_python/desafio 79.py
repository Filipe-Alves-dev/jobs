lista = []
print('\033[1;33m=\033[m' * 60)    
while True:
    valor = int(input('Digite um valor: '))
    if valor in lista:
        print('Valor duplicado! Não vou adicionar...')     
    else:  
        lista.append(valor)
    escolha = str(input('Quer continar? [S/N] ')).upper().strip()
    if escolha in 'N':
        break
print('\033[1;33m=\033[m' * 60)
print(f'Você digitou os valores {sorted(lista)}')
print('\033[1;33m=\033[m' * 60)
