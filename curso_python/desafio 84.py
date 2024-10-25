pessoas_peso = []
dados = []
extracao_pesos = []
nome_maior_peso = []
nome_menor_peso = []
while True:
    print('\033[1;33m=\033[m'* 60)
    pessoas_peso.append(str(input('DIGITE O NOME DA PESSOA : ')))
    pessoas_peso.append(float(input('DIGITE O PESO DA PESSOA : ')))
    dados.append(pessoas_peso[:])
    pessoas_peso.clear()
    print('\033[1;33m=\033[m'* 60)
    while True:
        escolha = str(input('QUER CONTINUAR ? [S/N] ')).upper().strip()
        if escolha == 'S' or escolha == 'N':
            break
    if escolha == 'N':
        break
print('\033[1;33m=\033[m'* 60)
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
for d in dados:
    extracao_pesos.append(d[1])
maior_peso = max(extracao_pesos)     
menor_peso = min(extracao_pesos)  
for r in dados:
    if maior_peso in r:
        nome_maior_peso.append(r[0])
    if menor_peso in r:
        nome_menor_peso.append(r[0])
print(f'O maior peso foi {maior_peso}kg. Peso de {nome_maior_peso}')
print(f'O menor peso foi {menor_peso}kg. Peso de {nome_menor_peso}')
print('\033[1;33m=\033[m'* 60)