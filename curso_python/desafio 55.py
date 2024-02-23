
pesos = []
for p in range(1, 6):
    peso = float(input(f'Digite o peso da {p}° pessoa : '))
    pesos += [peso]
print(f'O maior peso foi {max(pesos)}kg e o menor peso foi {min(pesos)}kg.')

# maior = 0
# menor = 0    
# if p == 1:
#         maior = peso
#         menor = peso
#     else:
#         if peso > maior:
#             maior = peso
#         if peso < menor:
#             menor = peso
# print(f'O maior peso lido foi de {maior}kg')
# print(f'O menor peso lido foi de {menor}kg')
