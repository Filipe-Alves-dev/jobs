

def fatorial(n):
    """_summary_

    Parametro n : Recebe o número em que deve ser feito o calculo do fatorial.
    Parametro return : Retorna a reposta do fatorial de n pela função.
        
    """
    f = 1
    for c in range(1 , n+1):
        f *= c
    return f

    
num = int(input('Digite um número para saber o seu fatorial:'))
fat = fatorial(num)
print(f'O fatorial de {num} é {fat}')