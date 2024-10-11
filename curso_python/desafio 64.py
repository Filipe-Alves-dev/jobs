n = total = cont = 0
n = int(input('Digite 999 para parar : '))
while n != 999:
    total += n
    cont += 1
    n = int(input('Digite 999 para parar : '))
print(f'Você digitou {cont} números e a soma de todos os números é igual a {total}.')