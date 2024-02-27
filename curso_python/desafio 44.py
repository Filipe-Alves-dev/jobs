from time import sleep
from emoji import emojize
print('\033[1;33m-=-\033[m' * 20 ) 
print(emojize('Seja Bem Vindo ao sistema de calculo de Produtos! :programador:', language='pt'))
print('\033[1;33m-=-\033[m' * 20 ) 
sleep(1)
valor_prod = float(input('Digite o valor do produto : R$'))
sleep(2)
metodo = str(input("""Digite o número do metodo de pagamento.\n
1 - À vista/Cheque / 10% desconto\n
2 - À vista no cartão / 5% desconto\n
3 - Em até 2x cartão de crédito\n
4 - 3x ou mais no cartão de credito / 20% juros\n:"""))
print('Calculando...')
sleep(2)
if metodo == '1':
    print(f'O valor a ser pago à vista é : R${valor_prod - (valor_prod / 100 * 10):.2f} ')
elif metodo == '2':
    print(f'O valor a ser pago no cartão à vista é : R${valor_prod - (valor_prod / 100 * 5):.2f} ')
elif metodo == '3':
    print(f'O valor a ser pago no cartão divido em 2x é : R${valor_prod} em 2x de R${valor_prod / 2} ')
elif metodo == '4':
    parcela = (int(input('Quantas parcelas ? ')))
    print(f'O valor a ser pago no cartão divido em 3x ou mais é : R${valor_prod + (valor_prod / 100 * 20)} em {parcela}x de {(valor_prod + (valor_prod / 100 * 20)) / parcela } ')
else:
    total = 0
    print('Opção inválida de pagamento, tente novamente.')
    