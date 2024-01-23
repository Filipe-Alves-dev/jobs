cidade = str(input('Digite o nome da sua cidade para saber se o nome começa com a palavra Santo : ')).strip()
cidade = cidade.upper()
dividido = cidade.split()
santo = dividido[0]
print('SANTO' in santo)
