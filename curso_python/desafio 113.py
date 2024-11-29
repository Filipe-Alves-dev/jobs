


def Leiaint(a,b):
    while type(a) != int:
        try:
            a = int(input('Digite um número inteiro: '))
        except (ValueError, TypeError):
            print(f'\033[91mERRO: por favor, digite um número inteiro válido.\033[m')
        except KeyboardInterrupt:
            print('Usuário não digitou o número.')
            a = 0
    while type(b) != float:
        try:
            b= float(input('Digite um número real: '))
        except (ValueError, TypeError):
            print(f'\033[91mERRO: por favor digite um número real válido.\033[m')
        except KeyboardInterrupt:
            print('Usuário não digitou o número.')
            b = 0.0
    if b == 0.0:
        b = 0
    print(f'O valor inteiro digitado foi {a} e o real foi {b}')


Leiaint(a = False , b = False)
