termo = int(input("Digite quantos termos você deseja da sequência Fibonacci : "))
n1 = 0 
n2 = 1
print(f'{n1} => {n2} => ', end='')
cont = 3
while cont <= termo:
    n3 = n1 + n2
    cont += 1
    print(f'{n3} => ', end='')
    n1 = n2
    n2 = n3   
print('Fim!')
