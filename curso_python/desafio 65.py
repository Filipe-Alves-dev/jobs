lista = []
cont = 0
total = 0
escolha = 'S'
while escolha == 'S':
    n = int(input('\nDigite um número : ')) 
    cont+=1
    total+=n
    escolha = str(input('\nQuer continuar S/N? : ')).upper()
    if escolha != 'N' and escolha != 'S':
        escolha = str(input('\nDigitou um caractere invalido. Quer continuar S/N? ')).upper()
    lista += [n]
print(f'\nVocê digitou {cont} números e a média foi de {total/cont} o maior valor foi {max(lista)} e o menor valor foi {min(lista)}. ')
print(n)