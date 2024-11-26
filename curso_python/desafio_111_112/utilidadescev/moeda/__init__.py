def metade(n, r):
    if r == True:
        f = f'R${n/2:.2f}' 
    else:
        f = n / 2
    return f


def dobro(n, r):
    if r == True:
        f = f'R${n*2:.2f}'
    else:
        f = n * 2
    return f


def aumentar(n, a, r):
    if r == True:
        f = f'R${n + ((a / 100) * n ):.2f}'
    else:
        f = n + ((a / 100) * n )
    return f


def diminuir(n , d, r):
    if r == True:
        f = f'R${n - ((d / 100) * n):.2f}'
    else:
        f = n - ((d / 100) * n)
    return f


def moeda(n):
    f = f'R${n:.2f}'
    return f

def resumo(n = 0, a = 10, d = 15):
    print('-' * 35)
    print(f'RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(n)}')
    print(f'Dobro do preço: \t{dobro(n, True):<30}')
    print(f'Metade do preço: \t{metade(n, True)}')
    print(f'{a}% de aumento: \t{aumentar(n, a, True)}')
    print(f'{d}% de redução: \t{diminuir(n, d, True)}')
    print('-' * 35)