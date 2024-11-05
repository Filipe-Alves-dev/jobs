# pessoas = {'nome':'Filipe', 'sexo': 'Masculino', 'idade': 23}
# print(pessoas['idade'])
# print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos e é do sexo {pessoas["sexo"]}')
# print(pessoas.keys())
# print(pessoas.values())
# print(pessoas.items())
# for k in pessoas.keys():
#     print(k)
# for v in pessoas.values():
#     print(v)
# for v in pessoas.items():
#     print(v)
# for k, v in pessoas.items():
#     print(f'{k} = {v}')
    
brasil = []
estado1 = {'uf':'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf':'São Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)

print(brasil[1]['Sigla'])
print(brasil[0]['uf'])

# estado = dict()
# brasil = list()
# for c in range(3):
#     estado['uf'] = str(input('Unidade federativa: '))
#     estado['sigla'] = str(input('Sigla do Estado: '))
#     brasil.append(estado.copy())
# for e in brasil:
#     for v in e.items():
#         print(v, end=' ')