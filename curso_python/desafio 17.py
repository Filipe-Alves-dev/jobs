from math import hypot
cato = float(input('Digite o valor do cateto oposto : '))
cata = float(input('Digite o valor do cateto adjacente : '))
hipo = hypot(cato, cata)
print('O valor da hipotenusa é : {:.2f}'.format(hipo))