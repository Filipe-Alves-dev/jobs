n1 = int(input('Digite o primeiro número : '))
n2 = int(input('Digite o segundo número : '))
if n1 > n2:
    print(f'O número {n1} é maior que o número {n2}!')
elif n2 > n1:
    print(f'O número {n2} é maior que o número {n1}!')
else:
    print(f'Não existe valor maior, os dois são iguais!')
