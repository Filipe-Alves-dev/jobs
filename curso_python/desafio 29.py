vel = int(input('Digite a velocidade que o veiculo estava quando passou pelo radar :'))
if vel < 0:
    print('Velocidade inválida!')
elif vel <= 80:
    print('O carro estava dentro da velocidade permitida.')
else:
    print(f'O carro ultrapassou o limite de velocidade de 80km e receberá multa.\nVelocidade que o carro passou {vel}km\nValor da multa a ser aplicada ao veiculo : R${(vel - 80) * 7}!')