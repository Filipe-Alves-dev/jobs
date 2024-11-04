jogador_gols = {}

def adicionar_jogador():
    '''Adiciona o nome do jogador ao dicionário jogador_gols.'''
    print('\033[1;33m-\033[m'* 40)
    jogador_gols["nome"] = str(input('Nome do jogador: '))

def adicionar_partidas_gols():
    '''Adiciona partidas/gols ao jogador.'''
    gols = []
    partidas = int(input(f'Quantas partidas {jogador_gols["nome"]} jogou? '))
    for c in range(1, partidas + 1):
        gol = int(input(f'Quantos gols na partida {c}? '))
        gols.append(gol)
    jogador_gols["gols"] = gols
    print('\033[1;33m-\033[m'* 40)

def mostrar_valores_soma_gols():
    '''Mostra valores do dicionario jogador_gols.'''
    total_gols = 0
    for k,v in jogador_gols.items():
        print(f'O campo {k} tem o valor {v}.')
    for c in jogador_gols["gols"]:
        total_gols += c
        jogador_gols["total_gols"] = total_gols
    print(f'O jogador fez um total {total_gols} gols.')
    print('\033[1;33m-\033[m'* 40) 
    
def mostrar_partida_gol():
    '''Mostra os resultados de estatistica do jogador.'''
    lista_gols = []
    lista_gols = jogador_gols["gols"] 
    print(f'O jogador {jogador_gols["nome"]} jogou {len(jogador_gols["gols"])} partidas.')
    for p, e in enumerate(lista_gols):
        print(f'=> Na partida {p + 1}, fez {e}')
    print('\033[1;33m-\033[m'* 40)
    print(f'Totalizando : {jogador_gols["total_gols"]} gols.')
    print('\033[1;33m-\033[m'* 40)
    
def main():
    adicionar_jogador()
    adicionar_partidas_gols()
    mostrar_valores_soma_gols()
    mostrar_partida_gol()

if __name__ == "__main__":
    main()
