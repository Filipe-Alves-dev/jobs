from time import sleep
print('\033[1;033m-=-\033[m' * 20)
print('\033[1;033m                   Programa de cálculos\033[m')
print('\033[1;033m-=-\033[m' * 20)
n1 = int(input('Digite o primeiro valor : '))
n2 = int(input('Digite o segundo valor : '))
escolha = ''
while escolha != 5:
    escolha = int(input('''\n\033[01;036mMenu de calculo\033[m\n
[1] SOMAR\n
[2] MULTIPLICAR\n
[3] MAIOR\n
[4] NOVOS NÚMEROS\n
[5] SAIR DO PROGRAMA\n
: '''))
    if escolha == 1:     
        soma = n1 + n2
        print(f'A soma dos números {n1} e {n2} é {soma}!')       
    if escolha == 2:
        mult = n1 * n2
        print (f'A multiplicação entre os números {n1} e {n2} é {mult}: ')
    if escolha == 3:
        maior = [n1, n2]
        print(f'O maior número entre {n1} e {n2} é o : {max(maior)}')
    if escolha == 4:
        n1 = int(input('Digite o primeiro valor : '))
        n2 = int(input('Digite o segundo valor : '))
    if escolha == 5:
        print ('\033[01;033mSaindo do programa...\033[m')
        sleep(2)
        print('\033[01;032mConcluido!\033[m')
        