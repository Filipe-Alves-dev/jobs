media = 0
maior_idade_homen = 0
nlist = ''
mulheres_menor_20 = 0
for c in range(1,5):
    print(f'\033[1;33m====================== {c}° Pessoa =========================\033[m')
    nome = str(input(f'Digite o nome da {c}° pessoa : ')).strip()
    idade = int(input(f'Digite a idade da {c}° pessoa : ') )
    sexo = str(input(f'Digite f para sexo feminino e m para masculino da {c}° pessoa :')).strip().upper()
    media += idade / 4
    if c == 1 and  sexo == 'M':
        maior_idade_homen = idade
        nlist = nome
    if sexo == 'M' and idade > maior_idade_homen:
        maior_idade_homen = idade
        nlist = nome
    if sexo == 'F' and idade < 20:
        mulheres_menor_20 += 1
print(f'A média da idade do grupo pessoas é : {media}')
print(f'O homem mais velho se chama {nlist} e tem {maior_idade_homen} anos.')
print(f'{mulheres_menor_20} Mulheres tem menos de 20 anos.')






# ilist = []
# nlist = []
# slist = []
# mlist = []
# ilist += [idade]
# nlist += [nome]
# slist += [sexo]
# if slist[0] == 'm' and slist != 'f' and ilist[0] == max(ilist):
#     print(f'{nlist[0]}')
# if slist[1] == 'm' and ilist[1] == max(ilist):
#     print(f'{nlist[1]}')
# if slist[2] == 'm' and ilist[2] == max(ilist):
#     print(f'{nlist[2]}')
# if slist[3] == 'm' and ilist[3] == max(ilist):
#     print(f'{nlist[3]}')    

