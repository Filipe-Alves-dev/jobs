from time import sleep


def linha():
    print('-=-' * 15)
    
    
def mostra_contagem():  
    linha()
    print('Contagem de 1 até 10 de 1 em 1')
    for c in range(1,11,1):
        print(c , end=' ')
        sleep(0.2)
    print('FIM!')
    linha()
    print('Contagem de 10 até 0 de 2 em 2')
    for c in range(10,-1,-1):
        print(c, end=' ') 
        sleep(0.2) 
    print('FIM!')
    linha()
    print('Agora é sua vez de personalizar a contagem!')
        
    
def contador(i, f, p):
    linha()
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i < f:
        for c in range(i, f +1, p):
            print(c, end=' ')
            sleep(0.2)
        print('FIM!')
    elif i > f:
        p = - p
        for c in range(i, f -1, p):
            print(c, end=' ')
            sleep(0.2)        
        print('FIM')
        
        
mostra_contagem()
contador( i = int(input('Inicio: ')),
          f = int(input('Fim:    ')),
          p = int(input('Passo:  ')))