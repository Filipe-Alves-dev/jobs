from time import sleep


def linha():
    print('\033[1;33m-=-\033[m' * 15)
    
    
def mostra_contagem():  
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1,11,1):
        print(c , end=' ')
        sleep(0.1)
    print('FIM!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10,-1,-2):
        print(c, end=' ') 
        sleep(0.1) 
    print('FIM!')
    linha()
   
        
    
def contador(i, f, p):
    linha() 
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
        print(f'Contagem de {i} até {f} de {p} em {p}') 
    else:
        print(f'Contagem de {i} até {f} de {p} em {p}') 
    if i < f:
        for c in range(i, f +1, p):
            print(c, end=' ')
            sleep(0.1)
    elif i > f and p > 0:
        p = -p
        for c in range(i, f -1, p):
            print(c, end=' ')
            sleep(0.1)
    elif p < 0:
        p = +p
        for c in range(i, f -1, p):
            print(c, end=' ')
            sleep(0.1)
    print('FIM!')
      
    
    
mostra_contagem()

print('Agora é sua vez de personalizar a contagem!')

contador( i = int(input('Inicio: ')),
          f = int(input('Fim:    ')),
          p = int(input('Passo:  ')))