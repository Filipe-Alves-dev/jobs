from time import sleep


def linha():
    print('\033[1;33m-=\033[m' * 30)


def maior(* num):
    linha()
    print('Analisando os valores passados... ')
    for c in num:
        print(c, end=' ')
        sleep(0.5)
    print(f'Foram informados {len(num)} valores ao  todo.')
    print(f'O maior valor infomado foi {max(num)}')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior(0)