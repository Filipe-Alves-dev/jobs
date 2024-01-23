#tipos primitivos

## int / 7, -4, 0, 9875
## float / 4.5, 0.0.76, -15.223. 7.0
## bool / True False
## str / 'Olá' , '7.5' ; ''


num = input('Digite o número : ')
print (type(num))

n1 = int(input('Digite o primeiro número : '))
n2 = int(input('Digite o segundo número : '))
s= n1 + n2
print('A soma entre {} e {} vale {}'.format(n1, n2, s))