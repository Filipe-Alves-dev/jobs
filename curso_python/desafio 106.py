from time import sleep


def background_verde(frase):
    til = '~' * len(frase)
    print(f'\033[1;37;42m{til:<118}{frase:<118}{til}\033[m')
    return frase

    
def background_azul(frase):
    til = '~' * len(frase)
    print(f'\033[1;37;46m{til:<118}{frase:<118}{til:<118}\033[m')
    return frase
    
    
def background_branco(frase):
    print(f'\033[1;37;41m{frase:<118}')
    return frase


def help():
    while True:
        sleep(2)
        background_verde(' SISTEMA DE AJUDA PyHELP ')
        ajuda = str(input('Função ou biblioteca > '))
        if ajuda == 'len':
            background_azul(" Acessando o manual do comando  'len' ")
            sleep(2)
            background_branco("""Help on built-in function len in module builtins:

len(obj, /)
Return the number of items in a container.
                                    """)
        elif ajuda == 'print':
            background_azul(" Acessando o manual do comando 'print' ")
            sleep(2)
            background_branco("""Help on built-in function print in module builtins:

print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
                                    
    sep
    string inserted between values, default a space.
    end
    string appended after the last value, default a newline.
    file
    a file-like object (stream); defaults to the current sys.stdout.
    flush
    whether to forcibly flush the stream.
    """)
        elif ajuda == 'input':
            background_azul(" Acessando o manual do comando 'input' ")
            sleep(2)
            background_branco("""Help on built-in function input in module builtins:

input(prompt='', /)
    Read a string from standard input.  The trailing newline is stripped.
                                    
    The prompt string, if given, is printed to standard output without a
    trailing newline before reading input.
                                    
    If the user hits EOF (*nix: Ctrl-D, Windows: Ctrl-Z+Return), raise EOFError.
    On *nix systems, readline is used if available.
    """)   
        if ajuda == 'fim':
            break
    return help


help()

