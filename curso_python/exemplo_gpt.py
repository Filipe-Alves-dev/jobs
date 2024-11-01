from time import sleep

def adicionar_aluno(alunos):
    """Adiciona um aluno à lista de alunos."""
    nome = input('Nome: ')
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    alunos.append({'nome': nome, 'notas': [nota1, nota2], 'media': media})

def mostrar_alunos(alunos):
    """Exibe a lista de alunos e suas médias."""
    print('\033[1;33m=\033[m' * 60)      
    print('No. NOME           MÉDIA')
    print('\033[1;33m-\033[m' * 30)  
    for i, aluno in enumerate(alunos):
        print(f'{i}   {aluno["nome"]:<10} {aluno["media"]:>10.1f}')

def mostrar_notas(alunos):
    """Mostra as notas de um aluno específico."""
    while True:
        pos_escolhida = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
        if pos_escolhida == 999:
            print('\033[1;33mFINALIZANDO...\033[m')
            sleep(1.5)
            print('\033[1;33m<<< VOLTE SEMPRE >>>\033[m')
            break
        if 0 <= pos_escolhida < len(alunos):
            aluno = alunos[pos_escolhida]
            print(f'Notas de {aluno["nome"]} são [{aluno["notas"][0]}, {aluno["notas"][1]}]')
        else:
            print('ID inválido! Tente novamente.')

def main():
    alunos = []
    
    while True:
        adicionar_aluno(alunos)
        continuar = input('Quer continuar? [S/N] ').strip().upper()
        if continuar == 'N':
            break
    
    mostrar_alunos(alunos)
    mostrar_notas(alunos)

if __name__ == "__main__":
    main()
