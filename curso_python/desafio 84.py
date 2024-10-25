pessoas_peso = []
dados = []
extracao_pesos = []
nome_maior_peso = []
nome_menor_peso = []
while True:
    pessoas_peso.append(str(input('DIGITE O NOME DA PESSOA : ')))
    pessoas_peso.append(float(input('DIGITE O PESO DA PESSOA : ')))
    dados.append(pessoas_peso[:])
    while True:
        escolha = str(input('QUER CONTINUAR ? [S/N] ')).upper().strip()
        if escolha == 'S' or escolha == 'N':
            break
    pessoas_peso.clear()
    if escolha == 'N':
        break
print(f'Ao todo, você cadastrou {len(dados)} pessoas.')
for r in dados:
    extracao_pesos.append(r[1])
    if max(extracao_pesos) in r: 
        nome_maior_peso.append(r)
    elif min(extracao_pesos) in r:
        nome_menor_peso.append(r)       
print(f'O maior peso foi {max(extracao_pesos)}kg. Peso de {nome_maior_peso} ')
print(f'O menor peso foi {min(extracao_pesos)}kg. Peso de {nome_menor_peso}')
