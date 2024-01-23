nome = str(input(' Digite o nome completo da pessoa para saber o seu primeiro e ultimo nome : ')).strip()
dividido = nome.split()
print(f'O primeiro nome da pessoa é : {dividido[0]}')
print(f'O ultimo nome da pessoa é : {dividido[-1]}')

