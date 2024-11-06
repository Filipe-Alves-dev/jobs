jogador_gols = {}
estatistica = []

def adicionar_jogadores():
    '''Adiciona jogadores.'''
    while True:
            '''Adiciona o nome do jogador ao dicionário jogador_gols.'''
            print('\033[1;33m-\033[m'* 40)
            jogador_gols["nome"] = str(input('Nome do jogador: '))
        
            '''Adiciona partidas/gols ao jogador.'''
            gols = []
            partidas = int(input(f'Quantas partidas {jogador_gols["nome"]} jogou? '))
            
            for c in range(1, partidas + 1):
                gol = int(input(f'Quantos gols na partida {c}? '))
                gols.append(gol)
            jogador_gols["gols"] = gols
            soma_gols = 0
            
            for soma in gols:
                soma_gols += soma
            jogador_gols["total"] = soma_gols
            estatistica.append(jogador_gols.copy())      
            print('\033[1;33m-\033[m'* 40)
            
            while True:
                escolha = str(input('Quer continuar? [S/N] ')).upper()
                if escolha in ['S','N']:
                    break
                
            if escolha == 'N':
                break
       
def mostrar_estatisticas():
    '''Mostra valores do dicionario jogador_gols.'''
    print(estatistica)   
    print('\033[1;33m-\033[m'* 60)
    print('cod  nome            gols                      total')
    
    for cod, m in enumerate(estatistica):
        print(f"{cod:<4} {m['nome']:<15} {str(m['gols']):<10} {m['total']:>17}")
    print('\033[1;33m-\033[m'* 60)
    
def mostrar_dados_ind():
    selecionar =  int(input('Mostrar dados de qual jogador? '))
    for s in estatistica:
        print(f'Levantamento do jogador {s[0][0]}')
    
def main():
    adicionar_jogadores()
    mostrar_estatisticas()
    mostrar_dados_ind()
if __name__ == "__main__":
    main()
