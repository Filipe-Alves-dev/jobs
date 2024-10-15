print('\033[1;33m-=-\033[m' * 20)
print (f"{'LOJA SUPER BARATÃO':^60}")
print('\033[1;33m-=-\033[m' * 20)
n_prod = preço = total = prod_plusmil = 0
list_prod_barato = []
while True:
    n_prod = str(input('DIGITE O NOME DO PRODUTO: ')).upper().strip()
    preço = float(input('DIGITE O VALOR DO PRODUTO: R$'))
    total += preço 
    list_prod_barato += [preço]
    if preço <= min(list_prod_barato):
        list_nome_prod_barato = n_prod
    if preço > 1000:
        prod_plusmil += 1
    escolha = ''
    while escolha != 'S' and escolha != 'N':
        escolha = str(input('QUER CONTINUAR? [S/N] : ')).upper().strip()
    if escolha == 'N':
        break
print('\033[1;33m-=-\033[m' * 20)
print(f'''\nTOTAL DA COMPRA FOI \033[1;33mR${total:.2f}\033[m\n
TEMOS \033[1;33m{prod_plusmil}\033[m PRODUTOS ACIMA DE \033[1;33mR$1000.00\033[m\n
O PRODUTO MAIS BARATO FOI \033[1;33m{list_nome_prod_barato}\033[m QUE CUSTA \033[1;33mR${min(list_prod_barato)}\033[m''')
print('\033[1;33m-=-\033[m' * 20)
