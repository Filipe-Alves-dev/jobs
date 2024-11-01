from time import sleep
lista_aluno = [] #Variavel List temporaria para inserção de dados
lista_geral = [] #Variavel List que recebe toda a lista de alunos e notas
id = [] #Variavel List que é responsavel por mostrar o Id de cada aluno 
media = 0 #Variavel vazia que serve para fazer o calculo das médias dos alunos

#Laço de repetição onde se insere os valores, adiciona a uma lista e pergunta se o usuário quer cadastrarmais valores ou não
while True: 
    lista_aluno.append(str(input('Nome: '))) #Valor de inserção temporario de nome
    lista_aluno.append(float(input('Nota 1: '))) #Valor de inserção temporario de nota 1
    lista_aluno.append(float(input('Nota 2: '))) #Valor de inserção temporario de nota 2
    lista_geral.append(lista_aluno[:]) #Adiciona os valores a uma lista única
    lista_aluno.clear() #Limpa valores da lista temporaria 
    while True: #Laço para escolha 
        escolha = str(input('Quer continuar? [S/N] ')).upper().strip()
        if escolha in ['S', 'N']:
            break     
    if escolha == 'N':
        break
    
#Cabeçalho  da lista de alunos  
print('\033[1;33m=\033[m' * 60)      
print('No. NOME           MÉDIA')
print('\033[1;33m-\033[m' * 30)  

#Laço que mostra númeração, nome e nota média dos alunos
for a,c in enumerate(lista_geral):
    id.append(a)
    media = (c[1] + c[2]) / 2
    print(f'{a}   {c[0]:<10} {media:>10.1f}')
    
#Laço que pergunta qual item individual da lista de alunos ele quer mostrar.
while True:
    id_escolhida = int(input('Mostrar notas de qual aluno? (999 interrompe): ')) #variavel que escolhe o ID
    for p,n in enumerate(lista_geral): #laço que verifica o ID escolhida  
        if id_escolhida == p:
            print(f'Notas de {n[0]} são [{n[1]}, {n[2]}]') #Mostra as notas com ID individual
        if id_escolhida >= len(lista_geral) or id_escolhida < 0:
            print(f'Opções disponiveis: {p} de {n[0]}') #Recusa IDS não existentes
    if id_escolhida == 999:#Caso o usuário queira parar o laço digitar 999
        print('\033[1;33mFINALIZANDO...\033[m')
        sleep(1.5)
        print('\033[1;33m<<< VOLTE SEMPRE >>>\033[m')
        break