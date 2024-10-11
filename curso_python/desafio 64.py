n = int(input('Digite 999 para parar : '))
total = 0
cont = 1
while n != 999:
    n = int(input('Digite 999 para parar : '))
    total += n
    cont += 1
print(f'Você digitou {cont - 1} números e a soma de todos os números é igual a {total - 999}.')