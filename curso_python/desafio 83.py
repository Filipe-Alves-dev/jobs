lista = [str(input('Digite uma expressão para saber se ela é válida ou não : '))]
cont_1 = 0
cont_2 = 0
for r in lista:
    for c in r:
        if c == '(':
            cont_1 += 1
        if c == ')':
            cont_2 += 1
if cont_1  % 2 == 0 and cont_2 != 0  and cont_2  % 2 == 0 and cont_2 != 0 :
    print('A expressão digitada é válida!')
else:
    print('A expressão digitada não é válida!')
print(cont_1, cont_2)