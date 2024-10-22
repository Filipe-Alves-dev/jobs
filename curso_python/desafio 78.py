list = [int(input('Digite um valor para a posição 0 : ')),
            int(input('Digite um valor para a posição 1 : ')),
            int(input('Digite um valor para a posição 2 : ')), 
            int(input('Digite um valor para a posição 3 : ')),
            int(input('Digite um valor para a posição 4 : '))] 
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

    