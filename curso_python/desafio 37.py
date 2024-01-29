from time import sleep
import re
print('\033[1;33m-=-\033[m' * 15)
print('Seja bem vindo a calculadora de conversão!')
print('\033[1;33m-=-\033[m' * 15)
sleep(2)
n = int(input('Digite o número desejado :'))
#numero = n.rjust(4, '0')
escolha = int(input('Digite...\n1 para conversão em número binário\n2 para conversão em número octal\n3 para conversão de número hexadecimal\n'))
binario = bin(n)[2:]
octal = oct(n)[2:]
hexa = hex(n)[2:]
if escolha == 1:
    print(f'O número que você digitou convertido para binário é : {binario}')
elif escolha == 2:
    print(f'O número que você digitou convertido para octal é : {octal}')
elif escolha == 3:
    print(f'O número que você digitou convertido para hexadecimal é : {hexa}')
else:
    print('Opção inválida. Tente novamente.')