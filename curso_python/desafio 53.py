frase = str(input('Digite um frase qualquer : '))
junto = frase.replace(' ','')
inversão = junto[::-1]
if junto == inversão:
    print('Essa frase é um palíndromo! ')
else:
    print('Essa frase não é um palíndromo!')