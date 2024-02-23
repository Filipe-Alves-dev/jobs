n = int(input('Digite um número inteiro para saber e ele é primo ou não :'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
print(f'O número {n} foi divisivel {tot} vezes.')
if tot == 2:
    print(f'O número {n} é primo!')
else:
    print(f'O número {n} digitado não é primo!')

       