

def voto(a=0):
    from datetime import date
    ano_atual = date.today().year
    idade =  ano_atual - a
    print(f'com {idade} anos: ', end='')
    if idade >= 18  and idade < 65:
        print('VOTO OBRIGÁTORIO')
    elif 16 <= idade < 18 or idade >= 65:
        print('VOTO OPCIONAL') 
    else:
        print('NÃO VOTA')
        
# Programa Principal     
print('-' * 30)
ano = voto(int(input('Em que ano você nasceu? ')))

