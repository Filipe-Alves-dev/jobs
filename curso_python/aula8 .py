# Condições 
# if : se
# else : senão 


#tempo = int(input('Quantos anos tem seu carro? '))
#if tempo <= 3:
#    print('Carro novo')
#else:
#    print('carro velho')
#print('--FIM--')

#nome = str(input('Qual é o seu nome ? '))
#if nome == 'Filipe':
#    print('Você é lindo! ')
#else:
#    print('Seu nome é tão normal!')
#print(f'Bom dia {nome}!')

n1 = float(input('Digite a primeira nota :'))
n2 = float(input('Digite o segunda nota :'))
media = (n1 + n2) / 2
print(f'A sua média foi {media:.1f}')
if media >= 7:
    print('Parabéns você passou de ano!')
else:
    print('Infelizmente você ficou de recuperação.')
