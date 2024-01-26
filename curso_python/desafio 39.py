from time import sleep
from datetime import date
nasc = int(input('Digite o ano que você nasceu para saber se você pode se alistar...'))
ano_atual = date.today().year
idade = ano_atual - nasc
if nasc >= 2007:
    print(f'Você ainda vai se alistar faltam {18 - idade} ano(s).')
elif nasc == 2006:
    print('Já esta na hora de você se alistar!')
elif nasc <= 2005:
    print(f'Infelizmente, já passou do seu tempo de alistamento, você tem {idade - 18} ano(s) a mais que o permitido. ')
