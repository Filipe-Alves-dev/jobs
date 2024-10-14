from random import randint
print('\033[1;33m-=-\033[m' * 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('\033[1;33m-=-\033[m' * 20)
eu = soma = cont = 0
while True:
    computador = randint(0,10)
    eu = int(input('Diga um valor : '))
    result = str(input('\nPar ou Ímpar? [P/I] : ')).upper().strip()
    soma = eu + computador
    print('\033[1;33m-=-\033[m' * 20)
    if soma % 2 == 0:
        print(f'\nVoce jogou {eu} e o computador jogou {computador}. Total de {soma} Deu Par')
    else:
        print(f'\nVoce jogou {eu} e o computador jogou {computador}. Total de {soma} Deu Ímpar')
    if  soma % 2 == 0 and result == 'P':
        print('''\nVocê VENCEU!\n
Vamos jogar novamente...''')     
        print('\033[1;33m-=-\033[m' * 20)
        cont += 1
    elif soma % 2 != 0 and result == 'I':
        print('''\nVocê VENCEU!\n
Vamos jogar novamente...\n''')
        print('\033[1;33m-=-\033[m' * 20)
        cont += 1
    elif soma % 2 != 0 and result == 'P':
        print('\nVocê PERDEU!\n')
        break
    elif soma % 2 == 0 and result == 'I':
        print('\nvocê PERDEU!')
        break
print(f'GAME OVER! Você ganhou {cont} vezes.')       
print('\033[1;33m-=-\033[m' * 20)