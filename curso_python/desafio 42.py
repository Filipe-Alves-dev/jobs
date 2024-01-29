import emoji
r1 = float(input('Digite o comprimento da primeira reta : '))
r2 = float(input('Digite o comprimento da segunda reta : '))
r3 = float(input('Digite o comprimento da terceira reta : '))

if r1 < (r2 + r3) and r2 < (r1 + r2) and r3 < (r1 + r2): 
    print(emoji.emojize('Com essa medidas é possivel fazer um triangulo! :marca_de_seleção_branca:', language='pt'))

    if r1 == r2 and r1 == r3:
        print('Esse triângulo é um triângulo Equilátero')
    elif r1 != r2 != r3 != r1:
        print('Esse triângulo é um triângulo Escaleno')
    else:
        print('Esse triângulo é um triângulo Isósceles')
else:
    print(emoji.emojize('Não é possivel fazer um triangulo com estas medidas! :xis:', language='pt'))