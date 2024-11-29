

def linha():
    """_summary_ função que mostra linha de 50 caracteres colorida na tela
    """
    print('\033[93m-\033[m' * 50)


def menu(e):
    while e != 3:
        linha()
        print('MENU PRINCIPAL'.center(50))
        linha()
        
        while 1 > e > 3:
            e = int(input('Sua opção: '))
            print('\033[91mErro digite uma opção válida.\033[m')
        
menu(0)    

