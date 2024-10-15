cont_idade = cont_sexo_masc = cont_mulher_menor20 = 0
while True:
    idade = sexo = escolha = 0
    print('\033[1;33m-=-\033[m' * 20)
    print('CADASTRE UMA PESSOA')
    print('\033[1;33m-=-\033[m' * 20)
    idade = int(input('IDADE: '))
    if idade >= 18:
        cont_idade += 1
    while sexo != 'M' and sexo != 'F':
        sexo = str(input('\nSEXO F/M : ')).upper().strip()
        if sexo == 'M':
            cont_sexo_masc += 1
        if sexo == 'F' and idade < 20:
            cont_mulher_menor20 += 1
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('\nCONTINUAR S/N : ')).upper().strip()
    if escolha == 'N':
        break
print('\033[1;33m-=-\033[m' * 20)
print(f'\nTotal de pessoas maiores de 18 anos cadastrados: {cont_idade} \nTotal de homens cadastrados: {cont_sexo_masc}\nTotal de mulheres com menos de 20 anos: {cont_mulher_menor20}\n')
print('\033[1;33m-=-\033[m' * 20)