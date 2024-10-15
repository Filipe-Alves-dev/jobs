# Tuplas são imutáveis
lanche = ('Hambúrguer', 'Suco', 'Pizza', 'Pudim')
for comida in lanche:
    print(f'Eu vou comer {comida}')
print('Comi pra caramba!')
print(len(lanche))
for comida in range(0, len(lanche)):
    print(lanche[comida])
for pos, comida in enumerate (lanche):
    print(f'Eu vou comer {comida} na posição {pos}')
print(sorted(lanche))
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(sorted(c))
print(len(c))
print(c.count(9))
print(c.index(8))
pessoa = ('Filipe', 23, 'M', 72.00)
del(pessoa)
print(pessoa)

