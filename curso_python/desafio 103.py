

def jogador_gol(n, g):
    """_summary_

    Args:
        n : Insere número de
        g : _description_
    """
    if n == '':
        n = '<desconhecido>'
    if g.isalpha() or g == '':
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato')
    
    
print('-' * 30)
jogador_gol(n = str(input('Nome do jogador: ')),
            g= str(input('Número de gols: ')))
