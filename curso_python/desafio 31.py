km = float(input('Digite a distancia que o carro percorreu : '))
if km < 0:
    print('Valor inválido!')
elif km <= 200:
    print(f'O valor a ser pago considerando R$0,50 por km é R${km * 0.50}')
else:   
    print(f'O valor a ser pago considerando R$0,45 por km é R${km * 0.45}')