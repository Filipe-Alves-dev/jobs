from datetime import date
ano_nasc = int(input('Digite o seu ano de nascimento para saber a categoria a qual você pertence: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc
print(f'Quem nasceu em {ano_nasc} tem {idade} ano(s)')
if idade > 0 and idade <= 9:
    print('Mirim')
elif idade > 9 and idade <= 14:
    print('Infantil')
elif idade > 14 and idade <= 19:
    print('Junior')
elif idade >= 20:
    print('Sênior')
elif idade > 25:
    print('Master')
    
