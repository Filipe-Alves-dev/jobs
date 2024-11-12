

def jogador_gol(n, g):
    """_summary_

    Args:
        n : Insere número de
        g : _description_
    """
    if n == '':
        n = '<desconhecido>'
    print(f'O jogador {n} fez {g} gol(s) no campeonato')
    
    
print('-' * 30)
jogador_gol(n = str(input('Nome do jogador: ')),
            g= str(input('Número de gols: ')))
