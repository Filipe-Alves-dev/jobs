n = 0
cont = 1
total = 0
escolha = 'S'
while escolha == 'S':
    n = int(input('Digite um número :')) 
    cont+=1
    total+=n
    escolha = str(input('Quer continuar S/N?')).upper()
print(f'Você digitou {cont} números e a média foi de {total/cont} o maior valor foi  e o menor valor foi .')