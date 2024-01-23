nome = str(input('Escreva seu nome completo : '))
('Analisando seu nome ...')
print(f'seu nome em maiúsculas é {nome.upper()}')
print(f'Seu nome em minúsculas é {nome.lower()}')
n1 = nome.replace(' ', '')
print(f'Seu nome ao todo tem {len(n1)} letras')
n2 = nome.split()
print(f'Seu primeiro nome tem {len(n2[0])} letras')


