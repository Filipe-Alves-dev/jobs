termo = int(input('Digite o termo : '))
razão = int(input('Digite a razão : '))
decimo = termo + (10 - 1)* razão
for c in range(termo, decimo + razão,razão):
    print(c, end=' --> ')
print('FIM')