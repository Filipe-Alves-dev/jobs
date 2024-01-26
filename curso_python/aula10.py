nome = str(input('Qual é o seu nome ? '))
if nome == 'Filipe':
    print('Seu nome é bonito!')
elif nome == 'João' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Alice , Yasmin, Amanda, Thamires, Rebeca, Carla':
    print(f'Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}')
