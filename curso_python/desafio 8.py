met = float(input('Digite o valor desejado em metros : '))
dec = met * 10
cent = met * 100
mil = met * 1000
deca = met / 10
hec = met /100
km = met / 1000

print('{:.0f} em metros corresponde a {:.0f} milímetros, {:.0f} centímetros, {:.0f} decímetros, {:.0f} decâmetros, {:.2f} Hectômetros e {:.2f} Quilômetros  .'.format(met, cent, mil, dec, deca, hec, km))
