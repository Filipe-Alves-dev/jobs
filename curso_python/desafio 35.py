import emoji
r1 = float(input('Digite o comprimento da primeira reta : '))
r2 = float(input('Digite o comprimento da segunda reta : '))
r3 = float(input('Digite o comprimento da terceira reta : '))
if r1 > (r2 + r3):
    print(emoji.emojize('Não é possivel fazer um triangulo com estas medidas! :xis:', language='pt'))
elif r2 > (r1 + r3):
    print(emoji.emojize('Não é possivel fazer um triangulo com estas medidas! :xis:', language='pt'))
elif r3 > (r1 + r2):
    print(emoji.emojize('Não é possivel fazer um triangulo com estas medidas! :xis:', language='pt'))
else:
    print(emoji.emojize('Com essa medidas é possivel fazer um triangulo! :marca_de_seleção_branca:', language='pt'))

    