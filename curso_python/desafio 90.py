nome_media = {}
nome_media["nome"] = str(input('Digite o nome do aluno: '))
nome_media["media"] = float(input(f'Média de {nome_media["nome"]}: '))
if nome_media["media"] >= 6:
    nome_media["situacao"] = 'Aprovado'
else:
    nome_media["situacao"] = 'Reprovado'
for k, v in nome_media.items():
    print(f'{k} é igual a {v}')
    
    
    