sexo = ''
while sexo != 'F' and sexo != 'M':
    sexo = str(input('Digite o seu sexo, M para masculino e F para feminino : ')).upper()
    print('Valor incorreto, por favor Digite M para masculino e F para feminino:')
if sexo == 'F':
    print('Você é do sexo Feminino!')
else:
    print('Você é do sexo Masculino!')    