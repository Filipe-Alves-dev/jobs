tupla = ('Brinquedo', 'Cadeira', 'Televisao', 'Computador', 'Monitor',
         'Relogio', 'Anel', 'Chave', 'Moto', 'Carro', 'programador')
vogais = ('a','e','i','o','u')
for r in tupla:      
    print(f'\nA palavra {r.upper()} possui as vogais : ', end = ' ')
    for letra in r:
        if letra in vogais:
            print(f'{letra.lower()}', end= ' ')
