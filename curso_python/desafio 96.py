def area(l , c):
    s =  l * c
    print(f'A  área de um terreno {l}x{c} é de {s}m².')
    
print('<< Controle de Terrenos >>')
print('-'*30)

area(l = float(input('LARGURA (m): ')),
     c = float(input('COMPRIMENTO (m): ')))