from datetime import date
ano_atual = date.today().year
total_maior = 0
total_menor = 0
for c in range(1, 8):
    ano_nasc = int(input('Digite o ano de nascimento para saber se você já é maior de idade :'))
    idade = ano_atual - ano_nasc
    if idade >= 21:
        total_maior += 1
    else:
        total_menor += 1
print(f'Ao todo tivemos {total_maior} pessoas maiores de idade.')
print(f'Ao todo tivemos {total_menor} pessoas menores de idade.')