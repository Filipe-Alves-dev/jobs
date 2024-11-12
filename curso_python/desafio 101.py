from datetime import date
ano_atual = date.today().year
print('-' * 30)

def voto(a=0):
    print(f'com {ano_atual - a} anos: ', end='')
    if a <= (ano_atual - 18)  and a > (ano_atual - 65):
        print('VOTO OBRIGÁTORIO')
    elif a < (ano_atual - 65):
        print('VOTO OPCIONAL') 
    else:
        print('NÃO VOTA')
        

ano = int(input('Em que ano você nasceu? '))
voto(ano)
