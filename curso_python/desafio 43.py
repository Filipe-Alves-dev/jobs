from emoji import emojize
from time import sleep
print('\033[1;33m-=-\033[m' * 20)
print(emojize('\033[1;36mSeja bem vindo ao programa de calculo de IMC\033[m :pessoa_levantando_peso:', language='pt'))
print('\033[1;33m-=-\033[m' * 20)
peso = float(input('Digite o seu peso : '))
altura = float(input('Digite a sua altura : '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você se encontra no estado de magreza vá a um nutricionista para avaliar seu caso.')
elif imc >= 18.5 and imc <= 24.9:
    print('Você tem um IMC dentro da classificação normal.')
elif imc >= 25 and imc <= 29.9:
    print('Você se encontra no estado de sobrepeso, tente emagrecer um pouco.')
elif imc >= 30 and imc <= 39.9:
    print('Você se encontra no estado de obesidade vá a um nutricionista par avaliar seu caso.')
elif imc >= 40:
    print('Você se encontra no estado de obesidade morbida vá a um médico nutricionista urgentemente para avaliar seu caso.')
    
    