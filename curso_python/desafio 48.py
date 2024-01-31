print('Abaixo estão somados todos valores  entre 1 e 500 que são multiplos de 3. ')
s = 0
vzs = 0 
for c in range(1 , 501):
    if  c % 3 == 0 and c % 2 != 0:
        s += c
        vzs = vzs + 1 
print(f'a soma de todos os {vzs} valores somados é igual a {s}', end=' ')


    
        