
'''Interactive Help'''
# print(input.__doc__)
# help(input)
# help(print)

'''Docstrings'''
# def contador(i, f, p):
#     """_summary_

#     Args:
#         i (parametro): Inicio contagem
#         f (parametro): Fim contagem
#         p (parametro): passo sem retorno
#         :return : sem retorno
#         Função criada por Filipe Alves 
#     """
#     c = i
#     while c <= f:
#         print(f'{c}', end='..')
#         c += p
#     print('FIM') 
    
    
# help(contador)  

# '''Parametros opcionais'''
# def somar(a=0, b=0, c=0):
#     s = a+b+c
#     print(f'A soma vale {s}')
    
    
# somar(3,2,5)
# somar(8,4)
# somar()
# somar(9)
# somar(b=4, c=2)

'''Escopo de Variáreis'''
'''Variavel local e variavel Global n -> var global , x -> var local'''
# def teste():
#     x = 8
#     print(f'Na função teste, n vale {n}')
#     print(f'Na função teste, x vae {x}')
# # Programa Principal
# n = 2
# print(f'No programa principal, n vale {n}')
# teste()
# print(f'No programa principal, n vale {x}')

# '''Retorno de valores'''
# def somar(a=0,b=0,c=0):
#     s = a+b+c
#     return s
    
    
# r1 = somar(3,2,5)
# r2 = somar(2,2,)
# r3 = somar(6)
# print(f'As somas valem {r1}, {r2} e {r3}')

"""Retorno de resultado com função return"""

# def fatorial(num=1):
    # f = 1
    # for c in range(num, 0, -1):
    #     f *= c
    # return f
# n = int(input('Digite um número'))
# print(f'O fatorial de {n} é iguala a {fatorial(n)}')
# f1 = fatorial(5)
# f2 = fatorial(4)
# f3 = fatorial()
# print(f'Os resultados são {f1}, {f2} e {f3}')

# def par(n=0):
#     if n%2 == 0:
#         return True
#     else:
#         return False

# num = int(input('Digite um número: '))
# if par(num):
#     print('Esse número é par.')
# else:
#     print('Esse núemro é impar.')
    