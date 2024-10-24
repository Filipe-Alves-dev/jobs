extenso = 'ZERO','UM','DOIS','TRÊS','QUATRO','CINCO','SEIS','SETE','OITO','NOVE','DEZ','ONZE','DOZE','TREZE','QUATORZE','QUINZE','DEZESSEIS','DEZESSETE','DEZOITO','DEZENOVE','VINTE'
print('\033[1;33m=\033[m'*60)
while True:
    n = int(input('DIGITE UM NÚMERO DE 0 A 20 E LEIA ELE POR EXTENSO : '))
    print('\033[1;33m=\033[m'*60)       
    if n >=0 and n <=20:
        print(f'\nVOCÊ DIGITOU O NÚMERO {extenso[n]}\n')
        break
    print('TENTE NOVAMENTE. ', end='')
print('FIM!\n')
print('\033[1;33m=\033[m'*60)