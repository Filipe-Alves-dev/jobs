from time import sleep
from emoji import emojize
print('\033[1;33m-=-\033[m' * 22)
print(emojize('Olá seja bem vindo ao sistema simulador de parcelas SSP!! :programador:', language='pt'))
print('\033[1;33m-=-\033[m' * 22)
sleep(2)
casa = float(input('Digite o valor da casa desejada : R$'))
salario = float(input('Digite o valor do seu salário : R$'))
ano = int(input('Digite em quantos anos deseja parcelar o imovel :'))
parcela_casa = casa / (ano * 12) 
if salario / 100 * 30 >= parcela_casa:
    print(emojize(f'Para financiar este imóvel no valor de R${casa} em {ano} ano(s) o valor da prestação é de {parcela_casa:.2f}.\nMeus parabéns! Você esta apto a financiar seu imóvel!!! :marca_de_seleção_branca:' , language='pt'))
else:
    print(emojize(f'Infelizmente o valor da sua renda não cumpre os requisitos para o financiamento desse imóvel, para financiar uma casa de R${casa} em {ano} ano(s) a prestação será de R${parcela_casa:.2f}\nImpréstimo NEGADO. :xis:', language='pt'))

