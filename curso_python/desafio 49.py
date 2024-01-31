print('\033[1;36m-=-' * 20)
print('Calculadora de tabuada:')
print('\033[1;36m-=-\033[m' * 20 )
n = int(input('Digite um número para saber sua tabuada : '))

for t in range(1,11,1):
    print(f'{n} x {t} = {n * t}')
    