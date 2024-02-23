s = 0
cont = 0
for c in range(1, 7):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        s += n  
        cont += 1  
print(f'Você informou {cont} números pares. A soma de todos os números  pares digiados é {s}')
   