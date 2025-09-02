
nome = input('Digite o seu nome : ')
idade = int(input('Digite a sua idade : '))
altura = float(input('Digite a sua altura : '))

if idade >= 18 :
    print('Você é maior de idade!')
else: 
    print('Você ainda é menor de idade!')

print (f'A variavel nome é do tipo :{type(nome)}')
print (f'A variavel idade é do tipo : {type(idade)}')
print (f'A variavel altura é do tipo : {type(altura)}')