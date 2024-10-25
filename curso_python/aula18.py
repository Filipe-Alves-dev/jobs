# dados = list()
# dados.append('Pedro')
# dados.append(25)
# print(dados[0])
# print(dados[1])
# pessoas = list()
# pessoas.append(dados[:]) #  copia da lista dados
# print(pessoas[0][0]) # indice 0 da lista na posicao 0
# print(pessoas[1][1]) # indice 1 da lista na posicao 1
# print(pessoas[2][0]) # indice 2 da lista na posicao 0
# print(pessoas[1]) # indice 1 da lista 

# teste = list()
# teste.append('Gustavo')
# teste.append(40)
# galera = list()
# galera.append(teste[:]) # com essa função a lista galera recebe a lista teste, e continua adicionando
# teste[0] = 'Maria'
# teste[1] = 22
# galera.append(teste)
# print(galera)
# galera = [['João' , 19], ['Joaquim', 13], ['Ana' ,33], ['Maria', 45]]
# print(galera[0][0])
# print(galera[3])
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade. ')
galera = list()
dado =  list()
totmaior = totmenor = 0
for c in range(0, 3):
    dado.append(str(input('Digite o nome : ')))
    dado.append(int(input('Digite a idade : ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor += 1
print(f'Total de {totmaior} maiores e {totmenor} menores de idade.')