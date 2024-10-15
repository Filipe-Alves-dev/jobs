import math
print('\033[1;33m-=-\033[m' * 20)
print (f"{'BANCO CEV':^60}")
print('\033[1;33m-=-\033[m' * 20)
valor = 0
while True: 
    valor = int(input('DIGITE O VALOR DO SAQUE: R$'))
    cinquenta = valor / 50
    resto_cinq = valor % 50 
    valor = resto_cinq
    vinte = valor / 20
    resto_vinte = valor % 20
    valor = resto_vinte
    dez = valor / 10
    resto_dez = dez % 10
    valor = resto_dez
    um = valor * 10
    valor = valor - um
    if valor <= 0:
        break
print('\033[1;33m-=-\033[m' * 20)
print(f'''\n\033[1;33mTOTAL DE {math.floor(cinquenta):.0f} CÉDULAS DE R$50\n
TOTAL DE {math.floor(vinte):.0f} CÉDULAS DE R$20\n
TOTAL DE {math.floor(dez):.0f} CÉDULAS DE R$10\n
TOTAL DE {um:.0f} CÉDULAS DE R$1\033[m''')
print('\033[1;33m-=-\033[m' * 20)
 