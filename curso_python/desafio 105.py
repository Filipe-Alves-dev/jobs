
def notas(* n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :parametro n: uma ou mais notas e situações de vários alunos.
    :parametro sit: (bool, optional): indicando se deve ou não adicionar uma situação. 
    :Returns: dicionário com várias informações sobre notas dos alunos e situação.
        
    """
    list_notas = n
    dict_notas = {}
    soma = 0
    for s in list_notas:
        soma += s 
    dict_notas['total'] = len(n)
    dict_notas['maior'] = max(list_notas)
    dict_notas['menor'] = min(list_notas)
    dict_notas['media'] = float(f'{soma / len(n):.1f}')
    if sit == True:
        if dict_notas['media'] >= 7:
            dict_notas['situação'] = 'BOA'
        elif dict_notas['media'] < 7 and dict_notas['media'] > 6:
            dict_notas['situação'] = 'RAZOAVEL'
        else:
            dict_notas['situação'] = 'RUIM'
    return dict_notas


# Programa Principal    
print('-' * 50)
resp = notas(3.5,10,6.5,2,1,7, sit= True)
print(resp)
help(notas)