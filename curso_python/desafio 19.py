from random import choice
n1 = input('Digite o primeiro nome : ')
n2 = input('Digite o segundo nome : ')
n3 = input('Digite o terceiro nome : ')
n4 = input('Digite o quarto nome : ')
nomes = [n1, n2, n3, n4]
n = choice(nomes)
print('O aluno escolhido para apagar o quadro foi : {}.'.format(n))
