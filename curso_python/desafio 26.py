frase = str(input('Digite uma frase qualquer para saber quantas letras (A) possuem na frase : ')).upper().strip()
print('número de vezes que aparece a letra (A) na frase : ')
print(frase.count('A'))
print('A letra (A) aparece pela primeira vez na posição : ')
print(frase.find('A') + 1)
print('A letra (A) aparece pela ultima vez na posição : ')
print(frase.rfind('A') + 1)