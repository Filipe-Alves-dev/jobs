nome_media = {}
nome_media["Nome"] = str(input('Digite o nome do aluno: '))
nome_media["Média"] = float(input(f'Média de {nome_media["Nome"]}: '))
if nome_media["Média"] >= 6:
    nome_media["Situacão"] = 'Aprovado'
else:
    nome_media["Situacão"] = 'Reprovado'
for k, v in nome_media.items():
    print(f'{k} é igual a {v}')
    
    
    