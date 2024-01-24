n1 = float(input('Digite o primeiro número : '))
n2 = float(input('Digite o segundo número : '))
n3 = float(input('Digite o terceiro número : '))

if n1 > n2 and n1 > n3 and n2 < n3:
    print(f'O maior número é o {n1:.0f}\nO menor número é o {n2:.0f}')#n1 maior e n2 menor
elif n1 > n2 and n1 > n3 and n3 < n2:
    print(f'O maior número é o {n1:.0f}\nO menor número é o {n3:.0f}')#n1 maior e n3 menor
elif n2 > n1 and n2 > n3 and n1 < n3:
    print(f'O maior número é o {n2:.0f}\nO menor número é o {n1:.0f}')#n2 maior e n1 menor
elif n2 > n1 and n2 > n3 and n3 < n1:
    print(f'O maior número é o {n2:.0f}\nO menor número é o {n3:.0f}')#n2 maior e n3 menor
elif n3 > n1 and n3 > n2 and n1 < n2:
    print(f'O maior número é o {n3:.0f}\nO menor número é o {n1:.0f}')#n3 maior e n1 menor
elif n3 > n1 and n3 > n2 and n2 < n3:
    print(f'O maior número é o {n3:.0f}\nO menor número é o {n2:.0f}')#n3 maior e n2 menor
