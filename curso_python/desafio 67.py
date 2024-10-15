n = 0
while True:
    n = int(input('Quer ver a tabuada de qual valor? '))
    print (f'\033[1;33m-\033[m'* 30)
    for c in range (1,11):
      print(f'\033[1;33m{n} x {c} = {n*c}\033[m')      
    print (f'\033[1;33m-\033[m'* 30)
    if n < 0:
        break
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')