km = float(input('Escreva a kilometragem que o carro percorreu : '))
dia = int(input('Escreva quantos dias o carro foi alugado : '))
preco_km = 0.15 * km
preco_dia = 60 * dia


print('Valor a ser pago: R${} pelo(s) kilometros rodados e R${} pelos dias alugados, totalizando o valor de : R${}'.format(preco_km, preco_dia, preco_km + preco_dia))
