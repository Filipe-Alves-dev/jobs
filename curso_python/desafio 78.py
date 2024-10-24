list = []
for c in range(0,5):
    list.append(int(input(f'Digite um valor para a posição {c}: ')))
pos_maior = []
pos_menor = []
print('Você digitou os valores : ', end=' ')
print(*list)
for c, r in enumerate(list):
    if r == max(list):
        pos_maior.append(c)
    if r == min(list):
        pos_menor.append(c)
print(f'O maior valor digitado é o {max(list)} nas posições ', pos_maior)
print(f'O menor valor digitado é o {min(list)} nas posições ', pos_menor)

    