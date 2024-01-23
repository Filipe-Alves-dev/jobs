#analise de texto

frase = 'Curso em vídeo Python'
print(frase.count('o')) 
print(frase.upper().count('O'))
print(len(frase.strip()))
print(frase.replace('Python', 'Android'))
print(frase[0])
print('Curso' in frase)
print(frase.find('vídeo'))
print(frase.lower().find('vídeo'))
dividido = frase.split()
print(dividido)
junto = frase.strip()
print(junto)
print(dividido [0])
print(junto[5])
print(dividido[2][3])
