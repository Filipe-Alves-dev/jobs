salario = float(input('Digite o valor do salário para saber o valor do aumento : '))
if salario > 1250:
    print(f'Aumento de 10%\nNovo salário: {(salario / 100 * 10) + salario:.0f}')
else:
    print(f'Aumento de 15%\nNovo salário: {(salario / 100 * 15) + salario:.0f}')