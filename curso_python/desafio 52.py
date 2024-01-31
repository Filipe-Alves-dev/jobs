n = int(input('Digite um número inteiro para saber e ele é primo ou não :'))
if n > 1:
    for c in range(2, n):
        if n % c == 0:
            print(f'{n} não é primo ')
            break
        else:
            print(f'{n} é primo ')
            break