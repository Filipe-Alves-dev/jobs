from time import sleep

# Cores para o fundo
c = ('\033[m',        # 0 - sem cores
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
    )


def ajuda(com):
    título(f'Acessando o manual do \'{com}\'', 4)
    print(c[6], end='')  # Cor do fundo branco
    help(com)
    print(c[0], end='')  # Restaura para a cor padrão
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')  # Cor do fundo conforme especificado
    print('~' * tam)
    print(f' {msg} ')
    print('~' * tam)
    print(c[0], end='')  # Restaura a cor para o padrão


# Programa Principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 2)  # Exibe o título em verde
    comando = str(input("Função ou Biblioteca > "))  # Recebe o comando do usuário
    if comando.upper() == 'FIM':  # Se o usuário digitar 'FIM', encerra o programa
        break
    else:
        ajuda(comando)  # Chama a função de ajuda
título('ATÉ LOGO!', 1)  # Exibe 'ATÉ LOGO!' com fundo vermelho
