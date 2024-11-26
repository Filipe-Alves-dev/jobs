def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',','.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[91mERRO: \"{entrada}\" Preço inválido\033[m')
        else:
            válido = True
            return float(entrada)

        