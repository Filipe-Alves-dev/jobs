cadastro_pessoas = {}
pessoas = []
idades = []
mulheres = []
media_idade = 0

def cadastrar_pessoas():
    '''Cadastra dados das pessoas.'''
    while True:
        print('\033[1;33m-\033[m'* 40)
        cadastro_pessoas["nome"] = str(input('Nome: '))
        
        while True:
            cadastro_pessoas["sexo"] = str(input('Sexo: [M/F] ')).upper()
            if cadastro_pessoas['sexo'] in ['M','F']:
                break
            print('Erro! Por favor, digite apenas M ou F.')
            
        cadastro_pessoas["idade"] = int(input('Idade: '))
        pessoas.append(cadastro_pessoas.copy())
        idades.append(cadastro_pessoas['idade'])
        
        '''Adiciona os nomes das mulheres a lista.'''
        if cadastro_pessoas["sexo"] == 'F':
            mulheres.append(cadastro_pessoas["nome"]) 
            
        print('\033[1;33m-\033[m'* 40)
        
        while True:
            
            continuar = str(input('Quer continuar? [S/N] ')).upper()
            if continuar in ['S','N']:
                break 
            print('ERRO! Reponda apenas S ou N.')
            
        if continuar == 'N':
            break
        
def mostrar_dados():
    '''Mostra dados das pessoas.'''
    print('\033[1;33m-\033[m'* 40)
    print(f'- O grupo tem {len(pessoas)} pessoas.')
    media_idades = 0
    for e in idades:
        media_idades += e 
    media_idade = (media_idades / len(idades))
    print(f'- Média de idade do grupo : {media_idade:.2f} anos.')
    print(f'- Lista de mulheres cadastradas :', end=' ')
    for m in mulheres:
        print(m, end=' ')
    print('\n- Lista de pessoas que tem idade acima da média :') 
    for v in pessoas:
        if v["idade"] > media_idade:
              print(f'\n{v}')    
    print('\033[1;33m-\033[m'* 40)
    print('\n\033[1;33m == ENCERRADO == \033[m')
    
def main():
    cadastrar_pessoas()
    mostrar_dados()
    
if __name__ == "__main__":
    main()
