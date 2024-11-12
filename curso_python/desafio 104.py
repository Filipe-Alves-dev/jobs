def leiaint(n):
    """
    -> Retorna se o usuário digitou um número e faz validação do mesmo.
    Args:
        n : extrai a variavel num para a função
        valor : faz o input de n
        valor_inteiro : faz a conversão do input para inteiro caso seja numerico.
    Returns:
        : retorna o número extraido.
    """
    while True:
        valor = input(n)
        if valor.isnumeric():  # Verifica se a entrada é um número
            valor_inteiro = int(valor)  # Converte para inteiro
            return valor_inteiro  # Retorna o valor assim que a conversão for bem-sucedida
        else:
            print('\033[91mERRO! Digite um número inteiro válido.\033[m')

# Chama a função e armazena o valor retornado em 'num'
num = leiaint('Digite um número: ')

# Imprime o valor obtido
print(f'Você digitou o valor {num}')
