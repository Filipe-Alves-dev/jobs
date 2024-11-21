
def fatorial(n, Show = False):
    """
    -> Calcula Fatorial
    n : (int, optional): número digitado pelo usuário para o calculo de fatorial.
    Show : (bool, optional): funcão opcional que mostra o calculo que foi realizado caso esteja com valor 'True'.
    return : retorno os valores do calculo.
    """
    print('-' * 30)
    list_fat = []
    f = 1
    for c in range(n,0,-1):
        f *= c
        list_fat.append(c)
        if Show == True:
            print(c, end=' ')
            if c > 1:
                print(f'x', end=' ')
            else:
                print('=', end=' ')
    return f
    
    
#  Programa Principal   
print(fatorial(3, Show= True))
